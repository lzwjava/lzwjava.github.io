---
audio: false
generated: false
lang: hant
layout: post
title: AI 工具技巧
translated: true
---

* 將範例代碼複製到 Cursor，並使用註釋提供上下文。

* 在香港地區，可接受使用 DeepSeek 或 Mistral 服務，但不接受使用 ChatGPT、Claude 或 Gemini。

* 地區的 API 政策大致與其應用程式政策相同。

* 使用 Cursor 取代 Visual Studio Code。

* 仍有需要使用 Visual Studio Code 的情況，例如進行 git 合併編輯器場景時，我仍使用 `git config --global core.editor "code --wait"`。

* 從 Deepseek V3 發布開始，我們不再需要訂閱任何 AI 工具。

* 使用 Gemini 或 Grok 根據提示生成節日慶祝圖片，例如「生成包含文字姓名的快樂農曆蛇年圖片」。

* 在某些情況下，即使將原始文字提供給 AI 模型以創建表格，輸出的幾個地方可能與輸入不同。例如，在 Cursor 中使用 Deepseek V3 模型生成 pip list 表格時，可能會包含類似 `1.極狐0` 的版本。此處的「極狐」指的是中國 GitLab 平台。

* 使用 Deepseek 或 Mistral API 根據提示翻譯標題，例如「你是專業翻譯員。你正在將 Jekyll 部落格文章從英文翻譯成中文。{text}」，可能會導致錯誤的翻譯。除了你提供的文字外，輸出通常會包含過多的翻譯。

* 雖然 Cursor 中的 AI 模型有時會提供部分正確的文字，但我們可以接受，因為我們可以添加後續指示，使 AI 模型重新生成正確的部分。

* 如果不太可能有幫助，避免向大型語言模型提供過多的上下文。例如，在生成對話對話行時，避免提供 100 個主題的內容。大型語言模型已經包含大量數據。

* 在翻譯或生成對話歌詞等任務中提供充足的上下文時，避免使用鏈式思考功能，因為它可能會變慢並導致冗長或無用的回應。

* 測試聊天機器人是否能遵循用戶指示的一種方法是，要求它用英文解釋某事，然後繼續用中文輸入，觀察聊天機器人是否保持英文輸出。

* 而不是向 LLM 提供上下文，可以基於大量文字或代碼的數據集微調模型，然後使用微調後的模型。

* 每週輪流使用 AI 聊天機器人，這樣你就能了解它們的差異。如果你想學習更多，不要只使用一個 AI 工具或最好的工具。

* 打開 Grok、Gemini、ChatGPT、DeepSeek、Mistral、Perplexity 和 Claude 並享受，打開許多標籤頁與它們互動，閱讀它們的回答，然後提問。我們可以比較答案或根據我們的興趣繼續提問。

* 如果任務是總結 YouTube 影片，優先使用 Gemini；如果涉及 X 的資訊，優先使用 Grok。

* 書籍越來越不實用。使用 AI 聊天機器人閱讀書籍；它們可以為你提供第一章或第二章、書籍摘要或書籍介紹。

* 而不是使用深度思考或鏈式思考 (CoT) 來解決難題，你可以簡化問題，讓標準模型解決它們。

* 與 AI 聊天時，語言很重要，尤其是涉及特定地區或領域時。使用相關的當地知識可以幫助你找到更準確的資訊——例如，如何獲得身份證或登記車輛。

* 在處理最新資訊——例如新發布的庫、代碼或文件時，最好與幾個 AI 聊天機器人核對，因為它們的知識截止點和回應可能在細微方面有所不同。

* 寫完文章後，我們可以使用 AI 聊天機器人修正語法，並使用 Git 查看差異。

* [AI 驅動的 Git 提交訊息](./gitmessageai-en)

* [對話音頻生成](./conversation-style-en)

* [Google 雲端轉錄](./speech-to-text-en)

* [嘗試 llama.cpp](./llama-cpp-en)

* [在 ChatGPT 中使用搜索的案例](./ai-search-en)

* [Deepseek、Mistral 和 Anthropic](./dma-en)