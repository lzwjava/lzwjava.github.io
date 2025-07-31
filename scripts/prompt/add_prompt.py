import os
import pyperclip

# Get the current directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the prompt.md file
prompt_file = os.path.join(script_dir, 'prompt.md')

# Get the prompt from clipboard
new_prompt = pyperclip.paste().strip()

# Check if the file exists and has content
if os.path.exists(prompt_file) and os.path.getsize(prompt_file) > 0:
    separator = '\n---\n'
else:
    separator = ''

# Append the new prompt
with open(prompt_file, 'a') as f:
    f.write(separator + new_prompt)