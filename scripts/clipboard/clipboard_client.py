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

def interactive_mode():
    """Interactive mode for continuous prompt-answer workflow"""
    print("🤖 GitHub Copilot Paperclip Assistant")
    print("Type 'quit' or 'exit' to stop")
    print("=" * 50)
    
    while True:
        try:
            prompt = input("\n💭 Enter your prompt: ").strip()
            
            if prompt.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
            
            if not prompt:
                print("❌ Please enter a valid prompt.")
                continue
            
            answer = paperclip_workflow(prompt)
            
            if answer:
                # Ask if user wants to save the answer somewhere
                save_choice = input("\n💾 Would you like to copy the answer back to clipboard? (y/n): ").strip().lower()
                if save_choice in ['y', 'yes']:
                    pyperclip.copy(answer)
                    print("✅ Answer copied to clipboard!")
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ An error occurred: {str(e)}")

def batch_prompts(prompts):
    """Process multiple prompts in batch"""
    results = []
    
    for i, prompt in enumerate(prompts, 1):
        print(f"\n🔄 Processing prompt {i}/{len(prompts)}")
        answer = paperclip_workflow(prompt)
        results.append({
            'prompt': prompt,
            'answer': answer
        })
        
        if i < len(prompts):
            continue_choice = input("\n➡️  Continue to next prompt? (y/n): ").strip().lower()
            if continue_choice not in ['y', 'yes']:
                break
    
    return results

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Command line mode with prompt as argument
        prompt = " ".join(sys.argv[1:])
        paperclip_workflow(prompt)
    else:
        # Interactive mode
        interactive_mode()
