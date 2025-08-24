import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from scripts.llm.openrouter_client import call_openrouter_api

import spacy
from langdetect import detect_langs

from scripts.translation.translate_utils import validate_translated_languages


def create_translation_prompt(
    target_language, type="content", front_matter_prompt=None
):
    if type == "title":
        base_prompt = "Translate the following title into {target_language}. Return only the translated title without any extra notes, explanations, or repetition of the input text. If the title is already in {target_language}, return it as is. If the target language is English, ensure the title is in Title Case.\n"
    else:
        base_prompt = "Translate the following markdown text into {target_language}. Return only the translated content without any additional notes or explanations. If the text is already in {target_language}, return it unchanged.\n"
        if front_matter_prompt:
            base_prompt += f"{front_matter_prompt}\n"
    if target_language == "ja":
        return base_prompt.format(target_language="Japanese")
    elif target_language == "es":
        return base_prompt.format(target_language="Spanish")
    elif target_language == "hi":
        return base_prompt.format(target_language="Hindi")
    elif target_language == "fr":
        return base_prompt.format(target_language="French")
    elif target_language == "zh":
        return base_prompt.format(target_language="Simplified Chinese")
    elif target_language == "hant":
        return base_prompt.format(target_language="Traditional Chinese (Hong Kong)")
    elif target_language == "en":
        return base_prompt.format(target_language="English")
    elif target_language == "de":
        return base_prompt.format(target_language="German")
    elif target_language == "ar":
        return base_prompt.format(target_language="Arabic")
    else:
        return base_prompt.format(target_language=target_language)


def translate_text(
    text,
    target_language,
    type="content",
    model="deepseek-v3",
    front_matter_prompt=None,
    original_lang=None,
):
    MIN_LENGTH = 1
    MAX_LENGTH = 5000
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text_len = len(text)
    if text_len < MIN_LENGTH or text_len > MAX_LENGTH:
        raise ValueError(f"text length {text_len} outside allowed range [{MIN_LENGTH}, {MAX_LENGTH}]")

    print(f"Debug: Starting translation process for text: {text[:50]}...")
    print(f"Debug: Target language: {target_language}")
    print(f"Debug: Model used: {model}")

    if target_language == original_lang:
        print(
            f"Debug: Target language matches original language, returning unchanged text"
        )
        return text

    prompt = (
        create_translation_prompt(target_language, type, front_matter_prompt)
        + "\n\n"
        + text
    )

    translated_text = call_openrouter_api(prompt, model)

    if not isinstance(translated_text, str):
        raise RuntimeError("Model returned non-text response")

    low_translated = translated_text.lower()
    low_text = text.lower().strip()

    if low_text and low_text in low_translated:
        raise RuntimeError("Model returned the original text or echoed input; aborting translation")

    commentary_indicators = [
        "the output is",
        "output is",
        "translated title",
        "the translation is",
        "translation is",
        "translated:",
        "result:",
        "output:",
        "return only",
        "return only the translated",
    ]
    for indicator in commentary_indicators:
        if indicator in low_translated:
            raise RuntimeError("Model included commentary or extra notes; aborting translation")

    if type == "title":
        if "\n" in translated_text.strip():
            raise RuntimeError("Model returned multi-line title; expected single-line title")

    validate_translated_languages(translated_text, target_language)

    return translated_text


if __name__ == "__main__":
    print("Debug: Running main test translation")
    text = translate_text(
        "Hi, it is sunny today. Hahaa...", "zh", model="mistral-medium", original_lang="en"
    )
    print(f"Debug: Final translated text: {text}")
