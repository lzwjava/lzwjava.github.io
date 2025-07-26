---
audio: true
generated: false
image: false
lang: ar
layout: post
title: سجل ترقية برو
translated: true
---

==> الانتهاء
ln -s ../../Cellar/azure-cli/2.68.0/etc/bash_completion.d/az az
ln -s ../Cellar/azure-cli/2.68.0/bin/az az
ln -s ../../../Cellar/azure-cli/2.68.0/share/fish/vendor_completions.d/az.fish az.fish
ln -s ../../../Cellar/azure-cli/2.68.0/share/zsh/site-functions/_az _az
==> التحذيرات
تم تثبيت إكمالات zsh في:
  /opt/homebrew/share/zsh/site-functions
==> الملخص
🍺  /opt/homebrew/Cellar/azure-cli/2.68.0: 24,507 ملفات، 580.4 ميجابايت
==> تشغيل `brew cleanup azure-cli`...
إزالة: /opt/homebrew/Cellar/azure-cli/2.67.0_1... (27,401 ملف، 647.1 ميجابايت)
إزالة: /Users/lzwjava/Library/Caches/Homebrew/azure-cli_bottle_manifest--2.67.0_1... (22.5 كيلوبايت)
إزالة: /Users/lzwjava/Library/Caches/Homebrew/azure-cli--2.67.0_1... (54 ميجابايت)
==> التحذيرات
==> openjdk
لكي تجد ملفات Java الخاصة بالنظام هذا JDK، قم بإنشاء رابط رمزي باستخدام:
  sudo ln -sfn /opt/homebrew/opt/openjdk/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk

openjdk هو keg-only، وهذا يعني أنه لم يتم إنشاء رابط رمزي له في /opt/homebrew،
لأن macOS يوفر برامج مماثلة، وتثبيت هذا البرنامج بالتوازي يمكن أن يسبب جميع أنواع المشاكل.

إذا كنت بحاجة إلى وضع openjdk أولاً في PATH الخاص بك، فقم بتشغيل:
  echo 'export PATH="/opt/homebrew/opt/openjdk/bin:$PATH"' >> ~/.zshrc

لكي يجد المُجمّعات openjdk، قد تحتاج إلى تعيين:
  export CPPFLAGS="-I/opt/homebrew/opt/openjdk/include"
==> ruby
بشكل افتراضي، سيتم وضع الملفات التنفيذية التي تم تثبيتها بواسطة gem في:
  /opt/homebrew/lib/ruby/gems/3.4.0/bin

قد ترغب في إضافة هذا إلى PATH الخاص بك.

ruby هو keg-only، وهذا يعني أنه لم يتم إنشاء رابط رمزي له في /opt/homebrew،
لأن macOS يوفر بالفعل هذا البرنامج، وتثبيت إصدار آخر بالتوازي يمكن أن يسبب جميع أنواع المشاكل.

إذا كنت بحاجة إلى وضع ruby أولاً في PATH الخاص بك، فقم بتشغيل:
  echo 'export PATH="/opt/homebrew/opt/ruby/bin:$PATH"' >> ~/.zshrc

لكي يجد المُجمّعات ruby، قد تحتاج إلى تعيين:
  export LDFLAGS="-L/opt/homebrew/opt/ruby/lib"
  export CPPFLAGS="-I/opt/homebrew/opt/ruby/include"
==> yt-dlp
تم تثبيت إكمالات zsh في:
  /opt/homebrew/share/zsh/site-functions
==> redis
لإعادة تشغيل redis بعد الترقية:
  brew services restart redis
أو، إذا كنت لا تريد/لا تحتاج إلى خدمة خلفية، فيمكنك فقط تشغيل:
  /opt/homebrew/opt/redis/bin/redis-server /opt/homebrew/etc/redis.conf
==> perl
بشكل افتراضي، يتم تثبيت وحدات cpan غير المُثبتة بواسطة brew في Cellar. إذا كنت ترغب
في أن تستمر وحداتك عبر التحديثات، نوصي باستخدام `local::lib`.

يمكنك إعداد ذلك على هذا النحو:
  PERL_MM_OPT="INSTALL_BASE=$HOME/perl5" cpan local::lib
واضف ما يلي إلى ملف تعريف shell الخاص بك، مثل ~/.profile أو ~/.zshrc
  eval "$(perl -I$HOME/perl5/lib/perl5 -Mlocal::lib=$HOME/perl5)"
==> awscli
تم تثبيت دليل "examples" في:
  /opt/homebrew/share/awscli/examples

تم تثبيت إكمالات ووظائف zsh في:
  /opt/homebrew/share/zsh/site-functions
==> php
لتفعيل PHP في Apache، أضف ما يلي إلى httpd.conf وأعد تشغيل Apache:
    LoadModule php_module /opt/homebrew/opt/php/lib/httpd/modules/libphp.so

    <FilesMatch \.php$>
        SetHandler application/x-httpd-php
    </FilesMatch>

أخيرًا، تحقق من أن DirectoryIndex يتضمن index.php
    DirectoryIndex index.php index.html

يمكن العثور على ملف php.ini و php-fpm.ini في:
    /opt/homebrew/etc/php/8.4/

لبدء php الآن وإعادة تشغيله عند تسجيل الدخول:
  brew services start php
أو، إذا كنت لا تريد/لا تحتاج إلى خدمة خلفية، فيمكنك فقط تشغيل:
  /opt/homebrew/opt/php/sbin/php-fpm --nodaemonize
==> nginx
جذر المستندات هو: /opt/homebrew/var/www

تم تعيين المنفذ الافتراضي في /opt/homebrew/etc/nginx/nginx.conf إلى 8080 بحيث
يمكن تشغيل nginx بدون sudo.

سيقوم nginx بتحميل جميع الملفات الموجودة في /opt/homebrew/etc/nginx/servers/.

لإعادة تشغيل nginx بعد الترقية:
  brew services restart nginx
أو، إذا كنت لا تريد/لا تحتاج إلى خدمة خلفية، فيمكنك فقط تشغيل:
  /opt/homebrew/opt/nginx/bin/nginx -g daemon\ off\;
==> git-lfs
حدّث إعدادات git الخاصة بك لإكمال التثبيت:

  # تحديث إعدادات git العالمية
  $ git lfs install

  # تحديث إعدادات git للنظام
  $ git lfs install --system

تم تثبيت إكمالات zsh في:
  /opt/homebrew/share/zsh/site-functions
==> wireshark
يقوم هذا البرنامج بتثبيت أدوات سطر الأوامر فقط بشكل افتراضي.

قم بتثبيت Wireshark.app باستخدام Homebrew Cask:
  brew install --cask wireshark

إذا كانت قائمة واجهات الالتقاط المتاحة لديك فارغة
(سلوك macOS الافتراضي)، قم بتثبيت ChmodBPF:
  brew install --cask wireshark-chmodbpf
==> doctl
تم تثبيت إكمالات zsh في:
  /opt/homebrew/share/zsh/site-functions
==> azure-cli
تم تثبيت إكمالات zsh في:
  /opt/homebrew/share/zsh/site-functions

