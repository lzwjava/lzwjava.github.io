import os
import argparse
import subprocess
from dotenv import load_dotenv
import concurrent.futures
import frontmatter
import hashlib
import json
import openai

load_dotenv()

INPUT_DIR = "original"
MAX_THREADS = 10
CACHE_DIR = "cache"

lang_map = {
    'ja': 'Japanese',
    'es': 'Spanish',
    'hi': 'Hindi',
    'zh': 'Simplified Chinese',
    'en': 'English',
    'fr': 'French',
    'de': 'German',
    'ar': 'Arabic',
    'hant': 'Traditional Chinese'
}

def get_blocks(md_content):
    blocks = []
    lines = md_content.splitlines(keepends=True)
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if stripped.startswith('```') or stripped.startswith('~~~'):
            fence = stripped[:3]
            code_lines = [line]
            i += 1
            while i < len(lines) and not lines[i].strip().startswith(fence):
                code_lines.append(lines[i])
                i += 1
            if i < len(lines):
                code_lines.append(lines[i])
                i += 1
            blocks.append(('code', ''.join(code_lines)))
        else:
            text_lines = []
            while i < len(lines) and lines[i].strip() != '' and not lines[i].strip().startswith('```') and not lines[i].strip().startswith('~~~'):
                text_lines.append(lines[i])
                i += 1
            if text_lines:
                blocks.append(('text', ''.join(text_lines)))
            while i < len(lines) and lines[i].strip() == '':
                blocks.append(('empty', lines[i]))
                i += 1
    return blocks

def translate_text(text, target_lang, model_provider, is_title=False):
    if model_provider == "deepseek":
        client = openai.OpenAI(base_url="https://api.deepseek.com", api_key=os.getenv("DEEPSEEK_API_KEY"))
        model_name = "deepseek-chat"
    elif model_provider == "mistral":
        client = openai.OpenAI(base_url="https://api.mistral.ai/v1", api_key=os.getenv("MISTRAL_API_KEY"))
        model_name = "mistral-large-latest"
    else:
        raise ValueError(f"Unknown model provider: {model_provider}")
    
    to_lang = lang_map.get(target_lang, target_lang)
    if is_title:
        prompt = f'Translate the following title to {to_lang}: "{text}"'
    else:
        prompt = f"Translate the following Markdown content to {to_lang}, keeping all formatting intact. Do not add, remove, or alter any Markdown syntax, code, or structure:\n\n{text}"
    
    response = client.chat.completions.create(
        model=model_name,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    return response.choices[0].message.content.strip() if is_title else response.choices[0].message.content

def translate_markdown_file(input_file, output_file, target_lang, model_provider):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    fm, md_content = frontmatter.parse(content)
    
    basename = os.path.basename(input_file)
    orig_lang = None
    for possible in ['en', 'zh', 'ja']:
        if basename.endswith(f"-{possible}.md"):
            orig_lang = possible
            break
    if not orig_lang:
        raise Exception(f"Unexpected filename format: {basename}")
    
    if target_lang == orig_lang:
        with open(output_file, 'w', encoding='utf-8') as out:
            out.write(content)
        return
    
    os.makedirs(CACHE_DIR, exist_ok=True)
    cache_filename = basename.replace(f"-{orig_lang}.md", ".json")
    cache_file = os.path.join(CACHE_DIR, cache_filename)
    
    cache = {}
    if os.path.exists(cache_file):
        with open(cache_file, 'r', encoding='utf-8') as cf:
            cache = json.load(cf)
    
    # Translate title
    original_title = fm.get('title', '')
    title_hash = hashlib.sha256(original_title.encode('utf-8')).hexdigest()
    if title_hash in cache and target_lang in cache[title_hash]:
        translated_title = cache[title_hash][target_lang]
    else:
        translated_title = translate_text(original_title, target_lang, model_provider, is_title=True)
        cache.setdefault(title_hash, {})[target_lang] = translated_title
    
    # Translate content blocks
    blocks = get_blocks(md_content)
    translated_blocks = []
    for block_type, block_content in blocks:
        if block_type in ('code', 'empty'):
            translated_blocks.append(block_content)
        elif block_type == 'text':
            block_hash = hashlib.sha256(block_content.encode('utf-8')).hexdigest()
            if block_hash in cache and target_lang in cache[block_hash]:
                translated = cache[block_hash][target_lang]
            else:
                translated = translate_text(block_content, target_lang, model_provider)
                cache.setdefault(block_hash, {})[target_lang] = translated
            translated_blocks.append(translated)
    
    translated_md = ''.join(translated_blocks)
    
    # Update frontmatter
    fm['title'] = translated_title
    
    output_content = frontmatter.dumps(fm) + '\n' + translated_md
    with open(output_file, 'w', encoding='utf-8') as out:
        out.write(output_content)
    
    # Save cache
    with open(cache_file, 'w', encoding='utf-8') as cf:
        json.dump(cache, cf, ensure_ascii=False, indent=4)

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
        print("Dry run mode enabled. No files will be modified.")
        print("Files that would be processed:")
        for filename, lang in changed_files:
            print(f"  - {filename} to language {lang}")        
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