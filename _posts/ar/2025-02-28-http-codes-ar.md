---
audio: false
generated: true
lang: ar
layout: post
title: أشعار الاستجابة الشائعة في بروتوكول نقل النص الفائق
translated: true
---

هل سبق لك أن وقعت على خطأ "404 Not Found" أثناء التصفح على الإنترنت وتساءلت عما يعنيه؟ أو ربما واجهت خطأ "500 Internal Server Error" وتهتمت لماذا ظهر؟ هذه الأرقام هي **رموز استجابة HTTP**، وهي من أهم العناصر في كيفية التواصل على الإنترنت. في هذا المدون، سنشرح ما هي هذه الرموز، ونستعرض بعض أكثرها شيوعًا، ونشرح لماذا من المهم فهمها - سواء كنت مطورًا أو مستخدمًا محترفًا على الإنترنت.

---

## ما هو HTTP؟

نبدأ من الأساس. **HTTP** أو *نظام نقل النص الفائق*، هو النظام الذي يوفر تبادل البيانات على الإنترنت. عندما تكتب عنوان URL في متصفحك وتضغط على Enter، يبعث متصفحك **طلبًا HTTP** إلى الخادم الذي يستضيف الموقع. ثم يرد الخادم **باستجابة HTTP** تتضمن رمزًا ثلاثي الأرقام **حالة**. هذا الرمز يوضح لك ما إذا كان طلبك ناجحًا، وإذا لم يكن كذلك، ما هو الخطأ.

---

## الفئات الخمسة لرموز استجابة HTTP

تم تنظيم رموز استجابة HTTP إلى خمس فئات، لكل منها غرض محدد:

- **1xx (معلوماتية)**: تلقى الخادم طلبك و هو لا يزال يعمل عليه.
- **2xx (نجاح)**: تلقى الخادم طلبك وفهمه و تم تنفيذه بنجاح.
- **3xx (إعادة توجيه)**: عليك أن تأخذ خطوة إضافية - مثل متابعة URL جديد - للحصول على ما تريد.
- **4xx (خطأ من جانب العميل)**: هناك خطأ من جانبك، مثل خطأ في الكتابة أو عدم وجود بيانات.
- **5xx (خطأ من جانب الخادم)**: واجه الخادم مشكلة ولم يتمكن من معالجة طلبك الصحيح.

الآن، دعونا نغوص في الرموز التي ستواجهها بشكل أكثر شيوعًا.

---

## شرح رموز استجابة HTTP الشائعة

هنا قائمة بالرموز الشائعة من استجابة HTTP، مع أمثلة لتوضيحها:

### 200 OK
- **ما يعنيه**: كان الطلب ناجحًا. قام الخادم بمعالجته و أرسل البيانات التي طلبتها.
- **مثال**: تحميل صفحة ويب مثل `www.example.com` دون أي مشاكل؟ هذا هو 200 OK.

### 201 Created
- **ما يعنيه**: كان طلبك ناجحًا، و تم إنشاء مورد جديد نتيجة لذلك.
- **مثال**: تقديم استمارة للاشتراك في النشرة الإخبارية، و يؤكد الخادم أن حسابك تم إنشاؤه.

### 301 Moved Permanently
- **ما يعنيه**: انتقل المورد الذي تريد الوصول إليه إلى URL جديد بشكل دائم، و يجب عليك استخدام هذا العنوان الجديد من الآن فصاعدًا.
- **مثال**: ينتقل مقال في المدونة من `oldblog.com/post1` إلى `newblog.com/post1`، و يوجه الخادمك إلى العنوان الجديد.

### 302 Found
- **ما يعنيه**: المورد مؤقتًا في URL مختلف، ولكن استخدم العنوان الأصلي للمطالبات المستقبلية.
- **مثال**: يتم إعادة توجيه الصفحة الرئيسية للموقع مؤقتًا إلى صفحة عرض خاص.

### 404 Not Found
- **ما يعنيه**: لا يمكن للخادم العثور على ما تبحث عنه - ربما تم حذف الصفحة أو كان URL غير صحيح.
- **مثال**: كتابة `www.example.com/oops` و الوصول إلى صفحة خطأ لأن "oops" غير موجود.

### 403 Forbidden
- **ما يعنيه**: يعرف الخادم ما تريد، ولكن لن يسمح لك به لأنك لا تملك الإذن.
- **مثال**: محاولة الوصول إلى لوحة تحكم خاصة دون تسجيل الدخول.

### 401 Unauthorized
- **ما يعنيه**: عليك التحقق من هويتك (مثل تسجيل الدخول) قبل أن تتمكن من الاستمرار.
- **مثال**: زيارة منتدى خاص بالعضوية دون تسجيل الدخول.

### 400 Bad Request
- **ما يعنيه**: لا يمكن للخادم فهم طلبك بسبب خطأ في الكتابة أو بيانات غير صالحة.
- **مثال**: تقديم استمارة تحتوي على حقل بريد إلكتروني يحتوي على حروف غير معقولة مثل “@#$%”.

### 500 Internal Server Error
- **ما يعنيه**: حدث خطأ في الخادم، ولكن لا يوضح ما هو.
- **مثال**: يتسبب موقع ويب في انهيار بسبب خطأ لم يتم اكتشافه من قبل المطورين.

### 503 Service Unavailable
- **ما يعنيه**: الخادم غير متوفر - ربما بسبب الصيانة أو لأنه مفرط في التحميل.
- **مثال**: محاولة التسوق عبر الإنترنت خلال عرض كبير، فقط لرؤية رسالة "حاول مرة أخرى لاحقًا".

---

## بعض الرموز الأخرى التي يجب معرفتها

هذه الرموز ليست شائعة، ولكنها تظهر بشكل كافٍ لتستحق الذكر:

- **100 Continue**: الخادم راضي عن إرسال طلب كبير، فاذهب إلى الأمام.
- **204 No Content**: كان الطلب ناجحًا، ولكن لا شيء للعودة به (مثل بعد حذف شيء).
- **304 Not Modified**: لم يتغير المورد، فاستخدم النسخة التي لديك محفوظة.
- **429 Too Many Requests**: أنت طلبت من الخادم كثيرًا، و هو يقول لك أن تتوقف (شائع في APIs).
- **502 Bad Gateway**: خادم وسيط تلقى استجابة سيئة من الخادم الرئيسي الذي يحاول الوصول إليه.

---

## أمثلة يومية لرموز HTTP

دعونا نجعل هذه الرموز أكثر قابلية للتفاهم مع بعض المقارنات اليومية:

- **200 OK**: طلبت قهوة، و تم تقديمها لك كما تحبها.
- **201 Created**: طلبت قميصًا مخصصًا، و يقول لك المتجر "إنه قيد العمل!"
- **301 Moved Permanently**: انتقل مطعمك المفضل عبر المدينة و أعطاك العنوان الجديد.
- **302 Found**: المطعم مغلق للتصليح، ولكن يشير إليك إلى شاحنة طعام قريبة.
- **404 Not Found**: طلبت كتابًا في المكتبة، ولكن لم يكن في فهرستهم.
- **403 Forbidden**: حاولت دخول حفلة خاصة دون دعوة.
- **401 Unauthorized**: حاولت استخدام صالة رياضية ولكن نسيت بطاقتك.
- **400 Bad Request**: طلبت طعامًا بلغة لا يفهمها الخادم.
- **500 Internal Server Error**: طلبت من طاهي حساء، و انفجرت المطبخ.
- **503 Service Unavailable**: اتصلت بخط ساخن، ولكن جميع الخطوط مشغولة.

---

## لماذا يجب أن تهمك رموز HTTP؟

للمطورين، هذه الرموز هي الذهب. تساعدك في تصحيح الأخطاء، معالجة الأخطاء بشكل راقي، وبناء تطبيقات لا تترك المستخدمين في انتظار. على سبيل المثال، معرفة ما إذا كان خطأ 400 أو 500 قد حدث يمكن تحديد ما إذا كان الخطأ من جانب المستخدم أو الخادم.

للمستخدمين العاديين، فهم أساسي لهذه الرموز يمكن أن يوضح بعض الأخطاء على الإنترنت. 404 يعني أن الصفحة مفقودة، بينما 503 يشير إلى الانتظار. كما لو كنت تمتلك ورقة شيفرة للإنترنت.

بالإضافة إلى ذلك، **موتورات البحث** تعتمد على هذه الرموز لSEO. يمكن أن يحافظ 301 على تصنيف موقعك عند نقل المحتوى، بينما يمكن أن يشير 404 إلى نهاية ميتة لGoogle.

---

## الخاتمة

رموز استجابة HTTP هي طريقة الإنترنت للتواصل معنا، لتخبرنا ما إذا كان طلبنا ناجحًا أو فشل. من **200 OK** الفائز إلى **500 Internal Server Error** المزعج، كل رمز يروي قصة. سواء كنت تكتب موقعًا أو فقط تتصفح، فهم هذه الرموز الشائعة يمكن أن يجعل حياتك على الإنترنت أكثر سلاسة وأقل غموضًا. لذلك، في المرة القادمة التي ترى فيها 404، ستعرف أنها ليست أنت - إنها فقط الإنترنت يقول "لا أستطيع العثور على هذه الصفحة!"