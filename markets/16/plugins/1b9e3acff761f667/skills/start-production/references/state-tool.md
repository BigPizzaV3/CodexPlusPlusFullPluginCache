# 制作状態をローカルファイルで管理する

`scripts/case_state.py` はPython標準ライブラリのみで動く。実行できない環境ではproduction.mdの文章メモを使う。利用者にJSONの作成を求めず、作業側で生成する。

```sh
python3 scripts/case_state.py init case.json --case-id case-001 --doctor-id doctor-a --profile-version 1 --profile-source 本人設定_最新版.md
python3 scripts/case_state.py claim case.json claim.json --expected-revision 1
python3 scripts/case_state.py artifact case.json script.json --expected-revision 2
python3 scripts/case_state.py status case.json
python3 scripts/case_state.py validate case.json
```

主張payloadの項目：`claim_id`, `text`, `source_refs`（出典の参照先の配列）, `verification`（verified/partial/unverified）, `allowed_expression`。source_refsは実際に確認した出典を入れる。自分でverifiedと書くことが検証の代わりになるわけではない。

成果物payloadの項目：`artifact_id`, `location`（実在ファイル等）, `status`（draft/complete）, `dependencies`。例えば台本がC001の版1を使う場合は `{"claim:C001": 1}`。サムネイルが台本版1を使う場合は `{"artifact:script": 1}`。章単位で依存を分けたい場合は原稿の節を個別artifactとして登録する。

本人設定を使う成果物には `"profile:doctor": 1` のように参照した本人設定の版も入れる。進行中の案件に新版を適用するときだけ `profile case.json profile.json --expected-revision 現在の案件版` を使う。profile.jsonは同じdoctor_idと新しいversion、sourceを持つ。別医師への変更は拒否するので案件を分ける。過去案件には自動適用しない。

同じIDの再登録でその対象の版が進む。依存する成果物はneeds_updateになる。修正・再照合した成果物を現在の参照版で登録し直すまで、旧成果物を最新版扱いしない。変化のない成果物を再登録すると不要な版上げが起きるので、実際に更新したときだけ登録する。

expected-revisionは直前に読んだ案件全体の版。古い値での上書きは失敗するので最新を読み直す。循環参照・存在しない依存先も拒否する。ロックが残った場合は別の更新処理が動いていないか確認し、勝手に他の処理のロックを削除しない。

ローカルファイルのlocationはcase.jsonのある場所からの相対パス、または絶対パス。completeの保存・確認時には実ファイルがあることも検査する。https/httpの保存先とchat:から始まる会話内参照はこのスクリプトでは閲覧しないので、呼び出す側が内容と所在を確認する。

このツールが確かめるのは版・依存関係・ローカル完成ファイルの存在であり、文章の意味・論文の実在・画像の文字・クラウドへの保存は別に確認する。
