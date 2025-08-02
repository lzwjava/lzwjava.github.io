import sys
import argparse
from pathlib import Path
from scripts.translation.openrouter_client import call_openrouter_api
import subprocess

def run_script(script_path):
    """Run a Python script and capture its output."""
    try:
        result = subprocess.run(['python', script_path], capture_output=True, text=True)
        return result.stdout + result.stderr
    except Exception as e:
        return str(e)

def fix_script(script_path, error_message):
    """Use OpenRouter API to suggest fixes for the script errors."""
    prompt = f"Error in script {script_path}:\n{error_message}\nPlease suggest a fix."
    response = call_openrouter_api(prompt)
    return response

def main():
    parser = argparse.ArgumentParser(description="Run and fix Python scripts.")
    parser.add_argument('script', type=str, help="Path to the Python script to run and fix.")
    args = parser.parse_args()
    
    script_path = Path(args.script)
    if not script_path.exists():
        print(f"Script {script_path} does not exist.")
        sys.exit(1)
    
    print(f"Running script: {script_path}")
    output = run_script(script_path)
    print("Script Output:")
    print(output)
    
    if "Traceback" in output or "Error" in output:
        print("Error detected, attempting to fix...")
        fix_suggestion = fix_script(script_path, output)
        print("Fix Suggestion:")
        print(fix_suggestion)

if __name__ == "__main__":
    main()
