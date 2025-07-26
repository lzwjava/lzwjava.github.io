---
audio: false
generated: false
image: false
lang: de
layout: post
title: Automatisierung Ihrer Lochkarte mit einem Telegram-Standort-Bot
translated: true
---

Hast du dich jemals gefragt, ob dein täglicher "Stempelkarten"-Routine weniger lästig sein könnte? Ich auf jeden Fall. Deshalb habe ich einen persönlichen Telegram-Bot gebaut, der Standortverfolgung nutzt, um Büroankunftsbenachrichtigungen zu automatisieren und mich an wichtige Check-ins zu erinnern. Dieser Beitrag zeigt, wie ich Python mit GitHub Actions kombiniert habe, um ein nahtloses, hands-off-System zu erstellen, das mich genau dann informiert, wenn ich es brauche – alles basierend auf meinem Standort.

```yml
name: Stündliche Standortprüfung

on:
  schedule:
    # Wird jede Stunde, auf die Stunde, zwischen 11 Uhr und 23 Uhr, an Wochentagen (Montag-Freitag) ausgeführt
    # Die Zeit ist in UTC. Singapur-Zeit (SGT) ist UTC+8.
    # Also ist 11 Uhr SGT 03:00 UTC und 23 Uhr SGT 15:00 UTC.
    # Daher müssen wir von 03:00 bis 15:00 UTC planen.
    - cron: '0 3-15 * * 1-5'

    # Erinnerung zum STARTEN der Live-Standortfreigabe: Mittwoch 11 Uhr SGT (3 Uhr UTC)
    # Aktuelle Zeit: Sonntag, 8. Juni 2025, 17:10:58 +08 (SGT)
    # Für Mittwoch 11 Uhr SGT (UTC+8): 11 - 8 = 3 Uhr UTC.
    - cron: '0 3 * * 3' # 3 für Mittwoch

    # Erinnerung zum STOPPEN der Live-Standortfreigabe: Freitag 23 Uhr SGT (15 Uhr UTC)
    # Aktuelle Zeit: Sonntag, 8. Juni 2025, 17:10:58 +08 (SGT)
    # Für Freitag 23 Uhr SGT (UTC+8): 23 - 8 = 15 Uhr UTC.
    - cron: '0 15 * * 5' # 5 für Freitag

  workflow_dispatch:  # Ermöglicht manuelles Auslösen des Workflows
  push:
    branches: ["main"]
    paths:
      - 'scripts/release/location_bot.py' # Korrigierter Pfad zu deinem Skript
      - '.github/workflows/location.yml' # Pfad zu dieser Workflow-Datei

concurrency:
  group: 'location'
  cancel-in-progress: false

jobs:
  check_and_notify:
    runs-on: ubuntu-latest
    env:
      TELEGRAM_LOCATION_BOT_API_KEY: ${{ secrets.TELEGRAM_LOCATION_BOT_API_KEY }}

    steps:
    - name: Repository auschecken
      uses: actions/checkout@v4
      with:
        fetch-depth: 5 # Lade nur die letzten 5 Commits für Effizienz

    - name: Python 3.13.2 einrichten
      uses: actions/setup-python@v4
      with:
        python-version: "3.13.2" # Spezifische Python-Version angeben

    - name: Abhängigkeiten installieren
      run: |
        python -m pip install --upgrade pip
        # Angenommen, du hast eine requirements.simple.txt in deinem Repo-Verzeichnis.
        # Falls nicht, verwende: pip install requests python-dotenv
        pip install -r requirements.simple.txt

    - name: Standortprüfungsskript ausführen (Geplant)
      run: python scripts/release/location_bot.py --job check_location
      # Dieser Schritt wird bei geplanten Auslösern für die stündliche Prüfung ausgeführt
      if: github.event.schedule == '0 3-15 * * 1-5' # Übereinstimmung mit dem stündlichen Cron-Zeitplan

    - name: Erinnerung zum STARTEN der Live-Standortfreigabe
      run: python scripts/release/location_bot.py --job start_sharing_message
      if: github.event.schedule == '0 3 * * 3' # Übereinstimmung mit dem Cron-Zeitplan für Mittwoch 11 Uhr SGT

    - name: Erinnerung zum STOPPEN der Live-Standortfreigabe
      run: python scripts/release/location_bot.py --job stop_sharing_message
      if: github.event.schedule == '0 15 * * 5' # Übereinstimmung mit dem Cron-Zeitplan für Freitag 23 Uhr SGT

    - name: Telegram-Skript für Testnachricht ausführen (Manuelle Auslösung)
      run: python scripts/release/location_bot.py --job send_message --message "Dies ist eine manuell ausgelöste Testnachricht von GitHub Actions."
      if: github.event_name == 'workflow_dispatch'

    - name: Telegram-Skript für Push auf den main-Zweig ausführen
      run: python scripts/release/location_bot.py --job send_message --message "Codeänderungen für den Standort-Bot wurden in den main-Zweig gepusht."
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
import time # Für potenzielle zukünftige kontinuierliche Überwachung

load_dotenv()

# Neu: Spezifischer API-Key für den Standort-Bot
TELEGRAM_LOCATION_BOT_API_KEY = os.environ.get("TELEGRAM_LOCATION_BOT_API_KEY") # Stelle sicher, dass dieser in deiner .env gesetzt ist
TELEGRAM_CHAT_ID = "610574272" # Diese Chat-ID wird zum Senden der Benachrichtigungsnachricht verwendet

# Definiere die Koordinaten deines Büros
OFFICE_LATITUDE = 23.135368
OFFICE_LONGITUDE = 113.32952

# Nähe-Radius in Metern
PROXIMITY_RADIUS_METERS = 300

def send_telegram_message(bot_token, chat_id, message):
    """Sendet eine Nachricht an einen Telegram-Chat unter Verwendung der Telegram-Bot-API."""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown" # Markdown für fett gedruckten Text in der Nachricht verwenden
    }
    response = requests.post(url, params=params)
    if response.status_code != 200:
        print(f"Fehler beim Senden der Telegram-Nachricht: {response.status_code} - {response.text}")

def get_latest_location(bot_token):
    """Ruft die neueste Live-Standortaktualisierung vom Bot ab."""
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    # Offset, um nur neue Aktualisierungen nach der letzten verarbeiteten zu erhalten (für kontinuierliches Polling)
    # Für ein einfaches Einmal-Skript holen wir einfach das neueste, aber für Polling würdest du einen Offset verwalten.
    params = {"offset": -1} # Hole die allerletzte Aktualisierung
    response = requests.get(url, params=params)
    print("GetUpdates Response:", response) # Debugging
    if response.status_code == 200:
        updates = response.json()
        print("GetUpdates JSON:", json.dumps(updates, indent=4)) # Debugging
        if updates['result']:
            last_update = updates['result'][-1]
            # Priorisiere edited_message für Live-Standorte
            if 'edited_message' in last_update and 'location' in last_update['edited_message']:
                return last_update['edited_message']['location'], last_update['edited_message']['chat']['id']
            elif 'message' in last_update and 'location' in last_update['message']:
                # Behandle anfängliche Live-Standortnachrichten oder statische Standortfreigaben
                return last_update['message']['location'], last_update['message']['chat']['id']
    return None, None

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Berechnet die Entfernung zwischen zwei Punkten auf der Erde mit der Haversine-Formel.
    Gibt die Entfernung in Metern zurück.
    """
    R = 6371000  # Radius der Erde in Metern

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
    parser = argparse.ArgumentParser(description="Telegram-Bot-Skript")
    # Aktualisierte Optionen für das --job-Argument
    parser.add_argument('--job', choices=['get_chat_id', 'send_message', 'check_location', 'start_sharing_message', 'stop_sharing_message'], required=True, help="Aufgabe, die ausgeführt werden soll")
    # Hinzugefügtes --message-Argument für die 'send_message'-Aufgabe
    parser.add_argument('--message', type=str, help="Nachricht zum Senden für die 'send_message'-Aufgabe")
    # Hinzugefügtes --test-Argument für die 'check_location'-Aufgabe
    parser.add_argument('--test', action='store_true', help="Für die 'check_location'-Aufgabe, eine Nachricht senden, unabhängig von der Nähe.")
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
                    print(f"Chat-ID: {chat_id}")
                else:
                    print("Chat-ID konnte nicht aus der letzten Aktualisierung abgerufen werden.")
            else:
                print("Keine Aktualisierungen gefunden.")
        else:
            print(f"Fehler beim Abrufen von Aktualisierungen: {response.status_code} - {response.text}")

    elif args.job == 'send_message':
        if TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = args.message if args.message else "Dies ist eine Standard-Testnachricht von deinem Telegram-Bot-Skript!"
            send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print(f"Nachricht erfolgreich gesendet: {message}")
        else:
            print("TELEGRAM_LOCATION_BOT_API_KEY und TELEGRAM_CHAT_ID sind nicht gesetzt.")

    elif args.job == 'start_sharing_message':
        if TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = "⚠️ *Erinnerung:* Bitte beginne damit, deinen Live-Standort mit dem Bot zu teilen!"
            send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print("Erinnerung zum Starten der Freigabe gesendet.")
        else:
            print("TELEGRAM_LOCATION_BOT_API_KEY und TELEGRAM_CHAT_ID sind nicht gesetzt.")

    elif args.job == 'stop_sharing_message':
        if TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = "✅ *Erinnerung:* Du kannst jetzt aufhören, deinen Live-Standort zu teilen."
            send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print("Erinnerung zum Stoppen der Freigabe gesendet.")
        else:
            print("TELEGRAM_LOCATION_BOT_API_KEY und TELEGRAM_CHAT_ID sind nicht gesetzt.")

    elif args.job == 'check_location':
        if not TELEGRAM_LOCATION_BOT_API_KEY or not TELEGRAM_CHAT_ID:
            print("TELEGRAM_LOCATION_BOT_API_KEY und TELEGRAM_CHAT_ID müssen für Standortprüfungen gesetzt sein.")
            return

        user_location, location_chat_id = get_latest_location(TELEGRAM_LOCATION_BOT_API_KEY)

        if user_location:
            current_latitude = user_location['latitude']
            current_longitude = user_location['longitude']

            distance = haversine_distance(
                OFFICE_LATITUDE, OFFICE_LONGITUDE,
                current_latitude, current_longitude
            )

            print(f"Aktueller Standort: ({current_latitude}, {current_longitude})")
            print(f"Entfernung zum Büro: {distance:.2f} Meter")

            needs_punch_card = distance <= PROXIMITY_RADIUS_METERS

            if needs_punch_card:
                print(f"Du bist innerhalb von {PROXIMITY_RADIUS_METERS}m des Büros!")
                notification_message = (
                    f"🎉 *Büro angekommen!* 🎉\n"
                    f"Zeit, in WeCom die Karte zu stempeln.\n"
                    f"Deine aktuelle Entfernung zum Büro: {distance:.2f}m."
                )
            else:
                print(f"Du bist außerhalb des {PROXIMITY_RADIUS_METERS}m-Büro-Kreises.")
                # Nachricht, wenn außerhalb des Radius
                notification_message = (
                    f"📍 Du bist *außerhalb* der Büro-Nähe ({PROXIMITY_RADIUS_METERS}m).\n"
                    f"Kein Stempeln der Karte erforderlich.\n"
                    f"Deine aktuelle Entfernung zum Büro: {distance:.2f}m."
                )

            # Nachricht senden, wenn innerhalb der Nähe ODER wenn die --test-Flag verwendet wird
            if needs_punch_card or args.test:
                send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, notification_message)
            else:
                # Wenn nicht innerhalb der Nähe UND nicht im Testmodus, nur in die Konsole drucken (keine Telegram-Nachricht)
                print("Nicht innerhalb der Nähe und nicht im Testmodus, keine Nachricht an Telegram gesendet.")
        else:
            print("Aktueller Standort konnte nicht abgerufen werden. Stelle sicher, dass du deinen Live-Standort mit dem Bot teilst.")

if __name__ == '__main__':
    main()
```

---

Aktualisierung: Das ist nicht gut, weil du deinen Live-Standort mit dem Bot teilen musst.