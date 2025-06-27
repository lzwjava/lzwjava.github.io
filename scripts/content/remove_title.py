import os
import re

def remove_note_from_title(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    title_pattern = re.compile(r'title:\s*"([^"]*?)\(Note:[^"]*?\)"')

    for i, line in enumerate(lines):
        match = title_pattern.search(line)
        if match:
            new_title = re.sub(r'\(Note:[^"]*?\)', '', match.group(1)).strip()
            lines[i] = f'title: "{new_title}"\n'
            print(f"Updated title in {file_path} to '{new_title}'")
            break

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

def process_markdown_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split frontmatter and body
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter = f'---{parts[1]}---\n'
            body = parts[2].lstrip('\n')
        else:
            # No valid frontmatter
            return
    else:
        # No frontmatter
        return

    # Split body into lines and check first three for level 1 title
    body_lines = body.splitlines()
    new_body_lines = []
    skip_count = 0
    for i in range(min(3, len(body_lines))):
        if body_lines[i].strip().startswith('# '):
            skip_count += 1
        else:
            break
    new_body_lines = body_lines[skip_count:]
    # Strip leading/trailing whitespace
    new_body = '\n'.join(new_body_lines).strip() + '\n'

    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(frontmatter)
        f.write('\n')
        f.write(new_body)

def process_files_in_directory(directory):
    if not os.path.isdir(directory):
        raise FileNotFoundError(f"Directory '{directory}' does not exist.")

    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            file_path = os.path.join(directory, filename)
            remove_note_from_title(file_path)
            process_markdown_content(file_path)

# Get the absolute path to the notes directory
current_directory = os.path.dirname(os.path.abspath(__file__))
notes_directory = os.path.join(current_directory, '../notes')

process_files_in_directory(notes_directory)
