---
audio: false
generated: false
image: false
lang: ar
layout: post
title: مرتشبات macOS التحكم
translated: true
---

## WiFi

```
networksetup -listallhardwareports
sudo networksetup -setairportpower en0 on
sudo networksetup -setairportpower en0 off
```

## Bluetooth

```
brew install blueutil
blueutil --power 0
blueutil --power 1
```

## Volume

```
# Set volume to 50%
osascript -e 'set volume output volume 50'

# Mute the volume
osascript -e 'set volume with output muted'

# Unmute the volume
osascript -e 'set volume without output muted'
```