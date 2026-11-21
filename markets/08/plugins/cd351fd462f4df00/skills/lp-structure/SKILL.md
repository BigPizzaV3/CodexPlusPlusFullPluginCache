---
name: lp-structure
description: 配布プラグインで新規LPや未承認の構成・コピーを承認用構成書にする。承認済み構成の画像制作はlp-image-builderへ。分析のみ・既存コードの部分修正には制作を開始しない。
---

# LP Structure

流入からCTAまでの説得構造と逐語コピーを、一つの承認可能な構成書として設計する。無料モードではユーザーが提供した事実と資料だけを根拠にし、有料read接続時だけ認可済み案件文脈を追加で使う。

## Optional MyMarketer quality connection

既に利用可能な無料共通チェックが今回の判断に関係する場合、またはユーザーが有料AI審査を明示依頼した場合だけ、[任意のcreative check契約](../lp-image-builder/references/creative-core-contract.md)を読む。新接続は本番未提供の開発候補であり、未接続時のローカル品質ルール・承認・非保存の標準工程はそのまま維持する。

この接続は **read-only by default / explicit save only** とする。

取得したpreviewの完全な`context`が同じrun・接続・案件・fingerprintで利用でき、後続toolの公開schemaが対応する場合だけ、guidanceとrubricに`contextMode: "reference"`を渡す。`contextReference.fields`はそのpreviewの`context`から解決し、条件が空になったとは解釈しない。schema未対応なら引数を省略する。文脈が失われた場合はpreviewを最大1回再取得し、復元できなければ無料モードへ戻す。`CONTEXT_TOO_LARGE`は再試行や旧ツールで回避せず、有料文脈を捨て、共通ポリシーの容量超過1行を表示する。重要な判断・禁止事項の切り捨てや、情報不足のまま品質連携済みとすることは避ける。

作業前に [共通の接続品質ポリシー](../lp-image-builder/references/connected-quality-policy.json) を読む。MyMarketerの`/mcp/quality` read接続と`quality_preview`が利用可能だと確認できない場合は、接続やログインを要求せず、利用不能ツールを試さず、ユーザー提供情報・一般知識・このローカルSkillだけで完結する。

有料read接続済みの場合だけ、必要なら`listProjects`で案件を一つに確定し、曖昧なら案件を選ぶ具体的な一問だけを聞く。`prepareMarketingJobPreview(deliverableType=landing_page)`で取得した`contextFingerprint`を変えずに`getProductionGuidanceInputs`と`getDeliverableReviewRubric`へ渡す。返却された案件文脈・制作条件・rubricを根拠に、このホストで3方向を作り、ユーザーの選択1回後に構成を作成し、rubricで非表示自己採点する。不合格時だけ最大1回改稿し、再採点してから提示する。`CONTEXT_CHANGED`なら非保存の文脈取得を一度だけやり直す。上流で確認済みの目的、CTA、claim境界、承認済み判断は変えない。

通常の品質工程では旧`persistence`引数付きツールを使わない。完成稿の案件保存をユーザーが明示した場合だけ`saveDeliverableV1`を使い、必要なら`mcp:write`の追加同意へ進む。OAuthのwrite権限は個別操作の承認ではない。施策提案、意思決定、学び、公開、配信、課金操作も、その都度ユーザーの明示確認後だけ行う。実績値が届く前に成果や学びを作らない。

接続、契約、権限、案件、予算のいずれかで失敗したら、そのrunの有料文脈を破棄して再利用せず、MyMarketer情報を推測しない。ポリシー所定の「有料品質ループ未適用」1行だけを表示し、無料モードで続ける。未接続で最初から無料モードの場合はこの失敗表示も出さない。

## Route Check

LP構成を書く前に、[Acquisition Architecture Router v1](references/acquisition-route-rule-v1.json) を読み、どのページ型にするかではなく、誰をどの心理状態から最終CVまで動かすために各接点が何を担当するかを決める。ユーザーはLP型を知る必要がない。ユーザーが記事LP・通常LP・診断LPを指定した場合もRoute Checkを省略しない。

1. `WHO / Current State / WHAT / Offer / Conversion Goal / 商品・サービス概要`を確認する。仮説として構成できる不足は仮置きと未確認範囲を示して進める。依頼の範囲を決められない不足だけ、関連する質問を最大3問にまとめて一度に聞く。一問ずつ何度も聞かない。複数のWHO、WHAT、Offerが競合し優先順位を選べない場合は`strategy_gap`として、候補と影響だけを示し、勝手に正式決定しない。
2. `Current State → Required Shift → Primary Barrier → Required Persuasion Jobs`を先に決め、その心理変化を広告・動画・記事・通常LP・診断・営業のどこに担当させるかを割り当てる。その後でChannel / Surface / Destination Format / Proof / CTA / Measurementを決める。B2B、年齢、価格、広告媒体など一つの属性だけでチャネルやページを決めない。
3. v1のDestination Formatは`direct_capture / article_reframe / diagnostic`の3つを比較する。`compare / customer case / demo / offer`は排他的なLP型ではなく、persuasion jobまたはproof moduleとして必要なページ内へ配置する。記事を挟んで同じ説明を重複させるよりDirectが短い場合はDirectを選ぶ。Diagnosticは将来候補の評価だけに留め、結果別の可視result・next action・destination bindingを正式契約で表現できるまではprimary/build targetにもRecommended routeにも選ばない。候補に残す場合も、根拠refを持つ異なるcondition、正規化後も異なるresult、正規化後も異なるnext actionを2系統以上構造化し、全回答を同じ販売結果へ送る疑似診断を作らない。
4. 主案1つ、代替案1つ以上、今回推奨しない案1つ以上を出し、主案の理由を必ず`Current State → Required Shift → Route`で説明する。推奨は未検証なら`recommended hypothesis`であり、「最適」「最も売れる」と断定しない。
5. 取得できる場合は価格、粗利、LTV、許容CAC、制作負荷、営業工数、商談化率、成約率、購買期間も確認する。数字を推測せず、不足時は心理導線の妥当性と採算性を分けて`economics.status: unconfirmed`とする。B2BではLPのCVで止めず、フォーム後の営業対応・商談・受注までを最終conversion pathとして扱う。
6. Routeが複数接点を持つ場合は、各touchpointへ重複のないmessage roleとpersuasion jobsを割り当て、今回構成する一つの`build_target_touchpoint_id`を固定する。広告がREFRAME / EDUCATEを完了するなら、遷移先で同じ教育を繰り返さない。`article_reframe`を選ぶ場合、build targetの記事は`reframe + educate`（必要なら`identify`も可）だけを担当し、`prove / offer / capture`を記事へ混ぜない。記事には`exit_action_kind: next_destination`と`exit_target_touchpoint_id`を置く。`exit_action`はfail-closedの情報閲覧handoffとし、次のコンテンツやサービス詳細、ガイド、事例・例、方法・プロセス・仕組みを「読む・見る・知る・学ぶ」と明確に表すwhole labelだけを使って後続Service LPのtouchpoint IDへbindする。この正の意味契約に入らない相談・予約・申込・購入・登録・無料体験などの行動は記事CTAにせず、最終touchpointとして置く`surface_kind: destination`かつ`direct_capture`のService LPで`prove + offer + capture`を担当させ、最終`conversion_action`はそのService LPだけへbindする。
7. ユーザー指定Routeが主案と異なる場合は、推奨との差・リスク・補正方法を短く示す。安全・法令・権限違反でなければ拒否せず、`user_override.applied: true`として指定Routeで最善の構成を作る。overrideはformat名ではなく、選択した`selected_route_id`と本来の`recommended_route_id`を残す。同じDestination Formatでも接点・message roleが異なるRouteを区別し、approval viewには「ユーザー選択」と「推奨」を別々に表示する。
8. [出典と承認範囲の契約](references/skill-contract.md#source-and-approval-scope)に従い、出典・既存承認・今回の仮説提案を分離する。既存原文が不明でも仮説草案は作れるが、推定Goalを既存承認へ格上げしない。Route Checkの結果は会話だけに置かず、schema 1.6構成書の`acquisition_route_brief`へ構造化する。`kind: acquisition-route-brief`、`schema_version: 1.0`、`route_rule_version: acquisition-route-v1`を使い、WHO、Current State、Required Shift、WHAT、Offer、Conversion Goal、Core Message、根拠種別、確度、主案・代替案・非推奨案、proof gaps、経済性、仮説、計測案を残す。`user_input`の根拠refは`source_ledger`へ解決し、推測は`inference`と明記する。無料モードは`mode: free_light`かつ`project_context: null`とし、有料案件由来を装わない。有料read接続時は`mode: paid_quality`とし、返却されたproject IDと`contextFingerprint`だけを正確にbindし、paid由来値のrefも同じfingerprintとauthority種別へbindする。
9. 通常のRoute Checkではbrief、入力、成果物、Telemetry、需要シグナルをMyMarketerへ保存しない。構成書をローカル成果物として生成することと、MyMarketer案件へ保存することを区別する。案件保存は完成稿についてユーザーが明示した場合だけ、既存のexplicit save境界へ進む。
10. 下流の構成では`WHO / WHAT / Offer / Conversion Goal / build targetのCurrent StateとRequired Shift / Core Message`を黙って変更しない。WHOはFVのaudience/relevance、WHATはscan contractのwhat-it-is、Offerはfive-second promise/core-benefit/source-offer、Core Messageはdominant messageへ逐語bindする。変更が必要なら`upstream_conflict`としてユーザーへ返す。各sectionに担当する`persuasion_jobs`を付け、build targetへ割り当てたjobsを全体で過不足なく扱い、Route内の同じjobを複数touchpointへ重複割当しない。

## 適用範囲

「LP作って」「LPを作りたい」「この会社のLP」「この商品のLP」「このサービスのLP」「Meta広告用LP」「無料相談LP」「無料体験LP」「LP構成・コピーだけ」は、配布版で構成未承認の制作を求める文脈ならここから開始する。

配布プラグインによるLP制作の構成段階を担当する。提供資料から構成・逐語コピーを作り、承認後の画像制作は兄弟スキルへ引き継ぐ。既存の承認済み構成から画像を作る依頼では `lp-image-builder` が主担当となる。

分析・改善提案だけなら依頼された評価で終了し、構成書の制作や承認フローを自動開始しない。既存Webコードの部分修正、一般UI、LP制作ではない相談は対象外。明示指定と既存成果物の方式を優先し、他の個人用・プロジェクト用スキルを一括で読まない。

このスキルは配布パッケージ内の資料だけで利用する。個人環境の非公開スキルを参照しない。編集元は `mymarketer-codex-plugin/plugins/mymarketer/skills/`、インストール済みコピーは編集しない。

## Workflow

依頼文または提供ソースに、このLPで実現したい主要な訪問者行動・事業上の結果があるかRoute Checkで確認する。欠けている場合は「このLPで一番増やしたい行動は、購入・問い合わせ・予約・資料ダウンロードのどれですか？」を他の重大不足と同じ一度の確認へまとめる。明らかなら聞かず、推奨材料を集めるための質問票にしない。回答はRoute BriefのConversion Goal、構成書の目的、build targetのexit actionへ継承する。

1. 次の入力を確認する。
   - 誰に届けるか、流入元、読者の認知段階
   - 解決する痛み、約束、オファー、主要CTA
   - 数字・実績・顧客の声・仕様を支える証拠、その出典、顧客素材の利用許諾とプライバシー確認
   - 電話導線が適切な地域・サービス事業か。適切なら、ユーザー提供の電話番号、受付時間・応答可能性、その出典
   - ブランド制約、法務制約、避ける表現
2. 完成品質に必要な入力が足りなければ、影響が大きい順に最大3問だけ質問する。ユーザーが仮定を明記した粗案を明示的に求めた場合だけ、未確認事項を分離して進める。
3. 次の内容を一つの構成書にまとめる。
   - `acquisition_route_brief`として、判断前提、必要な心理変化、各接点の役割、主案・代替案・非推奨案、build target、証拠不足、仮説と確度、計測案。structureのaudience / objective / offer / primary CTAと相互にbindする
   - 目的、対象読者、流入、オファー、主要CTA
   - `fv_handoff`として、5秒で伝わる対象読者・約束/オファー・正確な可視アクションラベル、一つのdominant message、可視表現を伴うbelief shift、visual job、可視表現と出典を結ぶcredibility判断、audience identityとは独立したprovider recognition判断、identity recognition判断、避ける印象
   - `context_assessment`としてtraffic/source message一致、awareness、category familiarity、offer complexity、decision risk、proof strength、visual explanatory power、action readiness、regulatory classを具体化し、source offer/CTAを5秒contractへ逐語bindする
   - `scan_contract`としてrelevance / what-it-is / core benefit / trust basis / next actionの答えと、許されるevidence mode (`copy|visual|proof|cta`) を固定する。visualやproofがcategory/trustを十分説明する場合、同じ説明copyを重複させない
   - `fv_content_budget`として、文脈から選んだ`lean|standard|reassurance-heavy` profileと理由、先頭sectionの全逐語copyを順番どおり過不足なく分割したvisible items、実在する後続sectionへ送るdeferred items
   - 判断シートと採用した説得方針
   - `authentic_proof`として、`customer-face` → `handwritten-feedback` → `verified-fallback`の順に利用可能性を確認し、最初に実在・出典・許諾・privacyを満たす方式だけを採用する。顧客assetの許諾/privacyは、user/controller提供・`authored_by_model:false`の外部JSON証拠path/hashへbindし、asset/use/scope/expiry/constraintsを一致させる。顧客、顔、手書きの声、testimonial、許諾を生成・推測しない
   - `cta_strategy`として主CTA一つを固定する。`direct_call`は文脈上適切で、正確な電話番号と受付時間・応答可能性の出典が完全一致の`verified_value`を持つ場合だけsecondaryとして`enabled`にする。電話を全LPの必須条件にしない
   - 安定したsection IDを持つセクション順
   - 全隣接sectionを順に結ぶN-1件の境界計画。各境界はfrom/to、次が自然に読まれる理由、`visual|layout|open-loop|contrast|copy|mixed`の仕組み、nullableなtransition copy、semantic/copy/visual/layoutのexact `bridge_plan`を持つ。矢印はsupportiveに限る
   - 全sectionを対象にしたseries candidate inventoryと、`present|none`＋理由のseries assessment。STEPなどの反復シリーズがある場合は、連続section/componentをまたげるmember列と、全memberで認識可能な共通cue
   - 各セクションの役割、見出し、本文、CTA、証拠、注記の逐語コピー
   - 画像化時の主題・感情・構図・インタラクティブ領域の希望
   - 根拠の所在、未確定事項、版付き`approval_contract`の今回承認範囲（freeform `locked_items`は空）
   - 外部approval receiptが固定する安定したJSON構造
4. 数字、受賞、顧客の声、商品仕様を捏造しない。未確認情報を本文へ混ぜず、未確定事項へ移す。
5. 境界はコピーを置く欄ではなく、読者の疑問と視覚の流れを設計する欄として使う。visual/layout/open-loop/contrastによるcopyless遷移を第一級の合格経路とし、transition copyは必要な境界にだけ使う。`mechanism: copy` のときだけtransition copyを必須にする。装飾矢印だけを遷移の仕組みにしない。
6. series候補を全section/componentで棚卸しする。該当なしでも`series_assessment.status: none`、理由、全sectionを覆うcandidate inventoryを残す。`present`では`series_candidate: true`の`section_id`/`component_id`組を、全`repeated_series.members`の組と過不足なく一致させ、候補を未割当のまま残さない。`STEP 1`/`STEP 2`のような明示的な番号seriesをnone扱いにしない。自動検出は保守的な補助なので、カード列、料金plan、比較項目など名前にSTEPがない反復の見落としは人間/controllerが確認する。
7. [references/lp-structure-document.template.json](references/lp-structure-document.template.json) に従い、Route Briefを内包するschema 1.6の一つのJSON構成書を保存する。既存schema 1.5成果物はRoute Briefなしでも従来どおり読み取り互換だが、新規作成では必ず含める。承認前に、その保存済みJSONを実際のbuilder validatorで検証し、同じJSONからRoute Checkを含む決定論的なMarkdown approval viewを生成して再検証する。例えばskill rootから次を実行する。

```bash
python3 scripts/render_structure_approval_view.py /path/to/structure.json /path/to/structure-approval.md --source-path structure/lp-structure-approved.json
python3 scripts/render_structure_approval_view.py /path/to/structure.json /path/to/structure-approval.md --source-path structure/lp-structure-approved.json --check
```

   JSONだけがコピー・順序・machine authorityであり、Markdownはsource pathとJSON SHA-256へbindされた読みやすいapproval viewにすぎない。変更は必ずJSONへ行ってからviewを再生成する。会話ではraw JSONを本文へdumpせず、既定でviewのgoal/audience/offer/action、簡潔なFV計画とdeferred items、各sectionのreader question→answer/headline/proof、unknowns/locksを示し、JSONはattachment/referenceとして渡す。SHA-256とapproval scope `lp-structure`を示す。`fv_handoff`は結果契約であり、レイアウト、写真/被写体、左右配置、色、badge数、named style pattern、画像制作手法を固定しない。belief shiftの`visible_expression`は先頭sectionのauthority copyへ完全一致で含める。visible credibilityは各refを既存`claim_source_ledger`へ解決し、各visible expressionを同じclaim本文と先頭section authority copyの両方へ含める。deferredならrefs/expressionsを空にする。provider recognitionはaudience identityとは独立に選び、visibleなら正確な`provider_name`を先頭section authority copyへ含め、deferredならnullにする。identity recognitionにも既定値を置かない。schema 1.1〜1.5は既存成果物の読み取り互換だけに使い、新規作成しない。approval viewには`source_ledger`へbindした`authentic_proof`の方式・許諾/privacy、主CTAと`cta_strategy.direct_call`判断、全N-1 `bridge_plan`を必ず表示する。自分で承認しない。提示時はvalidatorが描画した今回のscopeだけを説明する。`full_structure`の「OK」「このまま進めて」は明示した仮説を含むデザイン全体だけを承認し、次turnで画像制作へ続ける。`partial_structure`や`review_only`を全体制作許可にしない。
8. `fv_content_budget`は文脈でprofileを選ぶ。`lean`の90字/5 items/1 proof、`standard`の140/7/2、`reassurance-heavy`の180/8/3はpre-generation planning guardrailであり、普遍的な合否閾値ではない。exact countsと`within-profile|context-exception`、理由を記録する。超過時は原則copyを圧縮または後続へ送って再承認するが、decision risk等の具体的文脈が必要とする例外は宣言でき、最終合否は390px実寸render outcomeで決める。どのprofileもvisibleなsupport/audience/providerは各1件まで、`micro`は非空白24字までとする。visible itemはstable ID、semantic role (`audience|dominant|support|provider|proof|action`)、先頭section copy key、逐語text、visual weight (`primary|supporting|micro`)、nullable claim IDを持つ。dominantと主actionを各1件にし、全非空copy leafを同じ順で完全被覆する。proofはverified claimに結び、must-showの事実はclaim本文に含まれる短い逐語phraseをmicro signalとして使ってよく、長い説明文をFVへ持ち込まない。provider/identity/credibility/beliefのvisible/deferred判断をitemsへ結ぶ。deferred itemは実在する後続section IDと理由を持ち、そのtextをdestination sectionの全nested copy leaf（eyebrow/bullets等を含む）のどれかへ逐語bindし、proofならclaimの`use_sections`もdestinationへbindする。process詳細、完全なservice-area情報、map/photo calloutなどを送る。profileを重くして押し込むことを既定にしない。
9. `full_structure`の対象field/sectionを全部含む決定だけを制作許可にする。部分決定は`lp-structure-partial`として保持する。後続の別ユーザーturnで、直前に提示した構成書が一つに特定でき、そのpath/hashとscopeを示したうえで「OK」「このまま進めて」などの明示承認を受けた場合だけ、その返答を直前の構成書のscope `lp-structure`に限定して受ける。外部receipt bytesが提供された場合だけexternal receiptとして扱う。会話上の承認なら [conversation-approval-record.template.json](../lp-image-builder/references/conversation-approval-record.template.json) に従い、`decision_provided_by` と `recorded_by: model`、verbatimまたはmessage digest、scope、subject digestを正直に記録する。競合する構成書を残さない。
10. 直前の構成全体（`full_structure`）が明示承認された同じ後続turnで、兄弟スキル [../lp-image-builder/SKILL.md](../lp-image-builder/SKILL.md) を先頭から末尾まで完全に読み、そのEntry gate以降を承認済み構成書とapproval artifactから続ける。ユーザーにスキル名の指定や別スキルの呼び出しを求めず、まず390pxのFV候補制作へ自動的に進む。構成承認をHTML/CSS、hybrid、code-native、decompositionの開始許可として扱わない。直前が構成書でない、対象が複数ある、hash/scopeが不明、承認が曖昧なら引き継がず確認する。

## Output contract

構成書には少なくとも次を含める。JSON全体がコピーと順序のauthorityであり、Markdown approval viewはその表示用派生物、承認は別の外部receiptがこのfile hashを固定する。

```json
{
  "kind": "lp-structure-document",
  "schema_version": "1.6",
  "claim_source_ledger": [{"claim_id": "claim-01", "claim": "実績確認済みの支援内容", "status": "verified", "source_ids": ["source-01"], "use_sections": ["section-01"]}],
  "fv_handoff": {
    "five_second": {
      "audience": "誰向けか",
      "promise_or_offer": "伝える約束またはオファー",
      "next_action": "無料相談を予約する"
    },
    "context_assessment": {
      "traffic_source_message": "計測できるLPを始める",
      "source_message_match": "matched",
      "source_offer": "計測できるLPを始める",
      "source_action": "無料相談を予約する",
      "awareness": "課題認識済み",
      "category_familiarity": "中程度",
      "offer_complexity": "中程度",
      "decision_risk": "中程度",
      "proof_strength": "確認済み実績1件",
      "visual_explanatory_power": "visualでサービス種別を説明可能",
      "action_readiness": "相談準備済み",
      "regulatory_class": "通常"
    },
    "scan_contract": {
      "relevance": {"answer": "対象事業者", "evidence_modes": ["copy"], "rationale": "対象が識別できる"},
      "what_it_is": {"answer": "LP制作支援", "evidence_modes": ["visual"], "rationale": "visualで種別を説明できる"},
      "core_benefit": {"answer": "計測できるLPを始める", "evidence_modes": ["copy", "visual"], "rationale": "便益が識別できる"},
      "trust_basis": {"answer": "実績確認済み", "evidence_modes": ["proof"], "rationale": "確認済みproofがある"},
      "next_action": {"answer": "無料相談を予約する", "evidence_modes": ["cta"], "rationale": "主CTAが一つある"}
    },
    "dominant_message": "成果へ進む",
    "belief_shift": {"from": "まだ動けない", "to": "いま始められる", "visible_expression": "いま始められます。"},
    "visual_job": "ビジュアルが果たす伝達上の結果",
    "credibility": {"decision": "visible", "evidence_refs": ["claim-01"], "visible_expressions": [{"claim_id": "claim-01", "text": "実績確認済み"}], "rationale": "この流入では短い安心材料が必要"},
    "identity_recognition": {"decision": "deferred", "recognition_target": null, "rationale": "詳細な対象条件は次sectionで示す"},
    "provider_recognition": {"decision": "visible", "provider_name": "事業者名", "rationale": "指名を認識できる必要がある"},
    "avoid_impressions": ["避ける印象"],
    "fv_content_budget": {
      "profile": "standard",
      "rationale": "この流入文脈で必要な安心と即時理解の釣り合い",
      "visible_items": [
        {"id": "provider", "semantic_role": "provider", "copy_key": "headline", "text": "事業者名｜", "visual_weight": "micro", "claim_id": null},
        {"id": "dominant", "semantic_role": "dominant", "copy_key": "headline", "text": "成果へ進む", "visual_weight": "primary", "claim_id": null},
        {"id": "belief", "semantic_role": "support", "copy_key": "body", "text": "いま始められます。", "visual_weight": "supporting", "claim_id": null},
        {"id": "proof", "semantic_role": "proof", "copy_key": "body", "text": "実績確認済み", "visual_weight": "micro", "claim_id": "claim-01"},
        {"id": "action", "semantic_role": "action", "copy_key": "cta", "text": "無料相談を予約する", "visual_weight": "supporting", "claim_id": null}
      ],
      "guardrail_assessment": {"char_count": 31, "item_count": 5, "proof_count": 1, "status": "within-profile", "rationale": "文脈選択したlean guardrail内"},
      "deferred_items": [{"id": "audience-detail", "semantic_role": "audience", "text": "詳しい対象条件", "claim_id": null, "destination_section_id": "section-02", "rationale": "FVの主メッセージを優先する"}]
    }
  },
  "adjacent_boundary_plan": [
    {
      "order": 1,
      "from_section_id": "section-01",
      "to_section_id": "section-02",
      "why_next": "未解決の疑問を次で証明するため",
      "mechanism": "visual",
      "transition_copy": null
    }
  ],
  "repeated_series": [],
  "series_assessment": {
    "status": "none",
    "rationale": "反復シリーズに該当するcomponentがない",
    "candidate_inventory": [
      {"section_id": "section-01", "component_id": null, "label": "反復なし", "series_candidate": false},
      {"section_id": "section-02", "component_id": null, "label": "反復なし", "series_candidate": false}
    ]
  },
  "sections": [
    {
      "id": "section-01",
      "order": 1,
      "role": "説得上の役割",
      "copy": {"headline": "事業者名｜成果へ進む", "body": "いま始められます。実績確認済み", "cta": "無料相談を予約する"},
      "evidence": "根拠または未確認",
      "visual_direction": "主題・感情・構図",
      "interactive_region": "none"
    },
    {
      "id": "section-02",
      "order": 2,
      "role": "次の問いへ答える役割",
      "copy": {"headline": "対象条件", "body": "詳しい対象条件", "cta": null},
      "evidence": "根拠または未確認",
      "visual_direction": "主題・感情・構図",
      "interactive_region": "none"
    }
  ]
}
```

保存先や形式はユーザーの既存作業環境に合わせるが、成果物本文は一つに保つ。画像、実装コード、内部運用情報、認証情報は含めない。

## Outcome-oriented assistance

Policy boundary: `validated_structure_or_copy_only`.

構成・コピーまでがユーザーの明示した最終依頼で、保存済みJSONとapproval viewの検証が通ったときだけ完了境界とする。「LPを作って」「デザインまで」など完成LPが目的ならここは中間の承認・画像制作引き継ぎである。

完了時は[共通のoutcome-oriented assistanceポリシー](../lp-image-builder/references/outcome-oriented-assistance-policy.json)を適用し、根拠のある元の望む結果に対する構成書の達成状況と、依頼そのものに必要な次アクションだけを報告する。MyMarketerの利用、接続、有料機能を能動的に推さず、通常の後続質問は状態遷移せずそのまま答える。

ユーザーが既存のMyMarketerアカウントの接続を明示的に依頼した場合に限り、既存アカウントであることがユーザーの言葉またはホストで確認でき、接続UIがあれば`host_connection_ui`を最大1アクション示してよい。アカウント状態が不明なら売り込みなしの関連確認を最大1問にし、無料タスクは続行する。接続UIがなければ中立的に利用できないと伝え、登録、商談、トライアル、アップグレード、購入導線へ代替しない。権利は検証前に断定せず、中立的な説明だけにする。関心を測るためのツール呼び出しや会話本文送信は行わない。この制限はユーザーが作るLP自体の商品CTAや、真正なサポート・法務リンクを禁じるものではない。

構成書を固定するexternal receiptまたはtruthful conversation approval recordがない段階では画像制作を開始しない。genericな `OK` は直前に示した構成書とscopeだけを承認する。FV候補の選択、FV方向、page continuity、assemblyなど後続の未提示・別scopeを承認せず、FV候補選択には後続turnでexact candidate IDを一つ要求する。approval artifactのdeclared provenanceは暗号学的な本人確認ではないため、決定が実際にユーザー/controllerから来たことを会話上でも確認する。

When the user requests formal MyMarketer storage, resumption, or results-based improvement, follow [paid project continuity](../lp-image-builder/references/paid-continuity.md). This optional workflow never blocks free completion.

## Scoped marketing run delegation

When invoked inside an approved marketing-omakase run, read [the distinct expression delegation contract](../marketing-omakase/references/delegation.md). A scope-bound agent receipt can decide structure expression after actual human product, price, terms, fact and material-rights decisions. Keep every structure production/source, approval-view, copy, CTA and rights validator. Record the agent as the decision maker and never invent a user message or factual approval. Standalone runs retain their existing human approval workflow.
