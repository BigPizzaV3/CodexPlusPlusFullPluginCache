# ファイルを草案へ渡す

接続先が提示するtool schemaと返された転送先を使う。ローカルパスだけでは転送にならず、会話への添付だけではMyMarketerへ保存されない。

| 環境 | 使用する経路 |
| --- | --- |
| Codexなどローカルファイルを読める環境 | `transferStrategyFiles` の `prepare_upload` → 指定ファイルの実バイトを返された署名URLへPUT → `complete_upload` |
| ChatGPTなどホストがファイル参照を提供する環境 | toolの `_meta["openai/fileParams"]` 対象へホスト提供のfileを渡し、`import_host_file` を使う。参照URLやfile_idを推測・生成しない |
| 直接転送が利用できない環境 | サーバーが返した同じ草案の認証済みアップロード画面を案内し、`getStrategyDraft` で到着と保存状態を確認する |

用途は原資料 `source`、提案PPTX `proposal_pptx`、詳細DOCX `strategy_docx`、実行検証DOCX `execution_brief_docx`。アップロードの上限・形式はサーバー値に従う。ファイル名を変えて形式や容量制限を回避しない。

転送・保存の完了状態を確認する。原本の保存と内容の読み取りは別であり、MyMarketerの抽出結果がない資料はChatGPT/Codex側で読む。期限切れは同じ草案で新しい転送操作を準備し、以前の完了要求と異なる内容に同じ冪等キーを使わない。破損・暗号化・抽出失敗は、そのまま記録し、再転送やユーザーが選んだ資料の除外で解決する。

生成した3資料にも同じ転送経路を使う。ホスト上でダウンロードできることと、MyMarketerへの保存完了を区別する。転送完了までは戦略の確定工程へ進まない。
