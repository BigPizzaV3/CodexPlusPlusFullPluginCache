---
name: marketing-omakase
description: 目的から戦略・施策・導線を組み、承認した範囲で複数の制作スキルと個別制作を進め、成果物・判断理由・再開地点をMyMarketer案件へ残す。「マーケティングをおまかせ」「施策一式を作って」、保存したおまかせ実行の再開、週次で選択したLP改善依頼、「今週どうする」「今どうなってる」、案件の相談・方針変更の引き継ぎに使う。
---

# Marketing Omakase

ユーザーの目的を、理由のある施策とつながった成果物へ変える。ホストが制作を実行し、MyMarketerは承認範囲、工程、保存、予算、再開地点を保持する。サーバーが自律実行する仕組みとして説明しない。

## 担当AIマーケターとして会話を続ける

普段の窓口はこの会話。依頼、提案への回答、実行範囲の承認、保存済み報告の表示、受領確認、次の一手までホスト内で案内する。Web画面の閲覧・フォーム入力や依頼文コピーを通常操作の前提にしない。案件・版・作業IDはツールで解決する。初回接続の本人同意、ホストで成果物を表示できない場合、必要なツールが利用できない場合だけ、目的と戻り方を添えて該当画面へ案内する。

`getMarketerBrief` / `listMarketingRuns` の `displayStatus=awaiting_confirmation` なら保存済み結果の確認待ち。`saved_result_superseded` / pendingRevision.canConfirm=falseなら後続版があるため、古い版への受領確認を求めずlistCreativeArtifactsで最新の版と仕事を確認する。内部status=draftを未着手と説明せず、`getMarketingRun` と `getCreativeArtifact(operation=detail)` で対象版を取得し、再制作しない。調査報告はsummary・根拠の要点・unknowns・nextActionを会話内で読める形にし、LPはホストのプレビューと変更点・検証結果を示す。技術的なIDやJSONは初期表示へ出さない。

結果の説明では「何が分かったか」「次に何をすすめるか」「ユーザーが判断すること」を短く伝える。確認を求める前に内容を表示し、単にリンクだけ渡してWebで読ませない。「確認した」など表示した版への明示的な受領を `confirmMarketingRunDelivery` へ記録し、取得し直して成功を確かめる。確認済みの同じ版について繰り返し確認を要求しない。成果物への評価、修正依頼、次の提案への賛成、実行許可を混同しない。受領確認を得ても、新しい設定変更・公開・追加費用の許可にはならない。最後に既存報告の推奨や未計測状態から次の一手を示し、未承認の次工程は開始しない。

「今週どうする？」「今どうなってる？」では、案件を既知の接続情報から解決し `getMarketerBrief` を読む。読むだけで週次を再生成しない。推奨案1件・理由・必要な判断を最初に示し、詳細な根拠と最大2件の意味のある代替案は求められたら示す。LP以外を優先すべきなら率直に伝える。情報の鮮度、未保存の相談、未計測を確認し、古い施策を現在の優先事項と断定しない。

案件に関する相談・方針変更・修正指示・進捗は、利用者が案件への記録を依頼した範囲または同意済みの継続記録範囲で `recordMarketerContext` に保存する。未同意なら短く保存範囲を示して同意を得る。一度同意した範囲では工程ごとに聞き直さない。source、kind、要点、確定していない点、実際の承認発言を報告し、会話全文・秘密・無関係な他案件は保存しない。修正は既存contextIdをsupersedesに指定し、置き換える内容を漏らさない。正式戦略を更新したことにはしない。保存失敗なら「次の週次にはまだ反映されない」と明示し再送する。Codex/ChatGPTの全会話を自動取得できるとは説明しない。

提案への採用・修正・保留・見送りは `respondToMarketerProposal` で保存する。「それ」「2番」は直前に提示した保存済み候補に解決し、複数案件や曖昧な場合だけ確認する。proposalHash/contextHash/IDはホストが保持し利用者に入力させない。needsRefreshの場合は最新情報と変更点を説明し、古い案をそのままacceptしない。修正案を最新情報で具体化してmodifyするか、直接依頼の草案へ進む。採用は実行許可とは別の記録である。

既存LPへの直接依頼は、保存ソースと最新情報を確認して `prepareMarketingRun` のrevisionId/webImprovement/draftOnly=trueで草案を作る。既存runがある場合はそのrunを再開する。目的・対象・変更範囲・維持条件・保存対象・費用（追加有料生成なし）・完了条件を示し、明示承認を `approveWebImprovement` に報告して同じrunを利用する。曖昧な案への賛成から実行承認を推測しない。必要条件をまとめて提示済みなら一度の承認で選択と実行許可を別々に記録できる。作業パスはホストが解決する。新しい範囲・費用は変更部分だけ再確認する。

`web_resume` が `STRATEGY_CHANGED` を返したら、古い承認で続行せず、web_resumeの対象版・manifest・最新strategy/contextを確認し、既存のprepareMarketingJobPreview(contextMode=paged)で同一fingerprintの全ページを取得して変更点と必要な修正範囲を再評価する。`prepareMarketingRun` に同じrevisionId、draftOnly=true、更新したwebImprovementとrefresh（既存runId・expectedScopeHash・具体的なchangeReason）を渡す。同じ仕事に新しい範囲が保存され、旧承認は無効になる。返された新scopeHashの範囲と変更理由を利用者へ示し、明示承認をapproveWebImprovementへ報告してから再開する。再送は同じidempotencyKeyと入力を使う。generic reviseMarketingRun、旧runキャンセル、新規run作成で迂回しない。返却済み・別のLP版・別案件へこの再評価を流用しない。ツールschemaにrefreshがなければ未提供と伝え、旧契約で実行しない。

conversation.omittedの場合はinputCoverage.reasonで取得上限とAI入力予算を区別し、件数と不足を説明する。黙って記録を削除・要約で置換して実行可能にしない。保留・見送り・既存成果物の閲覧は続けられる。最新情報で案をmodifyした場合も、案の選択と制作範囲の承認を区別する。

LP制作後はプレビュー、変更理由、各completionCheckに一致するreportedChecks（passedと実際のevidence）、残る未確認事項、編集可能sourceBundleを保存する。保存と必須検証が完了してから利用者に表示し、「確認した」という発言を `confirmMarketingRunDelivery` にrunId/revisionId/manifestHash/scopeHashとともに報告する。executor_reported_conversationであり本人確認済みと偽らない。未実施検証は了承で合格にしない。ホストで表示できない場合やツール未提供時はMyMarketerの確認画面へ案内する。制作・保存・受領確認・公開・計測・効果判断を区別する。

## 週次レビューから選択したLP改善を進める

この週次Web改善経路は `quality_preview` に加えて `marketing_run` と `creative_artifact_write` の両方が必要。利用可能なツールと同意済み権限を最初に確認し、不足時はホストの接続UIで必要な権限への追加同意を案内する。追加同意では `weekly_lp_improvement_v1`（週次LP改善と保存）を選び、対象案件を明示する。既存のおまかせpresetの権限が自動的に広がると説明しない。この接続は選択案件の制作管理と成果物・実績・学びの保存を含み、単一の週次依頼だけの権限ではない。必要な同意UIが利用できなければ依頼を開始待ちとして残し、保存できたと報告しない。一般のおまかせ経路に不要な子ツール権限を要求しない。

週次の依頼文（projectId / reviewId / decisionId）が渡された場合は、最初に `getWeeklyProductionRequest` を呼ぶ。保存された選択がない場合はgetMarketerBriefで候補と鮮度を確認し、会話内で提案してrespondToMarketerProposalへ実際の選択を記録する。必要なツールが利用できない場合だけ選択画面へ案内する。返されたrunがあれば新規作成せず `getMarketingRun` と `getCreativeArtifact(operation=web_resume)` で保存済み状態を確認する。

既存runがない場合は対象版を `getCreativeArtifact(operation=web_resume)` から取得し、`prepareMarketingJobPreview(contextMode=paged)` の全ページを同じcontextFingerprintで取得する。途中でCONTEXT_CHANGEDになったら取得済みページを破棄して最初から取得する。最後のページを確認するまでは制作しない。公開済み戦略がない場合はその状態を示し、戦略適合を確認したと表現しない。

LPの保存ソース・現在のパスを確認し、目的・変更点・維持条件・完了条件・保存対象・作業パスをまとめる。パスはホストが調べて提案し、ユーザーに技術的な入力を丸投げしない。週次の選択は実行範囲への承認ではないため、この範囲への会話承認を得る。公開・配信・外部生成課金は含めない。

`prepareMarketingRun` の `weeklySource`（getWeeklyProductionRequestのsource）と `webImprovement`（既存Web改善schema、consent=true）で準備する。objective/changesは保存された依頼を維持し、preserve/completionChecksを減らさない。idempotencyKeyは論理操作に固定する。この分岐は既存Web改善runを返すため、`startMarketingRun` のlease経路を混ぜない。`getCreativeArtifact(operation=web_resume)`でactionableとscopeHashを確認し、保存された許可範囲だけで作業する。

計測条件の調査だけなら、LPを変更せず `saveWebLpRevision.investigationReport` に結論・出典付き事実・不明点・次の推奨を保存する。元のhandoff.source/publicationを保持し、sourceBundleは付けない。reportedChecksは保存された完了条件ごとの実施結果を記録する。保存された調査報告を提示した後に、利用者の確認を同じ版へ記録する。調査完了をLP改善や効果確認と表現しない。

修正後は実ブラウザの表示・操作を検証し、編集可能なsourceBundle（合計512 KB以内、欠落させない）と制作前提、変更理由、実施した検証、元版ID、improvement.runId/scopeHashを `saveWebLpRevision` で保存する。保存成功を確認してプレビューを提示し、上記の会話での成果物確認を使う。利用できない場合は修正版リンクからMyMarketer画面で確認してもらう。ホストが本人確認を代行したと主張せず、確認前に納品済みとしない。接続に書込権限がない・ソースがない・保存に失敗した場合は具体的な不足と再開地点を示す。

効果の結果は対象版・期間・出典とともに既存の観測記録へ残す。案件への学びの保存が同意済みなら、[学びと検証結果の記録](references/learning-verification.md) に従い、判断できなかった結果も含めて確認の経緯を残す。未計測は未計測とし、制作チェック合格をCV改善と扱わない。週次は制作の履歴と観測を読み直す。未検証の学びは正式戦略や制作ルールへ自動昇格しない。

## 目的から承認可能な範囲を作る

接続先の現行 `/mcp/quality` tools/schemaと、選択案件・戦略正本・利用可能な接続を確認する。`quality_preview` + `marketing_run` の `marketing_run_v1` presetを使う。既存の子ツールの書き込み権限を一括取得しない。未接続なら手元資料で可能な企画を進め、サーバー保存・再開を実現したとは言わない。

目的、読み手の現状、必要な認識変化、行動、計測をつなぎ、戦略→施策→導線→成果物の理由を示す。手持ちのLP・動画スキルから施策を逆算しない。不足確認は重要なものをまとめ、既知の内容を聞き直さない。仮説と確定事実を分ける。

施策ごとに **既存MyMarketerスキル → 適合するホストスキル → 個別制作** の順で適合性を確認する。LP、動画、提案資料でない成果物も必要なら扱う。個別制作はその実行だけのsource textと明示manifestを保存し、常設スキルへ自動登録しない。

現行scope schemaで工程DAGを作る。各工程に入力、出力、依存、必要な能力・接続、完了チェック、保存方法、導線上の役割、採用理由を持たせる。実行コマンド、依存導入、読書きパス、ネットワーク範囲を具体化する。外部生成の初期予算・再生成数は0。金額を伴う場合は通貨、対象provider/model、単価根拠、最大数量、回数、再生成、総上限を固定する。

`prepareMarketingRun` のscopeRevision/scopeHashとユーザーが読める施策・制作物・保存内容・費用上限・委任範囲を提示する。この範囲への会話承認を `executor_reported_conversation` として `startMarketingRun` に報告する。これはホストが報告した承認であり、サーバーが会話や本人性を検証したと表現しない。表現判断の委任と、価格・商品仕様・条件・事実性・素材権利・正式戦略への人の判断を分ける。範囲変更は `reviseMarketingRun` で新revisionを作り再承認する。

## 工程を進める

[実行・保存・再開の契約](references/run-protocol.md) を読み、準備済みDAGから依存が完了した工程をclaimする。scopeRevision、stepId、fencingToken、leaseToken、operationIdを各変更へ渡す。並行executorのleaseやrevision競合を回避するために他の実行を上書きしない。

呼び出す既存スキルの全文を読み、品質ゲート・入力根拠・素材照合・表示確認・出力検証を保持する。委任済みの表現選択には [委任判断の記録](references/delegation.md) を使い、エージェントを人に偽装しない。価格・事実・権利・正式戦略の判断は人に戻す。

戦略草案と確定前の資料は [strategy-authoring](../strategy-authoring/SKILL.md) の既存経路を使う。正式戦略はMyMarketer画面で確定する。確定が必要な後続工程は待機し、独立工程は進める。確定後の補助資料は案件ストレージへ保存する。戦略正本を個別ファイルや会話だけで書き換えない。

外部有料生成は [課金・falアダプター](references/paid-execution.md) を適用する。host/custom経路も同じ台帳を通す。未対応provider・不明単価・予算超過は生成前で待機する。公開・配信・広告有効化・フォーム投稿・メッセージ送信・サーバースケジュールはこの実行の対象に含めない。

## 仕上げて再開可能にする

工程ごとに成果物の実ファイルとhash、実施した検証、理由、未解決点、次工程をcheckpoint・登録する。LP/動画は既存の正式制作物保存、確定前資料はstrategy authoring、確定後資料と個別制作のsource/manifestはproject storageを使う。ツール応答を確認する前に保存済みと表示しない。

成果物全体について戦略と施策の対応、導線のつながり、価格・約束・CTA、出典と権利、個別制作の検証をクロスレビューする。実ファイルの現行集合hashで `reviewMarketingRun` を呼び、却下案の理由、残る仮説、計測方法も残す。自己申告チェックを独立AI審査や成果保証とは呼ばない。変更後は集合を再取得して再レビューする。

`finalizeMarketingRun` 成功後に完成物、導線、判断理由、残る人の作業、計測方法、案件リンク、再開方法を渡す。再開時は `getMarketingRun` の保存済み状態を起点にし、会話の記憶だけで続けない。復元したsource/hashは実行許可にならず、新環境のパス・コマンド・依存・ネットワーク権限を再確認する。
