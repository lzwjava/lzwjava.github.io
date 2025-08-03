from google import genai
from google.genai import types
from google.genai.types import GenerateImagesConfig
from PIL import Image
from io import BytesIO
import os

# Set your API key using the environment variable GEMINI_API_KEY
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

image = client.models.generate_images(
    model="imagen-4.0-generate-preview-06-06",
    prompt="A dog reading a newspaper",
    config=GenerateImagesConfig(
        image_size="2K",
        number_of_images=1,
        safety_filter_level="BLOCK_LOW_AND_ABOVE",
        person_generation="ALLOW_ADULT",
    ),
)

image.generated_images[0].image.save("output-image.png")
print(
    f"Created image using {len(image.generated_images[0].image.image_bytes)} bytes"
)

