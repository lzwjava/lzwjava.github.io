import os
import sys
import glob
import argparse


def delete_md(name):
    """Delete Markdown files and associated assets for the given name across languages."""
    posts_dir = "_posts"
    pdfs_dir = "assets/pdfs"
    audios_dir = "assets/audios"

    langs = ["en", "zh", "es", "fr", "de", "ja", "hi", "ar", "hant"]

    for lang in langs:
        # Construct the file name pattern
        md_file_pattern = os.path.join(posts_dir, lang, f"{name}-{lang}.md")
        pdf_file_pattern = os.path.join(pdfs_dir, lang, f"{name}-{lang}.pdf")
        audio_file_pattern = os.path.join(audios_dir, f"{name}-{lang}.mp3")

        # Find and delete matching Markdown files
        for md_file_path in glob.glob(md_file_pattern):
            if os.path.exists(md_file_path):
                os.remove(md_file_path)
                print(f"Deleted file: {md_file_path}")
            else:
                print(f"File not found: {md_file_path}")

        # Delete associated PDF files
        for pdf_file_path in glob.glob(pdf_file_pattern):
            if os.path.exists(pdf_file_path):
                os.remove(pdf_file_path)
                print(f"Deleted file: {pdf_file_path}")
            else:
                print(f"File not found: {pdf_file_path}")

        # Delete associated audio files
        if os.path.exists(audio_file_pattern):
            os.remove(audio_file_pattern)
            print(f"Deleted file: {audio_file_pattern}")
        else:
            print(f"File not found: {audio_file_pattern}")


def extract_post_name_from_path(file_path):
    """Extract post name from file path, handling both relative and absolute paths."""
    # Get the filename from the path
    filename = os.path.basename(file_path)

    # Remove the .md extension
    if filename.endswith(".md"):
        filename = filename[:-3]

    # Extract the post name by removing date and language suffix
    # Pattern: YYYY-MM-DD-postname-lang.md -> postname
    parts = filename.split("-")
    if len(parts) >= 4:
        # Remove date (first 3 parts) and language (last part)
        post_name = "-".join(parts[3:-1])
        return post_name
    else:
        # Fallback: assume the whole filename is the post name
        return filename


def combine_posts(main_post_path, sub_post_path):
    """Combine two posts: append sub-post content to main post and delete sub-post files."""

    # Convert relative paths to absolute paths
    if not os.path.isabs(main_post_path):
        main_post_path = os.path.abspath(main_post_path)
    if not os.path.isabs(sub_post_path):
        sub_post_path = os.path.abspath(sub_post_path)

    print(f"Main post: {main_post_path}")
    print(f"Sub post: {sub_post_path}")

    # Check if both files exist
    if not os.path.exists(main_post_path):
        print(f"Error: Main post file not found: {main_post_path}")
        return

    if not os.path.exists(sub_post_path):
        print(f"Error: Sub post file not found: {sub_post_path}")
        return

    # Extract post name from sub-post path for deletion
    sub_post_name = extract_post_name_from_path(sub_post_path)
    print(f"Extracted sub-post name: {sub_post_name}")

    # Read content from both files
    try:
        with open(main_post_path, "r", encoding="utf-8") as f:
            main_content = f.read()

        with open(sub_post_path, "r", encoding="utf-8") as f:
            sub_content = f.read()
    except Exception as e:
        print(f"Error reading files: {e}")
        return

    # Extract content after front matter from sub-post
    # Split by --- to separate front matter from content
    sub_parts = sub_content.split("---", 2)
    if len(sub_parts) >= 3:
        sub_body = sub_parts[2].strip()
    else:
        # No front matter found, use entire content
        sub_body = sub_content.strip()

    # Combine the content
    if sub_body:
        combined_content = main_content + "\n\n---\n\n" + sub_body
    else:
        print("Warning: Sub-post has no content to append")
        combined_content = main_content

    # Write combined content back to main post
    try:
        with open(main_post_path, "w", encoding="utf-8") as f:
            f.write(combined_content)
        print(f"Successfully combined content into: {main_post_path}")
    except Exception as e:
        print(f"Error writing combined content: {e}")
        return

    # Delete sub-post and its translations, PDFs, audio files
    print(f"Deleting sub-post files for: {sub_post_name}")
    delete_md(sub_post_name)

    print("Combine operation completed successfully!")


if __name__ == "__main__":
    """Main entry point to handle command-line arguments."""
    parser = argparse.ArgumentParser(description="Combine two blog posts")
    parser.add_argument(
        "--main-post",
        required=True,
        help="Path to the main post file (relative or absolute)",
    )
    parser.add_argument(
        "--sub-post",
        required=True,
        help="Path to the sub post file (relative or absolute)",
    )

    args = parser.parse_args()
    combine_posts(args.main_post, args.sub_post)
