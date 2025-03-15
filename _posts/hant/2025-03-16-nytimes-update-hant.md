---
audio: false
generated: true
lang: hant
layout: post
title: NYTimes新聞（CN）文章更新觸發
translated: true
---

點擊下面的按鈕以更新 [NYTimes CN 文章](./nytimes-en)。

<script async src="../assets/js/nytimes.js"></script>

<div class="nytimes" ></div>

本頁面允許您觸發更新 NYTimes CN 文章。點擊按鈕將啟動一個工作流程，該工作流程會獲取最新的文章，將其翻譯並更新本網站的內容。請注意，更新觸發後可能需要幾分鐘的時間才能看到變更。

Python 程式碼：

```python
import requests
from bs4 import BeautifulSoup
import os
import ssl
from dotenv import load_dotenv
import os
import sys

load_dotenv()

def call_mistral_api(prompt, model="mistral-small-2501"):
    """呼叫 Mistral API 以翻譯文字。"""
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("錯誤：MISTRAL_API_KEY 環境變數未設定。")
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
        print(f"呼叫 Mistral API 使用模型：{model}")
        print(f"發送的提示：{prompt[:1000]}...")  # 打印提示的前 100 个字符
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        print(f"Mistral API 回應：{response_json}")
        if response_json and response_json['choices']:
            content = response_json['choices'][0]['message']['content']
            print(f"Mistral API 內容：{content}")
            return content
        else:
            print(f"Mistral API 錯誤：無效的回應格式：{response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Mistral API 錯誤：{e}")
        if e.response:
            print(f"回應狀態碼：{e.response.status_code}")
            print(f"回應內容：{e.response.text}")
        return None

def fetch_html_content(url):
    """獲取給定 URL 的 HTML 內容。"""
    try:
        # 創建一個未驗證的 SSL 上下文
        context = ssl._create_unverified_context()
        print(f"從 {url} 获取 HTML 內容")
        response = requests.get(url, verify=False)
        response.raise_for_status()  # 為壞回應（4xx 或 5xx）引發 HTTPError
        print(f"成功從 {url} 获取 HTML 內容")
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"無法獲取 URL：{url} - {e}")
        return None

def extract_links(html):
    """從 cn.nytimes.com 的主頁中提取鏈接。"""
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for a in soup.find_all('a', href=True):
        url = a['href']
        if url.startswith('https://cn.nytimes.com/'):
            links.append({
                'url': url,
                'text': a.text.strip()
            })
    print(f"從主頁中提取了 {len(links)} 個鏈接。")
    return links

def translate_title(title):
    """使用 Mistral 將標題從中文翻譯成英文"""
    base_prompt = "將以下標題翻譯成 {target_language}。僅提供翻譯後的標題，不附加任何說明或解釋。不重複或提及輸入文本。\n"
    prompt = base_prompt.format(target_language="English") + f"{title}"
    print(f"翻譯標題：{title}")
    translated_title = call_mistral_api(prompt)
    if translated_title:
        translated_title = translated_title.strip()
        print(f"翻譯後的標題：{translated_title}")
        return translated_title
    else:
        raise Exception(f"翻譯標題失敗：{title}")

def summarize_article(html):
    """使用 Mistral API 以英文總結文章內容。"""
    soup = BeautifulSoup(html, 'html.parser')
    title_element = soup.select_one('.article-area .article-content .article-header header h1')
    title = title_element.text.strip() if title_element else ''
    print(f"提取標題：{title}")

    # 提取主文章文本
    article_area = soup.find('div', class_='article-area')
    if article_area:
        article_text = article_area.get_text(separator='\n', strip=True)
    else:
        article_text = None

    if not article_text:
        print("無法提取文章文本。")
        return None, None

    # 創建一個提示，讓 Mistral 進行總結
    prompt = f"以英文總結以下文章，專注於主要觀點，避免使用類似 'Summary:' 或 'This article is about:' 的引言。\n\n{article_text[:30000]}\n\n"  # 將文章文本限制為 30000 字符
    print(f"為標題創建總結：{title}")
    summary = call_mistral_api(prompt)

    if summary:
        # 通過移除前導的 "Summary:" 或類似短語來清理總結
        summary = summary.replace("Summary:", "").strip()
        print(f"生成的總結：{summary}")
        return title, summary
    else:
        print(f"生成標題的總結失敗：{title}")
        return None, None

def generate_markdown_list(articles):
    """從文章總結列表生成 Markdown 列表。"""
    if not articles:
        return '* 沒有找到文章。\n'

    markdown_list = ''
    for article in articles:
        title, summary = article
        translated_title = translate_title(title)
        markdown_list += f'## {translated_title}\n\n{summary}\n\n'
    print("生成 Markdown 列表。")
    return markdown_list

def update_markdown_file(filename, markdown_content):
    """使用給定內容更新 Markdown 文件。"""
    try:
        # 讀取文件的現有內容
        print(f"從 {filename} 讀取現有內容")
        with open(filename, 'r', encoding='utf-8') as f:
            existing_content = f.read()

        # 找到初始元數據後內容的起始和結束位置
        start_index = existing_content.find('---', 3) + 4  # 找到第二個 '---' 並移過它
        end_index = len(existing_content)

        # 构建更新的內容
        updated_content = existing_content[:start_index].strip() + '\n\n'  # 保留元數據並添加一個新行
        updated_content += markdown_content.strip() + '\n'  # 添加新的 Markdown 列表
        # updated_content += existing_content[end_index:].strip() # 如果存在，則附加列表後的任何內容

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print(f"成功更新 {filename}")
        markdown_changed = existing_content != updated_content
        print(f"Markdown 變更：{markdown_changed}")
        return markdown_changed
    except Exception as e:
        print(f"更新 {filename} 錯誤：{e}")
        return False

def main():
    """主函數以獲取、處理和更新 Markdown 文件。"""
    nytimes_url = 'https://m.cn.nytimes.com'
    print(f'從 {nytimes_url} 获取 NYTimes 鏈接')

    html_content = fetch_html_content(nytimes_url)
    if not html_content:
        print("獲取主頁內容失敗。")
        return

    links = extract_links(html_content)
    print(f'在主頁上找到 {len(links)} 個鏈接。提取鏈接...')

    all_articles = []
    for i, link in enumerate(links):
        url = link["url"]
        if not url.endswith('/dual/'):
            if not url.endswith('/'):
                url = url + '/dual/'
            else:
                url = url + 'dual/'

        print(f'處理鏈接 {i + 1} of {len(links)}: {url}')
        article_html = fetch_html_content(url)
        if article_html:
            title, summary = summarize_article(article_html)
            if title and summary:
                all_articles.append((title, summary))
        else:
            print(f'從 {link["url"]} 获取內容失敗')

    markdown_list = generate_markdown_list(all_articles)

    filename = 'original/2025-03-14-nytimes-en.md'
    markdown_changed = update_markdown_file(filename, markdown_list)

    if markdown_changed:
        print("Markdown 文件已更新新鏈接。")
        sys.exit(0)
    else:
        print("Markdown 文件未更新（無變更）。")
        sys.exit(1)

if __name__ == "__main__":
    main()

```

前端程式碼：

```javascript
const nytimesDiv = document.querySelector('.nytimes');

if (nytimesDiv) {
    const updateButton = document.createElement('button');
    updateButton.textContent = '更新 NYTimes 文章';
    nytimesDiv.appendChild(updateButton);

    updateButton.addEventListener('click', () => {
        fetch('https://api.github.com/repos/lzwjava/lzwjava.github.io/actions/workflows/nytimes.yml/dispatches', {
            method: 'POST',
            headers: {
                'Accept': 'application/vnd.github+json',
                'Authorization': 'Bearer token',
                'X-GitHub-Api-Version': '2022-11-28',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ ref: 'main' })
        })
        .then(response => {
            if (response.status === 204) {
                alert('更新觸發成功！請等待幾分鐘以查看結果。');
            } else {
                alert(`更新失敗。狀態碼：${response.status}`);
                console.error('更新失敗：', response);
            }
        })
        .catch(error => {
            alert('更新失敗。請檢查控制台錯誤。');
            console.error('觸發更新錯誤：', error);
        });
    });
} else {
    console.error("nytimes div 未找到！");
}
```