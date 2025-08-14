import pyperclip
import time
import sys

def copy_prompt_to_clipboard(prompt):
    """Copy the prompt to clipboard for pasting into Copilot chat"""
    pyperclip.copy(prompt)
    print("✅ Prompt copied to clipboard!")
    print("📋 Please paste it into GitHub Copilot Chat and get your answer.")
    print("🔄 Then copy the answer and press Enter to continue...")

def wait_for_answer():
    """Wait for user to copy the answer from Copilot chat"""
    input("Press Enter after you've copied the answer from Copilot Chat...")
    
    # Get the answer from clipboard
    answer = pyperclip.paste()
    
    if answer:
        print("\n✅ Answer retrieved from clipboard:")
        print("-" * 50)
        print(answer)
        print("-" * 50)
        return answer
    else:
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
    
    # Extract the user prompt from messages
    user_message = None
    for message in messages:
        if message.get("role") == "user":
            user_message = message.get("content")
            break
    
    if not user_message:
        raise Exception("No user message found in messages")
    
    return paperclip_workflow(user_message)

def call_clipboard_api(prompt, model=None, debug=False):
    """
    Clipboard API version that mimics the original OpenRouter API interface
    Uses paperclip workflow with Copilot Chat instead of API calls
    """
    messages = [{"role": "user", "content": prompt}]
    return call_clipboard_api_with_messages(messages, model, debug)

def paperclip_workflow(prompt):
    """Main workflow for paperclip approach with Copilot chat"""
    print("🚀 Starting Paperclip Workflow with GitHub Copilot Chat")
    print("=" * 60)
    print(f"📝 Your prompt: {prompt}")
    print("=" * 60)
    
    # Step 1: Copy prompt to clipboard
    copy_prompt_to_clipboard(prompt)
    
    # Step 2: Wait for user to get answer and copy it
    answer = wait_for_answer()
    
    if answer:
        print("\n🎉 Workflow completed successfully!")
        return answer
    else:
        print("\n❌ Workflow failed. Please try again.")
        return None


if __name__ == "__main__":
    prompt = " ".join(sys.argv[1:])
    paperclip_workflow(prompt)