# Jiminy編集用圧縮ファイル仕様 — version 1

拡張子: `.jiminy`。これは編集再開用であり、ミシンに直接渡すJEF/PES等とは別です。
圧縮には標準の **gzip（RFC 1952）/ DEFLATE（RFC 1951、LZ77とハフマン符号）** を使用します。
Jiminy独自の圧縮アルゴリズムではありません。暗号化・秘密鍵・外部辞書はありません。

## バイト構造

ファイル全体が単一の標準gzipメンバーです。先頭2バイトは `1f 8b`。
独自の前置きヘッダーはありません。gzipヘッダー、DEFLATEデータ、CRC32とISIZEのトレーラーを持ちます。
ブラウザ標準の `CompressionStream('gzip')` / `DecompressionStream('gzip')` を使い、外部圧縮ライブラリは組み込みません。
圧縮レベル・gzipヘッダーの任意フィールド・圧縮後のバイト列はブラウザ実装により異なり得ます。

解凍した内容はBOMなしUTF-8 JSONです。必須の構造:

```json
{"format":"jiminy-project","version":1,"state":{"stitch":{}}}
```

`format` は上記固定文字列、`version` は整数1。`state` は保存時の `store.getState()` の全JSONデータです。
画像のdata URL、色・領域・設定・生成済みステッチなどは元の状態のまま格納します。
JSON.stringifyによる既存JSON保存と同じ表現を使います。数値の丸め、点の間引き、画像の再圧縮は行いません。
JSONに表現できないJavaScript値の扱いもJSON.stringifyに従います。ブラウザの履歴・別サイトの状態まで保存する形式ではありません。
従来の `.json` はラッパーなしのstateオブジェクトとして読み込みます。
将来の非互換変更はversionを上げます。現在の読込は不明なバージョンを拒否し、現在のデータを置き換えません。

## Jiminyがなくても取り出す方法

標準のgzipで解凍可能です。拡張子を.gzにコピーして対応アーカイバーを使っても構いません。
Python標準ライブラリだけで従来のJSONを復元できます:

```python
import gzip, json
with gzip.open('sample.jiminy', 'rt', encoding='utf-8') as f:
    project = json.load(f)
if project.get('format') != 'jiminy-project' or project.get('version') != 1:
    raise ValueError('Unsupported Jiminy project')
with open('recovered.json', 'w', encoding='utf-8') as f:
    json.dump(project['state'], f, ensure_ascii=False)
```

コマンドライン: `gzip -dc < sample.jiminy > envelope.json`。
生成されたenvelope.jsonの `state` を取り出せば従来の編集JSONになります。

## 容量と検証

現在のブラウザ実装は入力および解凍後のUTF-8データに256MiBの上限を設けます。
gzipの整合性検証、JSON解析、形式・バージョン・stateの基本構造確認を完了してから現在の状態を置き換えます。
CRC32は偶発的な破損検出であり、改ざん防止の署名ではありません。
圧縮率は内容によって異なります。既に圧縮された画像が多い場合は縮みにくく、小さなデータは増える場合もあります。
`.jiminy`ファイル自体が既に圧縮済みなので、チャット転送時は通常compression=noneを選択します。
転送にさらにgzipを使う場合は、転送のgzipだけを解凍し、元の.jiminyの容量とSHA-256を照合してください。

## ライセンスと参考仕様

標準圧縮方式の使用と、Jiminyのソフトウェアコードの利用許諾は別です。
圧縮APIの利用のために第三者の圧縮ライブラリを追加・再配布しません。
RFCは特許に抵触しない形で実装できる方式として説明しています。本仕様はその一般的な方式を利用します。
本書は独立した復元実装のための形式説明です。Jiminyのソフトウェア全体のライセンスはサイトの利用条件に従います。

- RFC 1951: https://www.rfc-editor.org/rfc/rfc1951
- RFC 1952: https://www.rfc-editor.org/rfc/rfc1952
- Compression Standard: https://compression.spec.whatwg.org/
- 実装: public/stitch/js/common/project-codec.js
- テスト: tests/project-codec.mjs


## 編集保存・新規作成・再開（Jiminy format v1）
編集用の推奨保存形式は.jiminy。標準gzip/DEFLATEでUTF-8 JSONの全制作状態を可逆圧縮する。generate_editable_projectは既定でjiminy、format=jsonで従来JSONを生成。select_delivery_formatsはjiminy/json/jef/pes/pec/dstに対応。ミシン用形式と編集用形式は別。新規作成や画像の入れ替え前には既存の保存・破棄・取消の確認を使う。バックアップ生成を待ち、チャット添付またはユーザーの保存先確認が完了するまで現在の制作状態を保持する。保存要求と端末保存完了は区別する。メニューの「開く」で.jiminyと従来.jsonを読み込める。破損・未対応versionは現データを置換せずエラーになる。
圧縮アルゴリズムをJiminy独自発明と説明しない。仕様と独立した解凍手順: /jiminy-format.md。既に圧縮済みの.jiminyの転送はcompression=noneを推奨。転送gzipを使った場合、転送層だけを解凍し元.jiminyのbytes/SHA-256を照合する。圧縮率は実ファイルの測定値だけを報告する。プロジェクトをMCPサーバーへ送らない。


## v241 JEFの連続JUMPと顔試作
JEF出力で複数JUMPの途中へゼロ移動STITCHを入れず、連続JUMPの最後だけ従来の補助STITCHを入れる。島内回り込みの途中では針を落とさない。既存の単独JUMPの補助STITCHは保つ。/samples/bear-face-ready/ に更新経路を下縫い・実縫いの目鼻口と合成したJEF試作を置いた。顔切り出し73.5×47mm、110mm枠の仮指定。一色の毛／三色の毛でも顔パーツ込みの実糸は4種類。端末保存、ライブStudio操作、実機の縫製は未確認。全身の完成品とは言わない。
