from openrouter_client import call_openrouter_api
import argparse
import os

def suggest_file_name(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    original_name = os.path.basename(file_path)
    
    prompt = f"Suggest a concise and descriptive file name based on the following content and its original name '{original_name}':\n\n{content}\n\nRespond with only the suggested file name."
    
    response = call_openrouter_api(prompt)
    suggested_name = response.strip()  # Assuming the API returns the name as text
    
    return suggested_name

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Suggest a file name based on content.")
    parser.add_argument("file_path", type=str, help="Path to the file")
    args = parser.parse_args()
    
    new_name = suggest_file_name(args.file_path)
    print(new_name)
