---
audio: false
generated: false
image: false
lang: ar
layout: post
title: سير العمل هو BFS، والعامل هو DFS
translated: true
---

وفقًا لـ Anthropic [^1]:

- **التدفقات العملية (Workflows)** هي أنظمة يتم فيها تنسيق نماذج اللغات الكبيرة (LLMs) والأدوات من خلال مسارات برمجية محددة مسبقًا.
- **الوكلاء (Agents)**، من ناحية أخرى، هي أنظمة تتحكم فيها نماذج اللغات الكبيرة (LLMs) بشكل ديناميكي في عملياتها الخاصة واستخدام الأدوات، مع الحفاظ على المرونة في كيفية إنجاز المهام.

ما أفهمه من هذا هو:

- استخدام **سير العمل (workflows)** لتعزيز تطبيق أو منصة يشبه إلى حد كبير **البحث بالعرض أولاً (BFS)**، حيث يتم إكمال المهام بشكل منهجي ومستوى تلو الآخر.
- استخدام **الوكلاء (agents)** يشبه أكثر **البحث بالعمق أولاً (DFS)**، حيث يتم التعامل مع المهام بطريقة استكشافية خطوة بخطوة.

في بعض الأحيان، يمكن دمج **BFS** و **DFS**. يمكن أن يكون DFS متداخلًا داخل DFS آخر، وينطبق الشيء نفسه على BFS.

على سبيل المثال، **o1 (chain-of-thought)** يشبه البحث بالعرض أولاً (BFS). في البداية، يتم تقسيم المهام الرئيسية إلى خطوات منفصلة، ويتم توسيع كل خطوة إلى تفسيرات أكثر تفصيلاً. ثم، بناءً على كل التفكير، يتم تقديم النتيجة النهائية.

بالنسبة للمهام المعقدة للغاية، مثل طلب من الذكاء الاصطناعي بناء تطبيق YouTube أو إنشاء نظام تشغيل، يمكنه استخدام خوارزمية البحث بالعرض أولاً (BFS) أو البحث بالعمق أولاً (DFS) أو مزيج من الاثنين. الأمر يعتمد حقًا على كيفية استخدامنا لـ BFS وDFS — أحيانًا يحتاج الذكاء الاصطناعي إلى التعمق (DFS)، وأحيانًا يحتاج إلى توسيع نطاق نهجه (BFS).

اعتبار آخر هو أنه في كل خطوة، يجب على الذكاء الاصطناعي تقييم ما يجب فعله بعد ذلك لتحقيق أهدافه.

**الأهداف** هي جانب مثير للاهتمام. قد تكون هناك العديد من الأهداف، مثل إنشاء تطبيق YouTube، حيث يحتاج الذكاء الاصطناعي إلى التأكد من أن جميع الأكواد تعمل بشكل جيد، وجميع الميزات مُنفذة، وجميع الاختبارات تمر بنجاح. الطريقة للوصول إلى هذه الأهداف مثيرة للاهتمام. هل يجب على الذكاء الاصطناعي التعامل مع هدف واحد في كل مرة، أم يجب أن يُحرز تقدمًا في جميع الأهداف بشكل متزامن ثم يعيد التكرار على كل هدف؟

---

[^1]: بناء وكلاء فعالين، [Anthropic](https://www.anthropic.com/research/building-effective-agents)

