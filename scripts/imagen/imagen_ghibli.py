import vertexai
from vertexai.generative_models import Image, GenerativeModel
import os

# Initialize Vertex AI
import google.generativeai as genai

client = genai.Client(
    vertexai=True,
    project=os.getenv('GOOGLE_CLOUD_PROJECT'),
    location=os.getenv('GOOGLE_CLOUD_LOCATION')
)

# Load the base image
base_image_path = "assets/images/avatar/avatar.jpg"
base_image = Image.load_from_file(base_image_path)

# Define the editing prompt
prompt = """
Transform this image into the style of a Studio Ghibli film. 
Use a hand-painted watercolor aesthetic with a soft, vibrant color palette. 
The lighting should be warm and golden, creating a nostalgic and whimsical atmosphere.
"""

# Get the Imagen model for image editing
model = GenerativeModel(model_name="imagen-4-edit") # This model name is an example; check docs for the latest one

# Generate the new image
edited_images = model.generate_images(
    base_image=base_image,
    prompt=prompt,
    number_of_images=1
)

# Save the output
edited_images[0].save("ghibli_style_output.png")
print("Ghibli-style image saved as ghibli_style_output.png")