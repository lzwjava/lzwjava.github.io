import sys
import random
import subprocess
import argparse
from datetime import datetime, timedelta
from gpa import gpa
from create_note_from_clipboard import create_note

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
    parser = argparse.ArgumentParser(description="Create a note (requires --note-model).")
    parser.add_argument("--random", action="store_true", help="Use a random date within last 180 days")
    parser.add_argument("--model", required=True, help="Model key to annotate in frontmatter (must match scripts.llm.openrouter_client.MODEL_MAPPING)")
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

    create_note(date=random_date, note_model_key=args.note_model)
    # Call gpa function
    gpa()
