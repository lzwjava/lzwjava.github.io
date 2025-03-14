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

# Initialize the tracker for the last kept standard line
previous_standard = None

# Read lines from standard input
for line in sys.stdin:
    # Remove trailing whitespace (e.g., newlines)
    line = line.strip()
    
    # Split the line into parts using " | " as the separator, max 3 splits to get 4 parts
    parts = line.split(" | ", 3)
    
    # Check if the line is a standard log line (has exactly 4 parts)
    if len(parts) == 4:
        # Extract components, ignoring timestamp for comparison
        level, _, thread, message = parts
        current_standard = (level, thread, message)
        
        # Print the line if there's no previous standard line or if it differs from the last kept line
        if previous_standard is None or current_standard != previous_standard:
            print(line)
            previous_standard = current_standard
        # If it matches the previous standard line, skip it (continuous duplicate)
    else:
        # Non-standard line: print it and reset the tracker
        print(line)
        previous_standard = None
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