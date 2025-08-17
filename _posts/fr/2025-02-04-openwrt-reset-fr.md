---
audio: false
generated: false
image: false
lang: fr
layout: post
title: Réinitialisation d'OpenWrt
translated: true
---

## Réinitialisation via l'Interface Web

Il est recommandé de se connecter au routeur via un câble Ethernet. Après une réinitialisation, le SSID Wi-Fi reviendra à ses paramètres par défaut, ce qui peut ne pas correspondre à ce que vous attendez.

## Réinitialisation via la Ligne de Commande (SSH)

Vous pouvez réinitialiser OpenWrt aux paramètres par défaut en utilisant l'interface en ligne de commande (SSH). Voici comment procéder :

1. Connectez-vous à votre routeur OpenWrt via SSH.
2. Exécutez la commande suivante :

    ```bash
    root@OpenWrt:~# firstboot
    Cela effacera tous les paramètres et supprimera tous les paquets installés. Êtes-vous sûr ? [N/o]
    o
    /dev/ubi0_1 est monté comme /overlay, seul le contenu des fichiers est effacé
    root@OpenWrt:~# reboot
    ```
3. Le routeur redémarrera avec les paramètres par défaut.

**Explication des commandes :**

* `firstboot` : Cette commande lance le processus de réinitialisation, effaçant toutes les configurations et les paquets installés.
* `reboot` : Cette commande redémarre le routeur pour appliquer la réinitialisation.