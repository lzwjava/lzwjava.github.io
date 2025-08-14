import os
import glob
import sys


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


if __name__ == "__main__":
    """Main entry point to handle command-line arguments."""
    if len(sys.argv) < 2:
        print("Usage: python delete.py <name>")
        sys.exit(1)

    name = sys.argv[1]
    delete_md(name)