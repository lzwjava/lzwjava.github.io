import sys
import os
import random
import subprocess
import argparse
from datetime import datetime, timedelta
from gpa import gpa
from create_note_from_clipboard import create_note

# Ensure repository root is on sys.path for importing scripts.* packages
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from scripts.llm.openrouter_client import MODEL_MAPPING
from scripts.content.fix_mathjax import fix_mathjax_in_file

def git_pull_rebase() -> None:
    """Run 'git pull --rebase' at the repository root.

    This is helpful when creating notes from multiple machines to avoid conflicts.
    If not in a git repo or git is unavailable, fail gracefully.
    """
    try:
        toplevel = subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"], text=True
        ).strip()
        print(f"[info] Running 'git pull --rebase' in {toplevel}...")
        # Do not raise on non-zero; we only warn to avoid blocking note creation
        subprocess.run(["git", "-C", toplevel, "pull", "--rebase"], check=False)
    except Exception as e:
        print(f"[warn] Skipping git pull --rebase: {e}")

def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description="Create a note; first positional arg is the model key."
    )
    parser.add_argument(
        "model",
        choices=sorted(MODEL_MAPPING.keys()),
        help=(
            "Model key to annotate in frontmatter; choices shown above."
        ),
    )
    parser.add_argument(
        "--random",
        action="store_true",
        help="Use a random date within last 180 days",
    )
    parser.add_argument(
        "--math",
        action="store_true",
        help="Fix MathJax delimiters in the created file before git add",
    )
    return parser.parse_args()

def generate_random_date():
    """Generate a random date within the last 180 days"""
    end_date = datetime.now()
    start_date = end_date - timedelta(days=180)
    
    random_days = random.randint(0, 180)
    random_date = start_date + timedelta(days=random_days)
    
    return random_date.strftime('%Y-%m-%d')

if __name__ == "__main__":
    # Ensure we are up to date to avoid conflicts across machines
    git_pull_rebase()

    args = parse_args()
    random_date = generate_random_date() if args.random else None

    created_path = create_note(date=random_date, note_model_key=args.model)

    # Optionally fix MathJax before invoking GPT-assisted git add/commit
    if args.math and created_path and os.path.exists(created_path):
        try:
            fix_mathjax_in_file(created_path)
        except Exception as e:
            print(f"[warn] MathJax fix failed for {created_path}: {e}")
    # Call gpa function
    gpa()
