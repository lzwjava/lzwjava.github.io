---
audio: false
generated: false
image: false
lang: zh
layout: post
title: 如何学习Transformer中的KQV机制
translated: true
---

阅读了[K, Q, V机制在Transformer中的应用](https://lzwjava.github.io/notes/2025-06-02-attention-kqv-en)后，我大致理解了K、Q和V的工作原理。

Q代表Query，K代表Key，V代表Value。对于一个句子来说，Query是一个存储需要向其他token询问的token值的矩阵。Key代表token的描述，Value代表token的实际含义矩阵。

它们有特定的形状，因此需要了解它们的维度和细节。

我大约在2025年6月初理解了这一点。我最初是在2023年底左右才开始了解它的。当时，我读了像[The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)这样的文章，但当时并没有理解太多。

大约两年后，我发现现在更容易理解了。在这两年中，我主要专注于后端工作和准备副学士学位考试，没有读或学习太多关于机器学习的内容。不过，我偶尔在开车或做其他事情时会思考这些概念。

这让我想到时间的作用。我们可能在第一次看到某些东西时学到很多，即使当时并没有理解太多。但无论如何，它都为我们的思考提供了一个起点。

随着时间的推移，我发现对于知识和发现来说，第一次思考或理解某些事情是很难的。但后来，学习和了解起来似乎更容易了。

其中一个原因是，在AI时代，学习更容易，因为你可以深入任何细节或方面来解决你的疑问。还有更多相关的AI视频可供参考。更重要的一点是，你会看到有那么多人在学习并基于这些内容进行项目开发，比如[llama.cpp](https://github.com/ggml-org/llama.cpp)。

Georgi Gerganov的故事很有启发。作为一个从2021年开始学习机器学习的新手，他对AI社区产生了强大的影响。

这种事情会一再发生。因此，对于强化学习和最新的AI知识，尽管我目前还无法投入太多时间，但我认为我可以抽出一些时间快速学习并尽量多地思考它们。大脑会做好它的工作。