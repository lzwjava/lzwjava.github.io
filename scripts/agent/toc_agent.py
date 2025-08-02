import re
import sys
import argparse
from pathlib import Path

#!/usr/bin/env python3
"""
Table of Contents Generator for Jekyll Posts
Generates TOC from markdown headers in Jekyll post files.
"""


def extract_headers(content):
    """Extract headers from markdown content."""
    # Match headers (## to ######)
    header_pattern = r'^(#{2,6})\s+(.+)$'
    headers = []
    
    for line_num, line in enumerate(content.split('\n'), 1):
        match = re.match(header_pattern, line.strip())
        if match:
            level = len(match.group(1))
            title = match.group(2).strip()
            headers.append({
                'level': level,
                'title': title,
                'line': line_num
            })
    
    return headers

def create_anchor(title):
    """Create Jekyll-compatible anchor from header title."""
    # Convert to lowercase, replace spaces with hyphens, remove special chars
    anchor = re.sub(r'[^\w\s-]', '', title.lower())
    anchor = re.sub(r'[-\s]+', '-', anchor)
    return anchor.strip('-')

def generate_toc(headers, min_level=2):
    """Generate table of contents from headers."""
    if not headers:
        return ""
    
    toc_lines = ["### Table of Contents", ""]
    
    for i, header in enumerate(headers):
        if header['level'] < min_level:
            continue
            
        # Calculate indentation (level 2 = 0 indent, level 3 = 4 spaces, etc.)
        indent = "    " * (header['level'] - min_level)
        
        # Create anchor link
        anchor = create_anchor(header['title'])
        
        # Format TOC entry
        toc_entry = f"{indent}- [{header['title']}](#{anchor})"
        toc_lines.append(toc_entry)
    
    return "\n".join(toc_lines)

def process_file(file_path, output_only=False):
    """Process a single Jekyll post file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        headers = extract_headers(content)
        toc = generate_toc(headers)
        
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
    parser = argparse.ArgumentParser(description='Generate TOC for Jekyll posts')
    parser.add_argument('files', nargs='*', help='Markdown files to process')
    parser.add_argument('--output-only', action='store_true', 
                       help='Output only TOC without file info')
    parser.add_argument('--min-level', type=int, default=2,
                       help='Minimum header level to include (default: 2)')
    
    args = parser.parse_args()
    
    if not args.files:
        # If no files specified, look for markdown files in current directory
        md_files = list(Path('.').glob('*.md'))
        if not md_files:
            print("No markdown files found. Please specify files to process.")
            sys.exit(1)
        args.files = md_files
    
    for file_path in args.files:
        process_file(file_path, args.output_only)

if __name__ == "__main__":
    main()