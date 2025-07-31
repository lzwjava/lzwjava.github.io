import os
import sys

# Add the project root to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

# Import using direct file paths
script_dir = os.path.dirname(os.path.abspath(__file__))

# Import refactor_prompt from current directory
from refactor_prompt import generate_refactor_prompt

# Import openrouter_client from translation directory
sys.path.append(os.path.join(script_dir, "..", "translation"))
from openrouter_client import call_openrouter_api
import argparse


def refactor_python_code(file_path):
    """
    Generate a refactor prompt and get AI suggestions for improving Python code.
    """
    try:
        # Generate the refactor prompt
        prompt = generate_refactor_prompt(file_path)
        
        # Call the AI API for refactoring suggestions
        response = call_openrouter_api(
            prompt=prompt,
            model="moonshotai/kimi-k2:free"
        )
        
        return response
    except Exception as e:
        return f"Error during refactoring: {str(e)}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get AI suggestions for refactoring Python code")
    parser.add_argument("file_path", help="Path to the Python file to refactor")
    args = parser.parse_args()
    
    result = refactor_python_code(args.file_path)
    print(result)