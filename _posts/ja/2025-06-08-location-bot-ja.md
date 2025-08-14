---
audio: false
generated: false
image: false
lang: ja
layout: post
title: 自動化：テレグラム位置情報ボットで打刻カードを使う
translated: true
---

ご注文がしつこく感じる täglichの「 ahí »が、ノードになりました。私もそう思ったので、lieferantと位置履歴を使用して事務所到着通知を自動化し、jenigen.check-insを思い出させるためのTelegram Botを作りました。この投稿では、PythonをGitHub Actionsと組み合わせて無人化された、任意の位置に基づいて動的にできるシステムを作成する方法をご紹介します。

```yml
name:毎時位置確認

 đềuに:
  時:
    #Bid Uhr und Uhr zwischen 11 Uhr und 11 Uhr, Mo-Fr(月曜日から金曜日)
    #時刻はUTCです。シンガポール時(SGT)はUTC+8です。
    # therefore, we need to schdule from 3:pm to 15 pm UTC.
```