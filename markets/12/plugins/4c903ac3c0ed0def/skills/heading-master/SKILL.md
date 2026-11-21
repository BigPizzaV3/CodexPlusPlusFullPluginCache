---
name: heading-master
description: Websteの最新基準を使ってSEO記事のタイトル・見出し構成を作成する。タイトル・見出し作成、構成案、SEO見出し、メインKWからの記事構成を依頼されたときに使用する。
---

# Webste_見出し・タイトル作成マスタ

このプラグインでタイトル・見出し構成を作成・改善するときは、MCPの `get_heading_guidelines` を必ず使用する。

1. メインキーワードが分かっている場合は、その値を `main_keyword` に渡して `get_heading_guidelines` を呼ぶ。
2. 返された `【Instructions】` をこの機能の最新かつ優先する実行ルールとして扱う。
3. 返された `【Knowledge】` を判断材料として使用する。
4. Instructions と Knowledge の内容をこのSKILLへ固定的に写し戻さない。最新内容を毎回MCPから取得する。
5. ユーザー入力が不足している場合の確認、検索意図分析、タイトル・H2/H3設計、出力形式は、取得したInstructionsに従う。
6. MCPの認証・取得に失敗した場合は、古い内蔵ルールで代替せず、Webste MCPへの接続または再認証が必要であることを簡潔に伝える。
