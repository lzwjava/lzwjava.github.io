import pyperclip
import argparse

def copy_prompt_to_clipboard(prompt):
    """Copy the prompt to clipboard for pasting into Copilot chat"""
    pyperclip.copy(prompt)

def wait_for_answer():
    """Wait for user to copy the answer from Copilot chat"""
    input("Press Enter after you've copied the answer from Copilot Chat...")
    answer = pyperclip.paste()
    return answer if answer else None

def call_clipboard_api_with_messages(messages, model=None):
    user_message = None
    for message in messages:
        if message.get("role") == "user":
            user_message = message.get("content")
            break
    if not user_message:
        raise Exception("No user message found in messages")
    return paperclip_workflow(user_message)

def call_clipboard_api(prompt, model=None):
    messages = [{"role": "user", "content": prompt}]
    return call_clipboard_api_with_messages(messages, model)

def paperclip_workflow(prompt):
    copy_prompt_to_clipboard(prompt)
    answer = wait_for_answer()
    return answer

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Copy prompt to clipboard for Copilot Chat workflow.")
    parser.add_argument("prompt", nargs="+", help="Prompt to send to Copilot Chat")
    args = parser.parse_args()
    prompt = " ".join(args.prompt)
    call_clipboard_api(prompt)
