---
audio: false
generated: false
lang: fr
layout: post
title: Automatiser votre carte perforée avec un bot de localisation Telegram
translated: true
---

Vous en avez assez de votre "fiche de pointage" quotidienne ? Moi aussi. C'est pourquoi j'ai créé un bot Telegram personnel qui utilise le suivi de localisation pour automatiser les notifications d'arrivée au bureau et me rappeler ces enregistrements cruciaux. Ce post explique comment j'ai combiné Python avec GitHub Actions pour créer un système fluide et sans intervention, me tenant informé exactement quand j'en ai besoin, en fonction de ma localisation.

```yml
name: Vérification horaire de localisation

on:
  schedule:
    # Exécution toutes les heures, à l'heure pile, entre 11h et 23h, en semaine (lundi-vendredi)
    # L'heure est en UTC. L'heure de Singapour (SGT) est UTC+8.
    # Ainsi, 11h SGT correspond à 03:00 UTC, et 23h SGT à 15:00 UTC.
    # Par conséquent, nous planifions de 03:00 à 15:00 UTC.
    - cron: '0 3-15 * * 1-5'

    # Rappel pour COMMENCER le partage de localisation en direct : mercredi 11h SGT (3h UTC)
    # Heure actuelle : dimanche 8 juin 2025 à 17:10:58 +08 (SGT)
    # Pour mercredi 11h SGT (UTC+8) : 11 - 8 = 3h UTC.
    - cron: '0 3 * * 3' # 3 pour mercredi

    # Rappel pour ARRÊTER le partage de localisation en direct : vendredi 23h SGT (15h UTC)
    # Heure actuelle : dimanche 8 juin 2025 à 17:10:58 +08 (SGT)
    # Pour vendredi 23h SGT (UTC+8) : 23 - 8 = 15h UTC.
    - cron: '0 15 * * 5' # 5 pour vendredi

  workflow_dispatch:  # Permet un déclenchement manuel du workflow
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
    - name: Vérifier le dépôt
      uses: actions/checkout@v4
      with:
        fetch-depth: 5 # Récupère seulement les 5 derniers commits pour l'efficacité

    - name: Configurer Python 3.13.2
      uses: actions/setup-python@v4
      with:
        python-version: "3.13.2" # Version exacte de Python

    - name: Installer les dépendances
      run: |
        python -m pip install --upgrade pip
        # Supposons que vous avez un requirements.simple.txt à la racine de votre dépôt.
        # Sinon, utilisez : pip install requests python-dotenv
        pip install -r requirements.simple.txt 

    - name: Exécuter le script de vérification de localisation (Planifié)
      run: python scripts/release/location_bot.py --job check_location
      # Cette étape s'exécute lors des déclenchements planifiés pour la vérification horaire
      if: github.event.schedule == '0 3-15 * * 1-5' # Correspond à la planification cron horaire

    - name: Rappel pour COMMENCER le partage de localisation
      run: python scripts/release/location_bot.py --job start_sharing_message
      if: github.event.schedule == '0 3 * * 3' # Correspond au cron mercredi 11h SGT

    - name: Rappel pour ARRÊTER le partage de localisation
      run: python scripts/release/location_bot.py --job stop_sharing_message
      if: github.event.schedule == '0 15 * * 5' # Correspond au cron vendredi 23h SGT

    - name: Exécuter le script Telegram pour un message de test (Déclenchement manuel)
      run: python scripts/release/location_bot.py --job send_message --message "Ceci est un message de test manuel depuis GitHub Actions."
      if: github.event_name == 'workflow_dispatch'

    - name: Exécuter le script Telegram pour un push sur la branche main
      run: python scripts/release/location_bot.py --job send_message --message "Modifications du code pour le bot de localisation poussées sur la branche main."
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
import time # Pour un éventuel suivi continu

load_dotenv()

# Nouveau : Clé API spécifique pour le bot de localisation
TELEGRAM_LOCATION_BOT_API_KEY = os.environ.get("TELEGRAM_LOCATION_BOT_API_KEY") # Assurez-vous que ceci est défini dans votre .env
TELEGRAM_CHAT_ID = "610574272" # Cet ID de chat est pour envoyer le message de notification

# Définissez les coordonnées de votre bureau
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
    # Offset pour obtenir seulement les nouvelles mises à jour après la dernière traitée (pour un sondage continu)
    # Pour un script simple exécuté une fois, nous prenons simplement la dernière, mais pour un sondage, vous géreriez un offset.
    params = {"offset": -1} # Obtenir la toute dernière mise à jour
    response = requests.get(url, params=params)
    print("Réponse GetUpdates :", response) # Débogage
    if response.status_code == 200:
        updates = response.json()
        print("JSON GetUpdates :", json.dumps(updates, indent=4)) # Débogage
        if updates['result']:
            last_update = updates['result'][-1]
            # Priorité à edited_message pour les localisations en direct
            if 'edited_message' in last_update and 'location' in last_update['edited_message']:
                return last_update['edited_message']['location'], last_update['edited_message']['chat']['id']
            elif 'message' in last_update and 'location' in last_update['message']:
                # Gère les messages initiaux de localisation en direct ou les partages statiques
                return last_update['message']['location'], last_update['message']['chat']['id']
    return None, None

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calcule la distance entre deux points sur Terre en utilisant la formule haversine.
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
    parser = argparse.ArgumentParser(description="Script de bot Telegram")
    # Choix mis à jour pour l'argument --job
    parser.add_argument('--job', choices=['get_chat_id', 'send_message', 'check_location', 'start_sharing_message', 'stop_sharing_message'], required=True, help="Tâche à effectuer")
    # Ajout de l'argument --message pour la tâche 'send_message'
    parser.add_argument('--message', type=str, help="Message à envoyer pour la tâche 'send_message'")
    # Ajout de l'argument --test pour la tâche 'check_location'
    parser.add_argument('--test', action='store_true', help="Pour la tâche 'check_location', force l'envoi d'un message indépendamment de la proximité.")
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
                    print(f"ID de chat : {chat_id}")
                else:
                    print("Impossible de récupérer l'ID de chat depuis la dernière mise à jour.")
            else:
                print("Aucune mise à jour trouvée.")
        else:
            print(f"Erreur lors de la récupération des mises à jour : {response.status_code} - {response.text}")

    elif args.job == 'send_message':
        if TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = args.message if args.message else "Ceci est un message de test par défaut depuis votre script de bot Telegram !"
            send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print(f"Message envoyé avec succès : {message}")
        else:
            print("TELEGRAM_LOCATION_BOT_API_KEY et TELEGRAM_CHAT_ID ne sont pas définis.")

    elif args.job == 'start_sharing_message':
        if TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = "⚠️ *Rappel :* Veuillez commencer à partager votre localisation en direct avec le bot !"
            send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print("Rappel de partage envoyé.")
        else:
            print("TELEGRAM_LOCATION_BOT_API_KEY et TELEGRAM_CHAT_ID ne sont pas définis.")

    elif args.job == 'stop_sharing_message':
        if TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = "✅ *Rappel :* Vous pouvez arrêter de partager votre localisation en direct maintenant."
            send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print("Rappel d'arrêt envoyé.")
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
            print(f"Distance du bureau : {distance:.2f} mètres")

            needs_punch_card = distance <= PROXIMITY_RADIUS_METERS

            if needs_punch_card:
                print(f"Vous êtes à moins de {PROXIMITY_RADIUS_METERS}m du bureau !")
                notification_message = (
                    f"🎉 *Arrivé au bureau !* 🎉\n"
                    f"Il est temps de pointer dans WeCom.\n"
                    f"Votre distance actuelle du bureau : {distance:.2f}m."
                )
            else:
                print(f"Vous êtes en dehors du cercle de {PROXIMITY_RADIUS_METERS}m du bureau.")
                # Message pour quand vous êtes en dehors du rayon
                notification_message = (
                    f"📍 Vous êtes *en dehors* de la proximité du bureau ({PROXIMITY_RADIUS_METERS}m).\n"
                    f"Aucun pointage nécessaire pour le moment.\n"
                    f"Votre distance actuelle du bureau : {distance:.2f}m."
                )

            # Envoyer un message si dans la proximité OU si l'option --test est utilisée
            if needs_punch_card or args.test:
                send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, notification_message)
            else:
                # Si pas dans la proximité ET pas en mode test, juste imprimer dans la console (pas de message Telegram)
                print("Pas dans la proximité et pas en mode test, aucun message envoyé à Telegram.")
        else:
            print("Impossible de récupérer votre dernière localisation. Assurez-vous de partager votre localisation en direct avec le bot.")

if __name__ == '__main__':
    main()
```