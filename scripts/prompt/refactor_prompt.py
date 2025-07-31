import argparse

def generate_refactor_prompt(file_path):
    """Generate a refactor prompt for the given Python file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        prompt = f"""Refactor below Python code:

<currentDocument>
I have the following code in a file called `{file_path}`:
<selection>
{content}
</selection>
</currentDocument>
"""
        return prompt
    except FileNotFoundError:
        return f"Error: The file {file_path} was not found."
    except Exception as e:
        return f"Error reading file {file_path}: {str(e)}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a refactor prompt for a Python file.")
    parser.add_argument("file_path", help="Path to the Python file to refactor")
    args = parser.parse_args()
    
    print(generate_refactor_prompt(args.file_path))
