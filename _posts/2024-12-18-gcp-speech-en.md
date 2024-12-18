---
layout: post  
title: "Getting Started with Google Text-to-Speech API"  
---

I plan to convert some of Yin Wang's articles into audio. To do this, I'm experimenting with the Google Text-to-Speech API. Below are some tutorials provided by ChatGPT to guide the process. Once everything is ready, I will upload the audio here.

---

### Step 1: Set Up Google Cloud Account

1. **Create a Google Cloud Account**  
   If you don’t already have a Google Cloud account, head over to the [Google Cloud Console](https://console.cloud.google.com/) and sign up.

2. **Create a New Project**  
   - In the Google Cloud Console, click on the project dropdown menu (top left).
   - Select **New Project**, name it, and create the project.

3. **Enable the Text-to-Speech API**  
   - Go to the [Google Cloud Text-to-Speech API page](https://cloud.google.com/text-to-speech).
   - Click **Enable** to activate the API for your project.

4. **Create API Credentials**  
   - Navigate to **APIs & Services > Credentials** in the Cloud Console.
   - Click **Create Credentials**, and choose **Service Account**.
   - Follow the prompts to create the service account and ensure to **download the private key file** in JSON format.
   - Save this JSON file securely, as you’ll need it for authenticating your API requests.

---

### Step 2: Install Google Cloud SDK and Client Library

1. **Install Google Cloud SDK**  
   If you haven’t already installed the [Google Cloud SDK](https://cloud.google.com/sdk/docs/install), follow the installation instructions for your operating system.

2. **Install Python Client Library**  
   If you're using Python, install the `google-cloud-texttospeech` library by running the following command in your terminal:

   ```bash
   pip install google-cloud-texttospeech
   ```

---

### Step 3: Set Up Authentication

Before interacting with the Google Cloud Text-to-Speech API, set up authentication by specifying the location of your credentials file. Run this command in your terminal:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/Users/lzwjava/Downloads/google_credentials_service_account.json"
```

Replace the path with the actual location of your service account JSON key file.

---

### Step 4: Implement Text-to-Speech Conversion

Now you can use the Google Cloud Text-to-Speech API to convert text into speech. Below is a Python example demonstrating how to do this:

```python
from google.cloud import texttospeech

def text_to_speech(text, output_filename):
    # Initialize the Text-to-Speech client
    client = texttospeech.TextToSpeechClient()

    # Set up the synthesis input
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Choose the voice parameters
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",  # You can change to another language if needed
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL  # Male or Female options
    )

    # Set audio configuration
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3  # MP3 or LINEAR16 for WAV
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
Your article content goes here. Paste your article text in this string. 
Ensure it's properly formatted and does not exceed API limits.
"""
output_file = "output_audio.mp3"

# Call the function
text_to_speech(article_text, output_file)
```

---

### Step 5: Run the Script

1. Save the script as `text_to_speech.py`.
2. Run the script:

   ```bash
   python text_to_speech.py
   ```

This will create an audio file (`output_audio.mp3`) from the provided text.

---

### Step 6: Service Account Key

Your service account key should look like the example below:

```json
{
  "type": "service_account",
  "project_id": "your-project-id",
  "private_key_id": "your-private-key-id",
  "private_key": "your-private-key",
  "client_email": "your-service-account-email@your-project-id.iam.gserviceaccount.com",
  "client_id": "your-client-id",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "your-client-cert-url"
}
```

---

### Step 7: Generate a New Service Account Key (if necessary)

If your credentials file doesn't look like the example above, you may need to create a new service account key in the Google Cloud Console.

**Steps to create a new service account key:**
1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Navigate to **IAM & Admin**:
   - On the left sidebar, click **IAM & Admin** > **Service Accounts**.
3. **Create a new service account** (if you don't already have one):
   - Click **Create Service Account** at the top.
   - Enter a name for your service account and grant it the necessary roles (e.g., Viewer or Text-to-Speech API User).
   - Click **Create**.
4. **Generate a key**:
   - After creating the service account, click on it.
   - Go to the **Keys** tab and click **Add Key** > **Create new key**.
   - Select **JSON** as the key type, then download the key file.

---

### Example Audio Output

Once everything is set up, the output audio will be available here:  
[Download the audio file](./assets/audios/gcp-speech/output_audio.mp3).

---

### Conclusion

With the Google Cloud Text-to-Speech API, converting written text into natural-sounding speech is straightforward and efficient. Whether you're building an application that requires voice output or just experimenting with text-to-speech, this API provides powerful capabilities. Be sure to explore the documentation for more options, such as voice selection and language support!

