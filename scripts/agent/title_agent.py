import re
import sys
import os
import argparse
from pathlib import Path
import frontmatter

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
    prompt = f"""Generate a short, simple, and clean title for this content. Output ONLY the title text with no markdown formatting, quotes, or additional text. Keep it concise and straightforward:
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
                # Clean the title by removing markdown formatting and extra text
                clean_title = title.strip()
                # Remove common markdown formatting
                clean_title = re.sub(r'^[*#]+|[*#]+$', '', clean_title).strip()
                # Remove quotes
                clean_title = clean_title.strip('"\'')
                title_pattern = r'^title:\s*".*?"$'
                
                # Split frontmatter into lines for processing
                frontmatter_lines = frontmatter_content.split('\n')
                title_found = False
                
                # Process each line to replace or add title
                updated_lines = []
                for line in frontmatter_lines:
                    if re.match(title_pattern, line):
                        updated_lines.append(f'title: "{clean_title}"')
                        title_found = True
                    else:
                        updated_lines.append(line)
                
                # If title was not found, add it at the beginning
                if not title_found:
                    updated_lines.insert(0, f'title: "{clean_title}"')
                
                updated_frontmatter = '\n'.join(updated_lines)
                
                # Reconstruct content with updated frontmatter
                before_frontmatter = '\n'.join(lines[:frontmatter_start_idx+1])  # Include opening ---
                after_frontmatter = '\n'.join(lines[frontmatter_end_idx:])  # Include closing ---
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
