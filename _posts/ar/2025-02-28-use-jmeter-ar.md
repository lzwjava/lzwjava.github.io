---
audio: false
generated: true
lang: ar
layout: post
title: كيفية استخدام JMeter
translated: true
---

JMeter هو أداة برمجية مفتوحة المصدر مصممة لاختبار الحمل وإقياس أداء تطبيقات الويب، على الرغم من أنها يمكن أن تستهدف أنواع أخرى من الأنظمة مثل قواعد البيانات ومخدمات FTP. أدناه دليل واضح، خطوة بخطوة، لمساعدتك على البدء في استخدام JMeter لاختبار الأداء، مع التركيز بشكل أساسي على تطبيقات الويب.

---

#### **الخطوة 1: تثبيت JMeter**
- **المتطلبات الأساسية**: JMeter هو تطبيق قائم على Java، لذا يجب أن يكون لديك Java (النسخة 8 أو أحدث) مثبتًا على جهازك. يمكنك التحقق من ذلك من خلال تشغيل `java -version` في سطر الأوامر.
- **التنزيل**: زور موقع [Apache JMeter](https://jmeter.apache.org/) وتنزيل أحدث نسخة (ملف .zip أو .tgz).
- **التثبيت**: استخرج الملف المنزّل إلى مجلد من اختيارك (مثل `C:\JMeter` في Windows أو `/opt/jmeter` في Linux/Mac). لا توجد خطوات تثبيت إضافية مطلوبة.

---

#### **الخطوة 2: تشغيل JMeter**
- انتقل إلى مجلد `bin` داخل مجلد JMeter (مثل `C:\JMeter\apache-jmeter-x.x\bin`).
- **Windows**: انقر مرتين على `jmeter.bat` أو قم بتشغيله من خلال سطر الأوامر.
- **Linux/Mac**: افتح نافذة ترمينال، انتقل إلى مجلد `bin`، واطلب `./jmeter.sh`.
- سيتم فتح واجهة المستخدم الرسومية (GUI) التي تعرض لوحة عمل JMeter.

---

#### **الخطوة 3: إنشاء خطة اختبار**
- **خطة الاختبار** هي الأساس لاختبار الأداء الخاص بك. تحدد ما تريد اختباره وكيف.
- في واجهة JMeter، توجد خطة الاختبار بالفعل في الشريط الجانبي الأيسر. انقر بالزر الأيمن عليها لتغيير اسمها (مثل "اختبار أداء الويب") أو اتركها كما هي.

---

#### **الخطوة 4: إضافة مجموعة خيوط**
- **مجموعة الخيوط** تقم بإحاكة المستخدمين الذين سيرسلون طلبات إلى الخادم.
- انقر بالزر الأيمن على خطة الاختبار > **إضافة** > **خيوط (المستخدمون)** > **مجموعة الخيوط**.
- قم بتكوين:
  - **عدد الخيوط (المستخدمون)**: قم بتعيين عدد المستخدمين الافتراضيين الذي تريد (مثل 10).
  - **فترة التدرج (بالثواني)**: الوقت الذي يستغرقه بدء جميع الخيوط (مثل 10 ثانية يعني 1 خيط في الثانية).
  - **عدد التكرار**: عدد مرات تكرار الاختبار (مثل 1 أو قم بتحديد "إلى الأبد" للاختبار المستمر).

---

#### **الخطوة 5: إضافة عينات**
- **العينات** تحدد الطلبات المرسلة إلى الخادم. بالنسبة لاختبار الويب، استخدم عينة طلب HTTP.
- انقر بالزر الأيمن على مجموعة الخيوط > **إضافة** > **عينة** > **طلب HTTP**.
- قم بتكوين:
  - **اسم الخادم أو IP**: أدخل الموقع المستهدف (مثل `example.com`).
  - **المسار**: تحديد النهايات (مثل `/login`).
  - **الطريقة**: اختر `GET`، `POST`، إلخ، بناءً على سيناريو الاختبار الخاص بك.

---

#### **الخطوة 6: إضافة مستمعين**
- **المستمعون** يعرضون وتحليل نتائج الاختبار.
- انقر بالزر الأيمن على مجموعة الخيوط > **إضافة** > **مستمع** > (مثل **عرض شجرة النتائج** أو **تقرير ملخص**).
- خيارات شعبية:
  - **عرض شجرة النتائج**: يعرض بيانات الطلب/الإجابة التفصيلية.
  - **تقرير ملخص**: يقدم مقياسات مجمعة مثل متوسط وقت الاستجابة ونسبة الخطأ.

---

#### **الخطوة 7: تكوين الاختبار**
- تحسين اختبارك مع عناصر إضافية (اختيارية ولكن مفيدة):
  - **المؤقيتات**: إضافة تأخير بين الطلبات (مثل انقر بالزر الأيمن على مجموعة الخيوط > **إضافة** > **مؤقيت** > **مؤقيت ثابت**).
  - **التأكيدات**: التحقق من إجابات الخادم (مثل انقر بالزر الأيمن على طلب HTTP > **إضافة** > **التأكيدات** > **تأكيد الإجابة**).
  - **عناصر التكوين**: تعيين المتغيرات أو الافتراضات HTTP (مثل **إعدادات طلب HTTP الافتراضية**).

---

#### **الخطوة 8: تشغيل الاختبار**
- حفظ خطة الاختبار (**ملف** > **حفظ**) كملف `.jmx` لإعادة الاستخدام.
- انقر على زر **التشغيل** الأخضر (المثلث) في شريط الأدوات أو انتقل إلى **تشغيل** > **بدء**.
- سيقوم JMeter بتنفيذ الاختبار بناءً على إعدادات مجموعة الخيوط الخاصة بك.

---

#### **الخطوة 9: تحليل النتائج**
- بعد الانتهاء من الاختبار، تحقق من المستمعين:
  - **عرض شجرة النتائج**: فحص نجاحات/فشلات الطلبات الفردية.
  - **تقرير ملخص**: مراجعة المقياسات مثل معدل التوصيل، أوقات الاستجابة، ونسبة الخطأ.
- ابحث عن عوائق (مثل أوقات الاستجابة البطيئة) أو أخطاء تحتاج إلى تحقيق.

---

#### **الخطوة 10: تحسين الاختبار**
- بناءً على النتائج، قم بتعديل خطة الاختبار:
  - زيادة/تقلل من عدد الخيوط.
  - إضافة سيناريوهات أكثر واقعية (مثل عدة طلبات HTTP).
  - تعديل المؤقيتات أو التأكيدات للدقة.
- حفظ وإعادة تشغيل الاختبار لتأكيد التحسينات.

---

### نصائح إضافية
- **حفظ وتحميل**: استخدم ملفات `.jmx` لحفظ خطة الاختبار وتحميله لاحقًا من خلال **ملف** > **فتح**.
- **واجهة المستخدم الرسومية مقابل غير الرسومية**: بالنسبة للاختبارات الكبيرة، قم بتشغيل JMeter في وضع غير الرسومي (مثل `jmeter -n -t test.jmx -l results.jtl`) لحفظ الموارد النظامية.
- **تعلم المزيد**: استكشف الميزات المتقدمة مثل التخصيص (للبيانات الديناميكية) أو التزامن (للتطبيقات الويب الديناميكية) مع اكتساب الخبرة.

يوفر هذا الدليل الأساسيات لبدء استخدام JMeter بشكل فعال. مع الممارسة، يمكنك تعديل الاختبارات لتناسب احتياجات الاختبار الأداء الخاصة بك!