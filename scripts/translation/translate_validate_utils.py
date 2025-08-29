def validate_length(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    length = len(text)
    if not 1 <= length <= 30000:
        raise ValueError(f"text length {length} outside allowed range [1, 30000]")

def clean_response(text):
    if not isinstance(text, str):
        raise RuntimeError("Model returned non-text response")
    return text.strip()

def check_echo(original, translated):
    if original.lower().strip() in translated.lower():
        raise RuntimeError("Model returned input or echoed text")

def check_commentary(translated):
    indicators = [
        "the output is", "output is", "translated title",
        "the translation is", "translation is", "translated:",
        "result:", "output:", "return only", "return only the translated"
    ]
    low = translated.lower()
    for ind in indicators:
        if ind in low:
            raise RuntimeError("Model included commentary")

def check_title_strict(title, target_lang):
    """Strict title validation - removes quotes and special chars based on language"""
    if "\n" in title.strip():
        raise RuntimeError("Model returned multi-line title")
    
    # Define forbidden characters by language
    forbidden_chars = {
        'ja': ['"', "'", '"', '"', '「', '」', '『', '』', '《', '》'],
        'zh': ['"', "'", '"', '"', '「', '」', '『', '』', '《', '》', '〈', '〉'],
        'hant': ['"', "'", '"', '"', '「', '」', '『', '』', '《', '》', '〈', '〉'],
        'hi': ['"', "'", '"', '"', '«', '»'],
        'ar': ['"', "'", '"', '"', '«', '»'],
        'es': ['"', "'", '"', '"', '«', '»'],
        'fr': ['"', "'", '"', '"', '«', '»'],
        'de': ['"', "'", '"', '"', '„', '"', '»', '«'],
        'en': ['"', "'", '"', '"']
    }
    
    # Get forbidden chars for target language, default to common quotes
    chars_to_remove = forbidden_chars.get(target_lang, ['"', "'", '"', '"'])
    
    # Check if title contains any forbidden characters
    for char in chars_to_remove:
        if char in title:
            raise RuntimeError(f"Title contains forbidden character: {char}")
    
    return title.strip()

def check_markdown_table_formatting(text):
    """Check for markdown table formatting issues - headers immediately followed by tables"""
    import re
    
    lines = text.split('\n')
    issues = []
    
    for i, line in enumerate(lines):
        # Check if line is a header (starts with #)
        if re.match(r'^#+\s+', line.strip()):
            # Look for the next non-empty line
            next_line_idx = i + 1
            while next_line_idx < len(lines) and not lines[next_line_idx].strip():
                next_line_idx += 1
            
            # Check if the next non-empty line is a table (starts with |)
            if (next_line_idx < len(lines) and 
                lines[next_line_idx].strip().startswith('|')):
                header_text = line.strip()
                table_preview = lines[next_line_idx].strip()
                if len(table_preview) > 50:
                    table_preview = table_preview[:47] + "..."
                issues.append(f"Header '{header_text}' immediately followed by table '{table_preview}'")
    
    if issues:
        raise RuntimeError(f"Found {len(issues)} markdown table formatting issues: " + "; ".join(issues))