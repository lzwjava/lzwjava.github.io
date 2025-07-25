---
audio: false
generated: false
image: false
lang: hi
layout: post
title: Zsh प्रोफाइल
translated: true
---

यह zsh प्रोफ़ाइल कमांड-लाइन अनुभव को बढ़ाने के लिए बनाया गया है, जिसमें प्रॉक्सी कॉन्फ़िगरेशन, गिट इंटीग्रेशन, और उपयोगी एलियास पर फोकस है। नीचे दिए गए सेक्शन इसकी विशेषताओं का विवरण देते हैं:

**1. PATH कॉन्फ़िगरेशन:**

   - `export PATH=...`: यह लाइन `PATH` पर्यावरण चर सेट करती है, जो शेल को बताती है कि एग्ज़ीक्यूटेबल फ़ाइलों को कहाँ ढूँढ़ना है। यह विभिन्न डायरेक्टरी जैसे जावा, रूबी, होमब्रू, पायथन, फ्लटर, और गूगल क्लाउड एसडीके शामिल करती है। यह सुनिश्चित करता है कि इन टूल्स के कमांड सीधे टर्मिनल से चलाए जा सकते हैं।

**2. प्रॉक्सी प्रबंधन:**

   - `export GLOBAL_PROXY='127.0.0.1:7890'`: यह प्रॉक्सी सर्वर पते को रखने वाली चर `GLOBAL_PROXY` को परिभाषित करता है।
   - `function start_proxy { ... }`: यह फंक्शन `HTTP_PROXY`, `HTTPS_PROXY`, `http_proxy`, `https_proxy`, और `ALL_PROXY` पर्यावरण चर को निर्दिष्ट प्रॉक्सी का उपयोग करने के लिए सेट करता है। यह प्रॉक्सी के लिए पूर्ण URI अनुरोधों को अक्षम भी करता है।
   - `function start_proxy_without_prefix { ... }`: `start_proxy` के समान, लेकिन `http://` उपसर्ग के बिना प्रॉक्सी चर सेट करता है।
   - `function stop_proxy { ... }`: यह फंक्शन प्रॉक्सी चर असेट करता है, जिससे प्रॉक्सी अक्षम हो जाता है। यह प्रॉक्सी के लिए पूर्ण URI अनुरोधों को सक्षम भी करता है।
   - `export NO_PROXY="localhost,127.0.0.1,.example.com,::1"`: यह उन होस्ट्स की एक सूची निर्दिष्ट करता है जो प्रॉक्सी को बाईपास कर सकते हैं।

**3. गिट प्रॉक्सी:**

   - `function start_git_proxy { ... }`: यह फंक्शन गिट को एचटीटीपी और एचटीटीपीएस कनेक्शन के लिए ग्लोबल प्रॉक्सी का उपयोग करने के लिए कॉन्फ़िगर करता है।
   - `function stop_git_proxy { ... }`: यह फंक्शन गिट प्रॉक्सी सेटिंग्स को असेट करता है।

**4. होमब्रू इंटीग्रेशन:**

   - `eval "$(/opt/homebrew/bin/brew shellenv)"`: यह लाइन होमब्रू को शेल पर्यावरण में एकीकृत करती है, जिससे आप होमब्रू कमांड का उपयोग कर सकते हैं।

**5. सुविधाजनक एलियास:**

   - `alias gpa='python ~/bin/gitmessageai.py --api mistral'`: यह `gpa` नामक एक एलियास बनाता है जो `gitmessageai.py` नामक पायथन स्क्रिप्ट को मिस्ट्रल एपीआई के साथ चलाता है।
   - `alias gca='python ~/bin/gitmessageai.py --no-push'`: यह `gca` नामक एक एलियास बनाता है जो बदलावों को पुश किए बिना उसी स्क्रिप्ट को चलाता है।
   - `alias gm='python ~/bin/gitmessageai.py --only-message'`: यह `gm` नामक एक एलियास बनाता है जो उसी स्क्रिप्ट को चलाता है और सिर्फ कमिट मैसेज प्रिंट करता है।
   - `alias gpam=/usr/local/bin/git-auto-commit`: यह `gpam` नामक एक एलियास बनाता है जो `git-auto-commit` स्क्रिप्ट को चलाता है।
   - `alias rougify=/Users/lzwjava/projects/rouge/bin/rougify`: यह `rougify` नामक एक एलियास बनाता है जो `rougify` स्क्रिप्ट को चलाता है।

**6. एसएसएल सर्टिफिकेट:**

   - `export SSL_CERT_FILE=~/bin/cacert.pem`: यह एक कस्टम एसएसएल सर्टिफिकेट फ़ाइल के पाथ को सेट करता है।

**7. होमब्रू ऑटो-अपडेट:**

   - `export HOMEBREW_NO_AUTO_UPDATE=1`: यह होमब्रू के ऑटोमैटिक अपडेट को अक्षम करता है।

**8. प्री-एग्ज़ीक्यूशन प्रॉक्सी चेक:**

   - `preexec() { ... }`: यह फंक्शन हर कमांड के पहले चलता है। यह चेक करता है कि कमांड नेटवर्क-निर्भर कमांड्स की सूची में है कि नहीं। अगर है, और अगर कोई प्रॉक्सी चर सेट हैं, तो यह प्रॉक्सी सेटिंग्स को प्रदर्शित करता है।
   - `local network_commands=( ... )`: यह एरे उन कमांड्स की सूची करता है जो नेटवर्क-निर्भर माने जाते हैं।
   - `display_proxy() { ... }`: यह फंक्शन वर्तमान प्रॉक्सी सेटिंग्स को प्रदर्शित करता है।

**9. गूगल क्लाउड एसडीके कम्प्लीशन:**

   - `if [ -f '/Users/lzwjava/bin/google-cloud-sdk/completion.zsh.inc' ]; then . '/Users/lzwjava/bin/google-cloud-sdk/completion.zsh.inc'; fi`: यह लाइन ग्क्लाउड के लिए शेल कमांड कम्प्लीशन को सक्षम करती है।

**10. एपीआई कीज और क्रेडेंशियल्स:**

    - `export GOOGLE_APPLICATION_CREDENTIALS="/Users/lzwjava/bin/graphite-ally-445108-k3-035f0952219d.json"`: गूगल क्लाउड सर्विस अकाउंट क्रेडेंशियल्स के पाथ को सेट करता है।
    - `export DEEPSEEK_API_KEY="xxx"`: डीपसीक एपीआई की को सेट करता है।
    - `export MISTRAL_API_KEY="xxx"`: मिस्ट्रल एपीआई की को सेट करता है।
    - `export DYLD_LIBRARY_PATH=$(brew --prefix curl)/lib`: कर्ल के लिए डायनेमिक लाइब्रेरी पाथ सेट करता है।
    - `export SPEECH_ENDPOINT="https://ai-lzwjava-5596.cognitiveservices.azure.com/"`: एज़्यूर स्पीच एंडपॉइंट सेट करता है।
    - `export DO_API_KEY="xxx"`: डिजिटल ओशन एपीआई की को सेट करता है।
    - `export GEMINI_API_KEY="xxx"`: जेमिनी एपीआई की को सेट करता है।

**11. कोंडा पर्यावरण:**

    - `conda activate base`: बेस कोंडा पर्यावरण को एक्टिवेट करता है।

**सारांश में, यह zsh प्रोफ़ाइल एक डेवलपर के लिए एक व्यापक सेटअप प्रदान करता है, जिसमें शामिल हैं:**

- प्रॉक्सी प्रबंधन के लिए आसान फंक्शन जो प्रॉक्सी शुरू और रोक सकते हैं।
- गिट प्रॉक्सी कॉन्फ़िगरेशन।
- होमब्रू के साथ एकीकरण।
- आम कार्यों के लिए सुविधाजनक एलियास।
- नेटवर्क-निर्भर कमांड्स के लिए प्री-एग्ज़ीक्यूशन प्रॉक्सी चेक।
- विभिन्न सेवाओं के लिए एपीआई कीज और क्रेडेंशियल्स।
- कोंडा पर्यावरण एक्टिवेशन।

इस प्रोफ़ाइल का उद्देश्य उपयोगकर्ता के वर्कफ़्लो को स्ट्रीमलाइन करना और विभिन्न विकास टूल्स और सेवाओं को प्रबंधित करना आसान बनाना है।

```bash
export PATH=/opt/homebrew/Cellar/openjdk@17/17.0.13/libexec/openjdk.jdk/Contents/Home/bin:/opt/homebrew/opt/ruby/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Users/lzwjava/Library/Python/3.9/bin:/Library/TeX/texbin:/Users/lzwjava/bin:/Users/lzwjava/platform-tools:/Users/lzwjava/Downloads/google-cloud-sdk/bin:/Users/lzwjava/bin/flutter/bin:/opt/homebrew/lib/ruby/gems/3.3.0/bin:/opt/homebrew/Cellar/llama.cpp/4539/bin:/Users/lzwjava/bin/google-cloud-sdk/bin

# /opt/homebrew/opt/openjdk/bin

# /opt/homebrew/Cellar/openjdk@17/17.0.13/libexec/openjdk.jdk/Contents/Home/bin

export GLOBAL_PROXY='127.0.0.1:7890'
# export GLOBAL_PROXY='http://192.168.1.1:7890'

function start_proxy {
    export HTTP_PROXY="http://$GLOBAL_PROXY"
    export HTTPS_PROXY="http://$GLOBAL_PROXY"
    export http_proxy="http://$GLOBAL_PROXY"
    export https_proxy="http://$GLOBAL_PROXY"
    export HTTP_PROXY_REQUEST_FULLURI=false
    export HTTPS_PROXY_REQUEST_FULLURI=false
    export ALL_PROXY=$http_proxy
}

function start_proxy_without_prefix {
    export http_proxy=$GLOBAL_PROXY
		export HTTP_PROXY=$GLOBAL_PROXY
		export https_proxy=$GLOBAL_PROXY
    export HTTPS_PROXY=$GLOBAL_PROXY
    export HTTP_PROXY_REQUEST_FULLURI=false
    export HTTPS_PROXY_REQUEST_FULLURI=false
		export ALL_PROXY=$http_proxy
}

function stop_proxy {
    export http_proxy=
		export HTTP_PROXY=
		export https_proxy=
    export HTTPS_PROXY=
    export HTTP_PROXY_REQUEST_FULLURI=true
    export HTTPS_PROXY_REQUEST_FULLURI=true
		export ALL_PROXY=
}

export NO_PROXY="localhost,127.0.0.1,.example.com,::1"

function start_git_proxy {
  git config --global http.proxy $GLOBAL_PROXY
  git config --global https.proxy $GLOBAL_PROXY
}

function stop_git_proxy {
  git config --global --unset http.proxy
  git config --global --unset https.proxy
}

eval "$(/opt/homebrew/bin/brew shellenv)"

start_proxy
# start_git_proxy

# alias python3=/opt/homebrew/bin/python3
# alias pip3=/opt/homebrew/bin/pip3
# alias pip=pip3

alias gpa='python ~/bin/gitmessageai.py --api mistral'
alias gca='python ~/bin/gitmessageai.py --no-push'
alias gm='python ~/bin/gitmessageai.py --only-message'

alias gpam=/usr/local/bin/git-auto-commit

# bundle exec jekyll serve
export SSL_CERT_FILE=~/bin/cacert.pem

alias rougify=/Users/lzwjava/projects/rouge/bin/rougify

# git config --global core.editor "code --wait"
# git config --global -e

export HOMEBREW_NO_AUTO_UPDATE=1

# कुछ कमांड से पहले प्रॉक्सी सेटिंग्स को चेक करने और प्रदर्शित करने के लिए फंक्शन
# कुछ कमांड से पहले प्रॉक्सी सेटिंग्स को चेक करने और प्रदर्शित करने के लिए फंक्शन
preexec() {
    # नेटवर्क-निर्भर कमांड्स को परिभाषित करें
    local network_commands=(
        "gpa"
        "git"
        "ssh"
        "scp"
        "sftp"
        "rsync"
        "curl"
        "wget"
        "apt"
        "yum"
        "dnf"
        "npm"
        "yarn"
        "pip"
        "pip3"
        "gem"
        "cargo"
        "docker"
        "kubectl"
        "ping"
        "traceroute"
        "netstat"
        "ss"
        "ip"
        "ifconfig"
        "dig"
        "nslookup"
        "nmap"
        "telnet"
        "ftp"
        "nc"
        "tcpdump"
        "adb"
        "bundle"
        "brew"
        "cpanm"
        "bundle exec jekyll"
        "make"
        "python"
        "glcoud"
        # ज़रूरत के अनुसार और कमांड जोड़ें
    )

    # कमांड लाइन से पहले शब्द (कमांड) को निकालें
    local cmd
    cmd=$(echo "$1" | awk '{print $1}')

    # प्रॉक्सी चर को प्रदर्शित करने के लिए फंक्शन
    display_proxy() {
        echo -e "🚀 **प्रॉक्सी सेटिंग्स का पता चला:**"

        [ -n "$HTTP_PROXY" ] && echo "   - HTTP_PROXY: $HTTP_PROXY"
        [ -n "$HTTPS_PROXY" ] && echo "   - HTTPS_PROXY: $HTTPS_PROXY"

        echo ""
    }

    # चेक करें कि कमांड नेटवर्क-निर्भर है कि नहीं
    for network_cmd in "${network_commands[@]}"; do
        if [[ "$1" == "$network_cmd"* ]]; then
            if [ -n "$HTTP_PROXY" ] || [ -n "$http_proxy" ] || \
               [ -n "$HTTPS_PROXY" ] || [ -n "$https_proxy" ] || \
               [ -n "$ALL_PROXY" ] || [ -n "$all_proxy" ]; then

                display_proxy
            fi
            break
        fi
    done
}

# अगली लाइन gcloud के लिए शेल कमांड कम्प्लीशन को सक्षम करती है।
if [ -f '/Users/lzwjava/bin/google-cloud-sdk/completion.zsh.inc' ]; then . '/Users/lzwjava/bin/google-cloud-sdk/completion.zsh.inc'; fi

export GOOGLE_APPLICATION_CREDENTIALS="/Users/lzwjava/bin/graphite-ally-445108-k3-035f0952219d.json"

export DEEPSEEK_API_KEY="xxx"

export MISTRAL_API_KEY="xxx"

export DYLD_LIBRARY_PATH=$(brew --prefix curl)/lib

export SPEECH_ENDPOINT="https://ai-lzwjava-5596.cognitiveservices.azure.com/"

export DO_API_KEY="xxx"

export GEMINI_API_KEY="xxx"

conda activate base
```