---
audio: false
generated: false
image: false
lang: de
layout: post
title: Schwebende IPs und Verwaltung von Netzwerkschnitstellen
translated: true
---

### Inhaltsverzeichnis

1. [Floating IPs in Hetzner Cloud](#floating-ips-in-hetzner-cloud)
   - IP-Konfigurationsbefehle
   - Netplan-Konfiguration einrichten
   - Netzwerk-Konfigurationsdateien

2. [Netzwerkschnittstellen-Verwaltung](#network-interface-management)
   - Löschen von TUN-Schnittstellen
   - Überwachung des Schnittstellenstatus
   - Netzwerk-Fehlerbehebung

3. [LAN-IP-Scanner](#lan-ip-scanner)
   - Python-Netzwerk-Scan-Skript
   - Multithread-Host-Erkennung
   - Port-Scan-Funktionen
   - Geräteidentifikation in lokalen Netzwerken

4. [Umgehen lokaler IPs](#bypassing-local-ips)
   - Proxy-Konfiguration für lokale Netzwerke
   - Subnetzmaske-Berechnungen
   - Netzwerkbereichsplanung

5. [SSH-Verbindung mit IPv6-Adresse](#ssh-connection-using-ipv6-address)
   - IPv6-SSH-Konfiguration
   - SSH-Konfigurationsdatei-Verwaltung
   - ProxyCommand-Einrichtung für verschiedene Adresstypen
   - Leistungsoptimierung

6. [WLAN-Geschwindigkeit verbessern](#improving-wifi-speed)
   - Leistung: Alt vs. Neues Modem
   - Netzwerkeinrichtungskonfigurationen
   - Kabelgebundene vs. drahtlose Bridge-Modi
   - Engpassanalyse im Netzwerk

7. [OpenWrt Zurücksetzen](#openwrt-reset)
   - Zurücksetzen über die Weboberfläche
   - Zurücksetzen über die Kommandozeile
   - Werkseinstellungen wiederherstellen

---

## Floating IPs in Hetzner Cloud

### IP

```bash
sudo ip addr add 78.47.144.0 dev eth0
```

### Netplan

```bash
touch /etc/netplan/60-floating-ip.yaml
nano /etc/netplan/60-floating-ip.yaml
```

```yaml
network:
   version: 2
   renderer: networkd
   ethernets:
     eth0:
       addresses:
       - 78.47.144.0/32
```

```bash
sudo netplan apply
```

---

## Netzwerkschnittstellen-Verwaltung

Löschen der `tun`-Schnittstelle.

```bash
$ ipconfig

outline-tun0: flags=4305<UP,POINTOPOINT,RUNNING,NOARP,MULTICAST>  mtu 1500
        inet 10.0.85.1  netmask 255.255.255.255  destination 10.0.85.1
        unspec 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00  txqueuelen 500  (UNSPEC)
        RX packets 208  bytes 8712 (8.7 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 385  bytes 23322 (23.3 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

$ sudo ip link delete outline-tun0
```

---

## LAN-IP-Scanner

Dieses Python-Skript scannt ein lokales Netzwerk nach aktiven IP-Adressen. Es verwendet den `ping`-Befehl, um zu überprüfen, ob ein Host erreichbar ist, und nutzt Multithreading, um den Scan-Prozess zu beschleunigen. Ein Semaphor begrenzt die Anzahl der gleichzeitigen Threads, um das System nicht zu überlasten. Das Skript nimmt eine Netzwerkadresse (z. B. "192.168.1.0/24") als Eingabe und gibt aus, welche IP-Adressen im Netzwerk aktiv oder inaktiv sind.

Dieses Skript hilft dabei, Geräte im Netzwerk zu identifizieren, z. B. einen TP-LINK-Mesh-Router, der im kabelgebundenen Bridge-Modus betrieben wird, indem es nach aktiven IP-Adressen scannt.

```python
import subprocess
import ipaddress
import threading
import os
import socket
import argparse

MAX_THREADS = 50  # Maximale Anzahl der zu verwendenden Threads

def is_host_up(host, port=None):
    """
    Überprüft, ob ein Host erreichbar ist, mithilfe von ping oder telnet.
    Wenn ein Port angegeben ist, wird telnet verwendet, um zu prüfen, ob der Port offen ist.
    Andernfalls wird ping verwendet.
    Gibt True zurück, wenn der Host erreichbar ist, sonst False.
    """
    if port:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            if result == 0:
                return True
            else:
                return False
        except socket.error as e:
            return False
        finally:
            sock.close()
    else:
        try:
            # -c 1: Nur 1 Paket senden
            # -W 1: 1 Sekunde auf Antwort warten
            subprocess.check_output(["ping", "-c", "1", "-W", "1", host], timeout=1)
            return True
        except subprocess.CalledProcessError:
            return False
        except subprocess.TimeoutExpired:
            return False

def scan_ip(ip_str, up_ips, port=None):
    """
    Scannt eine einzelne IP-Adresse und gibt deren Status aus.
    """
    if is_host_up(ip_str, port):
        print(f"{ip_str} ist aktiv")
        up_ips.append(ip_str)
    else:
        print(f"{ip_str} ist inaktiv")

def scan_network(network, port=None):
    """
    Scannt ein Netzwerk nach aktiven Hosts mithilfe von Threads und begrenzt die Anzahl der gleichzeitigen Threads.
    """
    print(f"Scanne Netzwerk: {network}")
    threads = []
    semaphore = threading.Semaphore(MAX_THREADS)  # Begrenzt die Anzahl der gleichzeitigen Threads
    up_ips = []

    def scan_ip_with_semaphore(ip_str):
        semaphore.acquire()
        try:
            scan_ip(ip_str, up_ips, port)
        finally:
            semaphore.release()

    for ip in ipaddress.IPv4Network(network):
        ip_str = str(ip)
        thread = threading.Thread(target=scan_ip_with_semaphore, args=(ip_str,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return up_ips

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scannt ein Netzwerk nach aktiven Hosts.")
    parser.add_argument("network", nargs='?', default="192.168.1.0/24", help="Das zu scannende Netzwerk (z. B. 192.168.1.0/24)")
    parser.add_argument("-p", "--port", type=int, help="Der zu prüfende Port (optional)")
    args = parser.parse_args()

    network_to_scan = args.network
    port_to_scan = args.port

    up_ips = scan_network(network_to_scan, port_to_scan)
    print("\nAktive IPs:")
    for ip in up_ips:
        print(ip)
```

---

## Umgehen lokaler IPs

Das Skript identifiziert aktive IP-Adressen. Um eine ordnungsgemäße Netzwerkkommunikation sicherzustellen, muss überprüft werden, ob die Proxy-Einstellungen so konfiguriert sind, dass diese lokalen IPs umgangen werden.

```bash
192.168.0.0/16,10.0.0.0/8,172.16.0.0/12,127.0.0.1,localhost,*.local,timestamp.apple.com,sequoia.apple.com,seed-sequoia.siri.apple.com, 192.168.1.0/16
```

---

## Subnetzmasken

Mein zweiter Rechner befindet sich normalerweise unter 192.168.1.16.

Daher funktioniert der folgende Befehl:

```bash
python scripts/ip_scan.py 192.168.1.0/27 -p 22
```

denn 32 - 27 = 5, 2^5 = 32, daher werden die IP-Adressen von `192.168.1.0` bis `192.168.1.31` geprüft.

Es funktioniert jedoch nicht mit `192.168.1.0/28`, da 2^4 = 16, daher werden nur die IP-Adressen von `192.168.1.0` bis `192.168.1.15` geprüft, was `192.168.1.16` nicht abdeckt.

---

## SSH-Verbindung mit IPv6-Adresse

Ich versuche, mich mit einer Maschine in der Hetzner Cloud über IPv6 zu verbinden. `ssh 2a01:4f8:c17:2000::/64` funktioniert nicht, aber `ssh root@2a01:4f8:c17:2000::1` schon.

Die IPv6-Adresse wurde aus der Hetzner Cloud-Konsole kopiert.

Die Datei `~/.ssh/config` kann so konfiguriert werden, dass unterschiedliche Proxy-Regeln für IPv4- und IPv6-Adressen gelten. Diese Einrichtung ermöglicht es, für IPv4-Adressen ein Proxy-Kommando zu verwenden, während IPv6-Adressen anders behandelt werden.

```bash
Host 192.168.1.*
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
Host *.*.*.*
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
    ProxyCommand corkscrew localhost 7890 %h %p
Host *
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
```

Bei der Ausführung von `ssh root@192.168.1.3` zeigt die folgende Ausgabe, dass der SSH-Client Konfigurationsoptionen aus der Datei `~/.ssh/config` anwendet:

```bash
debug1: Lesen der Konfigurationsdaten aus /Users/lzwjava/.ssh/config
debug1: /Users/lzwjava/.ssh/config Zeile 1: Optionen für 192.168.1.* anwenden
debug1: /Users/lzwjava/.ssh/config Zeile 5: Optionen für *.*.*.* anwenden
debug2: add_identity_file: doppelter Schlüssel ~/.ssh/id_rsa wird ignoriert
debug1: /Users/lzwjava/.ssh/config Zeile 10: Optionen für * anwenden
debug2: add_identity_file: doppelter Schlüssel ~/.ssh/id_rsa wird ignoriert
debug1: Lesen der Konfigurationsdaten aus /etc/ssh/ssh_config
debug1: /etc/ssh/ssh_config Zeile 21: include /etc/ssh/ssh_config.d/* keine Dateien gefunden
debug1: /etc/ssh/ssh_config Zeile 54: Optionen für * anwenden
debug2: resolve_canonicalize: Hostname 192.168.1.3 ist eine Adresse
debug3: erweitert UserKnownHostsFile '~/.ssh/known_hosts' zu '/Users/lzwjava/.ssh/known_hosts'
debug3: erweitert UserKnownHostsFile '~/.ssh/known_hosts2' zu '/Users/lzwjava/.ssh/known_hosts2'
debug1: Authenticator-Anbieter $SSH_SK_PROVIDER konnte nicht aufgelöst werden; deaktivieren
debug3: channel_clear_timeouts: Löschen der Timeouts
debug1: Führe Proxy-Kommando aus: exec corkscrew localhost 7890 192.168.1.3 22
```

Die SSH-Verbindungsgeschwindigkeit war spürbar langsam, daher kehrte ich zur folgenden einfacheren Konfiguration zurück:

```bash
Host 192.168.1.*
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
Host *
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
    ProxyCommand corkscrew localhost 7890 %h %p
```

Das Problem tritt auf, wenn IPv6-Adressen mit der `ProxyCommand corkscrew localhost 7890 %h %p`-Direktive verwendet werden, da dieses Proxy-Kommando IPv6-Adressen möglicherweise nicht korrekt verarbeitet.

Die obige Konfiguration funktioniert immer noch nicht. Die folgende funktioniert jedoch:

```bash
Host 192.168.1.*
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
Host !192.*.*.*
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
    ProxyCommand corkscrew localhost 7890 %h %p
Host *
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
```

---

## WLAN-Geschwindigkeit verbessern

### Probleme mit altem Modem

Bei meinen Eltern zu Hause ist das Modem etwa 10 Jahre alt. Die ursprüngliche Netzwerkeinrichtung sah so aus:

Modem -> 3m drahtlos -> TP-Link AX3000 (drahtloser Bridge-Modus) -> 2m, eine Wand, drahtlos -> Laptop

Dies ergab eine niedrige Download-Geschwindigkeit mit einem Speedtest-Ergebnis von nur 10 Mbps.

Eine verbesserte Einrichtung bestand darin, eine kabelgebundene Verbindung zu verwenden:

Modem -> 2m Kabel -> TP-Link AX3000 (kabelgebundener Bridge-Modus) -> 4m drahtlos, eine Wand -> Laptop

Damit verbesserte sich die Download-Geschwindigkeit auf bis zu 90 Mbps.

### Leistung mit neuem Modem

In meinem eigenen Haus ist das Modem neu, und der TP-Link-Router funktioniert im drahtlosen Bridge-Modus gut. Die Netzwerkeinrichtung ist:

Modem -> 4m drahtlos -> TP-Link AX3000 (drahtloser Bridge-Modus) -> 2m drahtlos -> Laptop

Die Netzwerkqualität ist gut.

### Tipps zur Fehlerbehebung

Es gibt keine universelle Lösung, um die WLAN-Geschwindigkeit zu verbessern. Ein guter Ansatz besteht darin, ein Kabel zu verwenden, um jeden Teil des Netzwerks zu testen und Engpässe zu identifizieren. Vergleichen Sie die Geschwindigkeiten bei kabelgebundener Verbindung und WLAN. Versuchen Sie auch, Geräte direkt mit einem Kabel zu verbinden, um zu sehen, ob sich die Leistung verbessert.

---

## OpenWrt Zurücksetzen

### Zurücksetzen über die Weboberfläche

Es wird empfohlen, den Router über ein Ethernet-Kabel zu verbinden. Nach einem Reset wird die WLAN-SSID auf die Standardwerte zurückgesetzt, was möglicherweise nicht den Erwartungen entspricht.

### Zurücksetzen über die Kommandozeile (SSH)

OpenWrt kann über die Kommandozeilenschnittstelle (SSH) auf die Werkseinstellungen zurückgesetzt werden. So geht’s:

1. Verbinden Sie sich über SSH mit Ihrem OpenWrt-Router.
2. Führen Sie den folgenden Befehl aus:

    ```bash
    root@OpenWrt:~# firstboot
    Dies wird alle Einstellungen löschen und installierte Pakete entfernen. Sind Sie sicher? [N/y]
    y
    /dev/ubi0_1 ist als /overlay eingehängt, nur Dateien werden gelöscht
    root@OpenWrt:~# reboot
    ```
3. Der Router startet neu mit den Werkseinstellungen.

**Erklärung der Befehle:**

* `firstboot`: Dieser Befehl startet den Reset-Prozess und löscht alle Konfigurationen und installierten Pakete.
* `reboot`: Dieser Befehl startet den Router neu und wendet den Reset an.