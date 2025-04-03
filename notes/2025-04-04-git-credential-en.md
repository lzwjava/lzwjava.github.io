---
title: Git Credential Manager
lang: en
layout: post
audio: false
translated: false
generated: true
---

Git Credential Manager (GCM) is a secure Git credential helper that stores and manages authentication credentials for HTTPS Git repositories. It works with services like GitHub, GitLab, Bitbucket, and Azure DevOps.

---

## **1. Install Git Credential Manager**
GCM is included with Git for Windows and the official Git distributions for macOS and Linux. If it's not installed, download it from:

🔗 **[Git Credential Manager on GitHub](https://github.com/GitCredentialManager/git-credential-manager)**

### **Check if GCM is installed**
Run:
```sh
git credential-manager version
```
If it's installed, you'll see a version number. If not, install it manually.

---

## **2. Configure Git to Use GCM**
Run the following command:
```sh
git config --global credential.helper manager
```
For macOS/Linux, use:
```sh
git config --global credential.helper manager-core
```

To check the current credential helper:
```sh
git config --global credential.helper
```

---

## **3. Authenticate with a Git Server**
Once configured, the first time you interact with a remote repository over HTTPS (e.g., `git clone`, `git pull`), GCM will prompt you for credentials.

- If using GitHub, GitLab, or Bitbucket, GCM will open a browser for OAuth authentication.
- If using a personal access token (PAT), enter it instead of a password.

---

## **4. Store and Manage Credentials**
GCM securely stores credentials in the OS's credential store:
- **Windows**: Windows Credential Manager  
- **macOS**: macOS Keychain  
- **Linux**: GPG-encrypted file (`~/.git-credentials` or `~/.gitconfig`)

To manually add a credential:
```sh
git credential approve
```

To remove a stored credential:
```sh
git credential reject https://github.com
```

To clear all credentials:
```sh
git credential reject
```

---

## **5. Using Git Credential Manager with Different Git Providers**
### **GitHub**
Use a **Personal Access Token (PAT)** instead of a password:
```sh
git credential reject https://github.com
git pull
```
You'll be prompted to log in and enter your token.

### **GitLab**
For GitLab, use OAuth or a **PAT**:
```sh
git credential reject https://gitlab.com
git pull
```

### **Azure DevOps**
Use a **PAT** or Azure authentication.

---

## **6. Debugging Issues**
If credentials are not saved or retrieved correctly:
1. Check the credential helper:
   ```sh
   git config --global credential.helper
   ```
2. Reset Git Credential Manager:
   ```sh
   git credential reject https://your-git-service.com
   ```
3. Reinstall GCM if needed.

Would you like help configuring it for a specific service? 🚀