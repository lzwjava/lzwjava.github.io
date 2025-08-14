import pyperclip
import argparse

def call_pyperclip_api(prompt, model=None):
    messages = [{"role": "user", "content": prompt}]
    return call_clipboard_api_with_messages(messages, model)

def call_clipboard_api_with_messages(messages, model=None):
    user_message = None
    for message in messages:
        if message.get("role") == "user":
            user_message = message.get("content")
            break
    if not user_message:
        raise Exception("No user message found in messages")
    # Use call_pyperclip_api to handle the clipboard interaction
    pyperclip.copy(user_message)
    input("Press Enter after you've copied the answer from Copilot Chat...")
    answer = pyperclip.paste()
    return answer if answer else None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Copy prompt to clipboard for Copilot Chat workflow.")
    parser.add_argument("prompt", nargs="+", help="Prompt to send to Copilot Chat")
    args = parser.parse_args()
    prompt = " ".join(args.prompt)
    call_pyperclip_api(prompt)
