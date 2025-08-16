import subprocess
import argparse
import sys
import os
import shutil

def check_ripgrep():
    """Check if ripgrep is installed."""
    if not shutil.which('rg'):
        print("Error: ripgrep (rg) is not installed.")
        print("Please install it first:")
        print("  macOS: brew install ripgrep")
        print("  Ubuntu/Debian: sudo apt-get install ripgrep")
        print("  Windows: scoop install ripgrep")
        sys.exit(1)

def search_posts(query, ignore_case=False):
    """Search posts using ripgrep."""
    try:
        check_ripgrep()
        
        cmd = [shutil.which('rg')]
        if ignore_case:
            cmd.append('-i')
        
        # Add context lines around matches
        cmd.extend(['-C', '2'])
        
        # Show line numbers
        cmd.append('-n')
        
        # Add search pattern
        cmd.append(query)
        
        # Search in specific directories
        cmd.extend([
            '_posts/en',
            'original',
            'notes'
        ])
        
        # Execute search
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode not in [0, 1]:  # 1 means no matches found
            print("Error executing search command")
            print(result.stderr)
            return
            
        if result.stdout:
            print(result.stdout)
        else:
            print("No matches found")
            
    except subprocess.CalledProcessError as e:
        print(f"Error executing search: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search posts in the repository")
    parser.add_argument("query", help="Search pattern to look for")
    parser.add_argument("-i", "--ignore-case", action="store_true", 
                      help="Case insensitive search")
    
    args = parser.parse_args()
    search_posts(args.query, args.ignore_case)