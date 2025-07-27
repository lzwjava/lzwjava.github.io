---
audio: false
generated: false
image: true
lang: hant
layout: post
title: AI 程式設計工具的挑剔工程師觀點
translated: true
---

最近，我成功運行了 Claude Code，所以想分享一下我的工具選擇之旅。途中我也收集了一些 [AI 工具技巧](ai-tips-en.md)。

我採用 Claude Code 的時間相對較晚。

[Claude Code](https://www.anthropic.com/news/claude-3-5-sonnet) 大約在 2025 年底推出。

直到最近我才成功嘗試。其中一個原因是它需要使用 Anthropic API，但該 API 不支援中國的 Visa 信用卡。

另一個原因是 [Claude Code Router](https://github.com/musistudio/claude-code-router) 變得可用，這才使我最近的嘗試成功。

我經常聽到對它的讚譽。我於 2025 年 7 月嘗試過 Gemini CLI，但由於多次嘗試修復代碼失敗而放棄。

我也嘗試過 Aider，另一款軟體代理。我使用 Cursor 大約六個月後便停止，因為許多基於 VSCode 的外掛功能失靈。此外，我不想給 Cursor 太多功勞，因為它是基於 VSCode 建立的。由於 VSCode 的 Copilot 外掛近期改進，且效能不遜於其他工具，我更常使用它。

然而，VSCode 是基於 Electron 建立的開源技術。很難歸功於正確的團隊或個人。考慮到許多大公司和初創公司從開源專案獲利，我必須專注於我的預算和最適合我的工具。我不必太擔心歸功於誰。我更喜歡使用實惠且有效的工具。

我簡短地嘗試過 Cline，但沒有採用。

我使用 VSCode 的 Copilot 外掛，並透過 OpenRouter 使用自訂模型 Grok 3 beta，效果不錯。

我不認為 Claude Code 會改變我的習慣，但既然我能成功運行它，並且有耐心再嘗試幾次，我會看看未來幾週的感受。

我是一個挑剔的用戶，擁有十年的軟體工程經驗。我希望工具在實際使用中表現良好。我不買品牌的帳——我只關心日常實用性。

使用 Claude Code 修正這篇文章的文法後，我發現它在某些情境下運作良好。雖然我欣賞 AI 在文法協助方面的表現（我甚至寫了一個 Python 腳本來調用 LLM API 來實現這個目的），但我注意到一個令人沮喪的模式——即使我要求最小的修正，工具仍會提出大量文法建議供我審查。這種手動驗證過程敗壞了自動化的目的。作為妥協，我現在讓 AI 處理整篇文章，但這種方法限制了我的學習機會，因為我看不到具體的修正。

最令我印象深刻的是 Claude Code 顯示變更的方式——顯示類似 git diff 的前後比較，這使得審查修改更加容易。

一天後，我使用 Claude 修正了一些代碼。不過，我仍然使用 Copilot 外掛和 Grok 3 beta 模型，因為它簡單且易於使用。

{: .centered }
![](assets/images/claude/claude-code.jpg){: .responsive }
*來源：自拍截圖*{: .caption }

{: .centered }
![](assets/images/claude/claude-fix.jpg){: .responsive }
*來源：自拍截圖*{: .caption }

{: .centered }
![](assets/images/claude/vscode-fix.jpg){: .responsive }
*來源：自拍截圖*{: .caption }