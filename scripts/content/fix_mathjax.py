import os
import re
import markdown
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
import argparse

class CodeBlockFinder(Extension):
    """Markdown extension to record code block positions."""
    def __init__(self):
        super().__init__()
        self.code_blocks = []

    def extendMarkdown(self, md):
        md.registerExtension(self)
        self.md = md
        # Insert a preprocessor to find code blocks
        md.preprocessors.register(CodeBlockPreprocessor(self), 'code_block_finder', 25)

class CodeBlockPreprocessor(Preprocessor):
    """Preprocessor to identify code blocks in markdown."""
    def __init__(self, extension):
        self.extension = extension
        self.code_block_re = re.compile(r'^```[a-zA-Z0-9_]*\n.*?\n```', re.DOTALL | re.MULTILINE)

    def run(self, lines):
        text = "\n".join(lines)
        self.extension.code_blocks = []
        for match in self.code_block_re.finditer(text):
            self.extension.code_blocks.append({
                'start': match.start(),
                'end': match.end(),
                'content': match.group(0)
            })
        return lines

def fix_mathjax_in_file(filepath, gemini=False, reset=False):
    r"""
    Replaces instances of \( and \) with \\( and \\) respectively in a markdown file,
    skipping code blocks. If gemini is True, also replaces $ $ with \\( and \\).
    If reset is True, performs the reverse operation: \\( to \(, \\) to \), etc.

    Args:
        filepath (str): The path to the markdown file to process.
        gemini (bool, optional): Whether to also convert dollar sign notation to/from backslash notation.
        reset (bool, optional): Whether to reverse the replacements (\\( to \(, etc.).
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Use markdown parser to identify code blocks
        code_finder = CodeBlockFinder()
        md = markdown.Markdown(extensions=[code_finder])
        md.convert(content)  # This populates code_finder.code_blocks

        # Function to replace MathJax delimiters outside code blocks
        def replace_mathjax(text, gemini=False, reset=False):
            # Create a list to hold the parts of the text
            parts = []
            last_pos = 0
            
            for cb in code_finder.code_blocks:
                # Add the non-code part before this code block
                non_code_part = text[last_pos:cb['start']]
                parts.append(non_code_part)
                # Add the code block unchanged
                parts.append(cb['content'])
                last_pos = cb['end']
            
            # Add the remaining non-code part after the last code block
            parts.append(text[last_pos:])
            
            # Process only the non-code parts
            processed_parts = []
            for i, part in enumerate(parts):
                if i % 2 == 0:  # Non-code part
                    if reset:
                        # Reverse replacements: \\( to \(, \\) to \), etc.
                        part = re.sub(r'\\\\\(', r'\(', part)
                        part = re.sub(r'\\\\\)', r'\)', part)
                        part = re.sub(r'\\\\\[', r'\[', part)
                        part = re.sub(r'\\\\\]', r'\]', part)
                        if gemini:
                            # Reverse $...$ to \\(...\\)
                            part = re.sub(r'\\\\\((.*?)\\\\\)', r'$\1$', part)
                    else:
                        # Forward replacements: \( to \\(, \) to \\), etc.
                        part = re.sub(r'\\\(', r'\\\\(', part)
                        part = re.sub(r'\\\)', r'\\\\)', part)
                        part = re.sub(r'\\\[', r'\\\\[', part)
                        part = re.sub(r'\\\]', r'\\\\]', part)
                        if gemini:
                            # Replace $...$ with \\(...\\)
                            part = re.sub(r'\$(.*?)\$', r'\\\\(\1\\\\)', part)
                processed_parts.append(part)
            
            return ''.join(processed_parts)

        updated_content = replace_mathjax(content, gemini, reset)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)

        action = "Reversed" if reset else "Fixed"
        print(f"{action} MathJax delimiters in: {filepath}")
        return True

    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def fix_mathjax_in_markdown(directory, max_files=None, gemini=False, reset=False):
    r"""
    Finds all markdown files in a directory and replaces instances of
    \( and \) with \\( and \\) respectively, skipping code blocks.
    If gemini is True, also replaces $ $ with \\( and \\).
    If reset is True, performs the reverse operation.

    Args:
        directory (str): The directory to search for markdown files.
        max_files (int, optional): Maximum number of files to process. Defaults to None (unlimited).
        gemini (bool, optional): Whether to also convert dollar sign notation to/from backslash notation.
        reset (bool, optional): Whether to reverse the replacements.
    """
    files_processed = 0
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".md"):
                filepath = os.path.join(root, filename)
                success = fix_mathjax_in_file(filepath, gemini, reset)
                if success:
                    files_processed += 1

                if max_files and files_processed >= max_files:
                    print(f"Maximum files processed ({max_files}). Exiting directory.")
                    return

def main():
    """
    Main function to process either a single file or directories.
    """
    parser = argparse.ArgumentParser(description="Fix or reverse MathJax delimiters in Markdown files.")
    parser.add_argument("--maxfiles", type=int, help="Maximum number of files to process.")
    parser.add_argument("--file", type=str, help="Path to a specific markdown file to process.")
    parser.add_argument("--gemini", action="store_true", help="Convert dollar sign notation ($...$) to/from backslash notation (\\\\(...\\\\)).")
    parser.add_argument("--reset", action="store_true", help="Reverse the MathJax delimiter changes (\\\\( to \\(, etc.).")
    args = parser.parse_args()

    if args.file:
        # Process a single file
        if os.path.exists(args.file) and args.file.endswith(".md"):
            fix_mathjax_in_file(args.file, args.gemini, args.reset)
        else:
            print(f"Invalid file path or not a markdown file: {args.file}")
    else:
        # Process directories
        directories = ["_posts", "original", "notes"]
        for directory in directories:
            if os.path.exists(directory):
                fix_mathjax_in_markdown(directory, max_files=args.maxfiles, gemini=args.gemini, reset=args.reset)
            else:
                print(f"Directory not found: {directory}")

if __name__ == "__main__":
    main()