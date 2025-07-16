---
audio: false
generated: false
lang: en
layout: post
title: How I Learned the KQV Mechanism in Transformers
translated: false
---

After reading [K, Q, V Mechanism in Transformers](https://lzwjava.github.io/notes/2025-06-02-attention-kqv-en), I somehow understood how K, Q, and V work.

Q stands for Query, K stands for Key, and V stands for Value. For a sentence, the Query is a matrix that stores the value of a token that it needs to ask other tokens about. The Key stands for the description of the tokens, and the Value stands for the actual meaning matrix of the tokens.

They have specific shapes, so one needs to know their dimensions and details.

I understood this around early June 2025. I first learned about it around the end of 2023. At that time, I read articles like [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/), but I didn't understand much.

After about two years, I found it easier to understand now. During these two years, I focused on backend work and preparing for my associate degree exams, and I didn't read or learn much about machine learning. However, I did mull over these concepts from time to time when I was driving or doing other things.

This reminds me of the effect of time. We may learn a lot of things at first sight, even if we don't comprehend much. But somehow, it triggers a starting point for our thinking.

Over time, I found that for knowledge and discovery, it is hard to think about or understand things the first time. But later, it seems easier to learn and know.

One reason is that in the AI era, it is easier to learn because you can delve into any detail or aspect to resolve your doubts. There are also more related AI videos available. More importantly, you see that so many people are learning and building projects on top of that, like [llama.cpp](https://github.com/ggml-org/llama.cpp).

The story of Georgi Gerganov is inspiring. As a new machine learning learner starting around 2021, he made a powerful impact in the AI community.

This kind of thing will happen again and again. So, for reinforcement learning and the latest AI knowledge, even though I am still not able to dedicate much time to them, I think I can find some time to quickly learn and try to think about them a lot. The brain will do its work.