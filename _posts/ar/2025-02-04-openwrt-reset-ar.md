---
audio: false
generated: false
image: false
lang: ar
layout: post
title: إعادة ضبط OpenWrt
translated: true
---

## إعادة التعيين عبر واجهة الويب

يُنصح بالاتصال بالراوتر عبر كابل إثيرنت. بعد إعادة التعيين، سيعود اسم شبكة Wi-Fi (SSID) إلى الإعدادات الافتراضية، مما قد لا يكون متوقعًا.

## إعادة التعيين عبر سطر الأوامر (SSH)

يمكنك إعادة تعيين نظام OpenWrt إلى الإعدادات الافتراضية باستخدام واجهة سطر الأوامر (SSH). إليك كيفية القيام بذلك:

1. اتصل براوتر OpenWrt الخاص بك عبر SSH.
2. قم بتشغيل الأمر التالي:

    ```bash
    root@OpenWrt:~# firstboot
    This will erase all settings and remove any installed packages. Are you sure? [N/y]
    y
    /dev/ubi0_1 is mounted as /overlay, only erasing files
    root@OpenWrt:~# reboot
    ```
3. سيتم إعادة تشغيل الراوتر بالإعدادات الافتراضية.

**شرح الأوامر:**

*   `firstboot`: هذا الأمر يبدأ عملية إعادة التعيين، حيث يحذف جميع التهيئات والحزم المثبتة.
*   `reboot`: هذا الأمر يعيد تشغيل الراوتر، مما يطبق إعادة التعيين.