---
audio: false
generated: false
image: false
lang: ar
layout: post
title: الحالات التي ما زلنا بحاجة فيها إلى مربع البحث في GitHub
translated: true
---

```yaml
jobs:
  awesome-cv-copy:
    runs-on: ubuntu-latest
    steps:
```

     # ...

```yaml
      - name: تثبيت TeX Live 2023
        if: steps.cache-texlive.outputs.cache-hit != 'true'
        run: |
          # تثبيت التبعيات اللازمة لتثبيت TeX Live
          sudo apt-get update
          sudo apt-get install -y perl wget xz-utils
```

          # تنزيل مُثبِّت TeX Live
          wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
          tar -xzf install-tl-unx.tar.gz
          cd install-tl-*/

      # ...

```yaml
      - name: تثبيت حزم LaTeX المفقودة
        run: |
          sudo /usr/local/texlive/2023/bin/x86_64-linux/tlmgr install etoolbox adjustbox
```

```yaml
      - name: تأكيد تثبيت الحزمة
        run: |
          kpsewhich etoolbox.sty
          kpsewhich adjustbox.sty
```

      - name: تشغيل make awesome-cv-copy
        run: make awesome-cv-copy
```

أنا أعمل على نص GitHub Actions أعلاه.

أحتاج إلى البحث في GitHub للعثور على الكود المحدد لـ `etoolbox adjustbox language:YAML`.

واجهت الخطأ التالي:

```
2025-01-07T22:34:58.6493408Z 
2025-01-07T22:34:58.6493741Z ! خطأ في LaTeX: ملف adjustbox.sty غير موجود.
2025-01-07T22:34:58.6494172Z 
2025-01-07T22:34:58.6494593Z اكتب X للخروج أو <RETURN> للمتابعة،
2025-01-07T22:34:58.6495322Z أو أدخل اسمًا جديدًا. (الامتداد الافتراضي: sty)
```

أنا أبحث تحديدًا عن `etoolbox adjustbox language:YAML`، والنتائج في GitHub محدودة، حيث يوجد فقط 53 ملف YAML يحتوي على كل من `etoolbox` و `adjustbox`. أحتاج إلى **تطابق تام**.

على الرغم من أننا في عصر نماذج اللغة الكبيرة، إلا أن الحاجة إلى البحث عن التطابقات الدقيقة لا تزال ضرورية. هذا صحيح بشكل خاص عند التحقق من المعنى الدقيق لشيء ما أو العثور على كود عمل دقيق. وبالمثل، تعتمد منصات مثل Google أو Twitter أو غيرها على عمليات البحث الدقيقة للحصول على المعنى. نحن لا نريد نتائج تم إنشاؤها بواسطة الذكاء الاصطناعي أو نتائج تحتوي على أخطاء طفيفة.

لتدريب نماذج اللغة الكبيرة، يمكننا تطوير نظام يعثر على التطابقات الدقيقة. ربما يمكننا الجمع بين خوارزمية البحث **KMP (Knuth-Morris-Pratt)** وهندسة **المحولات (Transformer Architecture)** لتعزيز قدرات البحث. استخدام خوارزمية KMP مع المحولات قد يساعد في العثور على نتائج أكثر دقة للبحث عن أكواد محددة.

حاليًا، لا تستطيع نماذج اللغة الكبيرة التصفية حسب لغة الملف مثل YAML أو Python. ومع ذلك، يتم تنظيم جزء كبير من المعلومات في العالم الحقيقي بهذه الطريقة. هذا يعني أنه يمكننا تدريب نماذج اللغة الكبيرة باستخدام الملفات. إذا قمنا بتنظيم جميع بيانات النص حسب أنواع الملفات، يمكننا تدريب النموذج على فهمها بشكل أفضل. لذلك، بالنسبة لنماذج اللغة الكبيرة، سنحتاج إلى تحديد لغات الملفات مسبقًا في البداية. بشكل افتراضي، يمكن أن تكون "نص"، ولكن يمكننا أيضًا تحديد لغات أخرى، تمامًا كما يفعل GitHub Search. ستكون النتيجة إرجاع الملفات، تمامًا كما تفعل نتائج بحث GitHub.

الجزء المهم هو **تنسيق الملف** أو **الامتداد**، وليس اسم الملف. إليك بعض الأمثلة:

> بايثون، جافاسكريبت، جافا، روبي، جو، سي++، سي، سي#، تايب سكريبت، HTML، CSS، PHP، سويفت، كوتلن، رست، Objective-C، باش، ماركداون، R، لوا، هاسكل، MATLAB، بيرل، SQL، Dockerfile، YAML، JSON، TOML، VHDL، TeX، LaTeX، Assembly، GraphQL

> .py, .js, .java, .rb, .go, .cpp, .cc, .cxx, .h, .c, .cs, .ts, .html, .htm, .css, .php, .swift, .kt, .kts, .rs, .m, .h, .sh, .md, .r, .lua, .hs, .m, .pl, .pm, .sql, Dockerfile, .yaml, .yml, .json, .toml, .vhdl, .vhd, .tex, .asm, .graphql, .gql

ومع ذلك، عندما يخلط المستخدم بين النص العادي والتعابير والرموز الشبيهة بالملفات في طلبه، يصبح من الصعب إجراء بحث مثل هذا. على سبيل المثال، في منصات مثل Stack Overflow، غالبًا ما تحتوي الأسئلة أو الإجابات على نصوص مختلطة مع مقاطع من التعليمات البرمجية أو تعابير ملفات.

ولكن بالتأكيد، هناك منتجات جديدة يمكننا تخيلها في هذا المجال لسد الفجوة بين البحث باللغة الطبيعية والبحث القائم على الملفات.