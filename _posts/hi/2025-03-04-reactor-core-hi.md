---
audio: false
generated: true
lang: hi
layout: post
title: प्रतिक्रिया कार्यक्रमण जावा में
translated: true
---

**reactor-core** का उपयोग करने के लिए, एक Java लाइब्रेरी जो Reactive Streams स्पेसिफिकेशन पर आधारित नॉन-ब्लॉकिंग, एसिंक्रोनस एप्लिकेशन बनाने के लिए है, इन चरणों का पालन करें:

---

### 1. reactor-core को एक डिपेंडेंसी के रूप में जोड़ें
पहले, अपने प्रोजेक्ट में **reactor-core** को शामिल करें। अपने बिल्ड टूल के आधार पर:

- **Maven**: अपने `pom.xml` में यह जोड़ें:
  ```xml
  <dependency>
    <groupId>io.projectreactor</groupId>
    <artifactId>reactor-core</artifactId>
    <version>3.7.3</version>
  </dependency>
  ```

- **Gradle**: अपने `build.gradle` में यह जोड़ें:
  ```groovy
  implementation 'io.projectreactor:reactor-core:3.7.3'
  ```

इससे लाइब्रेरी आपके प्रोजेक्ट में उपलब्ध हो जाती है। आवश्यकता पड़ने पर [Maven Central](https://central.sonatype.com/artifact/io.projectreactor/reactor-core) पर नवीनतम संस्करण की जांच करें।

---

### 2. कोर घटक समझें
Reactor-core दो मुख्य क्लास प्रदान करता है रिएक्टिव प्रोग्रामिंग के लिए:
- **`Flux`**: एक एसिंक्रोनस स्ट्रीम का प्रतिनिधित्व करता है जो **0 से N आइटम** को एमिट कर सकता है।
- **`Mono`**: एक एसिंक्रोनस स्ट्रीम का प्रतिनिधित्व करता है जो **0 या 1 आइटम** को एमिट करता है।

ये आपकी रिएक्टिव डेटा को संभालने के लिए उपयोग करने वाले ब्लॉक हैं।

---

### 3. एक Flux या Mono बनाएं
आप `Flux` या `Mono` के इंस्टेंस बनाकर अपने डेटा स्ट्रीम का प्रतिनिधित्व कर सकते हैं।

- **Flux के साथ उदाहरण** (अनेक आइटम):
  ```java
  Flux<Integer> numbers = Flux.just(1, 2, 3, 4, 5);
  ```

- **Mono के साथ उदाहरण** (एकल आइटम):
  ```java
  Mono<String> greeting = Mono.just("Hello, World!");
  ```

`just` विधि एक सरल तरीका है स्टेटिक मानों से एक स्ट्रीम बनाने के लिए, लेकिन Reactor कई अन्य निर्माण विधियाँ प्रदान करता है (उदाहरण के लिए, एर्रे, रेंज, या कस्टम स्रोतों से)।

---

### 4. डेटा को प्रोसेस करने के लिए सब्सक्राइब करें
उत्पन्न आइटम को उपभोग करने के लिए, आपको `Flux` या `Mono` को **सब्सक्राइब** करना होगा। सब्सक्राइब करने से स्ट्रीम डेटा एमिट करने शुरू हो जाता है।

- **Flux को सब्सक्राइब करें**:
  ```java
  numbers.subscribe(System.out::println);  // प्रिंट करता है: 1, 2, 3, 4, 5
  ```

- **Mono को सब्सक्राइब करें**:
  ```java
  greeting.subscribe(System.out::println); // प्रिंट करता है: Hello, World!
  ```

`subscribe` विधि अतिरिक्त तर्कों को भी ले सकती है, जैसे कि त्रुटि हैंडलर या समापन कॉलबैक, अधिक नियंत्रण के लिए।

---

### 5. ऑपरेटरों के साथ डेटा को परिवर्तित करें
Reactor एक समृद्ध सेट ऑपरेटरों प्रदान करता है स्ट्रीम को संशोधित करने के लिए, जैसे कि `map`, `filter`, और अधिक।

- **Flux और map के साथ उदाहरण**:
  ```java
  numbers.map(n -> n * 2).subscribe(System.out::println);  // प्रिंट करता है: 2, 4, 6, 8, 10
  ```

- **Mono और map के साथ उदाहरण**:
  ```java
  greeting.map(s -> s.toUpperCase()).subscribe(System.out::println); // प्रिंट करता है: HELLO, WORLD!
  ```

ये ऑपरेटर्स आपको डेटा को परिवर्तित, फिल्टर, या एक घोषणात्मक तरीके से संयोजित करने की अनुमति देते हैं।

---

### 6. त्रुटियों और बैकप्रेशर को संभालें
Reactor-core त्रुटि हैंडलिंग और बैकप्रेशर प्रबंधन का समर्थन करता है:
- **त्रुटि हैंडलिंग**: `subscribe` के साथ एक त्रुटि उपभोक्ता का उपयोग करें:
  ```java
  Flux.error(new RuntimeException("Oops!"))
      .subscribe(System.out::println, error -> System.err.println(error.getMessage()));
  // प्रिंट करता है: Oops!
  ```
- **बैकप्रेशर**: उपभोक्ताओं द्वारा अतिरिक्त डेटा स्ट्रीम को कैसे संभालना है, ऑपरेटरों जैसे `onBackpressureBuffer()` या `onBackpressureDrop()` का उपयोग करके नियंत्रित करें।

---

### 7. और अधिक खोजें
अधिक उन्नत उपयोग के लिए:
- [अधिकारिक Reactor दस्तावेज़](https://projectreactor.io/docs/core/release/reference/) पर जांच करें विस्तृत उदाहरण और ट्यूटोरियल के लिए।
- [reactor-core GitHub रिपॉजिटरी](https://github.com/reactor/reactor-core) पर अतिरिक्त संसाधनों के लिए देखें।

---

### सारांश
**reactor-core** का उपयोग करने के लिए:
1. अपने प्रोजेक्ट में इसे एक डिपेंडेंसी के रूप में जोड़ें।
2. `Flux` के लिए अनेक आइटम या `Mono` के लिए एकल आइटम का उपयोग करें।
3. विधियों जैसे `just` के साथ स्ट्रीम बनाएं।
4. डेटा को प्रोसेस करने के लिए सब्सक्राइब करें।
5. आवश्यकता के अनुसार ऑपरेटरों को लागू करें स्ट्रीम को परिवर्तित करने के लिए।

यह **reactor-core** के साथ रिएक्टिव प्रोग्रामिंग का एक शुरुआती मित्रतापूर्ण बिंदु है। छोटे उदाहरणों के साथ प्रयोग करें अपने रिएक्टिव पैराडाइम से परिचित होने के लिए!