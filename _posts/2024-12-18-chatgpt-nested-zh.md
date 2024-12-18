---
layout: post
title: "ChatGPT 无法完美处理嵌套代码块的输出"
audio: true
---

当我要求 ChatGPT 精炼以下内容时：

```markdown
---
layout: post
title: "Google Text-to-Speech API 入门"
---
```

它生成了如下内容：

```yaml
---
layout: post
title: "Google Text-to-Speech API 入门"
---
```

然而，在渲染时，由于代码块嵌套不正确，导致页面渲染失败。

### 问题说明

问题出在 Jekyll 的 Markdown 解析器对嵌套代码块的处理方式。当你试图在一个代码块中嵌套另一个代码块时，解析器无法正确处理，导致渲染问题。

### 解决方案

要解决这个问题，确保嵌套的代码块正确缩进，或者使用其他方法（如 HTML 实体或围栏代码块）来防止 Jekyll 错误解析。

以下是如何正确处理嵌套代码块的示例：

```markdown
---
layout: post
title: "Jekyll 中的嵌套代码块"
---

这是一个在代码块中嵌套另一个代码块的示例：

```yaml
# 外层代码块
---
layout: post
title: "Google Text-to-Speech API 入门"
---

# 内层代码块（使用三重反引号进行围栏）
```
```

通过确保正确的缩进或使用围栏代码块，嵌套代码块将能够正确渲染，没有任何问题。

