---
audio: false
generated: false
image: false
lang: ja
layout: post
title: 大規模言語モデルの最大コンテキスト長
translated: true
---

最近、[AI-Powered Git Commit Messages](./gitmessageai-en)で説明されているように、DeepSeek APIを使用してコミットメッセージを生成しました。

コミットに多くの変更ファイルが含まれている場合、DeepSeek APIは入力が65,535トークン（2^16 - 1）のコンテキスト長制限を超えていると報告しました。

以下は、他のいくつかのモデルのコンテキストウィンドウサイズです：

*   **Claude 3 Family:** 2024年3月に導入され、これらのモデルは200,000トークンから始まるコンテキストウィンドウを持っています。
*   **GPT-4:** 標準版は8,192トークンをサポートし、拡張版（GPT-4-32k）は32,768トークンをサポートします。
*   **MetaのLLaMA 2:** 標準版は4,096トークンをサポートしますが、微調整されたバージョンは最大16,384トークンを処理できます。
*   **Mistral 7B:** 最大8,000トークンをサポートします。