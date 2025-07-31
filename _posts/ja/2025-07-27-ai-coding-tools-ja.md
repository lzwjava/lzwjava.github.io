---
audio: false
generated: false
image: true
lang: ja
layout: post
title: AIコーディングツールに関する厳選エンジニアの意見
translated: true
---

最近、Claude Codeを成功させて実行できたので、ツール選択の旅について共有したいと思います。その過程でいくつかの[AI Tool Tips](ai-tips-en.md)も収集しました。

Claude Codeの採用はかなり遅れていました。

[Claude Code](https://www.anthropic.com/news/claude-3-5-sonnet)は2025年2月末頃にリリースされました。

最近まで試すことができませんでした。その理由の一つは、Anthropic APIが中国のビザカードをサポートしていないからです。

もう一つの理由は、[Claude Code Router](https://github.com/musistudio/claude-code-router)が利用可能になったことで、最近の試みが成功したからです。

その評判をよく聞きます。2025年7月にGemini CLIを試しましたが、コードを修正するための何度かの試みに失敗した後、断念しました。

Aiderという別のソフトウェアエージェントも試しました。Cursorは約6ヶ月使った後、VSCodeベースのプラグインが多く機能しなかったため、使用を止めました。また、Cursorにはあまりクレジットを与えたくありません。それはVSCodeの上に構築されているからです。最近、VSCodeのCopilotプラグインが改善され、遅れを取っていないため、より頻繁に使用するようになりました。

しかし、VSCodeはElectronというオープンソース技術で構築されています。正しいチームや個人にクレジットを与えるのは難しいです。多くの大企業やスタートアップがオープンソースプロジェクトから利益を得ていることを考えると、予算と自分に最適なものに集中する必要があります。クレジットを与えることにあまり悩むべきではありません。手頃で効果的なツールを使うことを好みます。

Clineも少し試しましたが、採用しませんでした。

VSCodeのCopilotプラグインをカスタムモデルのGrok 3 betaをOpenRouter経由で使用しています。これはうまく動作します。

Claude Codeが私の習慣を変えるとは思いませんが、成功させて実行できるので、数回試してみるつもりです。今後数週間の感じを見てみます。

私は10年のソフトウェアエンジニアリングの経験を持つ選り好みなユーザーです。ツールが実際の使用で優れていることを望みます。ブランドにはこだわりません。日常的な有用性だけが気になります。

Claude Codeを使ってこの投稿の文法を修正した後、特定のシナリオでうまく機能することを発見しました。AIによる文法支援を評価しています（私はLLM APIを呼び出すためのPythonスクリプトさえ書きました）。しかし、最小限の修正を要求しても、ツールが数多くの文法提案を表示するというイライラするパターンに気づきました。この手動確認プロセスは自動化の目的を損なっています。妥協として、現在はAIに全体のエッセイを処理させるようにしています。ただし、このアプローチは、特定の修正が行われているのを見ることができないため、学習機会が制限されます。

最も印象的だったのは、Claude Codeが変更を表示する方法です。git diffに似た前後の比較を表示するため、編集の確認がはるかに簡単になります。

1日後、Claudeを使ってコードの修正も行いました。しかし、CopilotプラグインとGrok 3 betaモデルを使用し続けています。それはシンプルで私にとって簡単です。

Claude Codeを数日間使用した後、非常に印象的だと言わざるを得ません。コードを修正する方法が本当に気に入っています。

{: .centered }
![](assets/images/claude/claude-code.jpg){: .responsive }
*Source: Self-screenshot*{: .caption }

{: .centered }
![](assets/images/claude/claude-fix.jpg){: .responsive }
*Source: Self-screenshot*{: .caption }

{: .centered }
![](assets/images/claude/vscode-fix.jpg){: .responsive }
*Source: Self-screenshot*{: .caption }