import unittest
import re
import os

def scan_markdown_files_for_pronoun_usage():
    """Scan English markdown files for excessive usage of 'you' and 'we' pronouns."""
    results = []
    
    # Only scan original directory for English markdown files
    original_dir = 'original'
    
    if not os.path.exists(original_dir):
        return results
        
    # Walk through all subdirectories in original
    for root, dirs, files in os.walk(original_dir):
        for filename in files:
            if not filename.endswith('-en.md'):
                continue
                
            file_path = os.path.join(root, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Remove YAML front matter
                if content.startswith('---'):
                    parts = content.split('---', 2)
                    if len(parts) >= 3:
                        content = parts[2]
                
                # Count total words (excluding markdown syntax)
                # Remove markdown formatting
                clean_content = re.sub(r'[#*`\[\]()_]', ' ', content)
                clean_content = re.sub(r'\s+', ' ', clean_content).strip()
                
                if not clean_content:
                    continue
                    
                words = clean_content.lower().split()
                total_words = len(words)
                
                if total_words == 0:
                    continue
                
                # Count 'you', 'we' pronouns (case insensitive)
                pronoun_count = 0
                for word in words:
                    # Remove punctuation for exact matching
                    clean_word = re.sub(r'[^\w]', '', word)
                    if clean_word in ['you', 'we', "you're", "you'll", "you've", "you'd", "we're", "we'll", "we've", "we'd"]:
                        pronoun_count += 1
                
                # Calculate ratio
                pronoun_ratio = pronoun_count / total_words if total_words > 0 else 0
                
                results.append({
                    'file': file_path,
                    'total_words': total_words,
                    'pronoun_count': pronoun_count,
                    'pronoun_ratio': pronoun_ratio
                })
                        
            except (UnicodeDecodeError, IOError) as e:
                # Skip files that can't be read
                continue
    
    return results

class TestYouUsage(unittest.TestCase):
    def test_you_usage(self):
        """Test that English markdown files don't have excessive 'you'/'we' pronoun usage (>0.6 ratio)."""
        pronoun_results = scan_markdown_files_for_pronoun_usage()
        
        failing_files = []
        for result in pronoun_results:
            if result['pronoun_ratio'] > 0.6:
                failing_files.append(result)
        
        if failing_files:
            details = "\n".join([
                f"{result['file']} - {result['pronoun_count']}/{result['total_words']} words ({result['pronoun_ratio']:.3f} ratio)"
                for result in failing_files
            ])
            self.fail(f"Found {len(failing_files)} files with excessive 'you'/'we' usage (>0.6 ratio):\n{details}")

if __name__ == '__main__':
    unittest.main()