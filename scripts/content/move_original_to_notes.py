import sys
import shutil
import subprocess
from pathlib import Path
import frontmatter

#!/usr/bin/env python3

def move_original_to_notes(filename):
    """
    Delete file from _posts/ using delete script and move from original/ to notes/
    Also updates the front matter to set generated: true
    """
    # Define paths
    original_dir = Path("original")
    notes_dir = Path("notes")
    
    # Extract just the filename from the path
    file_path = Path(filename)
    base_filename = file_path.name
    
    # Ensure filename has .md extension for file operations
    if not base_filename.endswith('.md'):
        md_filename = base_filename + '.md'
    else:
        md_filename = base_filename
    
    # Use the original filename (without .md) for the delete script
    delete_filename = base_filename.replace('.md', '') if base_filename.endswith('.md') else base_filename
    # Remove '-en' suffix if present
    delete_filename = delete_filename.replace('-en', '')
    
    # Define file paths
    original_file = original_dir / md_filename
    notes_file = notes_dir / md_filename
    
    print(delete_filename)
    
    # Delete from _posts using the delete script
    try:
        result = subprocess.run([
            "/opt/homebrew/bin/python3", "scripts/create/file.py", "delete", delete_filename
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"Deleted from _posts: {delete_filename}")
        else:
            print(f"Delete script output: {result.stdout}")
            if result.stderr:
                print(f"Delete script error: {result.stderr}")
    except Exception as e:
        print(f"Error running delete script: {e}")
    
    # Move from original to notes and update front matter
    if original_file.exists():
        # Create notes directory if it doesn't exist
        notes_dir.mkdir(exist_ok=True)
        
        # Read the file with frontmatter
        with open(original_file, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
        
        # Update the front matter to set generated: true
        post.metadata['generated'] = True
        
        # Write to the new location
        with open(notes_file, 'w', encoding='utf-8') as f:
            frontmatter.dump(post, f)
        
        # Remove the original file
        original_file.unlink()
        
        print(f"Moved and updated: {original_file} -> {notes_file}")
    else:
        print(f"File not found in original: {original_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python move_original_to_notes.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    move_original_to_notes(filename)
