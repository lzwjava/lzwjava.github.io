---
audio: false
generated: false
lang: hant
layout: post
title: AI 程式設計工具的挑剔工程師觀點
translated: true
---

近期，我成功運行了 Claude Code，因此想分享我的工具選擇之旅。過程中我也收集了一些 [AI 工具技巧](ai-tips-en)。

我採用 Claude Code 的時間相對較晚。

[Claude Code](https://www.anthropic.com/news/claude-3-5-sonnet) 大約在 2025 年 2 月底推出。

直到最近我才成功嘗試。其中一個原因是它需要使用 Anthropic API，但該 API 不支援中國大陸的信用卡。

另一個原因是 [Claude Code Router](https://github.com/musistudio/claude-code-router) 變得可用，這才使我最近的嘗試成功。

我一直聽到對它的讚譽。我於 2025 年 7 月嘗試過 Gemini CLI，但由於多次嘗試修復代碼失敗而放棄。

我也嘗試過 Aider，另一款軟體代理。我使用 Cursor 大約六個月後停止，因為許多基於 VSCode 的外掛功能失效。我曾短暫嘗試過 Cline，但未採用。

我使用 VSCode 的 Copilot 外掛，並透過 OpenRouter 使用自訂模型 Grok 3 beta，效果不錯。

我不認為 Claude Code 會改變我的習慣，但既然我能成功運行它，並且有耐心再嘗試幾次，我會看看未來幾週的感受。

我是一位挑剔的用戶，擁有 10 年的軟體工程經驗。我希望工具在實際使用中表現出色。我不買賬品牌——我只關心日常實用性。

使用 Claude Code 修正本文的文法後，我發現它在某些情境下運作良好。雖然我欣賞 AI 提供的文法協助（我甚至寫了一個 Python 腳本來呼叫 LLM API 以此為目的），但我注意到一個令人沮喪的模式——即使我要求最小的修正，工具仍會提出大量文法建議供我檢查。這種手動驗證過程敗壞了自動化的目的。作為妥協，我現在讓 AI 處理整篇文章，但這種方法限制了我的學習機會，因為我看不到具體的修正內容。

最令我印象深刻的是 Claude Code 顯示變更的方式——它會顯示類似 git diff 的前後比較，這使得檢查修改更加容易。

{: .centered }
![](assets/images/claude/claude-code.jpg){: .responsive }
*來源：自拍截圖*{: .caption }

{: .centered }
![](assets/images/claude/claude-fix.jpg){: .responsive }
*來源：自拍截圖*{: .caption }