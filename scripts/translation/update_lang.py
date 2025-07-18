import os
import re
import argparse
import subprocess
from dotenv import load_dotenv
import yaml
import concurrent.futures
from markdown_translate_client import translate_markdown_file

load_dotenv()

INPUT_DIR = "original"
MAX_THREADS = 10


def get_changed_files():
    changed_files = set()
    languages = ['ja', 'es', 'hi', 'zh', 'en', 'fr', 'de', 'ar', 'hant']
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".md"):
            input_file = os.path.join(INPUT_DIR, filename)
            for target_lang in languages:         
                output_dir = f"_posts/{target_lang}"
                if filename.endswith("-en.md"):
                    output_filename = filename.replace("-en.md", f"-{target_lang}.md")
                elif filename.endswith("-zh.md"):
                    output_filename = filename.replace("-zh.md", f"-{target_lang}.md")
                elif filename.endswith("-ja.md"):
                    output_filename = filename.replace("-ja.md", f"-{target_lang}.md")
                else:
                    raise Exception(f"Unexpected filename format: {filename}")
                output_file = os.path.join(output_dir, output_filename)
                if not os.path.exists(output_file):
                    changed_files.add((input_file, target_lang))
                    print(f"  File {input_file} is missing translation for {target_lang}")
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".md"):
            input_file = os.path.join(INPUT_DIR, filename)
            try:
                with open(input_file, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                front_matter_match = re.match(r'---(.*?)---', content, re.DOTALL)
                if not front_matter_match:
                    raise Exception(f"No front matter found in markdown file: {input_file}")
                front_matter = front_matter_match.group(1)
                content_without_front_matter = content[len(front_matter_match.group(0)):] if front_matter_match else content
                front_matter_dict = yaml.safe_load(front_matter) if front_matter else {}
                original_title = front_matter_dict.get('title', '')
                original_lang = front_matter_dict.get('lang', 'en')
                
                output_dir = f"_posts/{original_lang}"
                output_filename = filename
                output_file = os.path.join(output_dir, output_filename)
                if not os.path.exists(output_file):
                    for target_lang in languages:           
                        output_dir = f"_posts/{target_lang}"
                        if filename.endswith("-en.md"):
                            output_filename = filename.replace("-en.md", f"-{target_lang}.md")
                        elif filename.endswith("-zh.md"):
                            output_filename = filename.replace("-zh.md", f"-{target_lang}.md")
                        elif filename.endswith("-ja.md"):
                            output_filename = filename.replace("-ja.md", f"-{target_lang}.md")
                        else:
                            raise Exception(f"Unexpected filename format: {filename}")
                        output_file = os.path.join(output_dir, output_filename)
                        if not os.path.exists(output_file):
                            changed_files.add((input_file, target_lang))
                            print(f"  File {input_file} is missing translation for {target_lang}")
                else:                
                    with open(output_file, 'r', encoding='utf-8') as translated_infile:
                        translated_content = translated_infile.read()
                    target_front_matter_match = re.match(r'---\n(.*?)\n---', translated_content, re.DOTALL)
                    translated_front_matter = target_front_matter_match.group(1) if target_front_matter_match else ""
                    translated_content_without_front_matter = translated_content[len(target_front_matter_match.group(0)):] if target_front_matter_match else translated_content
                    translated_front_matter_dict = yaml.safe_load(translated_front_matter) if translated_front_matter else {}
                    translated_title = translated_front_matter_dict.get('title', '')
                    if translated_title != original_title or translated_content_without_front_matter.strip() != content_without_front_matter.strip():                        
                        for target_lang in languages:
                            changed_files.add((input_file, target_lang))
                            print(f"  File {input_file} needs update for {target_lang} due to content change")
                        try:
                            diff_command = ["diff", input_file, output_file]
                            process = subprocess.Popen(diff_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                            stdout, stderr = process.communicate()
                            if process.returncode == 1 and len(stdout) > 0:
                                print(f"  Diff:\n{stdout}")
                            else:
                                print(f"  Diff:\n{stdout}")                                
                                print(f"  Diff command failed with error: {stderr}")
                                print(f"  No diff available for {input_file} and {output_file}")
                        except FileNotFoundError:
                            print(f"  Diff command not found.")
                        except Exception as e:
                            print(f"  Error generating diff for {input_file}: {e}")
            except Exception as e:
                print(f"Error processing file {input_file}: {e}")
    return changed_files

def main():
    parser = argparse.ArgumentParser(description="Translate markdown files to a specified language.")
    parser.add_argument("--lang", type=str, default="all", help="Target language for translation (e.g., ja, es, all).")
    parser.add_argument("--dry_run", action="store_true", help="Perform a dry run without modifying files.")
    parser.add_argument("--file", type=str, default=None, help="Specific file to translate.")
    parser.add_argument("--max_files", type=int, default=None, help="Maximum number of files to process.")
    parser.add_argument("--model", type=str, default="deepseek", help="Model to use for translation (deepseek or mistral).")
    args = parser.parse_args()
    target_language = args.lang
    dry_run = args.dry_run
    input_file = args.file
    max_files = args.max_files
    model = args.model
    
    if target_language == "all":
        languages = ['ja', 'es', 'hi', 'zh', 'en', 'fr', 'de', 'ar', 'hant']
    else:
        languages = [target_language]
    
    if input_file:
        changed_files = {(input_file, lang) for lang in languages}
        total_files_to_process = len(changed_files)
    else:
        changed_files = get_changed_files()
        if max_files and len(changed_files) > max_files:
            changed_files = set(list(changed_files)[:max_files])
        total_files_to_process = len(changed_files)
    
    if dry_run:
        print(f"Total Markdown files to process: {total_files_to_process}")
        return
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = []
        for filename, lang in changed_files:
            input_file = filename
            output_dir = f"_posts/{lang}"
            os.makedirs(output_dir, exist_ok=True)
            output_filename = os.path.basename(filename).replace("-en.md", f"-{lang}.md").replace("-zh.md", f"-{lang}.md").replace("-ja.md", f"-{lang}.md")
            output_file = os.path.join(output_dir, output_filename)
            print(f"Submitting translation job for {filename} to {lang}...")
            future = executor.submit(translate_markdown_file, input_file, output_file, lang, model)
            futures.append(future)
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"A thread failed: {e}")
    print(f"Total Markdown files to process: {total_files_to_process}")

if __name__ == "__main__":
    main()