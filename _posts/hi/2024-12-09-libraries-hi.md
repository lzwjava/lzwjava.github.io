---
audio: false
generated: false
image: false
lang: hi
layout: post
title: लाइब्रेरीज़ का उपयोग करते समय अपग्रेड पर विचार करें
translated: true
---

मैंने अपने स्टार्टअप प्रोजेक्ट, [Fun Live](https://github.com/lzwjava/live-server) में CodeIgniter का उपयोग किया था। हालांकि प्रोजेक्ट समाप्त हो गया, लेकिन कई सालों बाद, मैं इसे यादगार बनाने के लिए इसे फिर से जीवित करना चाहता था। हालांकि, 2016 में, मैंने CodeIgniter 3 का उपयोग किया था, जबकि अब नवीनतम संस्करण CodeIgniter 4 है।

अपग्रेड करना मुश्किल साबित हुआ है क्योंकि मेरा कोड CodeIgniter फ्रेमवर्क के साथ बहुत निकटता से जुड़ा हुआ है। [https://codeigniter4.github.io/CodeIgniter4/installation/upgrade_4xx.html](https://codeigniter4.github.io/CodeIgniter4/installation/upgrade_4xx.html) पर उपलब्ध अपग्रेड गाइड के अनुसार, कोडबेस को अपडेट करने के लिए काफी मेहनत की आवश्यकता है।

इस अनुभव ने मुझे एक महत्वपूर्ण सबक सिखाया: कोड लिखते समय, हमें भविष्य के अपडेट को कैसे संभालना है, इस पर सावधानीपूर्वक विचार करना चाहिए। यह सोचना महत्वपूर्ण है कि कोड के कौन से हिस्से हमारे नियंत्रण में हैं और कौन से हिस्से तीसरे पक्ष की निर्भरताओं द्वारा नियंत्रित हैं।