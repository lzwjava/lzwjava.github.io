---
audio: false
generated: false
lang: hi
layout: post
title: टेलीग्राम लोकेशन बॉट के साथ अपने पंच कार्ड को ऑटोमेट करने
translated: true
---

क्या आप अपने दैनिक "पंच कार्ड" को कम बोझिल बनाना चाहते हैं? मैं निश्चित रूप से चाहता था। इसलिए मैंने एक व्यक्तिगत टेलिग्राम बॉट बनाया है जो स्थान ट्रैकिंग का उपयोग करके कार्यालय पहुंच की सूचनाओं को स्वचालित करता है और उन महत्वपूर्ण चेक-इन के बारे में मुझे याद दिलाता है। यह पोस्ट बताता है कि मैंने कैसे पाइथन को GitHub Actions के साथ मिलाकर एक सीमलेस, हाथों से मुक्त प्रणाली बनाई, जो मुझे ठीक उसी समय सूचित रखता है जब मुझे इसकी आवश्यकता होती है, पूरी तरह से मेरे स्थान के आधार पर।

```yml
name: Hourly Location Check

on:
  schedule:
    # हर घंटे, घंटे पर, 11 AM और 11 PM के बीच, सप्ताह के दिनों में (सोमवार से शुक्रवार)
    # समय UTC में है। सिंगापुर का समय (SGT) UTC+8 है।
    # इसलिए, 11 AM SGT 03:00 UTC है, और 11 PM SGT 15:00 UTC है।
    # इसलिए, हमें 03:00 से 15:00 UTC तक शेड्यूल करना होगा।
    - cron: '0 3-15 * * 1-5'

    # लाइव लोकेशन शेयर करने की याद दिलाने के लिए: बुधवार 11 AM SGT (3 AM UTC)
    # वर्तमान समय: रविवार, 8 जून, 2025 को 5:10:58 PM +08 (SGT)
    # बुधवार 11 AM SGT (UTC+8) के लिए: 11 - 8 = 3 AM UTC.
    - cron: '0 3 * * 3' # 3 बुधवार के लिए

    # लाइव लोकेशन शेयर करना बंद करने की याद दिलाने के लिए: शुक्रवार 11 PM SGT (3 PM UTC)
    # वर्तमान समय: रविवार, 8 जून, 2025 को 5:10:58 PM +08 (SGT)
    # शुक्रवार 11 PM SGT (UTC+8) के लिए: 23 - 8 = 15 PM UTC.
    - cron: '0 15 * * 5' # 5 शुक्रवार के लिए

  workflow_dispatch:  # वर्कफ्लो को मैन्युअल रूप से ट्रिगर करने की अनुमति देता है
  push:
    branches: ["main"]
    paths:
      - 'scripts/release/location_bot.py' # आपकी स्क्रिप्ट के लिए सही पथ
      - '.github/workflows/location.yml' # इस वर्कफ्लो फाइल के लिए पथ

concurrency:
  group: 'location'
  cancel-in-progress: false

jobs:
  check_and_notify:
    runs-on: ubuntu-latest
    env:
      TELEGRAM_LOCATION_BOT_API_KEY: ${{ secrets.TELEGRAM_LOCATION_BOT_API_KEY }}

    steps:
    - name: रिपॉजिटरी चेकआउट
      uses: actions/checkout@v4
      with:
        fetch-depth: 5 # कुशलता के लिए केवल पिछले 5 कमिट्स को फेटच करें

    - name: Python 3.13.2 सेटअप
      uses: actions/setup-python@v4
      with:
        python-version: "3.13.2" # सही Python संस्करण निर्दिष्ट करें

    - name: निर्भरताओं को इंस्टॉल करें
      run: |
        python -m pip install --upgrade pip
        # मान लीजिए कि आपके रिपॉजिटरी रूट में एक requirements.simple.txt है।
        # अगर नहीं है, तो उपयोग करें: pip install requests python-dotenv
        pip install -r requirements.simple.txt

    - name: लोकेशन चेक स्क्रिप्ट चलाएं (शेड्यूल्ड)
      run: python scripts/release/location_bot.py --job check_location
      # यह चरण शेड्यूल्ड ट्रिगर्स के लिए घंटे भर में चेक के लिए चलाएगा
      if: github.event.schedule == '0 3-15 * * 1-5' # घंटे भर के क्रोन शेड्यूल के साथ मेल खाएं

    - name: लाइव लोकेशन शेयर करने की याद दिलाने के लिए
      run: python scripts/release/location_bot.py --job start_sharing_message
      if: github.event.schedule == '0 3 * * 3' # बुधवार 11 AM SGT क्रोन के साथ मेल खाएं

    - name: लाइव लोकेशन शेयर करना बंद करने की याद दिलाने के लिए
      run: python scripts/release/location_bot.py --job stop_sharing_message
      if: github.event.schedule == '0 15 * * 5' # शुक्रवार 11 PM SGT क्रोन के साथ मेल खाएं

    - name: टेस्ट संदेश के लिए टेलिग्राम स्क्रिप्ट चलाएं (मैन्युअल ट्रिगर)
      run: python scripts/release/location_bot.py --job send_message --message "यह एक मैन्युअल ट्रिगर टेस्ट संदेश है GitHub Actions से."
      if: github.event_name == 'workflow_dispatch'

    - name: मेन ब्रांच में पुश के लिए टेलिग्राम स्क्रिप्ट चलाएं
      run: python scripts/release/location_bot.py --job send_message --message "लोकेशन बॉट के लिए कोड बदलाव मेन ब्रांच में पुश किया गया है."
      if: github.event_name == 'push'
```

```python
import os
import requests
from dotenv import load_dotenv
import json
import subprocess
import argparse
import math
import time # भविष्य के संभावित निरंतर निगरानी के लिए

load_dotenv()

# नया: लोकेशन बॉट के लिए विशिष्ट API की
TELEGRAM_LOCATION_BOT_API_KEY = os.environ.get("TELEGRAM_LOCATION_BOT_API_KEY") # सुनिश्चित करें कि यह आपकी .env में सेट है
TELEGRAM_CHAT_ID = "610574272" # यह चैट आईडी सूचना संदेश भेजने के लिए है

# अपने कार्यालय के निर्देशांक परिभाषित करें
OFFICE_LATITUDE = 23.135368
OFFICE_LONGITUDE = 113.32952

# प्रॉक्सिमिटी रेडियस मीटर में
PROXIMITY_RADIUS_METERS = 300

def send_telegram_message(bot_token, chat_id, message):
    """टेलिग्राम चैट को संदेश भेजता है, टेलिग्राम बॉट API का उपयोग करके।"""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown" # संदेश में बोल्ड टेक्स्ट के लिए Markdown का उपयोग
    }
    response = requests.post(url, params=params)
    if response.status_code != 200:
        print(f"टेलिग्राम संदेश भेजने में त्रुटि: {response.status_code} - {response.text}")

def get_latest_location(bot_token):
    """बॉट से सबसे हालिया लाइव लोकेशन अपडेट प्राप्त करता है।"""
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    # पोलिंग के लिए पिछले प्रोसेस किए गए अपडेट के बाद के केवल नए अपडेट प्राप्त करने के लिए ऑफसेट
    # एक सरल रन-वन स्क्रिप्ट के लिए, हम बस सबसे हालिया प्राप्त करेंगे, लेकिन पोलिंग के लिए, आप एक ऑफसेट प्रबंधित करेंगे।
    params = {"offset": -1} # सबसे अंतिम अपडेट प्राप्त करें
    response = requests.get(url, params=params)
    print("GetUpdates Response:", response) # डिबगिंग
    if response.status_code == 200:
        updates = response.json()
        print("GetUpdates JSON:", json.dumps(updates, indent=4)) # डिबगिंग
        if updates['result']:
            last_update = updates['result'][-1]
            # लाइव लोकेशन के लिए edited_message को प्राथमिकता दें
            if 'edited_message' in last_update and 'location' in last_update['edited_message']:
                return last_update['edited_message']['location'], last_update['edited_message']['chat']['id']
            elif 'message' in last_update and 'location' in last_update['message']:
                # प्रारंभिक लाइव लोकेशन संदेशों या स्थिर लोकेशन शेयरों को हैंडल करें
                return last_update['message']['location'], last_update['message']['chat']['id']
    return None, None

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    पृथ्वी पर दो बिंदुओं के बीच की दूरी का गणना हेवर्साइन फॉर्मूला का उपयोग करके।
    मीटर में दूरी लौटाता है।
    """
    R = 6371000  # पृथ्वी की त्रिज्या मीटर में

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
    parser = argparse.ArgumentParser(description="टेलिग्राम बॉट स्क्रिप्ट")
    # --job तर्क के लिए अपडेट किए गए विकल्प
    parser.add_argument('--job', choices=['get_chat_id', 'send_message', 'check_location', 'start_sharing_message', 'stop_sharing_message'], required=True, help="करने के लिए काम")
    # 'send_message' काम के लिए --message तर्क जोड़ा गया
    parser.add_argument('--message', type=str, help="'send_message' काम के लिए भेजने के लिए संदेश")
    # 'check_location' काम के लिए --test तर्क जोड़ा गया
    parser.add_argument('--test', action='store_true', help="'check_location' काम के लिए, प्रॉक्सिमिटी के बावजूद संदेश भेजने के लिए मजबूर करें।")
    args = parser.parse_args()

    if args.job == 'get_chat_id':
        bot_token = TELEGRAM_LOCATION_BOT_API_KEY
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
                    print(f"चैट आईडी: {chat_id}")
                else:
                    print("पिछले अपडेट से चैट आईडी प्राप्त नहीं कर पाया।")
            else:
                print("कोई अपडेट नहीं मिला।")
        else:
            print(f"अपडेट प्राप्त करने में त्रुटि: {response.status_code} - {response.text}")

    elif args.job == 'send_message':
        if TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = args.message if args.message else "यह आपकी टेलिग्राम बॉट स्क्रिप्ट से एक डिफ़ॉल्ट टेस्ट संदेश है!"
            send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print(f"संदेश सफलतापूर्वक भेजा गया: {message}")
        else:
            print("TELEGRAM_LOCATION_BOT_API_KEY और TELEGRAM_CHAT_ID सेट नहीं हैं।")

    elif args.job == 'start_sharing_message':
        if TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = "⚠️ *याद दिलाने के लिए:* कृपया बॉट को अपने लाइव लोकेशन शेयर करना शुरू करें!"
            send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print("शुरू करने की याद दिलाने वाला संदेश भेजा गया।")
        else:
            print("TELEGRAM_LOCATION_BOT_API_KEY और TELEGRAM_CHAT_ID सेट नहीं हैं।")

    elif args.job == 'stop_sharing_message':
        if TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = "✅ *याद दिलाने के लिए:* अब आप अपने लाइव लोकेशन शेयर करना बंद कर सकते हैं।"
            send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print("बंद करने की याद दिलाने वाला संदेश भेजा गया।")
        else:
            print("TELEGRAM_LOCATION_BOT_API_KEY और TELEGRAM_CHAT_ID सेट नहीं हैं।")

    elif args.job == 'check_location':
        if not TELEGRAM_LOCATION_BOT_API_KEY or not TELEGRAM_CHAT_ID:
            print("लोकेशन चेक के लिए TELEGRAM_LOCATION_BOT_API_KEY और TELEGRAM_CHAT_ID सेट होने चाहिए।")
            return

        user_location, location_chat_id = get_latest_location(TELEGRAM_LOCATION_BOT_API_KEY)

        if user_location:
            current_latitude = user_location['latitude']
            current_longitude = user_location['longitude']

            distance = haversine_distance(
                OFFICE_LATITUDE, OFFICE_LONGITUDE,
                current_latitude, current_longitude
            )

            print(f"वर्तमान स्थान: ({current_latitude}, {current_longitude})")
            print(f"कार्यालय से दूरी: {distance:.2f} मीटर")

            needs_punch_card = distance <= PROXIMITY_RADIUS_METERS

            if needs_punch_card:
                print(f"आप कार्यालय के {PROXIMITY_RADIUS_METERS}m के भीतर हैं!")
                notification_message = (
                    f"🎉 *कार्यालय पहुंच गए!* 🎉\n"
                    f"समय WeCom में पंच कार्ड करना है।\n"
                    f"आपका वर्तमान कार्यालय से दूरी: {distance:.2f}m."
                )
            else:
                print(f"आप {PROXIMITY_RADIUS_METERS}m कार्यालय वृत्त के बाहर हैं।")
                # रेडियस के बाहर के लिए संदेश
                notification_message = (
                    f"📍 आप *बाहर* हैं कार्यालय के प्रॉक्सिमिटी ({PROXIMITY_RADIUS_METERS}m).\n"
                    f"इस समय पंच कार्ड की आवश्यकता नहीं है।\n"
                    f"आपका वर्तमान कार्यालय से दूरी: {distance:.2f}m."
                )

            # संदेश भेजें अगर प्रॉक्सिमिटी के भीतर हैं या --test फ्लैग का उपयोग किया गया है
            if needs_punch_card or args.test:
                send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, notification_message)
            else:
                # अगर प्रॉक्सिमिटी के बाहर हैं और टेस्ट मोड में नहीं हैं, तो केवल कंसोल में प्रिंट करें (कोई टेलिग्राम संदेश नहीं)
                print("प्रॉक्सिमिटी के बाहर हैं और टेस्ट मोड में नहीं हैं, कोई संदेश टेलिग्राम को नहीं भेजा गया।")
        else:
            print("आपका सबसे हालिया स्थान प्राप्त नहीं किया जा सका। सुनिश्चित करें कि आप बॉट के साथ लाइव लोकेशन शेयर कर रहे हैं।")

if __name__ == '__main__':
    main()
```

---

अपडेट: यह अच्छा नहीं है क्योंकि आपको बॉट के साथ अपने लाइव लोकेशन शेयर करने की आवश्यकता है।