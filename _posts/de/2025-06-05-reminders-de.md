---
audio: true
generated: false
lang: de
layout: post
title: Automatisierung von Erinnerungen mit GitHub Actions und Telegram
translated: true
---

In diesem Projekt habe ich ein automatisiertes Erinnerungssystem mit GitHub Actions und einem Telegram-Bot eingerichtet, um meine täglichen und monatlichen Aufgaben im Blick zu behalten. Mithilfe von Cron-Zeitplänen habe ich Erinnerungen für arbeitsbezogene Aufgaben wie das Einchecken in WeCom, das Einreichen von Stundenzetteln und das Überprüfen von Gehältern konfiguriert, sowie für persönliche Aufgaben wie den Besuch bei der Familie, Einkäufe auf JD.com und sogar das Fernsehen mit meinem Partner. Das System verwendet ein Python-Skript, um Nachrichten über die Telegram-Bot-API zu senden, wobei Umgebungsvariablen sicher in GitHub Secrets gespeichert sind. Dieser Aufbau stellt sicher, dass ich keine kritischen Fristen oder persönlichen Verpflichtungen verpasse und verbindet Technologie mit dem Alltag für maximale Effizienz.

```yaml
name: Erinnerungen

on:
  schedule:
    # Läuft alle 2 Stunden von 12 Uhr bis 20 Uhr (Peking-Zeit, UTC+8) von Mittwoch bis Freitag.
    - cron: '0 4,6,8,10,12 * * 3-5'
    # Läuft am 27. jedes Monats um 12 Uhr (Peking-Zeit, UTC+8).
    - cron: '0 4 27 * *'
    # Läuft am 30. jedes Monats um 14 Uhr (Peking-Zeit, UTC+8).
    - cron: '0 6 30 * *'
    # Läuft täglich um 1 Uhr Peking-Zeit (17 Uhr UTC am Vortag).
    - cron: '0 17 * * *'
    # Läuft täglich um 11 Uhr Peking-Zeit (3 Uhr UTC).
    - cron: '0 3 * * *'
    # Erinnert daran, am nächsten Tag zu den Eltern zu gehen: 21 Uhr Peking-Zeit (13 Uhr UTC) an Di, Mi, Do.
    - cron: '0 13 * * 2-4'
    # Erinnert daran, am nächsten Tag nach Hause zu gehen: 21 Uhr Peking-Zeit (13 Uhr UTC) an So, Mo, Fr, Sa.
    - cron: '0 13 * * 0,1,5,6'
    # Erinnert daran, frische Produkte direkt bei JD.com zu kaufen: 21 Uhr Peking-Zeit (13 Uhr UTC) am Mittwoch.
    - cron: '0 13 * * 3'
    # Erinnert daran, Schnelllieferessen von JD.com zu kaufen: 21 Uhr Peking-Zeit (13 Uhr UTC) am Freitag.
    - cron: '0 13 * * 5'
    # Erinnert an die Associate-Degree-Prüfung im März, April, September und Oktober jeden Montag um 13 Uhr Peking-Zeit (5 Uhr UTC).
    - cron: '0 5 * 3,4,9,10 1'
    # Erinnert daran, den Clarity-Stundenzettel jeden Freitag um 17 Uhr Taipeh-Zeit (9 Uhr UTC) einzureichen.
    - cron: '0 9 * * 5'
    # Erinnert daran, den Lieferanten-Stundenzettel am 25. jedes Monats um 0 Uhr Taipeh-Zeit (16 Uhr UTC am Vortag) einzureichen.
    - cron: '0 16 25 * *'
    # Erinnert daran, die Familie um Unterstützung bei der Hypothekenzahlung am 16. jedes Monats um 21 Uhr Taipeh-Zeit (13 Uhr UTC) zu bitten.
    - cron: '0 13 16 * *'
    # Erinnert daran, jeden Freitag, Samstag und Sonntag um 22 Uhr Taipeh-Zeit (14 Uhr UTC) mit dem Partner fernzusehen.
    - cron: '0 14 * * 5,6,0'
    # Erinnert daran, den Parkausweis-Aufkleber um 2 Uhr Peking-Zeit (18 Uhr UTC) an Mi, Do, Fr zu entfernen.
    - cron: '0 18 * * 3,4,5'
  workflow_dispatch:  # Ermöglicht manuelle Auslösung

concurrency:
  group: 'erinnerungen'
  cancel-in-progress: false

jobs:
  send-reminders:
    runs-on: ubuntu-latest
    environment: github-pages
    env:
      TELEGRAM_BOT2_API_KEY: ${{ secrets.TELEGRAM_BOT2_API_KEY }}

    steps:
      - name: Repository auschecken
        uses: actions/checkout@v4
        with:
          fetch-depth: 5

      - name: Python 3.10.x einrichten
        uses: actions/setup-python@v4
        with:
          python-version: "3.10.x"

      - name: Abhängigkeiten installieren
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.simple.txt

      - name: Telegram-Skript für tägliche Eincheck-Erinnerungen ausführen
        run: python scripts/release/reminders_bot.py --job send_message --message "In WeCom einchecken"
        if: github.event.schedule == '0 4,6,8,10,12 * * 3-5'

      - name: Telegram-Skript für monatliche Hypotheken-Erinnerung ausführen
        run: python scripts/release/reminders_bot.py --job send_message --message "Hypothekenabzug vorbereiten"
        if: github.event.schedule == '0 4 27 * *'

      - name: Telegram-Skript für monatliche Gehaltsüberprüfung ausführen
        run: python scripts/release/reminders_bot.py --job send_message --message "Gehalt überprüfen"
        if: github.event.schedule == '0 6 30 * *'

      - name: Telegram-Skript für Schlaf-Erinnerung ausführen
        run: python scripts/release/reminders_bot.py --job send_message --message "Zeit zum Schlafen!"
        if: github.event.schedule == '0 17 * * *'

      - name: Telegram-Skript für Aufsteh-Erinnerung ausführen
        run: python scripts/release/reminders_bot.py --job send_message --message "Zeit zum Aufstehen!"
        if: github.event.schedule == '0 3 * * *'

      - name: Telegram-Skript für Elternhaus-Erinnerung ausführen
        run: python scripts/release/reminders_bot.py --job send_message --message "Gehe morgen zu den Eltern!"
        if: github.event.schedule == '0 13 * * 2-4'

      - name: Telegram-Skript für eigenes Haus-Erinnerung ausführen
        run: python scripts/release/reminders_bot.py --job send_message --message "Gehe morgen nach Hause!"
        if: github.event.schedule == '0 13 * * 0,1,5,6'

      - name: Telegram-Skript für JD.com-Frischprodukte-Erinnerung ausführen
        run: python scripts/release/reminders_bot.py --job send_message --message "Kaufe frische Produkte direkt bei JD.com!"
        if: github.event.schedule == '0 13 * * 3'

      - name: Telegram-Skript für JD.com-Schnelllieferessen-Erinnerung ausführen
        run: python scripts/release/reminders_bot.py --job send_message --message "Kaufe Schnelllieferessen von JD.com!"
        if: github.event.schedule == '0 13 * * 5'

      - name: Telegram-Skript für Associate-Degree-Prüfungs-Erinnerung ausführen
        run: python scripts/release/reminders_bot.py --job send_message --message "Melde dich für die Associate-Degree-Prüfung an"
        if: github.event.schedule == '0 5 * 3,4,9,10 1'

      - name: Telegram-Skript für Clarity-Stundenzettel-Erinnerung ausführen
        run: python scripts/release/reminders_bot.py --job send_message --message "Reiche den Clarity-Stundenzettel ein"
        if: github.event.schedule == '0 9 * * 5'

      - name: Telegram-Skript für Lieferanten-Stundenzettel-Erinnerung ausführen
        run: python scripts/release/reminders_bot.py --job send_message --message "Reiche den Lieferanten-Stundenzettel ein"
        if: github.event.schedule == '0 16 25 * *'

      - name: Telegram-Skript für Hypotheken-Unterstützungs-Erinnerung ausführen
        run: python scripts/release/reminders_bot.py --job send_message --message "Bitte die Familie um Unterstützung bei der Hypothekenzahlung"
        if: github.event.schedule == '0 13 16 * *'

      - name: Telegram-Skript für TV-Erinnerung mit Partner ausführen
        run: python scripts/release/reminders_bot.py --job send_message --message "Zeit, mit deinem Partner fernzusehen!"
        if: github.event.schedule == '0 14 * * 5,6,0'

      - name: Telegram-Skript für Parkausweis-Aufkleber-Erinnerung ausführen
        run: python scripts/release/reminders_bot.py --job send_message --message "Entferne den Parkausweis-Aufkleber vom Autofenster"
        if: github.event.schedule == '0 18 * * 3,4,5'

      - name: Telegram-Skript für Testnachricht ausführen
        run: python scripts/release/reminders_bot.py --job send_message --message "Dies ist eine Testnachricht von GitHub Actions."
        if: github.event_name == 'workflow_dispatch'
```

```python
import os
import requests
from dotenv import load_dotenv
import json
import argparse

load_dotenv()

TELEGRAM_BOT2_API_KEY = os.environ.get("TELEGRAM_BOT2_API_KEY")
TELEGRAM_CHAT_ID = "610574272"

def send_telegram_message(bot_token, chat_id, message):
    """Sendet eine Nachricht an einen Telegram-Chat über die Telegram-Bot-API."""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, params=params)
    if response.status_code != 200:
        print(f"Fehler beim Senden der Telegram-Nachricht: {response.status_code} - {response.text}")

def get_chat_id(bot_token):
    """Ermittelt die Chat-ID der letzten an den Bot gesendeten Nachricht."""
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    response = requests.get(url)
    if response.status_code == 200:
        updates = response.json()
        print(json.dumps(updates, indent=4))
        if updates['result']:
            chat_id = updates['result'][-1]['message']['chat']['id']
            return chat_id
    return None

def send_reminder(message):
    """Sendet eine Erinnerungsnachricht an Telegram."""
    if TELEGRAM_BOT2_API_KEY and TELEGRAM_CHAT_ID:
        send_telegram_message(TELEGRAM_BOT2_API_KEY, TELEGRAM_CHAT_ID, f"Erinnerung: {message}")
    else:
        print("TELEGRAM_BOT2_API_KEY und TELEGRAM_CHAT_ID sind nicht gesetzt.")

def main():
    parser = argparse.ArgumentParser(description="Telegram-Bot-Skript")
    parser.add_argument('--job', choices=['get_chat_id', 'send_message'], required=True, help="Ausführender Job")
    parser.add_argument('--message', help="Benutzerdefinierte Nachricht zum Senden", default=None)
    args = parser.parse_args()

    if args.job == 'get_chat_id':
        bot_token = TELEGRAM_BOT2_API_KEY
        chat_id = get_chat_id(bot_token)
        if chat_id:
            print(f"Chat-ID: {chat_id}")
        else:
            print("Chat-ID konnte nicht ermittelt werden.")

    elif args.job == 'send_message':
        if args.message:
            send_reminder(args.message)
        else:
            print("Keine Nachricht für den send_message-Job angegeben.")
            
if __name__ == '__main__':
    main()
```