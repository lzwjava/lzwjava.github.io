---
audio: false
generated: true
lang: hi
layout: post
title: न्यूयॉर्क टाइम्स समाचार (सीएन) लेख अपडेट ट्रिगर
translated: true
---

नीचे दिए गए बटन पर क्लिक करें [NYTimes CN लेखों](./nytimes-en) को अपडेट करने के लिए।

<script async src="../assets/js/nytimes.js"></script>

<div class="nytimes" ></div>

इस पेज पर आप NYTimes CN लेखों को अपडेट करने के लिए एक कार्यक्रम शुरू कर सकते हैं। बटन पर क्लिक करने से एक कार्यक्रम शुरू होगा जो नवीनतम लेखों को फेटच करता है, उन्हें अनुवाद करता है, और इस साइट पर सामग्री को अपडेट करता है। कृपया ध्यान दें कि अपडेट ट्रिगर होने के बाद कुछ मिनट लग सकते हैं ताकि परिवर्तन दिखाई दें।

Python कोड:

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
    """Mistral API को कॉल करता है ताकि पाठ अनुवाद किया जा सके।"""
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("Error: MISTRAL_API_KEY पर्यावरण चर नहीं सेट है।")
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
        print(f"Calling Mistral API with model: {model}")
        print(f"Prompt being sent: {prompt[:1000]}...")  # Print the first 100 characters of the prompt
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        print(f"Mistral API Response: {response_json}")
        if response_json and response_json['choices']:
            content = response_json['choices'][0]['message']['content']
            print(f"Mistral API Content: {content}")
            return content
        else:
            print(f"Mistral API Error: Invalid response format: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Mistral API Error: {e}")
        if e.response:
            print(f"Response status code: {e.response.status_code}")
            print(f"Response content: {e.response.text}")
        return None

def fetch_html_content(url):
    """एक दिए गए URL से HTML सामग्री फेटच करता है।"""
    try:
        # एक अनवेरिफाइड SSL सांकेत बनाएं
        context = ssl._create_unverified_context()
        print(f"Fetching HTML content from: {url}")
        response = requests.get(url, verify=False)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        print(f"Successfully fetched HTML content from: {url}")
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Could not fetch URL: {url} - {e}")
        return None

def extract_links(html):
    """cn.nytimes.com के मुख्य पेज से लिंक्स निकालता है।"""
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for a in soup.find_all('a', href=True):
        url = a['href']
        if url.startswith('https://cn.nytimes.com/'):
            links.append({
                'url': url,
                'text': a.text.strip()
            })
    print(f"Extracted {len(links)} links from main page.")
    return links

def translate_title(title):
    """Mistral का उपयोग करके चीनी से अंग्रेजी में शीर्षक अनुवाद करता है"""
    base_prompt = "Translate the following title to {target_language}. Provide only the translated title, without any additional notes or explanations. Do not repeat or mention the input text.\n"
    prompt = base_prompt.format(target_language="English") + f"{title}"
    print(f"Translating title: {title}")
    translated_title = call_mistral_api(prompt)
    if translated_title:
        translated_title = translated_title.strip()
        print(f"Translated title: {translated_title}")
        return translated_title
    else:
        raise Exception(f"Failed to translate title: {title}")

def summarize_article(html):
    """Mistral API का उपयोग करके अंग्रेजी में लेख सामग्री सारांश करता है।"""
    soup = BeautifulSoup(html, 'html.parser')
    title_element = soup.select_one('.article-area .article-content .article-header header h1')
    title = title_element.text.strip() if title_element else ''
    print(f"Extracted title: {title}")

    # मुख्य लेख पाठ निकालें
    article_area = soup.find('div', class_='article-area')
    if article_area:
        article_text = article_area.get_text(separator='\n', strip=True)
    else:
        article_text = None

    if not article_text:
        print("Could not extract article text.")
        return None, None

    # Mistral के लिए सारांश बनाने के लिए एक प्रॉम्प बनाएं
    prompt = f"Summarize the following article in English, focusing on the main points and avoiding introductory phrases like 'Summary:' or 'This article is about:'.\n\n{article_text[:30000]}\n\n"  # Limit article text to 30000 characters
    print(f"Creating summary for title: {title}")
    summary = call_mistral_api(prompt)

    if summary:
        # सारांश को "Summary:" या समान वाक्यों को हटाकर साफ करें
        summary = summary.replace("Summary:", "").strip()
        print(f"Generated summary: {summary}")
        return title, summary
    else:
        print(f"Failed to generate summary for title: {title}")
        return None, None

def generate_markdown_list(articles):
    """एक लेख सारांशों की सूची से एक Markdown सूची बनाता है।"""
    if not articles:
        return '* No articles found.\n'

    markdown_list = ''
    for article in articles:
        title, summary = article
        translated_title = translate_title(title)
        markdown_list += f'## {translated_title}\n\n{summary}\n\n'
    print("Generated Markdown list.")
    return markdown_list

def update_markdown_file(filename, markdown_content):
    """एक दिए गए सामग्री के साथ एक Markdown फ़ाइल अपडेट करता है।"""
    try:
        # फ़ाइल की मौजूदा सामग्री पढ़ें
        print(f"Reading existing content from {filename}")
        with open(filename, 'r', encoding='utf-8') as f:
            existing_content = f.read()

        # प्रारंभिक मेटाडेटा के बाद सामग्री की शुरुआत और अंत की स्थिति पाएं
        start_index = existing_content.find('---', 3) + 4  # दूसरा '---' पाएं और उससे आगे बढ़ें
        end_index = len(existing_content)

        # अपडेट सामग्री बनाएं
        updated_content = existing_content[:start_index].strip() + '\n\n'  # मेटाडेटा रखें और एक नया लाइन जोड़ें
        updated_content += markdown_content.strip() + '\n'  # नया Markdown सूची जोड़ें
        # updated_content += existing_content[end_index:].strip() # सूची के बाद कुछ भी जोड़ें, अगर मौजूद है

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print(f"Successfully updated {filename}")
        markdown_changed = existing_content != updated_content
        print(f"Markdown changed: {markdown_changed}")
        return markdown_changed
    except Exception as e:
        print(f"Error updating {filename}: {e}")
        return False

def main():
    """Markdown फ़ाइल को फेटच, प्रोसेस, और अपडेट करने के लिए मुख्य फ़ंक्शन।"""
    nytimes_url = 'https://m.cn.nytimes.com'
    print(f'Fetching NYTimes links from: {nytimes_url}')

    html_content = fetch_html_content(nytimes_url)
    if not html_content:
        print("Failed to fetch main page content.")
        return

    links = extract_links(html_content)
    print(f'Found {len(links)} links on main page. Extracting links...')

    all_articles = []
    for i, link in enumerate(links):
        url = link["url"]
        if not url.endswith('/dual/'):
            if not url.endswith('/'):
                url = url + '/dual/'
            else:
                url = url + 'dual/'

        print(f'Processing link {i + 1} of {len(links)}: {url}')
        article_html = fetch_html_content(url)
        if article_html:
            title, summary = summarize_article(article_html)
            if title and summary:
                all_articles.append((title, summary))
        else:
            print(f'Failed to fetch content from {link["url"]}')

    markdown_list = generate_markdown_list(all_articles)

    filename = 'original/2025-03-14-nytimes-en.md'
    markdown_changed = update_markdown_file(filename, markdown_list)

    if markdown_changed:
        print("The Markdown file was updated with new links.")
        sys.exit(0)
    else:
        print("The Markdown file was not updated (no changes).")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

Frontend कोड:

```javascript
const nytimesDiv = document.querySelector('.nytimes');

if (nytimesDiv) {
    const updateButton = document.createElement('button');
    updateButton.textContent = 'Update NYTimes Articles';
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
                alert('Update triggered successfully! Please wait a few minutes to see the result.');
            } else {
                alert(`Update failed. Status code: ${response.status}`);
                console.error('Update failed:', response);
            }
        })
        .catch(error => {
            alert('Update failed. Check the console for errors.');
            console.error('Error triggering update:', error);
        });
    });
} else {
    console.error("nytimes div not found!");
}
```