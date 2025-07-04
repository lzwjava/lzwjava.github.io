import os
import datetime
import glob
import shutil

def publish_drafts_to_posts():
    """Checks for draft files created today and moves them to the _posts/en directory."""
    today = datetime.date.today()
    date_str = today.strftime('%Y-%m-%d')
    
    drafts_dir = '_drafts'
    posts_en_dir = os.path.join('original')

    if not os.path.exists(drafts_dir):
        print(f"Drafts directory '{drafts_dir}' does not exist. No files to publish.")
        return

    if not os.path.exists(posts_en_dir):
        os.makedirs(posts_en_dir)

    # Pattern to find files in drafts directory starting with today's date and ending with -en.md
    pattern = os.path.join(drafts_dir, f"{date_str}-*-en.md")
    
    found_files = glob.glob(pattern)

    if not found_files:
        print(f"No draft files found in '{drafts_dir}' starting with '{date_str}' to publish.")
        return

    for file_path in found_files:
        file_name = os.path.basename(file_path)
        destination_path = os.path.join(posts_en_dir, file_name)
        
        try:
            shutil.move(file_path, destination_path)
            print(f"Moved '{file_name}' from '{drafts_dir}' to '{posts_en_dir}'.")
        except Exception as e:
            print(f"Error moving '{file_name}': {e}")

if __name__ == "__main__":
    publish_drafts_to_posts()