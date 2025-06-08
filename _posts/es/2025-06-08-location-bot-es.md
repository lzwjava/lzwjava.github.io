---
audio: false
generated: false
lang: es
layout: post
title: Automatizando Tu Tarjeta de Puntos con un Bot de Ubicación en Telegram
translated: true
---

¿Alguna vez has deseado que tu "tarjeta de asistencia" diaria fuera menos tediosa? Yo sí. Por eso construí un bot personal de Telegram que utiliza el seguimiento de ubicación para automatizar las notificaciones de llegada a la oficina y recordarme esos registros cruciales. Este post explica cómo combiné Python con GitHub Actions para crear un sistema fluido y sin intervención, manteniéndome informado justo cuando lo necesito, todo basado en mi ubicación.

```yml
name: Verificación de Ubicación por Hora

on:
  schedule:
    # Se ejecuta cada hora, en punto, entre las 11 AM y las 11 PM, de lunes a viernes
    # La hora está en UTC. La hora de Singapur (SGT) es UTC+8.
    # Así, las 11 AM SGT son las 03:00 UTC, y las 11 PM SGT son las 15:00 UTC.
    # Por lo tanto, programamos de 03:00 a 15:00 UTC.
    - cron: '0 3-15 * * 1-5'

    # Recordatorio para INICIAR el compartir ubicación en vivo: miércoles a las 11 AM SGT (3 AM UTC)
    # Hora actual: domingo, 8 de junio de 2025 a las 5:10:58 PM +08 (SGT)
    # Para miércoles a las 11 AM SGT (UTC+8): 11 - 8 = 3 AM UTC.
    - cron: '0 3 * * 3' # 3 para miércoles

    # Recordatorio para DETENER el compartir ubicación en vivo: viernes a las 11 PM SGT (3 PM UTC)
    # Hora actual: domingo, 8 de junio de 2025 a las 5:10:58 PM +08 (SGT)
    # Para viernes a las 11 PM SGT (UTC+8): 23 - 8 = 15 PM UTC.
    - cron: '0 15 * * 5' # 5 para viernes

  workflow_dispatch:  # Permite la activación manual del flujo de trabajo
  push:
    branches: ["main"]
    paths:
      - 'scripts/release/location_bot.py' # Ruta corregida a tu script
      - '.github/workflows/location.yml' # Ruta a este archivo de flujo de trabajo

concurrency:
  group: 'location'
  cancel-in-progress: false

jobs:
  check_and_notify:
    runs-on: ubuntu-latest
    env:
      TELEGRAM_LOCATION_BOT_API_KEY: ${{ secrets.TELEGRAM_LOCATION_BOT_API_KEY }}

    steps:
    - name: Clonar repositorio
      uses: actions/checkout@v4
      with:
        fetch-depth: 5 # Solo obtiene los últimos 5 commits para eficiencia

    - name: Configurar Python 3.13.2
      uses: actions/setup-python@v4
      with:
        python-version: "3.13.2" # Especifica la versión exacta de Python

    - name: Instalar dependencias
      run: |
        python -m pip install --upgrade pip
        # Asumiendo que tienes un requirements.simple.txt en la raíz de tu repositorio.
        # Si no, usa: pip install requests python-dotenv
        pip install -r requirements.simple.txt 

    - name: Ejecutar script de verificación de ubicación (Programado)
      run: python scripts/release/location_bot.py --job check_location
      # Este paso se ejecutará en los triggers programados para la verificación por hora
      if: github.event.schedule == '0 3-15 * * 1-5' # Coincide con el horario cron por hora

    - name: Recordatorio para INICIAR el compartir ubicación en vivo
      run: python scripts/release/location_bot.py --job start_sharing_message
      if: github.event.schedule == '0 3 * * 3' # Coincide con miércoles a las 11 AM SGT cron

    - name: Recordatorio para DETENER el compartir ubicación en vivo
      run: python scripts/release/location_bot.py --job stop_sharing_message
      if: github.event.schedule == '0 15 * * 5' # Coincide con viernes a las 11 PM SGT cron

    - name: Ejecutar script de Telegram para mensaje de prueba (Activación Manual)
      run: python scripts/release/location_bot.py --job send_message --message "Este es un mensaje de prueba de activación manual desde GitHub Actions."
      if: github.event_name == 'workflow_dispatch'

    - name: Ejecutar script de Telegram para push a la rama main
      run: python scripts/release/location_bot.py --job send_message --message "Cambios en el código del bot de ubicación enviados a la rama main."
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
import time # Para posible monitoreo continuo en el futuro

load_dotenv()

# Nuevo: Clave API específica para el bot de ubicación
TELEGRAM_LOCATION_BOT_API_KEY = os.environ.get("TELEGRAM_LOCATION_BOT_API_KEY") # Asegúrate de configurarla en tu .env
TELEGRAM_CHAT_ID = "610574272" # Este ID de chat es para enviar el mensaje de notificación

# Define las coordenadas de tu oficina
OFFICE_LATITUDE = 23.135368
OFFICE_LONGITUDE = 113.32952

# Radio de proximidad en metros
PROXIMITY_RADIUS_METERS = 300

def send_telegram_message(bot_token, chat_id, message):
    """Envía un mensaje a un chat de Telegram usando la API del Bot de Telegram."""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown" # Usando Markdown para texto en negrita en el mensaje
    }
    response = requests.post(url, params=params)
    if response.status_code != 200:
        print(f"Error al enviar mensaje de Telegram: {response.status_code} - {response.text}")

def get_latest_location(bot_token):
    """Recupera la última actualización de ubicación en vivo del bot."""
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    # Offset para obtener solo actualizaciones nuevas después de la última procesada (para sondeo continuo)
    # Para un script simple de una sola ejecución, obtendremos solo la última, pero para sondeo, gestionarías un offset.
    params = {"offset": -1} # Obtiene la última actualización
    response = requests.get(url, params=params)
    print("Respuesta de GetUpdates:", response) # Depuración
    if response.status_code == 200:
        updates = response.json()
        print("JSON de GetUpdates:", json.dumps(updates, indent=4)) # Depuración
        if updates['result']:
            last_update = updates['result'][-1]
            # Prioriza edited_message para ubicaciones en vivo
            if 'edited_message' in last_update and 'location' in last_update['edited_message']:
                return last_update['edited_message']['location'], last_update['edited_message']['chat']['id']
            elif 'message' in last_update and 'location' in last_update['message']:
                # Maneja mensajes iniciales de ubicación en vivo o compartir ubicación estática
                return last_update['message']['location'], last_update['message']['chat']['id']
    return None, None

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calcula la distancia entre dos puntos en la Tierra usando la fórmula de Haversine.
    Devuelve la distancia en metros.
    """
    R = 6371000  # Radio de la Tierra en metros

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
    parser = argparse.ArgumentParser(description="Script del Bot de Telegram")
    # Opciones actualizadas para el argumento --job
    parser.add_argument('--job', choices=['get_chat_id', 'send_message', 'check_location', 'start_sharing_message', 'stop_sharing_message'], required=True, help="Trabajo a realizar")
    # Añadido argumento --message para el trabajo 'send_message'
    parser.add_argument('--message', type=str, help="Mensaje a enviar para el trabajo 'send_message'")
    # Añadido argumento --test para el trabajo 'check_location'
    parser.add_argument('--test', action='store_true', help="Para el trabajo 'check_location', fuerza el envío de un mensaje independientemente de la proximidad.")
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
                    print(f"ID de Chat: {chat_id}")
                else:
                    print("No se pudo recuperar el ID de chat de la última actualización.")
            else:
                print("No se encontraron actualizaciones.")
        else:
            print(f"Error al obtener actualizaciones: {response.status_code} - {response.text}")

    elif args.job == 'send_message':
        if TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = args.message if args.message else "¡Este es un mensaje de prueba predeterminado desde tu script de bot de Telegram!"
            send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print(f"Mensaje enviado con éxito: {message}")
        else:
            print("TELEGRAM_LOCATION_BOT_API_KEY y TELEGRAM_CHAT_ID no están configurados.")

    elif args.job == 'start_sharing_message':
        if TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = "⚠️ *Recordatorio:* ¡Por favor, comienza a compartir tu ubicación en vivo con el bot!"
            send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print("Recordatorio de inicio de compartir enviado.")
        else:
            print("TELEGRAM_LOCATION_BOT_API_KEY y TELEGRAM_CHAT_ID no están configurados.")

    elif args.job == 'stop_sharing_message':
        if TELEGRAM_LOCATION_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = "✅ *Recordatorio:* Ya puedes dejar de compartir tu ubicación en vivo."
            send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print("Recordatorio de detener compartir enviado.")
        else:
            print("TELEGRAM_LOCATION_BOT_API_KEY y TELEGRAM_CHAT_ID no están configurados.")

    elif args.job == 'check_location':
        if not TELEGRAM_LOCATION_BOT_API_KEY or not TELEGRAM_CHAT_ID:
            print("TELEGRAM_LOCATION_BOT_API_KEY y TELEGRAM_CHAT_ID deben estar configurados para verificaciones de ubicación.")
            return

        user_location, location_chat_id = get_latest_location(TELEGRAM_LOCATION_BOT_API_KEY)

        if user_location:
            current_latitude = user_location['latitude']
            current_longitude = user_location['longitude']

            distance = haversine_distance(
                OFFICE_LATITUDE, OFFICE_LONGITUDE,
                current_latitude, current_longitude
            )

            print(f"Ubicación actual: ({current_latitude}, {current_longitude})")
            print(f"Distancia a la oficina: {distance:.2f} metros")

            needs_punch_card = distance <= PROXIMITY_RADIUS_METERS

            if needs_punch_card:
                print(f"¡Estás dentro de los {PROXIMITY_RADIUS_METERS}m de la oficina!")
                notification_message = (
                    f"🎉 *¡Llegaste a la Oficina!* 🎉\n"
                    f"Hora de registrar la asistencia en WeCom.\n"
                    f"Tu distancia actual desde la oficina: {distance:.2f}m."
                )
            else:
                print(f"Estás fuera del círculo de {PROXIMITY_RADIUS_METERS}m de la oficina.")
                # Mensaje para cuando estás fuera del radio
                notification_message = (
                    f"📍 Estás *fuera* de la proximidad de la oficina ({PROXIMITY_RADIUS_METERS}m).\n"
                    f"No es necesario registrar asistencia en este momento.\n"
                    f"Tu distancia actual desde la oficina: {distance:.2f}m."
                )

            # Envía mensaje si estás dentro de la proximidad O si se usa el flag --test
            if needs_punch_card or args.test:
                send_telegram_message(TELEGRAM_LOCATION_BOT_API_KEY, TELEGRAM_CHAT_ID, notification_message)
            else:
                # Si no estás dentro de la proximidad Y no estás en modo prueba, solo imprime en consola (sin mensaje a Telegram)
                print("No estás dentro de la proximidad y no estás en modo prueba, no se envió mensaje a Telegram.")
        else:
            print("No se pudo recuperar tu última ubicación. Asegúrate de estar compartiendo tu ubicación en vivo con el bot.")

if __name__ == '__main__':
    main()
```