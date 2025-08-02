import os
import sys
import argparse

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))) 
from scripts.translation.openrouter_client import call_openrouter_api
from refactor_prompt import generate_refactor_prompt


def refactor_python_code(file_path):
    """
    Generate a refactor prompt and get AI suggestions for improving Python code.
    The resulting code is written directly back to the original file.
    """
    try:
        # Generate the refactor prompt
        prompt = generate_refactor_prompt(file_path)
        
        # Call the AI API for refactoring suggestions
        response = call_openrouter_api(
            prompt=prompt,
            model="kimi-k2"
        )
        
        # Write the refactored code back to the original file
        if not response.startswith("Error"):
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(response)
            return f"Successfully refactored {file_path}"
        else:
            return response
            
    except Exception as e:
        return f"Error during refactoring: {str(e)}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get AI suggestions for refactoring Python code")
    parser.add_argument("file_path", help="Path to the Python file to refactor")
    args = parser.parse_args()
    
    result = refactor_python_code(args.file_path)
    print(result)