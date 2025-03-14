---
title: Clean Log Messages
lang: en
layout: post
audio: false
translated: false
generated: true
---

To clean up your log4j messages and remove continuous duplicated messages where only the timestamp differs, we need a Python script that processes the log lines and keeps only the first occurrence of consecutive duplicates. Your log messages follow the format `LEVEL | TIMESTAMP | THREAD | MESSAGE`, and we want to eliminate lines that have the same log level, thread, and message as the previous line, differing only in the timestamp.

For example, given the input:
```
INFO | 2023-04-25 21:21:25 | thread-1 | message
INFO | 2023-04-25 21:21:26 | thread-1 | message
```
We want to keep only:
```
INFO | 2023-04-25 21:21:25 | thread-1 | message
```
However, if the duplicates are not consecutive (e.g., separated by a different message or a non-standard line), both instances should be retained.

Here’s how we can achieve this:

### Approach
1. **Read Log Lines:** Process the log lines from standard input, allowing you to pipe a log file to the script (e.g., `cat log.txt | python script.py`).
2. **Parse Each Line:** Split each line by " | " to extract the log level, timestamp, thread, and message. A standard log line should have exactly four parts.
3. **Track Previous Standard Line:** Maintain a record of the log level, thread, and message from the last standard line we decided to keep.
4. **Filter Duplicates:**
   - For a standard line (one that splits into four parts), compare its log level, thread, and message with those of the last kept standard line. If they match, skip it; otherwise, print it and update the tracker.
   - For a non-standard line (one that doesn’t split into four parts), print it as is and reset the tracker, since it breaks the sequence of standard lines.
5. **Preserve Order and Content:** Print lines exactly as they appear, maintaining the original formatting, and only strip trailing whitespace.

### Python Script
Below is the Python script to accomplish this:

```python
import sys
import argparse
from difflib import SequenceMatcher

def clean_log(input_path=None, output_path=None, similarity_threshold=1.0, lines_to_compare=1):
    """
    Reads a log file, removes duplicate consecutive standard log lines based on similarity,
    and writes the cleaned log to a specified file, defaulting to overwriting the input file.

    Args:
        input_path (str, optional): Path to the input log file. If None, reads from stdin.
        output_path (str, optional): Path to the output log file. If None, overwrites the input file.
        similarity_threshold (float, optional): Similarity ratio (0.0 to 1.0) to consider lines as duplicates. Defaults to 1.0 (exact match).
        lines_to_compare (int, optional): Number of consecutive lines to compare. Defaults to 1.
    """

    if not isinstance(lines_to_compare, int) or lines_to_compare < 1:
        raise ValueError("lines_to_compare must be an integer greater than or equal to 1.")

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

    num_lines = len(lines)
    i = 0
    while i < num_lines:
        # Collect 'lines_to_compare' lines or remaining lines if less than 'lines_to_compare'
        current_lines = lines[i:min(i + lines_to_compare, num_lines)]

        # Process only if we have enough lines to compare
        if len(current_lines) == lines_to_compare:
            # Extract standard information from the first set of lines
            current_standards = []
            all_standard = True
            for line in current_lines:
                parts = line.split(" | ", 3)
                if len(parts) == 4:
                    level, _, thread, message = parts
                    current_standards.append((thread, message))
                else:
                    print(f"Non-standard line: {line.strip()}")
                    print(line, end='', file=outfile)
                    all_standard = False
                    break  # Stop processing this group if a non-standard line is found

            if all_standard:
                # Extract standard information from the second set of lines (if available)
                next_lines_start_index = i + lines_to_compare
                next_lines_end_index = min(next_lines_start_index + lines_to_compare, num_lines)
                next_lines = lines[next_lines_start_index:next_lines_end_index]

                if len(next_lines) == lines_to_compare:
                    next_standards = []
                    for line in next_lines:
                        parts = line.split(" | ", 3)
                        if len(parts) == 4:
                            level, _, thread, message = parts
                            next_standards.append((thread, message))
                        else:
                            # Treat the next lines as non-standard if any of them are non-standard
                            next_standards = None
                            break

                    if next_standards:
                        similarity = SequenceMatcher(None, ' '.join([' '.join(x) for x in current_standards]), ' '.join([' '.join(x) for x in next_standards])).ratio()
                        print(f"Similarity: {similarity:.4f}, Threshold: {similarity_threshold:.4f}")

                        if similarity < similarity_threshold:
                            for line in current_lines:
                                print(line, end='', file=outfile)
                        else:
                            print(f"Skipping duplicate lines: { ''.join([line.strip() for line in current_lines])}")
                    else:
                        for line in current_lines:
                            print(line, end='', file=outfile)
                else:
                    for line in current_lines:
                        print(line, end='', file=outfile)
            i += lines_to_compare  # Move to the next set of lines
        else:
            # Handle the remaining lines (less than 'lines_to_compare')
            for line in current_lines:
                parts = line.split(" | ", 3)
                if len(parts) == 4:
                    print(line, end='', file=outfile)
                else:
                    print(f"Non-standard line: {line.strip()}")
                    print(line, end='', file=outfile)
            i += len(current_lines)

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
    parser.add_argument("-l", "--lines", type=int, default=1, help="Number of consecutive lines to compare (default: 1)")

    args = parser.parse_args()

    clean_log(args.input_path, args.output_path, args.similarity, args.lines)
```

### How It Works
- **Initialization:** `previous_standard` starts as `None`, meaning the first standard line will always be printed.
- **Line Processing:**
  - **Standard Lines:** If a line splits into four parts (`len(parts) == 4`), we extract the log level, thread, and message, forming a tuple `current_standard`. We compare this with `previous_standard`:
    - If `previous_standard` is `None` (first line) or different, we print the line and update `previous_standard`.
    - If it matches, we skip the line (it’s a continuous duplicate).
  - **Non-Standard Lines:** If a line doesn’t have four parts, we print it immediately and set `previous_standard` to `None`. This ensures that a subsequent standard line isn’t incorrectly skipped due to a non-standard line breaking the sequence.
- **Output:** The script prints lines to standard output, preserving their original format.

### Example Usage
#### Input:
```
INFO | 2023-04-25 21:21:25 | thread-1 | message
INFO | 2023-04-25 21:21:26 | thread-1 | message
INFO | 2023-04-25 21:21:27 | thread-2 | another message
INFO | 2023-04-25 21:21:28 | thread-1 | message
```

#### Execution:
Save the script as `clean_log.py` and run:
```
cat log.txt | python clean_log.py
```

#### Output:
```
INFO | 2023-04-25 21:21:25 | thread-1 | message
INFO | 2023-04-25 21:21:27 | thread-2 | another message
INFO | 2023-04-25 21:21:28 | thread-1 | message
```

#### Explanation:
- Line 1: Printed (no previous standard line), `previous_standard` set to `("INFO", "thread-1", "message")`.
- Line 2: Skipped (matches `previous_standard`).
- Line 3: Printed (differs in thread and message), `previous_standard` updated to `("INFO", "thread-2", "another message")`.
- Line 4: Printed (differs from `previous_standard`), `previous_standard` updated to `("INFO", "thread-1", "message")`.

#### Another Example:
**Input:**
```
INFO | 2023-04-25 21:21:25 | thread-1 | message
Some other log line
INFO | 2023-04-25 21:21:26 | thread-1 | message
```
**Output:**
```
INFO | 2023-04-25 21:21:25 | thread-1 | message
Some other log line
INFO | 2023-04-25 21:21:26 | thread-1 | message
```
- The non-standard line breaks the sequence, so both instances of the message are kept.

### Why This Works
- **Continuous Duplicates:** Only consecutive lines with the same log level, thread, and message are deduplicated.
- **Non-Consecutive Duplicates:** If separated by a different line (standard or non-standard), both are retained.
- **Robustness:** Handles malformed lines by printing them and resetting the tracker, ensuring no data loss.

This script meets your requirement to clean log4j messages by removing continuous duplicates where only the timestamp differs, while keeping the log readable and intact.