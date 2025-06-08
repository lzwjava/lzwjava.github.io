---
audio: false
generated: false
lang: hant
layout: post
title: 自動化新聞摘要機械人
translated: true
---

這篇貼文展示了一個基於Python的新聞機器人，它利用Mistral API從Hacker News、GitHub Trending和紐約時報（中文版）抓取並摘要頂尖新聞。該機器人會透過Telegram發送簡潔的每日報告，並透過GitHub Actions工作流程實現自動化執行。這是一個輕鬆追蹤科技與全球新聞的理想工具。以下是每日新聞摘要的範例。

---

每日新聞摘要 - 2025-06-07

Hacker News
-----------
1. 網頁顯示Facebook與當前瀏覽器不相容，建議更新至支援的瀏覽器以繼續使用服務。

2. 盧旺達的仇恨電台使用暗語煽動聽眾殺害圖西族人，從而引發種族滅絕。

3. Railway推出Railpack以取代Nixpacks，旨在解決阻礙20萬用戶的擴展性和依賴管理問題，實現更平順的過渡以支援1億用戶。

4. 文章深入探討Radiant AI的遺產，這是一個曾承諾用於《上古卷軸IV：湮沒》但最終被大幅刪減的爭議性且雄心勃勃的AI系統。

5. 《華盛頓郵報》建議用戶停止使用Chrome並刪除Meta的應用程式以增強隱私。


GitHub Trending
---------------
1. Cognee透過可擴展的模組化ECL管道，僅用五行代碼即可為AI代理創建動態記憶體。

2. NetBird結合基於WireGuard的點對點覆蓋網絡與集中式細粒度存取控制，簡化了安全私密網絡的建立。

3. NoteGen是一款AI驅動的跨平台Markdown筆記應用，整合錄音與書寫功能，將零散知識組織成連貫筆記。

4. Scrapy是一個快速、高階的Python網頁爬取框架，專為從網站提取結構化數據而設計。

5. React Bits提供免費開源的動畫化、互動式且可自訂的React元件集合，以增強網頁介面。


紐約時報（中文版）
-----------------
1. 中國國家主席習近平與美國總統特朗普通話後，雙方同意進一步貿易談判以緩解關稅和稀土供應的緊張局勢。

2. 中國近期的爭議凸顯了公眾對社會不平等現象的普遍不滿，以及認為成功往往取決於人脈而非能力的觀點。

3. 中國加強打擊稀土金屬走私，導致全球產業供應嚴重中斷，北京正收緊管制以將這些關鍵資源作為戰略工具。

4. 特朗普與馬斯克之間不斷升級的衝突可能帶來重大影響，兩位人物正利用各自的影響力和資源相互抗衡。

5. 中國暫停出口七種稀土金屬及其磁鐵，導致美國和歐洲可能出現工廠關閉的嚴重短缺情況。

---

```python
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import datetime
import sys
import re
import time

load_dotenv()

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_API_KEY")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "610574272")
MISTRAL_API_KEY = os.environ.get("MISTRAL_API_KEY")

TELEGRAM_MAX_LENGTH = 4096

def send_telegram_message(message):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("錯誤：未設置TELEGRAM_BOT_API_KEY或TELEGRAM_CHAT_ID。")
        return False
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    url_pattern = re.compile(r'(https?://[^\s]+)')
    # 移除所有星號（用於粗體/斜體）
    message_no_stars = message.replace('*', '')
    # 移除訊息中的連結
    message_no_links = url_pattern.sub('', message_no_stars)
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
            "chat_id": TELEGRAM_CHAT_ID,
            "text": part,
        }
        try:
            response = requests.post(url, params=params)
            response.raise_for_status()
            print(f"成功發送Telegram訊息部分（{len(part)}字符）。")
        except requests.exceptions.RequestException as e:
            print(f"發送Telegram訊息時出錯：{e}")
            success = False
    return success

def fetch_html_content(url):
    try:
        print(f"從以下網址獲取HTML內容：{url}")
        response = requests.get(url, timeout=15, verify=False)
        response.raise_for_status()
        print(f"成功從以下網址獲取HTML內容：{url}")
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"無法獲取URL：{url} - {e}")
        return None

def extract_hacker_news_links(html, max_links=5):
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    seen = set()
    for item in soup.select('.titleline > a'):
        url = item['href']
        title = item.text.strip()
        if url.startswith('item?id='):
            url = f"https://news.ycombinator.com/{url}"
        if url not in seen and title:
            links.append({'url': url, 'text': title})
            seen.add(url)
        if len(links) >= max_links:
            break
    print(f"從Hacker News提取了{len(links)}個連結。")
    return links

def extract_github_trending(html, max_links=5):
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for repo in soup.select('article.Box-row h2 a'):
        url = f"https://github.com{repo['href']}"
        title = re.sub(r'\s+', ' ', repo.text).strip()
        if title and url:
            links.append({'url': url, 'text': title})
        if len(links) >= max_links:
            break
    print(f"從GitHub提取了{len(links)}個熱門儲存庫。")
    return links

def call_mistral_api(prompt, model="mistral-small-latest"):
    api_key = MISTRAL_API_KEY
    if not api_key:
        print("錯誤：未設置MISTRAL_API_KEY環境變量。")
        return None

    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    try:
        print(f"使用模型調用Mistral API：{model}")
        print(f"發送的提示：{prompt[:1000]}...")
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        print(f"Mistral API回應：{response_json}")
        if response_json and response_json.get('choices'):
            content = response_json['choices'][0]['message']['content']
            print(f"Mistral API內容：{content}")
            return content
        else:
            print(f"Mistral API錯誤：無效的回應格式：{response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Mistral API錯誤：{e}")
        if hasattr(e, "response") and e.response is not None:
            print(f"回應狀態碼：{e.response.status_code}")
            print(f"回應內容：{e.response.text}")
        return None

def fetch_and_summarize(url, fallback_title=None):
    print(f"摘要：{url}")
    html = fetch_html_content(url)
    if not html:
        return {"url": url, "summary": "無法獲取內容。", "title": fallback_title or url}
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.title.text.strip() if soup.title else (fallback_title or url)
    paragraphs = soup.find_all('p')
    text_content = "\n".join(p.get_text() for p in paragraphs)
    if not text_content or len(text_content) < 100:
        text_content = soup.get_text(separator="\n")
    text_content = text_content.strip()
    if len(text_content) > 3000:
        text_content = text_content[:3000]
    summary = ai_summarize(text_content, url, title)
    return {"url": url, "summary": summary, "title": title}

def limit_to_n_words(text, n):
    words = text.strip().split()
    if len(words) <= n:
        return text.strip()
    return ' '.join(words[:n]) + "..."

def ai_summarize(text, url=None, title=None):
    if not MISTRAL_API_KEY:
        print("未設置MISTRAL_API_KEY。返回前15個字作為摘要。")
        return limit_to_n_words(text, 15)
    prompt = (
        "如果原文是中文，請用英文摘要。"
        "用清晰簡潔的英文摘要以下網頁內容。"
        "聚焦於單一最重要的觀點或見解。"
        "摘要應約300字符。"
        "僅輸出摘要句子：\n"
        f"標題：{title if title else ''}\n"
        f"{text}\n"
        f"{'原始連結：' + url if url else ''}"
    )
    summary = call_mistral_api(prompt)
    if summary is None:
        return limit_to_n_words(text, 15)
    # 最後截斷至300字符
    return summary.strip()[:300]

def generate_summarized_report(summaries, source_name):
    text = f"{source_name}\n"
    text += "-" * len(source_name) + "\n"
    if not summaries:
        text += "未找到項目。\n\n"
        return text
    url_pattern = re.compile(r'(https?://[^\s]+)')
    for idx, item in enumerate(summaries, 1):
        summary = item.get('summary', '').replace('\n', ' ').replace('\r', ').strip()
        summary = summary.replace('*', '')
        summary = url_pattern.sub('', summary)
        # 最後將每個摘要截斷至300字符
        summary = summary[:300]
        text += f"{idx}. {summary}\n\n"  # 在摘要之間添加額外換行
    text += "\n"
    return text

# --- 紐約時報（m.cn.nytimes.com）整合 ---

def extract_nytimes_links(html, max_links=5):
    """
    從cn.nytimes.com的首頁提取連結。
    僅包含以'https://cn.nytimes.com/'開頭的連結。
    """
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for a in soup.find_all('a', href=True):
        url = a['href']
        if url.startswith('https://cn.nytimes.com/'):
            links.append({
                'url': url,
                'text': a.text.strip()
            })
        if len(links) >= max_links:
            break
    print(f"從首頁提取了{len(links)}個連結。")
    return links

def summarize_nytimes_article(url):
    html = fetch_html_content(url)
    if not html:
        return {"url": url, "summary": "無法獲取內容。", "title": url}
    soup = BeautifulSoup(html, 'html.parser')
    # 嘗試提取文章主標題
    title_element = soup.select_one('.article-area .article-content .article-header header h1')
    title = title_element.text.strip() if title_element else (soup.title.text.strip() if soup.title else url)
    # 提取文章正文
    article_area = soup.find('section', class_='article-body')
    if article_area:
        article_text = article_area.get_text(separator='\n', strip=True)
    else:
        article_text = soup.get_text(separator='\n', strip=True)
    if not article_text or len(article_text) < 100:
        article_text = soup.get_text(separator='\n', strip=True)
    if len(article_text) > 3000:
        article_text = article_text[:3000]
    summary = ai_summarize(article_text, url, title)
    return {"url": url, "summary": summary, "title": title}

def main():
    # 檢查是否有--test參數
    is_test = "--test" in sys.argv

    today = datetime.datetime.now().strftime("%Y-%m-%d")
    report = f"每日新聞摘要 - {today}\n\n"

    if is_test:
        # 僅爬取一個連結並發送一個摘要（紐約時報中文版）
        ny_html = fetch_html_content('https://m.cn.nytimes.com')
        ny_links = []
        ny_summaries = []
        if ny_html:
            ny_links = extract_nytimes_links(ny_html, max_links=1)
            if ny_links:
                link = ny_links[0]
                summary = summarize_nytimes_article(link['url'])
                ny_summaries.append(summary)
        report = generate_summarized_report(ny_summaries, "紐約時報（中文版）")
        if ny_summaries:
            if send_telegram_message(report):
                print("測試摘要成功發送至Telegram。")
                sys.exit(0)
            else:
                print("發送測試摘要至Telegram失敗。")
                sys.exit(1)
        else:
            print("未收集到新聞，未發送任何內容至Telegram。")
            sys.exit(1)
    else:
        # --- Hacker News ---
        hn_html = fetch_html_content('https://news.ycombinator.com')
        hn_links = []
        hn_summaries = []
        if hn_html:
            hn_links = extract_hacker_news_links(hn_html)
            for link in hn_links:
                summary = fetch_and_summarize(link['url'], fallback_title=link['text'])
                hn_summaries.append(summary)
                time.sleep(2)
        report += generate_summarized_report(hn_summaries, "Hacker News")

        # --- GitHub Trending ---
        gh_html = fetch_html_content('https://github.com/trending')
        gh_links = []
        gh_summaries = []
        if gh_html:
            gh_links = extract_github_trending(gh_html)
            for link in gh_links:
                summary = fetch_and_summarize(link['url'], fallback_title=link['text'])
                gh_summaries.append(summary)
                time.sleep(2)
        report += generate_summarized_report(gh_summaries, "GitHub Trending")

        # --- 紐約時報（cn.nytimes.com） ---
        ny_html = fetch_html_content('https://m.cn.nytimes.com')
        ny_links = []
        ny_summaries = []
        if ny_html:
            ny_links = extract_nytimes_links(ny_html, max_links=5)
            for link in ny_links:
                summary = summarize_nytimes_article(link['url'])
                ny_summaries.append(summary)
                time.sleep(2)
        report += generate_summarized_report(ny_summaries, "紐約時報（中文版）")

        if any([hn_summaries, gh_summaries, ny_summaries]):
            if len(report) > TELEGRAM_MAX_LENGTH:
                print(f"報告超過{TELEGRAM_MAX_LENGTH}字符，將分割為多條訊息。")
            if send_telegram_message(report):
                print("每日新聞報告成功發送至Telegram。")
                sys.exit(0)
            else:
                print("發送每日新聞報告至Telegram失敗。")
                sys.exit(1)
        else:
            print("未收集到新聞，未發送任何內容至Telegram。")
            sys.exit(1)

if __name__ == "__main__":
    main()
```

```yml
name: 新聞機器人

on:
  schedule:
    # 每天北京時間上午9點（UTC時間凌晨1點）運行。
    - cron: '0 1 * * *'
  workflow_dispatch:  # 允許手動觸發
  push:
    # 僅當兩個文件在同一提交/推送中更改時觸發
    # 這需要下面的過濾工作來檢查兩個文件
    paths:
      - scripts/nytimes/news_bot.py
      - .github/workflows/news.yml

concurrency:
  group: 'news'
  cancel-in-progress: false

jobs:
  send-news:
    runs-on: ubuntu-latest
    environment: github-pages
    env:
      TELEGRAM_BOT_API_KEY: ${{ secrets.TELEGRAM_BOT_API_KEY }}
      MISTRAL_API_KEY: ${{ secrets.MISTRAL_API_KEY }}    

    steps:
      - name: 檢出儲存庫
        uses: actions/checkout@v4
        with:
          fetch-depth: 5

      - name: 設置Python 3.10.x
        uses: actions/setup-python@v4
        with:
          python-version: "3.10.x"

      - name: 安裝依賴
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.simple.txt

      - name: 運行新聞機器人腳本
        run: python scripts/nytimes/news_bot.py
              
```