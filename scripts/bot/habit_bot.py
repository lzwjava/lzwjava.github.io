import os
import requests
import argparse
import re
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Environment variables
TELEGRAM_HABIT_BOT_API_KEY = os.environ.get("TELEGRAM_HABIT_BOT_API_KEY")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
MISTRAL_API_KEY = os.environ.get("MISTRAL_API_KEY")

# Telegram message length limit
TELEGRAM_MAX_LENGTH = 4096

def send_telegram_message(bot_token, chat_id, message):
    """Sends a message to a Telegram chat using the Telegram Bot API."""
    if not bot_token or not chat_id:
        print("Error: TELEGRAM_HABIT_BOT_API_KEY or TELEGRAM_CHAT_ID not set.")
        return False
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    # Remove Markdown asterisks and URLs to ensure Telegram compatibility
    message_no_stars = message.replace('*', '')
    url_pattern = re.compile(r'(https?://[^\s]+)')
    message_no_links = url_pattern.sub('', message_no_stars)
    # Split message if it exceeds Telegram's length limit
    messages = []
    msg = message_no_links
    while len(msg) > TELEGRAM_MAX_LENGTH:
        split_idx = msg.rfind('\n', 0, TELEGRAM_MAX_LENGTH)
        if split_idx == -1 or split_idx < TELEGRAM_MAX_LENGTH // 2:
            split_idx = TELEGRAM_MAX_LENGTH
        messages.append(msg[:split_idx])
        msg = msg[split_idx:]
    messages.append(msg)
    success = True
    for part in messages:
        params = {
            "chat_id": chat_id,
            "text": part,
            "parse_mode": "Markdown"
        }
        try:
            response = requests.post(url, params=params)
            response.raise_for_status()
            print(f"Successfully sent Telegram message part ({len(part)} chars).")
        except requests.exceptions.RequestException as e:
            print(f"Error sending Telegram message: {e}")
            success = False
    return success

def call_mistral_api(prompt, model="mistral-small-latest"):
    """Calls the Mistral API to generate a response."""
    if not MISTRAL_API_KEY:
        print("Error: MISTRAL_API_KEY environment variable not set.")
        return None
    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {MISTRAL_API_KEY}"
    }
    data = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    try:
        print(f"Calling Mistral API with model: {model}")
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        if response_json and response_json.get('choices'):
            content = response_json['choices'][0]['message']['content']
            print(f"Mistral API Content: {content}")
            return content
        else:
            print(f"Mistral API Error: Invalid response format: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Mistral API Error: {e}")
        return None

def generate_copilot_message():
    """Generates a specific technical question via Mistral API."""
    prompt = (
        "Generate a single, specific technical question for a backend engineer using technologies like "
        "Java, Spring Boot, Control-M, IBM WebSphere, Maven, multithreading, or Nexus. "
        "The question should be concise, actionable, and practical (e.g., 'How to set X?' or 'What’s the best way to Y?'). "
        "Keep it under 300 characters, avoid Markdown or URLs, and output only the question."
    )
    message = call_mistral_api(prompt)
    if message:
        return message.strip()[:300]
    return "How do you set thread pool size in Java’s ExecutorService?"

def main():
    parser = argparse.ArgumentParser(description="Telegram Habit Reminder Bot")
    parser.add_argument("--job", choices=["send_reminder", "send_message"], required=True, help="Job to perform")
    parser.add_argument("--message", type=str, help="Message to send for 'send_message' job")
    args = parser.parse_args()

    if args.job == "send_reminder":
        if TELEGRAM_HABIT_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = generate_copilot_message()
            send_telegram_message(TELEGRAM_HABIT_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
        else:
            print("Error: TELEGRAM_HABIT_BOT_API_KEY or TELEGRAM_CHAT_ID not set.")
    elif args.job == "send_message":
        if TELEGRAM_HABIT_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = args.message if args.message else "Default test message from the bot!"
            send_telegram_message(TELEGRAM_HABIT_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
        else:
            print("Error: TELEGRAM_HABIT_BOT_API_KEY or TELEGRAM_CHAT_ID not set.")

if __name__ == "__main__":
    main()