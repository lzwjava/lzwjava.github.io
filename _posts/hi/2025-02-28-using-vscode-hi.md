---
audio: false
generated: true
lang: hi
layout: post
title: VS Code का उपयोग करते हुए
translated: true
---

### मुख्य बिंदु
- VS Code एक लोकप्रिय, मुफ्त कोड एडिटर है जो Windows, macOS, और Linux के लिए उपलब्ध है, और कई प्रोग्रामिंग भाषाओं का समर्थन करता है।
- इसका अनुमान है कि इसका सबसे उपयोगी फीचर सिंटैक्स हाइलाइटिंग, डिबगिंग, और Git इंटीग्रेशन शामिल हैं, डेवलपर उपयोग के आधार पर।
- सबूत यह दर्शाते हैं कि 30 से अधिक बिल्ट-इन फीचर हैं जो उत्पादकता को बढ़ाते हैं, जैसे कि मल्टी-कर्सर एडिटिंग और रिमोट डेवलपमेंट।

---

### VS Code के साथ शुरू करना
Visual Studio Code (VS Code) एक हल्का, ओपन-सोर्स कोड एडिटर है जो माइक्रोसॉफ्ट द्वारा विकसित किया गया है, जो Windows, macOS, और Linux पर कोडिंग के लिए आदर्श है। शुरू करने के लिए, इसे ऑफिसियल साइट से [यहाँ](https://code.visualstudio.com/download) डाउनलोड करें। इंस्टॉल होने के बाद, VS Code को लॉन्च करें और कोडिंग शुरू करें।

#### बेसिक उपयोग
- **फाइल बनाएं या खोलें**: नए फाइल के लिए `File > New File` (या Windows/Linux पर `Ctrl + N`, macOS पर `Cmd + N`) का उपयोग करें, और मौजूदा फाइल के लिए `File > Open` (या `Ctrl + O`, `Cmd + O`) का उपयोग करें। `Ctrl + S` या `Cmd + S` से सेव करें।
- **कोड एडिटिंग**: सिंटैक्स हाइलाइटिंग, ऑटो-इंडेंटेशन, और ब्रैकेट मैचिंग जैसे फीचर का आनंद लें, जो पढ़ने के लिए बेहतर बनाते हैं। कोड स्निपेट्स के लिए तेज़ इंसर्ट और मल्टी-कर्सर एडिटिंग (`Alt + Click`) के लिए एक साथ एडिट करें।
- **नविगेशन**: `Ctrl + Click` से परिभाषाओं पर जंप करें, राइट-क्लिक से संदर्भ खोजें, और `Ctrl + P` के लिए तेज़ फाइल एक्सेस का उपयोग करें। शीर्ष पर ब्रेडक्रम्ब्स फाइल पथों को नवीगेट करने में मदद करते हैं।
- **डिबगिंग और वर्सन कंट्रोल**: गटर पर क्लिक करके ब्रेकपॉइंट सेट करें, `F5` से डिबग करें, और स्रोत कंट्रोल पैनल से Git ऑपरेशन जैसे कि कमिट और पुश प्रबंधित करें।
- **कस्टमाइजेशन**: `File > Preferences > Color Theme` से थीम बदलें और `File > Preferences > Keyboard Shortcuts` के तहत शॉर्टकट्स को ट्यून करें।

#### 30 सबसे उपयोगी फीचर
VS Code एक समृद्ध सेट ऑफ बिल्ट-इन फीचर प्रदान करता है, जो डेवलपर्स के लिए उत्पादकता को बढ़ाते हैं। यहाँ 30 सबसे उपयोगी हैं, स्पष्टता के लिए वर्गीकृत:

| **वर्ग**        | **फीचर**                          | **विवरण**                                                                 |
|---------------------|--------------------------------------|---------------------------------------------------------------------------------|
| **एडिटिंग**         | सिंटैक्स हाइलाइटिंग                  | भाषा के आधार पर कोड को रंग देता है, पढ़ने के लिए।                                  |
|                     | ऑटो-इंडेंटेशन                     | कोड को सही संरचना के लिए स्वचालित रूप से इंडेंट करता है।                                |
|                     | ब्रैकेट मैचिंग                     | त्रुटि पता लगाने में मदद करने के लिए मिलते हुए ब्रैकेट को हाइलाइट करता है।                            |
|                     | कोड स्निपेट्स                        | तेज़ रूप से अक्सर उपयोग किए जाने वाले कोड पैटर्न इंसर्ट करता है।                                  |
|                     | मल्टी-कर्सर एडिटिंग                 | `Alt + Click` के साथ एक साथ कई कोड भागों को एडिट करता है।                    |
|                     | कोड फोल्डिंग                         | बेहतर अवलोकन के लिए कोड क्षेत्रों को फोल्ड/अनफोल्ड करता है।                             |
|                     | कोड लेंस                            | अतिरिक्त जानकारी जैसे कि कमिट इतिहास या टेस्ट स्थिति दिखाता है।                       |
|                     | पीक डिफिनिशन                      | एक होवर विंडो में फंक्शन/वेरिएबल डिफिनिशन देखें बिना नवीगेशन।       |
| **नविगेशन**      | गो टू डिफिनिशन                     | `Ctrl + Click` के साथ फंक्शन/वेरिएबल डिफिनिशन पर जंप करता है।                     |
|                     | फाइंड ऑल रेफरेंस                  | कोडबेस में एक फंक्शन/वेरिएबल के सभी अवसरों को खोजता है।                 |
|                     | क्विक ओपन                           | `Ctrl + P` के साथ फाइलें तेज़ी से खोलता है।                                            |
|                     | ब्रेडक्रम्ब नवीगेशन                | अलग-अलग हिस्सों तक आसानी से नवीगेट करने के लिए फाइल पथ दिखाता है।                      |
| **डिबगिंग**       | बिल्ट-इन डिबगर                    | ब्रेकपॉइंट सेट करता है, कोड में स्टेप करता है, और वेरिएबल्स को इंस्पेक्ट करता है।                   |
|                     | ब्रेकपॉइंट                          | त्रुटि खोजने के लिए विशेष लाइनों पर कार्यक्रम को रोकता है।                               |
|                     | स्टेप थ्रू कोड                    | डिबगिंग के दौरान कोड को लाइन-बाई-लाइन (`F10`, `F11`) चलाता है।                     |
|                     | वॉच वेरिएबल्स                      | डिबगिंग सेशन के दौरान वेरिएबल्स के मानों की निगरानी करता है।                             |
| **वर्सन कंट्रोल** | Git इंटीग्रेशन                      | कमिट, पुल, पुश जैसे Git ऑपरेशन का समर्थन करता है।                 |
|                     | कमिट, पुल, पुश                   | VS Code से Git कार्रवाई सीधे करता है।                                     |
|                     | ब्लेम व्यू                           | प्रत्येक कोड लाइन को अंतिम बार कौन संपादित किया था, दिखाता है।                                      |
| **कस्टमाइजेशन**   | कलर थीम्स                         | विभिन्न कलर स्कीम के साथ एडिटर की दिखावट को कस्टमाइज करता है।                        |
|                     | किबोर्ड शॉर्टकट्स                   | दक्षता के लिए कस्टमाइज या डिफॉल्ट शॉर्टकट्स का उपयोग करता है।                            |
|                     | सेटिंग्स सिंक                        | कई मशीनों पर सेटिंग्स को सिंक करता है, एकसंगतता के लिए।                        |
|                     | प्रोफाइल्स                             | अलग-अलग सेटिंग्स के लिए सेटिंग्स को सेट और स्विच करता है।                 |
| **रिमोट डेवलपमेंट** | रिमोट एसएसएच                     | एसएसएच के माध्यम से रिमोट सर्वरों पर डेवलपमेंट करता है।                         |
|                     | कंटेनर्स                           | अलग-अलग कंटेनर वातावरण में डेवलपमेंट करता है।                                    |
|                     | कोडस्पेस                           | GitHub से क्लाउड-बेस्ड डेवलपमेंट वातावरण का उपयोग करता है।                          |
| **उत्पादकता**    | कमांड पॅलेट                      | `Ctrl + Shift + P` के माध्यम से सभी कमांड्स तक पहुंचता है।                                   |
|                     | टास्क रनर                          | बिल्डिंग या टेस्टिंग कोड जैसे टास्क्स को इंटर्नल रूप से चलाता है।                            |
|                     | इंटीग्रेटेड टर्मिनल                  | VS Code के भीतर सीधे कमांड लाइन तक पहुंचता है।                                  |
|                     | प्रॉब्लम्स पैनल                       | त्रुटियां, चेतावनियां, और मुद्दे को तेज़ी से सुलझाने के लिए दिखाता है।                     |

विस्तृत जांच के लिए, ऑफिसियल डॉक्यूमेंटेशन [यहाँ](https://code.visualstudio.com/docs) पर जाएं।

---

### VS Code और इसके फीचर्स का व्यापक गाइड
इस खंड में, माइक्रोसॉफ्ट द्वारा विकसित एक बहुमुखी कोड एडिटर, Visual Studio Code (VS Code) का उपयोग करने का गहन अध्ययन किया जाता है, और डेवलपर प्राथमिकताओं और ऑफिसियल डॉक्यूमेंटेशन के आधार पर 30 सबसे उपयोगी बिल्ट-इन फीचर्स का विवरण दिया जाता है, 27 फरवरी 2025 तक। VS Code, जो Windows, macOS, और Linux के लिए उपलब्ध है, एक विस्तृत श्रृंखला में प्रोग्रामिंग भाषाओं का समर्थन करता है और अपने विस्तार्यता और प्रदर्शन के लिए जाना जाता है, जिसमें 73.6% डेवलपर्स का उपयोग करता है, 2024 Stack Overflow डेवलपर सर्वेक्षण के अनुसार।

#### इंस्टॉलेशन और प्रारंभिक सेटअप
शुरू करने के लिए, VS Code को ऑफिसियल वेबसाइट से [यहाँ](https://code.visualstudio.com/download) से डाउनलोड करें। इंस्टॉलेशन सरल है, कई प्लेटफॉर्म का समर्थन करता है, जिससे सभी उपयोगकर्ताओं के लिए पहुंच आसान होती है। लॉन्च होने पर, उपयोगकर्ताओं को एक स्वागत पेज मिलता है जो कार्रवाई जैसे कि एक फोल्डर खोलना या एक नया फाइल बनाना प्रदान करता है। वर्कस्पेस ट्रस्ट के लिए, खासकर डाउनलोड किए गए कोड के साथ, इसे सुरक्षा के लिए जांचें, जैसा कि डॉक्यूमेंटेशन [यहाँ](https://code.visualstudio.com/docs/getstarted/getting-started) में विस्तार से बताया गया है।

#### चरण-चरण उपयोग गाइड
1. **फाइल बनाएं और खोलें**: नए फाइल के लिए `File > New File` या `Ctrl + N` (`Cmd + N` on macOS) का उपयोग करें, और मौजूदा फाइल के लिए `File > Open` या `Ctrl + O` (`Cmd + O`) का उपयोग करें। `Ctrl + S` या `Cmd + S` से सेव करें। यह किसी भी प्रोजेक्ट शुरू करने के लिए आवश्यक है, जैसा कि प्रारंभिक वीडियो [यहाँ](https://code.visualstudio.com/docs/introvideos/basics) में बताया गया है।

2. **बेसिक एडिटिंग फीचर्स**: VS Code में सिंटैक्स हाइलाइटिंग, ऑटो-इंडेंटेशन, और ब्रैकेट मैचिंग शामिल हैं, जो पढ़ने को बेहतर बनाते हैं और त्रुटियों को कम करते हैं। उदाहरण के लिए, "console.log" टाइप करके टैब दबाएं, एक जावास्क्रिप्ट स्निपेट इंसर्ट करता है, जैसा कि एडिटिंग ट्यूटोरियल [यहाँ](https://code.visualstudio.com/docs/introvideos/codeediting) में उल्लेख किया गया है।

3. **एडवांस्ड एडिटिंग**: मल्टी-कर्सर एडिटिंग, जो `Alt + Click` से सक्रिय होता है, कई लाइनों पर एक साथ एडिट करने की अनुमति देता है, जो रिपीटिटिव टास्क्स के लिए उत्पादकता बढ़ाता है। कोड स्निपेट्स और फोल्डिंग फ्लो को और अधिक सुलभ बनाते हैं, जैसा कि टिप्स और ट्रिक्स [यहाँ](https://code.visualstudio.com/docs/getstarted/tips-and-tricks) में चर्चा की गई है।

4. **नविगेशन और सर्च**: `Ctrl + Click` से गो टू डिफिनिशन, राइट-क्लिक से फाइंड ऑल रेफरेंस, और `Ctrl + P` के लिए क्विक ओपन का उपयोग करें। शीर्ष पर ब्रेडक्रम्ब नवीगेशन जटिल फाइल संरचनाओं में नवीगेट करने में मदद करता है, जैसा कि यूजर इंटरफेस डॉक्यूमेंटेशन [यहाँ](https://code.visualstudio.com/docs/getstarted/userinterface) में विस्तार से बताया गया है।

5. **डिबगिंग क्षमता**: गटर पर क्लिक करके ब्रेकपॉइंट सेट करें, `F5` से डिबगिंग शुरू करें, और `F10` (स्टेप ओवर), `F11` (स्टेप इन), और `Shift + F11` (स्टेप आउट) के साथ विस्तृत इंस्पेक्शन करें। वेरिएबल्स को वॉच करें ताकि मानों की निगरानी की जा सके, जैसा कि विस्तार से [यहाँ](https://code.visualstudio.com/docs/editor/debugging) में चर्चा की गई है।

6. **Git के साथ वर्सन कंट्रोल**: स्रोत कंट्रोल व्यू के माध्यम से एक रिपोजिटरी को इंस्टॉल करें, `Ctrl + Enter` (macOS: `Cmd + Enter`) से कमिट करें, और पुल/पुश ऑपरेशन प्रबंधित करें। ब्लेम व्यू कोड संपादन इतिहास दिखाता है, जो सहयोग को बढ़ाता है, जैसा कि [यहाँ](https://code.visualstudio.com/docs/sourcecontrol/overview) में विस्तार से बताया गया है।

7. **कस्टमाइजेशन ऑप्शंस**: `File > Preferences > Color Theme` से कलर थीम बदलें, `File > Preferences > Keyboard Shortcuts` के तहत शॉर्टकट्स को कस्टमाइज करें, और सेटिंग्स सिंक के साथ सेटिंग्स को कई डिवाइसों पर सिंक करें। प्रोफाइल अलग-अलग प्रोजेक्ट के लिए अलग-अलग सेटिंग्स को सेट और स्विच करने की अनुमति देते हैं, जैसा कि [यहाँ](https://code.visualstudio.com/docs/getstarted/settings) में विस्तार से बताया गया है।

8. **रिमोट और क्लाउड डेवलपमेंट**: रिमोट सर्वरों पर एसएसएच के माध्यम से डेवलपमेंट, अलग-अलग कंटेनर वातावरण में डेवलपमेंट, और GitHub से क्लाउड-बेस्ड सेटअप का उपयोग करें, जैसा कि [यहाँ](https://code.visualstudio.com/docs/remote/remote-overview) में विस्तार से बताया गया है।

#### विस्तृत फीचर विश्लेषण
निम्न तालिका 30 सबसे उपयोगी बिल्ट-इन फीचर्स को सूचीबद्ध करती है, स्पष्टता के लिए वर्गीकृत, ऑफिसियल डॉक्यूमेंटेशन और डेवलपर उपयोग पैटर्न के आधार पर:

| **वर्ग**        | **फीचर**                          | **विवरण**                                                                 |
|---------------------|--------------------------------------|---------------------------------------------------------------------------------|
| **एडिटिंग**         | सिंटैक्स हाइलाइटिंग                  | भाषा के आधार पर कोड को रंग देता है, पढ़ने के लिए, हजारों भाषाओं का समर्थन करता है। |
|                     | ऑटो-इंडेंटेशन                     | कोड को सही संरचना के लिए स्वचालित रूप से इंडेंट करता है, एकसंगतता को बढ़ाता है।  |
|                     | ब्रैकेट मैचिंग                     | त्रुटि पता लगाने और पढ़ने में मदद करने के लिए मिलते हुए ब्रैकेट को हाइलाइट करता है।             |
|                     | कोड स्निपेट्स                        | तेज़ रूप से अक्सर उपयोग किए जाने वाले कोड पैटर्न इंसर्ट करता है, उदाहरण के लिए, "console.log" के लिए जावास्क्रिप्ट। |
|                     | मल्टी-कर्सर एडिटिंग                 | `Alt + Click` के साथ एक साथ कई कोड भागों को एडिट करता है, उत्पादकता बढ़ाता है। |
|                     | कोड फोल्डिंग                         | बेहतर अवलोकन के लिए कोड क्षेत्रों को फोल्ड/अनफोल्ड करता है, ध्यान को बढ़ाता है।             |
|                     | कोड लेंस                            | अतिरिक्त जानकारी जैसे कि कमिट इतिहास या टेस्ट स्थिति दिखाता है, रखरखाव में मदद करता है।    |
|                     | पीक डिफिनिशन                      | एक होवर विंडो में फंक्शन/वेरिएबल डिफिनिशन देखें बिना नवीगेशन, समय बचाता है। |
| **नविगेशन**      | गो टू डिफिनिशन                     | `Ctrl + Click` के साथ फंक्शन/वेरिएबल डिफिनिशन पर जंप करता है, नवीगेशन को बढ़ाता है। |
|                     | फाइंड ऑल रेफरेंस                  | एक फंक्शन/वेरिएबल के सभी अवसरों को खोजता है, रिफैक्टरिंग में उपयोगी।          |
|                     | क्विक ओपन                           | `Ctrl + P` के साथ फाइलें तेज़ी से खोलता है, फाइल एक्सेस को तेज़ करता है।                    |
|                     | ब्रेडक्रम्ब नवीगेशन                | अलग-अलग हिस्सों तक आसानी से नवीगेट करने के लिए फाइल पथ दिखाता है, ओरिएंटेशन को बढ़ाता है। |
| **डिबगिंग**       | बिल्ट-इन डिबगर                    | ब्रेकपॉइंट सेट करता है, कोड में स्टेप करता है, और वेरिएबल्स को इंस्पेक्ट करता है, टेस्टिंग के लिए आवश्यक। |
|                     | ब्रेकपॉइंट                          | त्रुटि खोजने के लिए विशेष लाइनों पर कार्यक्रम को रोकता है, त्रुटि खोजने में महत्वपूर्ण। |
|                     | स्टेप थ्रू कोड                    | कोड को लाइन-बाई-लाइन (`F10`, `F11`) चलाता है, गहन इंस्पेक्शन की अनुमति देता है।             |
|                     | वॉच वेरिएबल्स                      | डिबगिंग सेशन के दौरान वेरिएबल्स के मानों की निगरानी करता है, स्टेट ट्रैकिंग में मदद करता है।             |
| **वर्सन कंट्रोल** | Git इंटीग्रेशन                      | कमिट, पुल, पुश जैसे Git ऑपरेशन का समर्थन करता है, सहयोग को बढ़ाता है।        |
|                     | कमिट, पुल, पुश                   | VS Code से Git कार्रवाई सीधे करता है, वर्सन कंट्रोल को सुलझाता है।        |
|                     | ब्लेम व्यू                           | प्रत्येक कोड लाइन को अंतिम बार कौन संपादित किया था, कोड रिव्यू और जिम्मेदारी के लिए उपयोगी।    |
| **कस्टमाइजेशन**   | कलर थीम्स                         | एडिटर की दिखावट को कस्टमाइज करता है, कई विकल्पों के साथ दृश्य आराम को बढ़ाता है।       |
|                     | किबोर्ड शॉर्टकट्स                   | दक्षता के लिए कस्टमाइज या डिफॉल्ट शॉर्टकट्स का उपयोग करता है, पूरी तरह से कनफिगरेबल।  |
|                     | सेटिंग्स सिंक                        | कई मशीनों पर सेटिंग्स को सिंक करता है, एकसंगतता के लिए, विस्तार से [यहाँ](https://code.visualstudio.com/docs/getstarted/settings#_settings-sync) में बताया गया है। |
|                     | प्रोफाइल्स                             | अलग-अलग प्रोजेक्ट के लिए सेटिंग्स को सेट और स्विच करता है, लचीलापन को बढ़ाता है। |
| **रिमोट डेवलपमेंट** | रिमोट एसएसएच                     | एसएसएच के माध्यम से रिमोट सर्वरों पर डेवलपमेंट करता है, पहुंच को बढ़ाता है, विस्तार से [यहाँ](https://code.visualstudio.com/docs/remote/ssh) में बताया गया है। |
|                     | कंटेनर्स                           | अलग-अलग कंटेनर वातावरण में डेवलपमेंट करता है, एकसंगतता को सुनिश्चित करता है, नोट [यहाँ](https://code.visualstudio.com/docs/remote/containers) में किया गया है। |
|                     | कोडस्पेस                           | GitHub से क्लाउड-बेस्ड डेवलपमेंट वातावरण का उपयोग करता है, सहयोग को बढ़ाता है, विस्तार से [यहाँ](https://code.visualstudio.com/docs/remote/codespaces) में बताया गया है। |
| **उत्पादकता**    | कमांड पॅलेट                      | `Ctrl + Shift + P` के माध्यम से सभी कमांड्स तक पहुंचता है, फंक्शनलिटी को केंद्रित करता है।        |
|                     | टास्क रनर                          | बिल्डिंग या टेस्टिंग कोड जैसे टास्क्स को इंटर्नल रूप से चलाता है, फ्लो को बढ़ाता है, विस्तार से [यहाँ](https://code.visualstudio.com/docs/editor/tasks) में बताया गया है। |
|                     | इंटीग्रेटेड टर्मिनल                  | VS Code के भीतर सीधे कमांड लाइन तक पहुंचता है, इंटीग्रेशन को बढ़ाता है, नोट [यहाँ](https://code.visualstudio.com/docs/integrated-terminal) में किया गया है। |
|                     | प्रॉब्लम्स पैनल                       | त्रुटियां, चेतावनियां, और मुद्दे को तेज़ी से सुलझाने के लिए दिखाता है, डिबगिंग के लिए आवश्यक। |

ये फीचर्स विस्तृत अनुसंधान से संकलित किए गए हैं, जिसमें ऑफिसियल डॉक्यूमेंटेशन और डेवलपर-फोकस्ड लेख शामिल हैं, जिससे वे 2025 के उपयोग के साथ मेल खाते हैं। उदाहरण के लिए, Git और रिमोट डेवलपमेंट फीचर्स का इंटीग्रेशन VS Code के विकास को आधुनिक डेवलपमेंट आवश्यकताओं को पूरा करने के लिए विकसित होने का दर्शाता है, जैसा कि अपडेट [यहाँ](https://code.visualstudio.com/updates/v1_97) में देखा गया है।

#### अतिरिक्त विचार
VS Code के विस्तार्यता, जिसमें 30,000 से अधिक विस्तार शामिल हैं, इन बिल्ट-इन फीचर्स को पूरा करता है, लेकिन यहाँ पर ध्यान केंद्रित है। उदाहरण के लिए, जबकि GitHub Copilot लोकप्रिय है, यह एक विस्तार है, न कि बिल्ट-इन, इसलिए इसे छोड़ दिया गया है। तेज़ स्टार्टअप समय और दक्ष मेमोरी उपयोग, जैसा कि प्रदर्शन चर्चा [यहाँ](https://code.visualstudio.com/docs/editor/whyvscode) में देखा गया है, इसे दैनिक उपयोग के लिए उपयुक्त बनाता है, एक अप्रत्याशित विवरण है जो भारी आईडीई का अनुमान लगाने वाले उपयोगकर्ताओं के लिए है।

अधिक सीखने के लिए, प्रारंभिक वीडियो [यहाँ](https://code.visualstudio.com/docs/introvideos/basics) और टिप्स और ट्रिक्स [यहाँ](https://code.visualstudio.com/docs/getstarted/tips-and-tricks) पर जाएं, जिससे VS Code के क्षमताओं का व्यापक समझ हो सके।

---

### मुख्य सन्दर्भ
- [ऑफिसियल VS Code डॉक्यूमेंटेशन](https://code.visualstudio.com/docs/)
- [VS Code फीचर्स टिप्स और ट्रिक्स](https://code.visualstudio.com/docs/getstarted/tips-and-tricks)
- [VS Code डिबगिंग गाइड](https://code.visualstudio.com/docs/editor/debugging)
- [VS Code Git इंटीग्रेशन ओवरव्यू](https://code.visualstudio.com/docs/sourcecontrol/overview)
- [VS Code सेटिंग्स सिंक डॉक्यूमेंटेशन](https://code.visualstudio.com/docs/getstarted/settings#_settings-sync)
- [VS Code रिमोट एसएसएच डेवलपमेंट](https://code.visualstudio.com/docs/remote/ssh)
- [VS Code कंटेनर्स डेवलपमेंट](https://code.visualstudio.com/docs/remote/containers)
- [VS Code कोडस्पेस डेवलपमेंट](https://code.visualstudio.com/docs/remote/codespaces)
- [VS Code टास्क रनर डॉक्यूमेंटेशन](https://code.visualstudio.com/docs/editor/tasks)
- [VS Code इंटीग्रेटेड टर्मिनल गाइड](https://code.visualstudio.com/docs/integrated-terminal)
- [हमने VS Code एडिटर क्यों बनाया](https://code.visualstudio.com/docs/editor/whyvscode)
- [VS Code प्रारंभिक वीडियो](https://code.visualstudio.com/docs/introvideos/basics)
- [VS Code जनवरी 2025 अपडेट](https://code.visualstudio.com/updates/v1_97)