---
title: Fix YAML Then Hugo in Jekyll
lang: en
layout: post
audio: false
translated: false
generated: true
image: false
---

You’ve got two separate issues:

1. bad YAML front-matter
2. Hugo shortcodes / Go templates inside Jekyll (Liquid) files

Fix them in this order.

---

## 1) Fix the YAML “did not find expected key … at line 2”

This almost always means the **front-matter** block at the very top is malformed.

Checklist (apply to each of the 3 files mentioned):

* The very first line must be exactly `---` and the opening/closing fences must be symmetric:

```yaml
---
title: "Company Valuation Comparison"
date: 2025-06-25
layout: post
tags: [finance, notes]
# any other keys...
---
```

* **No tabs**. YAML only accepts spaces.
* Every `key:` must have a space after the colon.
* Quote any value containing `:`, `#`, `{}`, `[]`, `&`, `*`, `?`, `%`, `<`, `>` or starting with `{` or `[`.
  Example: `title: "A:B — why it matters"` (not `title: A:B — why it matters`)
* For multi-line text, use a block scalar:

```yaml
description: |
  Line one with a colon: yes
  Line two with # signs is fine
```

* Don’t leave a dangling key with no value:

```yaml
bad_key:        # ❌
good_key: ""    # ✅
```

Quick way to spot the problem line:

```bash
nl -ba notes/2025-06-25-company-valuation-comparison-en.md | sed -n '1,30p'
```

If line 2 is something like `title: A: B`, change to `title: "A: B"`.

To validate each file locally:

```bash
ruby -ryaml -e 'puts YAML.load_file(ARGV[0]).inspect' notes/2025-06-25-company-valuation-comparison-en.md
```

If that prints a Ruby hash, the front-matter is valid.

### Common “line 2” culprits

* A BOM or blank line **before** `---`. Make sure the file begins with `---` at byte 0.
* `tags:` written as a string that looks like YAML syntax. Prefer arrays:

```yaml
tags: ["tech", "valuation"]  # or
tags:
  - tech
  - valuation
```

---

## 2) Fix the Liquid warnings (you have Hugo syntax in Jekyll)

These messages show Hugo/Go-template syntax inside your posts:

* `{{< math >}}` / `{{< /math >}}`
* `{{ .Get "content" | safeHTML }}`
* `{{ .Inner | safeHTML }}`
* Expressions with `..`, `.`, or `<` inside `{{ ... }}`

Jekyll uses **Liquid**, not Hugo. You have 3 options:

### Option A — Convert to proper Jekyll/MathJax (recommended)

1. In `_config.yml`, enable MathJax via kramdown:

```yaml
markdown: kramdown
kramdown:
  input: GFM
  math_engine: mathjax
```

2. In your layout (e.g., `_layouts/post.html`) include MathJax:

```html
<script id="MathJax-script" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
```

3. Replace Hugo math shortcodes with TeX delimiters:

* Inline math: `\( a^2 + b^2 = c^2 \)` or `$a^2+b^2=c^2$`
* Block math:

```markdown
$$
E = mc^2
$$
```

Delete `{{< math >}}` and `{{< /math >}}` entirely.

4. Replace Hugo shortcodes like:

```markdown
{{ .Get "content" | safeHTML }}
{{ .Inner | safeHTML }}
```

with plain Markdown/HTML or a Liquid include. For example, if you intended to inject some variable `content`:

```liquid
{% include my-snippet.html content=page.content %}
```

(You must create `_includes/my-snippet.html` accordingly.)
If you just want to show the text, paste the text directly or render it via `{{ page.some_value | markdownify }}`.

### Option B — Keep Hugo-looking code as **literal text** (escape Liquid)

If those `{{< ... >}}` are just examples you want to display, wrap them with Liquid raw tags:

```liquid
{% raw %}
{{< math >}}
{{< /math >}}
{{ .Get "content" | safeHTML }}
{% endraw %}
```

This tells Jekyll not to parse them.

### Option C — Write Liquid equivalents

* There is no Liquid operator for `..` (range) or `.Get`. If you were iterating over a range in Hugo, in Liquid you’d typically precompute a list or use a collection and `{% for %}` loops.
* Any expression like `{{< something >}}` must be rewritten as either `{% something %}` (a tag) or `{{ something }}` (a variable) using **Liquid**, not Hugo.

---

## Quick “find and fix” commands

List files containing Hugo shortcodes:

```bash
grep -R --line-number -E '\{\{<|\.Get|\.Inner|\|\s*safeHTML' notes/
```

Wrap all `{{<` / `>}}` blocks with `{% raw %}` / `{% endraw %}` if you just want to show them:

```bash
# Back up first!
git commit -am "backup before shortcode escaping"

# Example (manual is safer): open the file and surround the snippet with:
# {% raw %} ... {% endraw %}
```

Find Liquid tags with `<` or `/` inside (likely Hugo):

```bash
grep -R --line-number -E '\{\{[^}]*[<>/][^}]*\}\}' notes/
```

---

## Minimal working example (put this at the top of your problem posts)

```yaml
---
title: "Hugo → Jekyll: Math and Shortcodes"
date: 2025-08-06
layout: post
tags: [jekyll, migration, math]
description: "Notes on converting Hugo shortcodes to Jekyll/Liquid with MathJax."
---
```

Then, inside the body:

```markdown
Inline math: $e^{i\pi}+1=0$.

Block math:

$$
\int_{-\infty}^{\infty} e^{-x^2}\,dx=\sqrt{\pi}
$$

If you need to **show** a Hugo shortcode:

{% raw %}
{{< math >}} E=mc^2 {{< /math >}}
{% endraw %}
```

---

## If you still get YAML errors

* Run a strict check on all posts:

```bash
for f in notes/*.md; do
  echo "Checking $f"
  ruby -ryaml -e 'YAML.load_file(ARGV[0])' "$f" || echo "YAML BROKEN -> $f"
done
```

* If the error persists at “line 2 column 1”, open the file and look for:

  * Byte Order Mark (BOM) before `---` (remove it).
  * A `title:` or `categories:` value containing `:` without quotes.
  * An array or map that’s mis-indented.

---

If you paste the first \~20 lines of one of the failing files, I’ll pinpoint the exact character causing the YAML crash and give a one-line fix.