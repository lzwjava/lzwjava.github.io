---
audio: false
generated: false
image: false
lang: zh
layout: post
title: 从神经网络到GPT
translated: true
---

### YouTube 视频

Andrej Karpathy - 从零开始手写 GPT：代码逐步实现

Umar Jamil - Attention is all you need（Transformer） - 模型解释（包含数学原理）、推理与训练

StatQuest with Josh Starmer - Transformer 神经网络（ChatGPT 的基础）清晰解析！！！

Pascal Poupart - CS480/680 课程 19：注意力机制与 Transformer 网络

The A.I. Hacker - Michael Phi - Transformer 神经网络插图指南：逐步详解

### 我的学习方法

在读完《神经网络与深度学习》一书的一半内容后，我开始复现手写数字识别的神经网络示例。我创建了一个 GitHub 仓库：https://github.com/lzwjava/neural-networks-and-zhiwei-learning。

这才是真正的难点所在。如果能完全从零开始写出代码，不借鉴任何现成代码，就说明理解得非常透彻。

我的复现代码仍缺少 `update_mini_batch` 和反向传播的实现。不过，通过仔细观察数据加载、前向传播和评估阶段的变量，我对向量、维度、矩阵和数据形状有了更深入的理解。

之后，我开始学习 GPT 和 Transformer 的实现。通过词嵌入与位置编码，文本被转化为数字。本质上，这与简单的手写数字识别神经网络并无区别。

Andrej Karpathy 的讲座「Let's build GPT」非常优秀，他解释得很清晰。

第一个原因是，这确实是从零开始。一开始我们看到生成的文本模糊而随机。第二个原因是 Andrej 能将复杂的概念讲得非常直观。他在 nanoGPT 项目上花了数月时间。

我突然有了一个新的评判讲座质量的标准：作者是否真正能写出这些代码？我为什么不理解？作者遗漏了哪些细节？除了那些精美的图示和动画，它们有什么缺陷和不足？

回到机器学习本身。如 Andrej 所提到的，dropout、残差连接、自注意力、多头注意力、掩码注意力……

在观看了更多上述视频后，我渐渐有了些许理解。

通过正弦和余弦函数的位置编码，我们得到一些权重。通过词嵌入，我们将单词转换为数字。

$$
    PE_{(pos,2i)} = sin(pos/10000^{2i/d_{model}}) \\
    PE_{(pos,2i+1)} = cos(pos/10000^{2i/d_{model}})
$$

> The pizza came out of the oven and it tasted good.

在这个句子中，算法如何知道「it」指的是 pizza 还是 oven？如何计算句子中每个单词的相似度？

我们需要一组权重。如果用 Transformer 网络做翻译任务，每次输入一个句子，就能输出另一种语言的对应句子。

关于这里的点积。我们使用点积的一个原因是，点积会考虑向量中的每一个数。如果用平方点积呢？先对数字平方，再做点积。如果做某种反向点积呢？

关于这里的掩码，我们将矩阵的一半数字改为负无穷。然后用 softmax 使值范围在 0 到 1 之间。如果把左下角的数字改为负无穷呢？

### 计划

继续阅读代码、论文和观看视频。保持兴趣，跟随好奇心前行。

https://github.com/karpathy/nanoGPT

https://github.com/jadore801120/attention-is-all-you-need-pytorch