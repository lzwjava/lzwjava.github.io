import os
from google import genai

# 1. Init your Vertex AI client
client = genai.Client(
    vertexai=True,
    project=os.getenv("GOOGLE_CLOUD_PROJECT"),
    location=os.getenv("GOOGLE_CLOUD_LOCATION"),
)

# 2. List all models your project can call
models = client.list_models()

# 3. Print out only those that support image editing
for m in models:
    if "generate_content" in m.supported_generation_methods and any(
        cap.startswith("IMAGE") for cap in m.supported_modalities
    ):
        print(f"{m.name}  ➔  modalities: {m.supported_modalities}")
