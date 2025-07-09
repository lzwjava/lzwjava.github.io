---
title: Customizing LaTeX Bold Text Sizes
lang: en
layout: post
audio: false
translated: false
generated: true
---

Looking at your LaTeX code and the awesome-cv class file, the text inside `\begin{*cvparagraph*}...\end{*cvparagraph*}` uses the `\paragraphstyle` which is defined in the class as:

```latex
\newcommand*{\paragraphstyle}{\fontsize{11pt}{1em}\bodyfontlight\upshape\color{text}}
```

To change the bold size within this paragraph, you have a few options:

## Option 1: Use explicit font size commands for bold text
```latex
\begin{*cvparagraph*}
Below is a summary of my expertise and knowledge domains. While I have a solid understanding of some topics and a more basic familiarity with others, I would be {\large\textbf{happy to share more in an interview}} if you are interested in any specific areas.
\end{*cvparagraph*}
```

## Option 2: Define a custom bold command with specific size
Add this to your preamble:
```latex
\newcommand*{\custombold}[1]{{\fontsize{12pt}{1em}\bodyfont\bfseries\color{darktext} #1}}
```

Then use it in your paragraph:
```latex
\begin{*cvparagraph*}
Below is a summary of my expertise and knowledge domains. While I have a solid understanding of some topics and a more basic familiarity with others, I would be \custombold{happy to share more in an interview} if you are interested in any specific areas.
\end{*cvparagraph*}
```

## Option 3: Redefine the paragraph style (affects all cvparagraph environments)
Add this after loading the awesome-cv class:
```latex
\renewcommand*{\paragraphstyle}{\fontsize{11pt}{1em}\bodyfontlight\upshape\color{text}}
% And define what bold should look like in paragraphs
\let\originaltextbf\textbf
\renewcommand{\textbf}[1]{{\fontsize{13pt}{1em}\bodyfont\bfseries\color{darktext} #1}}
```

The most flexible approach is **Option 1** using `\large`, `\Large`, `\huge`, etc. with `\textbf{}` for the specific text you want to emphasize with larger bold formatting.