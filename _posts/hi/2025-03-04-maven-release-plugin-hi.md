---
audio: false
generated: true
lang: hi
layout: post
title: मेवेन रिलीज़ प्लगइन
translated: true
---

यह एक व्यापक मार्गदर्शिका है कि कैसे **Maven Release Plugin** का उपयोग करके आप अपने Maven प्रोजेक्ट के लिए रिलीज़ प्रोसेस को प्रबंधित और स्वचालित कर सकते हैं।

---

### Maven Release Plugin क्या है?

**Maven Release Plugin** एक औजार है जो एक Maven प्रोजेक्ट को रिलीज़ करने की प्रक्रिया को स्वचालित करता है। यह निम्नलिखित कार्यों को संभालता है:

- प्रोजेक्ट के POM फ़ाइल(ओं) में वर्जन नंबर अपडेट करना।
- वर्जन नियंत्रण प्रणाली (VCS), जैसे कि Git में परिवर्तन को कमिट करना।
- VCS में रिलीज़ के लिए एक टैग बनाना।
- रिलीज़ आर्टिफैक्ट्स को बनाना और डिप्लॉय करना।
- अगले विकास चक्र के लिए प्रोजेक्ट को तैयार करना वर्जन नंबर को फिर से अपडेट करके।

प्लगइन के दो प्राथमिक लक्ष्य हैं:

- **`release:prepare`**: प्रोजेक्ट को रिलीज़ के लिए तैयार करता है वर्जन अपडेट, परिवर्तन कमिट और VCS में रिलीज़ को टैग करके।
- **`release:perform`**: VCS से टैग किए गए कोड का उपयोग करके रिलीज़ वर्जन को बनाता और डिप्लॉय करता है।

---

### Maven Release Plugin का उपयोग करने का चरणबद्ध मार्गदर्शिका

#### 1. POM फ़ाइल में Maven Release Plugin जोड़ें

प्लगइन का उपयोग करने के लिए, आपको इसे प्रोजेक्ट के `pom.xml` में शामिल करना होगा। इसे `<build><plugins>` खंड के तहत निम्न प्रकार से जोड़ें:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-release-plugin</artifactId>
            <version>2.5.3</version> <!-- नवीनतम स्थिर वर्जन का उपयोग करें -->
        </plugin>
    </plugins>
</build>
```

**नोट**: नवीनतम वर्जन के लिए [अधिकृत Maven Release Plugin पेज](https://maven.apache.org/maven-release/maven-release-plugin/) पर जाकर `2.5.3` को अनुकूलित करें।

#### 2. SCM (सोर्स कंट्रोल मैनेजमेंट) खंड का विन्यास करें

प्लगइन VCS (जैसे कि Git) के साथ बातचीत करता है परिवर्तन को कमिट करने और टैग बनाने के लिए। आपको अपने VCS की विवरण को `pom.xml` के `<scm>` खंड में स्पष्ट करना होगा। एक GitHub पर होस्टेड Git रिपोजिटरी के लिए, यह इस प्रकार दिख सकता है:

```xml
<scm>
    <connection>scm:git:git://github.com/username/project.git</connection>
    <developerConnection>scm:git:git@github.com:username/project.git</developerConnection>
    <url>https://github.com/username/project</url>
</scm>
```

- `username` और `project` को अपने वास्तविक GitHub यूजरनेम और रिपोजिटरी नाम से बदलें।
- अगर आप किसी अन्य Git होस्टिंग सेवा (जैसे कि GitLab, Bitbucket) का उपयोग कर रहे हैं, तो URL को अनुकूलित करें।
- रिपोजिटरी में परिवर्तन को पुश करने के लिए आवश्यक क्रेडेंशियल (जैसे कि SSH keys या एक व्यक्तिगत एक्सेस टोकन) को विन्यासित करने की सुनिश्चित करें।

#### 3. प्रोजेक्ट को रिलीज़ के लिए तैयार करें

रिलीज़ कमांड चलाने से पहले, सुनिश्चित करें कि आपका प्रोजेक्ट तैयार है:

- सभी टेस्ट पास होते हैं (`mvn test`).
- आपके कार्य क्षेत्र में कोई अनकमिटेड परिवर्तन नहीं हैं (परिवर्तन की जांच के लिए `git status` चलाएं).
- आप रिलीज़ के लिए सही ब्रांच (जैसे कि `master` या `main`) पर हैं।

#### 4. `release:prepare` चलाएं

`release:prepare` लक्ष्य आपके प्रोजेक्ट को रिलीज़ के लिए तैयार करता है। अपने टर्मिनल में निम्न कमांड चलाएं:

```bash
mvn release:prepare
```

**`release:prepare` के दौरान क्या होता है**:

- **अनकमिटेड परिवर्तन की जांच**: सुनिश्चित करता है कि आपके कार्य क्षेत्र साफ़ है।
- **वर्जन के लिए प्रॉम्प्ट करता है**: रिलीज़ वर्जन और अगले विकास वर्जन के लिए पूछता है।
  - उदाहरण: अगर आपका वर्तमान वर्जन `1.0-SNAPSHOT` है, तो यह `1.0` के लिए रिलीज़ और `1.1-SNAPSHOT` के लिए अगले विकास वर्जन के लिए सुझाव दे सकता है। आप डिफ़ॉल्ट्स को स्वीकार कर सकते हैं या कस्टम वर्जन (जैसे कि `1.0.1` के लिए एक पैच रिलीज़) दर्ज कर सकते हैं।
- **POM फ़ाइलें अपडेट करता है**: वर्जन को रिलीज़ वर्जन (जैसे कि `1.0`) में बदलता है, परिवर्तन को कमिट करता है और इसे VCS में टैग करता है (जैसे कि `project-1.0`).
- **अगले चक्र के लिए तैयार करता है**: POM को अगले विकास वर्जन (जैसे कि `1.1-SNAPSHOT`) में अपडेट करता है और इसे कमिट करता है।

**वैकल्पिक ड्राई रन**: परिवर्तन किए बिना प्रक्रिया को टेस्ट करने के लिए, उपयोग करें:

```bash
mvn release:prepare -DdryRun=true
```

यह तैयारी चरणों को सिमुलेट करता है बिना कमिट या टैग करने के।

#### 5. `release:perform` चलाएं

रिलीज़ तैयार करने के बाद, इसे बनाएं और डिप्लॉय करें:

```bash
mvn release:perform
```

**`release:perform` के दौरान क्या होता है**:

- VCS से टैग किए गए वर्जन को चेकआउट करता है।
- प्रोजेक्ट को बनाता है।
- आर्टिफैक्ट्स को POM के `<distributionManagement>` खंड में स्पष्टित रिपोजिटरी में डिप्लॉय करता है।

**`<distributionManagement>` का विन्यास करें** (अगर किसी रिमोट रिपोजिटरी में डिप्लॉय करने के लिए):

```xml
<distributionManagement>
    <repository>
        <id>releases</id>
        <url>http://my-repository-manager/releases</url>
    </repository>
    <snapshotRepository>
        <id>snapshots</id>
        <url>http://my-repository-manager/snapshots</url>
    </snapshotRepository>
</distributionManagement>
```

- URL को अपने रिपोजिटरी मैनेजर के पते (जैसे कि Nexus, Artifactory) से बदलें।
- सुनिश्चित करें कि क्रेडेंशियल आपके `~/.m2/settings.xml` फ़ाइल में `<servers>` के तहत मिलते हैं साथ मिलते हैं `id`s।

#### 6. रिलीज़ की पुष्टि करें

`release:perform` के बाद, रिलीज़ की पुष्टि करें:

- सुनिश्चित करें कि आर्टिफैक्ट्स (जैसे कि JARs, स्रोत) रिपोजिटरी मैनेजर में डिप्लॉय किए गए हैं।
- रिलीज़ वर्जन को किसी अन्य प्रोजेक्ट में एक डिपेंडेंसी के रूप में जोड़कर टेस्ट करें।

---

### अतिरिक्त विन्यास और टिप्स

#### विफलताओं का प्रबंधन

- **साफ़ करना**: अगर रिलीज़ प्रक्रिया विफल हो जाती है, तो उपयोग करें:
  ```bash
  mvn release:clean
  ```
  प्लगइन द्वारा बनाए गए अस्थायी फ़ाइलों को हटाने के लिए।
- **रोलबैक**: `release:prepare` द्वारा किए गए परिवर्तन को वापस करने के लिए:
  ```bash
  mvn release:rollback
  ```
  सावधानी बरतें और जो परिवर्तन वापस किए जा रहे हैं, उन्हें सत्यापित करें।

#### बहु-मॉड्यूल प्रोजेक्ट

बहु-मॉड्यूल प्रोजेक्ट के लिए, प्लगइन डिफ़ॉल्ट रूप से सभी मॉड्यूलों में वर्जन को एकसमान रूप से अपडेट करता है। सुनिश्चित करें कि माता-पिता POM में प्लगइन और SCM विन्यास शामिल है।

#### स्वचालन के लिए बैच मोड

रिलीज़ को नॉन-इंटरैक्टिव रूप से (जैसे कि एक CI/CD पाइपलाइन में) चलाने के लिए, `-B` फ्लैग का उपयोग करें और वर्जन स्पष्ट करें:

```bash
mvn release:prepare -B -DreleaseVersion=1.0 -DdevelopmentVersion=1.1-SNAPSHOT
mvn release:perform -B
```

#### आम समस्याएं और समाधान

- **VCS त्रुटियां**: सुनिश्चित करें कि Git कमांड (जैसे कि `git commit`, `git push`) मैन्युअल रूप से काम करते हैं। प्रमाणिकता (SSH keys, टोकन) की जांच करें।
- **बिल्ड विफलताएं**: सुनिश्चित करें कि बिल्ड स्थानीय रूप से सफल होता है (`mvn clean install`) और डिपेंडेंसियाँ सही ढंग से सुलझ जाती हैं।
- **वर्जन रणनीति**: डिफ़ॉल्ट्स को अनुकूलित करने के लिए वर्जन को प्रॉम्प्ट के दौरान या प्रॉपर्टीज के माध्यम से कस्टमाइज़ करें अगर वे आपके आवश्यकताओं को पूरा नहीं करते हैं।

---

### कमांडों की सारांश

1. **रिलीज़ तैयार करें**:
   ```bash
   mvn release:prepare
   ```
2. **रिलीज़ करें**:
   ```bash
   mvn release:perform
   ```
3. **वैकल्पिक ड्राई रन**:
   ```bash
   mvn release:prepare -DdryRun=true
   ```
4. **अगर आवश्यक हो तो साफ़ करना या रोलबैक करना**:
   ```bash
   mvn release:clean
   mvn release:rollback
   ```

---

### निष्कर्ष

Maven Release Plugin रिलीज़ प्रक्रिया को सरल बनाता है वर्जन प्रबंधन, VCS बातचीत और डिप्लॉयमेंट को स्वचालित करके। POM में प्लगइन जोड़ने, SCM विन्यास करने और `release:prepare` और `release:perform` चरणों का पालन करके, आप अपने Maven प्रोजेक्ट को दक्षता से रिलीज़ कर सकते हैं। हमेशा अपने विन्यास को एक ड्राई रन के साथ टेस्ट करें और परिणामों की पुष्टि करें सुनिश्चित करने के लिए एक सुलभ रिलीज़ प्रक्रिया।