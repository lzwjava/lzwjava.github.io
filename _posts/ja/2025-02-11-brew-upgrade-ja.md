---
audio: true
generated: false
image: false
lang: ja
layout: post
title: 醸造アップグレードログ
translated: true
---

==> まとめ
ln -s ../../Cellar/azure-cli/2.68.0/etc/bash_completion.d/az az
ln -s ../Cellar/azure-cli/2.68.0/bin/az az
ln -s ../../../Cellar/azure-cli/2.68.0/share/fish/vendor_completions.d/az.fish az.fish
ln -s ../../../Cellar/azure-cli/2.68.0/share/zsh/site-functions/_az _az
==> 注意点
zsh補完機能は以下にインストールされました:
  /opt/homebrew/share/zsh/site-functions
==> 要約
🍺  /opt/homebrew/Cellar/azure-cli/2.68.0: 24,507 ファイル, 580.4MB
==> `brew cleanup azure-cli` を実行しています...
削除: /opt/homebrew/Cellar/azure-cli/2.67.0_1... (27,401 ファイル, 647.1MB)
削除: /Users/lzwjava/Library/Caches/Homebrew/azure-cli_bottle_manifest--2.67.0_1... (22.5KB)
削除: /Users/lzwjava/Library/Caches/Homebrew/azure-cli--2.67.0_1... (54MB)
==> 注意点
==> openjdk
システムJavaラッパーがこのJDKを検出するには、シンボリックリンクを作成します。
  sudo ln -sfn /opt/homebrew/opt/openjdk/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk

openjdkはkeg-onlyです。つまり、macOSが同様のソフトウェアを提供しており、並行してインストールすると様々な問題が発生する可能性があるため、/opt/homebrewにシンボリックリンクされませんでした。

PATHの先頭にopenjdkを配置する必要がある場合は、以下を実行してください:
  echo 'export PATH="/opt/homebrew/opt/openjdk/bin:$PATH"' >> ~/.zshrc

コンパイラでopenjdkを使用するには、以下を設定する必要がある場合があります:
  export CPPFLAGS="-I/opt/homebrew/opt/openjdk/include"
==> ruby
デフォルトでは、gemによってインストールされたバイナリは以下に配置されます:
  /opt/homebrew/lib/ruby/gems/3.4.0/bin

PATHに追加することをお勧めします。

rubyはkeg-onlyです。つまり、macOSですでにこのソフトウェアが提供されているため、別のバージョンを並行してインストールすると様々な問題が発生する可能性があるため、/opt/homebrewにシンボリックリンクされませんでした。

PATHの先頭にrubyを配置する必要がある場合は、以下を実行してください:
  echo 'export PATH="/opt/homebrew/opt/ruby/bin:$PATH"' >> ~/.zshrc

コンパイラでrubyを使用するには、以下を設定する必要がある場合があります:
  export LDFLAGS="-L/opt/homebrew/opt/ruby/lib"
  export CPPFLAGS="-I/opt/homebrew/opt/ruby/include"
==> yt-dlp
zsh補完機能は以下にインストールされました:
  /opt/homebrew/share/zsh/site-functions
==> redis
アップグレード後にredisを再起動するには:
  brew services restart redis
または、バックグラウンドサービスを必要としない場合は、以下を実行してください:
  /opt/homebrew/opt/redis/bin/redis-server /opt/homebrew/etc/redis.conf
==> perl
デフォルトでは、brewedではないcpanモジュールはCellarにインストールされます。モジュールを更新後も保持したい場合は、`local::lib`を使用することをお勧めします。

以下の手順で設定できます:
  PERL_MM_OPT="INSTALL_BASE=$HOME/perl5" cpan local::lib
シェルプロファイル（例: ~/.profileまたは~/.zshrc）に以下を追加してください。
  eval "$(perl -I$HOME/perl5/lib/perl5 -Mlocal::lib=$HOME/perl5)"
==> awscli
"examples"ディレクトリは以下にインストールされました:
  /opt/homebrew/share/awscli/examples

zsh補完機能と関数は以下にインストールされました:
  /opt/homebrew/share/zsh/site-functions
==> php
ApacheでPHPを有効にするには、httpd.confに以下を追加してApacheを再起動してください:
    LoadModule php_module /opt/homebrew/opt/php/lib/httpd/modules/libphp.so

    <FilesMatch \.php$>
        SetHandler application/x-httpd-php
    </FilesMatch>

最後に、DirectoryIndexにindex.phpが含まれていることを確認してください。
    DirectoryIndex index.php index.html

php.iniとphp-fpm.iniファイルは以下にあります:
    /opt/homebrew/etc/php/8.4/

phpを今すぐ起動し、ログイン時に再起動するには:
  brew services start php
または、バックグラウンドサービスを必要としない場合は、以下を実行してください:
  /opt/homebrew/opt/php/sbin/php-fpm --nodaemonize
==> nginx
ドキュルートは:/opt/homebrew/var/wwwです。

デフォルトポートは/opt/homebrew/etc/nginx/nginx.confで8080に設定されているため、sudoなしでnginxを実行できます。

nginxは/opt/homebrew/etc/nginx/servers/内のすべてのファイルをロードします。

アップグレード後にnginxを再起動するには:
  brew services restart nginx
または、バックグラウンドサービスを必要としない場合は、以下を実行してください:
  /opt/homebrew/opt/nginx/bin/nginx -g daemon\ off\;
==> git-lfs
インストールを完了するには、gitの設定を更新してください:

  # グローバルgit設定の更新
  $ git lfs install

  # システムgit設定の更新
  $ git lfs install --system

zsh補完機能は以下にインストールされました:
  /opt/homebrew/share/zsh/site-functions
==> wireshark
このフォーミュラはデフォルトでコマンドラインユーティリティのみインストールします。

Homebrew Caskを使用してWireshark.appをインストールします:
  brew install --cask wireshark

使用可能なキャプチャインターフェースのリストが空の場合（macOSのデフォルトの動作）、ChmodBPFをインストールします:
  brew install --cask wireshark-chmodbpf
==> doctl
zsh補完機能は以下にインストールされました:
  /opt/homebrew/share/zsh/site-functions
==> azure-cli
zsh補完機能は以下にインストールされました:
  /opt/homebrew/share/zsh/site-functions

