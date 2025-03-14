import sys
import argparse
from difflib import SequenceMatcher

def clean_log(input_path=None, output_path=None, similarity_threshold=1.0):
    """
    Reads a log file, removes duplicate consecutive standard log lines based on similarity,
    and writes the cleaned log to a specified file, defaulting to overwriting the input file.

    Args:
        input_path (str, optional): Path to the input log file. If None, reads from stdin.
        output_path (str, optional): Path to the output log file. If None, overwrites the input file.
        similarity_threshold (float, optional): Similarity ratio (0.0 to 1.0) to consider lines as duplicates. Defaults to 1.0 (exact match).
    """

    previous_standard = None

    # Determine the input source
    if input_path:
        try:
            with open(input_path, 'r') as infile:
                lines = infile.readlines()
        except FileNotFoundError:
            print(f"Error: File not found at path: {input_path}", file=sys.stderr)
            sys.exit(1)
    else:
        lines = sys.stdin.readlines()  # Read all lines from stdin

    # Determine the output destination
    if output_path:
        try:
            outfile = open(output_path, 'w')
        except IOError:
            print(f"Error: Unable to open file for writing: {output_path}", file=sys.stderr)
            sys.exit(1)
    elif input_path:
        try:
            outfile = open(input_path, 'w')  # Overwrite the input file
        except IOError:
            print(f"Error: Unable to open file for writing: {input_path}", file=sys.stderr)
            sys.exit(1)
    else:
        outfile = sys.stdout  # Default to stdout if no input_path

    for line in lines:
        #line = line.strip() # remove strip()
        parts = line.split(" | ", 3)

        if len(parts) == 4:
            level, _, thread, message = parts
            current_standard = (thread, message)

            if previous_standard is None:
                print(f"First standard line: {line.strip()}")
                print(line, end='', file=outfile) # added end=''
                previous_standard = current_standard
            else:
                similarity = SequenceMatcher(None, ' '.join(current_standard), ' '.join(previous_standard)).ratio()
                print(f"Similarity: {similarity:.4f}, Threshold: {similarity_threshold:.4f}")
                if similarity < similarity_threshold:
                    print(line, end='', file=outfile) # added end=''
                    previous_standard = current_standard
                else:
                    print(f"Skipping duplicate line: {line.strip()}")
        else:
            print(f"Non-standard line: {line.strip()}")
            print(line, end='', file=outfile) # added end=''
            previous_standard = None

    if output_path or input_path:
        outfile.close()


def is_valid_similarity_threshold(value):
    """
    Check if the given value is a valid similarity threshold.
    """
    try:
        value = float(value)
    except ValueError:
        raise argparse.ArgumentTypeError("Similarity threshold must be a floating-point number.")
    if 0.0 <= value <= 1.0:
        return value
    else:
        raise argparse.ArgumentTypeError("Similarity threshold must be between 0.0 and 1.0.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean duplicate log lines from a file or stdin and write to a file, defaulting to overwriting the input file.")
    parser.add_argument("input_path", nargs="?", type=str, help="Path to the input log file (optional, defaults to stdin)")
    parser.add_argument("-o", "--output_path", type=str, help="Path to the output log file (optional, defaults to overwriting input file)")
    parser.add_argument("-s", "--similarity", type=is_valid_similarity_threshold, default=1.0, help="Similarity threshold (0.0-1.0) to consider lines as duplicates (default: 1.0)")
    args = parser.parse_args()

    clean_log(args.input_path, args.output_path, args.similarity)