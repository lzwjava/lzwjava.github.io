---
audio: false
lang: en
layout: post
title: Paragraph-Based on Tanslation to Reduce Token Usage
translated: false
generated: false
---

My jekyll blog used markdown to write paragraphs. After writing it in English, I will AI tools like DeepSeek or Mistral to translate to other eight languages. Thought they are already cheap, but they are still space to improve. 

Sometimes, I just edit a word or a paragraph, then whole text of a post will be transalted to other 8 languages. For this case, the token usage is high. If I just use one paragraph to transalte again. Then the token usage will be short, espcailly for those long post.

But I still want to use markdown to record my ideas. Use database and maintain in database to update post is not convenient. Use yaml or JSON is probably too. 

The importance to know is that what's difference between edit and after edit. If we use paragraph-based, that's mean I use new line "\n" character to split text. 

