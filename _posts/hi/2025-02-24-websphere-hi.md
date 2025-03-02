---
audio: false
generated: true
lang: hi
layout: post
title: WebSphere Liberty Server Commands का अनुवाद
translated: true
---

जब एक WebSphere Liberty सर्वर का प्रबंधन किया जाता है, कई कमांड्स अक्सर आवश्यक कार्यों जैसे कि सर्वर बनाना, शुरू करना, रोकना और निगरानी करने के लिए उपयोग किए जाते हैं। नीचे सबसे आमतौर पर उपयोग किए जाने वाले कमांड्स की सूची दी गई है, साथ ही प्रत्येक के बारे में एक संक्षिप्त विवरण:

- **`./server create <server_name>`**
  निर्दिष्ट नाम के साथ एक नया सर्वर इंस्टेंस बनाता है। यह कमांड सर्वर के लिए आवश्यक डायरेक्टरी संरचना और डिफ़ॉल्ट कॉन्फ़िगरेशन फ़ाइलें (जैसे `server.xml`) सेट अप करता है।

- **`./server start <server_name>`**
  सर्वर को पृष्ठभूमि में शुरू करता है। सर्वर एक पृष्ठभूमि प्रक्रिया के रूप में चलता है, और लॉग सर्वर के लॉग फ़ाइलों में लिखे जाते हैं।

- **`./server stop <server_name>`**
  चल रहे सर्वर इंस्टेंस को रोकता है। यह कमांड सर्वर को नम्रता से बंद करता है।

- **`./server status <server_name>`**
  जांच करता है कि निर्दिष्ट सर्वर चल रहा है या नहीं। यह वर्तमान स्थिति (जैसे शुरू या रोक) लौटाता है।

- **`./server run <server_name>`**
  सर्वर को फॉरग्राउंड में शुरू करता है। यह डिबगिंग या निगरानी के लिए उपयोगी है, क्योंकि सर्वर आउटपुट सीधे कंसोल में प्रदर्शित होता है।

- **`./server package <server_name>`**
  सर्वर, जिसमें इसके कॉन्फ़िगरेशन और एप्लिकेशन शामिल हैं, को एक ज़िप फ़ाइल में पैक करता है। यह सर्वर को दूसरे वातावरण में डिप्लॉय करने या बैकअप के लिए उपयोगी है।

- **`./server debug <server_name>`**
  सर्वर को डिबग मोड में शुरू करता है, जिससे आप सर्वर प्रक्रिया को डिबगर से जोड़ सकते हैं ताकि समस्या का निदान किया जा सके।

ये कमांड्स एक WebSphere Liberty सर्वर को प्रभावी ढंग से प्रबंधित करने के लिए आवश्यक मूल कार्यों को कवर करते हैं। अधिक उन्नत कार्यों के लिए, जैसे कि फीचर इंस्टॉल करने या सुरक्षा प्रबंधित करने, जैसे `featureUtility` या `securityUtility` जैसे अतिरिक्त यूटीलीटियां उपलब्ध हैं, लेकिन वे दैनिक कार्यों में कम अक्सर उपयोग किए जाते हैं।