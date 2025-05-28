import os
import re
import markdown
import argparse

def wrap_pmatrix_in_file(filepath):
    """
    Wraps LaTeX expressions containing pmatrix in a div tag in a markdown file,
    skipping code blocks.

    Args:
        filepath (str): The path to the markdown file to process.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Parse markdown to identify code blocks
        md = markdown.Markdown(extensions=['fenced_code'])
        html_content = md.convert(content)

        # Identify code blocks using regex
        code_blocks = list(re.finditer(r'<pre><code.*?>.*?</code></pre>', html_content, re.DOTALL))

        # Extract code block content and their positions
        code_block_data = []
        for match in code_blocks:
            code_block_data.append({
                'start': match.start(),
                'end': match.end(),
                'content': match.group(0)
            })

        # Function to wrap pmatrix expressions in divs outside code blocks
        def wrap_pmatrix(text):
            temp_text = text
            for cb in code_block_data:
                temp_text = temp_text.replace(cb['content'], 'CODE_BLOCK_PLACEHOLDER')

            # Pattern to match both \(...\) and $...$ delimiters containing pmatrix
            pattern = r'(\$|\\\()(.*?\\begin\{pmatrix\}.*?\\end\{pmatrix\}.*?)(\$|\\\))'
            
            def replacer(match):
                # Keep the original delimiters but wrap content in div
                opener = match.group(1)
                content = match.group(2)
                closer = match.group(3)
                return f'<div>{opener}\n{content}\n{closer}</div>'
            
            temp_text = re.sub(pattern, replacer, temp_text, flags=re.DOTALL)

            for cb in code_block_data:
                temp_text = temp_text.replace('CODE_BLOCK_PLACEHOLDER', cb['content'])
            return temp_text

        updated_content = wrap_pmatrix(content)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)

        print(f"Wrapped pmatrix expressions in divs in: {filepath}")
        return True

    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def wrap_pmatrix_in_markdown(directory, max_files=None):
    """
    Finds all markdown files in a directory and wraps pmatrix expressions in div tags.

    Args:
        directory (str): The directory to search for markdown files.
        max_files (int, optional): Maximum number of files to process. Defaults to None (unlimited).
    """
    files_processed = 0
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".md"):
                filepath = os.path.join(root, filename)
                success = wrap_pmatrix_in_file(filepath)
                if success:
                    files_processed += 1

                if max_files and files_processed >= max_files:
                    print(f"Maximum files processed ({max_files}). Exiting directory.")
                    return

def main():
    """
    Main function to process either a single file or directories.
    """
    parser = argparse.ArgumentParser(description="Wrap LaTeX pmatrix expressions in div tags in Markdown files.")
    parser.add_argument("--maxfiles", type=int, help="Maximum number of files to process.")
    parser.add_argument("--file", type=str, help="Path to a specific markdown file to process.")
    args = parser.parse_args()

    if args.file:
        # Process a single file
        if os.path.exists(args.file) and args.file.endswith(".md"):
            wrap_pmatrix_in_file(args.file)
        else:
            print(f"Invalid file path or not a markdown file: {args.file}")
    else:
        # Process directories
        directories = ["_posts", "original", "notes"]
        for directory in directories:
            if os.path.exists(directory):
                wrap_pmatrix_in_markdown(directory, max_files=args.maxfiles)
            else:
                print(f"Directory not found: {directory}")

if __name__ == "__main__":
    main()