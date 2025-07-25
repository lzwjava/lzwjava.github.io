from create_note_utils import get_clipboard_content, clean_grok_tags, generate_title, create_filename, format_front_matter, clean_content, write_note


def create_note():
    # Get and validate clipboard content
    content = get_clipboard_content()

    # Clean grok tags if present
    content = clean_grok_tags(content)

    # Generate titles
    full_title_prompt = lambda c: f"Generate a very short title (maximum six words) for the following text and respond with only the title: {c}"
    full_title = generate_title(content, 6, full_title_prompt)

    short_title_prompt = lambda c: f"Generate a very short title (maximum three words, all lowercase, use only letters, numbers, or hyphens, no spaces or special characters, do not have single quote, use hypen to concatenate words) for the following text and respond with only the title: {c}"
    short_title = generate_title(content, 3, short_title_prompt).lower()

    # Create file path
    file_path = create_filename(short_title)

    # Format front matter
    front_matter = format_front_matter(full_title)

    # Clean content
    content = clean_content(content)

    # Write to file
    write_note(file_path, front_matter, content)


if __name__ == "__main__":
    create_note()