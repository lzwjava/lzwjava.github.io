import os
import datetime
import pyperclip
import re
import requests
import sys

def call_mistral_api(prompt):
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
        "model": "mistral-small-latest",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        if response_json and response_json['choices']:
            content = response_json['choices'][0]['message']['content']
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

def get_first_n_words(text, n=500):
    words = text.split()
    return ' '.join(words[:n])

def process_title_for_filename(title):
    title = title.strip()
    title = re.sub(r'\s+', '-', title) 
    title = re.sub(r'[^a-zA-Z0-9-]', '', title)  # Remove special characters
    title = title.lower()
    return title

def clean_grok_tags(content):
    if "<grok:render" in content:
        prompt = f"""Remove all <grok:render> tags and their contents from the following text, and format the text cleanly by removing extra spaces and ensuring proper sentence spacing. Respond with only the cleaned text:

{content}"""
        cleaned_content = call_mistral_api(prompt)
        if not cleaned_content:
            print("Failed to clean grok tags. Using original content.")
            return content
        return cleaned_content.strip()
    return content

def create_note():
    # Get clipboard content
    content = pyperclip.paste()
    if len(content.strip()) < 100:
        print("Clipboard content is less than 100 characters. Aborting.")
        sys.exit(1)
    if not content.strip():
        print("Clipboard is empty. Nothing to create.")
        sys.exit(1)

    # Clean grok tags if present
    content = clean_grok_tags(content)

    # Generate full title for front matter
    prompt_content = get_first_n_words(content)
    prompt = f"Generate a very short title (maximum six words) for the following text and respond with only the title: {prompt_content}"
    full_title = call_mistral_api(prompt)
    if not full_title:
        print("Failed to generate full title. Exit.")
        sys.exit(1)
    full_title = re.sub(r'\*', ' ', full_title)
    full_title = full_title.strip()

    # Generate short title (max 3 words) for filename
    prompt = f"Generate a very short title (maximum three words, all lowercase, use only letters, numbers, or hyphens, no spaces or special characters, do not have single quote, use hypen to concatenate words) for the following text and respond with only the title: {prompt_content}"
    short_title = call_mistral_api(prompt)
    if not short_title:
        print("Failed to generate short title. Exit.")
        sys.exit(1)
    short_title = short_title.strip().lower()

    # Create filename with date
    today = datetime.date.today()
    date_str = today.strftime('%Y-%m-%d')
    notes_dir = 'notes'
    if not os.path.exists(notes_dir):
        os.makedirs(notes_dir)
    base_file_name = f"{date_str}-{short_title}-en.md"
    file_path = os.path.join(notes_dir, base_file_name)

    # Ensure unique filename
    counter = 1
    while os.path.exists(file_path):
        file_path = os.path.join(notes_dir, f"{date_str}-{short_title}-{counter}-en.md")
        counter += 1
        
    if ":" in full_title and '"' not in full_title:
        full_title = f'"{full_title}"'

    # Create front matter with full title
    front_matter = f"""---
title: {full_title}
lang: en
layout: post
audio: false
translated: false
generated: true
---"""

    # Remove title from content if it exists
    lines = content.splitlines()
    if lines and lines[0].startswith('# '):
        content = '\n'.join(lines[1:])
    content = content.strip()

    # Write to file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(front_matter + '\n\n' + content)
    print(f"Created note: {file_path}")

if __name__ == "__main__":
    create_note()