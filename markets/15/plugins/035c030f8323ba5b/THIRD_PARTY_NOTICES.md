# 用語データの出典と利用条件

Courtesy of the U.S. National Library of Medicine.

英語のMeSH由来の見出し語・同義語・識別子は、NLMのMeSH 2026 XML（2026年10月24日取得）を参照しています。最新版を常に反映する保証はありません。

- 公式配布：https://nlmpubs.nlm.nih.gov/projects/mesh/MESH_FILES/xmlmesh/
- MeSH専用利用条件：https://www.nlm.nih.gov/databases/download/terms_and_conditions_mesh.html
- NLM一般データ利用条件：https://www.nlm.nih.gov/databases/download/terms_and_conditions.html

NLMの利用条件は、出典の明示、NLMの推薦・承認を示唆しないこと、最新性についての注意または使用版の表示などを定めています。NLMはデータの正確性・完全性等を保証せず、利用結果に関する免責条件を設けています。利用時にはリンク先の全文を確認してください。

MeSH Translation（MTMS）ファイルは、MeSH英語データの利用条件ではカバーされません。本パッケージではMTMSや第三者の日本語MeSH辞書を取り込んでいません。日本語訳は、元の自作対訳をもとに独自に編集したものです。今回追加した臨床・研究用語の訳語も独自編集であり、NLM公認の日本語訳ではありません。

NLMは本プラグイン・日本語訳・サービスを推薦・承認していません。本表記は出典の案内であり、NLMデータを運営者独自のライセンスへ変更するものではありません。

## 独自補助語の選定に参照した資料

以下の資料は用語の対象・臨床的な区別・研究報告で必要な観点の確認に用いました。本文・対訳辞書・図表は同梱していません。

- EFP歯周・インプラント周囲疾患分類・診療指針：https://www.efp.org/publications/projects/new-classification/
- AAE診断用語：https://www.aae.org/specialty/wp-content/uploads/sites/2/2017/07/aaeconsensusconferencerecommendeddiagnosticterminology.pdf
- CONSORT 2025：https://www.bmj.com/content/389/bmj-2024-081124

これらの団体による推薦・日本語訳の公認を意味しません。

## 同梱する辞書と編集者

日本語対訳・臨床補助語の編集と確認：渡部準也（JUNYA WATANABE）。

運営者確認済みの基本667項目と、以前の基本から参照へ移した運営者確認済み90項目を利用します。日本語訳・コメントの確認結果と、運営者が指定した「形成」「生活断髄法」「生物学的幅径」「骨縁上組織付着」「サイナストラクト」、部分義歯の訳し分けを引き継いでいます。確認の対象は訳・表記の運用で、全ての英語別名や逆方向の自動変換を承認したものではありません。

基本35件・参照4件の計39件の略語指定を保持しています。MTA・BOP・QOL等の初出用正式日本語は既存草案から別フィールドに補ったものを含み、運営者による正式名の個別入力とは区別しています。

選定・表記の確認には文部科学省の歯学教育モデル・コア・カリキュラム、各専門学会の公開用語資料や診療資料、臨床論文を参照しました。学会用語集の一覧・定義文や論文抄録全文を本パッケージに転載していません。辞書が臨床論文全体に必要十分であることや、用語の使用頻度、学会監修を証明するものではありません。

- 歯学教育モデル・コア・カリキュラム：https://www.mext.go.jp/content/20230428-mxt_igaku-000029086_1.pdf
- 日本歯科医学会 学術用語集の案内：https://www.jads.jp/publication/yougo/
- 歯内療法学専門用語集・公開用語一覧：https://www.hozon.or.jp/member/publication/glossary/file/glossary_endodontics2023_term.pdf
- 日本歯周病学会 追加用語：https://www.perio.jp/publication/upload_file/Glossary_List_2019_addition.pdf

元の全件母集団、未確認の分野別候補7,022項目、保管索引27,520項目は作業元に保存し、本パッケージには同梱していません。利用時には本文の定義・対象・測定法を確認し、関連語を厳密な同義語として一括置換しません。以前の資料の「本論文」「本研究」という用語メモも、今回の入力を確認した事実とは扱いません。

## 論文検索のデータ（PubMed）

Courtesy of the U.S. National Library of Medicine.

論文の検索と論文情報の確認は、米国国立医学図書館（NLM）の国立生物工学情報センター（NCBI）が提供するE-utilitiesを通じて、PubMedのデータを取得します。NLMは本プラグインを推薦・承認していません。データは確認日時点のもので、最新・完全であることは保証されません。

- NCBIのWebサイト・データの利用方針、免責・著作権：https://www.ncbi.nlm.nih.gov/home/about/policies/
- NLMデータの利用条件：https://www.nlm.nih.gov/databases/download/terms_and_conditions.html

PubMedの抄録について、NLMは著作権を主張していませんが、出版社・著者が著作権を持つ場合があります。運営者の検索用サーバーは英語の検索語・PMID・DOIだけを受け取り、検索式を保存しません。詳しくはプライバシーポリシー（https://plugins.dentalgenai.com/privacy/）をご確認ください。
