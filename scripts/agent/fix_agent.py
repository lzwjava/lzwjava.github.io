import sys
import argparse
from pathlib import Path

import os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))) 

from scripts.translation.openrouter_client import call_openrouter_api
import subprocess

def run_script(script_path):
    """Run a Python script and capture its output."""
    try:
        result = subprocess.run(['python3', script_path], capture_output=True, text=True)
        return result.stdout + result.stderr
    except Exception as e:
        return str(e)

def fix_script(script_path, error_message, model):
    """Use OpenRouter API to suggest fixes for the script errors and apply them."""
    prompt = f"Error in script {script_path}:\n{error_message}\nPlease provide only the corrected code for the entire script without any explanations, markdown syntax, or additional text."
    response = call_openrouter_api(prompt, model=model)
    # Remove any markdown code block syntax from the response
    response = response.replace("```python", "").replace("```", "")
    # Write the fixed code back to the original script file
    try:
        with open(script_path, 'w') as f:
            f.write(response.strip())
        return f"Applied fix to {script_path}"
    except Exception as e:
        return f"Failed to apply fix: {str(e)}"
    
def main():
    parser = argparse.ArgumentParser(description="Run and fix Python scripts.")
    parser.add_argument('script', type=str, help="Path to the Python script to run and fix.")
    parser.add_argument('--model', type=str, default='deepseek/deepseek-chat-v3-0324:free',
                        choices=[
                            'anthropic/claude-opus-4',
                            'anthropic/claude-sonnet-4',
                            'google/gemini-2.5-flash',
                            'deepseek/deepseek-chat-v3-0324:free',
                            'google/gemini-2.5-pro'
                        ],
                        help="Model to use for OpenRouter API.")
    args = parser.parse_args()
    
    script_path = Path(args.script)
    if not script_path.exists():
        print(f"Script {script_path} does not exist.")
        sys.exit(1)
    
    # Run the script initially to capture output
    print("Running script for the first time...")
    output = run_script(script_path)
    print("Initial Script Output:")
    print(output)
    
    if "Traceback" in output or "Error" in output:
        print("Error detected, attempting to fix...")
        fix_result = fix_script(script_path, output, args.model)
        print("Fix Result:")
        print(fix_result)
        # Re-run the script after applying the fix
        print("Re-running script after fix...")
        output = run_script(script_path)
        print("Updated Script Output:")
        print(output)
    
    if "Traceback" in output or "Error" in output:
        print("Error still present after fix attempt.")
        print("Final Script Output:")
        print(output)

if __name__ == "__main__":
    main()
