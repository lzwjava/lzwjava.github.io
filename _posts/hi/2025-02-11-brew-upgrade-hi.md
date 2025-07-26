---
audio: true
generated: false
image: false
lang: hi
layout: post
title: ब्रू अपग्रेड का लॉग
translated: true
---

==> समाप्ति का कार्य
ln -s ../../Cellar/azure-cli/2.68.0/etc/bash_completion.d/az az
ln -s ../Cellar/azure-cli/2.68.0/bin/az az
ln -s ../../../Cellar/azure-cli/2.68.0/share/fish/vendor_completions.d/az.fish az.fish
ln -s ../../../Cellar/azure-cli/2.68.0/share/zsh/site-functions/_az _az
==> चेतावनियाँ
zsh पूर्णताएँ यहाँ स्थापित की गई हैं:
  /opt/homebrew/share/zsh/site-functions
==> सारांश
🍺  /opt/homebrew/Cellar/azure-cli/2.68.0: 24,507 फ़ाइलें, 580.4MB
==> `brew cleanup azure-cli` चला रहा है...
हटा रहा है: /opt/homebrew/Cellar/azure-cli/2.67.0_1... (27,401 फ़ाइलें, 647.1MB)
हटा रहा है: /Users/lzwjava/Library/Caches/Homebrew/azure-cli_bottle_manifest--2.67.0_1... (22.5KB)
हटा रहा है: /Users/lzwjava/Library/Caches/Homebrew/azure-cli--2.67.0_1... (54MB)
==> चेतावनियाँ
==> openjdk
सिस्टम जावा रैपर को इस JDK को खोजने के लिए, इसे सिम्बल लिंक करें:
  sudo ln -sfn /opt/homebrew/opt/openjdk/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk

openjdk keg-only है, जिसका अर्थ है कि इसे /opt/homebrew में सिम्बल लिंक नहीं किया गया था,
क्योंकि macOS समान सॉफ़्टवेयर प्रदान करता है और समानांतर में इस सॉफ़्टवेयर को स्थापित करने से सभी प्रकार की परेशानी हो सकती है।

अगर आपको अपने PATH में सबसे पहले openjdk की आवश्यकता है, तो चलाएँ:
  echo 'export PATH="/opt/homebrew/opt/openjdk/bin:$PATH"' >> ~/.zshrc

कंपाइलरों को openjdk खोजने के लिए आपको यह सेट करने की आवश्यकता हो सकती है:
  export CPPFLAGS="-I/opt/homebrew/opt/openjdk/include"
==> ruby
डिफ़ॉल्ट रूप से, gem द्वारा स्थापित बाइनरी यहाँ रखी जाएँगी:
  /opt/homebrew/lib/ruby/gems/3.4.0/bin

आप इसे अपने PATH में जोड़ना चाह सकते हैं।

ruby keg-only है, जिसका अर्थ है कि इसे /opt/homebrew में सिम्बल लिंक नहीं किया गया था,
क्योंकि macOS पहले से ही यह सॉफ़्टवेयर प्रदान करता है और समानांतर में एक और संस्करण स्थापित करने से सभी प्रकार की परेशानी हो सकती है।

अगर आपको अपने PATH में सबसे पहले ruby की आवश्यकता है, तो चलाएँ:
  echo 'export PATH="/opt/homebrew/opt/ruby/bin:$PATH"' >> ~/.zshrc

कंपाइलरों को ruby खोजने के लिए आपको यह सेट करने की आवश्यकता हो सकती है:
  export LDFLAGS="-L/opt/homebrew/opt/ruby/lib"
  export CPPFLAGS="-I/opt/homebrew/opt/ruby/include"
==> yt-dlp
zsh पूर्णताएँ यहाँ स्थापित की गई हैं:
  /opt/homebrew/share/zsh/site-functions
==> redis
अपग्रेड के बाद redis को पुनः आरंभ करने के लिए:
  brew services restart redis
या, यदि आपको पृष्ठभूमि सेवा की आवश्यकता नहीं है तो आप बस यह चला सकते हैं:
  /opt/homebrew/opt/redis/bin/redis-server /opt/homebrew/etc/redis.conf
==> perl
डिफ़ॉल्ट रूप से गैर-ब्रूड cpan मॉड्यूल सेलर में स्थापित किए जाते हैं। यदि आप चाहते हैं
कि आपके मॉड्यूल अपडेट के दौरान बने रहें तो हम `local::lib` का उपयोग करने की सलाह देते हैं।

आप इसे इस तरह से सेट कर सकते हैं:
  PERL_MM_OPT="INSTALL_BASE=$HOME/perl5" cpan local::lib
और अपनी शेल प्रोफ़ाइल जैसे ~/.profile या ~/.zshrc में निम्नलिखित जोड़ें
  eval "$(perl -I$HOME/perl5/lib/perl5 -Mlocal::lib=$HOME/perl5)"
==> awscli
"उदाहरण" निर्देशिका यहाँ स्थापित की गई है:
  /opt/homebrew/share/awscli/examples

zsh पूर्णताएँ और फलन यहाँ स्थापित किए गए हैं:
  /opt/homebrew/share/zsh/site-functions
==> php
Apache में PHP को सक्षम करने के लिए httpd.conf में निम्नलिखित जोड़ें और Apache को पुनः आरंभ करें:
    LoadModule php_module /opt/homebrew/opt/php/lib/httpd/modules/libphp.so

    <FilesMatch \.php$>
        SetHandler application/x-httpd-php
    </FilesMatch>

अंत में, जांचें कि DirectoryIndex में index.php शामिल है
    DirectoryIndex index.php index.html

php.ini और php-fpm.ini फ़ाइल यहाँ मिल सकती है:
    /opt/homebrew/etc/php/8.4/

अब php प्रारंभ करने और लॉगिन पर पुनः आरंभ करने के लिए:
  brew services start php
या, यदि आपको पृष्ठभूमि सेवा की आवश्यकता नहीं है तो आप बस यह चला सकते हैं:
  /opt/homebrew/opt/php/sbin/php-fpm --nodaemonize
==> nginx
डॉक रूट है: /opt/homebrew/var/www

डिफ़ॉल्ट पोर्ट को /opt/homebrew/etc/nginx/nginx.conf में 8080 पर सेट किया गया है ताकि
nginx sudo के बिना चल सके।

nginx /opt/homebrew/etc/nginx/servers/ में सभी फ़ाइलों को लोड करेगा।

अपग्रेड के बाद nginx को पुनः आरंभ करने के लिए:
  brew services restart nginx
या, यदि आपको पृष्ठभूमि सेवा की आवश्यकता नहीं है तो आप बस यह चला सकते हैं:
  /opt/homebrew/opt/nginx/bin/nginx -g daemon\ off\;
==> git-lfs
स्थापना पूरी करने के लिए अपनी git कॉन्फ़िगरेशन अपडेट करें:

  # वैश्विक git कॉन्फ़िगरेशन अपडेट करें
  $ git lfs install

  # सिस्टम git कॉन्फ़िगरेशन अपडेट करें
  $ git lfs install --system

zsh पूर्णताएँ यहाँ स्थापित की गई हैं:
  /opt/homebrew/share/zsh/site-functions
==> wireshark
यह फ़ॉर्मूला डिफ़ॉल्ट रूप से केवल कमांड-लाइन उपयोगिताएँ स्थापित करता है।

Homebrew Cask के साथ Wireshark.app स्थापित करें:
  brew install --cask wireshark

यदि आपके उपलब्ध कैप्चर इंटरफ़ेस की सूची खाली है
(डिफ़ॉल्ट macOS व्यवहार), ChmodBPF स्थापित करें:
  brew install --cask wireshark-chmodbpf
==> doctl
zsh पूर्णताएँ यहाँ स्थापित की गई हैं:
  /opt/homebrew/share/zsh/site-functions
==> azure-cli
zsh पूर्णताएँ यहाँ स्थापित की गई हैं:
  /opt/homebrew/share/zsh/site-functions
