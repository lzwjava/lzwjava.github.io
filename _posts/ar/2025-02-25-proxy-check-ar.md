---
audio: true
generated: true
lang: ar
layout: post
title: تنفيذ فحص الوكيل في ويندوز
translated: true
---

لإعداد فحص الوكيل في ويندوز باستخدام Git-Bash و PowerShell، عليك إعداد آليات في كل من هذه القشور لتحديد متى يتم تنفيذ الأوامر المتعلقة بالشبكة و عرض إعدادات الوكيل إذا كانت مهيأة. أدناه الخطوات والشيفرة لكل من Git-Bash و PowerShell. يُرجح أن يشير "الترمينال" إلى Windows Terminal الذي يستضيف هذه القشور، لذلك سنركز على تنفيذات Git-Bash و PowerShell.

---

### **لـ Git-Bash**

Git-Bash هو تقليد Bash على ويندوز، ويمكننا استخدام `DEBUG` trap لإجراء وظيفة قبل تنفيذ كل أمر. الهدف هو التحقق من أن الأمر هو أمر مرتبط بالشبكة، وإذا كانت إعدادات الوكيل مهيأة، فإظهارها.

#### **الخطوات:**

1. **تعريف قائمة الأوامر المتعلقة بالشبكة.**
2. **إنشاء وظيفة لإظهار إعدادات الوكيل.**
3. **إنشاء وظيفة للتحقق من الأمر وإعدادات الوكيل.**
4. **إعداد `DEBUG` trap لإجراء التحقق قبل كل أمر.**
5. **تعريف وظيفة `checkproxy` يدوية لإظهار إعدادات الوكيل حسب الطلب.**
6. **إضافة جميع التكوينات إلى ملف `.bashrc`.**

#### **التنفيذ:**

أضف الشيفرة التالية إلى ملف `~/.bashrc` الخاص بك (إنشئه إذا لم يكن موجودًا):

```bash
# قائمة الأوامر المتعلقة بالشبكة
network_commands=(
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
    "python"
    "glcoud"
)

# وظيفة لإظهار إعدادات الوكيل
display_proxy() {
    echo -e "🚀 **إعدادات الوكيل تم اكتشافها:**"
    [ -n "$HTTP_PROXY" ] && echo "   - HTTP_PROXY: $HTTP_PROXY"
    [ -n "$http_proxy" ] && echo "   - http_proxy: $http_proxy"
    [ -n "$HTTPS_PROXY" ] && echo "   - HTTPS_PROXY: $HTTPS_PROXY"
    [ -n "$https_proxy" ] && echo "   - https_proxy: $https_proxy"
    [ -n "$ALL_PROXY" ] && echo "   - ALL_PROXY: $ALL_PROXY"
    [ -n "$all_proxy" ] && echo "   - all_proxy: $all_proxy"
    echo ""
}

# وظيفة للتحقق من أن الأمر هو أمر مرتبط بالشبكة، وإعدادات الوكيل
proxy_check() {
    local cmd
    # استخراج أول كلمة من الأمر
    cmd=$(echo "$BASH_COMMAND" | awk '{print $1}')

    for network_cmd in "${network_commands[@]}"; do
        if [[ "$cmd" == "$network_cmd" ]]; then
            # التحقق من أن أي متغيرات بيئة الوكيل مهيأة
            if [ -n "$HTTP_PROXY" ] || [ -n "$http_proxy" ] || \
               [ -n "$HTTPS_PROXY" ] || [ -n "$https_proxy" ] || \
               [ -n "$ALL_PROXY" ] || [ -n "$all_proxy" ]; then
                display_proxy
            fi
            break
        fi
    done
}

# تعيين `DEBUG` trap لإجراء `proxy_check` قبل كل أمر
trap 'proxy_check' DEBUG

# وظيفة للتحقق يدوي من إعدادات الوكيل
checkproxy() {
    echo "HTTP_PROXY: $HTTP_PROXY"
    echo "HTTPS_PROXY: $HTTPS_PROXY"
    echo "Git HTTP Proxy:"
    git config --get http.proxy
    echo "Git HTTPS Proxy:"
    git config --get https.proxy
}
```

#### **كيف يعمل:**

- `network_commands` هو مصفوفة لأوامر مرتبطة بالشبكة.
- `display_proxy` يعرض جميع متغيرات بيئة الوكيل ذات الصلة إذا كانت مهيأة.
- `proxy_check` يستخدم `BASH_COMMAND` (متاحة في `DEBUG` trap) للحصول على الأمر الذي يتم تنفيذه، واستخراج أول كلمة، والتحقق من أن الأمر مطابق لأي أمر شبكة. إذا كانت متغيرات الوكيل مهيأة، فإنه يعرضها.
- `trap 'proxy_check' DEBUG` يضمن أن `proxy_check` يعمل قبل كل أمر.
- `checkproxy` يسمح لك بإظهار إعدادات الوكيل يدويًا، بما في ذلك إعدادات الوكيل الخاصة بـ Git.
- بعد إضافة هذا إلى `.bashrc`، أعيد تشغيل Git-Bash أو قم بتشغيل `source ~/.bashrc` لتطبيق التغييرات.

#### **الاستخدام:**

- عندما تقوم بتشغيل أمر شبكة (مثل `git clone`, `curl`), إذا كانت إعدادات الوكيل مهيأة، فإنها ستظهر قبل تنفيذ الأمر.
- قم بتشغيل `checkproxy` لإظهار إعدادات الوكيل يدويًا.

---

### **لـ PowerShell**

PowerShell لا يحتوي على مكافئ مباشر لـ Bash's `DEBUG` trap، ولكن يمكننا استخدام `PSReadLine` module's `CommandValidationHandler` لتحقيق وظائف مماثلة. هذا المعالج يعمل قبل كل أمر، مما يسمح لنا بالتحقق من الأوامر المتعلقة بالشبكة وإعدادات الوكيل.

#### **الخطوات:**

1. **تعريف قائمة الأوامر المتعلقة بالشبكة.**
2. **إنشاء وظيفة لإظهار إعدادات الوكيل.**
3. **إعداد `CommandValidationHandler` للتحقق من الأوامر وإعدادات الوكيل.**
4. **تعريف وظيفة `checkproxy` يدوية لإظهار إعدادات الوكيل حسب الطلب.**
5. **إضافة جميع التكوينات إلى ملف ملف PowerShell الخاص بك.**

#### **التنفيذ:**

أولًا، حدد ملف ملف PowerShell الخاص بك من خلال تشغيل `$PROFILE` في PowerShell. إذا لم يكن موجودًا، قم بإنشائه:

```powershell
New-Item -Type File -Force $PROFILE
```

أضف الشيفرة التالية إلى ملف PowerShell الخاص بك (مثلًا `Microsoft.PowerShell_profile.ps1`):

```powershell
# قائمة الأوامر المتعلقة بالشبكة
$networkCommands = @(
    "gpa",
    "git",
    "ssh",
    "scp",
    "sftp",
    "rsync",
    "curl",
    "wget",
    "apt",
    "yum",
    "dnf",
    "npm",
    "yarn",
    "pip",
    "pip3",
    "gem",
    "cargo",
    "docker",
    "kubectl",
    "ping",
    "traceroute",
    "netstat",
    "ss",
    "ip",
    "ifconfig",
    "dig",
    "nslookup",
    "nmap",
    "telnet",
    "ftp",
    "nc",
    "tcpdump",
    "adb",
    "bundle",
    "brew",
    "cpanm",
    "bundle exec jekyll",
    "make",
    "python",
    "glcoud"
)

# وظيفة لإظهار إعدادات الوكيل
function Display-Proxy {
    Write-Host "🚀 **إعدادات الوكيل تم اكتشافها:**"
    if ($env:HTTP_PROXY) { Write-Host "   - HTTP_PROXY: $env:HTTP_PROXY" }
    if ($env:http_proxy) { Write-Host "   - http_proxy: $env:http_proxy" }
    if ($env:HTTPS_PROXY) { Write-Host "   - HTTPS_PROXY: $env:HTTPS_PROXY" }
    if ($env:https_proxy) { Write-Host "   - https_proxy: $env:https_proxy" }
    if ($env:ALL_PROXY) { Write-Host "   - ALL_PROXY: $env:ALL_PROXY" }
    if ($env:all_proxy) { Write-Host "   - all_proxy: $env:all_proxy" }
    Write-Host ""
}

# إعداد `CommandValidationHandler` للتحقق من الأوامر قبل التنفيذ
Set-PSReadLineOption -CommandValidationHandler {
    param($command)
    # استخراج أول كلمة من الأمر
    $cmd = ($command -split ' ')[0]

    if ($networkCommands -contains $cmd) {
        # التحقق من أن أي متغيرات بيئة الوكيل مهيأة
        if ($env:HTTP_PROXY -or $env:http_proxy -or $env:HTTPS_PROXY -or $env:https_proxy -or $env:ALL_PROXY -or $env:all_proxy) {
            Display-Proxy
        }
    }
    # دائمًا إرجاع `true` لضمان تنفيذ الأمر
    return $true
}

# وظيفة للتحقق يدوي من إعدادات الوكيل
function checkproxy {
    Write-Host "HTTP_PROXY: $env:HTTP_PROXY"
    Write-Host "HTTPS_PROXY: $env:HTTPS_PROXY"
    Write-Host "Git HTTP Proxy:"
    git config --get http.proxy
    Write-Host "Git HTTPS Proxy:"
    git config --get https.proxy
}
```

#### **كيف يعمل:**

- `$networkCommands` هو مصفوفة لأوامر مرتبطة بالشبكة.
- `Display-Proxy` يعرض جميع متغيرات بيئة الوكيل ذات الصلة إذا كانت مهيأة.
- `Set-PSReadLineOption -CommandValidationHandler` يحدد كتلة شيفرة تعمل قبل كل أمر:
  - يستخرج أول كلمة من الأمر.
  - التحقق من أن الأمر موجود في `$networkCommands`.
  - إذا كانت متغيرات الوكيل مهيأة، فإنه يدعو `Display-Proxy`.
  - يرجع `$true` لضمان تنفيذ الأمر.
- `checkproxy` يسمح لك بإظهار إعدادات الوكيل يدويًا، بما في ذلك الوكيل الخاص بـ Git.
- بعد إضافة إلى ملف PowerShell الخاص بك، أعيد تشغيل PowerShell أو قم بتشغيل `. $PROFILE` لتطبيق التغييرات.

#### **المتطلبات:**

- `PSReadLine` module مطلوب، وهو مدمج بشكل افتراضي في PowerShell 5.1 و أحدث.
- إذا كنت تستخدم إصدارًا أقدم، قد تحتاج إلى تحديث PowerShell أو العثور على طريقة بديلة (لا تغطيها هذه الوثيقة، حيث أن معظم الأنظمة تستخدم إصدارات أحدث).

#### **الاستخدام:**

- عندما تقوم بتشغيل أمر شبكة (مثل `git pull`, `curl`), إذا كانت إعدادات الوكيل مهيأة، فإنها ستظهر قبل تنفيذ الأمر.
- قم بتشغيل `checkproxy` لإظهار إعدادات الوكيل يدويًا.

---

### **ملاحظات حول "الترمينال"**

- إذا كان "الترمينال" يشير إلى Windows Terminal، فهو مجرد مستضيف لأشكال مثل Git-Bash، PowerShell، أو Command Prompt (cmd.exe).
- تعمل هذه التنفيذات داخل جلسات Git-Bash أو PowerShell في Windows Terminal.
- تنفيذ وظائف مماثلة في Command Prompt (cmd.exe) غير عملي بسبب قدراته المحدودة في الكتابة، ويوصى باستخدام Git-Bash أو PowerShell بدلاً من ذلك.

---

### **اعتبارات إضافية**

- **تحليل الأوامر:**
  - تحقق كل من هذه التنفيذات فقط أول كلمة من الأمر ضد قائمة الأوامر المتعلقة بالشبكة. على سبيل المثال، `git clone` يثير لأن `git` موجود في القائمة.
  - الأوامر متعددة الكلمات مثل `bundle exec jekyll` ستثير إذا كان `bundle` موجودًا في القائمة، وهو كافي في معظم الحالات.
  - إذا كان ذلك ضروريًا، يمكنك تعديل الشيفرة للتحقق من جميع الكلمات في الأمر، ولكن هذا قد يؤدي إلى نتائج خاطئة إيجابية ويكون غير ضروري في الغالب.

- **متغيرات الوكيل:**
  - تحقق كل من هذه التنفيذات لـ `HTTP_PROXY`, `http_proxy`, `HTTPS_PROXY`, `https_proxy`, `ALL_PROXY`, و `all_proxy` لتغطية التغيرات الشائعة.
  - في ويندوز، متغيرات البيئة غير حساسة للحروف الكبيرة، ولكننا نتحقق من كلا الحروف الكبيرة والصغيرة للتوافق مع السلوك المماثل لـ Unix (خاصة في Git-Bash).

- **إعدادات الوكيل الخاصة بـ Git:**
  - `checkproxy` في كل من القشور يعرض إعدادات الوكيل الخاصة بـ Git باستخدام `git config --get`.

---

### **التجربة**

- **تعيين متغيرات الوكيل:**
  - في Git-Bash: `export HTTP_PROXY=http://proxy.example.com:8080`
  - في PowerShell: `$env:HTTP_PROXY = "http://proxy.example.com:8080"`
- **تشغيل الأوامر المتعلقة بالشبكة:**
  - حاول الأوامر مثل `git --version`, `curl -V`، إلخ.
  - يجب أن تظهر إعدادات الوكيل قبل خروجية الأمر.
- **استخدام `checkproxy`:**
  - قم بتشغيل `checkproxy` في أي قشر لإظهار إعدادات الوكيل يدويًا.

---

توفر هذه التنفيذ فحص الوكيل في كل من Git-Bash و PowerShell، مناسبة للاستخدام في Windows Terminal أو منفردة.