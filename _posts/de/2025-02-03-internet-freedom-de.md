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
   - Optionen für Blue Macau SIM-Karten
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

- Die beste Lösung ist der Kauf einer China-Macao-SIM-Karte, um bei Bedarf direkt mobiles Internet zu nutzen. Besuchen Sie [https://www.1888.com.mo](https://www.1888.com.mo). Die Kosten betragen etwa 80 CNY für 10 GB mobiles Datenvolumen und bieten ein schnelles und problemloses Erlebnis.

- China Telecom Macao SIM-Karten gibt es in zwei Varianten: rot und blau. Rote Karten bieten Tagespläne, die typischerweise 2, 3 oder 5 Macao-Patacas pro Tag kosten. Blaue Karten bieten Datentarife wie 10 GB für 98 Macao-Patacas oder 20 GB für 198 Macao-Patacas ohne monatliche Gebühren.

- Falls Sie mehr Datenvolumen benötigen oder häufig einen Laptop nutzen, sollten Sie [zhs.cloud](https://zhs.cloud) in Betracht ziehen. Es bietet Zugang zu etwa 15 globalen Proxy-Servern für nur 30 CNY pro Monat.

- Auf iOS verwenden Sie Shadowrocket mit Shadowsocks-Regeln: [https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever](https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever). Konfigurieren Sie die globale Weiterleitung, um den Datenverkehr aus China von dem aus dem Ausland zu trennen.

- Auf Android verwenden Sie V2Ray. Auf Fire TV nutzen Sie die V2Ray-App. Auf Apple TV verwenden Sie die Shadowrocket-App. Auf dem Mac nutzen Sie die Apps ShadowsocksX-NG oder ClashX.

- Es wird nicht empfohlen, einen eigenen Proxy-Server einzurichten. Protokolle wie Shadowsocks, VMess oder Trojan werden leicht blockiert, unabhängig vom verwendeten Server.

- Um den App Store auf die USA-Region umzustellen, aktivieren Sie einen globalen Proxy (USA), und es wird die Zahlungsoption „Keine“ angezeigt, sodass Sie die Region problemlos wechseln können.

- Verwenden Sie eine Visa-Karte, um Geschenkkarten von Amazon zu kaufen, oder nutzen Sie das Apple-Geschenkkarten-Portal, um Ihr App-Store-Konto aufzuladen.

---

## Der Weg zur Internetfreiheit

*03.02.2025, Dieser Beitrag wurde zuletzt im August 2025 aktualisiert.*

#### Der Weg

Von 2010 bis 2013 nutzte ich Goagent und das Proxy-Tool SwitchyOmega, um die GFW zu umgehen.

Zwischen 2014 und 2015 verwendete ich Qujing (曲径) für Proxy-Zwecke und folgte dessen Autor auf Twitter, der heute in Japan lebt.

Von Juni 2016 bis Juli 2018 nutzte ich Digital Ocean, um meinen Shadowsocks-Proxy-Server zu hosten.

Ab 2019 begann ich, [zhs.cloud](https://zhs.cloud) zu verwenden.

Im März 2023 begann ich, eine Macao-SIM-Karte in meinem Handy für den Internetzugang ohne Proxy oder VPN zu nutzen. Dies kostete etwa 150 CNY pro Monat für 20 GB mobiles Datenvolumen, und ich nutzte diese Methode etwa ein Jahr lang.

2024 begann ich erneut, Outline Manager mit meinem Shadowsocks-Proxy-Server zu verwenden und experimentierte mit verschiedenen Cloud-Anbietern.

Im Februar 2025 besteht meine bevorzugte Einrichtung aus Outline Manager mit einem Aliyun-Hongkong-Server für den täglichen Gebrauch und einem Nicht-Hongkong-Server (z. B. Singapur oder Japan) für KI-Tools. Ich behalte dieselbe Proxy-Regelkonfiguration bei, die in Shadowrocket oder Clash verwendet wird.

Ab Juni 2025 nutze ich ein Python-Skript auf meinem Laptop, das alle 10 Minuten automatisch einen Proxy-Server basierend auf Geschwindigkeitstestergebnissen auswählt. Das Skript priorisiert Singapur-Server gegenüber Hongkong-Servern für die Nutzung von KI-Tools. Weitere Details finden Sie unter [Automatisierung der Clash-Proxy-Verwaltung](/clash-en). Als VPN-Cloud-Anbieter nutze ich weiterhin [zhs.cloud](https://zhs.cloud).

Zusätzlich wechselte ich auf iOS zurück zur Nutzung einer Macao-SIM-Karte, die 150 CNY pro Monat für 20 GB Datenvolumen kostet. Ich kauft zusätzlich dreimal 5 GB Datenvolumen für jeweils 20 MOP, was insgesamt etwa 200 CNY für 35 GB Daten auf meinem Handy ergibt.

Diese Methode funktioniert seit den letzten 2 Monaten hervorragend. Ich hoffe, dass ich diese Methode weiterhin nutzen kann, um das Internet zu nutzen, bis ich China verlasse, um im Ausland zu arbeiten.

#### Der Unterschied im Vergleich zur Korrektur von Kurzsichtigkeit

Eine Herausforderung besteht darin, gegen die GFW zu kämpfen, die vom Menschen gemacht ist. Die andere besteht darin, die Prinzipien der Augenmuskelfunktion zu adressieren.

Die Wirksamkeit einer Proxy-Lösung lässt sich leicht messen. Die Korrektur von Kurzsichtigkeit erfordert jedoch Zeit, um festzustellen, ob sich der Augapfel verändert.

#### Gemeinsamkeiten mit der Korrektur von Kurzsichtigkeit

Eine Gemeinsamkeit besteht darin, dass sowohl eine Proxy-Lösung als auch eine Brille mit einer Reduktion von 200 Dioptrien oft gut funktionieren. Eine betrifft den Internetzugang, die andere die Verbesserung der Sehkraft. Beide lösen sehr wichtige Probleme.

Das zugrundeliegende Prinzip ist, dass wir, wenn wir verstehen, wie die GFW funktioniert und einen Weg finden, sie zu umgehen, die Lösung einfach sein sollte.

#### Überlegungen und Nuancen

Ich verstehe immer noch nicht vollständig, wie die GFW funktioniert. Wenn die IP meines Proxy-Servers blockiert wird, habe ich jetzt mehr Möglichkeiten, die Ursache zu untersuchen.

Ich kann überprüfen, ob die Blockade im Mobilfunknetz oder im heimischen Breitbandnetz auftritt. Falls es das Mobilfunknetz betrifft, kann ich prüfen, ob es sich um 4G oder 5G handelt.

Ähnlich verhält es sich mit meiner Kurzsichtigkeit: Wenn sich nach sechs Monaten oder einem Jahr keine Verbesserung zeigt, muss ich untersuchen, ob es Unterschiede zwischen meinen Augen gibt. Ich muss auch bedenken, ob ich die meiste Zeit über Dinge nur gerade so klar gesehen habe, ohne meine Augen zu überanstrengen.

#### Aktueller Stand

Mein Proxy-Server funktioniert derzeit sehr gut. Die Download-Geschwindigkeit auf meinem Handy erreicht 80 Mbit/s, und die Upload-Geschwindigkeit liegt bei 50 Mbit/s, wenn ich mit dem Hongkong-Proxy-Server verbunden bin. Das Gleiche gilt für meinen Laptop.

Ich verwende dieselben Proxy-Konfigurationen auf meinem Laptop und meinen Handys, und sie funktionieren einwandfrei. Normalerweise nutze ich einen Proxy-Server, um Websites außerhalb Chinas zu besuchen, und einen Nicht-HK-Server für KI-Tools.

#### Wiederherstellung

Falls etwas nicht funktioniert, ist meine Wiederherstellungsmethode einfach. Ich muss nur die elastische IP meines Aliyun-Hongkong-Proxy-Servers ändern und die neue Proxy-URL in der Cloud speichern. Das bedeutet, ich muss zwei Skripte ausführen, was etwa 1 Minute dauert, und mein Laptop und meine Handys können die Proxy-Server-Adresse aktualisieren.

#### Bedauern

Ich habe zu oft und zu lange gegen die GFW gekämpft. Ich habe viele Proxy-Protokolle ausprobiert, obwohl ich wusste, dass sie von der GFW erkannt und blockiert werden würden. Ohne einen zuverlässigen Proxy-Server ist es schwierig, einen Proxy auf einem OpenWrt-Router einzurichten.

Eine Sache, die ich bereue, ist, dass ich die Techniken von Proxy-Anbietern wie [zhs.cloud](https://zhs.cloud) nicht früher gelernt habe. Jetzt kenne ich die meisten ihrer Geheimnisse.

Das andere ist, dass ich, wenn mein Proxy-Server blockiert wurde, nicht tief genug nachdachte. Es schien, als bräuchte man nur einen neuen Proxy-Server mit einer neuen IP-Adresse, die noch nicht blockiert war. Doch das war oberflächliches Denken.

#### Metriken

Ich bereue, Speedtest nicht früher genutzt zu haben. Ich kannte den Namen des Tools schon lange, aber ich habe nicht gelernt, es sorgfältig zu verwenden.

Es ist gut, Speedtest häufig zu nutzen, wenn man mit 5G- oder 4G-Mobilfunkstationen oder einem heimischen Breitbandnetz verbunden ist.

Bei der Korrektur von Kurzsichtigkeit ist es ähnlich. Ich habe eine C-förmige Sehprobentafel und eine Standard-Sehprobentafel gekauft.

Keine Messung, keine Verbesserung. Das Messen von Dingen hilft beim Lernen. Die häufige Nutzung von Speedtest zeigt mir, dass es im 5G-Netz leicht ist, 100 Mbit/s zu überschreiten, während es im heimischen Breitbandnetz schwer ist, 100 Mbit/s zu erreichen.

#### Es ist noch früh

Wird die GFW in den nächsten Jahren fallen? Das ist schwer zu sagen.

Als ich nach zwei Jahren der Korrektur meiner Kurzsichtigkeit einem Freund sagte, dass meine Methode verbessert werden müsse und ich eine Brille mit 200 Dioptrien weniger als meine tatsächliche Sehstärke tragen sollte, statt 150 Dioptrien weniger,

sagte er, das sei kein Problem, es sei in Ordnung, keine Zeitverschwendung, und es sei noch früh. Ja. Diese Dinge sind grundlegend. Wie bei der Kurzsichtigkeit sollten die Menschen sie früher entdecken. Todd Becker teilte diese Entdeckung 2014 auf YouTube, und die Videos erreichten über eine Million Aufrufe. Und jetzt ist es 2025 – wie viele Menschen wissen wirklich davon auf der Welt? Ich schätze, es sind weniger als 10.000.

---

## Macao-SIM-Karten

*20.04.2023*

#### Meine Erfahrungen mit Macao-SIM-Karten

Während meines Wochenendbesuchs in Macao im Jahr 2023 kauft ich eine China Telecom Easy+ SIM-Karte für Macao. Nach meiner Ankunft in Guangzhou stellte ich fest, dass sie immer noch perfekt funktionierte und mir half, Englisch zu lernen und viele ausländische Apps herunterzuladen. Es fühlte sich an, als wäre ich noch in Macao. Ich empfehle sie sehr. Später probierte ich die Blue Macau SIM-Karte aus, die ebenfalls gut war. Hier ein kurzer Überblick über beide:

#### China Telecom Easy+ SIM-Karte

Einfach zu jeder Zeit nutzbar!

### Wichtige Punkte
- Keine Kaution; automatische Aktivierung für Festlandchina, Macao und Hongkong.
- Kein Vertrag oder Kündigungsgebühr; sofort einsatzbereit nach dem Kauf.
- Enthält eine Macao-Nummer; optionale Festlandchina-Nummer für Dual-Nummer-Nutzung.
- Aufladung online oder mit Wertkarten möglich.

### Tagesgebühren-Optionen
- 2 MOP/Tag: 4 GB Hochgeschwindigkeitsdaten, danach unbegrenzt mit reduzierter Geschwindigkeit; 5.000 Minuten lokale Anrufe.
- 3 MOP/Tag: 10 GB Hochgeschwindigkeitsdaten, danach unbegrenzt mit reduzierter Geschwindigkeit; 5.000 Minuten lokale Anrufe.
- 5 MOP/Tag: 20 GB Hochgeschwindigkeitsdaten, danach unbegrenzt mit reduzierter Geschwindigkeit; 5.000 Minuten lokale Anrufe.

### Zusätzliche Optionen
- Datennutzung in Hongkong: 0,1 MOP/MB.
- Tarifwechsel jederzeit per SMS möglich.

#### Blue Macau SIM-Karte

### Wichtige Punkte
- Keine monatliche Grundgebühr; Nutzung nach Verbrauch.
- Lokale Anrufe: 0,39 MOP/Minute; Internet: 0,1 MOP/MB; SMS: 1 MOP/Nachricht.
- Optionale Datenpakete ohne Ablaufdatum: 10 GB für 98 MOP, 20 GB für 188 MOP, 40 GB für 288 MOP.
- Aufladung alle 180 Tage erforderlich, um aktiv zu bleiben.

#### Kompatible Geräte
- Erfordert ein 4G-Vollnetz- oder China-Telecom-kompatibles Telefon.

Weitere Informationen finden Sie unter [China Telecom Macau](https://www.1888.com.mo/).

---

Diese Karten finden Sie auch auf Taobao:

<div align="center"><img src="/assets/images/macao/easy.jpg" width="300px" /><img/></div>

---

## Shadowsocks-Proxy-Probleme

*03.01.2025*

Zhiwei:

Ich war mit einem Freund grillieren und nutzte Shadowsocks mit einem Server in Singapur als Proxy, um die Great Firewall (GFW) zu umgehen. Während ich draußen 5G nutzte, konnte ich keine Verbindung herstellen, und der Test zeitete aus, als ich versuchte, auf YouTube zuzugreifen. Zu Hause funktioniert Shadowsocks jedoch einwandfrei, wenn ich 4G oder mein China-Telecom-Heimnetzwerk nutze. Warum ist das so?

Mistral:

Es scheint, als hätten Sie Verbindungsprobleme mit Ihrem Shadowsocks-Proxy, wenn Sie draußen 5G nutzen, aber nicht bei 4G oder Ihrem Heimnetzwerk. Dafür könnte es mehrere Gründe geben:

1. Unterschiede in der Netzwerkkonfiguration:
   - **5G-Netzwerk**: Das 5G-Netzwerk könnte andere Konfigurationen oder Einschränkungen als 4G aufweisen. Einige Anbieter könnten strengere Firewall-Regeln oder andere Netzwerkrouten für 5G haben, die die Leistung Ihres Shadowsocks-Proxy beeinträchtigen.
   - **4G-Netzwerk**: Das 4G-Netzwerk könnte entspanntere Einstellungen oder bessere Routen aufweisen, die es Ihrem Shadowsocks-Proxy ermöglichen, korrekt zu funktionieren.

2. Einschränkungen des Internetdienstanbieters (ISP):
   - **Richtlinien der Anbieter**: Verschiedene Anbieter könnten unterschiedliche Richtlinien bezüglich der Nutzung von VPNs oder Proxys haben. Ihr 5G-Anbieter könnte strengere Richtlinien haben, die VPN-Datenverkehr, einschließlich Shadowsocks, blockieren oder drosseln.
   - **Heimnetzwerk**: Ihr Heimnetzwerk, das von China Telecom bereitgestellt wird, könnte weniger Einschränkungen aufweisen, sodass Shadowsocks ohne Probleme funktioniert.

3. Signalstärke und -stabilität:
   - **5G-Signal**: Die Stabilität und Stärke des 5G-Signals kann variieren, insbesondere in Außenbereichen. Schwache oder instabile Signale können Verbindungsprobleme verursachen, einschließlich Zeitüberschreitungen.
   - **4G-Signal**: Das 4G-Signal könnte stabiler und konsistenter sein und eine bessere Verbindung für Ihren Shadowsocks-Proxy bieten.

4. Standort des Proxy-Servers:
   - **Singapur-Server**: Der Standort Ihres Shadowsocks-Servers in Singapur könnte Latenz und Konnektivität beeinflussen. Das 5G-Netzwerk könnte eine höhere Latenz oder weniger optimale Routen zum Singapur-Server aufweisen als das 4G-Netzwerk oder Ihr Heimnetzwerk.

5. Geräteeinstellungen:
   - **Konfiguration**: Stellen Sie sicher, dass die Einstellungen Ihres Geräts für die Nutzung von Shadowsocks korrekt konfiguriert sind. Manchmal kann das Wechseln zwischen Netzwerken (von 5G zu 4G oder Heim-WLAN) dazu führen, dass Einstellungen zurückgesetzt oder geändert werden.
   - **App-Berechtigungen**: Stellen Sie sicher, dass die Shadowsocks-App die notwendigen Berechtigungen hat, um in verschiedenen Netzwerken zu arbeiten.

### Schritte zur Fehlerbehebung:

1. **Netzwerkeinstellungen überprüfen**:
   - Stellen Sie sicher, dass Ihre Shadowsocks-Einstellungen sowohl für 5G- als auch für 4G-Netzwerke korrekt konfiguriert sind.
   - Überprüfen Sie, ob es spezifische Einschränkungen oder Einstellungen in Ihrem 5G-Netzwerk gibt, die den Proxy blockieren könnten.

2. **Verschiedene Server testen**:
   - Versuchen Sie, eine Verbindung zu verschiedenen Shadowsocks-Servern herzustellen, um zu prüfen, ob das Problem spezifisch für den Singapur-Server ist.
   - Überprüfen Sie die Latenz und Stabilität der Verbindung zum Server.

3. **Kontaktieren Sie Ihren Anbieter**:
   - Falls das Problem weiterhin besteht, wenden Sie sich an Ihren 5G-Anbieter, um nach Einschränkungen oder Einstellungen zu fragen, die Ihre Shadowsocks-Verbindung beeinträchtigen könnten.

4. **Software aktualisieren**:
   - Stellen Sie sicher, dass Ihre Shadowsocks-App und die Gerätesoftware auf dem neuesten Stand sind. Manchmal können Updates Verbindungsprobleme beheben.

5. **Alternative Proxys nutzen**:
   - Erwägen Sie die Verwendung alternativer Proxy-Dienste oder VPNs, die möglicherweise eine bessere Kompatibilität mit Ihrem 5G-Netzwerk aufweisen.

Durch systematisches Überprüfen dieser Faktoren sollten Sie die Ursache des Verbindungsproblems identifizieren und eine passende Lösung finden können.

---

**Aktualisierung**:

Tatsächlich nutze ich zu Hause WLAN von China Mobile Communications Corporation, und die IP-Adresse sieht aus wie 120.235.8.xx.

Interessanterweise habe ich inkonsistente Verbindungsmuster beobachtet – während mein Proxy-Server auf mobilen Daten und China-Telecom-Netzwerken normal funktioniert, scheitert die Verbindung gelegentlich, wenn ich mein Heim-WLAN-Netzwerk nutze.