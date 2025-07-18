from gemini_client import call_gemini_api
from deepseek_client import call_deepseek_api
from mistral_client import call_mistral_api

def create_translation_prompt(target_language, type="content", front_matter_prompt=None):
    if type == "title":
        base_prompt = "Translate the following title to {target_language}. Provide only the translated title, without any additional notes or explanations. Do not repeat or mention the input text.\n"
    else:
        base_prompt = "Translate the following markdown text to {target_language}. Provide only the translated output, without any additional notes or explanations.\n"
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


def translate_text(text, target_language, type="content", model="deepseek", front_matter_prompt=None):
    if not text or not text.strip():
        return ""
    if target_language == 'en':
        print(f"  Skipping translation for English: {text[:50]}...")
        return text.strip()
    print(f"  Translating text: {text[:50]}...")
    
    if model == "deepseek":
        prompt = create_translation_prompt(target_language, type, front_matter_prompt) + "\n\n" + text
        translated_text = call_deepseek_api(prompt)
        return translated_text
    elif model == "mistral":
        prompt = create_translation_prompt(target_language, type, front_matter_prompt) + "\n\n" + text
        translated_text = call_mistral_api(prompt)
        return translated_text
    elif model == "gemini":
        prompt = create_translation_prompt(target_language, type, front_matter_prompt) + "\n\n" + text
        translated_text = call_gemini_api(prompt)
        return translated_text
    else:
        print(f"  Error: Invalid model specified: {model}")
        return None
    
if __name__ == "__main__":
    text = translate_text('Hi, it is sunny today.', 'zh', model='mistral')
    print(text)
    