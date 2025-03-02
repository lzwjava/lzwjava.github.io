---
audio: false
generated: true
lang: hi
layout: post
title: फ़ाइल अपलोड
translated: true
---

### मुख्य बिंदु
- अनुसंधान से पता चलता है कि HTTP फ़ाइल अपलोड आमतौर पर वेब फॉर्म के लिए POST विधि का उपयोग करते हैं, जिसमें multipart/form-data शामिल है, जिससे कई फ़ाइलें और अतिरिक्त डेटा भेजा जा सकता है।
- PUT विधि भी फ़ाइलें अपलोड कर सकती है, जो कि raw content को सीधे भेजती है, जो RESTful APIs में सरलता के लिए अक्सर उपयोग होती है।
- सबूत दोनों विधियों को वैध मानने की ओर इशारा करता है, जिसमें सर्वर की सेटिंग और उपयोग के मामले का निर्णय होता है।

### सारांश
HTTP के माध्यम से फ़ाइलें अपलोड करना ऑनलाइन डेटा शेयर करने के लिए एक आम कार्य है, जैसे कि फोटो या दस्तावेज़ वेबसाइट पर भेजना। इसे दो मुख्य तरीकों से किया जा सकता है: POST विधि का उपयोग करने के साथ एक विशेष फ़ॉर्मेट multipart/form-data, जो वेब फॉर्म के लिए अच्छा है, या PUT विधि का उपयोग, जो सरल है और आधुनिक APIs में अक्सर उपयोग होती है। प्रत्येक विधि अपनी सेटिंग रखती है, और सही चुनाव उस पर निर्भर करता है कि सर्वर कैसे सेट किया गया है और आप क्या कर रहे हैं।

### यह कैसे काम करता है
- **POST with Multipart/Form-Data**: यह अपने फ़ाइल और किसी अतिरिक्त जानकारी (जैसे कि विवरण) को अलग-अलग हिस्सों में पैक करने जैसा है, जो एक अनोखे सीमा रेखा से चिह्नित है। यह वेब फॉर्मों में आम है जहां आप फ़ाइलें अपलोड करने के लिए चुनते हैं।
- **PUT विधि**: यह फ़ाइल सामग्री को सीधे एक विशेष URL पर भेजती है, जैसे कि सर्वर पर फ़ाइल को अपडेट करना। यह सरल है लेकिन इसे सर्वर को इसे समर्थन करने की आवश्यकता होती है।

### अप्रत्याशित विवरण
आप शायद यह नहीं सोचेंगे कि PUT विधि, जो आमतौर पर डेटा को अपडेट करने के लिए होती है, फ़ाइल अपलोड भी संभाल सकती है, विशेष रूप से APIs में, जिससे यह पारंपरिक फॉर्मों से परे एक बहुमुखी विकल्प बन जाता है।

---

### सर्वेक्षण नोट: HTTP फ़ाइल अपलोड का विस्तृत व्याख्या

HTTP के माध्यम से फ़ाइलें अपलोड करना वेब विकास में एक मूल कार्य है, जिससे उपयोगकर्ता सर्वरों के साथ डेटा जैसे कि छवियां, दस्तावेज़ या मीडिया शेयर कर सकते हैं। इस प्रक्रिया को दो प्राथमिक तरीकों से पूरा किया जा सकता है: POST विधि के साथ multipart/form-data एन्कोडिंग, जो आमतौर पर वेब फॉर्मों के लिए उपयोग होती है, और PUT विधि, जो RESTful APIs में सीधे फ़ाइल सामग्री के लिए अक्सर उपयोग होती है। नीचे, हम इन विधियों को गहनता से जांचते हैं, जिसमें उनके संरचना, कार्यान्वयन और विचार शामिल हैं, ताकि दोनों तकनीकी और गैर-तकनीकी दर्शकों के लिए एक व्यापक समझ प्रदान की जा सके।

#### Multipart/Form-Data: वेब फॉर्मों के लिए मानक

Multipart/form-data सामग्री प्रकार HTTP फ़ाइल अपलोड के लिए मानक विकल्प है, विशेष रूप से HTML फॉर्मों के साथ काम करते समय। यह विधि एक ही अनुरोध में कई फ़ाइलों और अतिरिक्त फॉर्म डेटा, जैसे कि टेक्स्ट फ़ील्डों, के साथ-साथ भेजने की अनुमति देता है। इस प्रक्रिया में एक अनुरोध शरीर का निर्माण होता है जो अलग-अलग हिस्सों में विभाजित होता है, प्रत्येक को एक अनोखे सीमा रेखा से अलग किया जाता है, जिससे सर्वर अलग-अलग डेटा टुकड़ों को पहचान सकता है।

##### संरचना और उदाहरण
अनुरोध शुरू होता है `Content-Type` हेडर को `multipart/form-data; boundary=boundary_string` पर सेट करके, जहां `boundary_string` एक अकस्मात् चुनी गई रेखा है ताकि फ़ाइल सामग्री के साथ टकराव से बचा जा सके। शरीर के प्रत्येक हिस्से में हेडर जैसे `Content-Disposition`, जो फॉर्म फ़ील्ड नाम और फ़ाइल के लिए फ़ाइल नाम को निर्दिष्ट करता है, और `Content-Type`, जो डेटा प्रकार को संकेत करता है (जैसे कि `text/plain` टेक्स्ट फ़ाइलों के लिए, `image/jpeg` JPEG छवियों के लिए)। हिस्सा सीमा रेखा से समाप्त होता है, और अंतिम हिस्सा सीमा के बाद दो हाइफन से चिह्नित होता है।

`example.txt` नामक फ़ाइल को "Hello, world!" के साथ [इस एंडपॉइंट](https://example.com/upload) पर अपलोड करने के लिए, फॉर्म फ़ील्ड नाम "file" के साथ, HTTP अनुरोध इस प्रकार दिखेगा:

```
POST /upload HTTP/1.1
Host: example.com
Content-Type: multipart/form-data; boundary=abc123
Content-Length: 101

--abc123
Content-Disposition: form-data; name="file"; filename="example.txt"
Content-Type: text/plain

Hello, world!
--abc123--
```

यहां, `Content-Length` 101 बाइट्स के रूप में गणना की जाती है, सीमा, हेडर और फ़ाइल सामग्री को शामिल करते हुए, और लाइन एंडिंग आमतौर पर CRLF (`\r\n`) के लिए सही HTTP फॉर्मेटिंग के लिए उपयोग होती है।

##### कई फ़ाइलें और फॉर्म फ़ील्डों का संचालन
इस विधि में अतिरिक्त मेटाडेटा की आवश्यकता होती है। उदाहरण के लिए, यदि एक फ़ाइल के साथ एक विवरण अपलोड किया जा रहा है, तो अनुरोध शरीर में कई हिस्से शामिल हो सकते हैं:

```
--abc123
Content-Disposition: form-data; name="description"

यह मेरा फ़ाइल है
--abc123
Content-Disposition: form-data; name="file"; filename="example.txt"
Content-Type: text/plain

Hello, world!
--abc123--
```

हर हिस्से का सामग्री संरक्षित रहता है, जिसमें कोई भी नया लाइन शामिल है, और सीमा अलगाव सुनिश्चित करती है। यह फ्लेक्सिबिलिटी इसे `<input type="file">` तत्वों वाले वेब फॉर्मों के लिए आदर्श बनाती है।

#### PUT विधि: RESTful APIs के लिए सीधे फ़ाइल अपलोड

PUT विधि एक सरल विकल्प प्रदान करती है, विशेष रूप से RESTful API सन्दर्भों में, जहां लक्ष्य है कि फ़ाइल सामग्री के साथ एक संसाधन को अपडेट या बनाना। multipart/form-data के विपरीत, PUT raw फ़ाइल डेटा को सीधे अनुरोध शरीर में भेजती है, ओवरहेड को कम करती है और सर्वर-साइड प्रोसेसिंग को सरल बनाती है।

##### संरचना और उदाहरण
`example.txt` को [इस URL](https://example.com/files/123) पर अपलोड करने के लिए, अनुरोध होगा:

```
PUT /files/123 HTTP/1.1
Host: example.com
Content-Type: text/plain
Content-Length: 13

Hello, world!
```

यहां, `Content-Type` फ़ाइल के MIME प्रकार को संकेत करता है (जैसे कि `text/plain`), और `Content-Length` फ़ाइल का आकार बाइट में है। यह विधि बड़ी फ़ाइलों के लिए दक्ष है, क्योंकि यह multipart/form-data के एन्कोडिंग ओवरहेड से बचती है, लेकिन इसे सर्वर को PUT अनुरोधों के लिए फ़ाइल अपलोडों को संभालने के लिए सेट किया जाना चाहिए।

##### उपयोग के मामले और विचार
PUT अक्सर ऐसे मामलों में उपयोग होती है जैसे कि उपयोगकर्ता अवतार अपडेट करना या API में एक विशेष संसाधन में फ़ाइल अपलोड करना। हालांकि, सभी सर्वर PUT के लिए फ़ाइल अपलोडों को डिफ़ॉल्ट रूप से समर्थन नहीं करते, विशेष रूप से शेयर्ड होस्टिंग वातावरणों में, जहां POST के साथ multipart/form-data अधिक सार्वभौमिक रूप से स्वीकार्य है। सर्वर सेटिंग, जैसे कि Apache में PUT verb को सक्षम करना, आवश्यक हो सकता है, जैसा कि [PHP Manual on PUT method support](https://www.php.net/manual/en/features.file-upload.put-method.php) में उल्लेख किया गया है।

#### तुलनात्मक विश्लेषण

दोनों विधियों के बीच अंतरों को समझाने के लिए, नीचे दिए गए तालिका में दोनों विधियों की तुलना की गई है:

| पहलू                  | POST के साथ Multipart/Form-Data          | Raw Content के साथ PUT                  |
|-------------------------|----------------------------------------|---------------------------------------|
| **उपयोग के मामले**            | वेब फॉर्म, कई फ़ाइलें, मेटाडेटा    | RESTful APIs, एकल फ़ाइल अपडेट     |
| **जटिलता**          | अधिक (सीमा प्रबंधन, कई हिस्से) | कम (सीधे सामग्री)               |
| **दक्षता**          | मध्यम (एन्कोडिंग ओवरहेड)           | अधिक (कोई एन्कोडिंग नहीं)                 |
| **सर्वर समर्थन**      | व्यापक रूप से समर्थित                      | सेटिंग की आवश्यकता हो सकती है            |
| **उदाहरण हेडर**     | `Content-Type: multipart/form-data; boundary=abc123` | `Content-Type: text/plain`           |
| **अनुरोध शरीर**        | सीमा से अलग हिस्से          | Raw फ़ाइल सामग्री                     |

इस तालिका से पता चलता है कि जबकि multipart/form-data वेब इंटरैक्शंस के लिए अधिक बहुमुखी है, PUT API-ड्राइव अपलोडों के लिए अधिक दक्ष है, सर्वर क्षमताओं पर निर्भर करता है।

#### कार्यान्वयन विवरण और चूक

##### सीमा चयन और फ़ाइल सामग्री
Multipart/form-data में सीमा रेखा चुनना फ़ाइल सामग्री के साथ टकराव से बचने के लिए महत्वपूर्ण है। यदि सीमा फ़ाइल के भीतर दिखाई दे, तो यह पर्सिंग त्रुटियों को पैदा कर सकती है। आधुनिक लाइब्रेरी सीमा को पैदा करने के लिए रैंडम सीमा का उपयोग करती हैं, लेकिन मैनुअल कार्यान्वयन में सावधानी की आवश्यकता होती है। बाइनरी फ़ाइलों के लिए, सामग्री जैसा है, सभी बाइट्स को संरक्षित किया जाता है, जो फ़ाइल की अखंडता बनाए रखने के लिए आवश्यक है।

##### फ़ाइल आकार और प्रदर्शन
दोनों विधियों को सर्वरों द्वारा लगाए गए फ़ाइल आकार सीमाओं को ध्यान में रखना चाहिए। Multipart/form-data अनुरोध कई फ़ाइलों के साथ बड़े हो सकते हैं, जिससे सर्वर सीमाओं को पार कर सकते हैं या मेमोरी समस्याएं पैदा कर सकते हैं। PUT, जबकि सरल, भी बड़ी फ़ाइलों के लिए स्ट्रीमिंग की आवश्यकता होती है ताकि पूरा सामग्री मेमोरी में लोड नहीं हो सके, जैसा कि [HTTPie documentation on file uploads](https://httpie.io/docs/cli/file-upload-forms) में चर्चा की गई है।

##### त्रुटि प्रबंधन और सुरक्षा
अनुरोध भेजने के बाद, क्लाइंट HTTP स्टेटस कोड की जांच करनी चाहिए। सफलता आमतौर पर 200 (OK) या 201 (Created) द्वारा संकेतित होती है, जबकि त्रुटियां जैसे कि 400 (Bad Request) या 403 (Forbidden) समस्याओं को संकेत करती हैं। सुरक्षा परम है, क्योंकि फ़ाइल अपलोड को खतरनाक कार्यक्रमों जैसे कि अपलोड करने के लिए उपयोग किया जा सकता है। सर्वर फ़ाइल प्रकारों को वैधता की जांच करनी चाहिए, मलवेयर के लिए स्कैन करना चाहिए और अपलोड डायरेक्टरी को सीमित करना चाहिए, जैसा कि [Stack Overflow discussions on HTTP file upload security](https://stackoverflow.com/questions/8659808/how-does-http-file-upload-work) में उल्लेख किया गया है।

#### विभिन्न भाषाओं में व्यावहारिक उदाहरण

विभिन्न प्रोग्रामिंग भाषाएं HTTP फ़ाइल अपलोड को सरल बनाने के लिए लाइब्रेरी प्रदान करती हैं। उदाहरण के लिए, Python की `requests` लाइब्रेरी multipart/form-data के साथ काम करती है:

```python
import requests
files = {'file': open('example.txt', 'rb')}
response = requests.post('https://example.com/upload', files=files)
```

PUT के लिए, curl का उपयोग किया जा सकता है, जैसा कि [Stack Overflow on testing PUT uploads](https://stackoverflow.com/questions/5143915/test-file-upload-using-http-put-method) में दिखाया गया है:

```bash
curl -X PUT "https://example.com/files/123" --upload-file example.txt
```

ये उदाहरणों में सादगी दिखाते हैं, लेकिन HTTP संरचना को समझना त्रुटि सुधार और कस्टम कार्यान्वयन के लिए महत्वपूर्ण है।

#### निष्कर्ष

सारांश में, HTTP फ़ाइल अपलोड POST के साथ multipart/form-data के लिए बहुमुखी वेब फॉर्म इंटरैक्शंस या PUT के लिए दक्ष API अपडेट के माध्यम से किया जा सकता है, प्रत्येक में अलग-अलग लाभ और आवश्यकताएं होती हैं। सर्वर सेटिंग, फ़ाइल आकार और सुरक्षा विचार महत्वपूर्ण हैं, जिससे मजबूत कार्यान्वयन सुनिश्चित होता है। और अधिक पढ़ने के लिए, विभिन्न भाषाओं में व्यावहारिक उदाहरणों के लिए [Medium's guide on POST file uploads](https://medium.com/@API4AI/post-a-file-via-http-request-the-ultimate-guide-b23fb70a3f73) का अन्वेषण करें।

### मुख्य संदर्भ
- [How do you upload your files to a web server Learn web development MDN](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Tools_and_setup/Upload_files_to_a_web_server)
- [How does HTTP file upload work Stack Overflow](https://stackoverflow.com/questions/8659808/how-does-http-file-upload-work)
- [POST a File via HTTP Request The Ultimate Guide by API4AI Medium](https://medium.com/@API4AI/post-a-file-via-http-request-the-ultimate-guide-b23fb70a3f73)
- [HTTP REST API File Uploads Phil Sturgeon](https://philsturgeon.com/http-rest-api-file-uploads/)
- [PHP PUT method support Manual](https://www.php.net/manual/en/features.file-upload.put-method.php)
- [curl Test file upload using HTTP PUT method Stack Overflow](https://stackoverflow.com/questions/5143915/test-file-upload-using-http-put-method)
- [File upload forms HTTPie 3.2.4 latest docs](https://httpie.io/docs/cli/file-upload-forms)