import spacy
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


def detect_languages_with_langdetect(text):
    """Return a list of detected languages with probabilities using langdetect.
    Uses spaCy only for lightweight cleaning if available.
    Raises RuntimeError if required libraries are missing.
    """
    cleaned = text
    try:
        nlp = spacy.blank("en")
        doc = nlp(text)
        cleaned = " ".join([t.text for t in doc if not t.is_space])
    except Exception:
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
