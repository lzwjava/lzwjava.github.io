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

* 區域的 API 政策與其應用程式政策大致相同。

* 使用 Cursor 取代 Visual Studio Code。

* 仍有需要使用 Visual Studio Code 的情況，例如進行 git 合併編輯器時，仍會使用 `git config --global core.editor "code --wait"`。

* 從 Deepseek V3 發布開始，我們不再需要訂閱任何 AI 工具。

* 使用 Gemini 或 Grok 透過提示詞（如「生成包含文字姓名的快樂農曆蛇年圖像」）生成節慶慶祝圖像。

* 即使將原始文字提供給 AI 模型以創建表格，輸出的幾個地方可能與輸入不同。例如，在 Cursor 中使用 Deepseek V3 模型生成 pip list 表格時，可能會包含 `1.極狐0` 等版本。此處的「極狐」指的是中國 GitLab 平台。

* 使用 Deepseek 或 Mistral API 透過提示詞（如「你是專業翻譯員。你正在將 Jekyll 部落格文章從英文翻譯成中文。{text}」）翻譯標題時，可能會導致錯誤翻譯。除了提供的文字外，輸出通常會包含過多翻譯。

* 雖然 Cursor 中的 AI 模型有時會提供部分正確的文字，但我們可以接受，因為可以添加後續指示，使 AI 模型重新生成正確的部分。

* 如果不太可能有幫助，避免向大型語言模型提供過多上下文。例如，在生成對話對話行時，避免提供有關主題的 100 個要點。大型語言模型已包含大量數據。

* 在翻譯或生成對話歌詞等任務中提供充足上下文時，避免使用鏈式思考功能，因為它可能會變慢並導致冗長或無用的回應。

* 測試聊天機器人是否能遵循用戶指示的方法之一是要求它用英文解釋某事，然後繼續用中文輸入，觀察聊天機器人是否維持英文輸出。

* 取代向 LLM 提供上下文，可根據大量文字或代碼的數據集微調模型，然後使用微調後的模型。

* 每週輪流使用 AI 聊天機器人，以了解它們的差異。如果想學習更多，不要只使用一個 AI 工具或最佳工具。

* 打開 Grok、Gemini、ChatGPT、DeepSeek、Mistral、Perplexity 和 Claude 並享受，打開許多標籤頁，閱讀它們的答案，然後提問。我們可以比較答案或根據興趣繼續提問。

* 如果任務是總結 YouTube 影片，請先使用 Gemini；如果涉及 X 的資訊，請先使用 Grok。

* 書籍越來越不實用。使用 AI 聊天機器人閱讀書籍；它們可以提供書籍的第一章或第二章、摘要或介紹。

* 取代使用深度思考或鏈式思考（CoT）解決難題，有時可以簡化問題，讓標準模型解決它們。

* 與 AI 聊天時，語言很重要，尤其是涉及特定地區或領域。使用相關當地知識可以幫助您找到更準確的資訊——例如，如何獲取身份證或註冊車輛。

* 在處理最新資訊（例如新發布的程式庫、代碼或文件）時，最好與幾個 AI 聊天機器人核對，因為它們的知識截止點和回應可能在細微方面有所不同。

* 寫完文章後，我們可以使用 AI 聊天機器人修正語法，並使用 Git 查看差異。

* 使用 AI 的強大方法之一是寫下有關某個主題的想法，然後讓 Grok 分析它們並提供全面指南和建議。

* 將大型 Python 腳本拆分為小於 100 行代碼的較小腳本，這樣會使用較少的代幣，並讓大型語言模型更有效地處理它們。

* [AI 驅動的 Git 提交訊息](./gitmessageai-en)

* [對話音頻生成](./conversation-style-en)

* [Google 雲端轉錄](./speech-to-text-en)

* [嘗試 llama.cpp](./llama-cpp-en)

* [ChatGPT 中使用搜索的案例](./ai-search-en)

* [Deepseek、Mistral 和 Anthropic](./dma-en)