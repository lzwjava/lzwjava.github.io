---
audio: false
lang: en
layout: post
title: Optimizing Token Usage: Strategies for Cost-Effective LLM Interactions
translated: false
generated: false
image: false
---

{: .centered }
![](assets/images/tokens/tokens1.png){: .responsive }
*Source: Self-screenshot*{: .caption }

To optimize token usage, begin with more cost-effective models. If issues arise, consider upgrading to more advanced models. Mistral, Gemini Flash, and DeepSeek are generally economical, while Claude Sonnet is typically more expensive. It's important to understand how Claude Code utilizes the routers shown below. 


```json
{
  "Router": {
    "default": "openrouter,google/gemini-2.5-flash",
    "background": "openrouter,google/gemini-2.5-flash",
    "think": "openrouter,google/gemini-2.5-flash",
    "longContext": "openrouter,google/gemini-2.5-flash",
    "longContextThreshold": 60000,
    "webSearch": "openrouter,google/gemini-2.5-flash"
  }
} 
```

