---
audio: false
generated: false
lang: hant
layout: post
title: 利用Telegram定位機器人自動化您的打卡系統
translated: true
---

```yml
name: 每小時位置檢查

on:
  schedule:
    # 每週一至週五，每小時整點執行一次，時間範圍為新加坡時間上午11點至晚上11點
    # 時間以UTC為準。新加坡時間（SGT）為UTC+8。
    # 因此，新加坡時間上午11點為UTC時間03:00，新加坡時間晚上11點為UTC時間15:00。
    # 所以我們需要設定從UTC時間03:00到15:00執行。
    - cron: '0 3-15 * * 1-5'

    # 提醒開始分享實時位置：每週三新加坡時間上午11點（UTC時間3點）
    # 當前時間：2025年6月8日星期日，新加坡時間下午5:10:58（UTC+8）
    # 週三新加坡時間上午11點（UTC+8）對應UTC時間：11 - 8 = 3 AM UTC。
    - cron: '0 3 * * 3' # 3代表週三

    # 提醒停止分享實時位置：每週五新加坡時間晚上11點（UTC時間15點）
    # 當前時間：2025年6月8日星期日，新加坡時間下午5:10:58（UTC+8）
    # 週五新加坡時間晚上11點（UTC+8）對應UTC時間：23 - 8 = 15 PM UTC。
    - cron: '0 15 * * 5' # 5代表週五

  workflow_dispatch:  # 允許手動觸發工作流程
  push:
    branches: ["main"]
    paths:
      - 'scripts/release/location_bot.py' # 修正後的腳本路徑
      - '.github/workflows/location.yml' # 本工作流程文件的路徑

concurrency:
  group: 'location'
  cancel-in-progress: false

jobs:
  check_and_notify:
    runs-on: ubuntu-latest
    env:
      TELEGRAM_LOCATION_BOT_API_KEY: ${{ secrets.TELEGRAM_LOCATION_BOT_API_KEY }}

    steps:
    - name: 檢出存儲庫
      uses: actions/checkout@v4
      with:
        fetch-depth: 5 # 僅獲取最後5次提交以提高效率

    - name: 設置 Python 3.13.2
      uses: actions/setup-python@v4
      with:
        python-version: "3.13.2" # 指定Python版本

    - name: 安裝依賴項
      run: |
        python -m pip install --upgrade pip
        # 假設存儲庫根目錄下有requirements.simple.txt文件。
        # 如果沒有，使用：pip install requests python-dotenv
        pip install -r requirements.simple.txt 

    - name: 執行位置檢查腳本（定時）
      run: python scripts/release/location_bot.py --job check_location
      # 此步驟將在定時觸發時執行每小時檢查
      if: github.event.schedule == '0 3-15 * * 1-5' # 匹配每小時的cron計劃

    - name: 提醒開始分享實時位置
      run: python scripts/release/location_bot.py --job start_sharing_message
      if: github.event.schedule == '0 3 * * 3' # 匹配週三新加坡時間上午11點的cron

    - name: 提醒停止分享實時位置
      run: python scripts/release/location_bot.py --job stop_sharing_message
      if: github.event.schedule == '0 15 * * 5' # 匹配週五新加坡時間晚上11點的cron

    - name: 執行Telegram腳本發送測試消息（手動觸發）
      run: python scripts/release/location_bot.py --job send_message --message "這是一條來自GitHub Actions的手動觸發測試消息。"
      if: github.event_name == 'workflow_dispatch'

    - name: 執行Telegram腳本推送至主分支
      run: python scripts/release/location_bot.py --job send_message --message "位置機器人的代碼更改已推送至主分支。"
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
import time # 為未來可能的持續監控準備

load_dotenv()

# 新增：專為位置機器人設置的API密鑰
TELEGRAM_LOCATION_BOT_API_KEY = os.environ.get("TELEGRAM_LOCATION_BOT_API_KEY") # 確保.env文件中已設置
TELEGRAM_CHAT_ID = "610574272" # 此聊天ID用於發送通知消息

# 定義辦公室坐標
OFFICE_LATITUDE = 23.135368
OFFICE_LONGITUDE = 113.32952

# 接近半徑（米）
PROXIMITY_RADIUS_METERS = 300

def send_telegram_message(bot_token, chat_id, message):
    """使用Telegram Bot API發送消息至指定聊天。"""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown" # 使用Markdown格式加粗消息文本
    }
    response = requests.post(url, params=params)
    if response.status_code != 200:
        print(f"發送Telegram消息時出錯：{response.status_code} - {response.text}")

def get_latest_location(bot_token):
    """從機器人獲取最新的實時位置更新。"""
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    # 偏移量以僅獲取上次處理後的新更新（用於持續輪詢）
    # 對於一次性運行的腳本，我們只獲取最新更新，但輪詢時需管理偏移量。
    params = {"offset": -1} # 獲取最後一條更新
    response = requests.get(url, params=params)
    print("GetUpdates 響應:", response) # 調試用
    if response.status_code == 200:
        updates = response.json()
        print("GetUpdates JSON:", json.dumps(updates, indent=4)) # 調試用
        if updates['result']:
            last_update = updates['result'][-1]
            # 優先處理edited_message中的實時位置
            if 'edited_message' in last_update and 'location' in last_update['edited_message']:
                return last_update['edited_message']['location'], last_update['edited_message']['chat']['id']
            elif 'message' in last_update and 'location' in last_update['message']:
                # 處理初始實時位置消息或靜態位置分享
                return last_update['message']['location'], last_update['message']['chat']['id']
    return None, None

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    使用Haversine公式計算地球上兩點之間的距離。
    返回距離（米）。
    """
    R = 6371000  # 地球半徑（米）

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
    parser = argparse.ArgumentParser(description="Telegram機器人腳本")
    # 更新--job參數的選項
    parser.add_argument('--job', choices=['get_chat_id', 'send_message', 'check_location', 'start_sharing_message', 'stop_sharing_message'], required=True, help="執行任務")
    # 為'send_message'任務添加--message參數
    parser.add_argument('--message', type=str, help="為'send_message'任務指定消息內容")
    # 為'check_location'任務添加--test參數
    parser.add_argument('--test', action='store_true', help="對於'check_location'任務，強制發送消息，無論是否接近。")
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
                    print(f"聊天ID: {chat_id}")
                else:
                    print("無法從最後一條更新中獲取聊天ID。")
            else:
                print("未找到更新記錄。")
        else:
            print(f"獲取更新時出錯：{response.status_code} - {response.text}")

    elif args.job == 'send_message':
        if TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = args.message if args.message else "這是來自Telegram機器人腳本的默認測試消息！"
            send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print(f"消息發送成功：{message}")
        else:
            print("未設置TELEGRAM_LOCATION_BOT_API_KEY或TELEGRAM_CHAT_ID。")

    elif args.job == 'start_sharing_message':
        if TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = "⚠️ *提醒：* 請開始向機器人分享您的實時位置！"
            send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print("已發送開始分享提醒。")
        else:
            print("未設置TELEGRAM_LOCATION_BOT_API_KEY或TELEGRAM_CHAT_ID。")

    elif args.job == 'stop_sharing_message':
        if TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = "✅ *提醒：* 您現在可以停止分享實時位置了。"
            send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print("已發送停止分享提醒。")
        else:
            print("未設置TELEGRAM_LOCATION_BOT_API_KEY或TELEGRAM_CHAT_ID。")

    elif args.job == 'check_location':
        if not TELEGRAM_LOCATION_BOT_API_KEY or not TELEGRAM_CHAT_ID:
            print("進行位置檢查必須設置TELEGRAM_LOCATION_BOT_API_KEY和TELEGRAM_CHAT_ID。")
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
            print(f"距離辦公室的距離：{distance:.2f} 米")

            needs_punch_card = distance <= PROXIMITY_RADIUS_METERS

            if needs_punch_card:
                print(f"您位於辦公室{PROMIXITY_RADIUS_METERS}米範圍內！")
                notification_message = (
                    f"🎉 *已到達辦公室！* 🎉\n"
                    f"請記得在企業微信打卡。\n"
                    f"您當前距離辦公室：{distance:.2f}米。"
                )
            else:
                print(f"您位於辦公室{PROMIXITY_RADIUS_METERS}米範圍外。")
                # 範圍外的提示消息
                notification_message = (
                    f"📍 您當前*不在*辦公室附近（{PROMIXITY_RADIUS_METERS}米範圍內）。\n"
                    f"此時無需打卡。\n"
                    f"您當前距離辦公室：{distance:.2f}米。"
                )

            # 若在範圍內或使用--test標記，則發送消息
            if needs_punch_card or args.test:
                send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, notification_message)
            else:
                # 若不在範圍內且非測試模式，僅打印至控制台（不發送Telegram消息）
                print("不在範圍內且非測試模式，未向Telegram發送消息。")
        else:
            print("無法獲取您的最新位置。請確保您正在向機器人分享實時位置。")

if __name__ == '__main__':
    main()
```