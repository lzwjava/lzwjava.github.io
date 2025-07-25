---
audio: false
generated: false
image: false
lang: hi
layout: post
title: Google क्लाउड सर्वर सेट करना
translated: true
---

Google Cloud में एक प्रॉक्सी सर्वर सेट करने से आप अपने इंटरनेट ट्रैफ़िक को सुरक्षित रूप से एक क्लाउड इंस्टेंस के माध्यम से रूट कर सकते हैं, जिससे गोपनीयता बढ़ती है और प्रतिबंधों को दरकिनार किया जा सकता है। इस गाइड में, हम आपको Google Cloud में एक बेसिक प्रॉक्सी सर्वर सेट करने और ट्रैफ़िक की अनुमति देने के लिए आवश्यक फ़ायरवॉल नियमों को कॉन्फ़िगर करने की प्रक्रिया के बारे में बताएंगे।

## विषय सूची
1. [Google Cloud VM इंस्टेंस बनाना](#creating-a-google-cloud-vm-instance)
2. [प्रॉक्सी सर्वर कॉन्फ़िगर करना](#configuring-the-proxy-server)
3. [फ़ायरवॉल नियम सेट करना](#setting-up-firewall-rules)
4. [प्रॉक्सी सर्वर का परीक्षण](#testing-the-proxy-server)
5. [निष्कर्ष](#conclusion)

---

## Google Cloud VM इंस्टेंस बनाना

प्रॉक्सी सर्वर सेटअप करने से पहले, आपको Google Cloud में एक वर्चुअल मशीन (VM) इंस्टेंस बनाना होगा।

1. Google Cloud Console में लॉग इन करें: [Google Cloud Console](https://console.cloud.google.com/) पर जाएं और अपने खाते में लॉग इन करें।

2. एक नया VM इंस्टेंस बनाएं:
   - Compute Engine > VM instances पर नेविगेट करें।
   - Create Instance पर क्लिक करें।
   - वांछित Region और Machine Type चुनें। सरलता के लिए, आप डिफ़ॉल्ट सेटिंग्स का उपयोग कर सकते हैं या हल्के वजन वाले कॉन्फ़िगरेशन जैसे `e2-micro` इंस्टेंस का चयन कर सकते हैं।
   - Firewall सेक्शन के तहत, वेब एक्सेस को सक्षम करने के लिए Allow HTTP traffic और Allow HTTPS traffic दोनों का चयन करें।

3. SSH एक्सेस सेटअप करें:
   - SSH Keys सेक्शन के तहत, इंस्टेंस को दूरस्थ रूप से एक्सेस करने के लिए अपनी SSH पब्लिक कुंजी जोड़ें। यह बाद में अपने प्रॉक्सी सर्वर को कॉन्फ़िगर करने के लिए महत्वपूर्ण है।

4. अपना VM लॉन्च करने के लिए Create पर क्लिक करें।

VM सेटअप होने के बाद, आप इसे Google Cloud Console से SSH के माध्यम से या टर्मिनल से कनेक्ट कर सकते हैं:

```bash
gcloud compute ssh <आपका-वीएम-नाम>
```

---

## प्रॉक्सी सर्वर को कॉन्फ़िगर करना

एक बार आपका VM सेट हो जाने के बाद, आप अपनी पसंद के किसी भी प्रॉक्सी सर्वर सॉफ़्टवेयर को कॉन्फ़िगर कर सकते हैं। प्रॉक्सी सॉफ़्टवेयर को इंस्टॉल किया जाना चाहिए और इसे वांछित पोर्ट (जैसे, सामान्य प्रॉक्सी सेटअप के लिए `3128`) पर कनेक्शन स्वीकार करने के लिए कॉन्फ़िगर किया जाना चाहिए। सुनिश्चित करें कि सॉफ़्टवेयर रिमोट क्लाइंट से कनेक्शन स्वीकार करता है।

---

## फ़ायरवॉल नियम सेट करना

अपने प्रॉक्सी सर्वर पर ट्रैफ़िक की अनुमति देने के लिए, आपको आवश्यक पोर्ट खोलने के लिए Google Cloud फ़ायरवॉल नियमों को कॉन्फ़िगर करना होगा।

1. Google Cloud Console में फ़ायरवॉल नियमों पर नेविगेट करें:
   - Google Cloud Console में VPC नेटवर्क > फ़ायरवॉल नियम पर जाएं।

2. एक नया फ़ायरवॉल नियम बनाएं:
   - Create Firewall Rule पर क्लिक करें।
   - नियम के लिए एक नाम दर्ज करें, जैसे `allow-proxy-access`।
   - ट्रैफ़िक की दिशा को Ingress (आने वाला ट्रैफ़िक) पर सेट करें।
   - मैच पर कार्रवाई को Allow पर सेट करें।
   - Targets को नेटवर्क में सभी इंस्टेंस या Specified target tags पर सेट करें (यदि आप अधिक नियंत्रण चाहते हैं)।
   - Source IP ranges के तहत, इसे `0.0.0.0/0` पर सेट करें ताकि सभी IP पतों से पहुंच की अनुमति मिल सके, या बेहतर सुरक्षा के लिए इसे विशिष्ट IP या रेंज तक सीमित करें।
   - Protocols and ports के तहत, Specified protocols and ports चुनें और अपने प्रॉक्सी सर्वर द्वारा उपयोग किए जाने वाले पोर्ट को दर्ज करें (उदाहरण के लिए, `tcp:3128`)।

3. फ़ायरवॉल नियम सहेजें:
   नियम कॉन्फ़िगर करने के बाद, फ़ायरवॉल को सक्षम करने के लिए Create पर क्लिक करें।

---

## प्रॉक्सी सर्वर का परीक्षण

फ़ायरवॉल को कॉन्फ़िगर करने के बाद, अब आपके प्रॉक्सी सर्वर का परीक्षण करने का समय है।

1. अपने स्थानीय मशीन से प्रॉक्सी का परीक्षण करें:

आप अपने स्थानीय मशीन के ब्राउज़र या सिस्टम प्रॉक्सी सेटिंग्स को अपने Google Cloud VM के बाहरी IP पते और उस पोर्ट के साथ कॉन्फ़िगर कर सकते हैं जिस पर आपका प्रॉक्सी सर्वर सुन रहा है (उदाहरण के लिए, `3128`)।

2. कमांड लाइन के साथ टेस्ट करें:

   आप `curl` का उपयोग करके प्रॉक्सी को टेस्ट कर सकते हैं, प्रॉक्सी पर्यावरण चर सेट करके:

```bash
export http_proxy=http://<आपका-वीएम-बाहरी-आईपी>:3128
export https_proxy=http://<आपका-वीएम-बाहरी-आईपी>:3128
curl -I http://example.com
```

यदि कनेक्शन सफल होता है, तो आपको वेबसाइट से एक प्रतिक्रिया दिखाई देनी चाहिए।

---

## निष्कर्ष

इस गाइड का पालन करके, आपने Google Cloud पर एक प्रॉक्सी सर्वर सेट करना और इनकमिंग ट्रैफ़िक की अनुमति देने के लिए फ़ायरवॉल नियमों को कॉन्फ़िगर करना सीख लिया है। यह सेटअप आपके इंटरनेट ट्रैफ़िक को सुरक्षित रूप से क्लाउड के माध्यम से रूट करने, नेटवर्क प्रतिबंधों को बायपास करने और गोपनीयता को बढ़ाने का एक आसान तरीका प्रदान करता है।