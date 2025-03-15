import requests
from bs4 import BeautifulSoup
import os
import ssl
from dotenv import load_dotenv
import os
import sys

load_dotenv()

def call_mistral_api(prompt, model="mistral-small-2501"):
    """Calls the Mistral API to translate text."""
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("Error: MISTRAL_API_KEY environment variable not set.")
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
        print(f"Prompt being sent: {prompt[:100]}...")  # Print the first 100 characters of the prompt
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
    """Fetches the HTML content of a given URL."""
    try:
        # Create an unverified SSL context
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
    """Extracts links from the main page of cn.nytimes.com."""
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
    """Translates the title from Chinese to English using Mistral """
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

def extract_nytimes_links(html):
    """Extracts NYTimes links from a given HTML page."""
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    title_element = soup.select_one('.article-area .article-content .article-header header h1')
    title = title_element.text.strip() if title_element else ''
    print(f"Extracted title: {title}")

    for a in soup.find_all('a', href=True):
        url = a['href']
        if url.startswith('https://www.nytimes.com/'):
            links.append({
                'url': url,
                'title': title,
                'text': a.text.strip()
            })
    print(f"Extracted {len(links)} NYTimes links.")
    return links

def generate_markdown_list(links):
    """Generates a Markdown list from a list of links."""
    if not links:
        return '* No links found.\n'

    markdown_list = ''
    for link in links:
        translated_title = translate_title(link["title"])
        markdown_list += f'* [{translated_title}]({link["url"]})\n'
    print("Generated Markdown list.")
    return markdown_list

def update_markdown_file(filename, markdown_content):
    """Updates a Markdown file with the given content."""
    try:
        # Read the existing content of the file
        print(f"Reading existing content from {filename}")
        with open(filename, 'r', encoding='utf-8') as f:
            existing_content = f.read()

        # Find the start and end positions of the content after the initial metadata
        start_index = existing_content.find('---', 3) + 4  # Find the second '---' and move past it
        end_index = len(existing_content)

        # Construct the updated content
        updated_content = existing_content[:start_index].strip() + '\n\n'  # Keep the metadata and add a newline
        updated_content += markdown_content.strip() + '\n'  # Add the new markdown list
        # updated_content += existing_content[end_index:].strip() # Append anything after the list, if it exists

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
    """Main function to fetch, process, and update the Markdown file."""
    nytimes_url = 'https://m.cn.nytimes.com'
    print(f'Fetching NYTimes links from: {nytimes_url}')

    html_content = fetch_html_content(nytimes_url)
    if not html_content:
        print("Failed to fetch main page content.")
        return

    links = extract_links(html_content)
    print(f'Found {len(links)} links on main page. Extracting links...')

    all_nytimes_links = []
    for i, link in enumerate(links):
        print(f'Processing link {i + 1} of {len(links)}: {link["url"]}')
        article_html = fetch_html_content(link["url"])
        if article_html:
            nytimes_links = extract_nytimes_links(article_html)
            print(f'Found {len(nytimes_links)} NYTimes links in {link["url"]}.')
            all_nytimes_links.extend(nytimes_links)
        else:
            print(f'Failed to fetch content from {link["url"]}')

    filtered_links = [link for link in all_nytimes_links if '本文英文版' in link['text']]
    print(f"Found {len(filtered_links)} links containing '本文英文版'. Generating list...")

    markdown_list = generate_markdown_list(filtered_links)

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
