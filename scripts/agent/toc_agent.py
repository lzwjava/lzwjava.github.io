import re
import sys
import argparse
from pathlib import Path
from scripts.llm.openrouter_client import call_openrouter_api

#!/usr/bin/env python3
"""
Table of Contents Generator for Jekyll Posts
Generates TOC from markdown headers in Jekyll post files using AI.
"""


def generate_toc_with_ai(content):
    """Generate table of contents using AI."""
    prompt = f"""Please generate a table of contents for the following markdown content. 
Follow these rules:
1. Only include headers from level 2 (##) to level 6 (######)
2. Create Jekyll-compatible anchor links (lowercase, hyphens for spaces, no special chars)
3. Use proper indentation (4 spaces per level)
4. Start with "### Table of Contents" as the title
5. Format as: `- [Header Title](#anchor-link)`

Markdown content:
{content}

Generate only the table of contents in markdown format:"""

    try:
        response = call_openrouter_api(prompt)
        return response.strip()
    except Exception as e:
        print(f"Error calling AI API: {e}", file=sys.stderr)
        return None


def process_file(file_path, output_only=False):
    """Process a single Jekyll post file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        toc = generate_toc_with_ai(content)

        if toc is None:
            return None

        if output_only:
            print(toc)
        else:
            print(f"Generated TOC for {file_path}:")
            print(toc)
            print()

        return toc

    except Exception as e:
        print(f"Error processing {file_path}: {e}", file=sys.stderr)
        return None


def main():
    parser = argparse.ArgumentParser(
        description="Generate TOC for Jekyll posts using AI"
    )
    parser.add_argument("files", nargs="*", help="Markdown files to process")
    parser.add_argument(
        "--output-only", action="store_true", help="Output only TOC without file info"
    )

    args = parser.parse_args()

    if not args.files:
        # If no files specified, look for markdown files in current directory
        md_files = list(Path(".").glob("*.md"))
        if not md_files:
            print("No markdown files found. Please specify files to process.")
            sys.exit(1)
        args.files = md_files

    for file_path in args.files:
        process_file(file_path, args.output_only)


if __name__ == "__main__":
    main()
