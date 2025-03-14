import requests
from bs4 import BeautifulSoup
import os
import ssl
from ..llm.test_mistral import call_mistral_api

def fetch_html_content(url):
    """Fetches the HTML content of a given URL."""
    try:
        # Create an unverified SSL context
        context = ssl._create_unverified_context()
        response = requests.get(url, verify=False)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
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
    return links

def translate_title(title):
    """Translates the title from Chinese to English using Mistral """
    base_prompt = "Translate the following title to {target_language}. Provide only the translated title, without any additional notes or explanations. Do not repeat or mention the input text.\n"
    prompt = base_prompt.format(target_language="English") + f"{title}"
    translated_title = call_mistral_api(prompt)
    if translated_title:
        return translated_title.strip()
    else:
        print(f"Failed to translate title: {title}")
        return title  # Return original title if translation fails

def extract_nytimes_links(html):
    """Extracts NYTimes links from a given HTML page."""
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    title_element = soup.select_one('.article-area .article-content .article-header header h1')
    title = title_element.text.strip() if title_element else ''

    for a in soup.find_all('a', href=True):
        url = a['href']
        if url.startswith('https://www.nytimes.com/'):
            links.append({
                'url': url,
                'title': title,
                'text': a.text.strip()
            })
    return links

def generate_markdown_list(links):
    """Generates a Markdown list from a list of links."""
    if not links:
        return '* No links found.\n'

    markdown_list = ''
    for link in links:
        translated_title = translate_title(link["title"])
        markdown_list += f'* [{translated_title}]({link["url"]})\n'
    return markdown_list

def update_markdown_file(filename, markdown_content):
    """Updates a Markdown file with the given content."""
    try:
        # Read the existing content of the file
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
        return existing_content != updated_content
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
    else:
        print("The Markdown file was not updated (no changes).")


if __name__ == "__main__":
    main()
