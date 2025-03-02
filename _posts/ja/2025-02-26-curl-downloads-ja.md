---
audio: false
generated: true
lang: ja
layout: post
title: curlのダウンロードのトラブルシューティング
translated: true
---

Eclipse ZIP ファイルを `curl -O` を使用して eclipse.org からダウンロードしようとすると、HTML ファイルがダウンロードされ、"301 Moved Permanently" エラーが表示されることがあります。これは、使用している URL が他の場所にリダイレクトされているためです。`curl` はそのリダイレクトを自動的に追跡して実際のファイルにアクセスしません。以下にその解決方法を示します。

### 問題の理解

- **301 Moved Permanently**: この HTTP ステータスコードは、リソース（ZIP ファイル）が新しい URL に永久に移動したことを意味します。サーバーはダウンロードリンクをミラーサイトや更新された場所にリダイレクトするためにリダイレクトを使用することが多いです。
- **`curl -O` の動作**: `-O` オプションは、`curl` にリモートファイル名でダウンロードしたコンテンツを保存するように指示します。しかし、リダイレクトを明示的に処理しない場合、`curl` は中間リダイレクト応答（通常は HTML ページ）のコンテンツを保存し、ZIP ファイルにリダイレクトすることができません。

### 解決方法

`curl` がリダイレクトを追跡して Eclipse ZIP ファイルをダウンロードするようにするには、`-L` オプションを `-O` と一緒に使用します。`-L` フラグは、`curl` にリダイレクトを追跡し、最終的な先に到達するように指示します。

#### コマンド

```bash
curl -L -O <URL>
```

- **`-L`**: リダイレクト（301 リダイレクトを含む）を追跡して新しい場所に移動します。
- **`-O`**: 最終的な URL からのオリジナルの名前でファイルを保存します。
- **`<URL>`**: これを特定の Eclipse ダウンロード URL に置き換えます。例えば、`https://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/2023-03/R/eclipse-java-2023-03-R-win32-x86_64.zip`。

### 手順

1. **正しい URL を見つける**:
   - Eclipse ウェブサイト（例：`https://www.eclipse.org/downloads/`）にアクセスします。
   - 望むパッケージ（例：Eclipse IDE for Java Developers）を選択します。
   - ダウンロードリンクまたはボタンを右クリックして URL をコピーします。または、ブラウザの開発者ツール（F12、ネットワークタブ）を使用して、ダウンロードをクリックしたときの正確な URL をキャプチャします。

2. **コマンドを実行**:
   - ターミナルを開きます。
   - コピーした URL を使用して `-L` と `-O` オプションを持つ `curl` コマンドを実行します：
     ```bash
     curl -L -O https://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/2023-03/R/eclipse-java-2023-03-R-win32-x86_64.zip
     ```
   - これにより、ZIP ファイル（例：`eclipse-java-2023-03-R-win32-x86_64.zip`）が現在のディレクトリにダウンロードされます。

### トラブルシューティング

問題が解決しない場合は、以下の追加の手順を試してください：

- **リダイレクトの確認（詳細な出力）**:
  - リクエストとリダイレクトの詳細情報を表示するために `-v` オプションを使用します：
    ```bash
    curl -v -L -O <URL>
    ```
  - 301 応答の `Location` ヘッダーを確認して、リダイレクト先が ZIP ファイルではなく HTML ページを指しているかどうかを確認します。URL が ZIP ファイルへの直接ダウンロードリンクでない場合、URL が正しいかどうかを確認してください。

- **URL の確認**:
  - Eclipse は `download.php` スクリプトを使用して、ミラーサイトにリダイレクトすることが多いです。URL が ZIP ファイルへの直接リンクであるか、ファイルに解決されるリダイレクトリンクであることを確認してください。例えば、直接のミラーリンクは以下のようになります：
    ```bash
    curl -L -O https://mirror.its.dal.ca/eclipse/technology/epp/downloads/release/2023-03/R/eclipse-java-2023-03-R-win32-x86_64.zip
    ```

- **User-Agent ヘッダーの設定**:
  - サーバーはクライアントに基づいて異なる動作をすることがあります。サーバーが `curl` を検出して HTML を返す場合、ブラウザを模倣するために User-Agent を追加します：
    ```bash
    curl -L -O -A "Mozilla/5.0" <URL>
    ```

### なぜこれが機能するのか

Eclipse ウェブサイトは、ダウンロードリクエストをミラーサイトまたは更新された URL にリダイレクトすることがあります。`-L` を使用しないと、`curl -O` はリダイレクト応答（HTML ページ）を保存し、実際の ZIP ファイルにリダイレクトすることができません。`-L` を追加することで、`curl` は 301 リダイレクトを追跡して実際の ZIP ファイルに解決し、問題を解決します。

これらの手順に従うことで、`curl` を使用して eclipse.org から Eclipse ZIP ファイルを正常にダウンロードできます。