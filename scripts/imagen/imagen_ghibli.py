import os
from google import genai
from google.genai import types
from PIL import Image as PILImage
from io import BytesIO

# 1. Init GenAI client (Vertex AI / ADC)
client = genai.Client(
    vertexai=True,
    project=os.getenv("GOOGLE_CLOUD_PROJECT"),
    location=os.getenv("GOOGLE_CLOUD_LOCATION")
)

# 2. Load your base avatar
base_image_path = "assets/images/avatar/avatar.jpg"
input_img = PILImage.open(base_image_path)

# 3. Define your edit prompt
prompt = (
    "Transform this image into the style of a Studio Ghibli film. "
    "Use a hand-painted watercolor aesthetic with a soft, vibrant palette. "
    "Lighting should be warm and golden, creating a nostalgic, whimsical atmosphere."
)

# 4. Call the Imagen edit model (mask-free)
response = client.models.generate_content(
    model="imagen-3-edit-preview",
    contents=[prompt, input_img],
    config=types.GenerateContentConfig(response_modalities=["IMAGE"])
)

# 5. Pull out the edited image and save
for part in response.candidates[0].content.parts:
    if part.inline_data:
        edited = PILImage.open(BytesIO(part.inline_data.data))
        edited.save("ghibli_style_output.png")
        print("✅ Saved Ghibli-style output to ghibli_style_output.png")
