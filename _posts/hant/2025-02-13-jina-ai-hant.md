---
audio: false
generated: false
image: false
lang: hant
layout: post
title: 探索 AI 搜尋 API：Jina AI 與 Tavily 整合應用
translated: true
---

### 目錄

1. [Jina AI](#jina-ai)
   - Jina AI 整合的 Python 脚本
   - 使用 `r.jina.ai` 抓取網址內容
   - 使用 `s.jina.ai` 處理搜尋查詢
   - Base64 編碼與 API 驗證

2. [Tavily AI](#tavily-ai)
   - 專為 LLM 應用設計的 AI 搜尋 API
   - 設定與 API 金鑰註冊
   - Python 客戶端實現
   - 搜尋請求範例與用法

3. [Open WebUI](#open-webui)
   - 本地 AI 介面安裝
   - 伺服器設定與配置
   - Ollama 本地模型整合
   - 安裝時間與需求

4. [Tableau、Scale 和 Power BI](#tableau-scale-和-power-bi)
   - 商業智能平台比較
   - Tableau 13 天試用體驗
   - Scale 資料平台概覽
   - Microsoft Power BI 功能

5. [使用 OpenRouter](#使用-openrouter)
   - 接受中國簽發的 Visa 信用卡付款
   - 模型排名與熱門趨勢分析
   - LLM 使用類別與應用
   - 香港用戶存取 Anthropic API 需使用 VPN

## Jina AI

此 Python 脚本透過 API 金鑰和命令列參數與 Jina AI 服務互動。它支援兩項主要功能：從網址抓取內容和執行搜尋查詢。脚本從環境變數中獲取 Jina API 金鑰，確保安全存取服務。它使用 `requests` 函式庫發送 HTTP 請求，並使用 `base64` 解碼搜尋查詢。最後，脚本會列印 Jina AI 服務的回應。

```python
import os
import requests
from dotenv import load_dotenv
import argparse
import base64

load_dotenv()

api_key = os.environ.get("JINA_API_KEY")
if not api_key:
    raise ValueError("未設定 JINA_API_KEY 環境變數。")

parser = argparse.ArgumentParser()
parser.add_argument("--job", type=str, choices=['url', 'search'], help="要執行的工作（url 或 search）", required=True)
parser.add_argument("--input", type=str, help="工作的輸入內容", required=True)
args = parser.parse_args()

if args.job == 'url':
    url = f'https://r.jina.ai/{args.input}'
    headers = {'Authorization': f'Bearer {api_key}'}
    print(f"網址：{url}")
    print(f"標頭：{headers}")
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
    print(f"網址：{url}")
    print(f"標頭：{headers}")
    response = requests.get(url, headers=headers)
    print(response.text)

else:
    print("請指定 --job url 或 --job search")

```

---

## Tavily AI

[Tavily](https://tavily.com) 是一個專為 LLM 應用設計的 AI 搜尋 API，透過結合網頁搜尋與 AI 處理，提供高度相關的搜尋結果。

要使用 Tavily，你需要：

1. 在 [tavily.com](https://tavily.com) 註冊取得 API 金鑰
2. 安裝 Python 套件。

```python
import os
from tavily import TavilyClient

# 從環境變數中獲取 API 金鑰
TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')

if TAVILY_API_KEY is None:
    raise ValueError("未找到 API 金鑰。請設定 TAVILY_API_KEY 環境變數。")

# 用獲取的 API 金鑰初始化 TavilyClient
tavily_client = TavilyClient(api_key=TAVILY_API_KEY)

# 發送搜尋請求
response = tavily_client.search("誰是 Lionel Messi？")

# 列印回應
print(response)

```

---

## Open WebUI

- Open WebUI 是一個優秀的工具。
- 要啟動伺服器，請執行以下指令：`pip install open-webui` 及 `open-webui serve`。
- 安裝過程可能需要一些時間（約 10 分鐘或以上）。
- Open WebUI 與 Ollama 配合良好。

---

## Tableau、Scale 和 Power BI

### Tableau

[https://tableau.com](https://tableau.com)

註冊後，獲知有 13 天試用期。

{: .centered }
![](assets/images/tsp/tableau.jpg)
*來源：tableau.com*{: .caption }

### Scale

[https://scale.com](https://scale.com)

{: .centered }
![](assets/images/tsp/scale.jpg)
*來源：scale.com*{: .caption }

### Power BI

[https://powerbi.microsoft.com](https://powerbi.microsoft.com)

---

## 使用 OpenRouter

- 接受中國簽發的 Visa 信用卡付款。
- 「排名」頁面可查看最熱門和趨勢模型，非常有趣。
- 可查看用戶如何在角色扮演、編程、行銷、行銷/SEO 和科技等類別中使用 LLM 模型。
- 香港用戶存取 Anthropic API 仍需使用 VPN。