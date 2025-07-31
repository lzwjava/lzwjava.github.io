from openrouter_client import call_openrouter_api
import argparse
import os

def rename_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    original_name = os.path.basename(file_path)
    dir_path = os.path.dirname(file_path)
    
    prompt = f"Suggest a concise and descriptive file name based on the following content and its original name '{original_name}':\n\n{content}\n\nRespond with only the suggested file name."
    
    response = call_openrouter_api(prompt)
    new_name = response.strip()  # Assuming the API returns the name as text
    
    new_path = os.path.join(dir_path, new_name)
    os.rename(file_path, new_path)
    
    return new_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rename file based on its content.")
    parser.add_argument("file_path", type=str, help="Path to the file")
    args = parser.parse_args()
    
    new_path = rename_file(args.file_path)
    print(f"File renamed to: {new_path}")
