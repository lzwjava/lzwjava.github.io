---
audio: false
generated: false
image: false
lang: ar
layout: post
title: إعادة ضبط OpenWrt
translated: true
---

## إعادة الضبط عبر واجهة الويب

يُوصى بالاتصال بالراوتر باستخدام كابل الإيثرنت. بعد إعادة الضبط، سيتم إعادة اسم شبكة الوايفاي (SSID) إلى الإعدادات الافتراضية، والتي قد لا تكون كما تتوقع.

## إعادة الضبط عبر سطر الأوامر (SSH)

يمكنك إعادة ضبط نظام OpenWrt إلى الإعدادات الافتراضية باستخدام واجهة سطر الأوامر (SSH). إليك الطريقة:

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

**شرح للأوامر:**

*   `firstboot`: هذا الأمر يبدأ عملية إعادة الضبط، حيث يحذف جميع التهيئات والحزم المثبتة.
*   `reboot`: هذا الأمر يعيد تشغيل الراوتر، تطبيق إعادة الضبط.