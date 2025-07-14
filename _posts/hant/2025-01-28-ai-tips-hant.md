---
audio: false
generated: false
lang: hant
layout: post
title: AI 工具技巧
translated: true
---

* 將範例代碼複製到 Cursor，並使用註解提供上下文。

* 在香港地區，可使用 DeepSeek 或 Mistral 服務，但不可使用 ChatGPT、Claude 或 Gemini。

* 地區的 API 政策與其應用程式政策大致相同。

* 使用 Cursor 取代 Visual Studio Code。

* 仍有需要使用 Visual Studio Code 的情況，例如進行 git 合併編輯時，仍會使用 `git config --global core.editor "code --wait"`。

* 自 Deepseek V3 發布日起，無需訂閱任何 AI 工具。

* 使用 Gemini 或 Grok 透過提示詞生成節慶慶祝圖片，例如「生成包含文字姓名的快樂農曆蛇年圖片」。

* 即使將原始文字提供給 AI 模型以生成表格，輸出內容仍可能與輸入內容有部分差異。例如，在 Cursor 中使用 Deepseek V3 模型生成 pip 列表時，可能會出現類似 `1.極狐0` 的版本號，其中「極狐」指的是中國 GitLab 平台。

* 使用 Deepseek 或 Mistral API 翻譯標題時，若使用提示詞如「您是專業翻譯員。您正在將 Jekyll 部落格文章從英文翻譯成中文。{text}」，可能會導致翻譯錯誤。除了您提供的文字外，輸出內容常常包含過多翻譯。

* 雖然 Cursor 中的 AI 模型有時會提供部分正確的文字，但我們可以接受，因為可以添加後續指示，讓 AI 模型重新生成正確的部分。

* 若不太可能有幫助，則避免向大型語言模型提供過多上下文。例如，生成對話對話行時，避免提供 100 個相關主題。大型語言模型已包含大量數據。

* 在翻譯或生成對話歌詞等任務中提供充足上下文時，避免使用鏈式思考功能，因為這可能會讓回應變慢或冗長。

* 測試聊天機器人是否能遵循用戶指示的方法之一，是要求它用英文解釋某事，然後繼續用中文輸入，觀察聊天機器人是否維持英文輸出。

* 取代向 LLM 提供上下文，可根據大量文字或代碼的數據集微調模型，然後使用微調後的模型。

* 每週輪流使用 AI 聊天機器人，以了解它們的差異。若想學習更多，則不要只使用一種 AI 工具或最佳工具。

* 開啟 Grok、Gemini、ChatGPT、DeepSeek、Mistral、Perplexity 和 Claude 非常有趣，同時開啟多個標籤頁，閱讀它們的回答，然後提問。我們可以比較答案或根據興趣繼續提問。

* 若任務是總結 YouTube 影片，則優先使用 Gemini；若涉及 X 的資訊，則優先使用 Grok。

* 書籍越來越不實用。使用 AI 聊天機器人閱讀書籍；它們可以提供書籍的第一章或第二章、摘要或介紹。

* 解決難題時，不必使用深度思考或鏈式思考 (CoT)，有時可以簡化問題，讓標準模型解決。

* 與 AI 聊天時，語言很重要，尤其是涉及特定地區或領域。使用相關本地知識可幫助您找到更準確的資訊，例如如何申請身份證或登記車輛。

* 使用最新資訊（例如新發布的程式庫、代碼或文件）時，最好與多個 AI 聊天機器人核對，因為它們的知識截止點和回應可能存在細微差異。

* 寫完文章後，我們可以使用 AI 聊天機器人修正文法，並使用 Git 查看差異。

* 使用 AI 的強大方式之一是寫下您對某個主題的想法，然後讓 Grok 分析並提供全面指南和建議。

* [AI 驅動的 Git 提交訊息](./gitmessageai-en)

* [對話音頻生成](./conversation-style-en)

* [Google 雲端轉錄](./speech-to-text-en)

* [嘗試 llama.cpp](./llama-cpp-en)

* [在 ChatGPT 中使用搜索的案例](./ai-search-en)

* [Deepseek、Mistral 和 Anthropic](./dma-en)