import argparse
import subprocess
from pathlib import Path

#!/usr/bin/env python3
"""
git_commit_filter.py
List all non-Python files touched by a given commit.

Usage:
    python git_commit_filter.py --repo /path/to/repo --commit abc123
"""



def list_non_python_files(repo: Path, commit: str) -> list[str]:
    """
    Return a list of non-Python file paths changed in the given commit.
    """
    cmd = [
        "git",
        "-C",
        str(repo),
        "diff-tree",
        "--no-commit-id",
        "--name-only",
        "-r",
        commit,
    ]
    try:
        output = subprocess.check_output(cmd, text=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"git diff-tree failed: {e}") from e

    files = output.strip().splitlines()
    non_python_files = [f for f in files if not f.lower().endswith(".py")]
    return non_python_files


def main() -> None:
    parser = argparse.ArgumentParser(
        description="List non-Python files changed by a specific git commit."
    )
    parser.add_argument(
        "--repo",
        type=Path,
        required=True,
        help="Path to the git repository.",
    )
    parser.add_argument(
        "--commit",
        required=True,
        help="Commit hash to inspect.",
    )

    args = parser.parse_args()

    try:
        files = list_non_python_files(args.repo, args.commit)
    except RuntimeError as e:
        print(e)
        return

    if files:
        print("Non-Python files changed:")
        for f in files:
            print(f)
    else:
        print("No non-Python files changed in this commit.")


if __name__ == "__main__":
    main()