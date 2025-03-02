---
audio: false
generated: true
lang: ar
layout: post
title: مشكلة بدء التشغيل
translated: true
---

عندما تقلك على `Eclipse.exe` لإطلاق Eclipse 4.6.3 وتواجه الأخطاء "خطأ: لم يمكن إنشاء آلة Java الافتراضية" و"خطأ: حدث استثناء قاتل. سيتم إغلاق البرنامج"، فهذا يشير إلى أن Eclipse لا يمكن أن يبدأ آلة Java الافتراضية (JVM) التي تحتاجها للعمل. يمكن أن يحدث ذلك لعدة أسباب، وسأرشدك على كيفية تشخيص وإصلاح المشكلة خطوة بخطوة.

### فهم المشكلة
Eclipse هو تطبيق قائم على Java، مما يعني أنه يعتمد على JVM للعمل. يشير الخطأ إلى أن هناك شيء يمنع JVM من البدء بشكل صحيح. تشمل الأسباب الشائعة مشاكل في إعدادات الذاكرة، أو تثبيت Java، أو تكوين Eclipse نفسه. دعونا نحقق في هذه الاحتمالات.

---

### خطوات لتحديد وإصلاح المشكلة

#### 1. **تحقق من الذاكرة المتاحة في النظام**
يحتاج JVM إلى كمية معينة من الذاكرة للبدء. إذا لم يكن لديك نظامك ذاكرة كافية، يمكن أن يحدث هذا الخطأ.

- **كيفية التحقق**: افتح مدير المهام (في Windows، اضغط على `Ctrl + Shift + Esc`) واطلع على علامة "الأداء" لمعرفة كم من الذاكرة متاحة.
- **ماذا يجب فعله**: تأكد من أن هناك 1-2 جيجابايت من ذاكرة الوصول العشوائي الحرة عند إطلاق Eclipse. أغلق التطبيقات غير الضرورية لتحرير الذاكرة إذا لزم الأمر.

#### 2. **تحقق من ملف `eclipse.ini` وإعداده**
يستخدم Eclipse ملفًا للاتفاقية يسمى `eclipse.ini`، الموجود في نفس المجلد الذي يحتوي على `eclipse.exe`، لتحديد إعدادات JVM، بما في ذلك تخصيص الذاكرة. يمكن أن تكون هذه الإعدادات غير صحيحة سببًا شائعًا لهذا الخطأ.

- **موقع الملف**: انتقل إلى مجلد تثبيت Eclipse (على سبيل المثال، `C:\eclipse`) واكتشف `eclipse.ini`.
- **تحقق من إعدادات الذاكرة**: افتح الملف في محرر النصوص واطلع على السطور مثل:
  ```
  -Xms256m
  -Xmx1024m
  ```
  - `-Xms` هو حجم الكومة الأولي (على سبيل المثال، 256 ميجابايت).
  - `-Xmx` هو حجم الكومة الأقصى (على سبيل المثال، 1024 ميجابايت).
- **لماذا يفشل**: إذا كانت هذه القيم مرتفعة جدًا بالنسبة لمتاحة الذاكرة في نظامك، فلا يمكن JVM تخصيص الكمية المطلوبة وتفشل في البدء.
- **إصلاحه**: حاول خفض هذه القيم. على سبيل المثال، قم بتحريرها إلى:
  ```
  -Xms128m
  -Xmx512m
  ```
  احفظ الملف وحاول إطلاق Eclipse مرة أخرى. إذا عمل، كانت الإعدادات الأصلية مرتفعة جدًا بالنسبة لنظامك.

#### 3. **تحقق من تثبيت Java**
يحتاج Eclipse 4.6.3 إلى بيئة تشغيل Java (JRE) أو كيت تطوير Java (JDK)، عادةً Java 8 أو أحدث. إذا كان Java مفقودًا أو غير مهيأ بشكل صحيح، فلا يمكن إنشاء JVM.

- **تحقق من تثبيت Java**:
  - افتح نافذة الأوامر (اضغط على `Win + R`، اكتب `cmd`، واضغط على Enter).
  - اكتب `java -version` واضغط على Enter.
  - **الخروج المتوقع**: شيء مثل `java version "1.8.0_351"`. هذا يثبت أن Java 8 مثبت.
  - **إذا لم يكن هناك خروج أو خطأ**: Java غير مثبت أو غير موجود في مسار النظام. قم بتثبيت JDK 8 (تحميل من موقع Oracle أو adoptium.net) واطمئن إلى أن مجلد `bin` (على سبيل المثال، `C:\Program Files\Java\jdk1.8.0_351\bin`) أضيف إلى متغير المسار في النظام.
- **تحقق من `eclipse.ini` لJVM محدد**:
  - اكتب `-vm`، مثل:
    ```
    -vm
    C:\Program Files\Java\jdk1.8.0_351\bin\javaw.exe
    ```
  - **تحقق من المسار**: اطمئن إلى أن هذا يشير إلى ملف `javaw.exe` صالح في تثبيت JDK/JRE. إذا كان المسار خاطئًا أو الملف غير موجود، قم بإصلاحه أو إزالة القسم `-vm` لتسمح Eclipse باستخدام Java الافتراضية في النظام.

#### 4. **اعتبر تثبيت Eclipse الفاسد**
إذا لم تقم بإصلاح المشكلة، فقد يكون تثبيت Eclipse فاسدًا.

- **كيفية إصلاحه**:
  - قم بتحميل Eclipse 4.6.3 مرة أخرى من الموقع الرسمي (eclipse.org).
  - استخرجه إلى مجلد جديد وحاول إطلاقه مرة أخرى.
  - اختياريًا، قم بحذف مجلد Eclipse القديم بعد نسخ أي إعدادات مخصصة أو مساحات عمل.

---

### كيفية المتابعة
اتبع هذه الخطوات بالترتيب:
1. **ابدأ بالذاكرة**: تحقق من ذاكرة النظام المتاحة واعدل `eclipse.ini` إذا لزم الأمر.
2. **تحقق من Java**: تأكد من تثبيت Java وتهيئته بشكل صحيح.
3. **أعد التثبيت إذا لزم الأمر**: استبدل تثبيت Eclipse إذا استمرت المشكلة.

بالتنقل بشكل منهجي عبر هذه التحققات، ستعرف ما إذا كانت المشكلة ناتجة عن قيود الذاكرة، أو إعدادات JVM، أو تثبيت فاسد. غالبًا ما يتم إصلاح هذا الخطأ عن طريق تعديل إعدادات الذاكرة في `eclipse.ini` أو إصلاح إعدادات Java.

أعلمني إذا كنت تحتاج إلى مساعدة في أي خطوة محددة!