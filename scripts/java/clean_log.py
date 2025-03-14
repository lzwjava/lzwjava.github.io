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
        
        