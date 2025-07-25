---
audio: false
generated: false
image: true
lang: ar
layout: post
title: عرض إعدادات الوكيل قبل تنفيذ الأوامر
translated: true
---

<div style="text-align: center;">  
    <img class="responsive" src="/assets/images/preexec/pe1.png" alt="prexec" />  
</div>

العيش في الصين أو العمل في شركات تستخدم شبكات VPN والوكلاء (proxies) يمكن أن يعقد عملية تطوير البرمجيات. نسيان تكوين هذه الإعدادات غالبًا ما يؤدي إلى مشاكل في الاتصال. لتبسيط سير العمل الخاص بك، قمت بإنشاء نص برمجي بسيط باستخدام Zsh بمساعدة ChatGPT يعرض تلقائيًا إعدادات الوكيل الخاص بك عند تشغيل أوامر معينة تعتمد على الشبكة.

## لماذا عرض إعدادات الوكيل؟

الوكلاء (Proxies) وشبكات VPN ضرورية للوصول إلى الموارد الخارجية بشكل آمن. عرض إعدادات الوكيل الخاص بك قبل تنفيذ الأوامر التي تعتمد على الشبكة يساعدك على تحديد مشكلات الاتصال وحلها بسرعة.

## النص البرمجي

هذا النص يستخدم وظيفة `preexec` في Zsh للتحقق مما إذا كانت الأمر القادم يعتمد على الشبكة. إذا كان الأمر كذلك وتم تعيين متغيرات البيئة للبروكسي، فإنه يعرض إعدادات البروكسي الحالية.

```bash
# دالة للتحقق من إعدادات الوكيل وعرضها قبل تنفيذ أوامر معينة
preexec() {
    # تعريف الأوامر التي تعتمد على الشبكة
    local network_commands=(
        "gpa"
        "git"
        "ssh"
        "scp"
        "sftp"
        "rsync"
        "curl"
        "wget"
        "apt"
        "yum"
        "dnf"
        "npm"
        "yarn"
        "pip"
        "pip3"
        "gem"
        "cargo"
        "docker"
        "kubectl"
        "ping"
        "traceroute"
        "netstat"
        "ss"
        "ip"
        "ifconfig"
        "dig"
        "nslookup"
        "nmap"
        "telnet"
        "ftp"
        "nc"
        "tcpdump"
        "adb"
        "bundle"
        "brew"
        "cpanm"
        "bundle exec jekyll"
        "make"
        # إضافة المزيد من الأوامر حسب الحاجة
    )
```

```bash
# استخراج الكلمة الأولى (الأمر) من سطر الأوامر
local cmd
cmd=$(echo "$1" | awk '{print $1}')
```

    # دالة لعرض متغيرات البروكسي
    display_proxy() {
        echo -e "\n🚀 تم اكتشاف إعدادات البروكسي:"

```bash
[ -n "$HTTP_PROXY" ] && echo "   - HTTP_PROXY: $HTTP_PROXY"
[ -n "$http_proxy" ] && echo "   - http_proxy: $http_proxy"
[ -n "$HTTPS_PROXY" ] && echo "   - HTTPS_PROXY: $HTTPS_PROXY"
[ -n "$https_proxy" ] && echo "   - https_proxy: $https_proxy"
[ -n "$ALL_PROXY" ] && echo "   - ALL_PROXY: $ALL_PROXY"
[ -n "$all_proxy" ] && echo "   - all_proxy: $all_proxy"
```

```bash
echo ""
```

```bash
    # التحقق مما إذا كانت الأمر يعتمد على الشبكة
    for network_cmd in "${network_commands[@]}"; do
        if [[ "$1" == "$network_cmd"* ]]; then
            if [ -n "$HTTP_PROXY" ] || [ -n "$http_proxy" ] || \
               [ -n "$HTTPS_PROXY" ] || [ -n "$https_proxy" ] || \
               [ -n "$ALL_PROXY" ] || [ -n "$all_proxy" ]; then
                
                display_proxy
            fi
            break
        fi
    done
}
```

## إعداد النص البرمجي في Zsh

### 1. افتح ملف `.zshrc` الخاص بك

استخدم محرر النصوص المفضل لديك لفتح ملف التهيئة `.zshrc`. على سبيل المثال:

```bash
nano ~/.zshrc
``` 

(ملاحظة: الأوامر البرمجية مثل `nano ~/.zshrc` لا تُترجم، حيث أنها أوامر تقنية تُستخدم كما هي في جميع اللغات.)

### 2. إضافة دالة `preexec`

الصق النص البرمجي أعلاه في نهاية الملف.

### 3. حفظ وإغلاق

اضغط `CTRL + O` لحفظ الملف و `CTRL + X` للخروج.

### 4. تطبيق التغييرات

قم بإعادة تحميل ملف `.zshrc` لتطبيق التكوين الجديد على الفور:

```bash
source ~/.zshrc
```

## اختبار الإعدادات

### 1. مع تفعيل الوكيل (Proxy)

قم بتعيين متغير الوكيل مؤقتًا وتنفيذ أمر يعتمد على الشبكة باستخدام `pip`:

```bash
export HTTP_PROXY="http://127.0.0.1:7890"
pip install selenium beautifulsoup4 urllib3
```

الإخراج المتوقع:

```

🚀 تم الكشف عن إعدادات البروكسي:
   - HTTP_PROXY: http://127.0.0.1:7890
   - http_proxy: 127.0.0.1:7890
   - HTTPS_PROXY: 127.0.0.1:7890
   - https_proxy: 127.0.0.1:7890
   - ALL_PROXY: 127.0.0.1:7890
   - all_proxy: 127.0.0.1:7890

جمع حزمة selenium
  يتم تنزيل selenium-4.x.x-py2.py3-none-any.whl (xxx كيلوبايت)
جمع حزمة beautifulsoup4
  يتم تنزيل beautifulsoup4-4.x.x-py3-none-any.whl (xxx كيلوبايت)
جمع حزمة urllib3
  يتم تنزيل urllib3-1.x.x-py2.py3-none-any.whl (xxx كيلوبايت)
...
```

### 2. بدون تفعيل الوكيل (Proxy)

قم بإلغاء تعيين متغير الوكيل (proxy) وقم بتشغيل أمر `pip` نفسه:

```bash
unset HTTP_PROXY
pip install selenium beautifulsoup4 urllib3
```

الإخراج المتوقع:

```
جمع selenium
  يتم تنزيل selenium-4.x.x-py2.py3-none-any.whl (xxx كيلوبايت)
جمع beautifulsoup4
  يتم تنزيل beautifulsoup4-4.x.x-py3-none-any.whl (xxx كيلوبايت)
جمع urllib3
  يتم تنزيل urllib3-1.x.x-py2.py3-none-any.whl (xxx كيلوبايت)
...
```

*(لا ينبغي أن تظهر أي إشعارات تتعلق بالوكيل.)*

### 3. أمر غير متعلق بالشبكة

قم بتنفيذ أمر محلي مثل `ls`:

```bash
ls
```

الإخراج المتوقع:

```
[قائمة الملفات والدلائل]
```

*(لا ينبغي أن تظهر أي إشعارات تتعلق بالوكيل.)*

## التخصيص

- توسيع `network_commands`: أضف أي أوامر إضافية تعتمد على الشبكة إلى مصفوفة `network_commands`.

- التعامل مع الأسماء المستعارة: تأكد من تضمين أي أسماء مستعارة للأوامر المعتمدة على الشبكة في قائمة `network_commands`.

  ```bash
  alias gpa='git push all'
  ```

تم تعيين اسم مستعار (alias) في سطر الأوامر باستخدام الأمر `alias`، حيث يتم تعيين الأمر `gpa` ليقوم بتنفيذ `git push all`. هذا يعني أنه عند كتابة `gpa` في سطر الأوامر، سيتم تنفيذ `git push all` تلقائيًا.

أضف `"gpa"` إلى مصفوفة `network_commands` لتفعيل إشعارات البروكسي عند استخدام هذا الاسم المستعار.

- تعزيز الرؤية باستخدام الألوان:

لتحسين الرؤية، خاصة في المحطات المزدحمة، يمكنك إضافة لون إلى إشعارات الوكيل:

  ```bash
  # أضف رموز الألوان في أعلى ملف .zshrc الخاص بك
  GREEN='\033[0;32m'
  NC='\033[0m' # بدون لون
```

  display_proxy() {
      echo -e "\n${GREEN}🚀 تم الكشف عن إعدادات البروكسي:${NC}"

```bash
[ -n "$HTTP_PROXY" ] && echo "   - HTTP_PROXY: $HTTP_PROXY"
[ -n "$http_proxy" ] && echo "   - http_proxy: $http_proxy"
[ -n "$HTTPS_PROXY" ] && echo "   - HTTPS_PROXY: $HTTPS_PROXY"
[ -n "$https_proxy" ] && echo "   - https_proxy: $https_proxy"
[ -n "$ALL_PROXY" ] && echo "   - ALL_PROXY: $ALL_PROXY"
[ -n "$all_proxy" ] && echo "   - all_proxy: $all_proxy"
```

      echo ""
  }
  ```

## الخلاصة

إدارة إعدادات الوكيل (Proxy) أمر بالغ الأهمية لتطوير البرمجيات بسلاسة في بيئات الشبكات المقيدة. يضمن هذا النص البرمجي لـ Zsh أن تكون دائمًا على علم بإعدادات الوكيل الخاصة بك عند تشغيل الأوامر التي تتطلب الوصول إلى الشبكة، مما يعزز من سير عملك وكفاءة استكشاف الأخطاء وإصلاحها.

برمجة سعيدة! 🚀