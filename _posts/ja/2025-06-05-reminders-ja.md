---
audio: true
generated: false
lang: ja
layout: post
title: Telegramで効率化するリマインダー
translated: true
---

このプロジェクトでは、GitHub ActionsとTelegramボットを活用して、日々のタスクや月次の業務を管理する自動リマインダーシステムを構築しました。cronスケジュールを利用して、WeComでの打刻、タイムシートの提出、給与確認といった仕事関連のタスクから、実家への訪問、JD.comでの買い物、パートナーとのテレビ鑑賞といったプライベートな予定までをリマインドするように設定しています。Pythonスクリプトを用いてTelegramのBot API経由でメッセージを送信し、環境変数はGitHub Secretsで安全に管理しています。このシステムにより、重要な締め切りや個人的な約束を見逃すことなく、テクノロジーと日常生活を融合させて最大限の効率を実現しています。

```yaml
name: リマインダー

on:
  schedule:
    # 毎週水曜日から金曜日、北京時間午後12時から午後8時まで2時間ごとに実行（UTC+8）
    - cron: '0 4,6,8,10,12 * * 3-5'
    # 毎月27日正午に実行（北京時間、UTC+8）
    - cron: '0 4 27 * *'
    # 毎月30日午後2時に実行（北京時間、UTC+8）
    - cron: '0 6 30 * *'
    # 毎日午前1時に実行（北京時間、前日UTC午後5時）
    - cron: '0 17 * * *'
    # 毎日午前11時に実行（北京時間、UTC午前3時）
    - cron: '0 3 * * *'
    # 火曜日から木曜日、午後9時に実家訪問をリマインド（北京時間、UTC午後1時）
    - cron: '0 13 * * 2-4'
    # 日曜日、月曜日、金曜日、土曜日、午後9時に自宅訪問をリマインド（北京時間、UTC午後1時）
    - cron: '0 13 * * 0,1,5,6'
    # 水曜日午後9時にJD.comで生鮮食品を購入するようリマインド（北京時間、UTC午後1時）
    - cron: '0 13 * * 3'
    # 金曜日午後9時にJD.comで速達食品を購入するようリマインド（北京時間、UTC午後1時）
    - cron: '0 13 * * 5'
    # 3月、4月、9月、10月の毎週月曜日午後1時に短大試験をリマインド（北京時間、UTC午前5時）
    - cron: '0 5 * 3,4,9,10 1'
    # 毎週金曜日午後5時にタイムシート提出をリマインド（台北時間、UTC午前9時）
    - cron: '0 9 * * 5'
    # 毎月25日午前0時にベンダータイムシート提出をリマインド（台北時間、前日UTC午後4時）
    - cron: '0 16 25 * *'
    # 毎月16日午後9時に家族へ住宅ローン支援を依頼するようリマインド（台北時間、UTC午後1時）
    - cron: '0 13 16 * *'
    # 毎週金曜日、土曜日、日曜日午後10時にパートナーとテレビ鑑賞をリマインド（台北時間、UTC午後2時）
    - cron: '0 14 * * 5,6,0'
    # 水曜日から金曜日、午前2時に駐車許可証ステッカーを剥がすようリマインド（北京時間、UTC午後6時）
    - cron: '0 18 * * 3,4,5'
  workflow_dispatch:  # 手動実行を許可

concurrency:
  group: 'reminders'
  cancel-in-progress: false

jobs:
  send-reminders:
    runs-on: ubuntu-latest
    environment: github-pages
    env:
      TELEGRAM_BOT2_API_KEY: ${{ secrets.TELEGRAM_BOT2_API_KEY }}

    steps:
      - name: リポジトリをチェックアウト
        uses: actions/checkout@v4
        with:
          fetch-depth: 5

      - name: Python 3.10.xをセットアップ
        uses: actions/setup-python@v4
        with:
          python-version: "3.10.x"

      - name: 依存関係をインストール
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.simple.txt

      - name: WeCom打刻リマインダーを送信
        run: python scripts/release/reminders_bot.py --job send_message --message "WeComで打刻してください"
        if: github.event.schedule == '0 4,6,8,10,12 * * 3-5'

      - name: 住宅ローンリマインダーを送信
        run: python scripts/release/reminders_bot.py --job send_message --message "住宅ローンの引き落とし準備をしてください"
        if: github.event.schedule == '0 4 27 * *'

      - name: 給与確認リマインダーを送信
        run: python scripts/release/reminders_bot.py --job send_message --message "給与を確認してください"
        if: github.event.schedule == '0 6 30 * *'

      - name: 就寝リマインダーを送信
        run: python scripts/release/reminders_bot.py --job send_message --message "寝る時間です！"
        if: github.event.schedule == '0 17 * * *'

      - name: 起床リマインダーを送信
        run: python scripts/release/reminders_bot.py --job send_message --message "起きる時間です！"
        if: github.event.schedule == '0 3 * * *'

      - name: 実家訪問リマインダーを送信
        run: python scripts/release/reminders_bot.py --job send_message --message "明日は実家に行きましょう！"
        if: github.event.schedule == '0 13 * * 2-4'

      - name: 自宅訪問リマインダーを送信
        run: python scripts/release/reminders_bot.py --job send_message --message "明日は自宅に行きましょう！"
        if: github.event.schedule == '0 13 * * 0,1,5,6'

      - name: JD.com生鮮食品購入リマインダーを送信
        run: python scripts/release/reminders_bot.py --job send_message --message "JD.comで産地直送の生鮮食品を購入しましょう！"
        if: github.event.schedule == '0 13 * * 3'

      - name: JD.com速達食品購入リマインダーを送信
        run: python scripts/release/reminders_bot.py --job send_message --message "JD.comで速達食品を購入しましょう！"
        if: github.event.schedule == '0 13 * * 5'

      - name: 短大試験登録リマインダーを送信
        run: python scripts/release/reminders_bot.py --job send_message --message "短大試験に登録してください"
        if: github.event.schedule == '0 5 * 3,4,9,10 1'

      - name: タイムシート提出リマインダーを送信
        run: python scripts/release/reminders_bot.py --job send_message --message "タイムシートを提出してください"
        if: github.event.schedule == '0 9 * * 5'

      - name: ベンダータイムシート提出リマインダーを送信
        run: python scripts/release/reminders_bot.py --job send_message --message "ベンダータイムシートを提出してください"
        if: github.event.schedule == '0 16 25 * *'

      - name: 住宅ローン支援依頼リマインダーを送信
        run: python scripts/release/reminders_bot.py --job send_message --message "家族に住宅ローンの支援を依頼してください"
        if: github.event.schedule == '0 13 16 * *'

      - name: パートナーとテレビ鑑賞リマインダーを送信
        run: python scripts/release/reminders_bot.py --job send_message --message "パートナーとテレビを見る時間です！"
        if: github.event.schedule == '0 14 * * 5,6,0'

      - name: 駐車許可証ステッカー除去リマインダーを送信
        run: python scripts/release/reminders_bot.py --job send_message --message "車の窓から駐車許可証ステッカーを剥がしてください"
        if: github.event.schedule == '0 18 * * 3,4,5'

      - name: テストメッセージを送信
        run: python scripts/release/reminders_bot.py --job send_message --message "これはGitHub Actionsからのテストメッセージです"
        if: github.event_name == 'workflow_dispatch'
```

```python
import os
import requests
from dotenv import load_dotenv
import json
import argparse

load_dotenv()

TELEGRAM_BOT2_API_KEY = os.environ.get("TELEGRAM_BOT2_API_KEY")
TELEGRAM_CHAT_ID = "610574272"

def send_telegram_message(bot_token, chat_id, message):
    """Telegram Bot APIを使用してチャットにメッセージを送信"""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, params=params)
    if response.status_code != 200:
        print(f"Telegramメッセージ送信エラー: {response.status_code} - {response.text}")

def get_chat_id(bot_token):
    """ボットに送信された最新メッセージのチャットIDを取得"""
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    response = requests.get(url)
    if response.status_code == 200:
        updates = response.json()
        print(json.dumps(updates, indent=4))
        if updates['result']:
            chat_id = updates['result'][-1]['message']['chat']['id']
            return chat_id
    return None

def send_reminder(message):
    """リマインダーメッセージをTelegramに送信"""
    if TELEGRAM_BOT2_API_KEY and TELEGRAM_CHAT_ID:
        send_telegram_message(TELEGRAM_BOT2_API_KEY, TELEGRAM_CHAT_ID, f"リマインダー: {message}")
    else:
        print("TELEGRAM_BOT2_API_KEYとTELEGRAM_CHAT_IDが設定されていません")

def main():
    parser = argparse.ArgumentParser(description="Telegramボットスクリプト")
    parser.add_argument('--job', choices=['get_chat_id', 'send_message'], required=True, help="実行するジョブ")
    parser.add_argument('--message', help="送信するカスタムメッセージ", default=None)
    args = parser.parse_args()

    if args.job == 'get_chat_id':
        bot_token = TELEGRAM_BOT2_API_KEY
        chat_id = get_chat_id(bot_token)
        if chat_id:
            print(f"チャットID: {chat_id}")
        else:
            print("チャットIDを取得できませんでした")

    elif args.job == 'send_message':
        if args.message:
            send_reminder(args.message)
        else:
            print("send_messageジョブにメッセージが指定されていません")
            
if __name__ == '__main__':
    main()
```