---
audio: false
generated: false
lang: hant
layout: post
title: 人工智能工具技巧
translated: true
---

* 將範例程式碼複製到 Cursor，並使用註解提供背景資訊。

* 在香港地區，可以使用 DeepSeek 或 Mistral 服務，但不可以使用 ChatGPT、Claude 或 Gemini。

* 一個地區的 API 政策大致與其應用程式政策相同。

* 使用 Cursor 取代 Visual Studio Code。

* 仍有一些情況需要使用 Visual Studio Code，例如在 git merge 編輯器情境下，我仍使用 `git config --global core.editor "code --wait"`。

* 從 Deepseek V3 發布開始，我們不需要訂閱任何 AI 工具。

* 使用 Gemini 或 Grok 生成節日慶祝圖片，例如使用提示語 "生成包含文字名稱的快樂農曆蛇年圖片"。

* 即使提供原始文字給 AI 模型來生成表格，輸出的幾個地方可能與輸入不同。例如，使用 Cursor 中的 Deepseek V3 模型生成 pip list 表格時，可能會包含像 `1.极狐0` 的版本。這裡的 `极狐` 指的是中國的 GitLab 平台。

* 使用 Deepseek 或 Mistral API 翻譯標題時，例如 `You are a professional translator. You are translating a markdown file for a Jekyll blog post from English to Chinese. {text}`，可能會導致錯誤的翻譯。除了你提供的文字，輸出通常會包含過多的翻譯。

* 雖然 Cursor 中的 AI 模型有時會提供部分正確的文字，我們可以接受，因為我們可以添加後續指示，使 AI 模型重新生成正確的部分。

* 如果不太可能有幫助，避免向大型語言模型提供過多的背景資訊。例如，生成對話對話行時，避免提供 100 個主題點。大型語言模型已經包含大量的數據。

* 在翻譯或生成對話歌詞等任務中提供充足的背景資訊時，避免使用鏈式思維功能，因為這可能會變慢並導致冗長或無幫助的回應。

* 測試聊天機器人是否能遵循使用者指示的一種方法是，要求它用英文解釋某事，然後繼續用中文輸入，觀察聊天機器人是否保持英文輸出。

* 而不是向 LLM 提供背景資訊，根據大量的文字或程式碼數據集微調模型，然後使用微調後的模型。

* 每週輪流使用 AI 聊天機器人，這樣你就能了解它們的差異。如果你想學習更多，不要只使用一個 AI 工具或最好的工具。

* 打開 Grok、Gemini、ChatGPT、DeepSeek、Mistral、Perplexity 和 Claude，開啟許多標籤頁，閱讀它們的答案，然後提問。我們可以比較答案或根據我們的興趣繼續提問。

* 如果任務是總結 YouTube 影片，首先使用 Gemini；如果涉及 X 的資訊，首先使用 Grok。

* 書籍變得越來越不實用。使用 AI 聊天機器人閱讀書籍；它們可以提供你第 1 章或第 2 章、書籍的摘要或介紹。

* [AI-Powered Git Commit Messages](./gitmessageai-en)

* [Conversation Audio Generation](./conversation-style-en)

* [Google Cloud Transcription](./speech-to-text-en)

* [Trying llama.cpp](./llama-cpp-en)

* [A Case Using Search in ChatGPT](./ai-search-en)

* [Deepseek, Mistral and Anthropic](./dma-en)