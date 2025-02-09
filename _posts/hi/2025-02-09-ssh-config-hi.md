---
audio: true
lang: hi
layout: post
title: SSH विन्यास
translated: true
---

यह `ssh-config` फ़ाइल SSH क्लाइंट के व्यवहार को कॉन्फ़िगर करती है। आइए प्रत्येक भाग को समझें:

- `Host * !192.*.*.*`: यह खंड सभी होस्ट पर लागू होता है *सिवाय* उन होस्ट के जो `192.*.*.*` पैटर्न (आमतौर पर, स्थानीय नेटवर्क पते) से मेल खाते हैं।
    - `ProxyCommand corkscrew localhost 7890 %h %p`: यह मुख्य भाग है। यह SSH को लक्ष्य होस्ट से कनेक्ट करने के लिए `corkscrew` प्रोग्राम का उपयोग करने के लिए कहता है।
        - `corkscrew`: एक उपकरण जो आपको HTTP या HTTPS प्रॉक्सी के माध्यम से SSH कनेक्शन टनल करने की अनुमति देता है।
        - `localhost 7890`: प्रॉक्सी सर्वर का पता (`localhost`) और पोर्ट (`7890`) निर्दिष्ट करता है। यह मानता है कि आपके पास आपके स्थानीय मशीन पर चल रहा एक प्रॉक्सी सर्वर है, जो पोर्ट 7890 (जैसे, Shadowsocks, एक SOCKS प्रॉक्सी, या कोई अन्य टनलिंग समाधान) पर सुन रहा है।
        - `%h`: एक विशेष SSH चर जो उस लक्ष्य होस्टनाम में विस्तारित होता है जिससे आप कनेक्ट करने का प्रयास कर रहे हैं।
        - `%p`: एक और SSH चर जो लक्ष्य पोर्ट (आमतौर पर SSH के लिए 22) में विस्तारित होता है।
    - संक्षेप में, यह `Host` ब्लॉक स्थानीय नेटवर्क को छोड़कर सभी कनेक्शनों के लिए `corkscrew` प्रॉक्सी का उपयोग करने के लिए SSH को कॉन्फ़िगर करता है।

- `Host *`: यह खंड *सभी* होस्ट पर लागू होता है।
    - `UseKeychain yes`: macOS पर, यह SSH को आपके Keychain से SSH कुंजियों को संग्रहीत करने और पुनः प्राप्त करने के लिए कहता है, ताकि आपको हर बार अपना पासवर्ड दर्ज न करना पड़े।
    - `AddKeysToAgent yes`: यह स्वचालित रूप से आपके SSH कुंजियों को SSH एजेंट में जोड़ता है, ताकि आपको प्रत्येक रिबूट के बाद उन्हें मैन्युअल रूप से जोड़ना न पड़े।
    - `IdentityFile ~/.ssh/id_rsa`: आपकी निजी SSH कुंजी फ़ाइल का पथ निर्दिष्ट करता है। `~/.ssh/id_rsa` RSA निजी कुंजी के लिए डिफ़ॉल्ट स्थान है।

**संक्षेप में, यह कॉन्फ़िगरेशन स्थानीय नेटवर्क पर उन कनेक्शनों को छोड़कर सभी SSH कनेक्शनों के लिए एक प्रॉक्सी सेट करता है, और यह सुविधा के लिए कुंजी प्रबंधन को कॉन्फ़िगर करता है।**


```bash
Host * !192.*.*.*
    ProxyCommand corkscrew localhost 7890 %h %p
Host *
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
```
