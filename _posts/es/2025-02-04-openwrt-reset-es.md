---
audio: false
generated: false
image: false
lang: es
layout: post
title: Restablecer OpenWrt
translated: true
---

## Restablecer mediante la Interfaz Web

Se recomienda conectarse al router mediante un cable ethernet. Después de un restablecimiento, el SSID de Wi-Fi volverá a su configuración predeterminada, lo que puede no ser lo que esperas.

## Restablecer mediante Línea de Comandos (SSH)

Puedes restablecer OpenWrt a su configuración predeterminada usando la interfaz de línea de comandos (SSH). Así es cómo:

1. Conéctate a tu router OpenWrt mediante SSH.
2. Ejecuta el siguiente comando:

    ```bash
    root@OpenWrt:~# firstboot
    Esto borrará toda la configuración y eliminará cualquier paquete instalado. ¿Estás seguro? [N/y]
    y
    /dev/ubi0_1 está montado como /overlay, solo se borrarán los archivos
    root@OpenWrt:~# reboot
    ```
3. El router se reiniciará con la configuración predeterminada.

**Explicación de los comandos:**

* `firstboot`: Este comando inicia el proceso de restablecimiento, borrando todas las configuraciones y paquetes instalados.
* `reboot`: Este comando reinicia el router, aplicando el restablecimiento.