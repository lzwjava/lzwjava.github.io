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
