from google import genai
from google.genai import types
from google.genai.types import GenerateImagesConfig
from PIL import Image
from io import BytesIO
import os

# Set up Vertex AI client
client = genai.Client(
    vertexai=True,
    project=os.getenv('GOOGLE_CLOUD_PROJECT'),
    location=os.getenv('GOOGLE_CLOUD_LOCATION')
)

image = client.models.generate_images(
    model="imagen-4.0-generate-preview-06-06",
    prompt="A dog reading a newspaper",
    config=GenerateImagesConfig(
        image_size="CUSTOM",
        custom_width=1200,
        custom_height=630,
        number_of_images=1,
        safety_filter_level="BLOCK_LOW_AND_ABOVE",
        person_generation="ALLOW_ADULT",
    ),
)

image.generated_images[0].image.save("test/output-image-og.png")
print(
    f"Created OG image using {len(image.generated_images[0].image.image_bytes)} bytes"
)
