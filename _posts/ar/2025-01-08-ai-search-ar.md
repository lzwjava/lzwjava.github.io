---
audio: false
generated: false
image: false
lang: ar
layout: post
title: حالة استخدام البحث في ChatGPT
translated: true
---

**Zhiwei:**  
كيف تعرّف Anthropic الفرق بين سير العمل (workflow) والوكيل (agent)؟

**ChatGPT 4.0:**  
تميز Anthropic بين مفاهيم "سير العمل" (workflow) و"الوكيل" (agent) في سياق أنظمة الذكاء الاصطناعي وكيفية عملها:

1. **سير العمل (Workflow):**
   - يشير **سير العمل** إلى تسلسل منظم للمهام أو العمليات المصممة لتحقيق هدف محدد. في مجال الذكاء الاصطناعي، يتضمن هذا عادةً سلسلة من الخطوات المحددة مسبقًا، حيث تعتمد كل خطوة على مدخلات محددة وتنتج مخرجات. غالبًا ما تكون سير العمل خطية وصلبة في هيكلها، مع تدفق واضح للتحكم من خطوة إلى أخرى.
   - **مثال:** قد يتضمن سير العمل النموذجي نظام ذكاء اصطناعي يقوم بجمع البيانات، وتنظيف البيانات، وتدريب نموذج، ثم نشر النموذج في الإنتاج. يتم تنفيذ كل من هذه الخطوات بترتيب محدد للوصول إلى النتيجة المرجوة.

2. **الوكيل (Agent):**
   - من ناحية أخرى، يُعتبر **الوكيل** كيانًا أكثر استقلالية ومرونة. في مجال الذكاء الاصطناعي، الوكيل هو كيان يدرك بيئته، ويتخذ قرارات بناءً على هذا الإدراك، ويتخذ إجراءات لتحقيق أهدافه. يتم تصميم الوكلاء للعمل بشكل مستقل، مع القدرة على التكيف والتعلم من تفاعلاتهم مع البيئة.
   - على عكس سير العمل (workflows)، التي تتبع تسلسلًا ثابتًا من الخطوات، فإن الوكلاء ديناميكيون ويمكنهم تعديل سلوكهم بناءً على المدخلات المتغيرة. لديهم القدرة على تعديل إجراءاتهم عند مواجهة سيناريوهات جديدة.
   - **مثال:** يمكن أن يكون الوكيل الذكي عبارة عن روبوت محادثة (chatbot) يتعلم ويعدل استجاباته بناءً على تفاعلات المستخدم، أو نظام توصيات يعدل التوصيات وفقًا لتغير تفضيلات المستخدم.

### الاختلافات الرئيسية:
- **الهيكل:** يكون سير العمل أكثر صلابة ويتبع تسلسلًا محددًا مسبقًا، بينما يكون الوكيل مرنًا ويتكيف بناءً على بيئته وأهدافه.
- **الاستقلالية:** تعمل الوكلاء عادةً بشكل مستقل، حيث تتعلم وتتكيف مع مرور الوقت، بينما تتبع سير العمل خطوات ثابتة مع القليل من اتخاذ القرارات في الوقت الفعلي أو بدونها.
- **الغرض:** تُستخدم سير العمل لأتمتة سلسلة من المهام، بينما تركز الوكلاء على اتخاذ القرارات وتحقيق الأهداف من خلال التفاعل مع بيئتها.

باختصار، **سير العمل (workflows)** هي تسلسلات منظمة للمهام، بينما **الوكلاء (agents)** هي أنظمة مستقلة تتخذ القرارات وتتكيف لتحقيق أهدافها.

**Zhiwei:**  
[https://www.anthropic.com/research/building-effective-agents](https://www.anthropic.com/research/building-effective-agents)  
احصل على التعريف من هنا.

**ChatGPT 4.0:**  
في المقالة *"بناء وكلاء فعالين"* من قبل Anthropic، يتم تعريف **الوكلاء** و**سير العمل** على النحو التالي:

1. **العوامل (Agents):**  
   - **العامل** هو نظام مستقل قادر على اتخاذ القرارات والقيام بإجراءات لتحقيق أهداف محددة. يمكن للعامل تعديل إجراءاته بناءً على التغذية الراجعة الفورية من بيئته، مما يجعله مرنًا وديناميكيًا.  
   - يُتوقع من العوامل التعامل مع مهام معقدة تتطلب التفكير والتفاعل والتكيف المستمر. تستخدم العوامل تقنيات مثل التخطيط والتعلم والذاكرة لتحسين عملية اتخاذ القرارات بمرور الوقت.  
   - تؤكد Anthropic أن العوامل قادرة على "التصرف في العالم" لتنفيذ المهام وتعديل استراتيجياتها عند مواجهة سيناريوهات جديدة أو غير متوقعة.

2. **سير العمل (Workflows):**  
   - **سير العمل**، على النقيض من ذلك، هو تسلسل مسبق التحديد ومنظم للمهام مصمم لتحقيق نتيجة محددة. عادةً ما تتبع سير العمل ترتيبًا محددًا وتكون قابلة للتنبؤ، مع حاجة أقل للتكيف أو اتخاذ القرارات في الوقت الفعلي.  
   - في مجال الذكاء الاصطناعي، قد يتضمن سير العمل تشغيل سلسلة من العمليات بترتيب معين، مع مدخلات ومخرجات محددة. عادةً ما تكون ثابتة وتُستخدم لأتمتة المهام أو العمليات المتكررة حيث لا تكون المرونة ضرورية.

### الفرق الرئيسي:
- **العوامل (Agents)** هي أنظمة مستقلة تتكيف وتتخذ قرارات بناءً على التغذية الراجعة المستمرة، مما يجعلها مناسبة للبيئات الديناميكية.
- **سير العمل (Workflows)** هي تسلسلات محددة مسبقًا ومنظمة تُستخدم لأتمتة المهام دون الحاجة إلى تعديلات في الوقت الفعلي.

بشكل أساسي، **العوامل (agents)** هي أنظمة اتخاذ قرار تعمل بمرونة واستقلالية، بينما **سير العمل (workflows)** هي تسلسلات جامدة تُستخدم لأتمتة المهام.