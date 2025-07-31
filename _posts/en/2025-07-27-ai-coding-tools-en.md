---
audio: false
generated: false
image: true
lang: en
layout: post
title: A Picky Engineer's Take on AI Coding Tools
translated: false
---

Recently, I successfully ran Claude Code, so I want to share my tool selection journey. I have also collected some [AI Tool Tips](ai-tips-en.md) along the way.

I was quite late to adopt Claude Code.

[Claude Code](https://www.anthropic.com/news/claude-3-5-sonnet) was released around the end of Feb 2025.

I didn't succeed in trying it until recently. One reason is that it requires the Anthropic API, which doesn't support Chinese Visa cards.

Another reason is that [Claude Code Router](https://github.com/musistudio/claude-code-router) became available, which made my recent attempt successful.

I keep hearing praise for it. I tried the Gemini CLI in July 2025 but abandoned it after several failed attempts to get it to fix my code.

I also tried Aider, another software agent. I stopped using Cursor after about six months because many of its VSCode-based plugins malfunctioned. Additionally, I don't want to give Cursor much credit since it is built on top of VSCode. As the Copilot plugin in VSCode has recently improved and doesn't lag far behind, I prefer to use it more often.

However, VSCode is built on Electron, an open-source technology. It's challenging to attribute credit to the right team or individual. Considering that many large companies and startups profit from open-source projects, I must focus on my budget and what suits me best. I shouldn't worry too much about giving credit. I prefer using affordable and effective tools.

I briefly experimented with Cline but didn't adopt it.

I use the Copilot plugin in VSCode with a customized model, Grok 3 beta through OpenRouter, which works well.

I don't think Claude Code will change my habits, but since I can successfully run it and have the patience to try it a few more times, I'll see how I feel in the coming weeks.

I am a picky user with 10 years of software engineering experience. I hope tools can be great in actual use. I don't buy into the brand—I just care about daily usefulness.

After using Claude Code to fix this post's grammar, I've found it works well in certain scenarios. While I appreciate AI for grammar assistance (I even wrote a Python script to call LLM APIs for this purpose), I've noticed a frustrating pattern - even when I request minimal fixes, the tools keep surfacing numerous grammar suggestions for review. This manual verification process defeats the purpose of automation. As a compromise, I now let AI handle entire essays, though this approach limits my learning opportunities since I don't see the specific corrections being made.

What impressed me most was how Claude Code displays changes - showing before-and-after comparisons similar to git diffs, which makes reviewing edits much easier.

After a day, I used Claude to fix some code as well. However, I continue to use the Copilot plugin with the Grok 3 beta model, as it is simple and easy for me.

After using Claude Code for several days, I have to say it's very impressive. I really like how it fixes my code.

{: .centered }
![](assets/images/claude/claude-code.jpg){: .responsive }
*Source: Self-screenshot*{: .caption }


{: .centered }
![](assets/images/claude/claude-fix.jpg){: .responsive }
*Source: Self-screenshot*{: .caption }

{: .centered }
![](assets/images/claude/vscode-fix.jpg){: .responsive }
*Source: Self-screenshot*{: .caption }