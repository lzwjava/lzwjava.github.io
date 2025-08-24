from langdetect import detect_langs, DetectorFactory
# make langdetect deterministic
DetectorFactory.seed = 0


def _map_target_code(code):
    mapping = {
        "hant": "zh",
        "zh": "zh",
        "ja": "ja",
        "en": "en",
        "es": "es",
        "hi": "hi",
        "fr": "fr",
        "de": "de",
        "ar": "ar",
    }
    return mapping.get(code, code)


def _simple_language_detect(text):
    """Simple language detection using common words."""
    # Common words for each language (top 20-30 most frequent)
    common_words = {
        'en': set(['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'i', 'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at', 'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she']),
        'zh': set(['的', '了', '在', '是', '我', '有', '和', '就', '不', '人', '都', '一', '个', '上', '也', '很', '到', '说', '要', '去', '你', '会', '着', '没有', '看', '好', '自己', '这', '那', '里']),
        'ja': set(['の', 'に', 'は', 'を', 'た', 'が', 'で', 'て', 'と', 'し', 'れ', 'さ', 'ある', 'いる', 'も', 'する', 'から', 'な', 'こと', 'として', 'い', 'や', 'あるい', '中', 'なる', '一', 'それ', 'いう', 'ため', '的']),
        'es': set(['de', 'la', 'que', 'el', 'en', 'y', 'a', 'los', 'del', 'se', 'las', 'por', 'un', 'para', 'con', 'no', 'una', 'su', 'al', 'lo', 'como', 'más', 'pero', 'sus', 'le', 'ya', 'o', 'este', 'sí', 'porque']),
        'fr': set(['de', 'le', 'et', 'à', 'un', 'il', 'être', 'et', 'en', 'avoir', 'que', 'pour', 'dans', 'ce', 'son', 'une', 'sur', 'avec', 'ne', 'se', 'pas', 'tout', 'plus', 'faire', 'leur', 'on', 'mais', 'ou', 'comme', 'si']),
        'de': set(['der', 'die', 'und', 'in', 'den', 'von', 'zu', 'das', 'mit', 'sich', 'des', 'auf', 'für', 'ist', 'im', 'dem', 'nicht', 'ein', 'eine', 'als', 'auch', 'es', 'an', 'werden', 'aus', 'er', 'hat', 'dass', 'sie', 'nach']),
        'hi': set(['है', 'और', 'में', 'की', 'का', 'हैं', 'से', 'को', 'पर', 'यह', 'हो', 'था', 'कि', 'जो', 'कर', 'मुझे', 'तो', 'लिए', 'नहीं', 'एक', 'करने', 'किया', 'था', 'बहुत', 'होता', 'आप', 'उसे', 'दिया', 'जब', 'कहा']),
        'ar': set(['في', 'من', 'إلى', 'على', 'هذا', 'هذه', 'التي', 'التي', 'كان', 'لقد', 'لم', 'قد', 'كل', 'إن', 'عن', 'أن', 'مع', 'هو', 'هي', 'إذا', 'فقد', 'أي', 'كان', 'بعد', 'قبل', 'بين', 'بعض', 'مع', 'أو', 'أي'])
    }
    
    # Convert text to lowercase and extract words
    import re
    words = re.findall(r'\b\w+\b', text.lower())
    if not words:
        return []
    
    # Count matches for each language
    lang_scores = {}
    for lang, word_set in common_words.items():
        matches = sum(1 for word in words if word in word_set)
        if matches > 0:
            lang_scores[lang] = matches / len(words)
    
    # Return sorted results
    results = [(lang, score) for lang, score in sorted(lang_scores.items(), key=lambda x: x[1], reverse=True)]
    
    # If no matches found, return empty list to let langdetect handle it
    return results

def detect_languages_with_langdetect(text):
    """Return a list of detected languages with probabilities."""
    # First try simple detection
    simple_results = _simple_language_detect(text)
    if simple_results:
        # Convert to expected format
        normalized = []
        for lang, score in simple_results:
            normalized.append(type("L", (), {"lang": lang, "prob": score}))
        print(f"Debug: simple detection output: {[(n.lang, n.prob) for n in normalized]}")
        return normalized
    
    # Fall back to langdetect if simple detection fails
    cleaned = text
    langs = detect_langs(cleaned)
    print(f"Debug: raw langdetect output: {[(l.lang, l.prob) for l in langs]}")
    # Normalize language tags like zh-cn -> zh
    normalized = []
    for l in langs:
        code = l.lang.split("-")[0]
        normalized.append(type("L", (), {"lang": code, "prob": l.prob}))
    print(f"Debug: normalized langdetect output: {[(n.lang, n.prob) for n in normalized]}")
    return normalized


def validate_translated_languages(translated_text, target_language, require_english=True):
    """Ensure translated_text contains the target language and some English and no additional third language.
    If require_english is False, English presence will not be enforced.
    Raises RuntimeError on validation failure.
    """
    target_code = _map_target_code(target_language)
    langs = detect_languages_with_langdetect(translated_text)
    detected = [(l.lang, l.prob) for l in langs]
    # debug print
    print(f"Debug: Detected languages: {detected}")
    present = [lang for lang, prob in detected if prob >= 0.10]
    if target_code not in present:
        raise RuntimeError(f"Translated text does not contain the target language '{target_code}' (detected: {detected})")
    if require_english and "en" not in present:
        # if the translated text is exactly the target language with very high certainty, allow it
        high_conf = any(prob >= 0.95 and lang == target_code for lang, prob in detected)
        if not high_conf:
            raise RuntimeError(f"Translated text does not contain English (detected: {detected})")
    extras = [lang for lang, prob in detected if lang not in {target_code, "en"} and prob >= 0.05]
    if extras:
        raise RuntimeError(f"Translated text contains unexpected additional language(s): {extras} (detected: {detected})")
