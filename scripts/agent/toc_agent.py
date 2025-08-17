import re
import sys
import os
import argparse
from pathlib import Path

# Add parent directories to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from scripts.llm.openrouter_client import call_openrouter_api

#!/usr/bin/env python3
"""
Table of Contents Generator for Jekyll Posts
Generates TOC from markdown headers in Jekyll post files using AI.
"""


def generate_toc_with_ai(content):
    """Generate table of contents using AI."""
    print("Generating TOC with AI...")
    prompt = f"""Generate a concise table of contents for this markdown following STRICT rules:

1. List main headers (##) as numbered points (1., 2.)
2. For each main header, extract 3-5 key summarized points from section content
   - Summarize core ideas, NOT subheaders (5-7 words max per point)
   - Exclude redundant points
3. Format:
### Table of Contents

1. [Main Topic](#anchor)
   - Key insight 1
   - Key insight 2
   - Key insight 3

4. Never include subheaders as bullet points
5. Never exceed 5 points per section
6. Never use markdown code blocks

Example Output:
1. [Team Scaling](#team-scaling)
   - Plan long-term financial runway
   - Maintain elite hiring standards
   - Remove poor performers quickly

Markdown content:
{content}"""

    try:
        response = call_openrouter_api(prompt)
        stripped = response.strip()
        # Raise exception if markdown code blocks still appear despite prompt instruction
        if stripped.startswith('```') and stripped.endswith('```'):
            raise ValueError("TOC contains markdown code blocks despite prompt instructions")
        return stripped
    except Exception as e:
        print(f"Error calling AI API: {e}", file=sys.stderr)
        return None


def process_file(file_path, output_only=False):
    """Process a single Jekyll post file."""
    print(f"Processing file: {file_path}")
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
            
            # Insert TOC into the file after frontmatter
            frontmatter_end = content.find("---\n", 3) + 4  # Find second ---\n
            updated_content = content[:frontmatter_end] + "\n" + toc + "\n\n" + content[frontmatter_end:]
            
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(updated_content)

        return toc

    except Exception as e:
        print(f"Error processing {file_path}: {e}", file=sys.stderr)
        return None
    finally:
        print(f"Finished processing: {file_path}")


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
