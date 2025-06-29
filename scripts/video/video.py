import os
from openai import OpenAI
from google.cloud import texttospeech
from moviepy.editor import TextClip, CompositeVideoClip, ColorClip, concatenate_videoclips
import requests
import random

DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY")  # Read from environment variable

# Initialize DeepSeek client
deepseek_client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")

# Function to refine script with DeepSeek
def refine_script_with_deepseek(script):
    prompt = f"""
    You are an expert scriptwriter for educational videos. Refine the following script to be concise, clear, and engaging for a 1-minute educational video. Ensure it is suitable for spoken narration and fits within 60 seconds when spoken at a natural pace. Split the script into 2-3 short paragraphs for caption display. Return the refined script as a list of paragraphs.

    Original script:
    {script}

    Output format:
    ["paragraph 1", "paragraph 2", "paragraph 3"]
    """
    response = deepseek_client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}],
        stream=False
    )
    refined_script = eval(response.choices[0].message.content)  # Convert string to list
    return refined_script

# Function to generate audio for each paragraph using Google Cloud Text-to-Speech
def generate_audio(paragraphs, output_dir="audio"):
    client = texttospeech.TextToSpeechClient()
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    audio_files = []
    for i, paragraph in enumerate(paragraphs):
        synthesis_input = texttospeech.SynthesisInput(text=paragraph)
        voice_name = random.choice(["en-US-Journey-D", "en-US-Journey-F", "en-US-Journey-O"])
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            name=voice_name
        )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )
        response = client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )
        audio_file = os.path.join(output_dir, f"paragraph_{i+1}.mp3")
        with open(audio_file, "wb") as out:
            out.write(response.audio_content)
        audio_files.append(audio_file)
    return audio_files

# Function to create video with captions and black background
def create_video(paragraphs, audio_files, output_file="educational_video.mp4"):
    clips = []
    for i, (paragraph, audio_file) in enumerate(zip(paragraphs, audio_files)):
        # Create text clip for captions
        text_clip = TextClip(
            paragraph,
            fontsize=40,
            color="white",
            font="Arial",
            size=(1280, 720),  # Standard HD resolution
            method="caption",
            align="center"
        )
        # Load audio and get its duration
        audio_clip = AudioFileClip(audio_file)
        duration = audio_clip.duration
        # Set text clip duration to match audio
        text_clip = text_clip.set_duration(duration)
        # Create black background clip
        bg_clip = ColorClip(size=(1280, 720), color=(0, 0, 0), duration=duration)
        # Combine text and background
        video_clip = CompositeVideoClip([bg_clip, text_clip.set_position("center")])
        # Add audio to video clip
        video_clip = video_clip.set_audio(audio_clip)
        clips.append(video_clip)
    
    # Concatinate all clips
    final_clip = concatenate_videoclips(clips)
    # Write final video
    final_clip.write_videofile(output_file, fps=24, codec="libx264", audio_codec="aac")
    final_clip.close()
    for clip in clips:
        clip.close()

# Main function
def main():
    # Example input script (replace with your educational content)
    input_script = """
    Machine learning is a field of artificial intelligence that allows computers to learn from data without being explicitly programmed. It involves algorithms that identify patterns and make predictions. Applications include image recognition, natural language processing, and more. This technology is transforming industries like healthcare and finance.
    """
    
    # Step 1: Refine script with DeepSeek
    refined_paragraphs = refine_script_with_deepseek(input_script)
    print("Refined Script:", refined_paragraphs)
    
    # Step 2: Generate audio for each paragraph
    audio_files = generate_audio(refined_paragraphs, "test")
    print("Audio files generated:", audio_files)
    
    # Step 3: Create video with captions and black background
    create_video(refined_paragraphs, audio_files)
    print("Video created: educational_video.mp4")

if __name__ == "__main__":
    main()