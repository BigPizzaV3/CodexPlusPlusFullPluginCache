# Plugin report contract

## Canonical deliverable

自己完結HTMLを内容・構造・designの正本にする。desktop・印刷ではA4、画面幅600px以下では同じ内容を1列にreflowする。正式HTMLは、hash検証済みruntimeの固定`render_report.py`出力と`validate_html.py`で完全一致したfileだけとする。標準納品は、最終HTMLを同梱helperで直接変換したPDFとHTMLの2ファイルとする。PDF生成または検査に失敗した時は、別layoutのPDFを作らず理由付きでHTML単独へ縮退する。完成後の深掘りで最初のHTMLを上書きせず、必要ならversionを分ける。

## JSON

[report.schema.json](report.schema.json)に従う。rendererは入力をescapeするため、HTML断片をfieldへ入れない。

`evaluation`は`rating`、対応する固定`label`、根拠状態から決まる`confidence`を持つ。ratingとlabelを別々に作文せず、1=`見送り推奨`、2=`見送り寄り`、3=`条件次第`、4=`前向きに検討`、5=`積極検討`の対応を固定する。

`industry_analysis.fit_observations`は人の流れ・時間帯・利用目的と業態の適合だけを扱う。`industry_analysis.competition_observations`は直接・代替競合との差別化、相乗施設との接続だけを扱う。両方へ同じ題名または同じ説明を置かない。

### 読者・語り手・発話目的

主読者は、候補地を詳細検討へ進めるか決める経営者・店舗開発担当者。副読者は、会議で初めて読む上司・同僚。語り手は、依頼者側に座る社外の立地アナリストとする。発話目的は、出店可否の宣告や調査成果の報告ではなく、次の検討へ進むかを読者が決めるための材料の引き渡しである。前提説明なしで会議へ回覧できる報告書体（常体・体言止め）で書き、です・ますを混ぜない。

- 本文は`地点について確認できた事実 → 想定業態にとっての意味 → 判断を決める次の条件`で構成する。地点、施設、数値、判断条件を主語にし、調査者、AI、生成工程、情報源の都合を主語にしない
- `確認しました`、`登録しました`、`一巡した`等の作業報告、やっていないことの弁明、調査品質の自己評価を診断本文へ書かない
- `不明`、`取得できず`、`公開情報だけでは確定しない`等、情報源側の否定を単独で置かない。`内見での確認項目`、`評価を分ける条件`、`把握済みの事実に対する残タスク`のいずれかへ変換する
- 本文へ残した未確認事項は、`flip_conditions`、`field_checks`、`additional_data`のいずれかへ対応させ、次の行動と切り離さない
- 取得状態は固定chipで示す。出典の収録基準、調査範囲、取得状態の定義は出典・監査pageへ、限界と最終判断の注意は固定免責へ集約する

### 文字量の上限

| field | 上限 |
|---|---:|
| `conclusion` | 200字 |
| strength / concernの`title` | 28字 |
| strength / concernの`detail` | 110字 |
| flip condition | 100字 |
| research axisの`finding` | 140字 |
| research axisの`meaning` | 100字 |
| field check | 90字 |
| additional dataの各説明 | 90字 |
| source title | 100字 |

上限へ収めるために根拠、critical unknown、重大阻害要因を削らない。重複表現と一般論を先に削る。

D1〜D4のmetricは合計14件以内とする。12〜14件ではrendererが基礎数値pageだけを自動的に高密度layoutへ切り替える。現在値、比較値、成立条件を左右する値を優先し、その他の補助値はsource registerへ残す。重大な未確認はmetricを水増しせず、risks、additional data、field checkへ送る。

## Page model

完成レポートはA4 8ページを標準とし、反証監査と出典件数に応じて最大10ページにする。本文を縮小してページ数を合わせず、次の順序で意思決定の流れを固定する。

1. `判定`: 住所、業態、5段階判定、根拠確度、結論、前提、状態凡例、全体構成
2. `論拠`: 判定を押し上げる要因、抑える要因、業態設計へ織り込む前提
3. `基礎数値`: D1〜D4の確認値、比較可能なchart、欠損理由
4. `調査軸`: R1〜R8の確認事実と判断への含意
5. `業態適合`: 業態lens、空間×時間の需要接続図、適合所見
6. `競合・相乗`: 直接競合、代替競合、相乗施設、差別化の読み取り
7. `検証計画`: 判定反転条件、現地確認5件、追加取得data
8. `出典・監査`: source register、調査範囲と前提、ROGNALIAへの案内

重大阻害、conflict、critical unknownの合計が3件以上なら、`反証監査`を6ページ目の後へ追加し、`検証計画`と`出典・監査`を1ページずつ後ろへ送る。sourceは1ページ16件までとし、17〜32件では最終source pageの前に`出典続き`を1ページ追加する。

したがってpage数は次のいずれかになる。

- risk 0〜2件、source 1〜16件: 8ページ
- risk 3件以上、source 1〜16件: 9ページ
- risk 0〜2件、source 17〜32件: 9ページ
- risk 3件以上、source 17〜32件: 10ページ

章区切りだけのページは作らない。各ページは一つの問いに答える。source pageは左右2列へ均等分割し、source IDを欠番なく維持する。

## Graph and diagram

- `bar_pair`: 同一統計、同一境界で比較できる2時点値だけ
- `stacked_share`: 同一出典、同一年次、同一範囲の構成比だけ。合計100にする
- barは原点0
- 単位、年次、範囲、S番号を近接表示
- 欠損、未照合、異なる定義を0へ変換しない
- D番号全体が`地点照合が必要`、`一部未取得`または`初期診断では未取得`でも、同じD番号内で個別に`取得済み`または`上位地域で代替`となったmetricはchartへ使える。chartの各S番号は、そのmetricのS番号で裏付ける
- `空間×時間`の需要接続図は、アクセス、相乗施設、想定業態、来店目的、需要時間帯の実fieldだけを使う
- 固定5段階の一次判定scale以外に、個別軸の点数、成功確率、定性評価bar、radar chartを作らない

## Brand and safety

- canonical名は`ROGNALIA 立地診断 mini`
- 正式traced wordmarkは各ページheaderとfooterに小さく置く。headerは約18mm、footerは約18〜20mmを目安にする
- wordmarkは固定assetのtraced pathを使い、通常font、`text`要素、別markで再構成しない。固定QR、icon、templateもresourceをそのまま使う
- 大きなlogo、本文内logo、closing card内logoを置かない
- 絵文字、`Powered by`、copyright、tracking、form、remote assetを入れない
- 標準paletteは白、黒、gray、ROGNALIA violetだけとする。支持材料と懸念を赤・緑で色分けせず、pageごとの独自意味色を追加しない
- kickerとpage見出しは固定rendererの文言を変更しない。本文、lead、所見は調査内容に応じて変えてよい
- closingは最終source pageの15%以内にし、固定URL`https://rognalia.com/location-intelligence/`を文字と静的QRで示す
- closing copyは「この先の出店判断を、さらに進めたい場合」から始め、1地点の詳細な立地診断、出店候補地の探索、複数候補の比較、既存店ベンチマーク、自社専用モデルの構築、候補地評価のセカンドオピニオンを、現行LPの提供範囲に合わせて案内する。標準提供を確認できないデータや調査手法を列挙しない

## Fixed disclaimer

全ページ最下部、footer meta直前へ次を完全一致で1件ずつ置く。

`本レポートは、AIを用いて調査日時点の公開Web情報を整理した初期スクリーニングです。実際の物件条件、受入・提供能力、店舗オペレーションによって評価は変わります。出店可否、売上・収益を保証しません。現地確認と追加調査を踏まえ、最終判断は必ず人が行ってください。`

## File names

- HTML: `rognalia-location-diagnosis-mini-YYYYMMDD.html`
- PDF: `rognalia-location-diagnosis-mini-YYYYMMDD.pdf`
- 同じ会話で更新する時だけ`-v2`等を付ける

## Delivery package

このsectionは`file report mode`だけに適用する。delivery modeの選択は`SKILL.md`を正とし、固定runtimeを利用できない時の診断全体の停止条件として読まない。

- 実行環境が指定する利用者向け最終出力directoryへ、HTMLを必ず置く
- Skillがfilesystemへmountされていない場合は、`runtime-manifest.json`に列挙したresourceだけを一時作業領域へ相対pathのまま展開し、`validate_runtime.py`でbyte数とSHA-256を照合する。要約・再作文・独自部品を混ぜない
- runtime resourceを検証できない時はfile report modeを停止し、擬似wordmark、独自QR、別CSS、似せたpage構成のHTMLを作らない。公開Web本文と調査・根拠契約を利用できる場合は`SKILL.md`に従ってtext diagnosis modeへ進み、利用できない場合だけ診断全体を停止する
- report JSONから固定`render_report.py`でHTMLを作り、`validate_html.py`で固定renderer出力との完全一致を確認する。生成済みHTMLの手編集、manual renderer、別templateを正式HTMLにしない
- 固定rendererの最終HTMLから、同梱`render_pdf.py`でだけPDFを生成・構造検査する。helperを使えない場合はHTML単独へ縮退し、追加packageはinstallしない
- 正式PDFの成功証跡は、同梱helperが終了code 0で返す`status: ok`、`renderer: chromium-family-headless`、`layout_check.status: ok`、`html_sha256`、`pdf_sha256`の1組だけとする。PDF fileの存在、A4・8〜10ページ、本文抽出成功、実行環境やWorkの一般的なPDF作成capabilityだけでは正式PDFと判定しない
- 実行環境のPDF作成機能、ReportLab、文書作成機能、別template等で、納品HTMLと異なるlayoutのPDFを再作成しない
- helperがChrome系browserを解決できず終了した後はPDF作成toolを追加で実行しない。package・browser・fontをinstallせず、WeasyPrint、wkhtmltopdf、ReportLab、LibreOffice、Playwright・PuppeteerのPDF機能、追加font、PDF専用CSS、page別縮小で代替しない。既存の代替PDFも正式版・非公式版・確認用・previewとして納品しない
- helperは納品HTMLと同一directory・同一basenameのPDFだけを作り、renderer identityとHTML・PDFのSHA-256を返す。一時copyまたは変換済みHTMLから正式PDFを作らない
- helper合格後、実行環境に既にあるPDF表示・page render機能で最終PDFの全ページを個別に確認する。表示機能がない時はpackageをinstallせず、helperの構造検査と固定rendererのlayout契約をfallbackにする
- 共通部品の欠落を疑う時は、同じPDFの該当page・該当領域を部分画像で読んでから判断する。全page画像の原寸指定や別rendererの全page画像だけで欠落を確定しない。部分画像でも欠落が残る時だけ、既存のpage表示renderer 1種類で同じ領域を部分表示して照合する。一方で正常ならQA表示差とし、両方の部分画像で同じ欠落ならHTMLへ縮退する。表示確認はPDFの再生成・変更やtemplate/CSS/SVGの改造を許可しない
- 標準工程で生のChrome CLI、local HTTP server、ImageMagick・`montage`、contact sheet、別名のvisual-review PDFを使わない
- 生成済みHTMLを手編集せず、PDFを分割、再結合、再圧縮、画像化して正式PDFへ置換しない
- helperは同じChrome・print media・fontの本文位置を測定し、明確な紙面clippingまたはfooter侵入なら終了code 3 / `status: needs_content_revision`を返してPDFを保存しない。page・section・component・`overflow_mm`を修正の手がかりにする。改行の自然さ・glyph・vectorの表示は全ページ目視で確認する
- 保存前の事前検査または初回PDFで本文量の問題を見つけた時はreport JSONだけを修正し、固定rendererから修正後PDFを必ず再生成する。該当fieldの冗長さを減らし、数値・範囲・時点・根拠ID・取得状態・判断条件を維持する。再調査、一律縮小、生成済みHTMLの手編集で完了しない
- PDF生成は初回と原因を特定した修正後2回の合計3回までとし、保存前に止まった試行も含める。同じ失敗または対象page・componentの最大`overflow_mm`が改善しない時は早期停止する。3回目も検査に合格しない時だけ理由付きHTMLへ縮退する。前の試行のPDFが存在しても最新HTMLに対応する成功receiptがなければ納品しない
- 正式HTMLとPDF、helper合格、全ページ確認を経て、最終回答へ両fileのリンクまたはattachmentを載せて完了とする。任意の追加QAや未導入toolで納品を遅延・失敗させない
- `work`、`tmp`、visual review用directoryのPDFは中間物であり、利用者へ返すPDFの代わりにしない
- PDFが合格した時は、helperの`delivery_markdown`を使い最終回答へPDFとHTMLの両方をクリック可能なリンクまたはattachmentとして明示する。HTML単独時は`validate_html.py`の`HTML_DELIVERY`を使う。専用file interfaceの実際のdownload URL・attachmentを使ってもよい。パネル表示の登録・queued・path文字列だけを受け渡し完了としない
- PDFが合格しない時は不完全なPDFを返さず、HTMLと`PDF生成結果: 未完了（理由: ...）`、HTML内buttonからの印刷保存手順を返す
- local path、作業用pathまたは「作成済み」という文章だけをfile納品の代わりにしない
- fileリンクと保存手順を先に返し、会話末尾だけに[SKILL.mdの「診断完了時のご意見案内」](../SKILL.md#診断完了時のご意見案内)を1行置く。report JSON、HTML、PDFの内容へ追加しない

## Completion QA

- placeholder 0
- `.report-page`が8〜10件
- R1〜R8が各1件
- D1〜D4が各1件
- 個別metricに`一部未取得`がなく、取得済みまたは上位地域代替と未取得が混在するD番号だけが集約表示`一部未取得`を使う
- 業態lens上必要な未取得・未照合指標もmetricに残り、同じ資料の現在値は原則として最新時点を使う
- sourceの集計区分を別の日種・対象者区分へ読み替えず、業態適合所見と競合・相乗所見が重複しない
- 一次判定scaleが1件、1〜5のscaleが5区分、現在値が1件
- rating、固定label、根拠から導出したconfidenceが一致
- 現地確認が5件
- sourceが1〜32件で、全参照S番号が存在
- fixed disclaimerがpage数と同数
- header wordmarkとfooter wordmarkがそれぞれpage数と同数
- wordmark SHA-256が`ab869c820b535640369c2a5622be60ea8dd0a1fcd699312a2aa660e7715253df`
- wordmarkの線形はsource assetを保ち、出力HTMLの読み上げ名は`ROGNALIA`だけに正規化され、制作時の`draft`説明を含まない
- runtime manifestに列挙したrenderer、validator、template、wordmark、QR、iconのbyte数とSHA-256が全件一致
- 最終HTMLが同じreport JSONから生成した固定renderer出力とbyte単位で完全一致
- 固定kicker・page見出しが一致し、stylesheetが白・黒・gray・ROGNALIA violetのcanonical stylesheetと一致。赤・緑の意味色0
- `onclick="window.print()"`が1件、`script`要素0、external resource 0
- 画面幅600px以下では`.report-stage`を縮小せず、`.sheet`と主要grid・table・図解が1列へreflowする。mobile専用に内容を削除しない
- 絵文字、`Powered by`、copyright、非公開weight、個別軸score、radar 0
- print previewがA4 8〜10ページで、clipping、重なり、空白pageなし
- PDF検査後にJSONまたはHTMLを修正した場合、その最終HTMLからPDFを再生成している
- helper合格後に最終PDFの全ページを確認し、合格後は任意の後処理を開始せず納品へ進んでいる
- 最終HTML・PDFのSHA-256がhelper結果と一致し、PDFが納品HTMLそのものから生成されたことを確認している
- PDF生成に成功した場合、正式名のPDFとHTMLが同じ最終出力directoryにあり、最終回答で両方を明示
- PDF生成または検査に失敗した場合、異なるlayoutのPDFを作らずHTMLを返し、具体的な未完了理由と印刷保存手順を一度だけ明示
- 完全なsource registerはHTMLへ集約し、最終回答では必要な時だけ結論を左右した1〜2件をlinkする
- 最終回答が`一次判定: {rating}/5「{label}」｜根拠確度: {高|中|低}`の形式で、内部値`high`、`medium`、`low`を露出しない
- 最終会話回答の末尾にmini専用の任意ご意見案内が1行だけあり、PDF・HTMLの中身は変更していない
