---
audio: false
generated: false
image: false
lang: ja
layout: post
title: 情報プロパティリストの解読
translated: true
---

macOSやiOSの開発をしていれば、`Info.plist`というファイルに出会ったことがあるでしょう。このXMLベースのファイルは、Appleアプリケーションやプラグインの重要な部分であり、システムにそのアイデンティティ、機能、振る舞いを伝えるパスポートのような役割を果たします。今日は、前回の投稿で紹介したXcodeプラグイン「Reveal-In-GitHub」の`Info.plist`を探索します。各行を細かく分析するのではなく、その目的と機能を定義する核心的な概念とパターンに焦点を当てます。

---

#### `Info.plist`ファイルとは？

`Info.plist`（「Information Property List」の略）は、アプリ、プラグイン、またはバンドルに関するメタデータを保持する構造化されたファイルです。XML（Appleが定義した特定のスキーマ）で記述され、キーと値のペアを使用して、アプリの名前、バージョン、互換性などの基本情報を説明します。「Reveal-In-GitHub」の場合、このファイルはそれをXcodeプラグインとして識別し、IDEとのスムーズな統合を保証します。

`.pbxproj`ファイルとは異なり、これは「何かをどのように構築するか」についてのものではなく、「その何かが何かであるか」についてのものです。これはアイデンティティと意図の宣言です。

---

#### ファイルの主要な概念

1. **バンドルの基本**
   以下のキーは、プラグインをmacOSバンドルとして定義します：
   - **`CFBundleExecutable`**：`$(EXECUTABLE_NAME)`は、ビルドプロセス中に定義されるコンパイルされたバイナリの名前のプレースホルダーです。
   - **`CFBundleIdentifier`**：`$(PRODUCT_BUNDLE_IDENTIFIER)`は`com.lzwjava.Reveal-In-GitHub`に解決され、このプラグインを他のものと区別するための一意の逆DNSスタイルのIDです。
   - **`CFBundlePackageType`**：`BNDL`はこれをバンドルとしてマークし、macOS上のプラグインやライブラリの一般的な形式です。
   - **`CFBundleName`**：`$(PRODUCT_NAME)`は「Reveal-In-GitHub」になり、人間に親しみやすい名前です。

2. **バージョニングと所有権**
   - **`CFBundleShortVersionString`**："1.0"はユーザー向けのバージョンです。
   - **`CFBundleVersion`**："1"は内部ビルド番号です。
   - **`NSHumanReadableCopyright`**："Copyright © 2015年 lzwjava. All rights reserved."は、クリエイター`lzwjava`をクレジットし、プラグインを2015年に日付付けします。
   - **`CFBundleSignature`**："????"はプレースホルダー（通常は4文字のコード）ですが、プラグインにはあまり重要ではありません。

3. **ローカライゼーション**
   - **`CFBundleDevelopmentRegion`**："en"は英語をデフォルト言語として設定し、リソース（あれば）のローカライズに影響を与えます。

4. **Xcodeプラグインの互換性**
   ここの特徴的な機能は、**`DVTPlugInCompatibilityUUIDs`**で、特定のXcodeバージョン（例：Xcode 6、7など）に対応する長いUUIDの配列です。これにより、プラグインは互換性のあるIDEでのみ読み込まれます。このリストは異常に広く、「Reveal-In-GitHub」が多くのXcodeリリースで動作するように設計されていることを示唆しています。これは、慎重な前方および後方互換性の証拠です。

5. **プラグイン固有の設定**
   - **`NSPrincipalClass`**：空（`<string></string>`）で、プラグインがエントリーポイントを動的に定義するか、Xcodeの規約に依存していることを示唆しています。
   - **`XC4Compatible`と`XC5Compatible`**：両方とも`<true/>`で、Xcode 4および5との互換性を確認しています。
   - **`XCGCReady`**：`<true/>`は、ガベージコレクションの準備ができていることを示し、これは古いmacOSメモリ管理機能（2015年にはARCに置き換えられました）です。
   - **`XCPluginHasUI`**：`<false/>`は、Xcodeに組み込まれているものを超えたカスタムUIがないことを示唆していますが、これは`.pbxproj`の`.xib`ファイルと矛盾しているように見えます。UIが最小限か異なる方法で処理されている可能性があります。

---

#### 注意すべきパターン

1. **柔軟性のためのプレースホルダー**
   `$(EXECUTABLE_NAME)`や`$(PRODUCT_BUNDLE_IDENTIFIER)`のようなキーは、ビルドシステム（`.pbxproj`で定義）に紐付けられた変数を使用します。これにより、`Info.plist`はデバッグとリリースなどの異なる構成間で再利用可能になります。

2. **ミニマリストデザイン**
   ファイルはシンプルで、基本的なものに焦点を当てています。ファンサイアイコン、エンタイトルメント、アプリ固有の設定などはありません。これは、既存のアプリ（Xcode）を拡張するプラグインに典型的です。

3. **互換性に焦点を当てる**
   長い`DVTPlugInCompatibilityUUIDs`リストと`XC4Compatible`のようなフラグは、長く使えるプラグインを示しています。このパターンは、ユーザーが安定性のために古いXcodeバージョンに留まる可能性がある開発ツールに一般的です。

4. **メタデータよりも振る舞い**
   コードファイルとは異なり、`Info.plist`は何もしません。その役割は受動的で、XcodeとmacOSがランタイムで解釈する情報を提供することです。

---

#### これは「Reveal-In-GitHub」について何を教えてくれるのでしょうか？

この`Info.plist`は、2015年にソロ開発者（`lzwjava`）によって作成された軽量で集中したXcodeプラグイン「Reveal-In-GitHub」を描いています。その広範な互換性は、広く使用できるように設計されていることを示唆していますが、UIフラグの欠如（プロジェクト内の`.xib`があるにもかかわらず）は、メニュー項目やコンテキストアクションのような微妙な統合を示唆しています。名前と`.pbxproj`のコンテキストから、これはおそらくGitHubのワークフローを簡素化するもので、Xcodeファイルをオンラインリポジトリにリンクするなどの機能を提供しているでしょう。

---

#### なぜこれが重要なのか

`Info.plist`は、アプリのシステムとのハンドシェイクです。開発者にとって、これを理解することは、コードを触らずに互換性、バージョニング、または振る舞いを調整できることを意味します。「Reveal-In-GitHub」にとって、これはXcodeにスムーズにフィットするための鍵です。次回、プラグインをデバッグしたり、自分のものを作成したりする際には、このファイルがスタート地点となります。小さくても強力です。