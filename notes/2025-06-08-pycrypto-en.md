---
title: Error Building pycrypto
lang: en
layout: post
audio: false
translated: false
generated: true
---

The error occurs because the `pycrypto` package requires the Python header file `longintrepr.h`, which is part of Python's development headers. This file is missing in your Python 3.13 environment. Here's how to resolve it:

### Solution:
1. **Install Python Development Headers**  
   Install the Python 3.13 development package for your OS. On Ubuntu/Debian, run:
   ```bash
   sudo apt-get install python3.13-dev
   ```

2. **Reinstall `pycrypto`**  
   After installing headers, retry the installation:
   ```bash
   pip install pycrypto
   ```

---

### Alternative Recommendations:
**Option 1: Replace `pycrypto` with `pycryptodome` (Preferred)**  
`pycrypto` is deprecated and unmaintained. Switch to the maintained fork `pycryptodome`, which is API-compatible:
```bash
pip uninstall pycrypto
pip install pycryptodome
```

**Option 2: Use a Legacy Python Version**  
If compatibility allows, use Python ≤3.9 (where `pycrypto` is known to work):
```bash
# Example using pyenv
pyenv install 3.9.18
pyenv local 3.9.18
pip install -r requirements.txt
```

---

### Why This Happened:
- `longintrepr.h` is an internal Python header used for integer representation. It's included in Python dev packages but not standard installations.
- Python 3.13 may have structural changes that break legacy packages like `pycrypto` (last updated in 2014).
- The deprecation warning indicates `pycrypto` uses outdated build methods unsupported in newer `pip` versions.

### Prevention:
1. **Avoid `pycrypto`**: Use `pycryptodome` for cryptography needs.
2. **Pin Python Versions**: For legacy projects, use Python ≤3.9 in environments like Docker/Venv.
3. **Check Dependencies**: Use `pip check` to identify incompatible packages.