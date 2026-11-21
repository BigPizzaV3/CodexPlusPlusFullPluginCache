# 制作環境と書き出し

このフォルダーは共通のSKILL.md・参照資料・パレット・SlideSpec見本・生成エンジンを持つ。`agents/openai.yaml` はCodex用の表示メタデータで、制作判断はSKILL.mdに置く。特定ホストの絶対パスやAPIキーは不要。

## 元スキルとの関係

元の `consulting-pptx-skill` がある環境では、その規約や型カタログも利用できる。本スキルでは案件データの読み方・マーケティング構成・ブランド指定を追加する。ユーザー指定の枚数や形式を優先し、見本に表紙・裏表紙を自動追加する必要はない。基本6枚と、3C・STP・KPIの3枚、深掘り用14枚を必要に応じて参照する。

`vendor/consulting` は [gozen3ji/consulting-pptx-skill](https://github.com/gozen3ji/consulting-pptx-skill) のローカル導入済み版から、PPTX生成に必要なファイルを同梱したもの。ローカル修正は、配置先のfile URL変換、元開発者専用パスの除去、ゴシック体・濃紺見出し・共通ヘッダーの公式ロゴ掲載。変更点と元・同梱ハッシュは `UPSTREAM.json` に記録する。配色と資料メタデータは外側の `build_deck.py` で適用する。ロゴはスキル内の画像を参照し、外部URLを取得しない。ライセンスは同ディレクトリの `LICENSE`、取り込み時点とファイルハッシュは `UPSTREAM.json`。同梱の `package.json` は本追加スキルが用意した依存定義。

## ファイルを生成できる環境

Python 3、Node.js、PptxGenJSが利用可能なら、スキルのルートから次のように実行する。

```sh
python3 scripts/build_deck.py assets/demo-spec.json /absolute/output/demo.pptx
python3 vendor/consulting/scripts/check_deck.py /absolute/output/demo.pptx
```

`check_deck.py` のPPTX検査には `python-pptx` が必要。利用環境に既存の依存ランタイムがあればそれを使う。Node実行ファイルは `--node`、PptxGenJSを含むnode_modulesディレクトリは `--module-dir` で指定できる。Codexデスクトップでは `load_workspace_dependencies` が返したパスを利用し、他人の絶対パスを流用しない。

PptxGenJSがないローカル環境では `vendor/consulting/pipeline` の `package.json` に従って依存を準備する。インストールの可否はホストのネットワーク・実行権限に従う。スクリプト自身はネットワーク接続・自動インストール・MCP呼び出しをしない。

入力はSlideSpecであり、MyMarketerのレスポンスJSONをそのまま渡せない。連携データを読んで構成した後に、`assets/demo-spec.json` や既存型のフィールド構造を参考に作る。実案件へ見本の数値を流用しない。

標準配色は自動適用され、入力の `palette` に指定した色が優先される。別の初期配色には `--palette palette.json` を使う。再書き出しで既存ファイルを置換するときのみ `--overwrite` を付ける。

出力の構造検査後、PPTXをPDFまたはページ画像にレンダリングして全ページを見る。プレビューも最終PPTXから作る。元スキルのHTMLレンダラーは別経路のため、PPTXと色・配置が同じとは仮定しない。使用可能なPowerPoint／LibreOffice／ホストのレンダラーを利用し、ホストに指定ランタイムがある場合はその規約に従う。

## ホストによる能力の違い

| 利用環境 | 選択する経路 |
| --- | --- |
| Codex / Claude Code等のローカル環境 | 発見可能なスキルとして読み、接続済みMyMarketer MCPから取得。依存が揃えば同梱エンジンでPPTXを生成 |
| ChatGPT等でコネクタとファイル実行が使える環境 | 提供されたスキル一式を読み、MyMarketerの読み取りツールを確認。Node等があれば同梱エンジン、なければホストの資料制作機能で同じ構成・配色を再現 |
| 接続なし・戦略エクスポートあり | 取得時点と台帳の完全性を明記して資料化。最新の正本との一致は未確認とする |
| ファイル生成機能なし | タイトル列・本文・根拠対応表と配色を出す。PPTXを作成したと主張しない |

ZIPを渡すだけで各サービスにスキルや接続が自動登録されるわけではない。利用ホストの現行の登録・添付方法に従う。本スキルに認証情報を追加しない。異なる生成エンジン・フォント間の完全な見た目の一致は未検証として扱う。

## 持ち運び用の依頼文

「添付のmymarketer-strategy-slidesのSKILL.mdを読み、利用可能なMyMarketer連携から対象案件の戦略と承認済み判断を取得して、選択理由と実行計画が伝わる資料を作って。対象案件は会話中で指定したもの。編集可能なPPTXとプレビューを希望。接続やファイル生成が利用できなければ、利用可能な範囲を明示して進めて。」

## 更新・検証

元スキルを更新するときは対象ファイルの差分とライセンスを確認し、スナップショット・ハッシュを更新する。標準パレット、明示的な上書き、構造検査、6枚見本の全ページ描画を再確認する。元スキル側へMyMarketer専用設定を直接書き込まない。

## 図解見本の再生成

[基本の3枚（PPTX）](../assets/examples/frameworks.pptx)と[追加14枚（PPTX）](../assets/examples/marketing.pptx)は全図形・文字が編集可能。PDF版も同じ場所に同梱する。追加14枚は重要箇所にゴールドを使う承認済み版、基本3枚は先に承認された濃紺の図解版を保つ。

スキルのルートから実行する。通常の `build_deck.py` と同じ `--node`、`--module-dir`、`--overwrite` が使える。

```sh
python3 scripts/build_examples.py frameworks /absolute/output/frameworks.pptx
python3 scripts/build_examples.py marketing /absolute/output/marketing.pptx
python3 vendor/consulting/scripts/check_deck.py /absolute/output/frameworks.pptx
python3 vendor/consulting/scripts/check_deck.py /absolute/output/marketing.pptx
```

`assets/examples/archetypes` のモジュールは架空案件の文章を含む見本ソースであり、汎用の入力テンプレートではない。`build_examples.py` は既存エンジンを一時領域へコピーし、見本型をそのコピーだけに登録して再生成する。通常の `build_deck.py` では見本型を受け付けず、実案件の入力を黙って架空例へ変換しない。生成後に一時エンジンは削除される。既存エンジンの新たな複製物をリポジトリに保管する必要はない。

3Cは `venn-geometry.json` の境界点を使い、（顧客 ∩ 自社）− 競合を編集可能なDrawingML自由図形へ置換してから完成ファイルを保存する。手作業の後処理は不要。円の位置・半径を変更するなら境界も再計算する。見本の境界点を別の配置へ流用しない。

実案件に適応するときは制作用コピーのソースまたはPPTX内の全文章・数値・出典・強調対象を見直す。見本JSONのタイトルだけを変えて実案件として出さない。図の選択基準と対応する入力は[マーケティング図解の選び方](marketing-diagrams.md)を参照する。

今回の見本の確認結果は[図解見本の検証記録](diagram-validation.md)を参照する。
