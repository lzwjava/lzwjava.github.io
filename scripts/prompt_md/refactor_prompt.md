```python
Refactor the Python code below, focusing on:
- Improving readability
- Enhancing maintainability
- Following Python best practices

I have the following code in a file called `scripts/prompt/refactor_prompt.py`:

```python
import argparse
import os
from sample_code import sample_code  # Importing the sample code function

def generate_refactor_prompt(file_path):
    """Generate a refactor prompt for the given Python file."""
    
    sample = sample_code()
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        prompt = f"""```python
Refactor the Python code below, focusing on:
- Improving readability
- Enhancing maintainability
- Following Python best practices

I have the following code in a file called `{file_path}`:

```python
{content}
```

Sample code (for reference):

```python
{sample}
```
"""
        return prompt
    except FileNotFoundError:
        return f"Error: The file {file_path} was not found."
    except Exception as e:
        return f"Error reading file {file_path}: {str(e)}"

def save_prompt_to_md(prompt, original_path):
    """Save the generated prompt to a markdown file in scripts/prompt_md/ directory."""
    try:
        # Get the base filename without extension
        base_name = os.path.basename(original_path)
        file_name = os.path.splitext(base_name)[0] + ".md"
        
        # Define the output directory
        output_dir = "scripts/prompt_md"
        os.makedirs(output_dir, exist_ok=True)
        
        # Define the full output path
        output_path = os.path.join(output_dir, file_name)
        
        # Save the prompt to the markdown file
        with open(output_path, 'w', encoding='utf-8') as md_file:
            md_file.write(prompt)
        return f"Prompt saved to {output_path}"
    except Exception as e:
        return f"Error saving prompt to markdown file: {str(e)}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a refactor prompt for a Python file and save it as markdown.")
    parser.add_argument("file_path", help="Path to the Python file to refactor")
    args = parser.parse_args()
    
    prompt = generate_refactor_prompt(args.file_path)
    print(prompt)
    print(save_prompt_to_md(prompt, args.file_path))

```

Sample code (for reference):

```python
from gemini_client import call_gemini_api
from deepseek_client import call_deepseek_api
from mistral_client import call_mistral_api

def create_translation_prompt(target_language, type="content", front_matter_prompt=None):
    if type == "title":
        base_prompt = "Translate the following title into {target_language}. Return only the translated title without any extra notes, explanations, or repetition of the input text. If the title is already in {target_language}, return it as is. If the target language is English, ensure the title is in Title Case.\n"
    else:
        base_prompt = "Translate the following markdown text into {target_language}. Return only the translated content without any additional notes or explanations. If the text is already in {target_language}, return it unchanged.\n"
        if front_matter_prompt:
            base_prompt += f"{front_matter_prompt}\n"
    if target_language == 'ja':
        return base_prompt.format(target_language="Japanese")
    elif target_language == 'es':
        return base_prompt.format(target_language="Spanish")
    elif target_language == 'hi':
        return base_prompt.format(target_language="Hindi")
    elif target_language == 'fr':
        return base_prompt.format(target_language="French")
    elif target_language == 'zh':
        return base_prompt.format(target_language="Simplified Chinese")
    elif target_language == 'hant':
        return base_prompt.format(target_language="Traditional Chinese (Hong Kong)")
    elif target_language == 'en':
        return base_prompt.format(target_language="English")
    elif target_language == 'de':
        return base_prompt.format(target_language="German")
    elif target_language == 'ar':
        return base_prompt.format(target_language="Arabic")
    else:
        return base_prompt.format(target_language=target_language)


def translate_text(text, target_language, type="content", model="deepseek", front_matter_prompt=None, original_lang=None):
    print(f"Debug: Starting translation process for text: {text[:50]}...")
    print(f"Debug: Target language: {target_language}")
    print(f"Debug: Model used: {model}")
    
    if target_language == original_lang:
        print(f"Debug: Target language matches original language, returning unchanged text")
        return text
    
    prompt = create_translation_prompt(target_language, type, front_matter_prompt) + "\n\n" + text
    
    if model == "deepseek":
        translated_text = call_deepseek_api(prompt)
        return translated_text
    elif model == "mistral":
        translated_text = call_mistral_api(prompt)
        return translated_text
    elif model == "gemini":
        translated_text = call_gemini_api(prompt)
        return translated_text
    else:
        print(f"Error: Invalid model specified: {model}")
        return None
    
if __name__ == "__main__":
    print("Debug: Running main test translation")
    text = translate_text('Hi, it is sunny today. Hahaa...', 'ja', model='mistral', original_lang='en')
    print(f"Debug: Final translated text: {text}")

```
