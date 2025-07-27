---
audio: false
generated: false
image: true
lang: zh
layout: post
title: 人工智能编码工具的挑剔工程师观点
translated: true
---

最近，我成功运行了Claude Code，所以想分享一下我的工具选择之旅。途中我也收集了一些[AI工具技巧](ai-tips-en.md)。

我采用Claude Code的时间比较晚。

[Claude Code](https://www.anthropic.com/news/claude-3-5-sonnet)大约在2025年2月底发布。

直到最近我才成功尝试。其中一个原因是它需要Anthropic API，但不支持中国信用卡。

另一个原因是[Claude Code Router](https://github.com/musistudio/claude-code-router)可用，这让我最近的尝试成功了。

我一直听到它的赞誉。我试过Gemini CLI，但在2025年7月尝试后因多次无法修复代码而放弃。

我也尝试过Aider，另一个软件代理。我大约使用了六个月的Cursor后停止使用，因为它的许多基于VSCode的插件出现了故障。此外，我不想给Cursor太多功劳，因为它是基于VSCode构建的。由于VSCode的Copilot插件最近有所改进，并且不落后太多，我更喜欢使用它。

然而，VSCode是基于Electron构建的，这是一种开源技术。很难将功劳归于正确的团队或个人。考虑到许多大公司和初创公司都从开源项目中获利，我必须专注于我的预算和最适合我的工具。我不必太担心给予功劳。我更喜欢使用价格合理且有效的工具。

我简单尝试过Cline，但没有采用。

我使用VSCode中的Copilot插件，并通过OpenRouter使用了自定义模型Grok 3 beta，效果不错。

我认为Claude Code不会改变我的习惯，但既然我能成功运行它，并且有耐心再尝试几次，我会看看接下来几周的感受。

我是一个挑剔的用户，有10年的软件工程经验。我希望工具在实际使用中表现出色。我不关心品牌——我只关心日常实用性。

使用Claude Code修复这篇文章的语法后，我发现它在某些场景下表现良好。虽然我感谢AI的语法帮助（我甚至写了一个Python脚本来调用LLM API用于此目的），但我注意到一个令人沮丧的模式——即使我只要求最小的修复，工具也会不断提出许多语法建议供审查。这种手动验证过程破坏了自动化的目的。作为妥协，我现在让AI处理整篇文章，但这种方法限制了我的学习机会，因为我看不到具体的修正。

最让我印象深刻的是Claude Code显示修改的方式——显示类似git diff的前后比较，这使得查看编辑更加容易。

一天后，我用Claude修复了一些代码。不过，我仍然继续使用带有Grok 3 beta模型的Copilot插件，因为它简单易用。

{: .centered }
![](assets/images/claude/claude-code.jpg){: .responsive }
*来源：自拍截图*{: .caption }

{: .centered }
![](assets/images/claude/claude-fix.jpg){: .responsive }
*来源：自拍截图*{: .caption }

{: .centered }
![](assets/images/claude/vscode-fix.jpg){: .responsive }
*来源：自拍截图*{: .caption }