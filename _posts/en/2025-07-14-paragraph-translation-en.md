---
audio: false
generated: false
image: false
lang: en
layout: post
title: Optimizing Translation Costs with Paragraph-Based Markdown
translated: false
---

My Jekyll blog uses Markdown to write paragraphs. After writing in English, I use AI tools like DeepSeek or Mistral to translate into eight other languages. Although they are already inexpensive, there is still room for improvement.

Sometimes, I just edit a word or a paragraph, and then the entire text of a post will be translated into the other eight languages. In this case, the token usage is high. If I only translate one paragraph again, the token usage will be lower, especially for long posts.

However, I still want to use Markdown to record my ideas. Using a database to maintain and update posts is not convenient. Using YAML or JSON might be too cumbersome as well.

The key is to identify the differences between the text before and after editing. If we use a paragraph-based approach, that means using the newline character "\n" to split the text.

I need to know which paragraphs have changed and which have not after editing. We need to know the one-to-one paragraph mappings between the text before and after editing.

We use a paragraph-based approach because we want to update the translations made by AI models. If we use sentences, it might not be as accurate.

For Markdown, it might be more important to use Markdown parsing to synchronize translations based on Markdown elements.

But if there are no code blocks or special Markdown syntax, we can use a paragraph-based approach.

For a simple paragraph-based approach, we have two arrays of paragraphs and need to know how they match.

When comparing any paragraph in these two arrays, there are two possible results: they are either the same or different. If they are different, there are several cases: both are newly added, the left one is newly added, or the right one is newly added.

I just want to save costs, so I want to reduce token usage. I don't need anything else. I just need to translate every paragraph, cache the result, and the next time, for every paragraph, I will first look for the translation result. If it doesn't exist, then I need to translate it again.

For Markdown, it is a bit more complicated. I don't want to translate code blocks. So, we can use a Markdown parsing library first to treat code blocks and normal text differently.