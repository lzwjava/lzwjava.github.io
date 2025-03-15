---
title: Streaming MKV Files from Nginx with VLC
lang: en
layout: post
audio: false
translated: false
generated: true
---

Since you have an Nginx server serving `.mkv` files (e.g., at `http://192.168.1.27/movies/`), and you want to view them from a Mac without downloading the entire file, you’re looking to **stream** the videos. Nginx can serve files in a way that supports HTTP range requests (which it does by default), allowing media players to stream rather than download fully. Here’s how to do it, along with suitable tools for macOS.

### Prerequisites
- Your Nginx config (e.g., `alias /var/www/movies/; autoindex on;`) is working, and `http://192.168.1.27/movies/` lists files.
- The `.mkv` files are accessible over the network (tested from another machine).

### Tools to Stream `.mkv` Files on macOS
You need a media player that supports streaming via HTTP and handles `.mkv` files well. Here are the best options:

#### 1. VLC Media Player (Free, Recommended)
VLC is a versatile, open-source player that supports streaming `.mkv` files over HTTP without downloading the whole file (it uses range requests).
- **Install**:
  - Download from [videolan.org](https://www.videolan.org/vlc/).
  - Install it on your Mac.
- **Stream**:
  1. Open VLC.
  2. Press `Cmd + N` (or go to `File > Open Network`).
  3. Enter the URL, e.g., `http://192.168.1.27/movies/yourfile.mkv`.
  4. Click `Open`.
- **Why It Works**: VLC buffers only what’s needed, letting you seek and play without downloading the entire file.

#### 2. IINA (Free, macOS-Native)
IINA is a modern, macOS-specific player with excellent `.mkv` support and streaming capabilities.
- **Install**:
  - Download from [iina.io](https://iina.io/) or `brew install iina` (with Homebrew).
- **Stream**:
  1. Open IINA.
  2. Press `Cmd + U` (or `File > Open URL`).
  3. Enter `http://192.168.1.27/movies/yourfile.mkv`.
  4. Click `OK`.
- **Why It Works**: Lightweight, supports HTTP streaming, and integrates nicely with macOS.

#### 3. QuickTime Player (Built-in, Limited)
macOS’s default QuickTime Player can stream some formats, but `.mkv` support is spotty without extra codecs.
- **Try It**:
  1. Open QuickTime Player.
  2. Press `Cmd + U` (or `File > Open Location`).
  3. Enter `http://192.168.1.27/movies/yourfile.mkv`.
  4. Click `Open`.
- **Caveat**: If it doesn’t work, install Perian (an old codec pack) or use VLC/IINA instead.

#### 4. Browser (Safari/Chrome, Simplest)
Modern browsers can stream `.mkv` files directly if they’re encoded with supported codecs (e.g., H.264 video, AAC audio).
- **How**:
  1. Open Safari or Chrome on your Mac.
  2. Go to `http://192.168.1.27/movies/`.
  3. Click `yourfile.mkv`.
- **Why It Works**: Browsers use HTML5 video tags and range requests for streaming.
- **Limitation**: If the `.mkv` uses unsupported codecs (e.g., VP9, Opus), it won’t play—fall back to VLC or IINA.

### Ensure Nginx Supports Streaming
Nginx handles range requests by default, which is what enables streaming. To confirm:
- Check your config doesn’t disable this (e.g., no `limit_rate` or custom headers blocking ranges).
- Test with VLC or IINA—if you can seek (e.g., jump to 5 minutes in), streaming is working.

### Recommended Workflow
1. **Use VLC** (it’s the most reliable):
   - Install VLC.
   - Open `http://192.168.1.27/movies/yourfile.mkv` via `Cmd + N`.
   - Play, pause, or seek as needed.
2. **Directory Browsing**:
   - Visit `http://192.168.1.27/movies/` in Safari/Chrome to see the file list (thanks to `autoindex on;`).
   - Copy the URL of `yourfile.mkv` and paste it into VLC or IINA.

### Troubleshooting
- **Buffering Issues**: Slow network or large `.mkv` files might lag—ensure your LAN is stable (e.g., Wi-Fi isn’t dropping).
- **Codec Errors**: If VLC says "unsupported format," the `.mkv` might use rare codecs—try re-encoding it with HandBrake to H.264/AAC.
- **Connection Refused**: Revisit firewall settings on the server (`sudo ufw allow 80` or equivalent).

With VLC or IINA, you’ll be streaming your `.mkv` files from your Mac in no time without downloading them fully. Let me know if you hit any snags!