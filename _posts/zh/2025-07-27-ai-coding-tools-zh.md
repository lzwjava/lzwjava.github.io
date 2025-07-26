---
audio: false
generated: false
image: true
lang: zh
layout: post
title: AI编程工具的挑剔工程师观点
translated: true
---

最近，我成功运行了Claude Code，所以想分享一下我的工具选择之旅。途中我也收集了一些[AI工具技巧](ai-tips-en)。

我采用Claude Code的时间比较晚。

[Claude Code](https://www.anthropic.com/news/claude-3-5-sonnet)大约在2025年2月底发布。

直到最近我才成功尝试。其中一个原因是它需要Anthropic API，而该API不支持中国信用卡。

另一个原因是[Claude Code Router](https://github.com/musistudio/claude-code-router)变得可用，这使得我最近的尝试成功。

我一直听到人们对它的赞扬。我于2025年7月尝试了Gemini CLI，但因多次尝试修复代码失败而放弃。

我也尝试了Aider，另一个软件代理。我大约使用了六个月后停止使用Cursor，因为许多基于VSCode的插件出现了故障。我简短地尝试了Cline，但没有采用。

我使用VSCode中的Copilot插件，并通过OpenRouter使用自定义模型Grok 3 beta，效果很好。

我认为Claude Code不会改变我的习惯，但既然我能成功运行它，并且有耐心再尝试几次，我会看看接下来几周的感受。

我是一个挑剔的用户，拥有10年的软件工程经验。我希望工具在实际使用中表现出色。我不买账品牌——我只关心日常实用性。

在使用Claude Code修复本文的语法后，我发现它在某些场景下表现良好。虽然我欣赏AI的语法帮助（我甚至写了一个Python脚本来调用LLM API用于此目的），但我注意到一个令人沮丧的模式——即使我只要求最小的修改，工具也会不断提出大量语法建议供审查。这种手动验证过程破坏了自动化的目的。作为妥协，我现在让AI处理整篇文章，但这种方法限制了我的学习机会，因为我看不到具体的修改。

最让我印象深刻的是Claude Code显示修改的方式——类似于git diff的前后对比，使得审查修改更加容易。

{: .centered }
![](assets/images/claude/claude-code.jpg){: .responsive }
*来源：自拍截图*{: .caption }

{: .centered }
![](assets/images/claude/claude-fix.jpg){: .responsive }
*来源：自拍截图*{: .caption }