---
name: lp-image-builder
description: 配布プラグインの承認済みLP構成から完成セクションPNGを制作し、依頼時に既存Webへ配置する。構成未承認ならlp-structureへ。一般の画像生成・HTML/CSS再構築・分析だけは対象外。
---

# LP Image Builder

承認済み構成を、完成セクション画像の連続として実装する。これはpixel-perfectなコード再構築ではない。承認画像そのものを表示し、静的な見た目とコピーをHTML/CSSで作り直さない。

## 週次で選択した既存LPの改善

週次依頼の識別情報がある場合は、新規画像LPへ作り直す前に [おまかせ制作の週次LP改善手順](../marketing-omakase/SKILL.md) を読む。対象がWeb版なら編集可能なソースと既存Web改善runを引き継ぎ、既存の版管理・確認を使う。新規LP用の構成承認や画像工程を一律に再開しない。

## 適用範囲

「承認済み構成」「直前構成にOK」「このまま進めて」「画像にして」「デザイン作って」は、直前のLP構成の承認が確認でき、完成画像LPを求める場合だけこの入口で扱う。

配布プラグインで承認済み構成から完成画像LPを制作する段階の主担当。構成・コピーの新規設計は兄弟スキル、画像の制作・レビューと依頼された既存Webへの配置は本スキルが担当する。

一般の画像生成、編集可能なHTML/CSSによる見た目の再構築、分析・提案だけの依頼では起動しない。「OK」「画像にして」だけでLP制作と判定せず、直前のLP構成・承認範囲を確認する。既存Webコードだけの修正依頼を新規の画像LP制作へ拡張しない。

このスキルは配布パッケージ内の資料だけで利用する。個人環境の非公開スキルを参照しない。編集元は `mymarketer-codex-plugin/plugins/mymarketer/skills/`、インストール済みコピーは編集しない。

## Optional MyMarketer quality connection

既に利用可能な無料共通チェックが今回の判断に関係する場合、またはユーザーが有料AI審査を明示依頼した場合だけ、[任意のcreative check契約](references/creative-core-contract.md)を読む。新接続は本番未提供の開発候補であり、未接続時のローカル品質ルール・承認・非保存の標準工程はそのまま維持する。

この接続は **read-only by default / explicit save only** とする。

取得したpreviewの完全な`context`が同じrun・接続・案件・fingerprintで利用でき、後続toolの公開schemaが対応する場合だけ、guidanceとrubricに`contextMode: "reference"`を渡す。`contextReference.fields`はそのpreviewの`context`から解決し、条件が空になったとは解釈しない。schema未対応なら引数を省略する。文脈が失われた場合はpreviewを最大1回再取得し、復元できなければ無料モードへ戻す。`CONTEXT_TOO_LARGE`は再試行や旧ツールで回避せず、有料文脈を捨て、共通ポリシーの容量超過1行を表示する。重要な判断・禁止事項の切り捨てや、情報不足のまま品質連携済みとすることは避ける。

作業前に [共通の接続品質ポリシー](references/connected-quality-policy.json) を読む。MyMarketerの`/mcp/quality` read接続と`quality_preview`が利用可能だと確認できない場合は、接続やログインを要求せず、利用不能ツールを試さず、ローカルSkillだけで完結する。

有料read接続済みの場合だけ、`listProjects`で承認済み構成の案件を一つに確定し、`prepareMarketingJobPreview(deliverableType=landing_page_visual)`で案件文脈と`contextFingerprint`を取得する。同じfingerprintを`getProductionGuidanceInputs`と`getDeliverableReviewRubric`へ渡す。ChatGPTが3方向を作り、ユーザーが1方向を選び、制作後にrubricで非表示自己採点し、不合格時だけ最大1回改稿して再採点する。`CONTEXT_CHANGED`なら文脈から再取得する。上流の目的、CTA、claim境界、承認済み判断は変更しない。

通常の品質工程では旧`persistence`引数付きツールを使わない。完成稿の案件保存をユーザーが明示した場合だけ`saveDeliverableV1`を使い、必要なら`mcp:write`の追加同意へ進む。OAuthのwrite権限は個別操作の承認ではない。施策提案、意思決定、学び、公開、配信、課金操作も、その都度ユーザーの明示確認後だけ行う。実績値が届く前に成果や学びを作らない。

接続、契約、権限、案件、予算のいずれかで失敗したら、そのrunの有料文脈を破棄して再利用せず、MyMarketer情報を推測しない。ポリシー所定の「有料品質ループ未適用」1行だけを表示し、無料モードで続ける。未接続で最初から無料モードの場合はこの失敗表示も出さない。

開始前に [references/direct-image-contract.md](references/direct-image-contract.md) を読む。`OK` など範囲を省略した返答は、直前に提示した成果物と明示したscopeだけを承認したものとして扱う。

元の望む結果は承認済み構成書の目的・主要CTAとその根拠から継承し、このスキルで聞き直さない。信頼できる元の結果を継承できない場合は推測せず、完了時の個別推奨を出さない。

構成が未承認・不明、または直前の承認対象を一つに特定できない場合は画像制作を始めない。兄弟スキル [../lp-structure/SKILL.md](../lp-structure/SKILL.md) を先頭から末尾まで完全に読み、構成設計とscope `lp-structure`の承認から進める。ユーザーにスキル名の指定や別スキルの呼び出しを求めない。直前の構成へのgenericな`OK`はその構成だけを承認できるが、FV候補の選択には使わず、候補提示後の別turnでexact candidate IDを一つ要求する。

構成schema 1.6の[出典と承認範囲](../lp-structure/references/skill-contract.md#source-and-approval-scope)を継承する。画像制作には`full_structure`の別turn承認が必要で、部分承認や一般的な草案へのOKを全体承認にしない。明示して承認された仮説デザインは上流原文が未確認でも制作でき、推定という出典を保持する。`href: null`は画像制作を止めないが、クリック可能なassembly前に根拠と一致するURL/pathと更新した承認bindingを要する。

## Entry gate

次が一つでも欠ければ停止する。

- 一つのschema 1.6 JSON構成書、そのJSONから決定論的に生成されsource path/hashへbindされたMarkdown approval view、そのpath/hashをsubjectとして固定するapproval artifactがある。JSONだけがauthorityであり、view driftは停止する。新規制作ではschema 1.6の`fv_handoff.fv_content_budget`を必須とし、structure schema 1.1〜1.5とworkflow schema 1.1〜1.4は既存成果物の従来の検証・表示を保持し、新規制作移行はstructure 1.6＋workflow 1.5を使う。構成書には順序どおりのN-1境界計画と、該当時の反復シリーズ計画がある。ユーザー/controllerがreceipt bytesを提供した場合はexternal receiptを使う。会話で明示承認した場合は、decision提供者とmodel recorderを区別するconversation approval recordを作る。
- セクション順と全逐語コピーが確定している。
- 最終assemblyを依頼している場合は、編集対象の既存Webプロジェクトと対象ルートが特定されている。
- host/sessionの画像生成またはユーザー提供の完成画像を利用できる。どちらも利用できなければ停止する。

未承認・欠落画像を理由に、HTML/CSS/JS/TS/TSX/React、browser screenshot、hybrid、code-native、decompositionへ切り替えない。

schema 1.5では、authentic proofのcustomer-face → handwritten-feedback → verified-fallback順を守り、顧客素材はsource/permission/privacyへbindする。direct-callは主CTAを置き換えないoptional secondaryであり、enabled時だけexact `tel:`、受付copy、tracking marker、44×44px以上のmobile geometryをtransparent overlayで検証する。page continuityとwhole-page reviewは承認済みsemantic/copy/visual/layout bridge planをexactに保持し、矢印をbridge本体にしない。

## Workflow

1. [references/workflow-state.template.json](references/workflow-state.template.json) からstateを作る。stateファイルは専用`artifact_root`の外へ置き、構成書、approval record、画像、review、manifest、assembly後のruntimeをそのrootだけに置く。`artifact_ledger`はroot配下の再帰的な全ファイルを相対path/hashで過不足なく列挙する。構成書JSONからセクションIDと順序を抽出し、コピー、主張、順序を変更しない。各phase移行前に次を実行する。

```bash
python3 scripts/validate_workflow_state.py /path/to/workflow-state.json --project-root /path/to/project
```

2. CTA、form、map、accordion、video、linkのうち実際に操作が必要なものだけをoverlayとして列挙する。CTAの完成ボタンと逐語ラベルは画像へ焼き込み、runtime CTAはその上のtransparent interactive hit areaだけにする。その他overlayもinteractive-onlyとし、provider identity、proof、hierarchyなどの静的要件をruntime overlayだけで補わない。
3. 最初はFVだけを独立した完成PNGとして1 batchちょうど2案制作する。候補は別path/hashを持つ実寸幅390px・高さ600〜900pxの完成デザインで、provenanceはそのturnで実際に呼び出したhost/session image generationのinvocation/result asset ID、または実際のユーザー添付のmessage/attachment IDへ結ぶ。bare enum、手書きの生成主張、過去rasterのrelabelをsource evidenceにしない。candidate hash、source evidence、ledger、presentationを記録する前に、各source PNGを `python3 scripts/normalize_candidate_png.py source.png candidate-01.png` でpublic 8-bit non-interlaced RGB/RGBA subsetへ正規化し、正規化後bytesだけをcandidateとしてbindする。source evidenceのhost/user referenceは保持するが、`source_sha256`は正規化後candidate bytesへbindする。特定のprovider/tool、レイアウト、被写体、左右、色、badge数、named styleを制作手順として固定しない。
4. [references/fv-creative-comparison.template.json](references/fv-creative-comparison.template.json) を使い、実際にsession内で各候補画像を表示・観察する。各候補について承認済みbudget profile、全visible item IDの同順inventory、観察した非空白文字数/item数/proof数、`no_unplanned_text: true`と空の`unplanned_visible_text`を記録し、budget内容とdigestをcomparisonへ固定する。90/140/180字等はpre-generation guardrailであり、final hard gateは390px実寸のsource-message/offer/action一致、scan outcomes（relevance / what-it-is / core benefit / trust basis / next action。copy/visual/proof/CTAのどれで答えてもよい）、主CTA一つ、H1最大3行、support最大4行、CTA 1行、nonuniform squeeze/condensed/clip/overflowなしである。候補IDは`candidate-01`のようなexact safe tokenにする。全候補の実pixelを順番どおり含むcandidate presentation PNGを作り、全candidate binding/provenance、reviewer input hashes、全pairの具体的なmaterial-difference axes、provider identity、belief/proof/actionの逐語可視証拠と位置、message-image alignment、読み順と位置、copy readability、generic substitutionの具体観察を中立に記録する。両inspectionは`selected: false`、`rejection_reason: null`、comparisonはschema 1.2の`selection_status: pending`とselected ID/context/approvalをnullにする。candidate image/provenance、selection専用のselected/rejectionを除くinspection、material difference、presentation、structure/budget/batch/validator scopeのcanonical selection-neutral projectionをSHA-256化し、`pending_comparison_sha256`としてcomparison、workflow state、current batch historyへ同じ値を固定する。batch固有のpending comparison pathと、`artifact_root`外の別workflow-state pathへschema 1.5 `fv-selection-pending` snapshotを書き、どちらも後続で上書きしない。closed-world ledgerと`fv_batch_history`の`selection-pending`を完成させ、そのpending state単体をvalidatorへ通した直後にhost/skillがstate pathと実bytesのSHA-256を記録する。この値はユーザーに管理させない。bound comparisonの全候補をユーザー/controllerに見える形で提示し、candidate IDを明記して、ここで必ず **END TURN** する。section image、FV review、continuity、assemblyはこのphaseで禁止する。同じturn内のmodel判断・model-authored receipt・genericな`OK`から選択を推定して進めない。後続turnでは新しいstate/comparison fileを作り、`fv_transition`へfrozen pending state/comparison/digestをbindし、hostが元pending fileと保存済みSHAを明示した`--prior-pending-state`＋`--prior-pending-state-sha256`付きvalidatorを通す。validatorはcurrent stateのbindingより先にcaller SHAと実bytesを比較するため、current state内とprior fileを含むhash/receipt/ledger/digestを全再計算しても元snapshotを再定義できない。exact candidate ID tokenが一つだけ明示された場合だけselection専用flags/reasons/context/approvalを加えて`fv-review`へ遷移する。selection subjectはprior pending-state binding、pending comparison binding/digest、presentation、全candidate hash、selected ID/hash、別turnのmessage IDsと逐語decisionを含む。逆候補のIDや曖昧な複数tokenは拒否する。validatorは宣言されたidentifier/hash/bindingと証拠完全性だけを検証し、identifierの著者性やaesthetic pixel truthを認証しない。
5. [references/fv-outcome-review.template.json](references/fv-outcome-review.template.json) でcreative comparison、selected observations、budget内容/digest/観測inventory、source/shown/selectedの完全一致、quality result、全outcome、`generic_substitution_risk: pass`を固定する。providerがvisibleなら正確なname、belief/proof/actionの逐語表現、3段階以上の観察済みhierarchyを欠かさない。source image自体にCTAラベルを含め、`visible_action_label`を承認済みnext actionと完全一致させ、blank plate、runtime-only label、visible duplicateをpassにしない。その後、comparisonもsubjectへ含めたscope `lp-fv-direction` のユーザー/controller明示承認を受け、stateを `fv-direction-approved` へ進める。schema 1.1/1.2/1.3の既存reviewはread-only continuityとして変更しない。
5a. ordered `fv_batch_history`に初回batch 1を必ず保持する。初回2案の後に許すのは、別turnでユーザー/controllerが明示的に求めたrevision batch 1回（再びちょうど2案）だけとし、batch 1のfrozen pending state/comparisonを保持したまま、別revision-outcome comparisonへ`revision-requested`＋request message ID/逐語requestを記録する。scope `lp-fv-candidate-revision` receiptは元pending state SHA/path、pending comparison binding/digest、request message ID/textをsubjectにする。batch 2 contextを同じreceiptへbindし、batch 2の提示時にも別pending state/comparisonをfreezeしてEND TURNする。この経路ではbatch 1のcandidate selectionやselection receiptを捏造しない。選ばれたbatchは`selected`＋既存のexact candidate ID approvalへbindする。過去pending state/comparison/candidates/path/hashをledgerから消す、上書きする、batch 2で再利用することを禁止し、batch 3を作らない。2案とも同じdensity/structure理由でfailした場合は候補再生成を止め、`lp-structure`へ戻って`fv_content_budget`を修正・再承認する。見た目だけを変えて同じ過密copyを再投入しない。
6. FV承認後、section 02以降を作る前に [references/page-continuity-plan.template.json](references/page-continuity-plan.template.json) を作る。ページ共通のvisual system、band rhythm、構成書の全N-1境界、反復シリーズの全memberとrecognizable cue invariantを固定する。copylessなvisual/layout/open-loop/contrast遷移を合格経路として扱い、transition copyを各sectionの定型文にしない。装飾矢印だけの遷移は不可とする。
7. page continuity planのpath/hashをsubjectにしたscope `lp-page-continuity` の明示承認を受け、stateを `page-continuity-approved` へ進める。この承認がない状態でsection 02以降を生成しない。
8. continuity承認後だけ、host/session image generationによる全面再生成または新たなユーザー提供完成画像から、残りの各セクションをそれぞれ独立した完成PNGとして制作する。full-section raster compositionや局所修正は新規schemaで使わない。各画像は [references/finished-image-source-evidence.template.json](references/finished-image-source-evidence.template.json) の該当するnested shape一つだけをsource evidenceファイルとして使い、source hashへ結ぶ。bare enumや既存rasterのrelabelを受け入れない。全PNGを実寸幅390pxに統一し、whole-page cropやscreenshotをsection画像にしない。
9. 全section PNGを順番どおり隙間なく縦積みしたwhole-page review PNGを作る。さらに [references/whole-page-review.template.json](references/whole-page-review.template.json) で、全N-1境界のsemantic seamとvisual seam、全sectionの日本語text fit、全反復シリーズのidentity continuityをレビューする。どれか一件でも欠ける／failなら承認へ進まない。
10. text fitは390px原寸で測る。FVはH1最大3行、support最大4行、主CTAちょうど1行をhard gateとする。nonuniform glyph scaling（glyphの部分的・非均一scale）、condensed-to-fit、clipping、overflowを禁止し、body 16px以上、supporting textがある場合14px以上、line-height 1.4以上を要求する。FVが900px内に収まらなければ高さを増やさず構成へ戻ってbudgetを修正・再承認する。section 02以降だけはsection heightを増やす、装飾を減らす／移す、sectionを分割して再承認する。文字を潰して収めない。
11. whole-page PNGはsection bytesから派生するreview-only成果物であり、FVやsectionのデザインsourceにはしない。各画像のpath、SHA-256、390×height、alt、accessible summary、overlay領域も示す。approval-bound whole-page reviewにもFVのexact image hash、H1/support/CTA行数、主CTA一つ、squeeze/clip/overflowなし、source-message/offer/action一致、全scan outcomeと実際のevidence modeを保持する。standalone manifest validatorもこれを必須検証し、workflow comparisonを省略したassemblyだけの実行でhard gateを迂回させない。validatorは宣言されたplan bindingとレビュー完全性を検証するが、pixel-levelの視覚的真実を自動証明しないため、実寸PNGの人間/controllerレビューを省略しない。
12. 次のtradeoffと、continuity plan、そのapproval artifact、whole-page review、whole-page composite、画像・dimensions・loading・alt/summary・全overlayを含むcanonical assembly digestを明示する。ユーザーまたは外部controllerから、そのdigestをsubjectとする明示承認を受ける。外部receipt bytesがなければ、同じtruthful conversation approval recordを作る。決定自体をmodelが行わない。
   - 画像内コピーは検索エンジンや支援技術が本文として読めない。
   - コピー、価格、法務表記、レイアウトの変更には画像再生成が必要。
   - 画像はHTML主体より重くなりやすい。
   - accessible summaryは内容の要約であり、画像内逐語コピーの完全な代替ではない。
13. [references/direct-image-manifest.template.json](references/direct-image-manifest.template.json) を埋め、次を実行する。

```bash
python3 scripts/validate_direct_image_manifest.py /path/to/direct-image-manifest.json --project-root /path/to/web-project
```

14. stateとfinal manifestがPASSし、外部assembly approvalを得た後だけ既存Webプロジェクトへ組み立てる。画像は承認時と同一bytesのままroute-owned assetsへ置き、section順にplain image要素で表示する。各imageにはmanifestどおりの`data-lp-section-id`と`data-lp-section-order`、各overlayには`data-lp-overlay-section-id`、`data-lp-overlay-index`、`data-lp-overlay-kind`を付ける。runtime sourceはmanifestの全section image pathを同じ順序で明示的に参照する。文字列を未使用定数やcommentへ置いただけの空routeを完成扱いにしない。
15. 320/390/430pxで実際のrouteをbrowser QAし、DOM image順、実pageが取得したimage Response bytesのhash、可視かつ正のgeometry、390px intrinsic width、隙間、横overflow、crop、overlay marker/count/label/bounds、altと`aria-describedby` summaryを確認する。再fetchしたURLのbytesで代用しない。未focus状態のCTA overlay本体と`::before`/`::after`に文字、visible descendant、background、border/border-image、shadow、nontransparent outline、filter、maskなどのpaintがないことも確認する。keyboardの`:focus-visible` outlineは保持する。`content-visibility: hidden`、透明paint、未承認coverをrejectし、scroll後の`elementsFromPoint`複数点paint sampleでimageまたはそのsectionの承認overlayが意味のある過半を占めることを確認する。キーボード操作とリンク先も人間/controllerが確認する。
16. [references/runtime-assembly-map.template.json](references/runtime-assembly-map.template.json) で正規化した`base_origin`、route、manifest hash、全runtime source path/hash、全section mappingを固定し、[references/runtime-browser-qa.template.json](references/runtime-browser-qa.template.json) でも同じoriginと3 viewportの結果、`validator_scope: bound-evidence-not-live-browser-truth`を固定する。portable contractでは`base_origin`をcredentials/path/query/fragmentなしの`http://127.0.0.1:<explicit-port>`または`http://localhost:<explicit-port>`だけに限定する。remote QAが必要なら停止し、将来の明示契約で再承認する。base originを含むsource/map/QAの全bindingをsubjectにしたscope `lp-runtime-assembly` の明示承認を受け、stateの`runtime_assembly`へapproval artifactもbindしてからphaseを`assembled`に進める。assembledの最終検証はcaller projectからPlaywrightとbrowserを利用できる状態で、実際にserve中の承認済みoriginを指定して実行する。依存またはbrowserがなければfail closedとする。

```bash
python3 scripts/validate_workflow_state.py /path/to/workflow-state.json --project-root /path/to/project --prior-pending-state /path/to/project/workflow-fv-batch-01-pending.json --prior-pending-state-sha256 <host-recorded-64-hex-sha256> --runtime-base-url http://127.0.0.1:3000
```

CLIの`--runtime-base-url`は承認済み`base_origin`と完全一致しなければならない。protocol-relativeな`//...` route、backslash、redirectを含むroute/origin driftはrejectする。validatorはread-onlyの [scripts/probe_runtime.mjs](scripts/probe_runtime.mjs) を実行し、その時点で観測したlive resultが承認済みQA JSONと完全一致することを検証する。これは将来もrouteが同じ状態であること、視覚的意味品質、暗号学的identityを証明しない。release前の実browser QAと人間/controller確認を省略しない。

## Assembly rules

- 各section PNGはwidth属性390、実height、`display: block; width: 100%; height: auto`で並べる。画像間のmargin、gap、line-height由来の隙間を0にする。
- FVだけをeagerかつ高優先度で読み込み、2枚目以降はlazyにする。
- 390pxでは原寸、320pxでは比例縮小、430pxでは390px列を中央配置する。画像をトリミングしない。
- 各画像に簡潔なaltと、`aria-describedby`で関連付けたaccessible summaryを付ける。summaryはscreen-reader向けにしてよいが、静的な逐語コピーを可視HTMLとして重ねない。
- HTML/CSS overlayは `cta`, `form`, `map`, `accordion`, `video`, `link` だけに限定する。CTAは画像内の完成ボタンと同じ領域へ透明hit areaを置き、可視ラベルやplateを重複表示しない。その他はinteractive-onlyとする。
- 既存プロジェクトのrouting、security、tracking、form処理を再利用する。外部送信、公開、deployは別途明示承認がない限り行わない。
- 承認済み画像を最適化、再圧縮、色変換、リサイズしてbytesを変えない。

## Stop conditions

phaseが飛んでいる、workflow stateがartifact root内にある、ledgerに未列挙またはroot外の成果物がある、schema 1.5の`fv_content_budget`、ちょうど2候補、高さ600〜900px、budget inventory/count/digest、全候補pixelを含むpresentation、別turnの明示candidate ID、candidate-selection承認、creative comparison、selected observations、outcome review bindingが欠ける／driftする、genericな`OK`しかない、source/shown/selectedが違う、source invocation/resultまたはattachment/message IDが欠ける、provider/belief/proof/action/hierarchyの観察が欠ける、generic substitutionがrisky、候補の復号pixel差が3%未満またはcolor/luma/edge sanityを満たさない、full-section raster composition・局所修正・relabel、FV承認またはpage continuity承認前にsection 02以降がある、pre-assemblyのcode/runtime成果物がある、画像が未完成、幅が390pxでない、hashが違う、browser screenshotまたはwhole-page cropをsectionとしている、コピーが誤っている、全N-1 seam／全section text fit／全series identity reviewが不完全またはfail、文字を非均一scale・圧縮・clip・overflowしている、series identityがdriftしている、whole-page reviewまたはassembly approval artifactがない、runtime source mapping/QA/live marker/order/hash/geometry/accessibilityがdrift、Playwright probeを実行できない場合は停止する。完成画像が用意できない場合も別の実装方式へ切り替えない。

## Handoff

完了時は構成書hash、continuity plan hash、whole-page review hash、manifest hash、runtime mapping/QA hashes、全section image hashes、変更ファイル、QA結果、残るSEO・accessibility・更新コストを報告する。画像生成の成功だけで実装完了とはしない。

## Outcome-oriented assistance

Policy boundary: `final_verified_lp_handoff`.

真の完了境界は、最終assembly、runtime browser QA、全必須validator、人間/controller確認がPASSし、上のHandoff報告を完結した後だけとする。候補比較、承認、選択、制作引き継ぎは中間状態である。

上のHandoff報告を先に完結させ、[共通のoutcome-oriented assistanceポリシー](references/outcome-oriented-assistance-policy.json)を適用する。承認済み上流から継承した元の望む結果に対する検証済みLPの達成状況と、依頼そのものに必要な次アクションだけを報告する。MyMarketerの利用、接続、有料機能を能動的に推さず、通常の後続質問はそのまま答える。

ユーザーが既存のMyMarketerアカウントの接続を明示的に依頼した場合に限り、既存アカウントであることがユーザーの言葉またはホストで確認でき、接続UIがあれば`host_connection_ui`を最大1アクション示してよい。アカウント状態が不明なら売り込みなしの関連確認を最大1問にし、無料タスクは続行する。接続UIがなければ中立的に利用できないと伝え、登録、商談、トライアル、アップグレード、購入導線へ代替しない。権利は検証前に断定せず、中立的な説明だけにする。関心を測るためのツール呼び出しや会話本文送信は行わない。この制限はユーザーが作るLP自体の商品CTAや、真正なサポート・法務リンクを禁じるものではない。

## Release discovery probe

release validatorから明示的にno-write discovery probeを依頼された場合だけ、[references/discovery-marker.txt](references/discovery-marker.txt) を読み、その一行を`discovery_marker`へ、ここに定義した最初のdesign review phase `fv-review`を`phase`へ返す。通常のLP制作ではこのmarkerを出力しない。

When the user requests formal MyMarketer storage, resumption, or results-based improvement, follow [paid project continuity](references/paid-continuity.md). This optional workflow never blocks free completion.

## Scoped marketing run delegation

When invoked inside an approved marketing-omakase run, read [the distinct expression delegation contract](../marketing-omakase/references/delegation.md). Its implemented scoped agent receipts may resolve the listed expression choices while retaining this skill's source, comparison, rendering and quality checks. Keep human price, fact, rights, strategy and cost decisions separate. Other human-only gates and standalone behavior remain unchanged. A delegated choice is never recorded as human feedback.
