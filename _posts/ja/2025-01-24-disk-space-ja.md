---
audio: false
generated: false
image: false
lang: ja
layout: post
title: ディスクスペースのクリーンアップ
translated: true
---

## 設定

パス Settings -> General -> Storage -> ストレージの設定を使用して、ディスクスペースがどのように使用されているかを確認し、不要なファイルを削除します。

## 大きなファイルの検索

`du` を使用して大きなファイルを見つけます。例えば、`du -hL -d 1 | sort -h` コマンドを使用します。

特定のディレクトリで、`find . -type f -print0 | xargs -0 du -h | sort -rh | head -n 20` を使用します。

## アプリケーションの削除

アプリケーションディレクトリからアプリケーションを削除します。

## ダウンロード

インターネットから簡単にダウンロードできるダウンロードパッケージの dmg ファイルを削除します。

## ポータブルディスク

ポータブルディスクを購入し、そこにいくつかのファイルを移動します。

## iPhone

iPhoneから写真をMacにインポートし、インポート後に削除します。