---
audio: false
generated: false
image: false
lang: hant
layout: post
title: 重設 OpenWrt
translated: true
---

## 透過網頁介面重設

建議使用乙太網路線連接至路由器。重設後，Wi-Fi 的 SSID 將恢復為預設設定，可能與您預期的不同。

## 透過命令列（SSH）重設

您可以使用命令列介面（SSH）將 OpenWrt 重設為預設設定。步驟如下：

1. 透過 SSH 連接至 OpenWrt 路由器。
2. 執行以下指令：

    ```bash
    root@OpenWrt:~# firstboot
    This will erase all settings and remove any installed packages. Are you sure? [N/y]
    y
    /dev/ubi0_1 is mounted as /overlay, only erasing files
    root@OpenWrt:~# reboot
    ```
3. 路由器將以預設設定重新啟動。

**指令說明：**

* `firstboot`：此指令啟動重設流程，清除所有設定及已安裝的套件。
* `reboot`：此指令重新啟動路由器，套用重設後的設定。