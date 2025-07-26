---
audio: false
generated: false
lang: ja
layout: post
title: AIコーディングツールに関する選びにくいエンジニアの意見
translated: true
---

最近、Claude Codeを成功させて実行できたので、ツール選択の旅について共有したいと思います。その過程でいくつかの[AIツールのヒント](ai-tips-en)も集めました。

Claude Codeの採用はかなり遅れました。

[Claude Code](https://www.anthropic.com/news/claude-3-5-sonnet)は2025年2月末頃にリリースされました。

最近まで試すことに成功しませんでした。その理由の一つは、Anthropic APIが中国のビザカードをサポートしていないことです。

もう一つの理由は、[Claude Code Router](https://github.com/musistudio/claude-code-router)が利用可能になったことで、最近の試みが成功したことです。

その評判をよく聞きます。2025年7月にGemini CLIを試しましたが、コードを修正させようとする試みが何度か失敗した後、断念しました。

Aiderという別のソフトウェアエージェントも試しました。Cursorは約6ヶ月使った後、VSCodeベースのプラグインが多く機能しなかったため、使用を止めました。Clineも少し試しましたが、採用しませんでした。

VSCodeのCopilotプラグインをカスタムモデルのGrok 3ベータをOpenRouter経由で使用していますが、これはうまく動作しています。

Claude Codeが私の習慣を変えるとは思いませんが、成功させて実行できて、さらに数回試す余裕があるので、今後の数週間でどう感じるか見てみます。

私は10年のソフトウェアエンジニアリングの経験を持つ厳選ユーザーです。ツールが実際の使用で優れていることを望みます。ブランドにはこだわりません。日常的な有用性だけが重要です。

Claude Codeを使ってこの投稿の文法を修正した後、特定のシナリオでうまく機能することを発見しました。AIによる文法支援を評価しています（私はLLM APIを呼び出すためのPythonスクリプトさえ書きました）。しかし、気になるパターンに気づきました - わずかな修正を依頼しても、ツールは数多くの文法提案を表示します。この手動確認プロセスは自動化の目的を損なっています。妥協として、現在はAIに全てのエッセイを処理させていますが、このアプローチは特定の修正が行われているのを見る機会が限られているため、学習の機会が制限されます。

最も印象的だったのは、Claude Codeが変更を表示する方法です - git diffに似た前後の比較を表示するため、編集の確認がはるかに簡単になります。

{: .centered }
![](assets/images/claude/claude-code.jpg){: .responsive }
*Source: Self-screenshot*{: .caption }

{: .centered }
![](assets/images/claude/claude-fix.jpg){: .responsive }
*Source: Self-screenshot*{: .caption }