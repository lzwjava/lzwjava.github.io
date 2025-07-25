---
audio: false
generated: false
image: false
lang: ar
layout: post
title: الحد الأقصى لوقت تنفيذ وظيفة GitHub Actions
translated: true
---

لقد كنت أستخدم GitHub Actions لأتمتة ترجمة منشورات مدونتي. في البداية، حاولت ترجمة جميع المنشورات في مهمة واحدة، مع إجراء التغييرات وإعادتها إلى المستودع فقط بعد اكتمال جميع الترجمات.

كنت متفائلاً وذهبت للنوم، متوقعًا أن تنتهي العملية. ومع ذلك، بعد 8 ساعات، استيقظت لأجد الخطأ التالي:

> تجاوزت المهمة التي تعمل على العدّاء GitHub Actions 12 الحد الأقصى لوقت التنفيذ وهو 360 دقيقة.

هذا يعني أن 6 ساعات من العمل في الترجمة قد ضاعت، حيث تم تنفيذ الـ commit فقط في النهاية.

لحل هذه المشكلة، قمت بتعديل سير العمل ليتم إجراء التغييرات كل 10 ملفات.

علاوة على ذلك، قمت بتنفيذ برمجة متعددة الخيوط (multithreaded programming) لتقليل الوقت الإجمالي للترجمة من 6 ساعات إلى حوالي ساعة واحدة.

يقدم GitHub Actions الكثير من المرونة. فهو يدعم وظائف سير العمل المتعددة، مما يسمح بفصل المهام. يمكن تشغيل بعض الوظائف عند كل عملية commit، بينما يمكن تشغيل وظائف أخرى بواسطة أحداث مختلفة.