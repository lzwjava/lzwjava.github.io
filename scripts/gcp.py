from google.cloud import texttospeech


def text_to_speech(text, output_filename):
    # Initialize the Text-to-Speech client
    client = texttospeech.TextToSpeechClient()

    # Set up the synthesis input
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Choose the voice parameters
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",  # You can change to another language if needed
        # You can change to MALE or FEMALE
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    # Set audio configuration
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3  # You can choose MP3 or LINEAR16
    )

    # Perform the text-to-speech request
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # Write the output audio to a file
    with open(output_filename, "wb") as out:
        out.write(response.audio_content)

    print(f"Audio content written to {output_filename}")


# Example usage
article_text = """
Your article content goes here. You can paste your entire article text in this string.
Make sure the text is appropriately formatted and does not exceed API limits.
"""
output_file = "output_audio.mp3"

# Call the function
text_to_speech(article_text, output_file)
