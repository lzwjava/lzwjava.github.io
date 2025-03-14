import sys
import argparse

def clean_log(input_path=None, output_path=None):
    """
    Reads a log file, removes duplicate consecutive standard log lines,
    and writes the cleaned log to a specified file, defaulting to overwriting the input file.

    Args:
        input_path (str, optional): Path to the input log file. If None, reads from stdin.
        output_path (str, optional): Path to the output log file. If None, overwrites the input file.
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
        line = line.strip()
        parts = line.split(" | ", 3)

        if len(parts) == 4:
            level, _, thread, message = parts
            current_standard = (level, thread, message)

            if previous_standard is None or current_standard != previous_standard:
                print(line, file=outfile)
                previous_standard = current_standard
        else:
            print(line, file=outfile)
            previous_standard = None

    if output_path or input_path:
        outfile.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean duplicate log lines from a file or stdin and write to a file, defaulting to overwriting the input file.")
    parser.add_argument("input_path", nargs="?", type=str, help="Path to the input log file (optional, defaults to stdin)")
    parser.add_argument("-o", "--output_path", type=str, help="Path to the output log file (optional, defaults to overwriting input file)")
    args = parser.parse_args()

    clean_log(args.input_path, args.output_path)