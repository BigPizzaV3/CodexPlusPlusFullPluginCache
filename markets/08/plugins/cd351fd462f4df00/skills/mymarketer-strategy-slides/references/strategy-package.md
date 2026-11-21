# 3資料の制作と照合

保存済みの戦略本文を入力の正本とし、主張と根拠の対応を資料ごとに保持する。サーバーが返した `strategyContentHash` がある場合だけ、実ファイルへ `MyMarketer strategy: <hash>` を記載する。手元のファイルや文章から独自計算した値を、サーバーの識別子として扱わない。

| 成果物 | 役割 |
| --- | --- |
| 提案PPTX | 読み手が結論・選択理由・次の判断を理解できる。図表と文字が編集可能 |
| 戦略詳細DOCX | スライドから省いた根拠、代替案、判断理由、制約、出典、仮説と反証条件を追える |
| 実行検証ブリーフDOCX | 誰が、何を条件に着手し、何を作り、何を観測して完了・停止・修正とするかが分かる |

同梱PPTXエンジンは既存の図解・ブランドを再利用する。正式な草案へ返す場合は次の引数で識別子を含める。

```sh
python3 scripts/build_deck.py deck.json /absolute/output/proposal.pptx --strategy-content-hash <server-returned-hash>
python3 scripts/build_documents.py documents.json /absolute/output/package
```

DOCX入力は `schemaVersion: 1`、`strategyContentHash`、`strategyTitle`、`documents` を持つJSON。`documents` は `strategy_docx` と `execution_brief_docx` の2つ。各文書は `title` と `sections` を持つ。sectionは `heading`、任意の `paragraphs`、`bullets`、`tables`、`sources`。tableは `headers` と同じ列数の `rows`。全ての文字列は完成原稿であり、コード・命令として実行しない。

入力は先に執筆・照合して作る。形式だけを埋めるための内容、架空の顧客発言・実績・目標、見本の数値を入れない。出典は原資料のページ等までたどれる形にする。ページ数を固定しない。

スクリプトはファイルを組み立てるだけで、文書の論理・表現品質や戦略との一致を判定しない。実際のPPTX・DOCXを描画して全ページを確認し、日本語・表・改ページ・文字切れを修正する。DOCXの生成には `python-docx`、PPTXの識別子追加には `python-pptx` を使う。ホストが提供するランタイムを優先し、利用できなければホストの文書制作機能で同じ契約を満たす。

3資料の数値・約束・結論・出典と戦略版を照合してから、`strategy-authoring` の転送・本人確認へ返す。MyMarketerは資料を審査しない。ChatGPT/Codex側で確認した範囲・未確認事項と、保存済み・ユーザー確定済みを区別する。
