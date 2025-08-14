import os
import glob
import sys
import argparse


def extract_name_from_path_or_name(input_str):
    """Extract the base name from either a file path or a simple name.

    Args:
        input_str: Either a file path (e.g., '_posts/en/example-en.md') or a name (e.g., 'example')

    Returns:
        The base name without language suffix and extension
    """
    # If it's a path, get the filename
    if os.path.sep in input_str or '/' in input_str:
        filename = os.path.basename(input_str)
        # Remove extension if present
        name_with_lang = os.path.splitext(filename)[0]
    else:
        name_with_lang = input_str

    # Remove language suffix if present (e.g., 'example-en' -> 'example')
    langs = ["en", "zh", "es", "fr", "de", "ja", "hi", "ar", "hant"]
    for lang in langs:
        if name_with_lang.endswith(f"-{lang}"):
            return name_with_lang[:-len(f"-{lang}")]

    # If no language suffix found, return as is
    return name_with_lang


def delete_md(name_or_path, include_original=False):
    """Delete Markdown files and associated assets for the given name or path across languages.
    
    Args:
        name_or_path: Either a file path or a simple name
        include_original: If True, also delete the original file (without language suffix)
    """
    # Extract the base name from either path or name
    name = extract_name_from_path_or_name(name_or_path)

    posts_dir = "_posts"
    pdfs_dir = "assets/pdfs"
    audios_dir = "assets/audios"

    langs = ["en", "zh", "es", "fr", "de", "ja", "hi", "ar", "hant"]

    print(f"Deleting files for base name: {name}")

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
        audio_file_path = audio_file_pattern
        if os.path.exists(audio_file_path):
            os.remove(audio_file_path)
            print(f"Deleted file: {audio_file_path}")
        else:
            print(f"File not found: {audio_file_path}")

    # Delete original file if include_original is True
    if include_original:
        # Look for original file in various possible locations
        original_patterns = [
            os.path.join(posts_dir, f"{name}.md"),
            os.path.join("original", f"{name}.md"),
            f"{name}.md"
        ]
        
        for pattern in original_patterns:
            for original_file in glob.glob(pattern):
                if os.path.exists(original_file):
                    os.remove(original_file)
                    print(f"Deleted original file: {original_file}")
        
        # Also check for original PDF and audio files
        original_pdf_patterns = [
            os.path.join(pdfs_dir, f"{name}.pdf"),
            os.path.join("original", f"{name}.pdf"),
            f"{name}.pdf"
        ]
        
        for pattern in original_pdf_patterns:
            for original_pdf in glob.glob(pattern):
                if os.path.exists(original_pdf):
                    os.remove(original_pdf)
                    print(f"Deleted original PDF: {original_pdf}")
        
        original_audio_patterns = [
            os.path.join(audios_dir, f"{name}.mp3"),
            f"{name}.mp3"
        ]
        
        for pattern in original_audio_patterns:
            for original_audio in glob.glob(pattern):
                if os.path.exists(original_audio):
                    os.remove(original_audio)
                    print(f"Deleted original audio: {original_audio}")


if __name__ == "__main__":
    """Main entry point to handle command-line arguments."""
    parser = argparse.ArgumentParser(description="Delete Markdown files and associated assets")
    parser.add_argument("name_or_path", help="Name or path of the file to delete")
    parser.add_argument("--include-original", action="store_true", 
                       help="Also delete the original file (without language suffix)")
    
    args = parser.parse_args()
    
    delete_md(args.name_or_path, args.include_original)