import os
import requests
from dotenv import load_dotenv
import json
import subprocess
import argparse
import math
import time # For potential future continuous monitoring

load_dotenv()

# New: Specific API key for the location bot
TELEGRAM_LOCATION_BOT_API_KEY = os.environ.get("TELEGRAM_LOCATION_BOT_API_KEY") # Ensure this is set in your .env
TELEGRAM_CHAT_ID = "610574272" # This chat ID is for sending the notification message

# Define your office coordinates
OFFICE_LATITUDE = 23.135368
OFFICE_LONGITUDE = 113.32952

# Proximity radius in meters
PROXIMITY_RADIUS_METERS = 300

def send_telegram_message(bot_token, chat_id, message):
    """Sends a message to a Telegram chat using the Telegram Bot API."""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown" # Using Markdown for bold text in the message
    }
    response = requests.post(url, params=params)
    if response.status_code != 200:
        print(f"Error sending Telegram message: {response.status_code} - {response.text}")

def get_latest_location(bot_token):
    """Retrieves the latest live location update from the bot."""
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    # Offset to get only new updates after the last processed one (for continuous polling)
    # For a simple run-once script, we'll just get the latest, but for polling, you'd manage an offset.
    params = {"offset": -1} # Get the very last update
    response = requests.get(url, params=params)
    print("GetUpdates Response:", response) # Debugging
    if response.status_code == 200:
        updates = response.json()
        print("GetUpdates JSON:", json.dumps(updates, indent=4)) # Debugging
        if updates['result']:
            last_update = updates['result'][-1]
            # Prioritize edited_message for live locations
            if 'edited_message' in last_update and 'location' in last_update['edited_message']:
                return last_update['edited_message']['location'], last_update['edited_message']['chat']['id']
            elif 'message' in last_update and 'location' in last_update['message']:
                # Handle initial live location messages or static location shares
                return last_update['message']['location'], last_update['message']['chat']['id']
    return None, None

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the distance between two points on Earth using the Haversine formula.
    Returns distance in meters.
    """
    R = 6371000  # Radius of Earth in meters

    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad

    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c
    return distance

def main():
    parser = argparse.ArgumentParser(description="Telegram Bot Script")
    parser.add_argument('--job', choices=['get_chat_id', 'send_message', 'check_location'], required=True, help="Job to perform")
    args = parser.parse_args()

    if args.job == 'get_chat_id':
        # This part is largely for debugging or initial setup
        bot_token = TELEGRAM_LOCATION_BOT_API_KEY # Or TELEGRAM_LOCATION_BOT_API_KEY, depending on which bot you want to get updates for
        url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
        response = requests.get(url)
        if response.status_code == 200:
            updates = response.json()
            print(json.dumps(updates, indent=4))
            if updates['result']:
                last_update = updates['result'][-1]
                chat_id = None
                if 'message' in last_update and 'chat' in last_update['message']:
                    chat_id = last_update['message']['chat']['id']
                elif 'edited_message' in last_update and 'chat' in last_update['edited_message']:
                    chat_id = last_update['edited_message']['chat']['id']
                elif 'channel_post' in last_update and 'chat' in last_update['channel_post']:
                    chat_id = last_update['channel_post']['chat']['id']
                elif 'edited_channel_post' in last_update and 'chat' in last_update['edited_channel_post']:
                    chat_id = last_update['edited_channel_post']['chat']['id']

                if chat_id:
                    print(f"Chat ID: {chat_id}")
                else:
                    print("Could not retrieve chat ID from the last update.")
            else:
                print("No updates found.")
        else:
            print(f"Error fetching updates: {response.status_code} - {response.text}")


    elif args.job == 'send_message':
        if TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = "This is a test message from your Telegram bot script!"
            send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print("Test message sent successfully.")
        else:
            print("TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID are not set.")

    elif args.job == 'check_location':
        if not TELEGRAM_LOCATION_BOT_API_KEY or not TELEGRAM_CHAT_ID:
            print("TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID must be set for location checks.")
            return

        user_location, location_chat_id = get_latest_location(TELEGRAM_LOCATION_BOT_API_KEY)

        if user_location:
            current_latitude = user_location['latitude']
            current_longitude = user_location['longitude']

            distance = haversine_distance(
                OFFICE_LATITUDE, OFFICE_LONGITUDE,
                current_latitude, current_longitude
            )

            print(f"Current location: ({current_latitude}, {current_longitude})")
            print(f"Distance to office: {distance:.2f} meters")

            if distance <= PROXIMITY_RADIUS_METERS:
                print(f"You are within {PROXIMITY_RADIUS_METERS}m of the office!")
                # The message should be sent to the specific chat ID you want to be notified in
                # This could be TELEGRAM_CHAT_ID (for blog updates) or location_chat_id (the one sending live location)
                # For "Punch card", it's likely a personal notification, so TELEGRAM_CHAT_ID or the specific location_chat_id is good.
                notification_message = (
                    f"🎉 *Arrived Office!* 🎉\n"
                    f"Time to Punch card in WeCom.\n"
                    f"Your current distance from office: {distance:.2f}m."
                )
                send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, notification_message)
            else:
                print(f"You are outside the {PROXIMITY_RADIUS_METERS}m office circle.")
        else:
            print("Could not retrieve your latest location. Make sure you are sharing live location with the bot.")

if __name__ == '__main__':
    main()