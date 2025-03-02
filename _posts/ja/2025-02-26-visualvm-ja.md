---
audio: false
generated: true
lang: ja
layout: post
title: Java アプリケーションのプロファイリングを VisualVM で
translated: true
---

ここには、VisualVMを使用してJavaアプリケーションのパフォーマンス、メモリ使用量、スレッドアクティビティを分析するための明確で簡潔なガイドがあります。VisualVMは、JDKに含まれる無料の強力なツールです。

---

### ステップ1: VisualVMのインストールと起動
- **VisualVMがインストールされているか確認**: VisualVMは通常、JDK（バージョン6アップデート7以降）に含まれています。JDKのインストールディレクトリの`bin`ディレクトリ（例: Windowsの`jdk/bin/visualvm.exe`）で探してください。
- **必要に応じてダウンロード**: 含まれていない場合は、[公式VisualVMウェブサイト](https://visualvm.github.io/)からダウンロードしてください。
- **VisualVMの起動**: `visualvm`実行ファイルを実行します。起動すると、ローカルマシン上で現在実行中のJavaプロセスの一覧が表示されます。

---

### ステップ2: Javaアプリケーションへの接続
- **ローカルアプリケーション**: VisualVMは、マシン上で実行中のJavaプロセスを自動的に検出します。監視したいプロセスをダブルクリックして接続します。
- **リモートアプリケーション**: 他のマシン上のJavaプロセスを監視するには:
  1. リモートJVMをJMX有効にして起動します（例: JVM引数に`-Dcom.sun.management.jmxremote`を追加）。
  2. VisualVMで左側のペインの**リモート**を右クリックし、**リモートホストの追加**を選択し、リモートマシンの詳細を入力します。
  3. 接続後、監視したいリモートプロセスを選択します。

---

### ステップ3: アプリケーションパフォーマンスの監視
接続後、**概要**タブにはプロセスIDやJVM引数などの基本的な詳細が表示されます。リアルタイムのパフォーマンスデータを表示するには、**モニタ**タブに切り替えます:
- **CPU使用率**: アプリケーションが使用するCPUの量を追跡します。
- **メモリ使用量**: ヒープとメタスペースの消費を時間経過とともに表示します。
- **スレッド**: アクティブなスレッドの数を表示します。
- **ガベージコレクション**: GCアクティビティを監視します。

これらのグラフは、アプリケーションの健全性の高レベルなビューを提供します。

---

### ステップ4: CPUとメモリ使用量のプロファイリング
より深い分析を行うには、**プロファイラ**タブを使用します:
- **CPUプロファイリング**: 最もCPU時間を消費するメソッドを特定します。
  1. **プロファイラ**タブに移動し、**CPU**をクリックします。
  2. **開始**をクリックしてプロファイリングを開始します。
  3. 分析したいワークロードを生成するためにアプリケーションを使用します。
  4. **停止**をクリックし、結果を確認して最も遅いメソッドを見つけます。
- **メモリプロファイリング**: オブジェクトの割り当てを追跡し、メモリリークを検出します。
  1. **プロファイラ**タブで**メモリ**をクリックします。
  2. **開始**をクリックし、アプリケーションを使用し、**停止**をクリックします。
  3. 結果を確認し、オブジェクトの数とサイズを確認して、潜在的なメモリ問題を見つけます。

**注意**: プロファイリングはオーバーヘッドを追加するため、開発またはテスト環境で使用してください。

---

### ステップ5: ヒープとスレッドダンプの分析
- **ヒープダンプ**: 詳細な分析のためのメモリスナップショットをキャプチャします。
  1. **モニタ**タブで**ヒープダンプ**をクリックします。
  2. **クラス**または**インスタンス**ビューでダンプを探索し、オブジェクトの割り当てを確認します。
  3. 異常なパターン（例: 多すぎるオブジェクト）を確認し、リークの兆候を見つけます。
- **スレッドダンプ**: デッドロックなどのスレッド問題を診断します。
  1. **スレッド**タブで**スレッドダンプ**をクリックします。
  2. スレッドの状態（例: RUNNABLE、WAITING）を確認して問題を特定します。

---

### ステップ6: 追加機能の探索
- **サンプラー**: **サンプラー**タブにあり、フルプロファイリングよりも軽量なCPUとメモリ分析を提供します。
- **Visual GC**: **ツール > プラグイン**からVisual GCプラグインをインストールして、ガベージコレクションの動作を視覚化します。
- **MBeans**: **MBeans**タブを使用して、カスタムメトリクスのためのJMXビーンを表示および管理します。

---

### ベストプラクティス
- **プロダクションでのプロファイリングを避ける**: プロファイリングはアプリケーションを遅くするため、開発またはテストセットアップに留めます。
- **シンプルに始める**: プロファイリングの前に**モニタ**タブを使用してベースラインを取得します。
- **特定の問題をターゲットにする**: オーバーヘッドを最小限に抑えるために、疑われる問題領域にプロファイリングを集中します。
- **GCデータを確認する**: メモリ使用量を最適化するためにガベージコレクションの統計を分析します。

---

### トラブルシューティング
- **アプリケーションが表示されない**: 互換性のあるJVMで実行されていることを確認し、VisualVMがアクセスできることを確認します。
- **リモートの問題**: リモートJVMがJMXに構成されていることを確認し、ネットワーク設定（例: ファイアウォール）が接続を許可していることを確認します。
- **パフォーマンスへの影響**: プロファイリングが遅い場合は、**サンプラー**を使用して軽量なオプションに切り替えます。

---

VisualVMは、Javaアプリケーションの理解と最適化に優れたツールです。これらの手順に従ってパフォーマンスを監視し、ボトルネックをプロファイリングし、問題を効果的に診断します。詳細については、[公式VisualVMドキュメント](https://visualvm.github.io/documentation.html)を参照してください。