---
audio: true
generated: false
lang: ja
layout: post
title: GitHub ActionsとTelegramによるリマインダーの効率化
translated: true
---

このプロジェクトでは、GitHub ActionsとTelegramボットを活用して、日々のタスクや月次の業務を管理する自動リマインダーシステムを構築しました。cronスケジュールを利用して、WeComでの打刻、タイムシート提出、給与確認といった仕事関連のタスクから、実家訪問、JD.comでの買い物、パートナーとのテレビ鑑賞といったプライベートな予定まで、さまざまなリマインダーを設定しています。PythonスクリプトでTelegramのBot APIを介してメッセージを送信し、環境変数はGitHub Secretsで安全に管理しています。このシステムにより、重要な締め切りや個人的な約束を見逃すことなく、テクノロジーと日常生活を融合させて最大限の効率を実現しています。

```yaml
name: リマインダー

on:
  schedule:
    # 北京時間（UTC+8）で水曜日から金曜日の午後12時から午後8時まで2時間ごとに実行
    - cron: '0 4,6,8,10,12 * * 3-5'
    # 毎月27日午後12時（北京時間、UTC+8）に実行
    - cron: '0 4 27 * *'
    # 毎月30日午後2時（北京時間、UTC+8）に実行
    - cron: '0 6 30 * *'
    # 毎日午前1時北京時間（前日午後5時UTC）に実行
    - cron: '0 17 * * *'
    # 毎日午前11時北京時間（午前3時UTC）に実行
    - cron: '0 3 * * *'
    # 翌日の実家訪問リマインダー：北京時間午後9時（午後1時UTC）火・水・木曜日
    - cron: '0 13 * * 2-4'
    # 翌日の自宅訪問リマインダー：北京時間午後9時（午後1時UTC）日・月・金・土曜日
    - cron: '0 13 * * 0,1,5,6'
    # JD.comで生鮮食品を直接購入するリマインダー：北京時間午後9時（午後1時UTC）水曜日
    - cron: '0 13 * * 3'
    # JD.comで速達食品を購入するリマインダー：北京時間午後9時（午後1時UTC）金曜日
    - cron: '0 13 * * 5'
    # 3月、4月、9月、10月の毎週月曜日午後1時北京時間（午前5時UTC）に準学士号試験のリマインダー
    - cron: '0 5 * 3,4,9,10 1'
    # 毎週金曜日午後5時台北時間（午前9時UTC）にClarityタイムシート提出リマインダー
    - cron: '0 9 * * 5'
    # 毎月25日午前0時台北時間（前日午後4時UTC）にベンダータイムシート提出リマインダー
    - cron: '0 16 25 * *'
    # 毎月16日午後9時台北時間（午後1時UTC）に家族へ住宅ローン支援依頼リマインダー
    - cron: '0 13 16 * *'
    # 毎週金・土・日曜日午後10時台北時間（午後2時UTC）にパートナーとテレビ鑑賞リマインダー
    - cron: '0 14 * * 5,6,0'
    # 北京時間午前2時（午後6時UTC）水・木・金曜日に駐車許可証ステッカー除去リマインダー
    - cron: '0 18 * * 3,4,5'
  workflow_dispatch:  # 手動トリガーを許可

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

      - name: WeCom打刻リマインダー用Telegramスクリプトを実行
        run: python scripts/release/reminders_bot.py --job send_message --message "WeComで打刻してください"
        if: github.event.schedule == '0 4,6,8,10,12 * * 3-5'

      - name: 住宅ローン月次リマインダー用Telegramスクリプトを実行
        run: python scripts/release/reminders_bot.py --job send_message --message "住宅ローンの引き落とし準備をしてください"
        if: github.event.schedule == '0 4 27 * *'

      - name: 給与確認月次リマインダー用Telegramスクリプトを実行
        run: python scripts/release/reminders_bot.py --job send_message --message "給与を確認してください"
        if: github.event.schedule == '0 6 30 * *'

      - name: 就寝リマインダー用Telegramスクリプトを実行
        run: python scripts/release/reminders_bot.py --job send_message --message "寝る時間です！"
        if: github.event.schedule == '0 17 * * *'

      - name: 起床リマインダー用Telegramスクリプトを実行
        run: python scripts/release/reminders_bot.py --job send_message --message "起きる時間です！"
        if: github.event.schedule == '0 3 * * *'

      - name: 実家訪問リマインダー用Telegramスクリプトを実行
        run: python scripts/release/reminders_bot.py --job send_message --message "明日は実家に行きましょう！"
        if: github.event.schedule == '0 13 * * 2-4'

      - name: 自宅訪問リマインダー用Telegramスクリプトを実行
        run: python scripts/release/reminders_bot.py --job send_message --message "明日は自宅に帰りましょう！"
        if: github.event.schedule == '0 13 * * 0,1,5,6'

      - name: JD.com生鮮食品購入リマインダー用Telegramスクリプトを実行
        run: python scripts/release/reminders_bot.py --job send_message --message "JD.comで生鮮食品を直接購入しましょう！"
        if: github.event.schedule == '0 13 * * 3'

      - name: JD.com速達食品購入リマインダー用Telegramスクリプトを実行
        run: python scripts/release/reminders_bot.py --job send_message --message "JD.comで速達食品を購入しましょう！"
        if: github.event.schedule == '0 13 * * 5'

      - name: 準学士号試験リマインダー用Telegramスクリプトを実行
        run: python scripts/release/reminders_bot.py --job send_message --message "準学士号試験に登録してください"
        if: github.event.schedule == '0 5 * 3,4,9,10 1'

      - name: Clarityタイムシート提出リマインダー用Telegramスクリプトを実行
        run: python scripts/release/reminders_bot.py --job send_message --message "Clarityタイムシートを提出してください"
        if: github.event.schedule == '0 9 * * 5'

      - name: ベンダータイムシート提出リマインダー用Telegramスクリプトを実行
        run: python scripts/release/reminders_bot.py --job send_message --message "ベンダータイムシートを提出してください"
        if: github.event.schedule == '0 16 25 * *'

      - name: 家族住宅ローン支援依頼リマインダー用Telegramスクリプトを実行
        run: python scripts/release/reminders_bot.py --job send_message --message "家族に住宅ローンの支援を依頼してください"
        if: github.event.schedule == '0 13 16 * *'

      - name: パートナーとテレビ鑑賞リマインダー用Telegramスクリプトを実行
        run: python scripts/release/reminders_bot.py --job send_message --message "パートナーとテレビを見る時間です！"
        if: github.event.schedule == '0 14 * * 5,6,0'

      - name: 車窓ステッカー除去リマインダー用Telegramスクリプトを実行
        run: python scripts/release/reminders_bot.py --job send_message --message "車窓から駐車許可証ステッカーを除去してください"
        if: github.event.schedule == '0 18 * * 3,4,5'

      - name: テストメッセージ用Telegramスクリプトを実行
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
    """ボットに送信された最後のメッセージのチャットIDを取得"""
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