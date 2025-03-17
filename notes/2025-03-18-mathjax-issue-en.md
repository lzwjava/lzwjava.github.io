---
title: mathjax-issue
lang: en
layout: post
audio: false
translated: false
generated: true
---

It seems that your MathJax configuration is not working as expected. Let's identify and fix the issue based on your provided code.

### Your Current Configuration
You have the following MathJax setup:

```html
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ["\\(","\\)"] ],
      displayMath: [ ['$$','$$'], ["\[","\]"] ],
      processEscapes: true
    },
    "HTML-CSS": { linebreaks: { automatic: true } },
    "CommonHTML": {
      linebreaks: { automatic: true },
      scale: 85
    },
    TeX: { equationNumbers: { autoNumber: "AMS" } }
  });
</script>

<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
```

This configuration aims to:
- Render inline math between `\( ... \)` delimiters.
- Render display math between `$$ ... $$` or `\[ ... \]` delimiters.
- Enable automatic line breaking for long equations.
- Scale math output to 85% size using the CommonHTML output processor.
- Automatically number equations using the AMS style.

However, you’ve reported that it’s "not working," which could mean the math isn’t rendering, or specific features (like line breaking) aren’t functioning as expected.

### The Problem
The primary issue lies in the `displayMath` delimiters configuration:

```javascript
displayMath: [ ['$$','$$'], ["\[","\]"] ]
```

In JavaScript, the string `"["` is interpreted literally as `[`, because `\[` is not a special escape sequence—it’s just a backslash followed by a bracket. Similarly, `"\]"` becomes `]`. As a result, MathJax is configured to recognize `[ ... ]` as display math delimiters, **not** `\[ ... \]`. Since your math expressions (like the sample `\[ \text{Bit rate} = 2400 \, \text{baud} \times 3 \, \text{bits/symbol} = 7200 \, \text{bits per second (bps)} \]`) use `\[ ... \]`, MathJax won’t recognize them as display math with the current setup.

The inline math delimiters `["\\(","\\)"]` are correct, as `\\(` and `\\)` in a JavaScript string represent `\(` and `\)`—the standard LaTeX delimiters for inline math. However, the display math delimiters need adjustment.

### The Solution
To fix this, update the `displayMath` configuration so that MathJax correctly recognizes `\[ ... \]` as display math delimiters. In JavaScript, to represent the string `\[`, you need to write `"\\["`, because each backslash must be escaped. Similarly, `\]` becomes `"\\]"`. Here’s the corrected configuration:

```html
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ["\\(","\\)"] ],
      displayMath: [ ["$$","$$"], ["\\[","\\]"] ],
      processEscapes: true
    },
    "HTML-CSS": { linebreaks: { automatic: true } },
    "CommonHTML": {
      linebreaks: { automatic: true },
      scale: 85
    },
    TeX: { equationNumbers: { autoNumber: "AMS" } }
  });
</script>

<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
```

#### Key Change
- Changed `["\[","\]"]` to `["\\[","\\]"]` in the `displayMath` array.
- This ensures the delimiters are set to `\[ ... \]` (and `$$ ... $$`), matching standard LaTeX notation.

### Additional Considerations
1. **Line Breaking Issues**: You mentioned that some expressions are too long and overflow, especially on mobile views. The `linebreaks: { automatic: true }` setting in the "CommonHTML" output processor should handle this, but it requires the math to be inside a container with a defined width (e.g., `width: 100%`). Ensure your HTML structure includes something like:

   ```html
   <div style="width: 100%; overflow-x: auto;">
     \[ \text{Bit rate} = 2400 \, \text{baud} \times 3 \, \text{bits/symbol} = 7200 \, \text{bits per second (bps)} \]
   </div>
   ```

   This allows MathJax to break lines based on the container’s width, adapting to screen size.

2. **Output Processor**: Your script loads `TeX-MML-AM_CHTML`, which uses the CommonHTML output by default. The `"CommonHTML"` settings (e.g., `scale: 85`, `linebreaks: { automatic: true }`) will apply, but the `"HTML-CSS"` settings may not, as that output processor isn’t active. Since CommonHTML is modern and widely supported, this is fine—just ensure your settings align with it.

3. **Testing**: After updating the configuration, test with your sample expression:

   ```html
   \[ \text{Bit rate} = 2400 \, \text{baud} \times 3 \, \text{bits/symbol} = 7200 \, \text{bits per second (bps)} \]
   ```

   It should now render correctly as display math with proper line breaking if needed.

4. **Browser Compatibility**: MathJax 2.7.7 should work in most modern browsers. If issues persist, ensure there are no JavaScript errors in the console or conflicting CSS rules (e.g., `white-space: nowrap`) overriding the math rendering.

### Final Corrected Code
Here’s the complete, corrected setup:

```html
<!-- MathJax Configuration -->
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ["\\(","\\)"] ],
      displayMath: [ ["$$","$$"], ["\\[","\\]"] ],
      processEscapes: true
    },
    "CommonHTML": {
      linebreaks: { automatic: true },
      scale: 85
    },
    TeX: { equationNumbers: { autoNumber: "AMS" } }
  });
</script>

<!-- Load MathJax -->
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

<!-- Example Math -->
<div style="width: 100%; overflow-x: auto;">
  \[ \text{Bit rate} = 2400 \, \text{baud} \times 3 \, \text{bits/symbol} = 7200 \, \text{bits per second (bps)} \]
</div>
```

### Why This Works
- **Delimiter Fix**: `["\\[","\\]"]` ensures MathJax recognizes `\[ ... \]` as display math, matching your content.
- **Line Breaking**: The `CommonHTML` settings with a proper container enable automatic line breaks for long expressions.
- **Rendering**: The CDN script and configuration together ensure math is processed and displayed correctly.

Update your code with this fix, and your MathJax setup should work as intended! If problems persist, please share specific examples of math expressions that fail or any error messages you encounter.

---

To configure MathJax to render the mathematical expressions in the provided content well, you need to ensure it correctly handles inline math expressions like \( T_p \) and \( 2 \times T_p \), which are enclosed in LaTeX-style delimiters. The content uses `\( ... \)` for inline math, and while it doesn't include display math (e.g., equations on separate lines), it's good practice to configure MathJax for both inline and display math for flexibility. Below is a step-by-step guide to achieve this.

### Step 1: Include MathJax in Your HTML
First, you need to load the MathJax library. You can use a Content Delivery Network (CDN) to include it in your HTML file. Add the following script tag to your HTML `<head>` or before the content that contains math:

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.9/MathJax.js?config=TeX-AMS_CHTML"></script>
```

This loads MathJax version 2.7.9 with the `TeX-AMS_CHTML` configuration, which supports LaTeX input and renders math as HTML with CSS, suitable for most web applications.

### Step 2: Configure MathJax Delimiters
MathJax needs to know which delimiters to recognize for math expressions. The content uses `\( ... \)` for inline math, which is a standard LaTeX delimiter. To ensure MathJax processes these correctly, add a configuration script before the MathJax library script. Here’s a basic configuration:

```html
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ['\\(', '\\)'] ],
      displayMath: [ ['$$', '$$'], ['\\[', '\\]'] ],
      processEscapes: true
    }
  });
</script>
```

- **`inlineMath`**: Tells MathJax to treat text between `\( ... \)` as inline math. The double brackets `[ ['\\(', '\\)'] ]` are used because MathJax accepts an array of delimiter pairs.
- **`displayMath`**: Configures MathJax to recognize `$$ ... $$` and `\[ ... \]` as display math, even though the current content doesn’t use these. This ensures compatibility with future content.
- **`processEscapes`**: Allows escaping delimiters (e.g., using `\$` to display a literal dollar sign), though it’s not critical for this specific content.

### Step 3: Enhance Rendering for Responsiveness
To make the rendered math adaptable to different screen sizes (e.g., preventing overflow on mobile devices), enable automatic line breaking for long expressions. Update the configuration like this:

```html
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ['\\(', '\\)'] ],
      displayMath: [ ['$$', '$$'], ['\\[', '\\]'] ],
      processEscapes: true
    },
    "HTML-CSS": { linebreaks: { automatic: true } },
    CommonHTML: { linebreaks: { automatic: true } },
    SVG: { linebreaks: { automatic: true } }
  });
</script>
```

- **`HTML-CSS`, `CommonHTML`, `SVG`**: These are output processors MathJax uses to render math. Enabling `linebreaks: { automatic: true }` ensures long expressions wrap naturally, though the expressions in this content (\( T_p \), \( 2 \times T_p \)) are short and unlikely to need wrapping.

### Step 4: Combine Everything
Here’s the complete setup to include in your HTML file before the content:

```html
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ['\\(', '\\)'] ],
      displayMath: [ ['$$', '$$'], ['\\[', '\\]'] ],
      processEscapes: true
    },
    "HTML-CSS": { linebreaks: { automatic: true } },
    CommonHTML: { linebreaks: { automatic: true } },
    SVG: { linebreaks: { automatic: true } }
  });
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.9/MathJax.js?config=TeX-AMS_CHTML"></script>
```

### Step 5: Verify the Content Renders Correctly
With this configuration, the inline math in your content—such as \( T_p \) and \( 2 \times T_p \)—will render as properly formatted mathematical expressions. For example:
- \( T_p \) becomes a subscripted variable.
- \( 2 \times T_p \) displays with a multiplication symbol (×) and the subscripted \( T_p \).

### Additional Notes
- **No Display Math**: Since your content only uses inline math, the `displayMath` settings aren’t strictly necessary but are included for completeness.
- **CSS Styling**: Ensure the HTML container for your content (e.g., a `<div>`) has `width: 100%` or appropriate styling to keep the layout responsive.
- **Testing**: After adding this configuration, load your page in a browser to confirm that \( T_p \) and \( 2 \times T_p \) render as expected.

This setup ensures MathJax renders the mathematical expressions in your CSMA/CD explanation clearly and professionally, enhancing readability for users.

