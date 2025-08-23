#!/usr/bin/env python3
import os
import sys
import argparse
from datetime import datetime
from rename_post import rename_post

def update_post_to_today(old_path):
    """Update a post's date to today by renaming the file"""
    
    # Extract just the filename from the path
    old_filename = os.path.basename(old_path)
    
    # Parse the old filename to extract the title and language
    if not old_filename.endswith('.md'):
        print(f"Error: {old_filename} is not a markdown file")
        return False
    
    # Split filename to get parts
    parts = old_filename[:-3].split('-')  # Remove .md extension
    
    if len(parts) < 4:
        print(f"Error: {old_filename} doesn't follow the expected format (YYYY-MM-DD-title-lang.md)")
        return False
    
    # Extract the title and language (everything after the date)
    title_and_lang = '-'.join(parts[3:])
    
    # Get today's date
    today = datetime.now().strftime('%Y-%m-%d')
    
    # Create new filename with today's date
    new_filename = f"{today}-{title_and_lang}.md"
    
    print(f"Updating {old_filename} to {new_filename}")
    
    # Use the rename_post function with just the filenames
    rename_post(old_filename, new_filename)
    
    return True

def main():
    parser = argparse.ArgumentParser(description="Update a post's date to today")
    parser.add_argument("filename", help="The post filename to update (e.g., 2023-01-01-title-en.md)")
    
    args = parser.parse_args()
    
    if not update_post_to_today(args.filename):
        sys.exit(1)
    
    print("Post updated successfully!")

if __name__ == "__main__":
    main()