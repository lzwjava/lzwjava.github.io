---
audio: false
generated: false
lang: fr
layout: post
title: Automatiser votre carte perforée avec un bot de localisation Telegram
translated: true
---

Vous avez déjà souhaité que votre "carte de pointage" quotidienne soit moins une corvée ? Moi, oui. C'est pourquoi j'ai créé un bot Telegram personnel qui utilise le suivi de localisation pour automatiser les notifications d'arrivée au bureau et me rappeler les vérifications cruciales. Cet article explique comment j'ai combiné Python avec GitHub Actions pour créer un système sans effort, me tenant informé au bon moment, tout en se basant sur ma localisation.

```yml
name: Vérification horaire de la localisation

on:
  schedule:
    # Exécuter chaque heure, à l'heure pile, entre 11h et 23h, les jours ouvrables (lundi-vendredi)
    # L'heure est en UTC. L'heure de Singapour (SGT) est UTC+8.
    # Donc, 11h SGT est 03:00 UTC, et 23h SGT est 15:00 UTC.
    # Par conséquent, nous devons planifier de 03:00 à 15:00 UTC.
    - cron: '0 3-15 * * 1-5'

    # Rappel pour COMMENCER à partager la localisation en direct : mercredi 11h SGT (3h UTC)
    # Heure actuelle : dimanche 8 juin 2025 à 17:10:58 +08 (SGT)
    # Pour mercredi 11h SGT (UTC+8) : 11 - 8 = 3h UTC.
    - cron: '0 3 * * 3' # 3 pour mercredi

    # Rappel pour ARRÊTER de partager la localisation en direct : vendredi 23h SGT (15h UTC)
    # Heure actuelle : dimanche 8 juin 2025 à 17:10:58 +08 (SGT)
    # Pour vendredi 23h SGT (UTC+8) : 23 - 8 = 15h UTC.
    - cron: '0 15 * * 5' # 5 pour vendredi

  workflow_dispatch:  # Permet le déclenchement manuel du workflow
  push:
    branches: ["main"]
    paths:
      - 'scripts/release/location_bot.py' # Chemin corrigé vers votre script
      - '.github/workflows/location.yml' # Chemin vers ce fichier de workflow

concurrency:
  group: 'location'
  cancel-in-progress: false

jobs:
  check_and_notify:
    runs-on: ubuntu-latest
    env:
      TELEGRAM_LOCATION_BOT_API_KEY: ${{ secrets.TELEGRAM_LOCATION_BOT_API_KEY }}

    steps:
    - name: Checkout du dépôt
      uses: actions/checkout@v4
      with:
        fetch-depth: 5 # Récupérer uniquement les 5 derniers commits pour l'efficacité

    - name: Configuration de Python 3.13.2
      uses: actions/setup-python@v4
      with:
        python-version: "3.13.2" # Spécifier la version exacte de Python

    - name: Installation des dépendances
      run: |
        python -m pip install --upgrade pip
        # En supposant que vous avez un fichier requirements.simple.txt à la racine de votre dépôt.
        # Sinon, utilisez : pip install requests python-dotenv
        pip install -r requirements.simple.txt

    - name: Exécution du script de vérification de localisation (Planifié)
      run: python scripts/release/location_bot.py --job check_location
      # Cette étape s'exécutera lors des déclenchements planifiés pour la vérification horaire
      if: github.event.schedule == '0 3-15 * * 1-5' # Correspond au planning cron horaire

    - name: Rappel pour COMMENCER à partager la localisation en direct
      run: python scripts/release/location_bot.py --job start_sharing_message
      if: github.event.schedule == '0 3 * * 3' # Correspond au cron mercredi 11h SGT

    - name: Rappel pour ARRÊTER de partager la localisation en direct
      run: python scripts/release/location_bot.py --job stop_sharing_message
      if: github.event.schedule == '0 15 * * 5' # Correspond au cron vendredi 23h SGT

    - name: Exécution du script Telegram pour un message de test (Déclenchement manuel)
      run: python scripts/release/location_bot.py --job send_message --message "Ceci est un message de test de déclenchement manuel depuis GitHub Actions."
      if: github.event_name == 'workflow_dispatch'

    - name: Exécution du script Telegram pour une poussée vers la branche principale
      run: python scripts/release/location_bot.py --job send_message --message "Modifications de code pour le bot de localisation poussées vers la branche principale."
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
import time # Pour une surveillance continue potentielle

load_dotenv()

# Nouveau : Clé API spécifique pour le bot de localisation
TELEGRAM_LOCATION_BOT_API_KEY = os.environ.get("TELEGRAM_LOCATION_BOT_API_KEY") # Assurez-vous que ceci est défini dans votre .env
TELEGRAM_CHAT_ID = "610574272" # Cet ID de chat est pour envoyer le message de notification

# Définir les coordonnées de votre bureau
OFFICE_LATITUDE = 23.135368
OFFICE_LONGITUDE = 113.32952

# Rayon de proximité en mètres
PROXIMITY_RADIUS_METERS = 300

def send_telegram_message(bot_token, chat_id, message):
    """Envoie un message à un chat Telegram en utilisant l'API Telegram Bot."""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown" # Utilisation de Markdown pour le texte en gras dans le message
    }
    response = requests.post(url, params=params)
    if response.status_code != 200:
        print(f"Erreur lors de l'envoi du message Telegram : {response.status_code} - {response.text}")

def get_latest_location(bot_token):
    """Récupère la dernière mise à jour de localisation en direct du bot."""
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    # Offset pour obtenir uniquement les nouvelles mises à jour après la dernière traitée (pour la surveillance continue)
    # Pour un script simple en une seule exécution, nous allons simplement obtenir le dernier, mais pour la surveillance, vous géreriez un offset.
    params = {"offset": -1} # Obtenir la toute dernière mise à jour
    response = requests.get(url, params=params)
    print("Réponse GetUpdates:", response) # Debugging
    if response.status_code == 200:
        updates = response.json()
        print("JSON GetUpdates:", json.dumps(updates, indent=4)) # Debugging
        if updates['result']:
            last_update = updates['result'][-1]
            # Prioriser edited_message pour les localisations en direct
            if 'edited_message' in last_update and 'location' in last_update['edited_message']:
                return last_update['edited_message']['location'], last_update['edited_message']['chat']['id']
            elif 'message' in last_update and 'location' in last_update['message']:
                # Gérer les messages de localisation en direct initiaux ou les partages de localisation statiques
                return last_update['message']['location'], last_update['message']['chat']['id']
    return None, None

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calcule la distance entre deux points sur Terre en utilisant la formule de Haversine.
    Retourne la distance en mètres.
    """
    R = 6371000  # Rayon de la Terre en mètres

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
    parser = argparse.ArgumentParser(description="Script du Bot Telegram")
    # Choix mis à jour pour l'argument --job
    parser.add_argument('--job', choices=['get_chat_id', 'send_message', 'check_location', 'start_sharing_message', 'stop_sharing_message'], required=True, help="Tâche à effectuer")
    # Ajout de l'argument --message pour la tâche 'send_message'
    parser.add_argument('--message', type=str, help="Message à envoyer pour la tâche 'send_message'")
    # Ajout de l'argument --test pour la tâche 'check_location'
    parser.add_argument('--test', action='store_true', help="Pour la tâche 'check_location', forcer l'envoi d'un message indépendamment de la proximité.")
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
                    print(f"Chat ID: {chat_id}")
                else:
                    print("Impossible de récupérer l'ID de chat à partir de la dernière mise à jour.")
            else:
                print("Aucune mise à jour trouvée.")
        else:
            print(f"Erreur lors de la récupération des mises à jour : {response.status_code} - {response.text}")

    elif args.job == 'send_message':
        if TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = args.message if args.message else "Ceci est un message de test par défaut de votre script de bot Telegram !"
            send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print(f"Message envoyé avec succès : {message}")
        else:
            print("TELEGRAM_LOCATION_BOT_API_KEY et TELEGRAM_CHAT_ID ne sont pas définis.")

    elif args.job == 'start_sharing_message':
        if TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = "⚠️ *Rappel:* Veuillez commencer à partager votre localisation en direct avec le bot !"
            send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print("Rappel de partage envoyé.")
        else:
            print("TELEGRAM_LOCATION_BOT_API_KEY et TELEGRAM_CHAT_ID ne sont pas définis.")

    elif args.job == 'stop_sharing_message':
        if TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = "✅ *Rappel:* Vous pouvez maintenant arrêter de partager votre localisation en direct."
            send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print("Rappel d'arrêt de partage envoyé.")
        else:
            print("TELEGRAM_LOCATION_BOT_API_KEY et TELEGRAM_CHAT_ID ne sont pas définis.")

    elif args.job == 'check_location':
        if not TELEGRAM_LOCATION_BOT_API_KEY or not TELEGRAM_CHAT_ID:
            print("TELEGRAM_LOCATION_BOT_API_KEY et TELEGRAM_CHAT_ID doivent être définis pour les vérifications de localisation.")
            return

        user_location, location_chat_id = get_latest_location(TELEGRAM_LOCATION_BOT_API_KEY)

        if user_location:
            current_latitude = user_location['latitude']
            current_longitude = user_location['longitude']

            distance = haversine_distance(
                OFFICE_LATITUDE, OFFICE_LONGITUDE,
                current_latitude, current_longitude
            )

            print(f"Localisation actuelle : ({current_latitude}, {current_longitude})")
            print(f"Distance par rapport au bureau : {distance:.2f} mètres")

            needs_punch_card = distance <= PROXIMITY_RADIUS_METERS

            if needs_punch_card:
                print(f"Vous êtes à moins de {PROXIMITY_RADIUS_METERS}m du bureau !")
                notification_message = (
                    f"🎉 *Arrivée au bureau !* 🎉\n"
                    f"Il est temps de pointer dans WeCom.\n"
                    f"Votre distance actuelle par rapport au bureau : {distance:.2f}m."
                )
            else:
                print(f"Vous êtes en dehors du cercle de {PROXIMITY_RADIUS_METERS}m du bureau.")
                # Message pour quand vous êtes en dehors du rayon
                notification_message = (
                    f"📍 Vous êtes *en dehors* de la proximité du bureau ({PROXIMITY_RADIUS_METERS}m).\n"
                    f"Aucun pointage nécessaire pour le moment.\n"
                    f"Votre distance actuelle par rapport au bureau : {distance:.2f}m."
                )

            # Envoyer le message si vous êtes à proximité OU si le drapeau --test est utilisé
            if needs_punch_card or args.test:
                send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, notification_message)
            else:
                # Si vous n'êtes pas à proximité ET pas en mode test, simplement afficher à la console (aucun message Telegram)
                print("Pas à proximité et pas en mode test, aucun message envoyé à Telegram.")
        else:
            print("Impossible de récupérer votre dernière localisation. Assurez-vous de partager votre localisation en direct avec le bot.")

if __name__ == '__main__':
    main()
```

---

Mise à jour : Ce n'est pas bon car vous devez partager votre localisation en direct avec le bot.