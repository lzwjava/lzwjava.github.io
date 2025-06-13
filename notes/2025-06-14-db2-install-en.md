---
title: Install Db2 Server on Ubuntu
lang: en
layout: post
audio: false
translated: false
generated: true
---

Installing an IBM Db2 database server on Ubuntu involves several steps, primarily downloading the Db2 Community Edition, preparing your system, and then running the installer.

**Important Notes Before You Begin:**

* **Db2 Community Edition:** This is a free, full-featured version of Db2 suitable for development and small production environments. You'll need an IBM account to download it.
* **System Requirements:** Ensure your Ubuntu system meets the prerequisites. For Db2 11.5, Ubuntu 22.04 LTS (x64) is generally supported. You'll need at least 2 GB of RAM and 2 GB of disk space for the software installation, plus more for your databases.
* **Root User:** While non-root installations are possible, it's generally recommended to install Db2 as the `root` user to prevent issues with future upgrades. You'll typically use `sudo` for commands.
* **Graphical vs. Console Installation:** Db2 offers a graphical setup wizard (`db2setup`) and a console-based installer (`db2_install`). The console-based installer is often preferred for server environments or when using SSH.

Here's a general outline of the installation process:

**1. Download the Db2 Community Edition Installation Package:**

* Go to the IBM Db2 Database download page. You might find it via a search for "Db2 Community Edition download" or "IDUG Db2 Downloads."
* You will need to sign in with your IBM credentials (or create a free IBM account if you don't have one).
* Locate and download the Linux x64 server edition (e.g., `v11.5.x_linuxx64_server_dec.tar.gz`).

**2. Prepare Your Ubuntu System:**

* **Enable 32-bit Architecture (if required for older versions/components):**
    ```bash
    sudo dpkg --add-architecture i386
    sudo apt-get update
    ```
* **Install Prerequisites/Dependencies:** Db2 often requires certain libraries. Common ones include:
    * `libstdc++6:i386` (for 32-bit compatibility)
    * `libpam0g:i386` (for 32-bit compatibility)
    * `libaio1`
    ```bash
    sudo apt-get install libstdc++6:i386 libpam0g:i386 libaio1 -y
    ```
    (Note: The exact packages might vary slightly depending on your Ubuntu version and the Db2 version you're installing. The `db2prereqcheck` utility will help identify missing ones.)
* **Create a directory for the installation:**
    ```bash
    sudo mkdir /home/db2install
    ```
    (You can choose a different location if preferred.)

**3. Extract the Installation Package:**

* Move the downloaded `.tar.gz` file to the directory you created (e.g., `/home/db2install`).
* Navigate to that directory:
    ```bash
    cd /home/db2install
    ```
* Extract the file:
    ```bash
    tar -xzvf v11.5.x_linuxx64_server_dec.tar.gz
    ```
    This will typically create a `server_dec` directory.
* Change into the extracted directory:
    ```bash
    cd server_dec
    ```

**4. Run Prerequisite Check (Highly Recommended):**

* Before installing, run the `db2prereqcheck` utility to ensure all system requirements are met.
    ```bash
    sudo ./db2prereqcheck -v 11.5.0.0
    ```
    (Adjust the version number `-v 11.5.0.0` to match your downloaded Db2 version.)
* Address any reported missing packages or configurations before proceeding.

**5. Install Db2 Server:**

* **Using the Console-Based Installer (`db2_install`):** This is generally recommended for server installations.
    ```bash
    sudo ./db2_install
    ```
    * The installer will prompt you to accept the license agreement. Type `yes` and press Enter.
    * It will ask for the default install directory (e.g., `/opt/ibm/db2/V11.5`). It's usually wise to accept the default.
    * When prompted "What exactly do you want to install?", type `server` and press Enter.
    * The installation process will proceed. It might take some time.
* **Using the Graphical Installer (`db2setup`):** If you have an X Window System (GUI) forwarded to your local workstation (e.g., via SSH with X11 forwarding enabled), you can use the graphical installer:
    ```bash
    sudo ./db2setup
    ```
    * This will launch the Db2 Setup wizard.
    * Click "New Install" and follow the on-screen prompts, selecting "Db2 Server Edition" during the process.

**6. Review the Installation Log:**

* After the installation completes, review the log files for any errors or warnings.
    * For root installations, the log file is typically `/tmp/db2setup.log` or `/tmp/db2_install.log.XXXX`.
    * An extended log file is often found in `/opt/ibm/db2/Vrr.m/install/logs/db2install.history`.

**7. Post-Installation Steps:**

* **Create a Db2 Instance:** After installing the software, you need to create a Db2 instance. The installer usually guides you through this or provides instructions.
    * You'll typically create a new user for the Db2 instance owner (e.g., `db2inst1`) and a fenced user (e.g., `db2fenc1`).
    * You'll then run `db2icrt` to create the instance.
    * Example (after logging in as root or sudo):
        ```bash
        # Create instance owner user (e.g., db2inst1)
        sudo useradd -m db2inst1 -g db2iadm1 -s /bin/bash # Adjust group if necessary
        sudo passwd db2inst1

        # Create fenced user (e.g., db2fenc1)
        sudo useradd -m db2fenc1 -g db2fadm1 -s /bin/bash # Adjust group if necessary
        sudo passwd db2fenc1

        # Navigate to the instance creation tool
        cd /opt/ibm/db2/V11.5/instance # Adjust version

        # Create the instance
        sudo ./db2icrt -u db2fenc1 db2inst1
        ```
* **Start the Db2 Instance:**
    ```bash
    su - db2inst1
    db2start
    ```
* **Create a Sample Database (Optional but recommended for testing):**
    ```bash
    su - db2inst1
    db2sampl
    ```
* **Verify the Installation:**
    ```bash
    su - db2inst1
    db2 list db directory
    db2 connect to sample
    db2 list tables
    ```

**Troubleshooting Tips:**

* **Check logs:** Always refer to the installation log files for specific error messages.
* **Prerequisites:** Most installation failures are due to unmet prerequisites. Double-check the `db2prereqcheck` output and ensure all required packages are installed.
* **Permissions:** Ensure you have appropriate permissions (using `sudo` or operating as `root`) during the installation process.
* **Documentation:** Refer to the official IBM Db2 documentation for your specific version, as details can vary slightly.

By following these steps, you should be able to successfully install an IBM Db2 database server on your Ubuntu system.