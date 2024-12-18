import os
import markdown
from google.cloud import texttospeech
from html import unescape
from bs4 import BeautifulSoup


def text_to_speech(text, output_filename, dry_run=False):
    if dry_run:
        print(f"Dry run: Would generate audio for file: {output_filename}")
        return

    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Journey-F"
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
    with open(md_file, 'r', encoding='utf-8') as file:
        md_content = file.read()
    html = markdown.markdown(md_content)
    text = unescape(BeautifulSoup(html, "html.parser").get_text())
    return text


def process_markdown_files(input_dir, output_dir, dry_run=False):
    os.makedirs(output_dir, exist_ok=True)
    for filename in os.listdir(input_dir):
        if filename.endswith('.md'):
            md_file_path = os.path.join(input_dir, filename)
            article_text = md_to_text(md_file_path)
            output_filename = os.path.join(
                output_dir, f"{os.path.splitext(filename)[0]}.mp3")
            text_to_speech(article_text, output_filename, dry_run)


input_directory = "pages"
output_directory = "assets/audios"
dry_run = True

process_markdown_files(input_directory, output_directory, dry_run)
