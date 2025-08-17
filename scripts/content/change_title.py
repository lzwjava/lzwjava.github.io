import os
import re

def parse_front_matter(file_content):
    match = re.search(r'---\n(.*?)\n---', file_content, re.DOTALL)
    if match:
        front_matter_str = match.group(1)
        front_matter = {}
        for line in front_matter_str.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                front_matter[key.strip()] = value.strip()
        return front_matter, match.end()
    return {}, 0

def update_front_matter(file_content, new_front_matter):
    front_matter, end_index = parse_front_matter(file_content)
    if front_matter:
        new_front_matter_str = ''
        for key, value in new_front_matter.items():
            new_front_matter_str += f'{key}: {value}\n'
        return f'---\n{new_front_matter_str}---{file_content[end_index:]}'
    return file_content

def extract_url_from_filename(filename):
    # Remove date and .md extension
    match = re.match(r'\d{4}-\d{2}-\d{2}-(.*?)\.md', filename)
    if match:
        return match.group(1)
    return None

def find_and_replace_hyperlinks(directory, old_url, new_url):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Replace URLs in the format [text](old_url)
                updated_content = re.sub(f'\[(.*?)\]\({re.escape(old_url)}(.*?)\)', r'[\1]({\2})\4'.format(new_url), content)

                # Replace standalone URLs
                updated_content = updated_content.replace(old_url, new_url)

                if updated_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(updated_content)
                    print(f'Updated hyperlinks in: {file_path}')

def change_post_title(file_path, new_title):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    front_matter, _ = parse_front_matter(content)
    if 'title' in front_matter:
        old_title = front_matter['title']
        front_matter['title'] = new_title
        updated_content = update_front_matter(content, front_matter)

        # Get old URL slug from filename
        filename = os.path.basename(file_path)
        old_url_slug = extract_url_from_filename(filename)

        # Generate new URL slug from new_title
        # Remove special characters to create a clean slug
        clean_new_title = re.sub(r'[^a-zA-Z0-9\s]', '', new_title) 
        new_url_slug = clean_new_title.lower().replace(' ', '-')
        
        # Check if new URL slug is different and rename file
        if old_url_slug and old_url_slug != new_url_slug:
            # Construct new filename with the new slug while retaining the date and extension
            date_part = filename.split('-', 3)[:3] # Extracts 'YYYY', 'MM', 'DD'
            new_filename = '-'.join(date_part) + '-' + new_url_slug + '.md'

            old_file_path = file_path
            new_file_path = os.path.join(os.path.dirname(file_path), new_filename)
            
            os.rename(old_file_path, new_file_path)
            print(f'Renamed file from {os.path.basename(old_file_path)} to {new_filename}')
            file_path = new_file_path # Update file_path to new path for writing content

            # Update hyperlinks in all markdown files in 'original' and '_posts' directories
            find_and_replace_hyperlinks('original', old_url_slug, new_url_slug)
            find_and_replace_hyperlinks('_posts', old_url_slug, new_url_slug)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print(f'Updated title in {os.path.basename(file_path)} from "{old_title}" to "{new_title}"')
    else:
        print(f'No title found in front matter of {file_path}')


# Example Usage:
# change_post_title('original/2025-07-28-change-habit-en.md', 'New Title for Change Habit Post')
# change_post_title('_posts/en/2025-08-18-llm-costs-en.md', 'Optimizing LLM API Costs: A Detailed Guide')

if __name__ == "__main__":
    # Example usage. Uncomment and modify as needed.
    # change_post_title('original/2025-07-28-change-habit-en.md', 'New Title for Change Habit Post')
    # change_post_title('_posts/en/2025-08-18-llm-costs-en.md', 'Optimizing LLM API Costs: A Detailed Guide')
    pass # Replace with actual calls