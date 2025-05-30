---
title: NVIDIA DKMS Build Issue
lang: en
layout: post
audio: false
translated: false
generated: true
---

It looks like you're encountering an error where the NVIDIA DKMS (Dynamic Kernel Module Support) module is failing to build for your new kernel, `6.8.0-60-generic`. This is a common issue when updating kernels, as the driver module needs to be recompiled for the new kernel version, and sometimes incompatibilities or build issues arise.

The key error messages are:
* `Building module(s)......(bad exit status: 2)`
* `Error! Bad return status for module build on kernel: 6.8.0-60-generic (x86_64)`
* `Consult /var/lib/dkms/nvidia/535.183.06/build/make.log for more information.`
* `dpkg: error processing package linux-image-6.8.0-60-generic (--configure):`
* `E: Sub-process /usr/bin/dpkg returned an error code (1)`

This means the NVIDIA driver version `535.183.06` could not be successfully compiled against kernel `6.8.0-60-generic`, which in turn has stopped the kernel image and related packages from being configured correctly.

Here's how you can try to fix this:

---

### 1. Examine the Build Log 🪵

The most crucial step is to check the detailed build log for specific error messages. This log will tell you *why* the compilation failed.
Open a terminal and run:
```bash
cat /var/lib/dkms/nvidia/535.183.06/build/make.log
```
Look for lines starting with `error:` or `fatal error:`. These will often point to missing files, compiler issues, or incompatibilities with the kernel source. The error `Applying patch disable_fstack-clash-protection_fcf-protection.patch... done.` followed by a build failure suggests the patch might not be fully compatible, or there are other issues the patch doesn't address.

---

### 2. Clean Up and Attempt to Fix Broken Packages 🛠️

First, you can try to let `apt` attempt to fix the broken dependencies and finish configuring packages.
```bash
sudo rm /var/crash/nvidia-dkms-535.0.crash # Remove old crash report to allow new ones
sudo apt --fix-broken install
sudo dpkg --configure -a
```
This might re-trigger the DKMS build. If it fails again, proceed to the next steps.

---

### 3. Ensure Kernel Headers are Correctly Installed 🧠

The DKMS build process requires the correct kernel headers for the kernel you're trying to build against.
```bash
sudo apt update
sudo apt install --reinstall linux-headers-6.8.0-60-generic linux-headers-generic-hwe-22.04
```
If you're not yet running the `6.8.0-60-generic` kernel (e.g., if the update was interrupted), you can specify the headers for your currently running kernel too, but the primary target here is `6.8.0-60-generic`.

---

### 4. Remove the Failing DKMS Module and Reconfigure ♻️

You can manually remove the problematic version of the NVIDIA module from DKMS and then try to let the system rebuild it.
```bash
sudo dkms remove nvidia/535.183.06 --all
```
Then, try to reconfigure the packages again:
```bash
sudo dpkg --configure -a
sudo apt update && sudo apt upgrade
```
This process should prompt DKMS to try and rebuild the module for the `6.8.0-60-generic` kernel.

---

### 5. Reinstall the NVIDIA Driver 💻

If the module still fails to build, the driver version `535.183.06` might have compatibility issues with kernel `6.8.0-60-generic`.

* **Purge the current problematic driver:**
    ```bash
    sudo apt-get purge nvidia-dkms-535 nvidia-driver-535
    sudo apt autoremove
    sudo apt clean
    ```

* **Install a suitable driver:**
    You can let Ubuntu try to install the recommended driver:
    ```bash
    sudo ubuntu-drivers autoinstall
    ```
    Alternatively, you can try to install the same version (if it's deemed compatible by the repositories now) or a potentially newer, more compatible version. For instance, to try installing the 535 series driver again:
    ```bash
    sudo apt update
    sudo apt install nvidia-driver-535
    ```
    (The package manager should pick the appropriate DKMS version.)

    After this, the system will attempt to build the DKMS module again.

---

### 6. Consider a Newer NVIDIA Driver Version 🚀

Kernel 6.8 is relatively new. It's possible that the NVIDIA 535 series driver has limitations with this kernel version. You might need a newer driver series (e.g., 545, 550, or newer, if available in your repositories or via NVIDIA's official channels/PPAs).

* Check available drivers:
    ```bash
    sudo apt search nvidia-driver
    ```
* If a newer proprietary driver is available (e.g., `nvidia-driver-550`), you could try installing that instead of `nvidia-driver-535`.
    ```bash
    sudo apt install nvidia-driver-VERSION_NUMBER # Replace VERSION_NUMBER
    ```

---

### 7. If You're Stuck in a Boot Loop or Have No GUI 📉

If the system fails to boot into a graphical environment:
* Boot into recovery mode or an older kernel (usually accessible from the GRUB menu during startup).
* Once in a command-line environment, you can try the steps above.
* If you need to temporarily use an open-source driver to get a GUI back while you fix the NVIDIA driver:
    ```bash
    sudo apt-get purge nvidia*
    sudo apt autoremove
    sudo apt install xserver-xorg-video-nouveau
    sudo reboot
    ```
    Then, attempt the NVIDIA driver installation again.

---

**Key takeaway:** The content of `/var/lib/dkms/nvidia/535.183.06/build/make.log` is very important. If the steps above don't work, the errors in that file will provide more specific clues, and you may need to search online for those specific errors in conjunction with your kernel version and NVIDIA driver version.