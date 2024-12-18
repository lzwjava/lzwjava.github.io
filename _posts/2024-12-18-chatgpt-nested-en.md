---
layout: post
title: "ChatGPT Couldn’t Provide the Perfect Output for Nested Code Blocks"
audio: true
---

When I asked ChatGPT to refine the following post:

```markdown
---
layout: post
title: "Getting Started with Google Text-to-Speech API"
---
```

It generated something like this:

```yaml
---
layout: post
title: "Getting Started with Google Text-to-Speech API"
---
```

However, when rendered, the post failed due to improper nesting of the code blocks.

### Issue Explanation

The issue arises because Jekyll’s Markdown parser treats nested code blocks differently. When you try to nest code blocks inside each other, the parser doesn’t always handle it correctly, causing rendering issues.

### Solution

To fix this, ensure that nested code blocks are properly indented or use alternative methods (such as HTML entities or fenced code blocks) to prevent misinterpretation by Jekyll.

Here’s an example of how to handle nested code blocks properly:

```markdown
---
layout: post
title: "Nested Code Blocks in Jekyll"
---

Here’s an example of a code block inside another code block:

```yaml
# Outer code block
---
layout: post
title: "Getting Started with Google Text-to-Speech API"
---

# Inner code block (fenced with triple backticks)
```
```

By ensuring correct indentation or using fenced code blocks, nested code blocks will render properly without issues.
