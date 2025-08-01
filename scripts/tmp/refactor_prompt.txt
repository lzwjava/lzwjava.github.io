import argparse
import os
from sample_code import sample_code  # Importing the sample code function

def generate_refactor_prompt(file_path):
    """Generate a refactor prompt for the given Python file with proper markdown formatting."""
    
    sample = sample_code()
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        prompt = f"""# Refactor Prompt

## Instructions
Refactor the Python code below, focusing on:
- Improving readability
- Enhancing maintainability
- Following Python best practices
- Added if __name__ == "__main__": to ensure that the script can be both imported as a module and run as a standalone script.
- Do not use main() function, use other meaningful function names to let it import from other scripts.
- Used argparse to allow for flexible input of the params.
- Do not need docstring in each function.
- The code is divided into smaller, reusable functions, each with a single responsibility.
- Improved variable names and overall structure for better readability.
- Although not explicitly added, the structure now makes it easier to add error handling where necessary.
- Only output the refactored code without any additional comments or explanations.

## Target File
`{file_path}`

## Code to Refactor
```python
{content}
```

## Sample Reference Code
```python
{sample}
```
"""
        return prompt
    except FileNotFoundError:
        return f"Error: The file {file_path} was not found."
    except Exception as e:
        return f"Error reading file {file_path}: {str(e)}"

def save_prompt_to_md(prompt, original_path):
    """Save the generated prompt to a markdown file in scripts/prompt_md/ directory."""
    try:
        # Get the base filename without extension
        base_name = os.path.basename(original_path)
        file_name = os.path.splitext(base_name)[0] + ".md"
        
        # Define the output directory
        output_dir = "scripts/prompt_md"
        os.makedirs(output_dir, exist_ok=True)
        
        # Define the full output path
        output_path = os.path.join(output_dir, file_name)
        
        # Save the prompt to the markdown file
        with open(output_path, 'w', encoding='utf-8') as md_file:
            md_file.write(prompt)
        return f"Prompt saved to {output_path}"
    except Exception as e:
        return f"Error saving prompt to markdown file: {str(e)}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a refactor prompt for a Python file and save it as markdown.")
    parser.add_argument("file_path", help="Path to the Python file to refactor")
    args = parser.parse_args()
    
    prompt = generate_refactor_prompt(args.file_path)
    print(prompt)
    print(save_prompt_to_md(prompt, args.file_path))
