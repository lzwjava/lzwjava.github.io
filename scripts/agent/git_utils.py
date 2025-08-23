#!/usr/bin/env python3
"""
Git utilities for Jekyll post processing
"""

import subprocess
import os
import re
import sys


def get_git_diff_lines(file_path):
    """Get the line numbers that have changes according to git diff."""
    try:
        # Get the git diff for the file
        result = subprocess.run(
            ["git", "diff", "HEAD", file_path],
            capture_output=True,
            text=True,
            cwd=os.path.dirname(os.path.abspath(file_path))
        )
        
        if result.returncode != 0:
            print(f"Error getting git diff: {result.stderr}", file=sys.stderr)
            return set()
        
        diff_output = result.stdout
        if not diff_output.strip():
            print(f"No changes detected in {file_path}")
            return set()
        
        # Parse the diff to get changed line numbers
        changed_lines = set()
        current_line = 0
        
        for line in diff_output.split('\n'):
            if line.startswith('@@'):
                # Parse the @@ -old_start,old_count +new_start,new_count @@ format
                match = re.search(r'@@\s+-\d+(?:,\d+)?\s+\+(\d+)(?:,(\d+))?\s+@@', line)
                if match:
                    current_line = int(match.group(1))
            elif line.startswith('+') and not line.startswith('+++'):
                # This is an added line
                changed_lines.add(current_line)
                current_line += 1
            elif line.startswith(' '):
                # This is a context line
                current_line += 1
            # Skip lines starting with '-' as they are deleted lines
        
        return changed_lines
    
    except Exception as e:
        print(f"Error getting git diff for {file_path}: {e}", file=sys.stderr)
        return set()


def extract_changed_content(content, changed_lines):
    """Extract only the changed lines and some context around them."""
    if not changed_lines:
        return ""
    
    lines = content.split('\n')
    content_to_fix = []
    
    # Group consecutive line numbers and add context
    sorted_lines = sorted(changed_lines)
    groups = []
    current_group = [sorted_lines[0]]
    
    for line_num in sorted_lines[1:]:
        if line_num - current_group[-1] <= 3:  # Group if within 3 lines
            current_group.append(line_num)
        else:
            groups.append(current_group)
            current_group = [line_num]
    groups.append(current_group)
    
    # Extract content for each group with context
    for group in groups:
        start_line = max(1, group[0] - 2)  # Add 2 lines of context before
        end_line = min(len(lines), group[-1] + 2)  # Add 2 lines of context after
        
        group_content = '\n'.join(lines[start_line-1:end_line])
        content_to_fix.append(group_content)
    
    return '\n\n---\n\n'.join(content_to_fix)


def apply_grammar_fixes_to_original(original_content, changed_content, fixed_content, changed_lines):
    """Apply grammar fixes from the fixed content back to the original content."""
    # For simplicity, we'll do a basic replacement of the changed sections
    # This assumes the fixed content maintains the same structure
    
    original_lines = original_content.split('\n')
    fixed_lines = fixed_content.split('\n')
    
    # Find the sections that were changed and replace them
    # This is a simplified approach - we'll replace the content around the changed lines
    if changed_lines:
        min_line = min(changed_lines)
        max_line = max(changed_lines)
        
        # Replace the section with fixed content
        # Add some context buffer
        start_idx = max(0, min_line - 3)
        end_idx = min(len(original_lines), max_line + 2)
        
        # Split the file into before, changed section, and after
        before_section = original_lines[:start_idx]
        after_section = original_lines[end_idx:]
        
        # Combine with fixed content
        new_lines = before_section + fixed_lines + after_section
        return '\n'.join(new_lines)
    
    return original_content