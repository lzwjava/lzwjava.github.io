import pyperclip
import argparse

def copy_prompt_to_clipboard(prompt, debug=False):
    """Copy the prompt to clipboard for pasting into Copilot chat"""
    pyperclip.copy(prompt)
    if debug:
        print("✅ Prompt copied to clipboard!")
        print("📋 Please paste it into GitHub Copilot Chat and get your answer.")
        print("🔄 Then copy the answer and press Enter to continue...")

def wait_for_answer(debug=False):
    """Wait for user to copy the answer from Copilot chat"""
    input("Press Enter after you've copied the answer from Copilot Chat...")
    answer = pyperclip.paste()
    if answer:
        if debug:
            print("\n✅ Answer retrieved from clipboard:")
            print("-" * 50)
            print(answer)
            print("-" * 50)
        return answer
    else:
        if debug:
            print("❌ No content found in clipboard. Please copy the answer first.")
        return None

def call_clipboard_api_with_messages(messages, model=None, debug=False):
    """
    Clipboard API version that mimics the original OpenRouter API interface
    Uses paperclip workflow with Copilot Chat instead of API calls
    """
    if debug:
        print(f"Using clipboard workflow (model parameter ignored: {model})")
        print(f"Messages: {messages}")
    user_message = None
    for message in messages:
        if message.get("role") == "user":
            user_message = message.get("content")
            break
    if not user_message:
        raise Exception("No user message found in messages")
    return paperclip_workflow(user_message, debug=debug)

def call_clipboard_api(prompt, model=None, debug=False):
    """
    Clipboard API version that mimics the original OpenRouter API interface
    Uses paperclip workflow with Copilot Chat instead of API calls
    """
    messages = [{"role": "user", "content": prompt}]
    return call_clipboard_api_with_messages(messages, model, debug)

def paperclip_workflow(prompt, debug=False):
    """Main workflow for paperclip approach with Copilot chat"""
    if debug:
        print("🚀 Starting Paperclip Workflow with GitHub Copilot Chat")
        print("=" * 60)
        print(f"📝 Your prompt: {prompt}")
        print("=" * 60)
    copy_prompt_to_clipboard(prompt, debug=debug)
    answer = wait_for_answer(debug=debug)
    if answer:
        if debug:
            print("\n🎉 Workflow completed successfully!")
        return answer
    else:
        if debug:
            print("\n❌ Workflow failed. Please try again.")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Copy prompt to clipboard for Copilot Chat workflow.")
    parser.add_argument("prompt", nargs="+", help="Prompt to send to Copilot Chat")
    parser.add_argument("--debug", action="store_true", help="Enable debug output")
    args = parser.parse_args()
    prompt = " ".join(args.prompt)
    call_clipboard_api(prompt, debug=args.debug)
