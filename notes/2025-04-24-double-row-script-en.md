---
title: Python Script to Double Row
lang: en
layout: post
audio: false
translated: false
generated: true
---

Here's a Python script that uses argparse to handle the repeat parameter, reads an Excel (.xls) file, doubles (or repeats n times) the values in the third row, and saves the output to a new file with "_plus.xls" appended to the original filename.

```python
import pandas as pd
import argparse
import os

def repeat_value(value, n):
    """Repeat the string representation of a value n times."""
    return str(value) * n

def process_excel(input_file, n):
    # Read the Excel file
    df = pd.read_excel(input_file, engine='xlrd')
    
    # Check if there are at least 3 rows
    if len(df) < 3:
        raise ValueError("Excel file must have at least 3 rows")
    
    # Process the third row (index 2)
    third_row = df.iloc[2].apply(lambda x: repeat_value(x, n))
    
    # Update the third row in the dataframe
    df.iloc[2] = third_row
    
    # Generate output filename
    base, ext = os.path.splitext(input_file)
    output_file = f"{base}_plus.xls"
    
    # Save to new Excel file
    df.to_excel(output_file, index=False, engine='xlwt')
    
    print(f"Processed file saved as: {output_file}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Double values in the third row of an Excel file")
    parser.add_argument("input_file", help="Path to the input Excel (.xls) file")
    parser.add_argument("-n", type=int, default=1, help="Number of times to repeat each value (default: 1)")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Process the Excel file
    process_excel(args.input_file, args.n)

if __name__ == "__main__":
    main()
```