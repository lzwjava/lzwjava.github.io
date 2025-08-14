---
audio: false
generated: false
image: false
lang: hant
layout: post
title: 探索人工智能搜索API：Jina AI與Tavily整合
translated: true
---

### Jina AI

這個Python腳本使用API金鑰和命令列參數與Jina AI服務互動。它支援兩個主要工作：從URL獲取內容和執行搜尋查詢。腳本從環境變數中獲取Jina API金鑰，確保安全地存取服務。它使用`requests`庫進行HTTP請求和`base64`解碼搜尋查詢。然後，它會印出來自Jina AI服務的響應。

```python
import os
import requests
from dotenv import load_dotenv
import argparse
import base64

load_dotenv()

api_key = os.environ.get("JINA_API_KEY")
if not api_key:
    raise ValueError("JINA_API_KEY環境變量未設置。")

parser = argparse.ArgumentParser()
parser.add_argument("--job", type=str, choices=['url', 'search'], helfen="要執行的工作（url或搜尋）",required=True)
parser.add_argument("--input", type=str, helfen="工作的輸入", required=True)
args = parser.parse_args()

if args.job == 'url':
    url = f'https://r.jina.ai/{args.input}'
    headers = {'Authorization': f'Bearer {api_key}'}
    print(f"URL: {url}")
    print(f"Headers: {headers}")
    response = requests.get(url, headers=headers)
    print(response.text)

elif args.job == 'search':
    question = base64.b64decode(args.input).decode('utf-8', errors='ignore')
    url = f'https://s.jina.ai/{question}'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'X-Engine': 'direct',
        'X-Retain-Images': 'none'
    }
    print(f"URL: {url}")
    print(f"Headers: {headers}")
    response = requests.get(url, headers=headers)
    print(response.text)

else:
    print("請指定--job url或--job搜尋")

```

---

## Tavily AI

[Tavily](https://tavily.com)是一款專門為LLM應用程序設計的AI搜尋API，它通過結合網路搜尋和AI處理提供高度相關的搜尋結果。

要使用Tavily，您需要：

1. 在[tavily.com](https://tavily.com)註冊API金鑰
2. 安裝Python套件。

```python
import os
from tavily import TavilyClient

# 從環境變量中獲取API金鑰
TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')

if TAVILY_API_KEY is None:
    raise ValueError("未找到API金鑰。請設定TAVILY_API_KEY環境變量。")

# 用獲取的API金鑰初始化TavilyClient
tavily_client = TavilyClient(api_key=TAVILY_API_KEY)

# 執行搜尋請求
response = tavily_client.search("Who is Leo Messi?")

# 印出響應
print(response)

```