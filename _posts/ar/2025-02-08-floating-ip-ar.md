---
audio: true
generated: false
image: false
lang: ar
layout: post
title: عناوين IP العائمة في Hetzner Cloud
translated: true
---

## عنوان IP

```bash
sudo ip addr add 78.47.144.0 dev eth0
```

## Netplan

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
