# 図解見本の検証記録

2026-09-05。架空の小売向け在庫管理サービスのデザイン見本。実MyMarketer連携や実案件の戦略評価を行った記録ではない。

- `build_examples.py frameworks`：3枚生成、SlideSpec検証 PASS、`check_deck.py` 0 FAIL / 0 WARN。
- `build_examples.py marketing`：14枚生成、SlideSpec検証 PASS、`check_deck.py` 0 FAIL / 0 WARN。
- 再生成PPTXの全スライドXML（名前空間を正規化）が承認済みPPTXと一致。LibreOfficeで再生成したPDFの全17ページは承認済みPDFと800pxレンダリングで画素一致。承認済み版は全ページ目視済み。
- 3Cの境界812点による多角形は、境界付近を除く12,923点で（顧客 ∩ 自社）− 競合の包含判定に一致。図形はネイティブの自由図形。
- 標準の `build_deck.py` は固定コピーの見本型を拒否し、実案件入力から架空例を出力しない。
- 既存出力の上書き拒否、`--overwrite` 指定時の生成失敗でも既存ファイルを保持、一時ファイルの後始末を確認。
- `skill-creator/scripts/quick_validate.py` PASS。検証専用PyYAMLは一時領域に準備し、配布依存へ追加していない。
- 追加14枚のゴールド文字は白地で4.53:1、濃紺地で7.52:1のコントラスト。重要な判断・キーワードに限定。
- 独立したソースレビュー：指摘なし。見本の一時登録、出力の完成後置換、参照リンク、source-mapの完全性、3C境界と外部参照なしを確認。

`runtime_validation_pending` を維持する。ネイティブ資産を保った配布bundleと各実行環境・実案件のend-to-endは未検証。PowerPointアプリでの表示確認は行っていない。製品内の生成機能は変更していない。
