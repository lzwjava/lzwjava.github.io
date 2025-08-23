---
audio: true
generated: false
image: false
lang: es
layout: post
title: Inversiones Semanales en Acciones con la API de TigerOpen
translated: true
---

Desarrollé un script en Python y un flujo de trabajo de GitHub Actions para automatizar mi estrategia de inversión semanal, comprando una acción de NVIDIA todos los miércoles a las 10:35 PM Hora Estándar de China (CST). Elegí los miércoles porque, en 2025, no hay días festivos en ese día, asegurando una ejecución consistente.

## Descripción General

El script utiliza la API de TigerOpen para colocar una orden de mercado para acciones de NVIDIA y monitorea su estado. El flujo de trabajo de GitHub Actions ejecuta el script en un horario, manejando la configuración y la autenticación de manera segura. A continuación se presentan los detalles de ambos componentes.

## Script en Python

Este script coloca una orden de compra para una acción de NVIDIA, verifica su estado durante hasta 60 segundos y la cancela si no se llena.

```python
import time
import os
from tigeropen.common.consts import Language, OrderStatus
from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.common.util.signature_utils import read_private_key
from tigeropen.trade.trade_client import TradeClient
from tigeropen.common.util.order_utils import market_order
from tigeropen.common.util.contract_utils import stock_contract

def get_client_config(sandbox=False):
    client_config = TigerOpenClientConfig(sandbox_debug=sandbox)
    client_config.private_key = read_private_key(os.environ.get('TIGER_PEM'))
    client_config.tiger_id = os.environ.get('TIGER_TIGER_ID')
    client_config.account = os.environ.get('TIGER_ACCOUNT')
    client_config.language = Language.zh_CN
    return client_config

# Función para colocar una orden
def place_order():
    client_config = get_client_config()
    trade_client = TradeClient(client_config)
    account = client_config.account  # Almacenar cuenta para uso posterior

    contract = stock_contract(symbol='NVDA', currency='USD')
    stock_order = market_order(
        account=account, contract=contract, action='BUY', quantity=1
    )
    # Colocar la orden
    order_id = trade_client.place_order(stock_order)
    print(f"Orden colocada con ID: {order_id}")

    # Seguir el tiempo
    start_time = time.time()
    while time.time() - start_time < 60:  # Tiempo de espera de 1 minuto
        # Obtener la orden y encontrar la que acabamos de colocar
        order = trade_client.get_order(id=order_id)
        if str(order.id) == str(order_id):
            print(f"ID de orden coincidente! Verificando el estado de la orden: {order.status}")
            # Verificar el estado de la orden utilizando los valores de la enumeración OrderStatus
            if order.status == OrderStatus.FILLED:
                print("Orden completada con éxito.")
                return
            elif order.status == OrderStatus.REJECTED:
                print(f"Orden rechazada: {order_id}")
                raise Exception(f"La orden {order_id} fue rechazada")
            elif order.status in [
                OrderStatus.PENDING_NEW,
                OrderStatus.NEW,
                OrderStatus.HELD,
                OrderStatus.PENDING_CANCEL
            ]:
                print(f"La orden está pendiente, estado: {order.status}")
            else:
                print(f"El estado de la orden es: {order.status}")

        # Dormir antes de verificar nuevamente
        time.sleep(5)  # Verificar cada 5 segundos

    # Si la orden no se completa en 1 minuto, cancelarla
    print("La orden no se completó en 1 minuto. Cancelando la orden.")
    trade_client.cancel_order(id=order_id)
    print(f"Orden cancelada: {order_id}")

if __name__ == '__main__':
    place_order()
```

## Flujo de Trabajo de GitHub Actions

El flujo de trabajo se ejecuta todos los miércoles a las 14:35 UTC (10:35 PM UTC) y configura el entorno, instala las dependencias y ejecuta el script.

```yaml
name: Inversión Regular

on:
  schedule:
    - cron: '35 14 * * 3'  # Ejecutar todos los miércoles a las 14:35 UTC
  workflow_dispatch:

concurrency:
  group: 'trading'
  cancel-in-progress: false

permissions:
  id-token: write
  contents: write
  pages: write

jobs:
  invest:
    runs-on: ubuntu-latest
    steps:
      - name: Verificar Repositorio
        uses: actions/checkout@v4
        with:
          fetch-depth: 5

      - name: Configurar Python 3.13.2
        uses: actions/setup-python@v4
        with:
          python-version: "3.13.2"

      - name: Instalar Dependencias
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Configurar Archivo Tiger PEM
        run: |
          echo "${{ secrets.TIGER_PEM_CONTENT }}" > tiger.pem
          chmod 600 tiger.pem

      - name: Ejecutar Script de Tiger
        id: tiger_update
        run: python invest.py
        env:
          TIGER_TIGER_ID: ${{ secrets.TIGER_TIGER_ID }}
          TIGER_ACCOUNT: ${{ secrets.TIGER_ACCOUNT }}
          TIGER_PEM: "tiger.pem"
```