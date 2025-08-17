---
audio: false
generated: false
image: false
lang: hant
layout: post
title: 從神經網絡到GPT
translated: true
---

### YouTube 影片

Andrej Karpathy - 從零開始、用程式碼逐步解釋如何構建 GPT

Umar Jamil - Attention is all you need（Transformer）— 模型解釋（包含數學）、推論與訓練

StatQuest with Josh Starmer - Transformer 神經網路，ChatGPT 的基礎，清楚解說！！！

Pascal Poupart - CS480/680 第 19 講：注意力機制與 Transformer 網路

The A.I. Hacker - Michael Phi - Transformer 神經網路圖解指南：逐步解釋

---

### 我的學習方式

當我讀完《神經網路與深度學習》一書的大半內容後，我開始重現書中識別手寫數字的神經網路範例。我建立了一個 GitHub 存儲庫：[https://github.com/lzwjava/neural-networks-and-zhiwei-learning](https://github.com/lzwjava/neural-networks-and-zhiwei-learning)。

這才是真正的難點所在。如果能夠不抄襲任何程式碼，從零開始寫出來，就代表真的理解透徹了。

我的重現程式碼仍缺少 `update_mini_batch` 和反向傳播（backprop）的實作。不過，透過仔細觀察載入資料、前向傳播（feed forwarding）和評估階段的變數，我對向量、維度、矩陣和物件的形狀（shape）有了更深入的理解。

接著，我開始學習 GPT 和 Transformer 的實作。透過詞嵌入（word embedding）和位置編碼（positional encoding），文字被轉換成數字。本質上，這與用簡單的神經網路識別手寫數字並無不同。

Andrej Karpathy 的課程《從零開始構建 GPT》非常優秀，他解釋得很清晰。

第一個原因是它真的是從零開始。我們首先看到如何生成文字，剛開始時文字模糊而隨機。第二個原因是 Andrej 能以非常直觀的方式講解。他花了數個月完成 nanoGPT 專案。

我突然有了新的想法來評判課程的品質：講者是否真的能寫出這些程式碼？我為什麼不理解？講者遺漏了哪些主題？除了那些優雅的圖表和動畫之外，它們有什麼缺陷和不足？

回到機器學習本身。如 Andrej 所提，像是 Dropout、殘差連接（residual connection）、自注意力（Self-Attention）、多頭注意力（Multi-Head Attention）、遮罩注意力（Masked Attention）等。

透過觀看更多上述影片，我逐漸有些理解。

透過正弦和餘弦函數的位置編碼，我們獲得了一些權重。透過詞嵌入，我們將文字轉換為數字。

$$
    PE_{(pos,2i)} = \sin\left(\frac{pos}{10000^{2i/d_{model}}}\right) \\
    PE_{(pos,2i+1)} = \cos\left(\frac{pos}{10000^{2i/d_{model}}}\right)
$$

> The pizza came out of the oven and it tasted good.

在這句話中，演算法如何知道「it」指的是 pizza 還是 oven？我們如何計算句子中每個詞的相似度？

我們想要一組權重。如果使用 Transformer 網路進行翻譯任務，每次輸入一句話，它就能輸出另一種語言的對應句子。

關於點積（dot product），我們在此使用點積的原因之一是它會考慮向量中的每個數字。如果我們使用平方點積呢？先對數字平方，再進行點積。如果進行某種反向點積呢？

關於遮罩（masked），我們將矩陣中一半的數值設為負無窮大，然後用 softmax 將值範圍限制在 0 到 1 之間。如果我們將左下角的數值設為負無窮大呢？

---

### 計劃

繼續閱讀程式碼、論文和觀看影片。享受過程，跟隨我的好奇心。

[https://github.com/karpathy/nanoGPT](https://github.com/karpathy/nanoGPT)

[https://github.com/jadore801120/attention-is-all-you-need-pytorch](https://github.com/jadore801120/attention-is-all-you-need-pytorch)