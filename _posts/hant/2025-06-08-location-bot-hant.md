---
audio: false
generated: false
lang: hant
layout: post
title: 自動化你的打卡系統以電報地點機器人
translated: true
---

總是希望每日「打卡」的流程能更輕鬆？我確實有同樣的感受。因此，我建立了一個個人 Telegram 機器人，利用位置追蹤功能自動通知辦公室到達時間，並提醒我進行重要的打卡。本文將深入探討如何結合 Python 與 GitHub Actions 創建一個無縫、無需手動操作的系統，在您需要時提供即時通知，完全基於您的位置。

```yml
name: 每小時位置檢查

on:
  schedule:
    # 每小時，在上午 11 時至晚上 11 時之間，於工作日（星期一至星期五）執行
    # 時間為 UTC 時區。新加坡時間（SGT）為 UTC+8。
    # 因此，上午 11 時 SGT 為 03:00 UTC，晚上 11 時 SGT 為 15:00 UTC。
    # 因此，我們需要從 03:00 至 15:00 UTC 進行排程。
    - cron: '0 3-15 * * 1-5'

    # 提醒開始分享實時位置：星期三上午 11 時 SGT（UTC+8）
    # 當前時間：2025 年 6 月 8 日星期日下午 5:10:58 +08 (SGT)
    # 星期三上午 11 時 SGT（UTC+8）：11 - 8 = 3 AM UTC。
    - cron: '0 3 * * 3' # 3 代表星期三

    # 提醒停止分享實時位置：星期五晚上 11 時 SGT（UTC+8）
    # 當前時間：2025 年 6 月 8 日星期日下午 5:10:58 +08 (SGT)
    # 星期五晚上 11 時 SGT（UTC+8）：23 - 8 = 15 PM UTC。
    - cron: '0 15 * * 5' # 5 代表星期五

  workflow_dispatch:  # 允許手動觸發工作流程
  push:
    branches: ["main"]
    paths:
      - 'scripts/release/location_bot.py' # 修正至您的腳本路徑
      - '.github/workflows/location.yml' # 此工作流程文件的路徑

concurrency:
  group: 'location'
  cancel-in-progress: false

jobs:
  check_and_notify:
    runs-on: ubuntu-latest
    env:
      TELEGRAM_LOCATION_BOT_API_KEY: ${{ secrets.TELEGRAM_LOCATION_BOT_API_KEY }}

    steps:
    - name: 檢查存儲庫
      uses: actions/checkout@v4
      with:
        fetch-depth: 5 # 為提高效率，僅獲取最後 5 次提交

    - name: 設定 Python 3.13.2
      uses: actions/setup-python@v4
      with:
        python-version: "3.13.2" # 指定精確的 Python 版本

    - name: 安裝依賴項
      run: |
        python -m pip install --upgrade pip
        # 假設您在存儲庫根目錄有 requirements.simple.txt。
        # 如果沒有，請使用：pip install requests python-dotenv
        pip install -r requirements.simple.txt

    - name: 執行位置檢查腳本（排程）
      run: python scripts/release/location_bot.py --job check_location
      # 此步驟將在排程觸發時執行每小時檢查
      if: github.event.schedule == '0 3-15 * * 1-5' # 匹配每小時 cron 排程

    - name: 提醒開始分享實時位置
      run: python scripts/release/location_bot.py --job start_sharing_message
      if: github.event.schedule == '0 3 * * 3' # 匹配星期三上午 11 時 SGT cron

    - name: 提醒停止分享實時位置
      run: python scripts/release/location_bot.py --job stop_sharing_message
      if: github.event.schedule == '0 15 * * 5' # 匹配星期五晚上 11 時 SGT cron

    - name: 執行 Telegram 腳本以測試訊息（手動觸發）
      run: python scripts/release/location_bot.py --job send_message --message "這是來自 GitHub Actions 的手動觸發測試訊息。"
      if: github.event_name == 'workflow_dispatch'

    - name: 執行 Telegram 腳本以推送到主分支
      run: python scripts/release/location_bot.py --job send_message --message "位置機器人的程式碼已推送到主分支。"
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
import time # 用於潛在未來的持續監控

load_dotenv()

# 新增：專用於位置機器人的 API 金鑰
TELEGRAM_LOCATION_BOT_API_KEY = os.environ.get("TELEGRAM_LOCATION_BOT_API_KEY") # 確保在您的 .env 中設定
TELEGRAM_CHAT_ID = "610574272" # 此聊天 ID 用於發送通知訊息

# 定義您的辦公室座標
OFFICE_LATITUDE = 23.135368
OFFICE_LONGITUDE = 113.32952

# 附近範圍半徑（公尺）
PROXIMITY_RADIUS_METERS = 300

def send_telegram_message(bot_token, chat_id, message):
    """使用 Telegram Bot API 向 Telegram 聊天發送訊息。"""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown" # 使用 Markdown 以在訊息中加粗文字
    }
    response = requests.post(url, params=params)
    if response.status_code != 200:
        print(f"發送 Telegram 訊息時出錯：{response.status_code} - {response.text}")

def get_latest_location(bot_token):
    """從機器人獲取最新的實時位置更新。"""
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    # 偏移量以獲取最後處理後的新更新（用於持續輪詢）
    # 對於簡單的一次性腳本，我們只獲取最新的，但對於輪詢，您需要管理偏移量。
    params = {"offset": -1} # 獲取最新的更新
    response = requests.get(url, params=params)
    print("GetUpdates 回應:", response) # 調試
    if response.status_code == 200:
        updates = response.json()
        print("GetUpdates JSON:", json.dumps(updates, indent=4)) # 調試
        if updates['result']:
            last_update = updates['result'][-1]
            # 優先處理編輯後的訊息以獲取實時位置
            if 'edited_message' in last_update and 'location' in last_update['edited_message']:
                return last_update['edited_message']['location'], last_update['edited_message']['chat']['id']
            elif 'message' in last_update and 'location' in last_update['message']:
                # 處理初始實時位置訊息或靜態位置分享
                return last_update['message']['location'], last_update['message']['chat']['id']
    return None, None

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    使用哈弗辛公式計算地球上兩點之間的距離。
    返回距離（公尺）。
    """
    R = 6371000  # 地球半徑（公尺）

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
    parser = argparse.ArgumentParser(description="Telegram 機器人腳本")
    # 更新 --job 參數的選項
    parser.add_argument('--job', choices=['get_chat_id', 'send_message', 'check_location', 'start_sharing_message', 'stop_sharing_message'], required=True, help="要執行的任務")
    # 為 'send_message' 任務新增 --message 參數
    parser.add_argument('--message', type=str, help="用於 'send_message' 任務的訊息")
    # 為 'check_location' 任務新增 --test 參數
    parser.add_argument('--test', action='store_true', help="對於 'check_location' 任務，強制發送訊息，不考慮附近範圍。")
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
                    print(f"聊天 ID: {chat_id}")
                else:
                    print("無法從最後的更新中獲取聊天 ID。")
            else:
                print("未找到更新。")
        else:
            print(f"獲取更新時出錯：{response.status_code} - {response.text}")

    elif args.job == 'send_message':
        if TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = args.message if args.message else "這是來自您的 Telegram 機器人腳本的預設測試訊息！"
            send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print(f"訊息已成功發送：{message}")
        else:
            print("TELEGRAM_LOCATION_BOT_API_KEY 和 TELEGRAM_CHAT_ID 未設定。")

    elif args.job == 'start_sharing_message':
        if TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = "⚠️ *提醒：* 請開始向機器人分享您的實時位置！"
            send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print("已發送開始分享提醒。")
        else:
            print("TELEGRAM_LOCATION_BOT_API_KEY 和 TELEGRAM_CHAT_ID 未設定。")

    elif args.job == 'stop_sharing_message':
        if TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = "✅ *提醒：* 您現在可以停止分享實時位置。"
            send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print("已發送停止分享提醒。")
        else:
            print("TELEGRAM_LOCATION_BOT_API_KEY 和 TELEGRAM_CHAT_ID 未設定。")

    elif args.job == 'check_location':
        if not TELEGRAM_LOCATION_BOT_API_KEY or not TELEGRAM_CHAT_ID:
            print("TELEGRAM_LOCATION_BOT_API_KEY 和 TELEGRAM_CHAT_ID 必須設定以進行位置檢查。")
            return

        user_location, location_chat_id = get_latest_location(TELEGRAM_LOCATION_BOT_API_KEY)

        if user_location:
            current_latitude = user_location['latitude']
            current_longitude = user_location['longitude']

            distance = haversine_distance(
                OFFICE_LATITUDE, OFFICE_LONGITUDE,
                current_latitude, current_longitude
            )

            print(f"當前位置：({current_latitude}, {current_longitude})")
            print(f"距離辦公室：{distance:.2f} 公尺")

            needs_punch_card = distance <= PROXIMITY_RADIUS_METERS

            if needs_punch_card:
                print(f"您已在辦公室 {PROXIMITY_RADIUS_METERS} 公尺範圍內！")
                notification_message = (
                    f"🎉 *已到達辦公室!* 🎉\n"
                    f"現在可以在 WeCom 打卡了。\n"
                    f"您當前距離辦公室：{distance:.2f} 公尺。"
                )
            else:
                print(f"您不在辦公室 {PROXIMITY_RADIUS_METERS} 公尺範圍內。")
                # 當超出範圍時的訊息
                notification_message = (
                    f"📍 您 *不在* 办公室附近 ({PROXIMITY_RADIUS_METERS} 公尺)。\n"
                    f"目前無需打卡。\n"
                    f"您當前距離辦公室：{distance:.2f} 公尺。"
                )

            # 如果在附近範圍內或使用 --test 旗標時發送訊息
            if needs_punch_card or args.test:
                send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, notification_message)
            else:
                # 如果不在附近範圍內且不在測試模式下，僅在控制台列印（不發送 Telegram 訊息）
                print("不在附近範圍內且不在測試模式下，未發送 Telegram 訊息。")
        else:
            print("無法獲取您的最新位置。請確保您已向機器人分享實時位置。")

if __name__ == '__main__':
    main()
```

---

更新：這不理想，因為您需要向機器人分享實時位置。