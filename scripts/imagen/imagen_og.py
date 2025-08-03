from google import genai
from google.genai.types import GenerateImagesConfig
import os

import sys
import argparse
from pathlib import Path
from imagen_prompt import imagen_prompt

def generate_image_with_imagen(prompt, output_path):
    """Generate image using Imagen model."""
    try:
        # Set up Vertex AI client
        client = genai.Client(
            vertexai=True,
            project=os.getenv('GOOGLE_CLOUD_PROJECT'),
            location=os.getenv('GOOGLE_CLOUD_LOCATION')
        )

        image = client.models.generate_images(
            model="imagen-4.0-generate-preview-06-06",
            prompt=prompt,
            config=GenerateImagesConfig(
                image_size="2K",
                number_of_images=1,
                safety_filter_level="BLOCK_LOW_AND_ABOVE",
                person_generation="ALLOW_ADULT",
            ),
        )

        image.generated_images[0].image.save(output_path)
        print(f"Created image at {output_path} using {len(image.generated_images[0].image.image_bytes)} bytes")
        return True

    except Exception as e:
        print(f"Error generating image: {e}", file=sys.stderr)
        return False


def process_file(file_path, debug=False):
    """Process a single Jekyll post file."""
    try:
        # Get image prompt using the imported function
        prompt = imagen_prompt(file_path, debug=debug)
        
        if prompt is None:
            return None

        # Create output filename
        file_stem = Path(file_path).stem
        output_path = f"test/{file_stem}.png"
        
        # Ensure test directory exists
        Path("test").mkdir(exist_ok=True)

        # Generate image
        success = generate_image_with_imagen(prompt, output_path)
        
        return prompt if success else None

    except Exception as e:
        print(f"Error processing {file_path}: {e}", file=sys.stderr)
        return None


def main():
    parser = argparse.ArgumentParser(
        description="Generate images for Jekyll posts using AI"
    )
    parser.add_argument("files", nargs="*", help="Markdown files to process")
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug output",
    )

    args = parser.parse_args()

    if not args.files:
        # If no files specified, look for markdown files in current directory
        md_files = list(Path(".").glob("*.md"))
        if not md_files:
            print("No markdown files found. Please specify files to process.")
            sys.exit(1)
        args.files = md_files

    for file_path in args.files:
        process_file(file_path, args.debug)


if __name__ == "__main__":
    main()
