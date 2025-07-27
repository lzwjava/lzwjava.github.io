---
audio: false
generated: false
image: true
lang: ja
layout: post
title: AIコーディングツールに関する厳選エンジニアの意見
translated: true
---

最近、Claude Codeを成功させて実行できたので、ツール選択の旅について共有したいと思います。その過程でいくつかの[AIツールのヒント](ai-tips-en.md)も集めました。

Claude Codeの採用はかなり遅れました。

[Claude Code](https://www.anthropic.com/news/claude-3-5-sonnet)は2025年2月末頃にリリースされました。

最近まで試すことができませんでした。その理由の一つは、Anthropic APIが中国のビザカードをサポートしていないためです。

もう一つの理由は、[Claude Code Router](https://github.com/musistudio/claude-code-router)が利用可能になったことで、最近の試みが成功したからです。

その評判をよく聞いていました。2025年7月にGemini CLIを試しましたが、コードを修正させる試みが何度か失敗した後、断念しました。

Aiderという別のソフトウェアエージェントも試しました。Cursorは6ヶ月ほど使った後、VSCodeベースのプラグインが多く機能しなかったため、使用を止めました。さらに、Cursorにはあまりクレジットを与えたくないと考えています。それはVSCodeの上に構築されているからです。VSCodeのCopilotプラグインは最近改善され、遅れを取っていないため、より頻繁に使用するようになりました。

しかし、VSCodeはElectronというオープンソース技術で構築されています。正しいチームや個人にクレジットを与えるのは難しいです。多くの大企業やスタートアップがオープンソースプロジェクトから利益を得ていることを考えると、予算と自分に合ったものに集中する必要があります。クレジットを与えることについてあまり心配する必要はありません。手頃で効果的なツールを使うことを好みます。

Clineも試しましたが、採用しませんでした。

VSCodeのCopilotプラグインをカスタムモデルのGrok 3 betaをOpenRouter経由で使用しています。これはうまく動作しています。

Claude Codeが私の習慣を変えるとは思いませんが、成功させて実行でき、さらに数回試す忍耐力があるので、今後数週間の感じを見てみます。

私は10年のソフトウェアエンジニアリング経験を持つ厳選ユーザーです。ツールが実際の使用で優れていることを望んでいます。ブランドにはこだわりません。日常的な有用性だけが重要です。

Claude Codeを使ってこの投稿の文法を修正した後、特定のシナリオでうまく動作することがわかりました。AIによる文法支援は感謝しています（私はLLM APIを呼び出すためのPythonスクリプトまで書きました）。しかし、最小限の修正を依頼しても、ツールが多数の文法提案を表示するという悩ましいパターンに気づきました。この手動確認プロセスは自動化の目的を損なっています。妥協として、現在はAIに全体のエッセイを処理させるようにしています。ただし、このアプローチは、特定の修正が行われているのを見る機会が限られるため、学習機会が制限されます。

最も印象的だったのは、Claude Codeが変更を表示する方法です。git diffに似た前後の比較を表示するため、編集の確認がはるかに簡単になります。

1日後、Claudeを使ってコードの修正も行いました。しかし、CopilotプラグインをGrok 3 betaモデルと一緒に使用し続けています。それはシンプルで私にとって使いやすいからです。

{: .centered }
![](assets/images/claude/claude-code.jpg){: .responsive }
*Source: Self-screenshot*{: .caption }

{: .centered }
![](assets/images/claude/claude-fix.jpg){: .responsive }
*Source: Self-screenshot*{: .caption }

{: .centered }
![](assets/images/claude/vscode-fix.jpg){: .responsive }
*Source: Self-screenshot*{: .caption }