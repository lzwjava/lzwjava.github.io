import os
import sys
import argparse

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from scripts.llm.openrouter_client import call_openrouter_api
from code_validation_utils import validate_code_quality


def generate_refactor_prompt(file_path):
    """Generate a refactor prompt for the given Python file with proper markdown formatting."""

    try:
        with open(file_path, "r", encoding="utf-8") as file:
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
- Each function should be below 30 lines for better maintainability.
- Include demo run examples for each function as comments.
- Improved variable names and overall structure for better readability.
- Although not explicitly added, the structure now makes it easier to add error handling where necessary.
- Only output the refactored code without any additional comments or explanations.

## Target File
`{file_path}`

## Code to Refactor
```python
{content}
```

"""
        return prompt
    except FileNotFoundError:
        return f"Error: The file {file_path} was not found."
    except Exception as e:
        return f"Error reading file {file_path}: {str(e)}"




def refactor_python_code(file_path, model="kimi-k2"):
    """
    Generate a refactor prompt and get AI suggestions for improving Python code.
    The resulting code is written directly back to the original file.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            original_code = file.read()
        
        prompt = generate_refactor_prompt(file_path)

        response = call_openrouter_api(prompt=prompt, model=model)

        if response.startswith("Error"):
            return response
        
        is_valid, validation_msg = validate_code_quality(original_code, response)
        if not is_valid:
            return f"Validation failed: {validation_msg}"
        
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(response)
        return f"Successfully refactored {file_path}"

    except Exception as e:
        return f"Error during refactoring: {str(e)}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Get AI suggestions for refactoring Python code"
    )
    parser.add_argument("file_path", help="Path to the Python file to refactor")
    parser.add_argument("--model", default="kimi-k2", 
                        help="Model to use for refactoring. Available models: claude-opus, claude-sonnet, gemini-flash, gemini-pro, kimi-k2, deepseek-v3, deepseek-v3.1, mistral-medium, qwen-coder, gpt-oss, gpt-5 (default: kimi-k2)")
    args = parser.parse_args()

    result = refactor_python_code(args.file_path, args.model)
    print(result)
