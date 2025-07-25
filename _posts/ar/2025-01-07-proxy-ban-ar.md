---
audio: false
generated: false
image: false
lang: ar
layout: post
title: تحليل حظر خادم الوكيل
translated: true
---

## هل يمكن لواجهات برمجة التطبيقات (APIs) في خوادم الوكيل تجنب حظر الجدار الناري العظيم (GFW)؟

أقوم بتشغيل خادم بسيط على مثيل Shadowsocks الخاص بي باستخدام الكود التالي:

```python
from flask import Flask, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)  # تمكين CORS لجميع المسارات

@app.route('/bandwidth', methods=['GET'])
def get_bandwidth():
    # تشغيل أمر vnstat للحصول على إحصائيات حركة المرور لفترة 5 دقائق لـ eth0
    result = subprocess.run(['vnstat', '-i', 'eth0', '-5', '--json'], capture_output=True, text=True)
    data = result.stdout

    # إرجاع البيانات التي تم التقاطها كاستجابة JSON
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

وأستخدم nginx لتقديم المنفذ 443 كما هو موضح أدناه:

```bash
server {
    listen 443 ssl;
    server_name www.some-domain.xyz;

    ssl_certificate /etc/letsencrypt/live/www.some-domain.xyz/fullchain.pem; # يتم إدارته بواسطة 
    # ...
    location / {

        proxy_pass http://127.0.0.1:5000/;
        # ...
    }
}
```

يوفر هذا البرنامج الخادم بيانات الشبكة، وأستخدم الخادم كخادم وكيل، مما يسمح لي بعرض حالة الاتصال بالإنترنت على مدونتي باستخدام بيانات الشبكة.

المثير للاهتمام هو أن الخادم لم يتم حظره من قبل الجدار الناري العظيم (GFW) أو أي أنظمة تحكم أخرى في الشبكة لعدة أيام حتى الآن. عادةً، يتم حظر خادم الوكيل الذي أقوم بإعداده في غضون يوم أو يومين. يعمل الخادم على تشغيل برنامج Shadowsocks على منفذ مثل 51939، لذا فهو يعمل مع حركة مرور Shadowsocks مختلطة مع حركة مرور API العادية. يبدو أن هذا المزيج يقود الجدار الناري إلى الاعتقاد بأن الخادم ليس خادم وكيل مخصص، بل خادم عادي، مما يمنعه من حظر عنوان IP.

هذه الملاحظة مثيرة للاهتمام. يبدو أن الجدار الناري يستخدم منطقًا محددًا للتمييز بين حركة مرور الوكيل وحركة المرور العادية. بينما يتم حظر العديد من المواقع مثل Twitter وYouTube في الصين، تظل العديد من المواقع الأجنبية — مثل مواقع الجامعات والشركات الدولية — قابلة للوصول.

يشير هذا إلى أن الجدار الناري يعمل على الأرجح بناءً على قواعد تميز بين حركة مرور HTTP/HTTPS العادية وحركة مرور الوكيل. يبدو أن الخوادم التي تتعامل مع كلا النوعين من حركة المرور تتجنب الحظر، بينما يتم حظر الخوادم التي تتعامل فقط مع حركة مرور الوكيل.

سؤال واحد هو ما هو النطاق الزمني الذي يستخدمه الجدار الناري لتجميع البيانات للحظر — سواء كان يومًا أو ساعة. خلال هذا النطاق الزمني، يكتشف ما إذا كانت حركة المرور تأتي حصريًا من وكيل. إذا كانت كذلك، يتم حظر عنوان IP الخاص بالخادم.

غالبًا ما أزور مدونتي لمراجعة ما كتبته، ولكن في الأسابيع القادمة، سينتقل تركيزي إلى مهام أخرى بدلًا من كتابة منشورات المدونة. سيقلل هذا من وصولي إلى واجهة برمجة التطبيقات `bandwidth` عبر المنفذ 443. إذا وجدت أنني أتعرض للحظر مرة أخرى، يجب أن أكتب برنامجًا للوصول إلى هذه الواجهة بانتظام لخداع الجدار الناري.

## كيفية عمل الجدار الناري العظيم (GFW).

### الخطوة 1: تسجيل الطلبات

```python
import time

# قاعدة بيانات لتخزين بيانات الطلبات
request_log = []

# دالة لتسجيل الطلبات
def log_request(source_ip, target_ip, target_port, body):
    request_log.append({
        'source_ip': source_ip,
        'target_ip': target_ip,
        'target_port': target_port,
        'body': body,
        'timestamp': time.time()
    })
```

تسجل دالة `log_request` الطلبات الواردة مع معلومات أساسية مثل عنوان IP المصدر، عنوان IP الهدف، منفذ الهدف، نص الطلب، والطابع الزمني.

### الخطوة 2: التحقق وحظر عناوين IP

```python
# دالة للتحقق من الطلبات وحظر عناوين IP
def check_and_ban_ips():
    banned_ips = set()

    # التكرار عبر جميع الطلبات المسجلة
    for request in request_log:
        if is_illegal(request):
            banned_ips.add(request['target_ip'])
        else:
            banned_ips.discard(request['target_ip'])

    # تطبيق الحظر على جميع عناوين IP المحددة
    ban_ips(banned_ips)
```

تكرر دالة `check_and_ban_ips` عبر جميع الطلبات المسجلة، وتحدد وتحظر عناوين IP المرتبطة بأنشطة غير قانونية.

### الخطوة 3: تحديد ما يجعل الطلب غير قانوني

```python
# دالة لمحاكاة التحقق مما إذا كان الطلب غير قانوني
def is_illegal(request):
    # مكان للتحقق الفعلي من منطق الطلب غير القانوني
    # على سبيل المثال، التحقق من نص الطلب أو الهدف
    return "illegal" in request['body']
```

هنا، تتحقق دالة `is_illegal` مما إذا كان نص الطلب يحتوي على كلمة "illegal". يمكن توسيع هذا ليشمل منطقًا أكثر تطورًا اعتمادًا على ما يعتبر نشاطًا غير قانوني.

### الخطوة 4: حظر عناوين IP المحددة

```python
# دالة لحظر قائمة من عناوين IP
def ban_ips(ip_set):
    for ip in ip_set:
        print(f"حظر عنوان IP: {ip}")
```

بمجرد تحديد عناوين IP غير القانونية، تقوم دالة `ban_ips` بحظرها عن طريق طباعة عناوين IP الخاصة بها (أو في نظام حقيقي، يمكن أن تقوم بحظرها).

### الخطوة 5: طريقة بديلة للتحقق وحظر عناوين IP بناءً على 80% من الطلبات غير القانونية

```python
# دالة للتحقق من الطلبات وحظر عناوين IP بناءً على 80% من الطلبات غير القانونية
def check_and_ban_ips():
    banned_ips = set()
    illegal_count = 0
    total_requests = 0

    # التكرار عبر جميع الطلبات المسجلة
    for request in request_log:
        total_requests += 1
        if is_illegal(request):
            illegal_count += 1

    # إذا كانت 80% أو أكثر من الطلبات غير قانونية، يتم حظر تلك العناوين
    if total_requests > 0 and (illegal_count / total_requests) >= 0.8:
        for request in request_log:
            if is_illegal(request):
                banned_ips.add(request['target_ip'])

    # تطبيق الحظر على جميع عناوين IP المحددة
    ban_ips(banned_ips)
```

تقيّم هذه الطريقة البديلة ما إذا كان يجب حظر عنوان IP بناءً على نسبة الطلبات غير القانونية. إذا كانت 80% أو أكثر من الطلبات من عنوان IP غير قانونية، يتم حظره.

### الخطوة 6: تحسين التحقق من الطلبات غير القانونية (مثل اكتشاف بروتوكول Shadowsocks وTrojan)

```python
def is_illegal(request):
    # التحقق مما إذا كان الطلب يستخدم بروتوكول Shadowsocks (نص الطلب يحتوي على بيانات تشبه الثنائية)
    if request['target_port'] == 443:
        if is_trojan(request):
            return True
    elif is_shadowsocks(request):
        return True
    return False
```

تقوم دالة `is_illegal` الآن أيضًا بالتحقق من بروتوكولات محددة مثل Shadowsocks وTrojan:
- **Shadowsocks**: قد نتحقق من وجود بيانات مشفرة أو تشبه الثنائية في نص الطلب.
- **Trojan**: إذا جاء الطلب عبر المنفذ 443 (HTTPS) وطابق أنماطًا محددة (مثل خصائص حركة مرور Trojan)، يتم تمييزه على أنه غير قانوني.

### الخطوة 7: مثال على الطلبات القانونية

على سبيل المثال، الطلبات مثل `GET https://some-domain.xyz/bandwidth` هي بالتأكيد قانونية ولن تؤدي إلى تفعيل آلية الحظر.

### الخطوة 8: خصائص حركة مرور خادم الوكيل

تتمتع خوادم الوكيل بخصائص حركة مرور مختلفة تمامًا مقارنة بخوادم الويب أو واجهات برمجة التطبيقات العادية. يحتاج الجدار الناري إلى التمييز بين حركة مرور خادم الويب العادي وحركة مرور خادم الوكيل، والتي يمكن أن تبدو مختلفة تمامًا.

### الخطوة 9: نماذج التعلم الآلي والذكاء الاصطناعي للكشف الذكي

نظرًا لتنوع الطلبات والاستجابات التي تمر عبر الإنترنت، يمكن أن يستخدم الجدار الناري نماذج الذكاء الاصطناعي والتعلم الآلي لتحليل أنماط حركة المرور والكشف بذكاء عن السلوك غير القانوني. من خلال تدريب النظام على مجموعة متنوعة من أنواع حركة المرور واستخدام تقنيات متقدمة، يمكنه حظر أو تصفية حركة المرور بشكل أكثر فعالية بناءً على الأنماط الملاحظة.

## تحديث

على الرغم من جهودي، يستمر حظر خادم الوكيل الخاص بي. للتخفيف من هذا، قمت بتنفيذ حل بديل باستخدام ميزة IP المعكوس من Digital Ocean، والتي تسمح لي بتعيين عنوان IP جديد بسرعة كلما حدث حظر.