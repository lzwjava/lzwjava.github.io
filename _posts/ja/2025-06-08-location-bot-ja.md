---
audio: false
generated: false
lang: ja
layout: post
title: テレグラム位置ボットでパンチカードを自動化
translated: true
---

毎日の「出勤打刻」がもっと楽にならないかなと思ったことはありませんか？私は確かに思いました。そこで、位置情報追跡を利用してオフィス到着通知を自動化し、重要なチェックインをリマインドする個人用Telegramボットを作りました。この記事では、PythonとGitHub Actionsを組み合わせて、位置情報に基づいて必要なタイミングで通知を受け取れる、手間のかからないシームレスなシステムを構築した方法を紹介します。

```yml
name: 毎時位置確認

on:
  schedule:
    # 平日（月曜日～金曜日）の11時から23時まで毎時0分に実行
    # 時間はUTCです。シンガポール時間（SGT）はUTC+8です。
    # つまり、11時SGTは03:00 UTC、23時SGTは15:00 UTCです。
    # したがって、03:00から15:00 UTCの間でスケジュールします。
    - cron: '0 3-15 * * 1-5'

    # ライブ位置情報の共有開始リマインダー: 水曜日11時SGT（3時UTC）
    # 現在時刻: 2025年6月8日（日）午後5:10:58 +08（SGT）
    # 水曜日11時SGT（UTC+8）の場合: 11 - 8 = 3時UTC。
    - cron: '0 3 * * 3' # 3は水曜日

    # ライブ位置情報の共有停止リマインダー: 金曜日23時SGT（15時UTC）
    # 現在時刻: 2025年6月8日（日）午後5:10:58 +08（SGT）
    # 金曜日23時SGT（UTC+8）の場合: 23 - 8 = 15時UTC。
    - cron: '0 15 * * 5' # 5は金曜日

  workflow_dispatch:  # ワークフローの手動トリガーを許可
  push:
    branches: ["main"]
    paths:
      - 'scripts/release/location_bot.py' # スクリプトへの正しいパス
      - '.github/workflows/location.yml' # このワークフローファイルのパス

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
        fetch-depth: 5 # 効率化のため直近5コミットのみ取得

    - name: Python 3.13.2のセットアップ
      uses: actions/setup-python@v4
      with:
        python-version: "3.13.2" # 特定のPythonバージョンを指定

    - name: 依存関係のインストール
      run: |
        python -m pip install --upgrade pip
        # リポジトリルートにrequirements.simple.txtがあると仮定
        # ない場合は: pip install requests python-dotenv
        pip install -r requirements.simple.txt 

    - name: 位置確認スクリプトの実行（スケジュール時）
      run: python scripts/release/location_bot.py --job check_location
      # このステップは毎時cronスケジュール時に実行
      if: github.event.schedule == '0 3-15 * * 1-5' # 毎時cronスケジュールに一致

    - name: ライブ位置情報共有開始リマインダー
      run: python scripts/release/location_bot.py --job start_sharing_message
      if: github.event.schedule == '0 3 * * 3' # 水曜日11時SGTのcronに一致

    - name: ライブ位置情報共有停止リマインダー
      run: python scripts/release/location_bot.py --job stop_sharing_message
      if: github.event.schedule == '0 15 * * 5' # 金曜日23時SGTのcronに一致

    - name: テストメッセージ用Telegramスクリプト実行（手動トリガー時）
      run: python scripts/release/location_bot.py --job send_message --message "これはGitHub Actionsからの手動トリガーテストメッセージです"
      if: github.event_name == 'workflow_dispatch'

    - name: mainブランチへのプッシュ時Telegramスクリプト実行
      run: python scripts/release/location_bot.py --job send_message --message "位置情報ボットのコード変更がmainブランチにプッシュされました"
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
import time # 将来の継続的モニタリング用

load_dotenv()

# 新規: 位置情報ボット用の特定APIキー
TELEGRAM_LOCATION_BOT_API_KEY = os.environ.get("TELEGRAM_LOCATION_BOT_API_KEY") # .envで設定を確認
TELEGRAM_CHAT_ID = "610574272" # 通知メッセージ送信用のチャットID

# オフィス座標を定義
OFFICE_LATITUDE = 23.135368
OFFICE_LONGITUDE = 113.32952

# 近接半径（メートル）
PROXIMITY_RADIUS_METERS = 300

def send_telegram_message(bot_token, chat_id, message):
    """Telegram Bot APIを使用してチャットにメッセージを送信"""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown" # メッセージの太字にMarkdownを使用
    }
    response = requests.post(url, params=params)
    if response.status_code != 200:
        print(f"Telegramメッセージ送信エラー: {response.status_code} - {response.text}")

def get_latest_location(bot_token):
    """ボットから最新のライブ位置情報更新を取得"""
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    # 最後に処理した更新以降の新しい更新のみ取得（継続的ポーリング用）
    # 単発実行スクリプトでは最新のみ取得、ポーリングの場合はオフセット管理が必要
    params = {"offset": -1} # 最後の更新を取得
    response = requests.get(url, params=params)
    print("GetUpdates レスポンス:", response) # デバッグ用
    if response.status_code == 200:
        updates = response.json()
        print("GetUpdates JSON:", json.dumps(updates, indent=4)) # デバッグ用
        if updates['result']:
            last_update = updates['result'][-1]
            # ライブ位置情報にはedited_messageを優先
            if 'edited_message' in last_update and 'location' in last_update['edited_message']:
                return last_update['edited_message']['location'], last_update['edited_message']['chat']['id']
            elif 'message' in last_update and 'location' in last_update['message']:
                # 初期ライブ位置情報メッセージまたは静的位置情報共有を処理
                return last_update['message']['location'], last_update['message']['chat']['id']
    return None, None

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    ハーバーサイン公式を使用して地球上の2点間の距離を計算
    メートル単位で距離を返す
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
    parser = argparse.ArgumentParser(description="Telegramボットスクリプト")
    # --job引数の選択肢を更新
    parser.add_argument('--job', choices=['get_chat_id', 'send_message', 'check_location', 'start_sharing_message', 'stop_sharing_message'], required=True, help="実行するジョブ")
    # 'send_message'ジョブ用に--message引数を追加
    parser.add_argument('--message', type=str, help="'send_message'ジョブで送信するメッセージ")
    # 'check_location'ジョブ用に--test引数を追加
    parser.add_argument('--test', action='store_true', help="'check_location'ジョブで、近接に関係なくメッセージを強制送信")
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
                print("更新が見つかりませんでした。")
        else:
            print(f"更新取得エラー: {response.status_code} - {response.text}")

    elif args.job == 'send_message':
        if TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = args.message if args.message else "これはTelegramボットスクリプトからのデフォルトテストメッセージです！"
            send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print(f"メッセージ送信成功: {message}")
        else:
            print("TELEGRAM_LOCATION_BOT_API_KEYとTELEGRAM_CHAT_IDが設定されていません。")

    elif args.job == 'start_sharing_message':
        if TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = "⚠️ *リマインダー:* ボットにライブ位置情報の共有を開始してください！"
            send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print("共有開始リマインダーを送信しました。")
        else:
            print("TELEGRAM_LOCATION_BOT_API_KEYとTELEGRAM_CHAT_IDが設定されていません。")

    elif args.job == 'stop_sharing_message':
        if TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = "✅ *リマインダー:* ライブ位置情報の共有を停止できます。"
            send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print("共有停止リマインダーを送信しました。")
        else:
            print("TELEGRAM_LOCATION_BOT_API_KEYとTELEGRAM_CHAT_IDが設定されていません。")

    elif args.job == 'check_location':
        if not TELEGRAM_LOCATION_BOT_API_KEY or not TELEGRAM_CHAT_ID:
            print("位置確認にはTELEGRAM_LOCATION_BOT_API_KEYとTELEGRAM_CHAT_IDの設定が必要です。")
            return

        user_location, location_chat_id = get_latest_location(TELEGRAM_LOCATION_BOT_API_KEY)

        if user_location:
            current_latitude = user_location['latitude']
            current_longitude = user_location['longitude']

            distance = haversine_distance(
                OFFICE_LATITUDE, OFFICE_LONGITUDE,
                current_latitude, current_longitude
            )

            print(f"現在位置: ({current_latitude}, {current_longitude})")
            print(f"オフィスまでの距離: {distance:.2f} メートル")

            needs_punch_card = distance <= PROXIMITY_RADIUS_METERS

            if needs_punch_card:
                print(f"オフィスから{PROXIMITY_RADIUS_METERS}m圏内にいます！")
                notification_message = (
                    f"🎉 *オフィス到着！* 🎉\n"
                    f"WeComで打刻する時間です。\n"
                    f"現在のオフィスからの距離: {distance:.2f}m。"
                )
            else:
                print(f"オフィスから{PROXIMITY_RADIUS_METERS}m圏外にいます。")
                # 圏外時のメッセージ
                notification_message = (
                    f"📍 オフィス近接圏（{PROXIMITY_RADIUS_METERS}m）の*外側*にいます。\n"
                    f"現時点で打刻は不要です。\n"
                    f"現在のオフィスからの距離: {distance:.2f}m。"
                )

            # 近接圏内または--testフラグ使用時にメッセージ送信
            if needs_punch_card or args.test:
                send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, notification_message)
            else:
                # 近接圏外かつテストモードでない場合、コンソールに表示のみ（Telegramメッセージなし）
                print("近接圏外かつテストモードではないため、Telegramにメッセージを送信しませんでした。")
        else:
            print("最新の位置情報を取得できませんでした。ボットとライブ位置情報を共有していることを確認してください。")

if __name__ == '__main__':
    main()
```