---
audio: true
generated: false
lang: zh
layout: post
title: 自动新闻摘要机器人
translated: true
---

这篇帖子展示了一个基于Python的新闻机器人，它利用Mistral API从Hacker News、GitHub Trending和《纽约时报》（中文版）抓取并摘要头条新闻，通过Telegram发送简洁的每日报告，并通过GitHub Actions工作流实现自动化执行。是轻松追踪科技和全球新闻的理想工具。以下是一份每日新闻摘要的示例。

---

每日新闻摘要 - 2025-06-07

Hacker News
-----------
1. 网页显示Facebook与当前浏览器不兼容，建议更新至支持的浏览器以继续使用服务。

2. 卢旺达的仇恨电台曾使用暗语煽动听众杀害图西族人，酿成种族灭绝惨剧。

3. Railway推出Railpack替代Nixpacks，旨在解决阻碍20万用户的扩展性和依赖管理问题，为支持1亿用户提供更顺畅的过渡。

4. 文章深入探讨了Radiant AI的遗产，这个为《上古卷轴IV：湮没》承诺开发却最终被大幅删减的争议性AI系统。

5. 《华盛顿邮报》建议用户停用Chrome并删除Meta应用以增强隐私保护。


GitHub Trending
---------------
1. Cognee仅用五行代码即可通过可扩展的模块化ECL管道为AI代理创建动态记忆。

2. NetBird结合点对点WireGuard覆盖网络与集中式细粒度访问控制，简化安全私密网络搭建。

3. NoteGen是跨平台AI驱动的Markdown笔记应用，整合录音与书写功能，将碎片知识组织成连贯笔记。

4. Scrapy是Python快速高效的网络爬虫框架，专为从网站提取结构化数据设计。

5. React Bits提供免费开源的可动画化、交互式及可定制的React组件集合，助力提升网页界面。


纽约时报（中文版）
-----------------
1. 中美两国元首通话后同意就贸易问题进一步磋商，以缓解关税和稀土供应引发的紧张局势。

2. 中国近期争议事件凸显公众对普遍社会不平等现象的挫败感，认为人脉而非能力常决定成功。

3. 中国加强打击稀土金属走私导致全球产业供应链严重中断，北京正收紧管控以将这些关键资源作为战略工具。

4. 特朗普与马斯克不断升级的冲突可能产生重大影响，双方都在动用影响力和资源相互对抗。

5. 中国暂停出口七种稀土金属及其磁体造成严重短缺，可能导致欧美工厂停产。

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
        print("错误：未设置TELEGRAM_BOT_API_KEY或TELEGRAM_CHAT_ID")
        return False
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    url_pattern = re.compile(r'(https?://[^\s]+)')
    # 移除消息中所有星号（用于加粗/斜体）
    message_no_stars = message.replace('*', '')
    # 移除消息中的链接
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
            print(f"成功发送Telegram消息部分（{len(part)}字符）")
        except requests.exceptions.RequestException as e:
            print(f"发送Telegram消息出错：{e}")
            success = False
    return success

def fetch_html_content(url):
    try:
        print(f"正在从{url}获取HTML内容")
        response = requests.get(url, timeout=15, verify=False)
        response.raise_for_status()
        print(f"成功从{url}获取HTML内容")
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"无法获取URL：{url} - {e}")
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
    print(f"从Hacker News提取了{len(links)}条链接")
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
    print(f"从GitHub提取了{len(links)}个热门仓库")
    return links

def call_mistral_api(prompt, model="mistral-small-latest"):
    api_key = MISTRAL_API_KEY
    if not api_key:
        print("错误：未设置MISTRAL_API_KEY环境变量")
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
        print(f"正在调用Mistral API，模型：{model}")
        print(f"发送的提示：{prompt[:1000]}...")
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        print(f"Mistral API响应：{response_json}")
        if response_json and response_json.get('choices'):
            content = response_json['choices'][0]['message']['content']
            print(f"Mistral API内容：{content}")
            return content
        else:
            print(f"Mistral API错误：无效响应格式：{response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Mistral API错误：{e}")
        if hasattr(e, "response") and e.response is not None:
            print(f"响应状态码：{e.response.status_code}")
            print(f"响应内容：{e.response.text}")
        return None

def fetch_and_summarize(url, fallback_title=None):
    print(f"正在摘要：{url}")
    html = fetch_html_content(url)
    if not html:
        return {"url": url, "summary": "无法获取内容", "title": fallback_title or url}
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
        print("未设置MISTRAL_API_KEY，返回前15个单词作为摘要")
        return limit_to_n_words(text, 15)
    prompt = (
        "如果原文是中文，请用英文摘要。"
        "用清晰简洁的英文总结以下网页内容。"
        "聚焦于最重要的观点或见解。"
        "摘要长度约300字符。"
        "仅输出摘要句子：\n"
        f"标题：{title if title else ''}\n"
        f"{text}\n"
        f"{'原文链接：' + url if url else ''}"
    )
    summary = call_mistral_api(prompt)
    if summary is None:
        return limit_to_n_words(text, 15)
    # 最终截断至300字符
    return summary.strip()[:300]

def generate_summarized_report(summaries, source_name):
    text = f"{source_name}\n"
    text += "-" * len(source_name) + "\n"
    if not summaries:
        text += "未找到项目\n\n"
        return text
    url_pattern = re.compile(r'(https?://[^\s]+)')
    for idx, item in enumerate(summaries, 1):
        summary = item.get('summary', '').replace('\n', ' ').replace('\r', ' ').strip()
        summary = summary.replace('*', '')
        summary = url_pattern.sub('', summary)
        # 最终将每个摘要截断至300字符
        summary = summary[:300]
        text += f"{idx}. {summary}\n\n"  # 在摘要间添加额外换行
    text += "\n"
    return text

# --- 《纽约时报》中文版集成 ---

def extract_nytimes_links(html, max_links=5):
    """
    从cn.nytimes.com主页提取链接。
    仅包含以'https://cn.nytimes.com/'开头的链接。
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
    print(f"从主页提取了{len(links)}条链接")
    return links

def summarize_nytimes_article(url):
    html = fetch_html_content(url)
    if not html:
        return {"url": url, "summary": "无法获取内容", "title": url}
    soup = BeautifulSoup(html, 'html.parser')
    # 尝试提取文章主标题
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
    # 检查--test参数
    is_test = "--test" in sys.argv

    today = datetime.datetime.now().strftime("%Y-%m-%d")
    report = f"每日新闻摘要 - {today}\n\n"

    if is_test:
        # 仅抓取一条链接并发送一份摘要（《纽约时报》中文版）
        ny_html = fetch_html_content('https://m.cn.nytimes.com')
        ny_links = []
        ny_summaries = []
        if ny_html:
            ny_links = extract_nytimes_links(ny_html, max_links=1)
            if ny_links:
                link = ny_links[0]
                summary = summarize_nytimes_article(link['url'])
                ny_summaries.append(summary)
        report = generate_summarized_report(ny_summaries, "《纽约时报》（中文版）")
        if ny_summaries:
            if send_telegram_message(report):
                print("测试摘要已成功发送至Telegram")
                sys.exit(0)
            else:
                print("向Telegram发送测试摘要失败")
                sys.exit(1)
        else:
            print("未收集到新闻，未向Telegram发送内容")
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

        # --- GitHub热门项目 ---
        gh_html = fetch_html_content('https://github.com/trending')
        gh_links = []
        gh_summaries = []
        if gh_html:
            gh_links = extract_github_trending(gh_html)
            for link in gh_links:
                summary = fetch_and_summarize(link['url'], fallback_title=link['text'])
                gh_summaries.append(summary)
                time.sleep(2)
        report += generate_summarized_report(gh_summaries, "GitHub热门项目")

        # --- 《纽约时报》中文版 ---
        ny_html = fetch_html_content('https://m.cn.nytimes.com')
        ny_links = []
        ny_summaries = []
        if ny_html:
            ny_links = extract_nytimes_links(ny_html, max_links=5)
            for link in ny_links:
                summary = summarize_nytimes_article(link['url'])
                ny_summaries.append(summary)
                time.sleep(2)
        report += generate_summarized_report(ny_summaries, "《纽约时报》（中文版）")

        if any([hn_summaries, gh_summaries, ny_summaries]):
            if len(report) > TELEGRAM_MAX_LENGTH:
                print(f"报告超过{TELEGRAM_MAX_LENGTH}字符，将被分割为多条消息")
            if send_telegram_message(report):
                print("每日新闻报告已成功发送至Telegram")
                sys.exit(0)
            else:
                print("向Telegram发送每日新闻报告失败")
                sys.exit(1)
        else:
            print("未收集到新闻，未向Telegram发送内容")
            sys.exit(1)

if __name__ == "__main__":
    main()
```

```yml
name: 新闻机器人

on:
  schedule:
    # 每天北京时间上午9点（UTC凌晨1点）运行
    - cron: '0 1 * * *'
  workflow_dispatch:  # 允许手动触发
  push:
    # 仅当两个文件在同一提交/推送中更改时触发
    # 这需要下面的过滤作业检查两个文件
    paths:
      - scripts/nytimes/news_bot.py
      - .github/workflows/news.yml

concurrency:
  group: 'news'
  cancel-in-progress: false

jobs:
  发送新闻:
    runs-on: ubuntu-latest
    environment: github-pages
    env:
      TELEGRAM_BOT_API_KEY: ${{ secrets.TELEGRAM_BOT_API_KEY }}
      MISTRAL_API_KEY: ${{ secrets.MISTRAL_API_KEY }}    

    steps:
      - name: 检出仓库
        uses: actions/checkout@v4
        with:
          fetch-depth: 5

      - name: 设置Python 3.10.x
        uses: actions/setup-python@v4
        with:
          python-version: "3.10.x"

      - name: 安装依赖
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.simple.txt

      - name: 运行新闻机器人脚本
        run: python scripts/nytimes/news_bot.py
```