---
title: "LLMs Confirm My CFA Insights"
lang: en
layout: post
audio: false
translated: false
generated: true
---

https://weibo.com/6347862377/5183994120372979

---

Certainly! Here is the text separated into paragraphs:

In a previous Weibo post, I mentioned that I like using LLMs to handle complex things that I don't enjoy doing or reading. This includes many academic papers. Over a decade has passed since I created PySonar2 (a Python type inference and static analyzer) in 2009-2010.

Surprisingly, I found myself discussing control-flow analysis (CFA) with ChatGPT, which reminded me of a debate I had with a "CFA student" ten years ago (web link). It's quite interesting that something I knew over a decade ago has now been "confirmed" by ChatGPT.

Over a decade ago, when PySonar2 was first developed, it actually surpassed all academic research on CFA at the time, including the then-latest CFA2. For Python, a quasi-functional language with lambda closures, this was the first implementation of such type inference.

To me, this wasn't a big deal because I didn't particularly care about the Python language. Moreover, those academic papers were too abstruse, and I wasn't interested in reading them thoroughly, so I only skimmed through. I developed PySonar2 in a few months and let others use it freely without writing any papers. I was too modest.

Looking at all those papers on CFA, k-CFA, CFA2... piles of papers that couldn't solve practical problems. It's unbelievable that k-CFA had a basic issue like "call and return mismatch," something I never imagined would happen. PySonar never had such problems.

CFA2 introduced something called a "pushdown automaton," which essentially just restored the function call stack from its initial flawed design. PySonar2 always had a "pushdown automaton" because interpreting function calls naturally involves a stack. Aren't these papers just producing nonsense? Yes. Now you can confirm this with ChatGPT :)

I must thank ChatGPT for clearly stating the facts I observed, saving me from reading those obscure papers and still being uncertain. I feel that LLMs will greatly aid human progress.

Now, I'm sharing a segment of my conversation with ChatGPT about CFA, hoping it will be helpful to researchers in this field: https://chatgpt.com/share/6864e9a1-66c8-8002-b9f5-55e845fde7ae