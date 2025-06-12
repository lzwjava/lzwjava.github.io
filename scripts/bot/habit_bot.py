import os
import requests
import argparse

# Load environment variables
TELEGRAM_HABIT_BOT_API_KEY = os.environ.get("TELEGRAM_HABIT_BOT_API_KEY")
TELEGRAM_CHAT_ID = "610574272" 

def send_telegram_message(bot_token, chat_id, message):
    """Sends a message to a Telegram chat using the Telegram Bot API."""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, params=params)
    if response.status_code != 200:
        print(f"Error sending Telegram message: {response.status_code} - {response.text}")
    else:
        print(f"Message sent: {message}")


def main():
    parser = argparse.ArgumentParser(description="Telegram Habit Reminder Bot")
    parser.add_argument("--job", choices=["send_reminder", "send_message"], required=True, help="Job to perform")
    parser.add_argument("--message", type=str, help="Message to send for 'send_message' job")
    args = parser.parse_args()

    if args.job == "send_reminder":
        if TELEGRAM_HABIT_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = "❓ *Ask Copilot!*"
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