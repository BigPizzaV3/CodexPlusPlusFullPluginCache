# Paper Interpreter (Japanese)

![Paper Interpreter](assets/logo.png)

論文のPDFをアップロードするかURLを入力すると、内容を日本語で分かりやすく説明します。This is the Japanese version of Paper Interpreter. The international version is available at https://chat.openai.com/g/g-R9Dry2N5h-paper-interpreter

作者: Daichi Konno。無料公開GPTs [Paper Interpreter (Japanese)](https://chatgpt.com/g/g-hxDOCBQrs-paper-interpreter-japanese) のCodexプラグイン版です。

公開審査用パッケージ（version 0.1.0）です。ディレクトリでの提供状況はOpenAIのPlugins Directoryでご確認ください。

## 会話のきっかけ

👇PDFをアップロードするか論文URLを入力してください👇

導入後、新しい会話でプラグインを選び、論文PDFを添付するか論文URLを入力します。追加の依頼文がなくても解説します。図は「Figure 1を説明して」のように質問できます。

同名の個人用スキルがある場合は、プラグインを選ぶか `$paper-interpreter:paper-interpreter` を明示します。

## 元GPTsから再現した動作

- 題名（英語・日本語）、掲載先・発表年、筆頭著者・最終著者（英語）、最初の所属1件（英語）、要旨、背景、方法、結果、考察、新規性、限界、応用可能性の12項目。各項目は大きい太字見出しです。
- 通常の解説は日本語の「だ・である」調。数値・単位・小数点・P値は論文の記載を保持します。
- アップロード／ローカルPDFは、そのPDFだけを参照してWeb検索しません。URLはインターネットで一次資料を確認します。
- 図の質問には毎回PDF／URLを開き直し、凡例に存在する全パネルを明示して説明します。パネルや結果を創作しません。
- 新しいPDFは回答前に読み直します。
- 使い方の固定文と、その中のInternational版GPTへのリンクを保持しています。
- 元GPTsの名称・長い説明・会話のきっかけ・元のアイコンを使用しています。短い説明だけを公開申請の30文字上限に合わせています。

## ZIPを受け取った人の導入

ZIPを解凍すると `paper-interpreter/` が現れます。隠しフォルダ `.codex-plugin/` も含めて保持してください。ZIPをチャットへ添付するだけではインストールされません。

Codexで解凍したフォルダを開き、次の依頼を送ります。

```text
$plugin-creator を使って、このフォルダの Paper Interpreter (Japanese) を私の個人用マーケットプレイスへ導入してください。
README.md と .codex-plugin/plugin.json を確認してください。既存のマーケットプレイスや他のプラグインを保持し、paper-interpreter だけを追加してください。
標準の個人用配置 ~/plugins/paper-interpreter に置き、同名の異なるファイルがあれば上書き前に確認してください。
Plugin Creatorの標準手順で登録・検証・インストールし、完了後は新しい会話で使う方法を教えてください。
```

開発者のAPIキー、専用サーバー、追加の有料サービス契約は不要です。実行に使うCodex環境と利用枠は利用者が用意します。APIキー認証で実行する場合のAPI利用料は利用者の設定に従います。

## データと配布

このプラグインには、開発者へ論文を送る機能や、独自の外部サーバー接続はありません。PDFモードのWeb検索禁止は、Codex自体のAI処理が完全にオフラインになることを意味しません。

導入者は同梱の指示ファイルを読むことができます。元GPTsの内部設定非開示の指示は、非公開システム指示・認証情報の保護として引き継ぎ、公開プラグインの仕様説明は可能にしています。

固定の使い方は、元の丁寧語と英語の一文を例外として保持しています。

このZIPは公開審査用パッケージです。ワークスペース内の共有と一般公開は異なり、一般公開には[OpenAIへの申請・審査](https://developers.openai.com/plugins/deploy/submission)が必要です。

元GPTsの推奨モデルや画面配置は、このプラグインから固定しません。応答は利用者のモデル・ツール・上位指示にも依存します。個人用スキルへの依存はありません。
