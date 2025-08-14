---
audio: false
generated: false
image: false
lang: hant
layout: post
title: 搜索 Tavily AI 使用 API
translated: true
---

[Tavily](https://tavily.com)是一款專為LLM應用而設計的AI搜索API，它通过结合網路搜索和AI處理提供高度相關的搜索結果。

使用Tavily需要：

1. 前往[ Tavily.com](https://tavily.com)註冊獲取API金鑰
2. 安裝Python套件

```python
import os
from tavily import TavilyClient

# 從環境變量中獲取API金鑰
TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')

if TAVILY_API_KEY is None:
    raise ValueError("未找到API金鑰。請設定TAVILY_API_KEY環境變量。")

# 使用獲取的API金鑰初始化TavilyClient
tavily_client = TavilyClient(api_key=TAVILY_API_KEY)

# 提交搜索請求
response = tavily_client.search("誰是利奧·梅西？")

# 打印響應
print(response)
```