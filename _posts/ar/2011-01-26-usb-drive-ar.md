---
audio: false
generated: false
image: false
lang: ar
layout: post
title: تخصيص قارطة USB بكلمة وأيقونة
translated: true
---

هذه المنشورة كتبت في البداية بالصينية ونشرت على Qzone.

---

**I. تقليل أيقونة USB:**

1. في البداية، اختر أيقونة ترغب فيها. يجب أن يكون امتداد ملف أيقونة `.ico`.
2. انقِل أيقونة الملف إلى USB وانشئ ملف نصوص جديد على USB.
3. في ملف النص، اكتب ما يلي:
   ```
   [autorun]
   ICON=\xxx.ico,0
   ```
   حيث `xxx.ico` هو اسم ملف أيقونتك (بما في ذلك الامتداد).
4. احفظ ملف النص باسم `autorun.inf`.
   **ملاحظة:** من الضروري تغيير الامتداد إلى `.inf`، لا `.txt`. إذا تغيرت أيقونة الملف إلى ذات عجلة صفراء، فأنت فعلت ذلك بشكل صحيح.
   سحب USB وربطه مرة أخرى. ستلاحظ أن أيقونة USB تغيرت إلى تلك التي اخترتها.
   يمكن استخدام هذا الأسلوب أيضًا للأقراص الصلبة الخارجية أو حرق الأقراص المضغوطة أو DVD.

**II. تعديل الخلفية:**

1. في البداية، اختر صورة خلفية ترغب فيها وأقْلع عليها إلى USB.
2. انشئ ملف نص جديد وأقُلع ما يلي فيه:
   ```
   [ExtShellFolderViews]
   {BE098140-A513-11D0-A3A4-00C04FD706EC}={BE098140-A513-11D0-A3A4-00C04FD706EC}
   [{BE098140-A513-11D0-A3A4-00C04FD706EC}]
   Attributes=1
   IconArea_Image=aaa.jpg
   IconArea_Text=0x00FFFFFF
   [.ShellClassInfo]
   ConfirmFileOp=0
   ```
   وهذا يعني:

   حيث `aaa.jpg` هو اسم ملف الصورة المفضلة (بما في ذلك الامتداد).

   `IconArea_Text= 0x00FFFFFF`  هذه السطر تغير لون النص على USB.

   رموز الألوان هي:

   *   أحمر: `0x000000FF`
   *   أصفر: `0x0000FFFF`
   *   أزرق: `0x00FF0000`
   *   رمادي: `0x00808080`
   *   أخضر ليموني: `0x006BDEC7`
   *   أسود: `0x00000000`
   *   لون خلفية Excel: `0x00848284`
   *   أبيض: `0x00FFFFFF`
   *   أخضر: `0x00008000`
   *   Purple: `0x00C000C0`

   اختر اللون الذي ترغب فيه (الذي يتوافق مع خلفية) واسحب على الرمز الحالي.

   يمكنك تغيير اللون بعد `IconArea_Text=` إلى اللون المفضل لديك.

3. احفظ ملف النص باسم `Desktop.ini`. الانتهاء من التعديلات.
   تحديث USB وسترى التغييرات.
   يمكن إخفاء جميع الأربعة ملفات المذكورة أعلاه لمنع الحذف بالخطأ.
   بعد تغيير الأيقونة، يجب سحب USB وإعادة الربط لمرؤية التأثير.
   بعد تغيير الخلفية، تحديث USB لمرؤية التغييرات.