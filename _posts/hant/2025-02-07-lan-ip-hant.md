---
audio: true
lang: hant
layout: post
title: 局域網 IP 掃描器
translated: true
---

## LAN IP 掃描器

這段 Python 腳本掃描區域網絡以查找活躍的 IP 地址。它使用 `ping` 命令檢查主機是否可達，並使用多線程來加快掃描過程。信號量限制同時運行的線程數量，以避免壓垮系統。腳本接收網絡地址（例如，「192.168.1.0/24」）作為輸入，並打印網絡中每個 IP 地址的狀態（活躍或不活躍）。

此腳本有助於識別網絡上的設備，例如在有線橋接模式下運行的 TP-LINK 網狀路由器，方法是掃描活躍的 IP 地址。


```python
import subprocess
import ipaddress
import threading
import os
import socket
import argparse

MAX_THREADS = 50  # 最大線程數

def is_host_up(host, port=None):
    """
    使用 ping 或 telnet 檢查主機是否活躍。
    如果指定端口，則使用 telnet 檢查端口是否打開。
    否則，使用 ping。
    如果主機活躍，則返回 True，否則返回 False。
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
            # -c 1: 只發送 1 個數據包
            # -W 1: 等待 1 秒的響應
            subprocess.check_output(["ping", "-c", "1", "-W", "1", host], timeout=1)
            return True
        except subprocess.CalledProcessError:
            return False
        except subprocess.TimeoutExpired:
            return False

def scan_ip(ip_str, up_ips, port=None):
    """
    掃描單個 IP 地址並打印其狀態。
    """
    if is_host_up(ip_str, port):
        print(f"{ip_str} is up")
        up_ips.append(ip_str)
    else:
        print(f"{ip_str} is down")

def scan_network(network, port=None):
    """
    使用線程掃描網絡以查找活躍的主機，限制同時運行的線程數量。
    """
    print(f"Scanning network: {network}")
    threads = []
    semaphore = threading.Semaphore(MAX_THREADS)  # 限制同時運行的線程數量
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
    parser = argparse.ArgumentParser(description="掃描網絡以查找活躍的主機。")
    parser.add_argument("network", nargs='?', default="192.168.1.0/24", help="要掃描的網絡（例如，192.168.1.0/24）")
    parser.add_argument("-p", "--port", type=int, help="要檢查的端口（可選）")
    args = parser.parse_args()

    network_to_scan = args.network
    port_to_scan = args.port

    up_ips = scan_network(network_to_scan, port_to_scan)
    print("\nLive IPs:")
    for ip in up_ips:
        print(ip)


```

## 跳過區域 IP

腳本識別活躍的 IP 地址。為確保正確的網絡通訊，請驗證代理設置是否已配置為跳過這些區域 IP。

```bash
192.168.0.0/16,10.0.0.0/8,172.16.0.0/12,127.0.0.1,localhost,*.local,timestamp.apple.com,sequoia.apple.com,seed-sequoia.siri.apple.com, 192.168.1.0/16
```
