---
audio: false
generated: false
lang: zh
layout: post
title: 自动化你的打卡机器人
translated: true
---

# 翻译后的简体中文

你是否曾希望每天的“打卡”流程能更轻松一些？我确实如此。这就是我为什么构建了一个个人Telegram机器人，利用位置追踪来自动化办公室到达通知，并提醒我进行那些关键的打卡。本文将深入探讨我如何结合Python和GitHub Actions创建一个无缝、无需手动操作的系统，在你需要时保持你的信息更新，所有这些都基于你的位置。

```yml
name: 每小时位置检查

on:
  schedule:
    # 每小时运行一次，在上午11点到晚上11点之间，工作日（周一至周五）
    # 时间为UTC时间。新加坡时间（SGT）为UTC+8。
    # 因此，上午11点SGT为03:00 UTC，晚上11点SGT为15:00 UTC。
    # 因此，我们需要从03:00到15:00 UTC安排。
    - cron: '0 3-15 * * 1-5'

    # 提醒开始共享实时位置：周三上午11点SGT（3 AM UTC）
    # 当前时间：2025年6月8日星期日下午5:10:58 +08 (SGT)
    # 周三上午11点SGT（UTC+8）：11 - 8 = 3 AM UTC。
    - cron: '0 3 * * 3' # 3代表周三

    # 提醒停止共享实时位置：周五晚上11点SGT（3 PM UTC）
    # 当前时间：2025年6月8日星期日下午5:10:58 +08 (SGT)
    # 周五晚上11点SGT（UTC+8）：23 - 8 = 15 PM UTC。
    - cron: '0 15 * * 5' # 5代表周五

  workflow_dispatch:  # 允许手动触发工作流
  push:
    branches: ["main"]
    paths:
      - 'scripts/release/location_bot.py' # 修正到你的脚本路径
      - '.github/workflows/location.yml' # 此工作流文件的路径

concurrency:
  group: 'location'
  cancel-in-progress: false

jobs:
  check_and_notify:
    runs-on: ubuntu-latest
    env:
      TELEGRAM_LOCATION_BOT_API_KEY: ${{ secrets.TELEGRAM_LOCATION_BOT_API_KEY }}

    steps:
    - name: 检出仓库
      uses: actions/checkout@v4
      with:
        fetch-depth: 5 # 仅获取最后5次提交以提高效率

    - name: 设置Python 3.13.2
      uses: actions/setup-python@v4
      with:
        python-version: "3.13.2" # 指定精确的Python版本

    - name: 安装依赖
      run: |
        python -m pip install --upgrade pip
        # 假设你在仓库根目录下有一个requirements.simple.txt。
        # 如果没有，使用: pip install requests python-dotenv
        pip install -r requirements.simple.txt

    - name: 运行位置检查脚本（定时）
      run: python scripts/release/location_bot.py --job check_location
      # 此步骤将在定时触发时运行每小时检查
      if: github.event.schedule == '0 3-15 * * 1-5' # 匹配每小时的cron安排

    - name: 提醒开始共享实时位置
      run: python scripts/release/location_bot.py --job start_sharing_message
      if: github.event.schedule == '0 3 * * 3' # 匹配周三上午11点SGT的cron

    - name: 提醒停止共享实时位置
      run: python scripts/release/location_bot.py --job stop_sharing_message
      if: github.event.schedule == '0 15 * * 5' # 匹配周五晚上11点SGT的cron

    - name: 运行Telegram脚本发送测试消息（手动触发）
      run: python scripts/release/location_bot.py --job send_message --message "这是来自GitHub Actions的手动触发测试消息。"
      if: github.event_name == 'workflow_dispatch'

    - name: 运行Telegram脚本推送到主分支
      run: python scripts/release/location_bot.py --job send_message --message "位置机器人的代码更改已推送到主分支。"
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
import time # 用于潜在的未来持续监控

load_dotenv()

# 新增：位置机器人的特定API密钥
TELEGRAM_LOCATION_BOT_API_KEY = os.environ.get("TELEGRAM_LOCATION_BOT_API_KEY") # 确保在你的.env中设置了此项
TELEGRAM_CHAT_ID = "610574272" # 此聊天ID用于发送通知消息

# 定义你的办公室坐标
OFFICE_LATITUDE = 23.135368
OFFICE_LONGITUDE = 113.32952

# 邻近半径（米）
PROXIMITY_RADIUS_METERS = 300

def send_telegram_message(bot_token, chat_id, message):
    """使用Telegram Bot API向Telegram聊天发送消息。"""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown" # 使用Markdown以在消息中使用粗体
    }
    response = requests.post(url, params=params)
    if response.status_code != 200:
        print(f"发送Telegram消息时出错: {response.status_code} - {response.text}")

def get_latest_location(bot_token):
    """从机器人获取最新的实时位置更新。"""
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    # 偏移量以获取最后处理后的新更新（用于持续轮询）
    # 对于简单的一次性脚本，我们只获取最新的，但对于轮询，你会管理一个偏移量。
    params = {"offset": -1} # 获取最新的更新
    response = requests.get(url, params=params)
    print("GetUpdates响应:", response) # 调试
    if response.status_code == 200:
        updates = response.json()
        print("GetUpdates JSON:", json.dumps(updates, indent=4)) # 调试
        if updates['result']:
            last_update = updates['result'][-1]
            # 优先处理编辑后的消息以获取实时位置
            if 'edited_message' in last_update and 'location' in last_update['edited_message']:
                return last_update['edited_message']['location'], last_update['edited_message']['chat']['id']
            elif 'message' in last_update and 'location' in last_update['message']:
                # 处理初始实时位置消息或静态位置共享
                return last_update['message']['location'], last_update['message']['chat']['id']
    return None, None

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    使用Haversine公式计算地球上两点之间的距离。
    返回米为单位的距离。
    """
    R = 6371000  # 地球半径（米）

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
    parser = argparse.ArgumentParser(description="Telegram机器人脚本")
    # 更新--job参数的选项
    parser.add_argument('--job', choices=['get_chat_id', 'send_message', 'check_location', 'start_sharing_message', 'stop_sharing_message'], required=True, help="要执行的任务")
    # 为'send_message'任务添加--message参数
    parser.add_argument('--message', type=str, help="为'send_message'任务发送的消息")
    # 为'check_location'任务添加--test参数
    parser.add_argument('--test', action='store_true', help="对于'check_location'任务，无论邻近情况都强制发送消息。")
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
                    print("无法从最后的更新中检索到聊天ID。")
            else:
                print("未找到更新。")
        else:
            print(f"获取更新时出错: {response.status_code} - {response.text}")

    elif args.job == 'send_message':
        if TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = args.message if args.message else "这是来自你的Telegram机器人脚本的默认测试消息！"
            send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print(f"消息发送成功: {message}")
        else:
            print("TELEGRAM_LOCATION_BOT_API_KEY和TELEGRAM_CHAT_ID未设置。")

    elif args.job == 'start_sharing_message':
        if TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = "⚠️ *提醒:* 请开始向机器人共享你的实时位置！"
            send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print("已发送开始共享提醒。")
        else:
            print("TELEGRAM_LOCATION_BOT_API_KEY和TELEGRAM_CHAT_ID未设置。")

    elif args.job == 'stop_sharing_message':
        if TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = "✅ *提醒:* 你现在可以停止共享实时位置了。"
            send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print("已发送停止共享提醒。")
        else:
            print("TELEGRAM_LOCATION_BOT_API_KEY和TELEGRAM_CHAT_ID未设置。")

    elif args.job == 'check_location':
        if not TELEGRAM_LOCATION_BOT_API_KEY or not TELEGRAM_CHAT_ID:
            print("位置检查需要设置TELEGRAM_LOCATION_BOT_API_KEY和TELEGRAM_CHAT_ID。")
            return

        user_location, location_chat_id = get_latest_location(TELEGRAM_LOCATION_BOT_API_KEY)

        if user_location:
            current_latitude = user_location['latitude']
            current_longitude = user_location['longitude']

            distance = haversine_distance(
                OFFICE_LATITUDE, OFFICE_LONGITUDE,
                current_latitude, current_longitude
            )

            print(f"当前位置: ({current_latitude}, {current_longitude})")
            print(f"距离办公室: {distance:.2f}米")

            needs_punch_card = distance <= PROXIMITY_RADIUS_METERS

            if needs_punch_card:
                print(f"你在办公室周围{PROXIMITY_RADIUS_METERS}m内！")
                notification_message = (
                    f"🎉 *已到达办公室!* 🎉\n"
                    f"现在可以在企业微信中打卡了。\n"
                    f"你当前距离办公室: {distance:.2f}m."
                )
            else:
                print(f"你在办公室周围{PROXIMITY_RADIUS_METERS}m之外。")
                # 当超出半径时的消息
                notification_message = (
                    f"📍 你*不在*办公室邻近范围内（{PROXIMITY_RADIUS_METERS}m）。\n"
                    f"现在不需要打卡。\n"
                    f"你当前距离办公室: {distance:.2f}m."
                )

            # 如果在邻近范围内或使用了--test标志，则发送消息
            if needs_punch_card or args.test:
                send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, notification_message)
            else:
                # 如果不在邻近范围内且不在测试模式下，仅打印到控制台（不发送Telegram消息）
                print("不在邻近范围内且不在测试模式下，未向Telegram发送消息。")
        else:
            print("无法获取你的最新位置。请确保你已向机器人共享实时位置。")

if __name__ == '__main__':
    main()
```

---

更新：这不太好，因为你需要向机器人共享你的实时位置。