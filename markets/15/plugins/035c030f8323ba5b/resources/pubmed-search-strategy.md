# PubMed検索の方針と調整

[検索と確認](../skills/dental-literature-search/SKILL.md) と [学習Q&A](../skills/dental-paper-learning-qa/SKILL.md) が、検索式を作る・直すときに参照する。毎回の前処理として全部を読まない。記載はPubMed Helpと2026-11-04の確認に基づく。

## 質問の型と方針

| 質問の型 | 絞り込み（ツールの引数） | 並び順 | 補足 |
|---|---|---|---|
| 治療・予防の効果 | `publication_types: ["systematic_review", "meta_analysis"]`。3件未満なら `["randomized_controlled_trial"]`、それでも少なければ外す | relevance | 方針を必ず表示する |
| 新しい研究の動向 | `year_from: 今年-5` | pub_date | 新しさ優先と表示する |
| 診断精度 | なし | relevance | 検索式に `sensitivity[tiab] OR specificity[tiab] OR "diagnostic accuracy"[tiab]` を加える |
| 予後・経過 | なし | relevance | `prognos*[tiab] OR cohort[tiab] OR survival[tiab]` などを加える |
| 稀な疾患・合併症・有害事象 | なし（症例報告を含める） | relevance | 総説がないことが多い |
| 定義・分類・推奨 | `publication_types: ["guideline"]`、必要なら `["review"]` | relevance | 推奨の強さは本文で確認が必要と示す |
| 特定の論文 | なし | relevance | 題名 `"…"[ti]`、著者 `Wu MK[au]`、年 `2000[dp]` |

PubMed Helpの「Clinical Queries」の狭義フィルター（例：治療 `(randomized controlled trial[Publication Type] OR (randomized[Title/Abstract] AND controlled[Title/Abstract] AND trial[Title/Abstract]))`、診断 `(specificity[Title/Abstract])`）を検索式に加えてもよい。加えた場合はその旨を方針に書く。

- `systematic_review` は `systematic[sb]`（検索戦略と論文種別の併用）として送られる。`"systematic review"[pt]` より広い。
- 論文種別 `[pt]` は下位の種別も含む。
- PubMedの関連度（Best Match）は、語の一致や新しさ等にもとづく順位で、研究の質の評価ではない。

## 検索式の書き方

- 概念ごとに `( MeSH OR 題名・抄録の語 )` を作り、概念同士を `AND` でつなぐ。例：`("peri-implantitis"[mh] OR peri-implantitis[tiab]) AND (nonsurgical[tiab] OR non-surgical[tiab] OR debridement[tiab])`
- 二重引用符で囲んだ語やフィールドタグを付けた語は、PubMedの自動変換（Automatic Term Mapping）を受けない。ただし、引用符の語句が索引にない場合、PubMedは引用符を無視することがある（`QUOTED_PHRASE_NOT_FOUND`）。
- 前方一致の `*` は4文字以上で使い、自動変換が止まることに注意する。
- DOIでの特定は `get_pubmed_articles` の `dois` を使う（検索式に書かない）。

## 歯科でつまずきやすい語

| 日本語 | 避ける形 | 使う形（例） | 理由 |
|---|---|---|---|
| インプラント | `implant` | `"dental implants"[mh] OR "dental implant*"[tiab]` | `implant` は薬剤のインプラントや胚の着床にも展開される（2026-11-04実測） |
| インプラント周囲炎 | `implantitis` | `"peri-implantitis"[mh] OR peri-implantitis[tiab]` | 綴りの揺れ |
| ブリッジ | `bridge` | `"denture, partial, fixed"[mh] OR "fixed partial denture*"[tiab]` | 一般語の bridge が混ざる |
| クラウン | `crown` | `crowns[mh] OR "dental crown*"[tiab]` | 歯冠（解剖）と補綴装置の区別 |
| 根管治療 | — | `"root canal therapy"[mh] OR "root canal treatment"[tiab]` | 処置名と疾患名を混ぜない |

表は例であり、全ての語の正解を示すものではない。日本語の専門語は、同梱辞書の `lookup_terms.py --direction ja-en` で英語の候補を確かめてよい。検索式に入れるのは英語の用語だけにする。

## 結果に応じた調整（自動では1回まで）

| 状況 | 調整 |
|---|---|
| 0件 | 絞り込みを1つ外す、`[mh]` に `[tiab]` の同義語を `OR` で足す、`[majr]` を `[mh]` に戻す |
| 数千件以上 | 主要概念を `[majr]` にする、`[tiab]` を `[ti]` にする、論文種別や年で絞る |
| `PHRASE_NOT_FOUND` | 綴りを直すか、別の語に替える |
| `BROAD_TRANSLATION` | 歯科の意味のMeSHに替える |
| 結果が質問とずれる | 検索式と方針を示し、利用者に条件を確かめる |

調整した場合は、元の検索式と変えた点を1行で示す。
