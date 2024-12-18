import os
import markdown
from google.cloud import texttospeech
from html import unescape
from bs4 import BeautifulSoup
import re
import random
from pydub import AudioSegment
import tempfile
import json
import time

PROGRESS_FILE = 'progress.json'

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_progress(progress):
    with open(PROGRESS_FILE, 'w') as f:
        json.dump(progress, f, indent=4)

def split_text(text, max_bytes=4000):
    chunks = []
    current_chunk = ""
    for line in text.split('\n'):
        if current_chunk:
            tentative_chunk = current_chunk + '\n' + line
        else:
            tentative_chunk = line
        if len(tentative_chunk.encode('utf-8')) > max_bytes:
            if current_chunk:
                chunks.append(current_chunk)
            if len(line.encode('utf-8')) > max_bytes:
                chunks.append(line)
                current_chunk = ""
            else:
                current_chunk = line
        else:
            current_chunk = tentative_chunk
    if current_chunk:
        chunks.append(current_chunk)
    return chunks

def text_to_speech(text, output_filename, language_code="en-US", voice_name=None, dry_run=False, start_chunk=0, progress=None):
    if dry_run:
        print(f"Dry run: Would generate audio for file: {output_filename}")
        return
    print(f"Generating audio for: {output_filename}")
    try:
        client = texttospeech.TextToSpeechClient()
        text_chunks = split_text(text)
        if not text_chunks:
            print("No text chunks to process.")
            return

        audio_segments = []
        # If resuming, load already processed chunks
        if progress and output_filename in progress:
            processed_chunks = progress[output_filename].get('processed_chunks', [])
            audio_segments = [AudioSegment.from_mp3(chunk_path) for chunk_path in progress[output_filename].get('temp_files', [])]
            start_chunk = len(processed_chunks)
            print(f"Resuming from chunk {start_chunk + 1}/{len(text_chunks)}")
        else:
            processed_chunks = []
            progress[output_filename] = {'processed_chunks': [], 'temp_files': []}

        for idx in range(start_chunk, len(text_chunks)):
            chunk = text_chunks[idx]
            synthesis_input = texttospeech.SynthesisInput(text=chunk)
            if language_code == "en-US" and not voice_name:
                voice_name = random.choice(["en-US-Journey-D", "en-US-Journey-F", "en-US-Journey-O"])
            elif language_code == "cmn-CN" and not voice_name:
                voice_name = random.choice(["cmn-CN-Wavenet-A", "cmn-CN-Wavenet-B", "cmn-CN-Wavenet-C", "cmn-CN-Wavenet-D"])
            voice = texttospeech.VoiceSelectionParams(language_code=language_code, name=voice_name)
            audio_config = texttospeech.AudioConfig(
                audio_encoding=texttospeech.AudioEncoding.MP3,
                effects_profile_id=["small-bluetooth-speaker-class-device"]    
            )
            
            # Retry logic
            retries = 3
            for attempt in range(1, retries + 1):
                try:
                    response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)
                    break  # Success, exit retry loop
                except Exception as e:
                    print(f"Error on chunk {idx + 1}: {e}")
                    if attempt < retries:
                        wait_time = 2 ** attempt  # Exponential backoff
                        print(f"Retrying chunk {idx + 1} in {wait_time} seconds (Attempt {attempt + 1}/{retries})...")
                        time.sleep(wait_time)
                    else:
                        raise e  # Exceeded retries

            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
                tmp_file.write(response.audio_content)
                temp_filename = tmp_file.name
            audio_segment = AudioSegment.from_mp3(temp_filename)
            audio_segments.append(audio_segment)
            os.remove(temp_filename)
            print(f"Chunk {idx + 1}/{len(text_chunks)} processed.")
            
            # Update progress
            progress[output_filename]['processed_chunks'].append(idx)
            progress[output_filename]['temp_files'].append(temp_filename)
            save_progress(progress)

        if audio_segments:
            combined = audio_segments[0]
            for segment in audio_segments[1:]:
                combined += segment
            combined.export(output_filename, format="mp3")
            print(f"Audio content written to {output_filename}")
            # Cleanup temp files
            for temp_file in progress[output_filename]['temp_files']:
                if os.path.exists(temp_file):
                    os.remove(temp_file)
            # Remove progress entry for completed file
            del progress[output_filename]
            save_progress(progress)
        else:
            print("No audio segments to combine.")
    except Exception as e:
        print(f"An error occurred while generating audio for {output_filename}: {e}")
        save_progress(progress)  # Ensure progress is saved even on error

def md_to_text(md_file):
    print(f"Reading file: {md_file}")
    try:
        with open(md_file, 'r', encoding='utf-8') as file:
            md_content = file.read()
        md_content = re.sub(r'---\n.*?\n---', '', md_content, flags=re.DOTALL)
        html = markdown.markdown(md_content)
        text = unescape(BeautifulSoup(html, "html.parser").get_text())
        return text
    except Exception as e:
        print(f"Error reading or parsing {md_file}: {e}")
        return ""

def process_markdown_files(input_dir, output_dir, max_files=100, dry_run=False):
    os.makedirs(output_dir, exist_ok=True)
    all_md_files = [f for f in os.listdir(input_dir) if f.endswith('.md')]
    total_files = len(all_md_files)
    if total_files == 0:
        print("No Markdown files found.")
        return

    print(f"Total Markdown files to process: {total_files}")
    files_processed = 0

    # Load existing progress
    progress = load_progress()

    for filename in all_md_files:
        md_file_path = os.path.join(input_dir, filename)
        output_filename = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.mp3")
        if os.path.exists(output_filename):
            print(f"Skipping {filename}: {output_filename} already exists.")
            continue
        article_text = md_to_text(md_file_path)
        if not article_text.strip():
            print(f"Skipping {filename}: No content to convert.")
            continue
        print(f"\nProcessing {files_processed + 1}/{total_files}: {filename}")
        try:
            if '-zh' in filename:
                text_to_speech(
                    article_text, 
                    output_filename, 
                    language_code="cmn-CN", 
                    dry_run=dry_run,
                    progress=progress
                )
            else:
                text_to_speech(
                    article_text, 
                    output_filename, 
                    dry_run=dry_run,
                    progress=progress
                )
            files_processed += 1
            print(f"File {files_processed}/{total_files} processed.\n")
            if files_processed >= max_files:
                print("Processed the maximum allowed files.")
                break
        except Exception as e:
            print(f"Failed to process {filename}: {e}")
            # Optionally, continue to next file or break
            continue

    print(f"Processing complete! {files_processed}/{total_files} files processed.")

if __name__ == "__main__":
    input_directory = "pages"
    output_directory = "assets/audios"
    dry_run = False
    process_markdown_files(input_directory, output_directory, max_files=4, dry_run=dry_run)
