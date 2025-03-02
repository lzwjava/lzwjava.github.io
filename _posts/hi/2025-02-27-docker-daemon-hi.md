---
audio: false
generated: true
lang: hi
layout: post
title: Docker Daemon Connection Issues का समस्या
translated: true
---

### मुख्य बिंदु
- डॉकर डेमोन चल रहा नहीं लगता, त्रुटि संदेश के आधार पर।
- अनुसंधान सुझाव देता है कि डॉकर डेस्कटॉप एप्लिकेशन खुला है, क्योंकि यह macOS पर आम तौर पर उपयोग किया जाता है।
- सबूत इस ओर इशारा करता है कि सॉकेट पथ की जांच करें, जो एक अनूठे स्थान पर गलत हो सकता है जैसे /Users/lzwjava/.docker/run docker sock.

### डॉकर डेस्कटॉप चल रहा है, सुनिश्चित करें
पहले, सुनिश्चित करें कि डॉकर डेस्कटॉप एप्लिकेशन इंस्टॉल और चल रहा है। आप इसे अपने एप्लिकेशन फोल्डर में ढूंढ सकते हैं या मेनू बार में इसका आइकन ढूंढ सकते हैं। अगर यह चल नहीं रहा है, तो इसे खोलें और इसे शुरू होने के लिए इंतजार करें। अगर आप मानक सेटअप का उपयोग कर रहे हैं, तो यह समस्या हल कर देगा।

### सॉकेट पथ और DOCKER_HOST की जांच करें
त्रुटि में /Users/lzwjava/.docker/run docker sock पर एक सॉकेट पथ का उल्लेख है, जो एक अनूठा है क्योंकि इसमें एक स्पेस है। यह एक टाइपो हो सकता है, और इरादे में पथ /Users/lzwjava/.docker/run/dockersock हो सकता है। इस फाइल की मौजूदगी की जांच करने के लिए टर्मिनल में `ls /Users/lzwjava/.docker/run/dockersock` चलाएं। साथ ही, `echo $DOCKER_HOST` चलाएं ताकि देखें कि यह एक अनूठे पथ पर सेट है; अगर है, तो इसे डिफॉल्ट /var/run/dockersock पर वापस करने के लिए `unset DOCKER_HOST` से अनसेट करें।

### अनूठे इंस्टॉलेशन का सामना करें
अगर आप डॉकर डेस्कटॉप का उपयोग नहीं कर रहे हैं, तो आपके पास एक अनूठा सेटअप हो सकता है (जैसे, colima)। सुनिश्चित करें कि आपका डॉकर इंजन शुरू हो गया है, उदाहरण के लिए, colima के लिए `colima start`। अगर सॉकेट मौजूद है, तो `ls -l /var/run/dockersock` के साथ अनुमतियों की जांच करें और आवश्यकता के अनुसार सजाएं।

---

### सर्वेक्षण नोट: macOS पर डॉकर डेमोन कनेक्शन समस्याओं का विस्तृत विश्लेषण

इस खंड में "unix://Users/lzwjava/.docker/run docker sock पर डॉकर डेमोन से कनेक्शन नहीं हो सकता। क्या डॉकर डेमोन चल रहा है?" समस्या पर macOS पर डॉकर डेमोन कनेक्शन समस्याओं का एक व्यापक अन्वेषण किया गया है, जिसमें समस्या के संभावित कारण, ट्रबलशूटिंग कदम और मानक और अनूठे इंस्टॉलेशन के लिए विचार शामिल हैं। विश्लेषण इस समझ पर आधारित है कि macOS पर डॉकर आम तौर पर डॉकर डेस्कटॉप एप्लिकेशन पर निर्भर करता है, जो डॉकर इंजन को एक लिनक्स वर्चुअल मशीन (VM) में चलाता है, और अनूठे संरचनाओं जैसे अनूठे संरचनाओं का अन्वेषण करता है।

#### पृष्ठभूमि और संदर्भ
डॉकर एक प्लेटफॉर्म है जो ऑपरेटिंग सिस्टम स्तर पर वर्चुअलाइजेशन का उपयोग करके एप्लिकेशन को कंटेनरों में विकसित, शिप और चलाने के लिए है। macOS पर, लिनक्स कर्नल विशेषताओं जैसे cgroups और namespaces की कमी के कारण, डॉकर को एक VM में चलने के लिए आवश्यक है। आधिकारिक तरीका डॉकर डेस्कटॉप के माध्यम से है, जो डिफॉल्ट रूप से /var/run/dockersock पर एक यूनिक्स सॉकेट के माध्यम से डॉकर डेमोन को प्रदर्शित करता है। हालांकि, त्रुटि संदेश एक अनूठे पथ, /Users/lzwjava/.docker/run docker sock, से कनेक्शन करने का प्रयास दिखाता है, जो या तो एक गलत संरचना या एक अनूठा इंस्टॉलेशन का सुझाव देता है।

"डॉकर डेमोन से कनेक्शन नहीं हो सकता" त्रुटि आम तौर पर तब होती है जब डॉकर क्लाइंट डॉकर डेमोन के साथ संचार नहीं कर सकता, अक्सर डेमोन नहीं चलने, गलत सॉकेट पथ या अनुमतियों के कारण। वर्तमान समय 03:57 AM PST है, गुरुवार, 27 फरवरी, 2025, और मानक प्रथाओं को ध्यान में रखते हुए, हम दोनों मानक डॉकर डेस्कटॉप सेटअप और संभावित अनूठे संरचनाओं का अन्वेषण करेंगे।

#### मानक डॉकर डेस्कटॉप सेटअप
मैकओएस के लिए आधिकारिक डॉकर डेस्कटॉप का उपयोग करने वाले उपयोगकर्ताओं के लिए, डॉकर इंजन एक HyperKit VM में चलता है, और सॉकेट /var/run/dockersock पर प्रदर्शित होता है। समस्या को हल करने के लिए:

- **डॉकर डेस्कटॉप चल रहा है, सुनिश्चित करें:** /Applications/Docker.app से डॉकर डेस्कटॉप एप्लिकेशन खोलें या मेनू बार में इसका आइकन ढूंढें। अगर इंस्टॉल नहीं है, तो इसे [आधिकारिक डॉकर वेबसाइट](https://www.docker.com/products/container-platform) से डाउनलोड करें। चलने के बाद, यह VM और डॉकर इंजन को शुरू करेगा, जिससे सॉकेट उपलब्ध हो जाएगा।

- **DOCKER_HOST पर्यावरण चर का जांच करें:** टर्मिनल में `echo $DOCKER_HOST` चलाएं ताकि यह सेट है या नहीं। अगर यह "unix://Users/lzwjava/.docker/run docker sock" पर सेट है, तो यह त्रुटि का कारण है, क्योंकि यह डिफॉल्ट पथ को ओवरराइड करता है। इसे /var/run/dockersock पर वापस करने के लिए `unset DOCKER_HOST` से अनसेट करें।

- **सॉकेट फाइल की पुष्टि करें:** `ls /var/run/dockersock` चलाएं ताकि सॉकेट मौजूद है। अगर मौजूद है, तो अनुमतियों की जांच करें `ls -l /var/run/dockersock` ताकि सुनिश्चित करें कि उपयोगकर्ता को एक्सेस है। डॉकर डेस्कटॉप आम तौर पर अनुमतियों का प्रबंधन करता है, लेकिन आवश्यकता पड़ने पर `docker ps` को sudo के साथ चलाने से समस्याओं को पार कर सकते हैं।

#### अनूठे इंस्टॉलेशन और सॉकेट पथ विश्लेषण
त्रुटि संदेश का पथ, /Users/lzwjava/.docker/run docker sock, एक अनूठे संरचना का सुझाव देता है, क्योंकि यह मानक /var/run/dockersock नहीं है। "run docker sock" में स्पेस अनूठा है, जो एक टाइपो का सुझाव देता है; यह शायद /Users/lzwjava/.docker/run/dockersock होना चाहिए। यह पथ कुछ अनूठे सेटअप के साथ मेल खाता है, जैसे colima, जो सॉकेट को /Users/<username>/.colima/run/dockersock पर रखता है, हालांकि यहाँ यह .docker है, नहीं .colima।

- **सॉकेट फाइल की मौजूदगी की जांच करें:** `ls /Users/lzwjava/.docker/run/dockersock` चलाएं (अगर स्पेस एक टाइपो है)। अगर मौजूद है, तो समस्या डेमोन नहीं चलने या अनुमतियों हो सकती है। अगर मौजूद नहीं है, तो डेमोन को वहां सॉकेट बनाने के लिए कॉन्फ़िगर नहीं किया गया है।

- **अनूठे इंस्टॉलेशन के लिए डॉकर इंजन शुरू करें:** अगर डॉकर डेस्कटॉप का उपयोग नहीं किया जा रहा है, तो इंस्टॉलेशन विधि का पहचान करें। colima के लिए, `colima start` चलाएं ताकि VM और डॉकर इंजन को शुरू करें। अन्य अनूठे सेटअप के लिए, विशेष दस्तावेज़ देखें, क्योंकि डॉकर-इंजन को macOS पर एक VM के बिना सीधे इंस्टॉल नहीं किया जा सकता।

- **DOCKER_HOST सेट करें:** अगर एक अनूठे पथ का उपयोग किया जा रहा है, तो सुनिश्चित करें कि DOCKER_HOST सही तरह से सेट है, उदाहरण के लिए, `export DOCKER_HOST=unix://Users/lzwjava/.docker/run/dockersock`। .bashrc या .zshrc जैसे शेल कॉन्फ़िगरेशन फाइलों में स्थायी सेटिंग्स की जांच करें।

#### अनुमति और ट्रबलशूटिंग विचार
अनुमतियाँ कनेक्शन समस्याओं का कारण हो सकती हैं। अगर सॉकेट फाइल मौजूद है लेकिन एक्सेस मना कर दिया गया है, तो `ls -l` के साथ जांच करें और सुनिश्चित करें कि उपयोगकर्ता को पढ़ने/लिखने की अनुमति है। macOS पर डॉकर डेस्कटॉप के साथ अनुमतियाँ आम तौर पर प्रबंधित होती हैं, लेकिन अनूठे सेटअप के लिए, उपयोगकर्ता को एक डॉकर समूह में जोड़ना (यदि लागू) या sudo का उपयोग करना आवश्यक हो सकता है।

अगर समस्या जारी है, तो डॉकर डेस्कटॉप को ट्रबलशूट मेनू के माध्यम से रीसेट करने का विचार करें या त्रुटियों के लिए लॉग्स की जांच करें। अनूठे इंस्टॉलेशन के लिए, समुदाय फोरम या दस्तावेज़ देखें, क्योंकि सेटअप बदल सकता है।

#### तुलनात्मक विश्लेषण: मानक vs. अनूठे पथ
संभावित पथों और कार्यों को संगठित करने के लिए, निम्नलिखित तालिका का विचार करें:

| **इंस्टॉलेशन प्रकार** | **अपेक्षित सॉकेट पथ**          | **डेमोन को शुरू करने के लिए कार्रवाई**         | **DOCKER_HOST की जांच**                     |
|-----------------------|------------------------------------|------------------------------------|-------------------------------------------|
| डॉकर डेस्कटॉप        | /var/run/dockersock               | डॉकर डेस्कटॉप एप्लिकेशन खोलें    | सुनिश्चित करें कि अनसेट या unix://var/run/dockersock पर सेट है |
| अनूठे (जैसे, Colima) | /Users/<username>/.colima/run/dockersock | `colima start` चलाएं                 | आवश्यकता के अनुसार अनूठे पथ पर सेट करें, उदाहरण के लिए, unix://Users/lzwjava/.colima/run/dockersock |
| अनूठे (उपयोगकर्ता का पथ)  | /Users/lzwjava/.docker/run/dockersock | सेटअप पर निर्भर करता है, दस्तावेज़ देखें       | सॉकेट फाइल मौजूद है तो unix://Users/lzwjava/.docker/run/dockersock पर सेट करें |

इस तालिका में दिखाया गया है कि उपयोगकर्ता का पथ colima के डिफॉल्ट से मेल नहीं खाता, जो एक अनूठे सेटअप का सुझाव देता है। पथ में स्पेस एक संभावित टाइपो है, और `ls` कमांडों के साथ सत्यापन करना महत्वपूर्ण है।

#### अनपेक्षित विवरण: होम डायरेक्टरी में अनूठे सॉकेट पथ
एक अनपेक्षित विवरण यह है कि सॉकेट उपयोगकर्ता के होम डायरेक्टरी में हो सकता है, जैसा कि त्रुटि संदेश में दिखाया गया है। जबकि /var/run/dockersock डॉकर डेस्कटॉप के लिए मानक है, अनूठे टूल्स या संरचनाएँ इसे अन्य स्थान पर रख सकते हैं, जैसे /Users/<username>/.docker/run/dockersock, जिससे उपयोगकर्ताओं को DOCKER_HOST को अनुकूलित करने की आवश्यकता होती है। यह कम आम है और ट्रबलशूटिंग को जटिल बना सकता है।

#### निष्कर्ष
समस्या डॉकर डेमोन नहीं चलने या /Users/lzwjava/.docker/run docker sock पर गलत कॉन्फ़िगर DOCKER_HOST से उत्पन्न हो सकती है, जो /Users/lzwjava/.docker/run/dockersock के लिए एक संभावित टाइपो हो सकता है। शुरू में सुनिश्चित करें कि डॉकर डेस्कटॉप चल रहा है, DOCKER_HOST अनसेट करें और सॉकेट फाइल की पुष्टि करें। अनूठे सेटअप के लिए, इंस्टॉलेशन विधि का पहचान करें और इंजन को अनुकूलित करें। अगर समस्या हल नहीं होती, तो आगे की निदान के लिए समुदाय समर्थन खोजें।

### मुख्य उद्धरण
- [Mac Docker Desktop Install Guide](https://docs.docker.com/desktop/install/mac-install/)
- [Docker Desktop Usage and Start Daemon](https://docs.docker.com/desktop/usage/#start-the-docker-daemon)
- [Docker Desktop Connect to Engine API](https://docs.docker.com/desktop/usage/#connect-to-the-docker-engine-api)