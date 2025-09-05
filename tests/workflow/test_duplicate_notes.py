#!/usr/bin/env python3
"""
Fast duplicate detection for notes - group by date and compare within each date

Groups notes by date from filename (YYYY-MM-DD prefix) and checks for duplicates
within each date group using fast content comparison.

Usage:
    python test_duplicate_notes.py          # Test mode - reports duplicates
    python test_duplicate_notes.py --fix    # Fix mode - removes duplicates
"""

import argparse
import os
import re
from pathlib import Path
import unittest
import sys


class TestDuplicateNotes(unittest.TestCase):
    """Test case for detecting duplicate notes group by date."""
    
    def setUp(self):
        """Set up test by finding all note files."""
        self.notes_dir = Path(__file__).parent.parent.parent / "notes"
        self.note_files = []
        
        # Find all markdown files in notes directory
        if self.notes_dir.exists():
            self.note_files = list(self.notes_dir.glob("*.md"))
    
    def _extract_date_from_filename(self, filename):
        """Extract date from filename (format: YYYY-MM-DD-title)"""
        match = re.match(r'^(\d{4}-\d{2}-\d{2})-', filename)
        return match.group(1) if match else None
    
    def _extract_content_without_frontmatter(self, file_path):
        """Extract content without front matter"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Split on front matter
            sections = content.split('---', 2)
            if len(sections) >= 3:
                return sections[2].strip()
            
            # If no front matter, return content
            return content.strip()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return ""
    
    def _are_notes_quick_similar(self, content1, content2):
        """Fast similarity check between two note contents"""
        if not content1 or not content2:
            return False
        
        # Quick length check within 5% tolerance
        len1 = len(content1)
        len2 = len(content2)
        if max(len1, len2) == 0:
            return False
            
        if abs(len1 - len2) / max(len1, len2) > 0.05:
            return False
        
        # Fast content check - first 200 chars
        first200_1 = content1[:200]
        first200_2 = content2[:200]
        
        # Exact match for first 100 chars, 90% match for 200 chars
        if len(first200_1) >= 100 and len(first200_2) >= 100:
            if first200_1[:100] != first200_2[:100]:
                return False
            
            # 90% similarity for 200 chars
            matches = sum(c1 == c2 for c1, c2 in zip(first200_1[:200], first200_2[:200]))
            return matches >= 180  # 90% of 200
        
        return content1.strip() == content2.strip()
    
    def test_no_duplicate_notes(self):
        """Test that there are no duplicate notes within each date group."""
        if not self.note_files:
            print("✓ No note files found")
            return
            
        # Group notes by date
        date_groups = {}
        for file_path in self.note_files:
            date = self._extract_date_from_filename(file_path.name)
            if date:
                if date not in date_groups:
                    date_groups[date] = []
                date_groups[date].append(file_path)
            else:
                # Files without date prefixes go to special group
                if 'no_date' not in date_groups:
                    date_groups['no_date'] = []
                date_groups['no_date'].append(file_path)
        
        duplicates = []
        
        # Check for duplicates within each date group
        for date, files in date_groups.items():
            if len(files) <= 1:
                continue
                
            # Read all contents for this date
            contents = {}
            for file_path in files:
                content = self._extract_content_without_frontmatter(file_path)
                contents[file_path.name] = content
            
            # Check each pair only once
            file_names = list(contents.keys())
            for i, name1 in enumerate(file_names):
                for j, name2 in enumerate(file_names[i+1:], i+1):
                    if self._are_notes_quick_similar(contents[name1], contents[name2]):
                        duplicates.append(f"{date}: {name1} ~ {name2}")
        
        # Report results
        if duplicates:
            print("✗ DUPLICATE NOTES DETECTED:")
            print("-" * 40)
            for dup in sorted(duplicates):
                print(f"  {dup}")
            print(f"-" * 40)
            self.fail(f"Found {len(duplicates)} duplicate note pairs")
        else:
            total_files = len(self.note_files)
            total_dates = len(date_groups)
            print(f"✓ No duplicates found among {total_files} files across {total_dates} date groups")


if __name__ == '__main__':
    unittest.main()