import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from scripts.count.count_lang import count_files
from count_original import count_md_files_in_original
from scripts.generate.count_notes import count_notes


def get_file_counts():
    """Collect all file counts and return as a list of tuples (category, count)"""
    base_dir = "./"
    counts = []
    
    # Count Python files in scripts directory (excluding ml)
    scripts_dir = os.path.join(base_dir, "scripts")
    py_count = count_files(scripts_dir, [".py"], exclude_dirs=["ml"])
    counts.append(("Python files (scripts, excluding ml)", py_count))
    
    # Count Python files in scripts/ml directory
    ml_dir = os.path.join(base_dir, "scripts", "ml")
    ml_count = count_files(ml_dir, [".py"])
    counts.append(("Python files (scripts/ml)", ml_count))
    
    # Count C files
    c_dir = os.path.join(base_dir, "c")
    c_count = count_files(c_dir, [".c", ".h"])
    counts.append(("C files", c_count))
    
    # Count Rust files
    rust_dir = os.path.join(base_dir, "rust")
    rust_count = count_files(rust_dir, [".rs"])
    counts.append(("Rust files", rust_count))
    
    # Count C++ files
    cpp_dir = os.path.join(base_dir, "cpp")
    cpp_count = count_files(cpp_dir, [".cpp", ".hpp", ".h"])
    counts.append(("C++ files", cpp_count))
    
    # Count markdown files in original
    original_count = count_md_files_in_original(quiet=True)
    counts.append(("Markdown files (original)", original_count))
    
    # Count notes files
    notes_count = count_notes()
    counts.append(("Notes files", notes_count))
    
    return counts


def print_markdown_table(counts):
    """Print counts as a markdown table"""
    print("| File Type | Count |")
    print("|-----------|-------|")
    for category, count in counts:
        print(f"| {category} | {count} |")


if __name__ == "__main__":
    counts = get_file_counts()
    print_markdown_table(counts)
