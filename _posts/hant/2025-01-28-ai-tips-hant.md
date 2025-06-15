---
audio: false
generated: false
lang: hant
layout: post
title: 人工智能工具小貼士
translated: true
---

* 將示例代碼複製到Cursor中，並使用註釋提供上下文。

* 在香港地區，可以使用DeepSeek或Mistral服務，但不允許使用ChatGPT、Claude或Gemini。

* 一個地區的API政策大致與其應用政策相同。

* 使用Cursor而非Visual Studio Code。

* 仍有情況下需要使用Visual Studio Code，例如在git合併編輯器場景中，我仍會使用`git config --global core.editor "code --wait"`。

* 從Deepseek V3發布之日起，我們無需訂閱任何AI工具。

* 使用Gemini或Grok生成節日慶祝圖片，提示如「生成一張包含文字名稱的快樂農曆蛇年新年圖片」。

* 在某些情況下，即使向AI模型提供原始文本來創建表格，輸出中的少數地方也可能與輸入不同。例如，在Cursor中使用Deepseek V3模型生成pip列表表格時，可能會包含像`1.極狐0`這樣的版本號。此處的`極狐`指的是中文GitLab平台。

* 當使用Deepseek或Mistral API翻譯標題，並給出如`你是一名專業翻譯員。你正在將一篇Jekyll博客文章的markdown文件從英文翻譯成中文。{text}`的提示時，可能會導致錯誤的翻譯。除了你提供的文本外，輸出往往包含過多的翻譯內容。

* 雖然有時Cursor中的AI模型給出的文本部分正確，但我們可以接受，因為我們可以添加後續指令，讓AI模型重新生成正確的部分。

* 如果不太可能有幫助，避免向大型語言模型提供過多上下文。例如，在生成對話台詞時，避免提供關於某個主題的100個要點。大型語言模型已經包含大量數據。

* 在為翻譯或生成對話歌詞等任務提供充足上下文時，避免使用思維鏈功能，因為這可能會導致速度變慢並產生冗長或無用的回應。

* 測試聊天機器人是否能遵循用戶指令的一種方法是，讓它用英文解釋某件事，然後繼續用中文輸入，觀察聊天機器人是否保持其英文輸出。

* 與其向LLM提供上下文，不如基於大量文本或代碼數據集對模型進行微調，然後使用微調後的模型。

* 輪流使用AI聊天機器人一周，這樣你可以了解它們的差異。如果你想學到更多，不要只堅持使用一個AI工具或最好的工具。

* 同時打開Grok、Gemini、ChatGPT、Deepseek、Mistral、Perplexity和Claude，打開多個標籤頁閱讀它們的回答，然後提問，這很有趣。我們可以比較答案或根據興趣繼續提問。

* 如果任務是總結YouTube視頻，首先使用Gemini；如果涉及X的信息，首先使用Grok。

* 書籍的用處越來越小。使用AI聊天機器人來閱讀一本書；它們可以為你提供第一章或第二章、摘要或書籍介紹。

* 與其使用深度思考或思維鏈（CoT）來解決難題，有時可以簡化問題，讓標準模型來解決。

* 與AI聊天時，語言很重要，尤其是在涉及特定地區或領域時。使用相關的本地知識可以幫助你找到更準確的信息——例如，關於如何獲取身份證或註冊車輛的信息。

* [AI驅動的Git提交消息](./gitmessageai-en)

* [對話音頻生成](./conversation-style-en)

* [Google Cloud語音轉文字](./speech-to-text-en)

* [嘗試llama.cpp](./llama-cpp-en)

* [在ChatGPT中使用搜索的案例](./ai-search-en)

* [Deepseek、Mistral和Anthropic](./dma-en)