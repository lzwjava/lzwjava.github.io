import os
import re
import markdown
import argparse

def fix_mathjax_in_markdown(directory, max_files=None):
    """
    Finds all markdown files in a directory and replaces instances of
    \( and \) with \\( and \\) respectively, skipping code blocks.

    Args:
        directory (str): The directory to search for markdown files.
        max_files (int, optional):  Maximum number of files to process. Defaults to None (unlimited).
    """
    files_processed = 0
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".md"):
                filepath = os.path.join(root, filename)
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

                    # Function to replace MathJax delimiters outside code blocks
                    def replace_mathjax(text):
                        temp_text = text
                        for cb in code_block_data:
                            temp_text = temp_text.replace(cb['content'], 'CODE_BLOCK_PLACEHOLDER')

                        temp_text = re.sub(r'\\\(', r'\\\\(', temp_text)
                        temp_text = re.sub(r'\\\)', r'\\\\)', temp_text)         

                        for cb in code_block_data:
                            temp_text = temp_text.replace('CODE_BLOCK_PLACEHOLDER', cb['content'])
                        return temp_text

                    updated_content = replace_mathjax(content)

                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(updated_content)

                    print(f"Fixed MathJax delimiters in: {filepath}")
                    files_processed += 1

                    if max_files and files_processed >= max_files:
                        print(f"Maximum files processed ({max_files}). Exiting directory.")
                        return

                except Exception as e:
                    print(f"Error processing {filepath}: {e}")


def main():
    """
    Main function to specify directories to process.
    """
    parser = argparse.ArgumentParser(description="Fix MathJax delimiters in Markdown files.")
    parser.add_argument("--maxfiles", type=int, help="Maximum number of files to process.")
    args = parser.parse_args()

    directories = ["_posts", "original", "notes"]  # Add "." to process the current directory as well
    for directory in directories:
        if os.path.exists(directory):
            fix_mathjax_in_markdown(directory, max_files=args.maxfiles)
        else:
            print(f"Directory not found: {directory}")

if __name__ == "__main__":
    main()
