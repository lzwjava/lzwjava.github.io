---
audio: false
generated: false
lang: hant
layout: post
title: 用Mistral打造習慣養成機器人
translated: true
---

在這篇博客文章中，我們探討如何創建一個習慣機器人，利用Python和GitHub Actions發送自動提醒。這個機器人運用Telegram API進行訊息傳遞，並整合Mistral AI來生成情境相關的提示。透過GitHub Actions排程任務，機器人能夠適時發送通知，鼓勵養成持續的習慣。我們將逐步介紹從環境配置到腳本編寫及部署的整個設置過程，為自動化你的習慣追蹤系統提供實用指南。

## 代碼

```python
import os
import requests
import argparse
import re
import datetime
from dotenv import load_dotenv
import random

# 從.env檔案載入環境變數
load_dotenv()

# 環境變數
TELEGRAM_HABIT_BOT_API_KEY = os.environ.get("TELEGRAM_HABIT_BOT_API_KEY")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
MISTRAL_API_KEY = os.environ.get("MISTRAL_API_KEY")

# Telegram訊息長度限制
TELEGRAM_MAX_LENGTH = 4096

def send_telegram_message(bot_token, chat_id, message):
    """使用Telegram Bot API發送訊息到Telegram聊天室。"""
    if not bot_token or not chat_id:
        print("錯誤：TELEGRAM_HABIT_BOT_API_KEY或TELEGRAM_CHAT_ID未設置。")
        return False
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    # 移除Markdown星號和URL以確保Telegram兼容性
    message_no_stars = message.replace('*', '')
    url_pattern = re.compile(r'(https?://[^\s]+)')
    message_no_links = url_pattern.sub('', message_no_stars)
    # 如果訊息超過Telegram的長度限制，則分割訊息
    messages = []
    msg = message_no_links
    while len(msg) > TELEGRAM_MAX_LENGTH:
        split_idx = msg.rfind('\n', 0, TELEGRAM_MAX_LENGTH)
        if split_idx == -1 or split_idx < TELEGRAM_MAX_LENGTH // 2:
            split_idx = TELEGRAM_MAX_LENGTH
        messages.append(msg[:split_idx])
        msg = msg[split_idx:]
    messages.append(msg)
    success = True
    for part in messages:
        params = {
            "chat_id": chat_id,
            "text": part,
            "parse_mode": "Markdown"
        }
        try:
            response = requests.post(url, params=params)
            response.raise_for_status()
            print(f"成功發送Telegram訊息部分（{len(part)}字元）。")
        except requests.exceptions.RequestException as e:
            print(f"發送Telegram訊息時出錯：{e}")
            success = False
    return success


def call_mistral_api(prompt, model="mistral-large-latest"):
    """調用Mistral API生成回應。"""
    if not MISTRAL_API_KEY:
        print("錯誤：MISTRAL_API_KEY環境變數未設置。")
        return None
    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {MISTRAL_API_KEY}"
    }
    data = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7,  # 調整溫度以控制創造性
        "max_tokens": 300  # 限制回應長度
    }
    try:
        print(f"使用模型調用Mistral API：{model}")
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        if response_json.get('choices'):
            content = response_json['choices'][0]['message']['content']
            print(f"Mistral API內容：{content}")
            return content
        print(f"Mistral API錯誤：{e}")
        return None

def generate_copilot_message():
    """通過Mistral API生成鼓勵使用Copilot的技術提示句子。"""
    prompt = (
        f"為後端工程師生成一個獨特、具體的技術提示句子"
        "隨機選擇以下一項技術：Java、Spring Boot、Control-M、IBM WebSphere、Maven、多線程、Nexus、Windows、JVM、Service-NOW、Python、AI或DevOps、Linux。算法和銀行業 "
        "格式為'卡在[具體挑戰]？問問Copilot！'或'在[任務]上遇到困難？找Copilot幫忙！' "
        "確保挑戰多樣化（例如配置、調試、優化）。 "
        "保持句子在300字元以內，避免使用Markdown或URL，僅輸出句子。"
    )
    message = call_mistral_api(prompt)
    if message:
        return message.strip()[:300]
    return "卡在配置Control-M訂單日期？問問Copilot！"

def main():
    parser = argparse.ArgumentParser(description="Telegram習慣提醒機器人")
    parser.add_argument("--job", choices=["send_reminder", "send_message"], required=True, help="要執行的任務")
    parser.add_argument("--message", type=str, help="'send_message'任務要發送的訊息")
    args = parser.parse_args()

    if args.job == "send_reminder":
        if TELEGRAM_HABIT_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = generate_copilot_message()
            send_telegram_message(TELEGRAM_HABIT_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
        else:
            print("錯誤：TELEGRAM_HABIT_BOT_API_KEY或TELEGRAM_CHAT_ID未設置。")
    elif args.job == "send_message":
        if TELEGRAM_HABIT_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = args.message if args.message else "來自機器人的默認測試訊息！"
            send_telegram_message(TELEGRAM_HABIT_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
        else:
            print("錯誤：TELEGRAM_HABIT_BOT_API_KEY或TELEGRAM_CHAT_ID未設置。")

if __name__ == "__main__":
    main()
```

## GitHub Action

```yaml
name: 習慣

on:
  schedule:
    # 每10分鐘運行一次（每小時的0、10、20、30、40、50分），UTC時間05:00–13:00，週一至週五
    # UTC時間05:00–13:00 = 北京時間13:00–21:00（UTC+8）
    - cron: '0,10,20,30,40,50 5-13 * * 1-5'

  workflow_dispatch:
    # 允許手動觸發測試
    inputs:
      message:
        description: '測試用的自訂訊息（可選）'
        required: false
        default: '來自GitHub Actions的測試訊息。'
      job:
        description: '要運行的任務（可選）'
        required: false
        default: 'send_message'

  push:
    branches: ["main"]
    paths:
      - 'scripts/bot/habit_bot.py'
      - '.github/workflows/habit_reminder.yml'

concurrency:
  group: 'habit_reminder'
  cancel-in-progress: false

jobs:
  habit_reminder_job:
    runs-on: ubuntu-latest
    environment: github-pages
    env:
      TELEGRAM_HABIT_BOT_API_KEY: ${{ secrets.TELEGRAM_HABIT_BOT_API_KEY }}
      TELEGRAM_CHAT_ID: ${{ secrets.TELEGRAM_CHAT_ID }}
      MISTRAL_API_KEY: ${{ secrets.MISTRAL_API_KEY }}

    steps:
      - name: 檢出存儲庫
        uses: actions/checkout@v4
        with:
          fetch-depth: 5

      - name: 設置Python 3.13
        uses: actions/setup-python@v4
        with:
          python-version: "3.13"

      - name: 安裝依賴
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: 運行習慣提醒腳本（排程）
        run: python scripts/bot/habit_bot.py --job send_reminder
        if: github.event_name == 'schedule'

      - name: 運行習慣提醒腳本（手動觸發）
        run: python scripts/bot/habit_bot.py --job ${{ github.event.inputs.job }} --message "${{ github.event.inputs.message }}"
        if: github.event_name == 'workflow_dispatch'

      - name: 推送至主分支時通知
        run: python scripts/bot/habit_bot.py --job send_message --message "習慣機器人的代碼更改已推送至主分支。"
        if: github.event_name == 'push'
```