import os
import markdown
from google.cloud import texttospeech
from html import unescape
from bs4 import BeautifulSoup
import re
import random
from pydub import AudioSegment  # Install via: pip install pydub
import tempfile

def split_text(text, max_bytes=5000):
    """
    Splits text into chunks, each not exceeding max_bytes.
    
    Args:
        text (str): The input text to split.
        max_bytes (int): Maximum byte size per chunk.
        
    Returns:
        List[str]: A list of text chunks.
    """
    chunks = []
    current_chunk = ""
    for line in text.splitlines(True):  # Keep line breaks
        # Check if adding the new line exceeds the limit
        if len((current_chunk + line).encode('utf-8')) > max_bytes:
            if current_chunk:
                chunks.append(current_chunk)
                current_chunk = ""
            # If the single line is longer than max_bytes, split the line
            while len(line.encode('utf-8')) > max_bytes:
                # Find the split point
                split_point = max_bytes
                while split_point > 0 and not line[split_point - 1].isspace():
                    split_point -= 1
                if split_point == 0:
                    split_point = max_bytes  # Forced split
                chunks.append(line[:split_point].strip())
                line = line[split_point:]
            current_chunk += line
        else:
            current_chunk += line
    if current_chunk:
        chunks.append(current_chunk)
    return chunks

def text_to_speech(text, output_filename, language_code="en-US", voice_name=None, dry_run=False):
    """
    Converts text to speech and saves it as an MP3 file.
    
    Args:
        text (str): The input text to convert.
        output_filename (str): The path to save the output MP3 file.
        language_code (str): The language code for synthesis.
        voice_name (str, optional): Specific voice to use.
        dry_run (bool): If True, simulate the conversion without generating audio.
    """
    if dry_run:
        print(f"Dry run: Would generate audio for file: {output_filename}")
        return

    print(f"Generating audio for: {output_filename}")

    try:
        client = texttospeech.TextToSpeechClient()
        
        # Split the text into manageable chunks
        text_chunks = split_text(text)
        if not text_chunks:
            print("No text chunks to process.")
            return

        audio_segments = []

        for idx, chunk in enumerate(text_chunks):
            synthesis_input = texttospeech.SynthesisInput(text=chunk)
        
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
                speaking_rate=1.0,  # Adjust speaking rate as needed
                volume_gain_db=0.0   # Adjust volume gain as needed
            )
            response = client.synthesize_speech(
                input=synthesis_input, voice=voice, audio_config=audio_config
            )
            
            # Save the chunk audio to a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
                tmp_file.write(response.audio_content)
                temp_filename = tmp_file.name
            
            # Load the temporary audio file using pydub
            audio_segment = AudioSegment.from_mp3(temp_filename)
            audio_segments.append(audio_segment)
            
            # Remove the temporary file
            os.remove(temp_filename)
            
            print(f"Chunk {idx + 1}/{len(text_chunks)} processed.")
        
        # Concatenate all audio segments
        if audio_segments:
            combined = audio_segments[0]
            for segment in audio_segments[1:]:
                combined += segment
            
            # Export the combined audio
            combined.export(output_filename, format="mp3")
            print(f"Audio content written to {output_filename}")
        else:
            print("No audio segments to combine.")
    
    except Exception as e:
        print(f"An error occurred while generating audio for {output_filename}: {e}")

def md_to_text(md_file):
    """
    Converts a Markdown file to plain text.
    
    Args:
        md_file (str): The path to the Markdown file.
        
    Returns:
        str: The plain text extracted from the Markdown file.
    """
    print(f"Reading file: {md_file}")
    try:
        with open(md_file, 'r', encoding='utf-8') as file:
            md_content = file.read()

        # Remove YAML front matter
        md_content = re.sub(r'---\n.*?\n---', '', md_content, flags=re.DOTALL)

        html = markdown.markdown(md_content)
        text = unescape(BeautifulSoup(html, "html.parser").get_text())
        return text
    except Exception as e:
        print(f"Error reading or parsing {md_file}: {e}")
        return ""

def process_markdown_files(input_dir, output_dir, max_files=4, dry_run=False):
    """
    Processes Markdown files in the input directory and converts them to MP3 audio files.
    
    Args:
        input_dir (str): Directory containing Markdown files.
        output_dir (str): Directory to save MP3 files.
        max_files (int): Maximum number of files to process.
        dry_run (bool): If True, simulate the conversion without generating audio.
    """
    os.makedirs(output_dir, exist_ok=True)

    # Get list of Markdown files
    all_md_files = [f for f in os.listdir(input_dir) if f.endswith('.md')]
    total_files = len(all_md_files)

    if total_files == 0:
        print("No Markdown files found.")
        return

    print(f"Total Markdown files to process: {total_files}")

    files_processed = 0

    for filename in all_md_files:
        # Construct full path for input and output files
        md_file_path = os.path.join(input_dir, filename)
        output_filename = os.path.join(
            output_dir, f"{os.path.splitext(filename)[0]}.mp3")

        # Check if the output MP3 already exists
        if os.path.exists(output_filename):
            print(f"Skipping {filename}: {output_filename} already exists.")
            continue  # Skip to the next file

        # Process the file
        article_text = md_to_text(md_file_path)
        if not article_text.strip():
            print(f"Skipping {filename}: No content to convert.")
            continue  # Skip files with no content

        print(f"\nProcessing {files_processed + 1}/{total_files}: {filename}")

        if '-zh' in filename:
            # Select a Chinese voice
            text_to_speech(article_text, output_filename,
                           language_code="cmn-CN", dry_run=dry_run)
        else:
            # Select an English voice
            text_to_speech(article_text, output_filename, dry_run=dry_run)

        files_processed += 1

        print(f"File {files_processed}/{total_files} processed.\n")

        if files_processed >= max_files:
            print("Processed the maximum allowed files.")
            break

    print(f"Processing complete! {files_processed}/{total_files} files processed.")

if __name__ == "__main__":
    input_directory = "pages"
    output_directory = "assets/audios"
    dry_run = False  # Set to True for a dry run without generating audio files

    process_markdown_files(input_directory, output_directory, max_files=4, dry_run=dry_run)
