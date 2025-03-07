---
audio: true
generated: false
lang: hi
layout: post
title: काम
translated: true
---

- कोड रिपॉजिटरी तक पहुंचने से पहले, सहयोगियों से `pom.xml` फ़ाइल मांगे और Nexus dependencies डाउनलोड करने की कोशिश करें।

- वास्तविक कोड के बिना, लेकिन Nexus लाइब्रेरियों के साथ, हम वास्तव में JAR को डीकम्पाइल कर सकते हैं या लाइब्रेरियों के साथ प्रयोग कर सकते हैं। हम काफी कुछ कर सकते हैं। बॉक्स के बाहर सोचें।

- Sonatype Nexus Repository में `settings.yaml` में User Tokens को कॉन्फ़िगर करने का प्राथमिकता है।

- एक्सेस रिक्वेस्ट टिकेट की अनुमति के इंतजार न करें। जब तक आप एक्सेस अधिकार नहीं पाते, सोचें कि आप क्या कर सकते हैं।

- अधिकांश काम शुरू करने से पहले किया जा सकता है। कोई भी लगभग सब कुछ पहले से ही परिचित हो सकता है। सब कुछ ओपन-सोर्स कोड या सामग्री की प्रतिस्थापन है।

- एक काम में विशेष सेटिंग्स, थोड़ा अलग कोड लॉजिक, और काम करने के लिए चीजों को करने के लिए एक्सेस अधिकार या पासवर्ड शामिल होते हैं।

- अगले चरण को भविष्यदृष्टि में रखें। वर्तमान परियोजना कैसे आगे बढ़ेगी और उपयोगकर्ताओं को क्या चाहिए या अपेक्षित है, सोचें।

- काम करने के सभी संभव तरीकों को सोचें, प्रगति करें और जितना संभव हो सके, आप एक्सेस अधिकार या दूसरों द्वारा प्रदान की जाने वाली सामग्री प्राप्त करने से पहले तैयार हों।

- संतुष्ट न हों; चीजें कराएं और जितना संभव हो सके, ऑटोमेट करें।

- Python `requests` लाइब्रेरी का उपयोग Postman के स्थान पर करें।

- Windows और PowerShell भी वैध विकल्प हैं। आमतौर पर उपयोग किए जाने वाले कमांडों की संख्या कुछ दर्जनों तक सीमित है। उन्हें अच्छी तरह से सीखें।

- एक इंजीनियर इस परियोजना पर 5 या 10 साल काम कर सकता है, और सोचें कि कैसे आप तेजी से समान दक्षता प्राप्त कर सकते हैं।

- नोट्स और लॉग डायरेक्टरी का उपयोग करें। कंसोल या फ्रंटएंड पेजों से लॉग्स को सावधानी से कॉपी करें, विस्तृत विश्लेषण के लिए।

- नए टीम सदस्यों को इस ज्ञान को कैसे संचारित किया जाए, सोचें।

- सोचें कि अगर सभी अपने सर्वश्रेष्ठ करते हैं और हम 50 ऐसे इंजीनियरों हैं, तो हम क्या प्राप्त कर सकते हैं।

- जो लाइब्रेरियां आसानी से आंतरिक Nexus रिपॉजिटरी से डाउनलोड की जा सकती हैं, उन्हें मैन्युअल रूप से डाउनलोड कर `.m2` रिपॉजिटरी में रखें।

- `pom.xml` फ़ाइल को पढ़ें ताकि परियोजना के लिए Maven कॉम्पाइल टारगेट और आवश्यक JDK संस्करण को निर्धारित किया जा सके।

- Jira या Confluence खोजने के बजाय, सीधे URL बनाएं ताकि प्रोफ़ाइल पर जाएं और पेजों को खोजें।

- अगर हम एक बग से सामना करते हैं, उदाहरण के लिए अगर `npm run build` में एक बड़े बिल्ड पाइपलाइन में समस्याएं हैं, तो हम इसे अलग से चलाएं ताकि पूरा पाइपलाइन चलाने से पहले यह काम करे। इससे डिबग साइकिल तेज और छोटा हो जाता है।

- आपके करियर के दौरान, समस्याएं या समान बग बार-बार दोहराएंगे, इसलिए इनके बारे में नोट्स रखें। यह अभ्यास AI युग में भी उपयोगी रहता है। कभी-कभी, बड़े भाषा मॉडल जो जवाब देते हैं, वे पूरी तरह से सही नहीं होते हैं और आपको उन्हें सत्यापित करना पड़ता है।

- कुछ बड़े कंपनियों में, AI चैटबॉट्स या आंतरिक AI टूल्स की प्रगति धीमी हो सकती है। हम अपने व्यक्तिगत कंप्यूटर का उपयोग कर सकते हैं ताकि कार्य के बाद संबंधित सार्वजनिक तकनीकों के साथ AI टूल्स सीखें। इससे कॉर्पोरेट कंप्यूटर पर काम करना कम कठिन हो जाता है क्योंकि हम पहले से ही काफी से परिचित हैं।