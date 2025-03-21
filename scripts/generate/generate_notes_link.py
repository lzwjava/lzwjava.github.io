import os
import frontmatter  # You need to install the 'python-frontmatter' package
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_notes_links():
    # Path to the notes directory
    notes_dir = 'notes'

    # List all .md files in the notes directory
    note_files = [f for f in os.listdir(notes_dir) if f.endswith('.md')]
    logging.info(f"Found {len(note_files)} note files in {notes_dir}")

    # Parse each markdown file to extract the title and generate the links
    all_links = []
    for file in note_files:
        # Load the markdown file content and front matter
        file_path = os.path.join(notes_dir, file)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
                title = post.get('title', file.replace('.md', ''))  # Default to filename if no title is found
                lang = post.get('lang', 'en') # Default to english if no lang is found
            logging.info(f"  Extracted title: {title}, lang: {lang} from {file}")

            date = file.split('-')[:3] # Extract date from filename
            
            # Generate the markdown link with the title and add an asterisk (*) in front
            link = f"* [{title}](/notes/{file.replace('.md', '')})"
            all_links.append((date, link))
            logging.info(f"  Generated link: {link}")
        except Exception as e:
            logging.error(f"Error processing {file}: {e}")

    # Generate and update the markdown file for each language
    
    # Sort links by date descending
    all_links.sort(key=lambda item: item[0], reverse=True)
    sorted_links = [link for _, link in all_links]
    file_path = os.path.join('original', '2025-01-11-notes-en.md')
    content = f"""---
audio: true
lang: en
layout: post
title: Notes
generated: false
---

These notes are primarily generated by AI chatbots. I used them to summarize key points and will walk through them to enhance my understanding.

{chr(10).join(sorted_links)}
"""

    # Update the markdown file with the generated content
    try:
        with open(file_path, 'w', encoding='utf-8') as md_file:
            md_file.write(content)
        logging.info(f"Updated {file_path}")
    except Exception as e:
        logging.error(f"Error updating {file_path}: {e}")

if __name__ == "__main__":
    generate_notes_links()
