import os
import argparse
import subprocess
from dotenv import load_dotenv
import concurrent.futures
import frontmatter
from markdown_translate_client import translate_markdown_file

load_dotenv()

INPUT_DIR = "original"
MAX_THREADS = 10


def get_output_filename(filename, target_lang):
    orig_langs = ['en', 'zh', 'ja']
    for orig in orig_langs:
        suffix = f"-{orig}.md"
        if filename.endswith(suffix):
            return filename.replace(suffix, f"-{target_lang}.md")
    raise Exception(f"Unexpected filename format: {filename}")


def get_changed_files():
    changed_files = set()
    languages = ['ja', 'es', 'hi', 'zh', 'en', 'fr', 'de', 'ar', 'hant']
    print("Starting to scan files in the input directory...")
    for filename in os.listdir(INPUT_DIR):
        if not filename.endswith(".md"):
            print(f"Skipping non-markdown file: {filename}")
            continue
        # Extract orig_lang from filename
        orig_lang = None
        for possible in ['en', 'zh', 'ja']:
            if filename.endswith(f"-{possible}.md"):
                orig_lang = possible
                break
        if not orig_lang:
            print(f"Unexpected filename format: {filename}")
            continue
        
        input_file = os.path.join(INPUT_DIR, filename)
        print(f"Processing file: {input_file}")
        try:
            with open(input_file, 'r', encoding='utf-8') as infile:
                content = infile.read()
            if not content.lstrip().startswith('---'):
                raise Exception(f"No front matter found in markdown file: {input_file}")
            front_matter_dict, content_without_front_matter = frontmatter.parse(content)
            front_matter_dict = front_matter_dict or {}
            original_title = front_matter_dict.get('title', '')
            print(f"  Original language (from filename): {orig_lang}, Title: {original_title}")
            
            output_dir = f"_posts/{orig_lang}"
            output_filename = filename
            output_file = os.path.join(output_dir, output_filename)
            print(f"  Checking original output file: {output_file}")
            
            needs_retranslate_all = True  # Default to True if file doesn't exist
            if os.path.exists(output_file):
                with open(output_file, 'r', encoding='utf-8') as translated_infile:
                    translated_content = translated_infile.read()
                translated_front_matter_dict, translated_content_without_front_matter = frontmatter.parse(translated_content)
                translated_front_matter_dict = translated_front_matter_dict or {}
                translated_title = translated_front_matter_dict.get('title', '')
                print(f"  Translated title: {translated_title}")
                if translated_title == original_title and translated_content_without_front_matter.strip() == content_without_front_matter.strip():
                    needs_retranslate_all = False
                else:
                    print(f"  File {input_file} needs update due to content change in original lang {orig_lang}")
            else:
                print(f"  Original output file does not exist: {output_file}")
            
            for target_lang in languages:
                target_dir = f"_posts/{target_lang}"
                target_filename = get_output_filename(filename, target_lang)
                target_file = os.path.join(target_dir, target_filename)
                print(f"  Checking translation for language {target_lang}: {target_file}")
                if needs_retranslate_all or not os.path.exists(target_file):
                    changed_files.add((input_file, target_lang))
                    if needs_retranslate_all:
                        print(f"  File {input_file} needs update for {target_lang} due to content change")
                    else:
                        print(f"  File {input_file} is missing translation for {target_lang}")
                else:
                    print(f"  Translation for {target_lang} already exists, skipping.")
        except Exception as e:
            print(f"Error processing file {input_file}: {e}")
    print(f"Finished scanning. Total files needing updates: {len(changed_files)}")
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
            output_filename = get_output_filename(os.path.basename(filename), lang)
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