---
title: CSV Sorter Script
lang: en
layout: post
audio: false
translated: false
generated: true
---

I'll create a Python script that uses argparse to parse a CSV file path, sorts a single line of comma-separated values alphabetically, and outputs the result to a file named "name_sorted.csv".

```python
#!/usr/bin/env python3
import argparse
import csv

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Sort a single-line CSV file alphabetically')
    parser.add_argument('file_path', help='Path to the input CSV file')
    
    # Parse arguments
    args = parser.parse_args()
    
    try:
        # Read the input CSV file
        with open(args.file_path, 'r') as file:
            reader = csv.reader(file)
            # Get the first line only
            for row in reader:
                values = row
                break
        
        # Sort the values alphabetically
        sorted_values = sorted(values)
        
        # Write to output file
        with open('name_sorted.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(sorted_values)
        
        print(f"Successfully sorted values and saved to name_sorted.csv")
        
    except FileNotFoundError:
        print(f"Error: File '{args.file_path}' not found")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

```

This script:
1. Uses argparse to get the input file path
2. Opens the CSV file and reads only the first line
3. Sorts the values alphabetically
4. Writes the sorted values to "name_sorted.csv"

To run the script, save it to a file (e.g., "sort_csv.py"), make it executable if needed, and run it with the path to your CSV file:

```
python sort_csv.py path/to/your/file.csv
```

Would you like me to explain any part of the code in more detail?