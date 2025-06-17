---
title: Stable Diffusion Proxy Issue
lang: en
layout: post
audio: false
translated: false
generated: true
---

Based on the error and your environment, here's how to fix the "Unknown scheme for proxy URL" issue:

### Solution:
The error occurs because **`httpx` doesn't support `socks://` proxies by default**. You have two options:

#### Option 1: Remove the SOCKS Proxy Reference
1. Check your environment variables for stray proxy settings:
   ```bash
   env | grep -i proxy
   ```
   Look for `socks://` references (especially `ALL_PROXY` or `http_proxy`).

2. Unset the problematic variable (replace `VAR_NAME` with the actual name found above):
   ```bash
   unset VAR_NAME  # e.g., unset ALL_PROXY
   ```

#### Option 2: Add SOCKS Support to `httpx`
1. Activate your Python virtual environment:
   ```bash
   source /home/lzw/Projects/stable-diffusion-webui/venv/bin/activate
   ```

2. Install required dependencies:
   ```bash
   pip install -U "httpx[socks]"
   ```

3. Deactivate the environment:
   ```bash
   deactivate
   ```

### Why this happens:
- Your main proxies (`HTTP_PROXY/HTTPS_PROXY`) use `http://` (supported), but something (likely another app/script) is setting a `socks://` proxy that `httpx` can't handle without extra packages.
- The stack trace shows Gradio/`httpx` is trying to use `socks://127.0.0.1:7891`, which isn't in your `checkproxy` output.

### Verification:
After fixing, run:
```bash
./webui.sh
```
The SOCKS proxy error should disappear.

> 💡 **Note**: If you didn't intentionally set a SOCKS proxy, investigate applications that might auto-configure proxies (e.g., VPNs, network managers, or shell config files like `~/.bashrc`).