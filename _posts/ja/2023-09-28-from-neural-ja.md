---
audio: false
generated: false
image: false
lang: ja
layout: post
title: ニューラルネットワークからGPTへ
translated: true
---

### YouTube動画

Andrej Karpathy - GPTをゼロから、コードで、詳しく構築しよう。

Umar Jamil - Attention is all you need (Transformer) - モデルの説明（数学を含む）、推論とトレーニング

Josh StarmerのStatQuest - Transformerニューラルネットワーク、ChatGPTの基盤、わかりやすく解説!!!

Pascal Poupart - CS480/680 講義19: アテンションとトランスフォーマーネットワーク

A.I. ハッカー - Michael Phi - イラスト付きTransformerニューラルネットワークガイド: ステップバイステップの解説

### 私の学習方法

「Neural Networks and Deep Learning」という本を半分ほど読んだ後、手書き数字を認識するニューラルネットワークの例を再現し始めました。GitHubにリポジトリを作成しました、https://github.com/lzwjava/neural-networks-and-zhiwei-learning。

それが本当に難しい部分です。もし誰かがコードを一切コピーせずにゼロから書けるなら、その人は非常によく理解していると言えるでしょう。

私のレプリケートコードにはまだ`update_mini_batch`と`backprop`の実装が欠けています。しかし、データのロード、フィードフォワード、評価の段階での変数を注意深く観察することで、ベクトル、次元、行列、オブジェクトの形状についてより深く理解することができました。

そして、GPTとトランスフォーマーの実装について学び始めました。単語埋め込みと位置エンコーディングによって、テキストは数字に変換されます。本質的には、手書き数字を認識する単純なニューラルネットワークと何ら変わりはありません。

Andrej Karpathyの講義「Let's build GPT」は非常に優れています。彼は物事をうまく説明してくれます。

最初の理由は、それが本当にゼロから始まることです。まず、テキストを生成する方法を見ます。それは少しぼやけていてランダムです。2番目の理由は、Andrejが非常に直感的に物事を説明できることです。Andrejは数か月間、プロジェクトnanoGPTを行いました。

私は講義の質を判断するための新しいアイデアを思いつきました。講師は本当にこれらのコードを書けるのか？なぜ私には理解できないのか、そして講師はどのトピックを見落としているのか？これらの洗練された図やアニメーションの他に、彼らの欠点や欠陥は何か？

機械学習の話題に戻りましょう。Andrejが言及しているように、ドロップアウト、残差接続、Self-Attention、Multi-Head Attention、Masked Attentionなどがあります。

上記の動画をさらに見ていくことで、少しずつ理解が深まりました。

sin関数とcos関数を用いた位置エンコーディングにより、いくつかの重みが得られます。単語埋め込みによって、単語を数値に変換します。

$$
    PE_{(pos,2i)} = \sin\left(\frac{pos}{10000^{2i/d_{model}}}\right) \\
    PE_{(pos,2i+1)} = \cos\left(\frac{pos}{10000^{2i/d_{model}}}\right)
$$

> ピザがオーブンから出てきて、美味しかった。

この文において、アルゴリズムは「it」が「pizza」を指すのか「oven」を指すのかをどのように判断するのでしょうか？また、文中のすべての単語に対して類似度をどのように計算するのでしょうか？

私たちは一連の重みを求めています。もしTransformerネットワークを使って翻訳のタスクを行う場合、毎回文章を入力すると、それに対応する別の言語の文章を出力することができます。

ここでドット積を使用する理由の一つは、ドット積がベクトル内のすべての数値を考慮するからです。もし、二乗ドット積を使用したらどうなるでしょうか？まず、数値の二乗を計算し、それからドット積を行います。逆ドット積を行ったらどうなるでしょうか？

マスクされた部分について、行列の半分の数値を負の無限大に変更します。そして、softmaxを使用して値を0から1の範囲に変換します。では、左下の数値を負の無限大に変更するのはどうでしょうか？

### 計画

コードや論文を読み続け、動画も視聴します。好奇心に従って楽しむだけです。

https://github.com/karpathy/nanoGPT

https://github.com/jadore801120/attention-is-all-you-need-pytorch