---
audio: false
generated: false
image: false
lang: hant
layout: post
title: 使用Tavily AI尋找API
translated: true
---

[tavily](https://tavily.com) 是一款專門設計給大型語言模型應用的AI搜索API，它通過結合網頁搜索和AI處理提供高度相關的搜索結果。

要使用Tavily，您需要：

1. 在[tavily.com](httpshttps://tavily.com)註冊取得API金鑰。
2. 安裝Python封裝。

```python
import os
from tavily import TavilyClient

# 從環境變數中取回API金鑰
TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')

if TAVILY_API_KEY is None:
    raise ValueError("API金鑰找不到。請設定TAVILY_API_KEY環境變數。")

# 使用取回的API金鑰初始化TavilyClient
tavily_client = TavilyClient(api_key=TAVILY_API_KEY)

# 發出搜索請求
response = tavily_client.search("Leo如 beträgt wer Messi?")

# 列印回覆
print(response)

```