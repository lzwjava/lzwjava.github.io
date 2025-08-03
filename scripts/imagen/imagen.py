from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import os

# Set your API key using the environment variable GEMINI_API_KEY
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_images(
    model="imagen-4.0-generate-preview-06-06",
    prompt="A dog reading a newspaper",
    config=types.GenerateImagesConfig(
        number_of_images=1,
        # image_size="2K",  # optional for 2K resolution; requires newer fast-preview library
        aspect_ratio="1:1",
        safety_filter_level="BLOCK_MEDIUM_AND_ABOVE",
        person_generation="ALLOW_ADULT",
    )
)

for i, generated in enumerate(response.generated_images):
    raw = generated.image.image_bytes
    pil = Image.open(BytesIO(raw))  # Convert raw bytes into a PIL image
    pil.save(f"output-image-{i+1}.png")
    print(f"Saved image {i+1}, {len(raw):,} bytes")
