---
audio: false
generated: false
image: false
lang: ar
layout: post
title: تخفيض تكاليف الترجمة باستخدام النص المرقم
translated: true
---

مدونتي التي تعمل على Jekyll تستخدم Markdown لكتابة الفقرات. بعد الكتابة بالإنجليزية، أستخدم أدوات الذكاء الاصطناعي مثل DeepSeek أو Mistral لتحويلها إلى ثمانية لغات أخرى. على الرغم من أنها رخيصة بالفعل، إلا أنه لا يزال هناك مجال للتحسن.

في بعض الأحيان، أقوم بتحرير كلمة أو فقرة واحدة، ثم يتم ترجمة النص بأكمله للمقال إلى اللغات الثمانية الأخرى. في هذه الحالة، يكون استخدام الرموز مرتفعًا. إذا ترجمت فقرة واحدة فقط مرة أخرى، فسيكون استخدام الرموز أقل، خاصة للمقالات الطويلة.

ومع ذلك، أريد استخدام Markdown لتسجيل أفكاري. استخدام قاعدة بيانات لإدارة وتحديث المقالات غير مريح. قد يكون استخدام YAML أو JSON معقدًا أيضًا.

الشيء الرئيسي هو تحديد الفروق بين النص قبل وبعد التحرير. إذا استخدمنا نهجًا قائمًا على الفقرات، فهذا يعني استخدام حرف newline "\n" لتفكيك النص.

أحتاج إلى معرفة أي الفقرات التي تغيرت وأيها لم تتغير بعد التحرير. نحتاج إلى معرفة الخريطة الواحدة إلى واحدة للفقرات بين النص قبل وبعد التحرير.

نستخدم نهجًا قائمًا على الفقرات لأننا نريد تحديث الترجمات التي يقوم بها نماذج الذكاء الاصطناعي. إذا استخدمنا الجمل، فقد لا تكون دقيقة.

للماركداون، قد يكون من المهم استخدام تحليل الماركداون لتزامن الترجمات بناءً على عناصر الماركداون.

لكن إذا لم يكن هناك أي كتل من الكود أو صياغة خاصة للماركداون، فيمكننا استخدام نهج قائم على الفقرات.

لنهج بسيط قائم على الفقرات، لدينا مصفوفتان من الفقرات ونحتاج إلى معرفة كيفية مطابقةهما.

عند مقارنة أي فقرة في هذه المصفوفتين، هناك نتيجة محتملة: إما أنها متطابقة أو مختلفة. إذا كانت مختلفة، هناك عدة حالات: كلاهما جديد المضافة، أو اليسار جديد المضافة، أو اليمين جديد المضافة.

أريد فقط تخفيض التكاليف، لذلك أريد تقليل استخدام الرموز. لا أحتاج إلى أي شيء آخر. أريد فقط ترجمة كل فقرة، تخزين النتيجة، وفي المرة القادمة، سأبحث عن نتيجة الترجمة لكل فقرة. إذا لم تكن موجودة، فسيتعين علي ترجمتها مرة أخرى.

للماركداون، الأمر أكثر تعقيدًا قليلاً. لا أريد ترجمة كتل الكود. لذلك، يمكننا استخدام مكتبة تحليل الماركداون أولاً لمعالجة كتل الكود والنص العادي بشكل مختلف.