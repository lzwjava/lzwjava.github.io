---
audio: false
generated: false
image: true
lang: ja
layout: post
title: AIコーディングツールに関する厳選エンジニアの意見
translated: true
---

最近、Claude Codeを成功させたので、ツール選択の旅について共有したいと思います。その過程でいくつかの[AIツールのヒント](ai-tips-en)も集めました。

Claude Codeの採用はかなり遅れました。

[Claude Code](https://www.anthropic.com/news/claude-3-5-sonnet)は2025年2月末頃にリリースされました。

最近まで試すことができませんでした。その理由の一つは、Anthropic APIが中国のビザカードをサポートしていないことです。

もう一つの理由は、[Claude Code Router](https://github.com/musistudio/claude-code-router)が利用可能になったことで、最近の試みが成功したからです。

常にその評判を聞いています。2025年7月にGemini CLIを試しましたが、コードを修正するための複数の試みに失敗した後、断念しました。

また、Aiderという別のソフトウェアエージェントも試しました。Cursorは約6ヶ月後に使用を停止しました。そのVSCodeベースのプラグインの多くが機能しなかったからです。Clineも短期間試しましたが、採用しませんでした。

私は、OpenRouterを通じてカスタマイズされたモデル、Grok 3 betaを使用して、VSCodeのCopilotプラグインを使用しています。これはうまく動作しています。

Claude Codeが私の習慣を変えるとは思いませんが、成功させて実行できるので、今後数週間、もう少し試してみるつもりです。

私は10年のソフトウェアエンジニアリングの経験を持つ厳選ユーザーです。ツールが実際の使用で優れていることを望んでいます。ブランドにはこだわりません。日常的な有用性だけが重要です。

Claude Codeを使用してこの投稿の文法を修正した後、特定のシナリオでうまく動作することを発見しました。AIによる文法支援を評価しています（私はLLM APIを呼び出すためのPythonスクリプトさえ書きました）。しかし、私は悩ましいパターンに気づきました。最小限の修正を要求しても、ツールは数多くの文法提案を表示し続けます。この手動検証プロセスは、自動化の目的を損なっています。妥協として、現在はAIに全体のエッセイを処理させています。ただし、このアプローチは、特定の修正が行われているのを見る機会が限られるため、学習機会が制限されます。

最も印象的だったのは、Claude Codeが変更を表示する方法でした。git diffに似た前後の比較を表示するため、編集の確認がはるかに簡単になります。

1日後、Claudeを使用してコードの修正も行いました。しかし、CopilotプラグインとGrok 3 betaモデルを引き続き使用しています。それはシンプルで私にとって使いやすいからです。

{: .centered }
![](assets/images/claude/claude-code.jpg){: .responsive }
*Source: Self-screenshot*{: .caption }

{: .centered }
![](assets/images/claude/claude-fix.jpg){: .responsive }
*Source: Self-screenshot*{: .caption }