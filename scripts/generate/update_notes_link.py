import os
import re
import time
from generate_notes_link import generate_notes_links


def count_notes_files():
    # Count the number of markdown files in the notes directory
    notes_dir = 'notes'
    try:
        note_files = [f for f in os.listdir(notes_dir) if f.endswith('.md')]
        return len(note_files)
    except Exception as e:
        print(f"Error counting notes files: {e}")
        return 0

def count_links_in_notes_md():
    # Count the number of links in the notes markdown file
    file_path = os.path.join('original', '2025-01-11-notes-en.md')
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Count the number of markdown links in the file
            links = re.findall(r'\* \[.*?\]\(/notes/.*?\)', content)
            return len(links)
    except Exception as e:
        print(f"Error counting links in notes markdown file: {e}")
        return 0

def check_last_modified_time():
    # Check when the notes markdown file was last modified
    file_path = os.path.join('original', '2025-01-11-notes-en.md')
    try:
        mod_time = os.path.getmtime(file_path)
        current_time = time.time()
        hours_since_modified = (current_time - mod_time) / 3600  # Convert seconds to hours
        
        print(f"Hours since last modification: {hours_since_modified:.2f}")
        return hours_since_modified > 2  # Return True if more than 2 hours have passed
    except Exception as e:
        print(f"Error checking modification time: {e}")
        return True  # Default to True if there's an error

def main():
    notes_count = count_notes_files()
    links_count = count_links_in_notes_md()
    
    print(f"Notes files count: {notes_count}")
    print(f"Links count in markdown: {links_count}")
    
    if notes_count != links_count and check_last_modified_time():
        print("Notes files count and links count don't match and last modification was more than 2 hours ago, regenerating notes links.")
        generate_notes_links()
    else:
        print("Skipping notes link regeneration.")

if __name__ == "__main__":
    main()
