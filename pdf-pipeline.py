import os
import json
import argparse
from datetime import datetime
import subprocess  # For calling pandoc

# Define progress files for both tasks
PROGRESS_FILES = {
    'pages': 'progress_pages.json',
    'posts': 'progress_posts.json'
}

# Fixed output directory
OUTPUT_DIRECTORY = "assets/pdfs"

def load_progress(task):
    """
    Load the progress from a JSON file for the given task.
    """
    progress_file = PROGRESS_FILES.get(task)
    if progress_file and os.path.exists(progress_file):
        with open(progress_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_progress(task, progress):
    """
    Save the progress to a JSON file for the given task.
    """
    progress_file = PROGRESS_FILES.get(task)
    if progress_file:
        with open(progress_file, 'w', encoding='utf-8') as f:
            json.dump(progress, f, indent=4, ensure_ascii=False)

def text_to_pdf(input_markdown_path, output_pdf_path, dry_run=False):
    """
    Convert Markdown file to PDF using pandoc.
    """
    if dry_run:
        print(f"Dry run: Would generate PDF for file: {output_pdf_path}")
        return
    print(f"Generating PDF for: {output_pdf_path}")
    try:
        # Construct the pandoc command
        command = [
            'pandoc',
            input_markdown_path,
            '-o',
            output_pdf_path,
            '--from', 'markdown',
            '--pdf-engine', 'xelatex'  # You can choose other PDF engines like 'pdflatex' or 'wkhtmltopdf'
        ]

        # Execute the pandoc command
        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode != 0:
            print(f"Pandoc error for {output_pdf_path}: {result.stderr}")
            raise Exception(f"Pandoc failed for {input_markdown_path}")

        print(f"PDF content written to {output_pdf_path}")
    except FileNotFoundError:
        print("Pandoc is not installed or not found in PATH. Please install pandoc to proceed.")
        raise
    except Exception as e:
        print(f"An error occurred while generating PDF for {output_pdf_path}: {e}")
        raise e  # Re-raise exception to handle it in the caller

def get_last_n_files(input_dir, n=10):
    """
    Retrieve the last n modified Markdown files from the input directory.
    """
    try:
        # Get all markdown files with their modification time
        md_files = [
            (f, os.path.getmtime(os.path.join(input_dir, f)))
            for f in os.listdir(input_dir) if f.endswith('.md')
        ]
        # Sort by modification time descending
        md_files_sorted = sorted(md_files, key=lambda x: x[1], reverse=True)
        # Get the last n files
        last_n_files = [f[0] for f in md_files_sorted[:n]]
        return last_n_files
    except Exception as e:
        print(f"Error retrieving files from {input_dir}: {e}")
        return []

def process_markdown_files(task, input_dir, output_dir, n=10, max_files=100, dry_run=False):
    """
    Process Markdown files to generate PDFs.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    if task == 'pages':
        # Process all Markdown files in 'pages'
        all_md_files = [f for f in os.listdir(input_dir) if f.endswith('.md')]
        md_files_to_process = all_md_files
        total_files = len(md_files_to_process)
        print(f"Total Markdown files to process in 'pages': {total_files}")
    elif task == 'posts':
        # Process the last n Markdown files in '_posts'
        md_files_to_process = get_last_n_files(input_dir, n)
        total_files = len(md_files_to_process)
        print(f"Total Markdown files to process in '_posts' (last {n}): {total_files}")
    else:
        print("Invalid task specified.")
        return

    if total_files == 0:
        print(f"No Markdown files found in '{input_dir}' directory.")
        return

    files_processed = 0

    # Load existing progress
    progress = load_progress(task)

    for idx, filename in enumerate(md_files_to_process, start=1):
        md_file_path = os.path.join(input_dir, filename)
        pdf_filename = f"{os.path.splitext(filename)[0]}.pdf"
        output_filename = os.path.join(output_dir, pdf_filename)
        
        if os.path.exists(output_filename):
            print(f"Skipping {filename}: {output_filename} already exists.")
            continue
        if filename in progress:
            print(f"Skipping {filename}: Already processed.")
            continue

        print(f"\nProcessing {files_processed + 1}/{total_files}: {filename}")
        try:
            if not os.path.isfile(md_file_path):
                print(f"Skipping {filename}: File does not exist.")
                continue

            with open(md_file_path, 'r', encoding='utf-8') as file:
                markdown_content = file.read()

            if not markdown_content.strip():
                print(f"Skipping {filename}: No content to convert.")
                continue

            text_to_pdf(
                input_markdown_path=md_file_path, 
                output_pdf_path=output_filename, 
                dry_run=dry_run
            )
            files_processed += 1
            print(f"File {files_processed}/{total_files} processed.\n")

            # Update progress
            progress[filename] = {
                'output': output_filename,
                'timestamp': datetime.now().isoformat()
            }
            save_progress(task, progress)

            if files_processed >= max_files:
                print("Processed the maximum allowed files.")
                break
        except Exception as e:
            print(f"Failed to process {filename}: {e}")
            continue

    print(f"Processing complete! {files_processed}/{total_files} files processed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process Markdown files to generate PDFs using pandoc.")
    parser.add_argument('--task', choices=['pages', 'posts'], required=True, help="Task to perform: 'pages' or 'posts'")
    parser.add_argument('--n', type=int, default=10, help="Number of last files to process (only for 'posts').")
    parser.add_argument('--max_files', type=int, default=100, help="Maximum number of files to process.")
    parser.add_argument('--dry_run', action='store_true', help="Perform a dry run without generating PDFs.")
    
    args = parser.parse_args()

    # Determine input_dir based on task
    if args.task == 'pages':
        input_directory = "pages"
        max_files = args.max_files
        n = None  # Not used for 'pages'
    elif args.task == 'posts':
        input_directory = "_posts"
        n = args.n
        max_files = args.max_files  # Can be set as needed
    else:
        print("Invalid task specified. Choose either 'pages' or 'posts'.")
        exit(1)

    # Execute the processing
    if args.task in ['pages', 'posts']:
        process_markdown_files(
            task=args.task,
            input_dir=input_directory,
            output_dir=OUTPUT_DIRECTORY,
            n=args.n if args.task == 'posts' else 0,
            max_files=args.max_files,
            dry_run=args.dry_run
        )
