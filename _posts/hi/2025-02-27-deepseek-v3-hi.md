---
audio: false
generated: true
lang: hi
layout: post
title: गहन खोज V3
translated: true
---

### अवलोकन और प्रमुख बिंदु
1. मॉडल नाम: DeepSeek-V3, एक Mixture-of-Experts (MoE) भाषा मॉडल है, जिसमें 671 अरब पैरामीटर हैं, जिनमें से प्रति टोकन 37 अरब सक्रिय हैं।
2. ट्रेनिंग डेटासेट: 14.8 ट्रिलियन विविध, उच्च गुणवत्ता वाले टोकन पर प्री-ट्रेन किया गया है।
3. कोर नवाचार: Multi-Head Latent Attention (MLA) और DeepSeekMoE आर्किटेक्चर के साथ ऑक्सिलरी-लॉस-फ्री लोड बैलेंसिंग के साथ शामिल हैं।
4. ट्रेनिंग एफिशेंसी: केवल 2.788 मिलियन H800 GPU घंटों के साथ पूर्ण ट्रेनिंग प्राप्त होती है।
5. कोस्ट एफिशेंसी: ट्रेनिंग लागत 5.576M USD अनुमानित है, 2 USD प्रति GPU घंटे की अनुमानित दर पर।

---

### आर्किटेक्चरल नवाचार
6. ट्रांसफॉर्मर-बेस्ड फ्रेमवर्क: स्केलेबिलिटी और फ्लेक्सिबिलिटी के लिए ट्रांसफॉर्मर आर्किटेक्चर को बनाए रखता है।
7. Multi-Head Latent Attention (MLA): की-वैल्यू कैश को संपीड़ित करने के बिना पेरफॉर्मेंस हानि के बिना इन्फरेंस मेमोरी को कम करता है।
8. DeepSeekMoE: कोस्ट-एफेक्टिव ट्रेनिंग और उच्च कंप्यूटेशनल एफिशेंसी के लिए शेयर और रूटेड एक्सपर्ट्स का उपयोग करता है।
9. ऑक्सिलरी-लॉस-फ्री लोड बैलेंसिंग: पेरफॉर्मेंस को कम करने के बिना बेलेंस्ड एक्सपर्ट लोड्स को बनाए रखने के लिए बायस टर्म्स को पेश करता है।
10. Multi-Token Prediction (MTP): प्रत्येक पोजिशन के लिए कई टोकन को अनुक्रमिक रूप से भविष्यवाणी करता है, डेटा एफिशेंसी और प्रतिनिधित्व प्री-प्लानिंग को बेहतर बनाता है।

---

### ट्रेनिंग फ्रेमवर्क
11. FP8 मिक्स्ड प्रिसिजन ट्रेनिंग: फाइन-ग्रेनेड क्वांटाइजेशन और लो-प्रिसिजन स्टोरेज का उपयोग करके मेमोरी और कंप्यूटेशन को ऑप्टिमाइज करता है।
12. ड्यूलपाइप एल्गोरिथम: कंप्यूटेशन और कम्युनिकेशन फेजों को ओवरलैप करता है, पाइपलाइन बबल्स को कम करता है और पैरलेलिज्म को बेहतर बनाता है।
13. इफिशेंट क्रॉस-नोड कम्युनिकेशन: ऑल-टू-ऑल ऑपरेशंस के लिए ऑप्टिमाइज्ड कर्नल का उपयोग करता है, NVLink और InfiniBand बैंडविड्थ का उपयोग करता है।
14. लो-प्रिसिजन ऑप्टिमाइजर स्टेट्स: BF16 में ऑप्टिमाइजर स्टेट्स को स्टोर करता है, मेमोरी कंसम्प्शन को कम करता है बिना पेरफॉर्मेंस हानि के।
15. मेमोरी ऑप्टिमाइजेशन टेक्निक्स: बैक-प्रोपेगेशन के दौरान कुछ ऑपरेशंस (जैसे RMSNorm) को पुनः कंप्यूट करता है मेमोरी को बचाने के लिए।

---

### प्री-ट्रेनिंग विवरण
16. स्टेबल ट्रेनिंग प्रोसेस: प्री-ट्रेनिंग के दौरान कोई अनिर्वाच्य लॉस स्पाइक्स या रोलबैक नहीं हुई।
17. कॉन्टेक्स्ट लेंग्थ एक्सटेंशन: 32K और फिर 128K तक दो चरणों में कॉन्टेक्स्ट लेंग्थ को बढ़ाया गया।
18. ट्रेनिंग लागत: प्री-ट्रेनिंग में 2.664M GPU घंटे, कॉन्टेक्स्ट एक्सटेंशन में 119K GPU घंटे और पोस्ट-ट्रेनिंग में 5K GPU घंटे की आवश्यकता थी।
19. टोकन एफिशेंसी: ट्रेनिंग एफिशेंसी को ट्रिलियन टोकन प्रति GPU घंटे को कम करने से सुनिश्चित किया गया।
20. उच्च गुणवत्ता का डेटा: विविधता और प्रासंगिकता के लिए प्री-ट्रेनिंग डेटासेट तैयार किया गया।

---

### पोस्ट-ट्रेनिंग सुधार
21. सुपरवाइज्ड फाइन-ट्यूनिंग (SFT): मॉडल आउटपुट्स को मानव पसंद के साथ संरेखित करता है।
22. रिनफोर्समेंट लर्निंग (RL): ग्रुप रिलेटिव पॉलिसी ऑप्टिमाइजेशन के लिए फाइन-ट्यूनिंग का उपयोग करता है।
23. नॉलेज डिस्टिलेशन: डिपसीक-आर1 मॉडल्स से रीज़निंग क्षमताओं को एकीकृत करता है।
24. आउटपुट स्टाइल कंट्रोल: सटीकता को लंबाई और स्टाइल के साथ संतुलित करता है।
25. पेरफॉर्मेंस रिफाइनमेंट: पोस्ट-ट्रेनिंग बेंचमार्क परिणामों को और बेहतर बनाता है।

---

### बेंचमार्क पेरफॉर्मेंस
26. MMLU (शैक्षिक बेंचमार्क): 88.5 प्राप्त करता है, अन्य ओपन-सोर्स मॉडल्स को पार करता है।
27. GPQA (सामान्य ज्ञान): 59.1 स्कोर करता है, GPT-4o और क्लॉड-3.5-सोनेट के साथ तुलनात्मक है।
28. मैथ बेंचमार्क: गणितीय रीज़निंग टास्क्स में स्टेट-ऑफ़-द-आर्ट पेरफॉर्मेंस।
29. कोड प्रतियोगिताएं: लाइवकोडबेंच जैसे कोडिंग बेंचमार्क में उत्कृष्ट है।
30. सत्यापन ज्ञान: अंग्रेजी और चीनी सत्यापन बेंचमार्क में श्रेष्ठ परिणाम दिखाता है।

---

### इन्फरेंस और डिप्लॉयमेंट
31. प्रिफिलिंग स्टेज: टेंसर पैरलेलिज्म (TP4), सीक्वेंस पैरलेलिज्म (SP), और एक्सपर्ट पैरलेलिज्म (EP32) को संयोजित करता है।
32. डिकोडिंग स्टेज: EP320 के साथ IBGDA के लिए लो-लैटेंसी कम्युनिकेशन का उपयोग करता है।
33. डायनामिक रेडंडेंसी: एक्सपर्ट लोड्स को डायनामिक रूप से संशोधित करता है संसाधन उपयोग को ऑप्टिमाइज करने के लिए।
34. स्टेजों का विभाजन: प्रिफिलिंग और डिकोडिंग स्टेजों को अलग कर दिया गया है थ्रूपुट को बढ़ाने के लिए।
35. हार्डवेयर उपयोग: H800 GPUs के साथ NVLink और InfiniBand इंटरकनेक्ट्स के लिए ऑप्टिमाइज किया गया है।

---

### लोड बैलेंसिंग और डिकोडिंग में नवाचार
36. बायस-बेस्ड रूटिंग: बायस टर्म्स को पेश करता है ताकि एक्सपर्ट लोड्स को डायनामिक रूप से संतुलित किया जा सके।
37. स्पेक्युलेटिव डिकोडिंग: MTP मॉड्यूल्स का उपयोग करके जनरेशन लैटेंसी को बढ़ाता है।
38. रेडंडेंट एक्सपर्ट्स: उच्च लोड एक्सपर्ट्स को डुप्लिकेट करता है GPU वर्कलोड को संतुलित करने के लिए।
39. नोड-लिमिटेड रूटिंग: टोकन रूटिंग को 4 नोड्स तक सीमित करता है कम्युनिकेशन ओवरहेड को कम करने के लिए।
40. टोकन ड्रॉपिंग नहीं: ट्रेनिंग और इन्फरेंस के दौरान सभी टोकन को बनाए रखता है।

---

### तकनीकी विवरण
41. क्लस्टर कॉन्फिगरेशन: 2048 NVIDIA H800 GPUs के साथ क्लस्टर पर ट्रेन किया गया।
42. पाइपलाइन पैरलेलिज्म: 16-वे पैरलेलिज्म योजना का उपयोग करता है स्केलेबिलिटी के लिए।
43. मेमोरी फुटप्रिंट: मेमोरी उपयोग को ऑप्टिमाइज करके महंगे टेंसर पैरलेलिज्म से बचता है।
44. कस्टम कर्नल: क्रॉस-नोड ऑपरेशंस को प्रभावी रूप से हैंडल करने के लिए विशेषीकृत कम्युनिकेशन कर्नल विकसित करता है।
45. मिक्स्ड प्रिसिजन ऑप्टिमाइजेशन: FP8 और BF16 फॉर्मेट्स को संयोजित करता है ऑप्टिमल ट्रेनिंग डायनामिक्स के लिए।

---

### मूल्यांकन और परिणाम
46. व्यापक बेंचमार्क: शिक्षा, कोडिंग और रीज़निंग सहित विविध डोमेन में मूल्यांकित किया गया।
47. ओपन-सोर्स नेतृत्व: अपने श्रेणी में सबसे मजबूत ओपन-सोर्स बेस मॉडल के रूप में उभरता है।
48. बंद-सोर्स मॉडल्स के साथ तुलना: GPT-4o और क्लॉड-3.5-सोनेट के साथ तुलनात्मक पेरफॉर्मेंस।
49. चीनी ज्ञान में ताकत: चीनी सत्यापन बेंचमार्क में नेतृत्व करने वाले मॉडल्स को पार करता है।
50. लंबी कॉन्टेक्स्ट हैंडलिंग: लंबी कॉन्टेक्स्ट प्रोसेसिंग की आवश्यकता वाले टास्क्स में उत्कृष्ट है।

---

### भविष्य के दिशा
51. डायनामिक रेडंडेंसी का अन्वेषण: और अधिक अनुकूल रेडंडेंसी रणनीतियों का अन्वेषण।
52. स्पेक्युलेटिव डिकोडिंग का विस्तार: इन्फरेंस त्वरित करने के लिए MTP के और उपयोगों का अन्वेषण।
53. हार्डवेयर को-डिजाइन: अगले पीढ़ी के GPUs के लिए अनुकूलित किया गया है बेहतर पेरफॉर्मेंस के लिए।
54. व्यापक बेंचमार्क कवरेज: और विविध टास्क्स पर मूल्यांकन का विस्तार।
55. सततता: अल्गोरिथमिक और हार्डवेयर ऑप्टिमाइजेशन के माध्यम से ट्रेनिंग लागत को और कम करना।

---

यह दस्तावेज DeepSeek-V3 का एक व्यापक सारांश प्रदान करता है, जिसमें इसके आर्किटेक्चर, ट्रेनिंग विधियों, बेंचमार्क पेरफॉर्मेंस और भविष्य के संभावनाओं को शामिल किया गया है। मुझे बताएं अगर आपको किसी खंड पर और अधिक विवरण चाहिए या और बिंदुओं की आवश्यकता है!