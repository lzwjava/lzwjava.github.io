---
title: Python Script to Double Row
lang: en
layout: post
audio: false
translated: false
generated: true
---

Here's the updated Python script modified to work with .xlsx files instead of .xls files. It uses `openpyxl` for handling .xlsx files, keeps the same functionality of repeating values in the third row based on the provided parameter, and saves the output to a new .xlsx file with "_plus.xlsx" appended to the original filename. The artifact_id is reused since this is an update to the previous artifact.

```python
import pandas as pd
import argparse
import os

def repeat_value(value, n):
    """Repeat the string representation of a value n times."""
    return str(value) * n

def process_excel(input_file, n):
    # Read the Excel file
    df = pd.read_excel(input_file, engine='openpyxl')
    
    # Check if there are at least 3 rows
    if len(df) < 3:
        raise ValueError("Excel file must have at least 3 rows")
    
    # Process the third row (index 2)
    third_row = df.iloc[2].apply(lambda x: repeat_value(x, n))
    
    # Update the third row in the dataframe
    df.iloc[2] = third_row
    
    # Generate output filename
    base, ext = os.path.splitext(input_file)
    output_file = f"{base}_plus.xlsx"
    
    # Save to new Excel file
    df.to_excel(output_file, index=False, engine='openpyxl')
    
    print(f"Processed file saved as: {output_file}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Double values in the third row of an Excel file")
    parser.add_argument("input_file", help="Path to the input Excel (.xlsx) file")
    parser.add_argument("-n", type=int, default=1, help="Number of times to repeat each value (default: 1)")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Process the Excel file
    process_excel(args.input_file, args.n)

if __name__ == "__main__":
    main()
```