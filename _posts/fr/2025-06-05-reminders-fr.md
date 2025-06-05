---
audio: false
generated: false
lang: fr
layout: post
title: Rationalisation des rappels avec GitHub Actions et Telegram
translated: true
---

Dans ce projet, j'ai mis en place un système de rappels automatisé utilisant GitHub Actions et un bot Telegram pour suivre mes tâches quotidiennes et mensuelles. En exploitant des planifications cron, j'ai configuré des rappels pour des tâches professionnelles comme pointer sur WeCom, soumettre des feuilles de temps et vérifier les salaires, ainsi que des tâches personnelles comme rendre visite à ma famille, faire des achats sur JD.com, et même regarder la télévision avec ma partenaire. Le système utilise un script Python pour envoyer des messages via l'API Bot de Telegram, avec des variables d'environnement stockées de manière sécurisée dans GitHub Secrets. Cette configuration garantit que je ne manque jamais des échéances critiques ou des engagements personnels, combinant technologie et vie quotidienne pour une efficacité maximale.

```yaml
name: Rappels

on:
  schedule:
    # S'exécute toutes les 2 heures de 12h à 20h (heure de Pékin, UTC+8) du mercredi au vendredi.
    - cron: '0 4,6,8,10,12 * * 3-5'
    # S'exécute le 27 de chaque mois à 12h (heure de Pékin, UTC+8).
    - cron: '0 4 27 * *'
    # S'exécute le 30 de chaque mois à 14h (heure de Pékin, UTC+8).
    - cron: '0 6 30 * *'
    # S'exécute tous les jours à 1h du matin (heure de Pékin, 17h UTC la veille).
    - cron: '0 17 * * *'
    # S'exécute tous les jours à 11h (heure de Pékin, 3h UTC).
    - cron: '0 3 * * *'
    # Rappelle d'aller chez les parents le lendemain : 21h heure de Pékin (13h UTC) mardi, mercredi, jeudi.
    - cron: '0 13 * * 2-4'
    # Rappelle d'aller chez soi le lendemain : 21h heure de Pékin (13h UTC) dimanche, lundi, vendredi, samedi.
    - cron: '0 13 * * 0,1,5,6'
    # Rappelle d'acheter des produits frais directement sur JD.com : 21h heure de Pékin (13h UTC) mercredi.
    - cron: '0 13 * * 3'
    # Rappelle d'acheter de la nourriture en livraison rapide sur JD.com : 21h heure de Pékin (13h UTC) vendredi.
    - cron: '0 13 * * 5'
    # Rappelle l'examen de diplôme associé en mars, avril, septembre et octobre chaque lundi à 13h heure de Pékin (5h UTC).
    - cron: '0 5 * 3,4,9,10 1'
    # Rappelle de soumettre la feuille de temps Clarity chaque vendredi à 17h heure de Taipei (9h UTC).
    - cron: '0 9 * * 5'
    # Rappelle de soumettre la feuille de temps fournisseur le 25 de chaque mois à minuit heure de Taipei (16h UTC la veille).
    - cron: '0 16 25 * *'
    # Rappelle de demander à la famille de soutenir le paiement du prêt le 16 de chaque mois à 21h heure de Taipei (13h UTC).
    - cron: '0 13 16 * *'
    # Rappelle de regarder la télévision avec sa partenaire chaque vendredi, samedi et dimanche à 22h heure de Taipei (14h UTC).
    - cron: '0 14 * * 5,6,0'
    # Rappelle d'enlever l'autocollant de stationnement à 2h du matin (heure de Pékin, 18h UTC) mercredi, jeudi, vendredi.
    - cron: '0 18 * * 3,4,5'
  workflow_dispatch:  # Permet un déclenchement manuel

concurrency:
  group: 'rappels'
  cancel-in-progress: false

jobs:
  envoyer-rappels:
    runs-on: ubuntu-latest
    environment: github-pages
    env:
      TELEGRAM_BOT2_API_KEY: ${{ secrets.TELEGRAM_BOT2_API_KEY }}

    steps:
      - name: Vérifier le dépôt
        uses: actions/checkout@v4
        with:
          fetch-depth: 5

      - name: Configurer Python 3.10.x
        uses: actions/setup-python@v4
        with:
          python-version: "3.10.x"

      - name: Installer les dépendances
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.simple.txt

      - name: Exécuter le script Telegram pour les rappels de pointage quotidien
        run: python scripts/release/reminders_bot.py --job send_message --message "Pointer sur WeCom"
        if: github.event.schedule == '0 4,6,8,10,12 * * 3-5'

      - name: Exécuter le script Telegram pour le rappel mensuel de prêt immobilier
        run: python scripts/release/reminders_bot.py --job send_message --message "Préparer le prélèvement du prêt immobilier"
        if: github.event.schedule == '0 4 27 * *'

      - name: Exécuter le script Telegram pour le rappel mensuel de vérification de salaire
        run: python scripts/release/reminders_bot.py --job send_message --message "Vérifier le salaire"
        if: github.event.schedule == '0 6 30 * *'

      - name: Exécuter le script Telegram pour le rappel de sommeil
        run: python scripts/release/reminders_bot.py --job send_message --message "Il est temps de dormir !"
        if: github.event.schedule == '0 17 * * *'

      - name: Exécuter le script Telegram pour le rappel de réveil
        run: python scripts/release/reminders_bot.py --job send_message --message "Il est temps de se réveiller !"
        if: github.event.schedule == '0 3 * * *'

      - name: Exécuter le script Telegram pour le rappel chez les parents
        run: python scripts/release/reminders_bot.py --job send_message --message "Aller chez les parents demain !"
        if: github.event.schedule == '0 13 * * 2-4'

      - name: Exécuter le script Telegram pour le rappel chez soi
        run: python scripts/release/reminders_bot.py --job send_message --message "Aller chez toi demain !"
        if: github.event.schedule == '0 13 * * 0,1,5,6'

      - name: Exécuter le script Telegram pour le rappel d'achat de produits frais sur JD.com
        run: python scripts/release/reminders_bot.py --job send_message --message "Acheter des produits frais directement sur JD.com !"
        if: github.event.schedule == '0 13 * * 3'

      - name: Exécuter le script Telegram pour le rappel d'achat de nourriture en livraison rapide sur JD.com
        run: python scripts/release/reminders_bot.py --job send_message --message "Acheter de la nourriture en livraison rapide sur JD.com !"
        if: github.event.schedule == '0 13 * * 5'

      - name: Exécuter le script Telegram pour le rappel d'examen de diplôme associé
        run: python scripts/release/reminders_bot.py --job send_message --message "S'inscrire à l'examen de diplôme associé"
        if: github.event.schedule == '0 5 * 3,4,9,10 1'

      - name: Exécuter le script Telegram pour le rappel de feuille de temps Clarity
        run: python scripts/release/reminders_bot.py --job send_message --message "Soumettre la feuille de temps Clarity"
        if: github.event.schedule == '0 9 * * 5'

      - name: Exécuter le script Telegram pour le rappel de feuille de temps fournisseur
        run: python scripts/release/reminders_bot.py --job send_message --message "Soumettre la feuille de temps fournisseur"
        if: github.event.schedule == '0 16 25 * *'

      - name: Exécuter le script Telegram pour le rappel de soutien familial au prêt
        run: python scripts/release/reminders_bot.py --job send_message --message "Demander à la famille de soutenir le paiement du prêt"
        if: github.event.schedule == '0 13 16 * *'

      - name: Exécuter le script Telegram pour le rappel de regarder la télévision avec sa partenaire
        run: python scripts/release/reminders_bot.py --job send_message --message "Il est temps de regarder la télévision avec ta partenaire !"
        if: github.event.schedule == '0 14 * * 5,6,0'

      - name: Exécuter le script Telegram pour le rappel d'enlever l'autocollant de stationnement
        run: python scripts/release/reminders_bot.py --job send_message --message "Enlever l'autocollant de stationnement de la voiture"
        if: github.event.schedule == '0 18 * * 3,4,5'

      - name: Exécuter le script Telegram pour un message de test
        run: python scripts/release/reminders_bot.py --job send_message --message "Ceci est un message de test depuis GitHub Actions."
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
    """Envoie un message à un chat Telegram en utilisant l'API Bot de Telegram."""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, params=params)
    if response.status_code != 200:
        print(f"Erreur lors de l'envoi du message Telegram : {response.status_code} - {response.text}")

def get_chat_id(bot_token):
    """Récupère l'ID du chat du dernier message envoyé au bot."""
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
    """Envoie un message de rappel sur Telegram."""
    if TELEGRAM_BOT2_API_KEY and TELEGRAM_CHAT_ID:
        send_telegram_message(TELEGRAM_BOT2_API_KEY, TELEGRAM_CHAT_ID, f"Rappel : {message}")
    else:
        print("TELEGRAM_BOT2_API_KEY et TELEGRAM_CHAT_ID ne sont pas définis.")

def main():
    parser = argparse.ArgumentParser(description="Script de Bot Telegram")
    parser.add_argument('--job', choices=['get_chat_id', 'send_message'], required=True, help="Tâche à effectuer")
    parser.add_argument('--message', help="Message personnalisé à envoyer", default=None)
    args = parser.parse_args()

    if args.job == 'get_chat_id':
        bot_token = TELEGRAM_BOT2_API_KEY
        chat_id = get_chat_id(bot_token)
        if chat_id:
            print(f"ID du chat : {chat_id}")
        else:
            print("Impossible de récupérer l'ID du chat.")

    elif args.job == 'send_message':
        if args.message:
            send_reminder(args.message)
        else:
            print("Aucun message fourni pour la tâche send_message.")
            
if __name__ == '__main__':
    main()
```