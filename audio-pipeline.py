import os
import markdown
from google.cloud import texttospeech
from html import unescape
from bs4 import BeautifulSoup
import re
import random


def text_to_speech(text, output_filename, language_code="en-US", voice_name=None, dry_run=False):
    if dry_run:
        print(f"Dry run: Would generate audio for file: {output_filename}")
        return

    print(f"Generating audio for: {output_filename}")

    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=text)

    if language_code == "en-US" and not voice_name:
        # Randomly select an English voice if not provided
        voice_name = random.choice(
            ["en-US-Journey-D", "en-US-Journey-F", "en-US-Journey-O"])
    elif language_code == "cmn-CN" and not voice_name:
        # Randomly select a Chinese voice if not provided
        voice_name = random.choice(
            ["cmn-CN-Wavenet-A", "cmn-CN-Wavenet-B", "cmn-CN-Wavenet-C", "cmn-CN-Wavenet-D"])

    voice = texttospeech.VoiceSelectionParams(
        language_code=language_code,
        name=voice_name
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        effects_profile_id=["small-bluetooth-speaker-class-device"],
        pitch=0.0,
        speaking_rate=0.0,
        volume_gain_db=5.0
    )
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    with open(output_filename, "wb") as out:
        out.write(response.audio_content)
    print(f"Audio content written to {output_filename}")


def md_to_text(md_file):
    print(f"Reading file: {md_file}")
    with open(md_file, 'r', encoding='utf-8') as file:
        md_content = file.read()

    md_content = re.sub(r'---\n.*?\n---', '', md_content, flags=re.DOTALL)

    html = markdown.markdown(md_content)
    text = unescape(BeautifulSoup(html, "html.parser").get_text())
    return text


def process_markdown_files(input_dir, output_dir, max_files=4, dry_run=False):
    os.makedirs(output_dir, exist_ok=True)

    files_processed = 0
    total_files = sum(1 for filename in os.listdir(
        input_dir) if filename.endswith('.md'))

    if total_files == 0:
        print("No Markdown files found.")
        return

    print(f"Total Markdown files to process: {total_files}")

    for filename in os.listdir(input_dir):
        if filename.endswith('.md'):
            files_processed += 1
            md_file_path = os.path.join(input_dir, filename)
            article_text = md_to_text(md_file_path)
            output_filename = os.path.join(
                output_dir, f"{os.path.splitext(filename)[0]}.mp3")

            print(f"\nProcessing {files_processed}/{total_files}: {filename}")

            if '-zh' in filename:
                # Randomly select a Chinese voice
                text_to_speech(article_text, output_filename,
                               language_code="cmn-CN", dry_run=dry_run)
            else:
                # Randomly select an English voice
                text_to_speech(article_text, output_filename, dry_run=dry_run)

            print(f"File {files_processed}/{total_files} processed.\n")

            if files_processed >= max_files:
                print("Processed the maximum allowed files.")
                break

    print(f"Processing complete! {files_processed}/{total_files} files processed.")


input_directory = "pages"
output_directory = "assets/audios"
dry_run = False

process_markdown_files(input_directory, output_directory, max_files=4, dry_run=dry_run)
