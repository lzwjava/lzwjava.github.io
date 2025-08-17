---
audio: false
generated: false
image: false
lang: de
layout: post
title: Der Weg zur Verfolgung der Internetfreiheit
translated: true
---

### Inhaltsverzeichnis

1. [Proxy-Lösungen in China](#proxy-lösungen-in-china)
   - Macao-SIM-Karten-Lösungen (Beste Option)
   - Proxy-Server-Empfehlungen
   - App-Konfiguration und Einrichtung
   - Zahlung und regionale Einstellungen

2. [Der Weg zur Internetfreiheit](#der-weg-zur-internetfreiheit)
   - Zeitstrahl der Proxy-Methoden (2010–2025)
   - Vergleich: Internetfreiheit vs. Kurzsichtigkeitslösungen
   - Aktuelle Einrichtung und Leistung
   - Wiederherstellungsmethoden und gelernte Lektionen

3. [Macao-SIM-Karten](#macao-sim-karten)
   - Details zur China Telecom Easy+ SIM-Karte
   - Blue Macau SIM-Karten-Optionen
   - Preise und Datentarife
   - Gerätekompatibilität

4. [Shadowsocks-Proxy-Probleme](#shadowsocks-proxy-probleme)
   - Netzwerkspezifische Verbindungsprobleme
   - Leistungsunterschiede zwischen 5G und 4G
   - Fehlerbehebung und Lösungen
   - Auswirkungen der Richtlinien von ISPs und Mobilfunkanbietern

---

## Proxy-Lösungen in China

*29.12.2024*

- Die beste Methode ist der Erwerb einer **China-Macao-SIM-Karte**, um bei Bedarf direkt mobiles Internet zu nutzen. Besuchen Sie [https://www.1888.com.mo](https://www.1888.com.mo). Eine Karte mit **10 GB mobilen Daten** kostet etwa **80 CNY** und bietet eine schnelle, unkomplizierte Nutzung.

- **China Telecom Macao-SIM-Karten** gibt es in zwei Varianten: **rot** und **blau**.
  - **Rote Karten** bieten Tagespakete (z. B. **2, 3 oder 5 Macao-Dollar/Tag**).
  - **Blaue Karten** bieten Datentarife wie **10 GB für 98 Macao-Dollar** oder **20 GB für 198 Macao-Dollar** ohne monatliche Grundgebühr.

- Falls Sie mehr Daten benötigen oder häufig einen Laptop nutzen, empfehle ich [zhs.cloud](https://zhs.cloud). Für **30 CNY/Monat** erhalten Sie Zugang zu etwa **15 globalen Proxy-Servern**.

- **Auf iOS**: Nutzen Sie **Shadowrocket** mit Shadowsocks-Regeln:
  [https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever](https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever).
  Konfigurieren Sie **globale Routing-Regeln**, um den Datenverkehr zwischen China und dem Ausland zu trennen.

- **Auf Android**: Verwenden Sie **V2Ray**.
  - **Fire TV**: V2Ray-App.
  - **Apple TV**: Shadowrocket-App.
  - **Mac**: ShadowsocksX-NG oder ClashX.

- **Eigenen Proxy-Server einrichten wird nicht empfohlen**. Protokolle wie **Shadowsocks, VMess oder Trojan** werden schnell blockiert – unabhängig vom Server.

- **App Store auf USA-Regional umstellen**:
  Aktivieren Sie einen **globalen Proxy (USA)**, dann erscheint die Zahlungsoption *„Keine“*, sodass Sie die Region problemlos wechseln können.

- **Guthabenkarten kaufen**:
  Nutzen Sie eine **Visa-Karte**, um Amazon-Guthaben oder Apple-Guthabenkarten über das Apple-Portal zu erwerben.

---

## Der Weg zur Internetfreiheit

*03.02.2025, letzter Update: August 2025*

### Meine Reise

- **2010–2013**: Nutzung von **Goagent** und **SwitchyOmega**, um die GFW zu umgehen.
- **2014–2015**: Proxy mit **Qujing (曲径)**; der Autor lebt mittlerweile in Japan.
- **Juni 2016–Juli 2018**: Eigenen **Shadowsocks-Proxy-Server** auf **Digital Ocean** gehostet.
- **Ab 2019**: Wechsel zu [zhs.cloud](https://zhs.cloud).
- **März 2023**: Nutzung einer **Macao-SIM-Karte** im Handy für **internet ohne Proxy/VPN** (ca. **150 CNY/Monat** für **20 GB**; etwa ein Jahr lang genutzt).
- **2024**: Rückkehr zu **Outline Manager** mit eigenem Shadowsocks-Server; Tests mit verschiedenen Cloud-Anbietern.
- **Februar 2025**: Aktuelle Lösung:
  - **Outline Manager** mit **Aliyun-Hongkong-Server** für den täglichen Gebrauch.
  - **Nicht-Hongkong-Server** (z. B. Singapur/Japan) für **KI-Tools**.
  - Gleiche Proxy-Regeln wie in **Shadowrocket/Clash**.
- **Ab Juni 2025**:
  - **Python-Skript** auf dem Laptop, das alle **10 Minuten** automatisch den schnellsten Proxy-Server basierend auf Geschwindigkeitstests auswählt (Priorität: **Singapur > Hongkong** für KI-Tools).
  - Details: [Automatisierung von Clash-Proxy-Management](/clash-en).
  - Cloud-Anbieter bleibt [zhs.cloud](https://zhs.cloud).
  - **Auf iOS**: Rückkehr zur **Macao-SIM-Karte** (**150 CNY/Monat** für **20 GB** + **3x 5 GB Nachkauf** à **20 MOP**, Gesamt: **~200 CNY** für **35 GB**).

  Die letzten **2 Monate** funktioniert dies einwandfrei. Ich hoffe, diese Methode bis zu meinem Auslandsaufenthalt nutzen zu können.

### Unterschiede im Vergleich zur Kurzsichtigkeits-Behandlung

- **GFW** ist **menschengemacht** – **Proxy-Lösungen** lassen sich leicht messen.
- **Kurzsichtigkeit** erfordert **Zeit**, um Veränderungen der Augapfelform zu erkennen.

### Gemeinsamkeiten

- Beide Lösungen (**Proxy & Brille mit -200 Dioptrien**) funktionieren oft gut.
- **Internetzugang** vs. **Sehverbesserung** – beides löst **grundlegende Probleme**.
- **Prinzip**: Versteht man die **Funktionsweise der GFW**, findet man leicht eine Umgehung.

### Reflexionen und Nuancen

- Ich verstehe die **GFW nicht vollständig**. Wenn mein Proxy-Server blockiert wird, habe ich nun mehr Möglichkeiten, die Ursache zu analysieren:
  - **Mobiles Netz oder Festnetz?** → **4G oder 5G?**
  - Bei **Kurzsichtigkeit**: Nach **6–12 Monaten** prüfen, ob sich Unterschiede zwischen den Augen zeigen oder ob ich die meiste Zeit nur „gerade so scharf“ sehe, ohne die Augen zu überanstrengen.

### Aktueller Status

- Mein Proxy-Server läuft **einwandfrei**:
  - **Handy**: **80 Mbit/s Download**, **50 Mbit/s Upload** (Hongkong-Server).
  - **Laptop**: Gleiche Leistung.
- **Konfiguration**: Gleiche Proxy-Einstellungen auf allen Geräten.
  - **Standard**: Proxy für **ausländische Websites**.
  - **KI-Tools**: **Nicht-Hongkong-Server** (z. B. Singapur).

### Wiederherstellung

Falls etwas nicht funktioniert:
1. **Elastische IP** des **Aliyun-Hongkong-Servers** ändern.
2. Neue Proxy-URL in die **Cloud speichern**.
3. **Zwei Skripte ausführen** (~1 Minute) → Laptop/Handy aktualisieren die Serveradresse automatisch.

### Bedauern

- Ich habe **zu viel Zeit** mit dem **Kampf gegen die GFW** verschwendet und viele Protokolle ausprobiert, obwohl ich wusste, dass sie erkannt und blockiert werden.
- **Ohne zuverlässigen Proxy-Server** ist die Einrichtung auf einem **OpenWrt-Router** schwierig.
- **Was ich bereue**:
  - **Techniken von Anbietern wie [zhs.cloud](https://zhs.cloud)** nicht früher gelernt zu haben – jetzt kenne ich die meisten ihrer Geheimnisse.
  - **Oberflächliche Analyse**: Bei Blockaden dachte ich nur: *„Neuen Server aufsetzen = neue IP“*, ohne tiefer nach Ursachen zu forschen.

### Metriken

- **Speedtest hätte ich früher nutzen sollen** – ich kannte das Tool lange, aber nicht seine volle Anwendung.
- **Regelmäßige Tests** helfen:
  - **5G**: Oft **>100 Mbit/s**.
  - **Festnetz**: Selten **>100 Mbit/s**.
- **Kurzsichtigkeit**:
  - Ich besorgte mir eine **C-förmige Sehtafel** und eine **Standard-Sehtesttafel**.
  - **Ohne Messung keine Verbesserung** – regelmäßige Tests zeigen Fortschritte.

### Es ist noch früh

- **Wird die GFW in den nächsten Jahren fallen?** Ungewiss.
- Als ich nach **2 Jahren Kurzsichtigkeits-Behandlung** einem Freund sagte, meine Methode müsse verbessert werden (Brille mit **-200 statt -150 Dioptrien**), antwortete er:
  *„Kein Problem, es ist nicht verschwendete Zeit – es ist noch früh.“*
  - **Grundlegende Dinge** wie Kurzsichtigkeit sollten **früher entdeckt** werden.
  - **Todd Becker** teilte seine Erkenntnisse **2014 auf YouTube** (über 1 Mio. Aufrufe) – doch **2025** wissen **weniger als 10.000 Menschen** weltweit davon. Wie viele werden es in 10 Jahren sein?

---

## Macao-SIM-Karten

*20.04.2023*

### Meine Erfahrungen mit Macao-SIM-Karten

Bei einem Wochenendbesuch in Macao **2023** kaufte ich eine **China Telecom Easy+ SIM-Karte**. Zurück in **Guangzhou** funktionierte sie **einwandfrei** – ich konnte **Englisch lernen** und **ausländische Apps herunterladen**, als wäre ich noch in Macao. **Absolut empfehlenswert!**
Später testete ich die **Blue Macau SIM-Karte**, die ebenfalls gut war. Hier ein kurzer Überblick:

#### **China Telecom Easy+ SIM-Karte**

**Einfach zu nutzen – jederzeit!**

### Wichtige Punkte
- **Keine Kaution**; automatische Aktivierung für **Festlandchina, Macao und Hongkong**.
- **Kein Vertrag, keine Kündigungsgebühr**; sofort einsatzbereit nach Kauf.
- **Macao-Nummer inklusive**; optionale **Festlandchina-Nummer** für Dual-Number-Nutzung.
- **Online oder per Wertkarte aufladbar**.

### Tagesgebühren-Optionen
- **2 MOP/Tag**: **4 GB Hochgeschwindigkeitsdaten**, dann unbegrenztes Datenvolumen mit reduzierter Geschwindigkeit; **5.000 Minuten** lokale Gespräche.
- **3 MOP/Tag**: **10 GB Hochgeschwindigkeitsdaten**, dann unbegrenzt reduziert; **5.000 Minuten** lokale Gespräche.
- **5 MOP/Tag**: **20 GB Hochgeschwindigkeitsdaten**, dann unbegrenzt reduziert; **5.000 Minuten** lokale Gespräche.

### Extras
- **Datenverbrauch in Hongkong**: **0,1 MOP/MB**.
- **Tarifwechsel jederzeit per SMS möglich**.

#### **Blue Macau SIM-Karte**

### Wichtige Punkte
- **Keine monatliche Grundgebühr**; Nutzung nach Verbrauch.
- **Lokale Gespräche**: **0,39 MOP/Minute**; **Internet**: **0,1 MOP/MB**; **SMS**: **1 MOP/Nachricht**.
- **Optionale Datenpakete ohne Ablauf**:
  - **10 GB für 98 MOP**
  - **20 GB für 188 MOP**
  - **40 GB für 288 MOP**
- **Alle 180 Tage aufladen**, um aktiv zu bleiben.

#### **Kompatible Geräte**
- Erfordert ein **4G-fähiges Gerät** oder ein **China-Telecom-kompatibles Handy**.

Weitere Infos: [China Telecom Macau](https://www.1888.com.mo/).

---
Auf **Taobao** finden Sie diese Karten auch:

<div align="center"><img src="/assets/images/macao/easy.jpg" width="300px" /><img/></div>

---

## Shadowsocks-Proxy-Probleme

*03.01.2025*

**Zhiwei:**
Ich war mit einem Freund grillieren und nutzte **Shadowsocks mit einem Singapur-Server**, um die GFW zu umgehen. **Auf 5G draußen** konnte ich mich **nicht verbinden** – YouTube ließ sich nicht aufrufen (Timeout). **Zu Hause mit 4G oder China-Telecom-Festnetz** funktioniert Shadowsocks jedoch problemlos. Warum?

**Mistral:**
Das klingt nach **netzwerkspezifischen Verbindungsproblemen** mit Shadowsocks auf **5G im Freien**, nicht aber auf **4G oder im heimischen Netzwerk**. Mögliche Gründe:

1. **Unterschiede in der Netzwerkkonfiguration**:
   - **5G-Netzwerk**: Strengere **Firewall-Regeln** oder **andere Routing-Pfade** als 4G. Manche Anbieter blockieren oder drosseln **VPN/Proxy-Verkehr** auf 5G.
   - **4G-Netzwerk**: Lockerere Einstellungen oder bessere Kompatibilität mit Shadowsocks.

2. **Einschränkungen des Internetdienstanbieters (ISP)**:
   - **Mobilfunkanbieter-Politik**: Unterschiedliche Regeln für **VPN-Nutzung**. Ihr 5G-Anbieter könnte **Shadowsocks aktiv blockieren**.
   - **Heimnetzwerk (China Telecom)**: Weniger Restriktionen → Shadowsocks läuft ohne Probleme.

3. **Signalstärke und Stabilität**:
   - **5G-Signal**: In Außenbereichen oft **instabil** – schwache Verbindung → Zeitüberschreitungen.
   - **4G-Signal**: **Stabiler** und konsistenter → bessere Proxy-Leistung.

4. **Standort des Proxy-Servers**:
   - **Singapur-Server**: **Latenz und Routing** könnten auf 5G schlechter sein als auf 4G oder im Festnetz.

5. **Geräteeinstellungen**:
   - **Konfiguration prüfen**: Stellen Sie sicher, dass Shadowsocks für **alle Netzwerke** (5G/4G/WLAN) korrekt eingerichtet ist.
   - **App-Berechtigungen**: Shadowsocks benötigt **Volle Netzwerkzugriffsrechte**.

### **Fehlerbehebung:**

1. **Netzwerkeinstellungen prüfen**:
   - Shadowsocks-Konfiguration für **5G und 4G** überprüfen.
   - Gibt es **spezifische Blockaden** im 5G-Netz?

2. **Andere Server testen**:
   - Verbindung zu **alternativen Shadowsocks-Servern** herstellen (z. B. Hongkong/Japan).
   - **Latenz und Stabilität** der Server vergleichen.

3. **Mobilfunkanbieter kontaktieren**:
   - Nachfragen, ob **5G-Netzwerk VPN/Proxy-Verkehr einschränkt**.

4. **Software aktualisieren**:
   - **Shadowsocks-App und Gerätesoftware** auf dem neuesten Stand halten.

5. **Alternative Proxys/VPNs ausprobieren**:
   - Manche Dienste (z. B. **V2Ray, Trojan**) könnten **bessere 5G-Kompatibilität** bieten.

---
**Aktualisierung:**

Tatsächlich nutze ich zu Hause **China Mobile** (IP-Bereich: **120.235.8.xx**).
**Interessanterweise**:
- Proxy funktioniert **normal auf mobilen Daten und China-Telecom-Netzen**, scheitert aber **gelegentlich auf meinem heimischen WLAN**.

**Systematische Überprüfung** dieser Faktoren sollte die Ursache eingrenzen.