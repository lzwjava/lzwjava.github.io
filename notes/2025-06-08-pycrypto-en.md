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

---

None of the packages you listed (`aliyunsdkcore`, `aliyun-python-sdk-ecs`, `alibabacloud_vpc20160428`, etc.) directly depend on **`pycrypto`**.  

However, if you're seeing `pycrypto` being installed, it might be an **indirect dependency** of one of these packages. To check which package requires `pycrypto`, run:  

```bash
pip show pycrypto
```  
or  
```bash
pipdeptree | grep -i pycrypto
```  

### Likely Suspects:
1. **Old or deprecated security-related packages** (though none in your list explicitly require `pycrypto`).  
2. **A legacy dependency** from a package like `paramiko` (SSH) or `google-auth`, but these usually switched to `pycryptodome`.  

### Recommended Action:
1. **Replace `pycrypto` with `pycryptodome`** (modern, maintained fork):  
   ```bash
   pip uninstall pycrypto
   pip install pycryptodome
   ```  
   Some packages accept `pycryptodome` as a drop-in replacement.  

2. **Force-reinstall dependencies** to ensure no hidden links:  
   ```bash
   pip install --upgrade --force-reinstall -r requirements.txt
   ```  

3. **If `pycrypto` persists**, audit your environment:  
   ```bash
   pipdeptree --warn silence | grep -i crypto
   ```  

### Key Takeaway:
Your listed packages don’t directly depend on `pycrypto`, but another hidden dependency might. Isolating it with `pipdeptree` will clarify the culprit. If no critical package requires it, **remove `pycrypto` outright**—it’s deprecated and potentially insecure.