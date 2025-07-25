---
audio: false
generated: false
image: false
lang: ar
layout: post
title: مزايا تراكم السجلات
translated: true
---

عندما كنت أعمل كمقاول لمصرف سابقًا، كنا نستخدم منصة تطبيقات متعددة السحابة لخدمة الخدمات الصغيرة. في ذلك الوقت، بدأت في جمع السجلات أثناء العمل في الشركة.

مرت عدة سنوات، وأظل أعتقد أنها واحدة من أفضل الطرق التي تساعدني في العمل أو إجراء هندسة البرمجيات. مع مرور الوقت، في مجلد السجلات لدي، هناك hundreds of log files.

لا لدي مجلدات فرعية محددة أو أسماء ملفات سجلات رسمية لتلك السجلات. أحيانًا، أستخدم فقط اسم مهمة JIRA كprefix لاسم ملف السجل أو تلك الميزة. ثم أضيف رقم في suffix. مثل mutual-fund-1.log، mutual-fund-2.log، إلخ. وهذا يعني في خدمة mutual fund الصغيرة، لدي تلك السجلات عند تشغيل تلك الخدمة.

أحيانًا، عند العمل على مشاريع تخدم مناطق متعددة، سأضيف تلك الدولة كsuffix، مثل mutual-fund-cn-1.log، mutual-fund-sg-1.log. أسماء ملفات السجلات somewhat casual. لأن في ذلك الوقت، كنت بحاجة إلى التركيز على stacks of errors أو الدالة المحيطة للمكالمة.

سجلات البرامج مهمة. الجميع يعرف ذلك. ومع ذلك، أريد أن أوضح أهمية جمع السجلات بدلاً من مجرد مشاهدتها في الواجهة الأمامية وتجاهلها. ستجد المزيد من الراحة عندما تستمر المشروع. لديك المزيد من الوقت للعثور على السجلات السابقة. قد تحتاج إلى معرفة ما إذا حدث مكالمة إجراء مخزن بيانات مماثل قبل ذلك. قد تحتاج إلى معرفة ما إذا حدث نفس الخطأ قبل ذلك. قد تحتاج إلى استعادة كيفية إصلاح هذه المشكلة في المرة السابقة.

هناك العديد من التفاصيل في مشروع كبير أو عشرات الخدمات الصغيرة. والخطأ، الاستثناءات، أو المشاكل تحدث مرة بعد أخرى. السجل هو مثل الوثيقة الجارية للبرنامج. وهي تُولد تلقائيًا من قبل البرنامج دون الحاجة إلى كتابة الإنسان. وللمطورين، هذه السجلات قابلة للقراءة. لذا، عند بدء مهمة جديدة أو إصلاح عيب جديد، لديك hundreds of logs في يدك لإصلاح هذا العيب الجديد. أنت لست وحيدًا.

لماذا نجمعها؟ لأن الأشياء أو المعرفة سهلة النسيان.

حدث تقدم في الحضارة البشرية عندما تم اختراع الورق. وعندما تم اختراع computers، كان هناك مستوى آخر من تقدم الحضارة البشرية. الاحتفاظ بالملاحظات على الورق هو مثل جمع السجلات في computers.

لا فقط للإنسان، ولكن أيضًا للروبوتات الدردشة AI، أدوات LLM، هذه السجلات تصبح أكثر أهمية. GreptimeDB، قاعدة بيانات لجمع وتحليل بيانات المراقبة الموحدة (المعايير، السجلات، والمتابعات) التي تأسست في 2022، ليست مصادفة.

لماذا لم أفعل ذلك قبل ذلك؟ بعد أن عملت كمقاول لمصارف كبيرة، كنت بحاجة إلى المزيد من التعاون والعمل على مشاريع أكبر. قبل ذلك، معظم الوقت في startup أو فترة startup الخاصة بي، كنت أعمل بمفردي. عندما كنت أعمل في LeanCloud قبل ذلك، كنت أعمل على تطبيق IM LeanChat لمدة نصف الوقت تقريبًا.

وعندما دخلت إلى العالم الشركاتي الرسمي، كان تطوير المشاريع مختلفًا عن مشروعي الشخصي أو startup. لديهم بيئات SIT، UAT للاختبار. والبيئة الإنتاجية غالبًا ما تكون مفتوحة فقط لزمالة فريق صغير. الحصول على السجلات منهم وإصلاح المشاكل يصبح طويلًا بعض الشيء. وrunning project takes time، souvent besoin de la moitié d'une heure pour s'exécuter.

لذلك، لا يمكنني تشغيل أو اختبار البرنامج مثل fly. لا يمكنني إجراء نشر simplement en tapant une commande sur mon ordinateur personnel et en téléchargeant le code sur le serveur pour l'exécution.

لذلك، هذا يجعلني جمع السجلات للحصول على المزيد من السياق لتناول المهام. يجب علينا إصلاح المشاكل في المرة الأولى. يجب علينا التحقق من إصلاحنا في مرات قليلة فقط. لا نستطيع بسهولة الحصول على سجلات البرنامج الذي يعمل في السحابة أو خادم الشركة، لذا من الأفضل نسخها وحفظها على جهاز الكمبيوتر المحمول المحلي، لإجراء التحليل.

والآن، بالنسبة لمشروعي الشخصية، سأجمع السجلات أيضًا. أصبح هذا عادة. بعد العمل في شركات كبيرة لعدة سنوات، لدي بعض الصبر أو الاستراتيجية لجعل مشروعي أكبر وأطول. لذا، أعرف أنني أحتاج إلى هذه السجلات مع مرور الوقت.

قد يقول شخص ما أنك فقط تحتاج إلى أن يكون لديك كود أنيق ومشروع يعمل. لا تحتاج إلى جمع السجلات أو traces of errors. هذا جيد. عندما لدينا عيب أو ميزة جديدة، يمكننا تشغيل البرنامج للحصول على السجلات الحالية. لا نحتاج إلى السجلات من عملية التطوير. هم مثل السجلات التفصيلية للتجارب العلمية. في البداية، يبدو ذلك جيدًا. ولكن في المدى الطويل، إذا كنت تريد العمل عليه مرة أخرى، أو تريد مشاركته، أو السماح للآخرين بالعمل عليه، فقد لا يكون ذلك جيدًا.

أعتقد أنه قد يكون هناك فرص جيدة هنا. في الشركات، لماذا لا نشجع كل مطور على مشاركة السجلات التي جمعها؟ في المشاريع مفتوحة المصدر، يجب أن يكون لدينا ذلك أيضًا. لا نجد سجلات الآخرين جذابة لأننا لا نعرفهم. نفقد السياق عند حفظ تلك السجلات. وهناك، يبدو أن هناك العديد من الرسائل غير ذات الصلة أو التافهة.

لكن الجهد لجمع السجلات هو مجرد تافه. هو مجرد copy and paste كل مرة نرى بعض السجلات، خاصة تلك السجلات التي تحتوي على أخطاء. وما إذا كنا سنفعل ذلك بطريقة آلية؟ من فكرة جيدة تسجيل السجلات في مجلد كل مرة نعمل على مشروع، مثل تلك المشاريع Spring Boot.

العالم يصبح أكثر رقمية، لذا جمع سجلات البرامج الرقمية هو مثل جمع الكتب في العالم المادي.