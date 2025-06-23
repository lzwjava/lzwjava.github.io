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

def get_first_n_words(text, n=100):
    words = text.split()
    return ' '.join(words[:n])

def process_title_for_filename(title):
    title = title.strip()
    title = re.sub(r'\s+', '-', title)  # Replace whitespace with hyphens
    title = re.sub(r'[^a-zA-Z0-9-]', '', title)  # Remove special characters
    title = title.lower()
    if len(title) > 50:
        title = title[:50]
    return title

def main():
    # Get clipboard content
    content = pyperclip.paste()
    if not content.strip():
        print("Clipboard is empty. Nothing to create.")
        sys.exit(1)

    # Generate title using AI
    prompt_content = get_first_n_words(content)
    prompt = f"Generate a short title for the following text and respond with only the title: {prompt_content}"
    title = call_mistral_api(prompt)
    if not title:
        print("Failed to generate title. Using default.")
        title = "untitled"
    title = title.strip()

    # Process title for filename
    processed_title = process_title_for_filename(title)
    if not processed_title:
        processed_title = "note"

    # Create filename with date
    today = datetime.date.today()
    date_str = today.strftime('%Y-%m-%d')
    notes_dir = 'notes'
    if not os.path.exists(notes_dir):
        os.makedirs(notes_dir)
    base_file_name = f"{date_str}-{processed_title}-en.md"
    file_path = os.path.join(notes_dir, base_file_name)

    # Ensure unique filename
    counter = 1
    while os.path.exists(file_path):
        file_path = os.path.join(notes_dir, f"{date_str}-{processed_title}-{counter}-en.md")
        counter += 1

    # Create front matter
    front_matter = f"""---
title: {title}
lang: en
layout: post
audio: false
translated: false
generated: true
---"""

    # Write to file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(front_matter + '\n\n' + content)
    print(f"Created note: {file_path}")

if __name__ == "__main__":
    main()