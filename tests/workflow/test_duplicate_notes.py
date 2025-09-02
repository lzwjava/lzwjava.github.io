#!/usr/bin/env python3
"""
Test for detecting duplicate notes in the _posts directory.

This test compares notes by:
1. First comparing content length (approximate match)
2. Then using difflib.SequenceMatcher for content similarity > 90%
3. Grouping duplicates and reporting them
"""

import os
import difflib
from pathlib import Path
import unittest


@unittest.skip("Disabled: too strict skip now for duplicate notes")
class TestDuplicateNotes(unittest.TestCase):
    """Test case for detecting duplicate notes."""
    
    def setUp(self):
        """Set up test by finding all note files."""
        self.posts_dir = Path(__file__).parent.parent.parent / "_posts"
        self.note_files = []
        
        # Find all markdown files in _posts and subdirectories
        for lang_dir in self.posts_dir.iterdir():
            if lang_dir.is_dir():
                for note_file in lang_dir.glob("*.md"):
                    self.note_files.append(note_file)
    
    def _read_note_content(self, file_path):
        """Read and return the content of a note file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return ""
    
    def _are_notes_similar(self, content1, content2, threshold=0.9):
        """
        Check if two note contents are similar using difflib.
        
        Args:
            content1: First note content
            content2: Second note content
            threshold: Similarity threshold (default 0.9 = 90%)
        
        Returns:
            bool: True if content similarity > threshold
        """
        if not content1 or not content2:
            return False
        
        # Use SequenceMatcher for similarity
        similarity = difflib.SequenceMatcher(None, content1, content2).ratio()
        return similarity >= threshold
    
    def test_no_duplicate_notes(self):
        """Test that there are no duplicate notes in the _posts directory."""
        duplicates = []
        processed_files = set()
        
        # Group files by approximate length first
        length_groups = {}
        
        for file_path in self.note_files:
            content = self._read_note_content(file_path)
            if not content:
                continue
                
            content_length = len(content)
            
            # Group by approximate length (within 5% difference)
            found_group = False
            for group_length in length_groups:
                if abs(content_length - group_length) <= max(content_length * 0.05, 100):
                    length_groups[group_length].append((file_path, content))
                    found_group = True
                    break
            
            if not found_group:
                length_groups[content_length] = [(file_path, content)]
        
        # Check for actual duplicates within length groups
        for group_length, files_in_group in length_groups.items():
            if len(files_in_group) > 1:
                # Compare all pairs in this group
                for i, (file1, content1) in enumerate(files_in_group):
                    for j, (file2, content2) in enumerate(files_in_group[i+1:], i+1):
                        if file1 != file2 and (file1, file2) not in processed_files and (file2, file1) not in processed_files:
                            if self._are_notes_similar(content1, content2):
                                duplicates.append((file1, file2))
                                processed_files.add((file1, file2))
        
        # Report duplicates if found
        if duplicates:
            print("\n" + "="*60)
            print("DUPLICATE NOTES DETECTED!")
            print("="*60)
            
            for file1, file2 in duplicates:
                content1 = self._read_note_content(file1)
                content2 = self._read_note_content(file2)
                similarity = difflib.SequenceMatcher(None, content1, content2).ratio()
                
                print(f"\nDUPLICATE PAIR:")
                print(f"  File 1: {file1.relative_to(self.posts_dir.parent)}")
                print(f"  File 2: {file2.relative_to(self.posts_dir.parent)}")
                print(f"  Similarity: {similarity:.2%}")
                print(f"  Length 1: {len(content1)} chars")
                print(f"  Length 2: {len(content2)} chars")
                print("-" * 40)
            
            print(f"\nTOTAL DUPLICATE PAIRS: {len(duplicates)}")
            print("="*60)
            
            # Fail the test with a summary
            self.fail(f"Found {len(duplicates)} duplicate note pairs. See console output for details.")
        else:
            print(f"✓ No duplicate notes found among {len(self.note_files)} files.")


if __name__ == '__main__':
    unittest.main()