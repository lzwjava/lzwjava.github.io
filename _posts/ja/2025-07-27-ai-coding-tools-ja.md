---
audio: false
generated: false
image: true
lang: ja
layout: post
title: AIコーディングツールに関する厳選エンジニアの意見
translated: true
---

最近、Claude Codeを成功させて実行できたので、ツール選択の旅について共有したいと思います。その過程でいくつかの[AIツールのヒント](ai-tips-en.md)も収集しました。

Claude Codeの採用はかなり遅れました。

[Claude Code](https://www.anthropic.com/news/claude-3-5-sonnet)は2025年2月末頃にリリースされました。

最近まで試すことに成功しませんでした。その理由の一つは、Anthropic APIが中国のビザカードをサポートしていないことです。

もう一つの理由は、[Claude Code Router](https://github.com/musistudio/claude-code-router)が利用可能になったことで、最近の試みが成功したことです。

その評判をよく聞きます。2025年7月にGemini CLIを試しましたが、コードを修正させる試みが何度か失敗した後、断念しました。

Aiderという別のソフトウェアエージェントも試しました。Cursorは6ヶ月ほど使った後、多くのVSCodeベースのプラグインが機能しなかったため、使用を停止しました。さらに、Cursorにはあまりクレジットを与えたくないと思っています。それはVSCodeの上に構築されているからです。VSCodeのCopilotプラグインは最近改善され、遅れを取っていないので、より頻繁に使用することを好みます。

Clineも briefly 試しましたが、採用しませんでした。

私はVSCodeのCopilotプラグインをカスタムモデルのGrok 3 betaをOpenRouter経由で使用していますが、これはうまく動作しています。

Claude Codeが私の習慣を変えるとは思いませんが、成功させて実行できて、さらに数回試す忍耐力があるので、今後数週間の感じを見てみます。

私は10年のソフトウェアエンジニアリングの経験を持つ厳選ユーザーです。ツールが実際の使用で優れていることを望みます。ブランドにはこだわりません—毎日使えることだけが重要です。

この投稿の文法を修正するためにClaude Codeを使用した後、特定のシナリオでうまく機能することがわかりました。AIによる文法支援を評価しています（私はLLM APIを呼び出すためのPythonスクリプトさえ書きました）。しかし、最小限の修正をリクエストしても、ツールが数多くの文法提案を表示するという悩ましいパターンに気づきました。この手動確認プロセスは自動化の目的を損なっています。妥協策として、現在はAIに全体のエッセイを処理させるようにしていますが、このアプローチは特定の修正が行われているのを見る機会が限られるため、学習の機会が制限されます。

最も印象的だったのは、Claude Codeが変更を表示する方法です—git diffに似た前後の比較を表示するため、編集の確認がはるかに簡単になります。

1日後、Claudeを使用してコードの修正も行いました。しかし、CopilotプラグインとGrok 3 betaモデルを使用し続けています。それはシンプルで私にとって使いやすいからです。

{: .centered }
![](assets/images/claude/claude-code.jpg){: .responsive }
*Source: Self-screenshot*{: .caption }

{: .centered }
![](assets/images/claude/claude-fix.jpg){: .responsive }
*Source: Self-screenshot*{: .caption }

{: .centered }
![](assets/images/claude/vscode-fix.jpg){: .responsive }
*Source: Self-screenshot*{: .caption }