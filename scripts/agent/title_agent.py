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
Title Updater for Jekyll Posts
Generates titles for Jekyll post files using AI.
"""


def generate_title_with_ai(content):
    """Generate a title using AI."""
    print("Generating title with AI...")
    prompt = f"""Generate a concise title:
{content}"""

    try:
        response = call_openrouter_api(prompt)
        stripped = response.strip()
        return stripped
    except Exception as e:
        print(f"Error calling AI API: {e}", file=sys.stderr)
        return None


def process_file(file_path, output_only=False):
    """Process a single Jekyll post file to update its title."""
    print(f"Processing file: {file_path}")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        title = generate_title_with_ai(content)

        if title is None:
            return None

        if output_only:
            print(title)
        else:
            print(f"Generated title for {file_path}:")
            print(title)
            print()
            
            # Update title in frontmatter
            lines = content.split('\n')
            in_frontmatter = False
            frontmatter_start_idx = -1
            frontmatter_end_idx = -1
            
            # Find frontmatter boundaries
            for i, line in enumerate(lines):
                if line.strip() == '---':
                    if frontmatter_start_idx == -1:
                        frontmatter_start_idx = i
                        in_frontmatter = True
                    elif in_frontmatter:
                        frontmatter_end_idx = i
                        break
            
            if frontmatter_start_idx != -1 and frontmatter_end_idx != -1:
                # Extract frontmatter
                frontmatter_lines = lines[frontmatter_start_idx+1:frontmatter_end_idx]
                frontmatter_content = '\n'.join(frontmatter_lines)
                
                # Replace or add title in frontmatter
                title_pattern = r'title:\s*".*?"'
                if re.search(title_pattern, frontmatter_content):
                    updated_frontmatter = re.sub(title_pattern, f'title: "{title}"', frontmatter_content)
                else:
                    # Add title if not present
                    updated_frontmatter = f'title: "{title}"\n{frontmatter_content}'
                
                # Reconstruct content with updated frontmatter
                before_frontmatter = '\n'.join(lines[:frontmatter_start_idx+1])
                after_frontmatter = '\n'.join(lines[frontmatter_end_idx:])
                updated_content = f"{before_frontmatter}\n{updated_frontmatter}\n{after_frontmatter}"
                
                # Write updated content back to file
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(updated_content)
            else:
                print("Error: Could not find frontmatter boundaries", file=sys.stderr)

        return title

    except Exception as e:
        print(f"Error processing {file_path}: {e}", file=sys.stderr)
        return None
    finally:
        print(f"Finished processing: {file_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate titles for Jekyll posts using AI"
    )
    parser.add_argument("files", nargs="*", help="Markdown files to process")
    parser.add_argument(
        "--output-only", action="store_true", help="Output only title without file info"
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
