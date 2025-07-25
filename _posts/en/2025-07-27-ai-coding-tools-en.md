---
audio: false
generated: false
image: true
lang: en
layout: post
title: A Picky Engineer's Take on AI Coding Tools
translated: false
---

Recently, I successfully ran Claude Code, so I want to share my tool selection journey. I have also collected some [AI tool tips](ai-tips-en) along the way.

I was quite late to adopt Claude Code.

[Claude Code](https://www.anthropic.com/news/claude-3-5-sonnet) was released around the end of Feb 2025.

I didn't succeed in trying it until recently. One reason is that it requires the Anthropic API, which doesn't support Chinese Visa cards.

Another reason is that [Claude Code Router](https://github.com/musistudio/claude-code-router) became available, which made my recent attempt successful.

I keep hearing praise for it. I tried the Gemini CLI in July 2025 but abandoned it after several failed attempts to get it to fix my code.

I also tried Aider, another software agent. I stopped using Cursor after about six months because many of its VSCode-based plugins malfunctioned. I briefly experimented with Cline but didn't adopt it.

I use the Copilot plugin in VSCode with a customized model, Grok 3 beta through OpenRouter, which works well.

I don't think Claude Code will change my habits, but since I can successfully run it and have the patience to try it a few more times, I'll see how I feel in the coming weeks.

I am a picky user with 10 years of software engineering experience. I hope tools can be great in actual use. I don't buy into the brand—I just care about daily usefulness.

After using Claude Code to fix this post's grammar, I've found it works well in certain scenarios. While I appreciate AI for grammar assistance (I even wrote a Python script to call LLM APIs for this purpose), I've noticed a frustrating pattern - even when I request minimal fixes, the tools keep surfacing numerous grammar suggestions for review. This manual verification process defeats the purpose of automation. As a compromise, I now let AI handle entire essays, though this approach limits my learning opportunities since I don't see the specific corrections being made.

What impressed me most was how Claude Code displays changes - showing before-and-after comparisons similar to git diffs, which makes reviewing edits much easier.

{: .centered }
![](assets/images/claude/claude-code.jpg){: .responsive }
*Source: Self-screenshot*{: .caption }


{: .centered }
![](assets/images/claude/claude-fix.jpg){: .responsive }
*Source: Self-screenshot*{: .caption }