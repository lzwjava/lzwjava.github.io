import os
import re

def fix_mathjax_in_markdown(directory):
    """
    Finds all markdown files in a directory and replaces instances of
    \( and \) with \\( and \\) respectively.

    Args:
        directory (str): The directory to search for markdown files.
    """
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".md"):
                filepath = os.path.join(root, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Replace \( with \\( and \) with \\)
                    updated_content = re.sub(r'\\\(', r'\\\\(', content)
                    updated_content = re.sub(r'\\\)', r'\\\\)', updated_content)
                    updated_content = re.sub(r'\(', r'\\\\(', updated_content)
                    updated_content = re.sub(r'\)', r'\\\\)', updated_content)


                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(updated_content)

                    print(f"Fixed MathJax delimiters in: {filepath}")

                except Exception as e:
                    print(f"Error processing {filepath}: {e}")


def main():
    """
    Main function to specify directories to process.
    """
    directories = ["_posts", "original", "."]  # Add "." to process the current directory as well
    for directory in directories:
        if os.path.exists(directory):
            fix_mathjax_in_markdown(directory)
        else:
            print(f"Directory not found: {directory}")

if __name__ == "__main__":
    main()
