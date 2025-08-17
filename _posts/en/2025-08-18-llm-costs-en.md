---
audio: false
generated: false
image: false
lang: en
layout: post
title: Optimizing LLM API Costs
translated: false
---

## Table of Contents
1. [Optimizing LLM API Costs](#optimizing-llm-api-costs)
2. [API Usage of Deepseek and Mistral](#api-usage-of-deepseek-and-mistral)
   2.1 [DeepSeek](#deepseek)
   2.2 [Mistral](#mistral)
   2.3 [Grok](#grok)


## Optimizing LLM API Costs

{: .centered }
![](assets/images/tokens/tokens1.png){: .responsive }
*Source: penrouter.ai*{: .caption }

{: .centered }
![](assets/images/tokens/tokens2.png){: .responsive }
*Source: openrouter.ai*{: .caption }

While optimizing token usage, it's advisable to start with more cost-effective models. Should issues arise, consider upgrading to more advanced models. Mistral, Gemini Flash, and DeepSeek are typically economical, whereas Claude Sonnet is generally more expensive. It's crucial to understand how Claude Code uses the routers shown below.

In my recent experience, I incurred significant costs due to neglecting this principle. I was trying to reach my maximum usage to determine the cost, which isn't a rational approach; it's a simple calculation. For instance, do I truly need Sonnet 4? Not necessarily. Although I perceive it as a more advanced model from Anthropic and it ranks highly on OpenRouter, I'm unclear about the differences between Sonnet 4 and Sonnet 3.5.

I learned something valuable from a recent [interview](https://www.vanta.com/resources/replit-future-of-code) with Replit founder, Amjad Masad: for many tasks, highly advanced models aren't necessary. Ideally, if we can avoid using the LLM API altogether, that's perfect. Certain NLP libraries are effective for simpler tasks; for example, [HanLP](https://github.com/hankcs/HanLP) excels at handling Chinese language tasks.

Furthermore, we can develop custom or specialized agents to handle tasks efficiently from the outset. Claude Code might not always be the best or most cost-effective solution for every task. 

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

---

## Api Usage Of Deepseek And Mistral

### DeepSeek

In one month, 15 million tokens cost me approximately 23.5 CNY.

This was my usage in one day:

| Type              | Tokens    |
|-------------------|-----------|
| Input (Cache Hit)  | 946,816   |
| Input (Cache Miss) | 2,753,752 |
| Output            | 3,100,977 |

The calculation is as follows:

0.94 * 0.1 + 2.75 * 1 + 3.10 * 2 = 11.83

So, depending on the task, the token usage largely depends on the input (cache miss) and output.

This result aligns with the expected cost.

[DeepSeek API Pricing](https://api-docs.deepseek.com/quick_start/pricing/)

{: .centered }
![](assets/images/deepseek/d.jpg)
*Source: Self-Screenshot*{: .caption }

### Mistral


The pricing for Mistral models is as follows:

| Model                 | Input (USD per million tokens) |  Output (USD per million tokens) |
|-----------------------|------------------------------|---------------------------------|
| `mistral-large-2411`  | 2                            | 6                               |
| `mistral-small-latest`| 0.2                          | 0.6                             |

In one day, my Mistral account usage was as follows (Model: `mistral-large-2411`):

| Type   | Tokens  | Cost (USD) |
|--------|---------|------------|
| Total  | 772,284 | 3.44       |
| Output | 474,855 | 2.85       |
| Input  | 297,429 | 0.59       |


For the `mistral-small-2409` model, the total usage was 1,022,407 tokens.

Assuming 1/3 of these were input tokens and 2/3 were output tokens:

There were 340,802 input tokens and 681,605 output tokens.

Therefore, the total cost is calculated as 340,802 * 0.2 / 1,000,000 + 681,605 * 0.6 / 1,000,000 = 0.07 + 0.41 = 0.48 USD.

The Mistral console reports a total usage cost of 0.43 USD, which approximately matches our calculation.

### Grok

| Model         | Input (USD per million tokens) | Output (USD per million tokens) |
|---------------|------------------------------|---------------------------------|
| `grok-2-latest` | 2                            | 10                              |