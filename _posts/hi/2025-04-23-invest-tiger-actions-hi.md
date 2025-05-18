---
audio: true
generated: false
lang: hi
layout: post
title: साप्ताहिक स्टॉक निवेश टाइगरओपन एपीआई के साथ
translated: true
---

मैंने एक Python स्क्रिप्ट और एक GitHub Actions वर्कफ़्लो बनाया है ताकि मेरी सप्ताहिक निवेश योजना को स्वचालित किया जा सके, जो हर बुधवार को 10:35 PM UTC पर एक NVIDIA स्टॉक खरीदता है। मैंने बुधवार को चुना क्योंकि 2025 में इस दिन कोई छुट्टी नहीं है, जिससे निरंतर निष्पादन सुनिश्चित होता है।

## अवलोकन

इस स्क्रिप्ट का उपयोग TigerOpen API से NVIDIA स्टॉक के लिए एक मार्केट ऑर्डर लगाने और उसकी स्थिति का निगरानी करने के लिए किया जाता है। GitHub Actions वर्कफ़्लो इस स्क्रिप्ट को एक शेड्यूल पर चलाता है, सेटअप और प्रमाणीकरण को सुरक्षित रूप से संभालता है। नीचे दोनों घटकों के विवरण दिए गए हैं।

## Python स्क्रिप्ट

यह स्क्रिप्ट एक NVIDIA स्टॉक के लिए खरीद ऑर्डर लगाती है, उसकी स्थिति को 60 सेकंड तक चेक करती है, और अगर पूरा नहीं हुआ तो इसे रद्द करती है।

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

# ऑर्डर लगाने का फ़ंक्शन
def place_order():
    client_config = get_client_config()
    trade_client = TradeClient(client_config)
    account = client_config.account  # बाद में उपयोग के लिए अकाउंट स्टोर करें

    contract = stock_contract(symbol='NVDA', currency='USD')
    stock_order = market_order(
        account=account, contract=contract, action='BUY', quantity=1
    )
    # ऑर्डर लगाएं
    order_id = trade_client.place_order(stock_order)
    print(f"ऑर्डर लगाया गया ID: {order_id}")

    # समय ट्रैक करें
    start_time = time.time()
    while time.time() - start_time < 60:  # 1 मिनट टाइमआउट
        # ऑर्डर प्राप्त करें और जिस ऑर्डर को हमने लगाया है उसे ढूँढें
        order = trade_client.get_order(id=order_id)
        if str(order.id) == str(order_id):
            print(f"ऑर्डर ID मिल गया! ऑर्डर स्थिति चेक कर रहा हूँ: {order.status}")
            # ऑर्डर स्थिति चेक करें OrderStatus enum मानों का उपयोग करके
            if order.status == OrderStatus.FILLED:
                print("ऑर्डर सफलतापूर्वक पूरा हुआ।")
                return
            elif order.status == OrderStatus.REJECTED:
                print(f"ऑर्डर अस्वीकृत: {order_id}")
                raise Exception(f"ऑर्डर {order_id} अस्वीकृत हुआ")
            elif order.status in [
                OrderStatus.PENDING_NEW,
                OrderStatus.NEW,
                OrderStatus.HELD,
                OrderStatus.PENDING_CANCEL
            ]:
                print(f"ऑर्डर प्रतीक्षा में है, स्थिति: {order.status}")
            else:
                print(f"ऑर्डर स्थिति है: {order.status}")

        # फिर से चेक करने से पहले सोएँ
        time.sleep(5)  # हर 5 सेकंड पर चेक करें

    # अगर ऑर्डर 1 मिनट में पूरा नहीं हुआ, तो इसे रद्द करें
    print("ऑर्डर 1 मिनट में पूरा नहीं हुआ। ऑर्डर रद्द कर रहा हूँ।")
    trade_client.cancel_order(id=order_id)
    print(f"ऑर्डर रद्द: {order_id}")

if __name__ == '__main__':
    place_order()
```

## GitHub Actions वर्कफ़्लो

यह वर्कफ़्लो हर बुधवार को 14:35 UTC (10:35 PM UTC) पर चलता है और वातावरण सेटअप करता है, निर्भरताओं को इंस्टॉल करता है, और स्क्रिप्ट को निष्पादित करता है।

```yaml
name: Regular Invest

on:
  schedule:
    - cron: '35 14 * * 3'  # हर बुधवार को 14:35 UTC पर चलाएं
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
      - name: रिपॉजिटरी चेकआउट करें
        uses: actions/checkout@v4
        with:
          fetch-depth: 5

      - name: Python 3.13.2 सेटअप करें
        uses: actions/setup-python@v4
        with:
          python-version: "3.13.2"

      - name: निर्भरताओं को इंस्टॉल करें
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Tiger PEM फ़ाइल सेटअप करें
        run: |
          echo "${{ secrets.TIGER_PEM_CONTENT }}" > tiger.pem
          chmod 600 tiger.pem

      - name: Tiger स्क्रिप्ट चलाएँ
        id: tiger_update
        run: python invest.py
        env:
          TIGER_TIGER_ID: ${{ secrets.TIGER_TIGER_ID }}
          TIGER_ACCOUNT: ${{ secrets.TIGER_ACCOUNT }}
          TIGER_PEM: "tiger.pem"
```