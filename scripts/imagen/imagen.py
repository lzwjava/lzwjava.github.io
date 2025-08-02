from google import genai
from google.genai.types import GenerateImagesConfig

client = genai.Client()
image = client.models.generate_images(
    model="imagen-4.0-generate-preview-06-06",
    prompt="A dog reading a newspaper",
    config=GenerateImagesConfig(image_size="2K"),
)

image.generated_images[0].image.save("output-image.png")
print(
    f"Created output image using {len(image.generated_images[0].image.image_bytes)} bytes"
)
