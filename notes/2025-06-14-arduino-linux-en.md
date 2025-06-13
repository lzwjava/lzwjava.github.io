---
title: Installing Arduino IDE on Ubuntu
lang: en
layout: post
audio: false
translated: false
generated: true
---

To install the Arduino IDE on Ubuntu Linux, follow these steps:

1. **Download the Arduino IDE**:
   - Visit the official Arduino website at [https://www.arduino.cc/en/software](https://www.arduino.cc/en/software).
   - Under the "Arduino IDE" section, select the "Linux 64 bits" download option (or the appropriate version for your system, e.g., Linux ARM for Raspberry Pi).

2. **Extract the Downloaded File**:
   - The downloaded file is a compressed `.tar.xz` archive (e.g., `arduino-1.8.19-linux64.tar.xz`).
   - Open a terminal and navigate to the download directory (e.g., `cd ~/Downloads`).
   - Extract the file using:
     ```bash
     tar -xf arduino-*.tar.xz
     ```
   - This creates a folder like `arduino-1.8.19`.

3. **Move to an Appropriate Directory (Optional)**:
   - For system-wide access, move the extracted folder to `/opt` (requires superuser privileges):
     ```bash
     sudo mv arduino-1.8.19 /opt/arduino
     ```

4. **Run the Installation Script**:
   - Navigate to the Arduino folder:
     ```bash
     cd /opt/arduino
     ```
   - Run the installation script:
     ```bash
     sudo ./install.sh
     ```
   - This creates a desktop shortcut and sets up the necessary permissions.

5. **Add Your User to the Dialout Group**:
   - To access the Arduino board via the serial port, add your user to the `dialout` group:
     ```bash
     sudo usermod -a -G dialout $USER
     ```
   - Log out and back in, or reboot for the group change to take effect.

6. **Launch the Arduino IDE**:
   - If you ran the `install.sh` script, you can launch the IDE from the application menu or by searching for "Arduino IDE."
   - Alternatively, run it directly from the terminal:
     ```bash
     /opt/arduino/arduino
     ```

7. **Update Permissions for the Arduino Board (if needed)**:
   - When connecting your Arduino, ensure it’s detected (e.g., `/dev/ttyACM0` or `/dev/ttyUSB0`).
   - If you encounter permission issues, set the correct permissions:
     ```bash
     sudo chmod a+rw /dev/ttyACM0
     ```
   - Replace `/dev/ttyACM0` with the appropriate port.

8. **Verify Installation**:
   - Connect your Arduino board via USB.
   - Open the IDE, go to **Tools > Board** and select your Arduino model (e.g., Arduino Uno).
   - Go to **Tools > Port** and select the port (e.g., `/dev/ttyACM0`).
   - Try uploading a sample sketch (e.g., **File > Examples > 01.Basics > Blink**) to confirm everything works.

**Alternative: Install via Snap or Flatpak**:
- **Snap**:
  ```bash
  sudo snap install arduino
  ```
- **Flatpak**:
  ```bash
  sudo flatpak install flathub cc.arduino.ArduinoIDE
  ```
- These methods simplify installation but may have limitations with permissions or board detection.

**Notes**:
- Ensure you have Java installed, as the Arduino IDE requires it. Install it if needed:
  ```bash
  sudo apt update
  sudo apt install default-jre
  ```
- For the latest version or troubleshooting, check the Arduino forums or the [official documentation](https://www.arduino.cc/en/Guide/Linux).

If you encounter issues, let me know your Ubuntu version or specific error for tailored help!