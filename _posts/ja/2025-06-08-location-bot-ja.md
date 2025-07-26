---
audio: false
generated: false
image: false
lang: ja
layout: post
title: テレグラム位置ボットでパンチカードを自動化する
translated: true
---

毎日の「出勤カード」が面倒だと思いませんか？ 私もそう思いました。 そのため、私は位置情報追跡を使用してオフィス到着通知を自動化し、重要なチェックインを思い出させてくれる個人用Telegramボットを構築しました。 この投稿では、PythonとGitHub Actionsを組み合わせて、位置情報に基づいて必要なときに通知を受け取る、シームレスでハンズフリーなシステムを作成した方法を掘り下げます。

```yml
name: Hourly Location Check

on:
  schedule:
    # 毎日、11時から23時まで、1時間ごとに、平日（月曜日～金曜日）に実行
    # 時間はUTCです。 シンガポール時間（SGT）はUTC+8です。
    # 11時 SGTは03:00 UTC、23時 SGTは15:00 UTCです。
    # したがって、03:00から15:00 UTCの間にスケジュールを設定する必要があります。
    - cron: '0 3-15 * * 1-5'

    # ライブ位置情報の共有を開始するリマインダー：水曜日 11時 SGT（3時 UTC）
    # 現在の時間：2025年6月8日 17:10:58 +08 (SGT)
    # 水曜日 11時 SGT（UTC+8）：11 - 8 = 3時 UTC。
    - cron: '0 3 * * 3' # 3は水曜日

    # ライブ位置情報の共有を停止するリマインダー：金曜日 23時 SGT（15時 UTC）
    # 現在の時間：2025年6月8日 17:10:58 +08 (SGT)
    # 金曜日 23時 SGT（UTC+8）：23 - 8 = 15時 UTC。
    - cron: '0 15 * * 5' # 5は金曜日

  workflow_dispatch:  # ワークフローの手動トリガーを許可
  push:
    branches: ["main"]
    paths:
      - 'scripts/release/location_bot.py' # スクリプトへの修正されたパス
      - '.github/workflows/location.yml' # このワークフローファイルへのパス

concurrency:
  group: 'location'
  cancel-in-progress: false

jobs:
  check_and_notify:
    runs-on: ubuntu-latest
    env:
      TELEGRAM_LOCATION_BOT_API_KEY: ${{ secrets.TELEGRAM_LOCATION_BOT_API_KEY }}

    steps:
    - name: リポジトリのチェックアウト
      uses: actions/checkout@v4
      with:
        fetch-depth: 5 # 効率化のため、最後の5つのコミットのみを取得

    - name: Python 3.13.2の設定
      uses: actions/setup-python@v4
      with:
        python-version: "3.13.2" # 正確なPythonバージョンを指定

    - name: 依存関係のインストール
      run: |
        python -m pip install --upgrade pip
        # リポジトリのルートにrequirements.simple.txtがあると仮定しています。
        # ない場合は: pip install requests python-dotenv
        pip install -r requirements.simple.txt

    - name: 位置情報チェックスクリプトの実行（スケジュール）
      run: python scripts/release/location_bot.py --job check_location
      # このステップは、1時間ごとのチェックのためのスケジュールトリガーで実行されます
      if: github.event.schedule == '0 3-15 * * 1-5' # 1時間ごとのcronスケジュールに一致

    - name: ライブ位置情報の共有を開始するリマインダー
      run: python scripts/release/location_bot.py --job start_sharing_message
      if: github.event.schedule == '0 3 * * 3' # 水曜日 11時 SGT cronに一致

    - name: ライブ位置情報の共有を停止するリマインダー
      run: python scripts/release/location_bot.py --job stop_sharing_message
      if: github.event.schedule == '0 15 * * 5' # 金曜日 23時 SGT cronに一致

    - name: テストメッセージ用のTelegramスクリプトの実行（手動トリガー）
      run: python scripts/release/location_bot.py --job send_message --message "これはGitHub Actionsからの手動トリガーテストメッセージです。"
      if: github.event_name == 'workflow_dispatch'

    - name: mainブランチへのプッシュ用のTelegramスクリプトの実行
      run: python scripts/release/location_bot.py --job send_message --message "位置情報ボットのコード変更がmainブランチにプッシュされました。"
      if: github.event_name == 'push'
```

```python
import os
import requests
from dotenv import load_dotenv
import json
import subprocess
import argparse
import math
import time # 将来の連続モニタリングのため

load_dotenv()

# 新しい位置情報ボット用の特定のAPIキー
TELEGRAM_LOCATION_BOT_API_KEY = os.environ.get("TELEGRAM_LOCATION_BOT_API_KEY") # .envに設定されていることを確認
TELEGRAM_CHAT_ID = "610574272" # 通知メッセージを送信するためのこのチャットID

# オフィスの座標を定義
OFFICE_LATITUDE = 23.135368
OFFICE_LONGITUDE = 113.32952

# 近接半径（メートル）
PROXIMITY_RADIUS_METERS = 300

def send_telegram_message(bot_token, chat_id, message):
    """Telegram Bot APIを使用してTelegramチャットにメッセージを送信します。"""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown" # メッセージ内の太字テキスト用にMarkdownを使用
    }
    response = requests.post(url, params=params)
    if response.status_code != 200:
        print(f"Telegramメッセージの送信エラー: {response.status_code} - {response.text}")

def get_latest_location(bot_token):
    """ボットから最新のライブ位置情報更新を取得します。"""
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    # 最後の処理されたもの以降の新しい更新のみを取得するためのオフセット
    # 単一実行スクリプトの場合は、最新のものを取得しますが、ポーリングの場合はオフセットを管理します。
    params = {"offset": -1} # 最後の更新を取得
    response = requests.get(url, params=params)
    print("GetUpdates Response:", response) # デバッグ
    if response.status_code == 200:
        updates = response.json()
        print("GetUpdates JSON:", json.dumps(updates, indent=4)) # デバッグ
        if updates['result']:
            last_update = updates['result'][-1]
            # ライブ位置情報のためにedited_messageを優先
            if 'edited_message' in last_update and 'location' in last_update['edited_message']:
                return last_update['edited_message']['location'], last_update['edited_message']['chat']['id']
            elif 'message' in last_update and 'location' in last_update['message']:
                # 初期ライブ位置情報メッセージまたは静的位置情報共有を処理
                return last_update['message']['location'], last_update['message']['chat']['id']
    return None, None

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    ハバーサインの公式を使用して、地球上の2点間の距離を計算します。
    メートル単位の距離を返します。
    """
    R = 6371000  # 地球の半径（メートル）

    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad

    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c
    return distance

def main():
    parser = argparse.ArgumentParser(description="Telegram Bot Script")
    # --job引数の更新された選択肢
    parser.add_argument('--job', choices=['get_chat_id', 'send_message', 'check_location', 'start_sharing_message', 'stop_sharing_message'], required=True, help="実行するジョブ")
    # 'send_message'ジョブ用の--message引数を追加
    parser.add_argument('--message', type=str, help="'send_message'ジョブのメッセージ")
    # 'check_location'ジョブ用の--test引数を追加
    parser.add_argument('--test', action='store_true', help="'check_location'ジョブの場合、近接に関係なくメッセージを強制送信します。")
    args = parser.parse_args()

    if args.job == 'get_chat_id':
        bot_token = TELEGRAM_LOCATION_BOT_API_KEY
        url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
        response = requests.get(url)
        if response.status_code == 200:
            updates = response.json()
            print(json.dumps(updates, indent=4))
            if updates['result']:
                last_update = updates['result'][-1]
                chat_id = None
                if 'message' in last_update and 'chat' in last_update['message']:
                    chat_id = last_update['message']['chat']['id']
                elif 'edited_message' in last_update and 'chat' in last_update['edited_message']:
                    chat_id = last_update['edited_message']['chat']['id']
                elif 'channel_post' in last_update and 'chat' in last_update['channel_post']:
                    chat_id = last_update['channel_post']['chat']['id']
                elif 'edited_channel_post' in last_update and 'chat' in last_update['edited_channel_post']:
                    chat_id = last_update['edited_channel_post']['chat']['id']

                if chat_id:
                    print(f"チャットID: {chat_id}")
                else:
                    print("最後の更新からチャットIDを取得できませんでした。")
            else:
                print("更新が見つかりません。")
        else:
            print(f"更新の取得エラー: {response.status_code} - {response.text}")

    elif args.job == 'send_message':
        if TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = args.message if args.message else "これはTelegramボットスクリプトからのデフォルトテストメッセージです！"
            send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print(f"メッセージが正常に送信されました: {message}")
        else:
            print("TELEGRAM_LOCATION_BOT_API_KEYとTELEGRAM_CHAT_IDが設定されていません。")

    elif args.job == 'start_sharing_message':
        if TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = "⚠️ *リマインダー:* ボットにライブ位置情報を共有してください！"
            send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print("共有開始リマインダーが送信されました。")
        else:
            print("TELEGRAM_LOCATION_BOT_API_KEYとTELEGRAM_CHAT_IDが設定されていません。")

    elif args.job == 'stop_sharing_message':
        if TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = "✅ *リマインダー:* 今、ライブ位置情報の共有を停止できます。"
            send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print("共有停止リマインダーが送信されました。")
        else:
            print("TELEGRAM_LOCATION_BOT_API_KEYとTELEGRAM_CHAT_IDが設定されていません。")

    elif args.job == 'check_location':
        if not TELEGRAM_LOCATION_BOT_API_KEY or not TELEGRAM_CHAT_ID:
            print("位置情報チェックにはTELEGRAM_LOCATION_BOT_API_KEYとTELEGRAM_CHAT_IDを設定する必要があります。")
            return

        user_location, location_chat_id = get_latest_location(TELEGRAM_LOCATION_BOT_API_KEY)

        if user_location:
            current_latitude = user_location['latitude']
            current_longitude = user_location['longitude']

            distance = haversine_distance(
                OFFICE_LATITUDE, OFFICE_LONGITUDE,
                current_latitude, current_longitude
            )

            print(f"現在の位置: ({current_latitude}, {current_longitude})")
            print(f"オフィスまでの距離: {distance:.2f} メートル")

            needs_punch_card = distance <= PROXIMITY_RADIUS_METERS

            if needs_punch_card:
                print(f"あなたはオフィスから {PROXIMITY_RADIUS_METERS}メートル以内にいます！")
                notification_message = (
                    f"🎉 *オフィス到着!* 🎉\n"
                    f"WeComで出勤カードを打つ時間です。\n"
                    f"現在のオフィスからの距離: {distance:.2f}m."
                )
            else:
                print(f"あなたは {PROXIMITY_RADIUS_METERS}メートルのオフィス円の外にいます。")
                # 半径外のメッセージ
                notification_message = (
                    f"📍 あなたはオフィスの近接範囲外です（{PROXIMITY_RADIUS_METERS}m）。\n"
                    f"現在のオフィスからの距離: {distance:.2f}m."
                )

            # 近接内であるか、または--testフラグが使用されている場合はメッセージを送信
            if needs_punch_card or args.test:
                send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, notification_message)
            else:
                # 近接外であり、テストモードでない場合はコンソールに出力（Telegramメッセージなし）
                print("近接外であり、テストモードでないため、Telegramにメッセージは送信されません。")
        else:
            print("最新の位置情報を取得できませんでした。ボットにライブ位置情報を共有していることを確認してください。")

if __name__ == '__main__':
    main()
```

---

更新：これは良くないです。ボットにライブ位置情報を共有する必要があるからです。