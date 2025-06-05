import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import ssl
import datetime
import sys

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
        context = ssl._create_unverified_context()
        print(f"Fetching HTML content from: {url}")
        response = requests.get(url, verify=False)
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
    for item in soup.select('.titleline > a'):
        url = item['href']
        title = item.text.strip()
        if url.startswith('item?id='):  # Handle internal HN links
            url = f"https://news.ycombinator.com/{url}"
        links.append({'url': url, 'text': title})
    print(f"Extracted {len(links)} links from Hacker News.")
    return links[:5]  # Limit to top 5 stories

def extract_github_trending(html):
    """Extracts trending repositories from GitHub."""
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for repo in soup.select('article.Box-row h1 a'):
        url = f"https://github.com{repo['href']}"
        title = repo.text.strip().replace('\n', '').replace(' ', '')
        links.append({'url': url, 'text': title})
    print(f"Extracted {len(links)} trending repositories from GitHub.")
    return links[:5]  # Limit to top 5 repos

def extract_nytimes_links(html):
    """Extracts links from the main page of cn.nytimes.com."""
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for a in soup.find_all('a', href=True):
        url = a['href']
        if url.startswith('https://m.cn.nytimes.com/'):
            links.append({
                'url': url,
                'text': a.text.strip()
            })
    print(f"Extracted {len(links)} links from NYTimes.")
    return links[:5]  # Limit to top 5 articles

def generate_markdown_report(articles, source_name):
    """Generates a Markdown report for the given articles."""
    markdown = f"### {source_name}\n\n"
    for article in articles:
        markdown += f"- [{article['text']}]({article['url']})\n"
    return markdown + "\n"

def main():
    """Main function to scrape news and send to Telegram."""
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    markdown_report = f"# Daily News Summary - {today}\n\n"

    # Hacker News
    hn_html = fetch_html_content('https://news.ycombinator.com')
    if hn_html:
        hn_links = extract_hacker_news_links(hn_html)
        markdown_report += generate_markdown_report(hn_links, "Hacker News")

    # GitHub Trending
    gh_html = fetch_html_content('https://github.com/trending')
    if gh_html:
        gh_links = extract_github_trending(gh_html)
        markdown_report += generate_markdown_report(gh_links, "GitHub Trending")

    # NYTimes
    nytimes_html = fetch_html_content('https://m.cn.nytimes.com')
    if nytimes_html:
        nytimes_links = extract_nytimes_links(nytimes_html)
        markdown_report += generate_markdown_report(nytimes_links, "NYTimes (Chinese)")

    # Send report to Telegram
    if markdown_report.strip() != f"# Daily News Summary - {today}":
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