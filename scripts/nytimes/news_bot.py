import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import datetime
import sys
import re

load_dotenv()

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_API_KEY")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "610574272")

def send_telegram_message(message):
    """Sends a message to a Telegram chat using the Telegram Bot API."""
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("Error: TELEGRAM_BOT_API_KEY or TELEGRAM_CHAT_ID not set.")
        return False
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    params = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, params=params)
        response.raise_for_status()
        print(f"Successfully sent Telegram message.")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error sending Telegram message: {e}")
        return False

def fetch_html_content(url):
    """Fetches the HTML content of a given URL."""
    try:
        print(f"Fetching HTML content from: {url}")
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        print(f"Successfully fetched HTML content from: {url}")
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Could not fetch URL: {url} - {e}")
        return None

def extract_hacker_news_links(html):
    """Extracts links from Hacker News."""
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    seen = set()
    for item in soup.select('.titleline > a'):
        url = item['href']
        title = item.text.strip()
        if url.startswith('item?id='):  # Handle internal HN links
            url = f"https://news.ycombinator.com/{url}"
        # Avoid duplicates and empty titles
        if url not in seen and title:
            links.append({'url': url, 'text': title})
            seen.add(url)
        if len(links) >= 5:
            break
    print(f"Extracted {len(links)} links from Hacker News.")
    return links

def extract_github_trending(html):
    """Extracts trending repositories from GitHub."""
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for repo in soup.select('article.Box-row h2 a'):
        url = f"https://github.com{repo['href']}"
        # Clean up repo name: remove extra whitespace and newlines
        title = re.sub(r'\s+', ' ', repo.text).strip()
        if title and url:
            links.append({'url': url, 'text': title})
        if len(links) >= 5:
            break
    print(f"Extracted {len(links)} trending repositories from GitHub.")
    return links

def extract_nytimes_links(html):
    """Extracts links from the main page of cn.nytimes.com."""
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    seen = set()
    # NYTimes mobile Chinese site: look for news article links in <section> or <article>
    for a in soup.find_all('a', href=True):
        url = a['href']
        text = a.get_text(strip=True)
        # Only keep links that look like news articles and have non-empty text
        if url.startswith('https://m.cn.nytimes.com/') and text and url not in seen:
            links.append({'url': url, 'text': text})
            seen.add(url)
        if len(links) >= 5:
            break
    print(f"Extracted {len(links)} links from NYTimes.")
    return links

def generate_markdown_report(articles, source_name):
    """Generates a Markdown report for the given articles."""
    markdown = f"### {source_name}\n\n"
    if not articles:
        markdown += "_No items found._\n\n"
        return markdown
    for article in articles:
        # Escape parentheses in text to avoid Markdown link issues
        safe_text = article['text'].replace('(', '\\(').replace(')', '\\)')
        markdown += f"- [{safe_text}]({article['url']})\n"
    return markdown + "\n"

def main():
    """Main function to scrape news and send to Telegram."""
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    markdown_report = f"# Daily News Summary - {today}\n\n"

    # Hacker News
    hn_html = fetch_html_content('https://news.ycombinator.com')
    hn_links = []
    if hn_html:
        hn_links = extract_hacker_news_links(hn_html)
    markdown_report += generate_markdown_report(hn_links, "Hacker News")

    # GitHub Trending
    gh_html = fetch_html_content('https://github.com/trending')
    gh_links = []
    if gh_html:
        gh_links = extract_github_trending(gh_html)
    markdown_report += generate_markdown_report(gh_links, "GitHub Trending")

    # NYTimes
    nytimes_html = fetch_html_content('https://m.cn.nytimes.com')
    nytimes_links = []
    if nytimes_html:
        nytimes_links = extract_nytimes_links(nytimes_html)
    markdown_report += generate_markdown_report(nytimes_links, "NYTimes (Chinese)")

    # Only send if at least one section has news
    if any([hn_links, gh_links, nytimes_links]):
        if send_telegram_message(markdown_report):
            print("Daily news report sent to Telegram successfully.")
            sys.exit(0)
        else:
            print("Failed to send daily news report to Telegram.")
            sys.exit(1)
    else:
        print("No news collected, nothing sent to Telegram.")
        sys.exit(1)

if __name__ == "__main__":
    main()