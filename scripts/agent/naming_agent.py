import os
import sys
import argparse

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(script_dir, "..", "translation"))
from openrouter_client import call_openrouter_api

def get_name_suggestions(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    original_name = os.path.basename(file_path)
    
    prompt = f"Suggest 5 concise and descriptive file names based on the following content and its original name '{original_name}'. Respond with only the names, one per line:\n\n{content}"
    
    response = call_openrouter_api(prompt, model="anthropic/claude-3.5-sonnet")
    suggestions = response.strip().split('\n')
    return suggestions[:5]  # Ensure we only get 5 names

def rename_file(file_path):
    suggestions = get_name_suggestions(file_path)
    
    print("\nSuggested names:")
    for i, name in enumerate(suggestions, 1):
        print(f"{i}. {name}")
    print("0. Cancel")
    
    while True:
        choice = input("\nEnter your choice (0-5): ")
        if choice.isdigit() and 0 <= int(choice) <= 5:
            break
        print("Invalid choice. Please enter a number between 0 and 5.")
    
    choice = int(choice)
    if choice == 0:
        print("Operation cancelled.")
        return None
    
    new_name = suggestions[choice - 1]
    dir_path = os.path.dirname(file_path)
    new_path = os.path.join(dir_path, new_name)
    
    os.rename(file_path, new_path)
    return new_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rename file based on its content.")
    parser.add_argument("file_path", type=str, help="Path to the file")
    args = parser.parse_args()
    
    new_path = rename_file(args.file_path)
    if new_path:
        print(f"\nFile renamed to: {new_path}")
