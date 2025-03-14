import sys
import argparse

def clean_log(input_path=None):
    """
    Reads a log file, removes duplicate consecutive standard log lines,
    and prints the cleaned log to standard output.

    Args:
        input_path (str, optional): Path to the input log file. If None, reads from stdin.
    """

    previous_standard = None

    # Determine the input source
    if input_path:
        try:
            with open(input_path, 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            print(f"Error: File not found at path: {input_path}", file=sys.stderr)
            sys.exit(1)
    else:
        lines = sys.stdin

    for line in lines:
        line = line.strip()
        parts = line.split(" | ", 3)

        if len(parts) == 4:
            level, _, thread, message = parts
            current_standard = (level, thread, message)

            if previous_standard is None or current_standard != previous_standard:
                print(line)
                previous_standard = current_standard
        else:
            print(line)
            previous_standard = None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean duplicate log lines from a file or stdin.")
    parser.add_argument("input_path", nargs="?", type=str, help="Path to the input log file (optional, defaults to stdin)")
    args = parser.parse_args()

    clean_log(args.input_path)