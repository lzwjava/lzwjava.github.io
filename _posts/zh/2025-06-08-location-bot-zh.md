---
audio: false
generated: false
lang: zh
layout: post
title: 用Telegram定位机器人自动化打卡
translated: true
---

是否曾希望每日的“打卡”不再那么繁琐？我深有同感。为此，我开发了一个基于位置追踪的Telegram个人机器人，它能自动发送到岗通知并提醒我关键签到。本文将分享如何用Python结合GitHub Actions打造这套无感化系统，让我在需要时精准接收位置触发的提醒。

```yml
name: 每小时位置检查

on:
  schedule:
    # 每周一至周五，每小时整点执行（新加坡时间上午11点至晚上11点）
    # UTC时间需换算：新加坡时间（SGT）为UTC+8
    # 故11 AM SGT对应03:00 UTC，11 PM SGT对应15:00 UTC
    - cron: '0 3-15 * * 1-5'

    # 每周三11 AM SGT提醒开启实时位置共享（3 AM UTC）
    - cron: '0 3 * * 3' # 3表示周三

    # 每周五11 PM SGT提醒关闭实时位置共享（3 PM UTC）
    - cron: '0 15 * * 5' # 5表示周五

  workflow_dispatch:  # 支持手动触发工作流
  push:
    branches: ["main"]
    paths:
      - 'scripts/release/location_bot.py' # 脚本路径
      - '.github/workflows/location.yml' # 工作流文件路径

concurrency:
  group: 'location'
  cancel-in-progress: false

jobs:
  检查与通知:
    runs-on: ubuntu-latest
    env:
      TELEGRAM_LOCATION_BOT_API_KEY: ${{ secrets.TELEGRAM_LOCATION_BOT_API_KEY }}

    steps:
    - name: 检出代码库
      uses: actions/checkout@v4
      with:
        fetch-depth: 5 # 仅获取最近5次提交以提高效率

    - name: 配置Python 3.13.2
      uses: actions/setup-python@v4
      with:
        python-version: "3.13.2" # 指定Python版本

    - name: 安装依赖
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.simple.txt 

    - name: 执行位置检查脚本（定时任务）
      run: python scripts/release/location_bot.py --job check_location
      if: github.event.schedule == '0 3-15 * * 1-5' # 匹配每小时定时任务

    - name: 发送开启位置共享提醒
      run: python scripts/release/location_bot.py --job start_sharing_message
      if: github.event.schedule == '0 3 * * 3' # 匹配周三11 AM SGT

    - name: 发送关闭位置共享提醒
      run: python scripts/release/location_bot.py --job stop_sharing_message
      if: github.event.schedule == '0 15 * * 5' # 匹配周五11 PM SGT

    - name: 手动触发测试消息
      run: python scripts/release/location_bot.py --job send_message --message "这是来自GitHub Actions的手动触发测试消息"
      if: github.event_name == 'workflow_dispatch'

    - name: 主分支推送通知
      run: python scripts/release/location_bot.py --job send_message --message "位置机器人代码已推送至主分支"
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
import time

load_dotenv()

# 定位机器人专用API密钥
TELEGRAM_LOCATION_BOT_API_KEY = os.environ.get("TELEGRAM_LOCATION_BOT_API_KEY")
TELEGRAM_CHAT_ID = "610574272" # 通知消息接收的聊天ID

# 办公室坐标
OFFICE_LATITUDE = 23.135368
OFFICE_LONGITUDE = 113.32952

# 签到半径（米）
PROXIMITY_RADIUS_METERS = 300

def send_telegram_message(bot_token, chat_id, message):
    """通过Telegram Bot API发送消息"""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown" # 使用Markdown加粗文本
    }
    response = requests.post(url, params=params)
    if response.status_code != 200:
        print(f"发送Telegram消息失败: {response.status_code} - {response.text}")

def get_latest_location(bot_token):
    """获取最新的实时位置更新"""
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    params = {"offset": -1} # 获取最后一条更新
    response = requests.get(url, params=params)
    print("获取更新响应:", response) # 调试日志
    if response.status_code == 200:
        updates = response.json()
        print("更新数据:", json.dumps(updates, indent=4)) # 调试日志
        if updates['result']:
            last_update = updates['result'][-1]
            if 'edited_message' in last_update and 'location' in last_update['edited_message']:
                return last_update['edited_message']['location'], last_update['edited_message']['chat']['id']
            elif 'message' in last_update and 'location' in last_update['message']:
                return last_update['message']['location'], last_update['message']['chat']['id']
    return None, None

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    使用Haversine公式计算地球表面两点距离
    返回单位为米
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
    parser.add_argument('--job', choices=['get_chat_id', 'send_message', 'check_location', 'start_sharing_message', 'stop_sharing_message'], required=True, help="执行任务类型")
    parser.add_argument('--message', type=str, help="发送消息任务的内容")
    parser.add_argument('--test', action='store_true', help="测试模式：无论距离都发送消息")
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
                    print("无法从最后更新中获取聊天ID")
            else:
                print("未找到更新记录")
        else:
            print(f"获取更新失败: {response.status_code} - {response.text}")

    elif args.job == 'send_message':
        if TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = args.message if args.message else "这是来自Telegram机器人脚本的默认测试消息！"
            send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print(f"消息发送成功: {message}")
        else:
            print("未设置TELEGRAM_LOCATION_BOT_API_KEY或TELEGRAM_CHAT_ID")

    elif args.job == 'start_sharing_message':
        if TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = "⚠️ *提醒：* 请开始向机器人共享实时位置！"
            send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print("已发送开启共享提醒")
        else:
            print("未设置TELEGRAM_LOCATION_BOT_API_KEY或TELEGRAM_CHAT_ID")

    elif args.job == 'stop_sharing_message':
        if TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = "✅ *提醒：* 现在可以停止共享实时位置了"
            send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print("已发送停止共享提醒")
        else:
            print("未设置TELEGRAM_LOCATION_BOT_API_KEY或TELEGRAM_CHAT_ID")

    elif args.job == 'check_location':
        if not TELEGRAM_LOCATION_BOT_API_KEY or not TELEGRAM_CHAT_ID:
            print("位置检查需要设置TELEGRAM_LOCATION_BOT_API_KEY和TELEGRAM_CHAT_ID")
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
            print(f"距离办公室: {distance:.2f} 米")

            needs_punch_card = distance <= PROXIMITY_RADIUS_METERS

            if needs_punch_card:
                print(f"您位于办公室{PROXIMITY_RADIUS_METERS}米范围内！")
                notification_message = (
                    f"🎉 *已到达办公室!* 🎉\n"
                    f"请及时在企业微信打卡\n"
                    f"当前距离: {distance:.2f}米"
                )
            else:
                print(f"您位于办公室{PROXIMITY_RADIUS_METERS}米范围外")
                notification_message = (
                    f"📍 您当前*不在*办公室附近（{PROXIMITY_RADIUS_METERS}米）\n"
                    f"无需此时打卡\n"
                    f"当前距离: {distance:.2f}米"
                )

            if needs_punch_card or args.test:
                send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, notification_message)
            else:
                print("非测试模式且未进入范围，不发送Telegram消息")
        else:
            print("无法获取最新位置，请确认已向机器人共享实时位置")

if __name__ == '__main__':
    main()
```