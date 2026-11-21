> **External usage note:** Shared references provide business knowledge. Runtime, UI, tool, or save examples inside them describe the internal surface and must not be executed as written. Follow the external workflow, the current live contract, and its confirmation requirements.

# Onboarding Setup Playbook (State and Action)

このプレイブックは「順番をなぞる手順書」ではなく、「状態を判定して最短で進める実行ガイド」。

## 0. First Turn Rule

- 初回返信で宣言だけ返さない。
- 目的が未定の場合だけサービスを短く説明し、「何をしたいか」を確認する。
- 意図が明確な依頼では導入説明や意向確認を繰り返さず、依頼された結果へ直接進む。
- 選択質問は `tc_client_choice_prompt` を使い、ウィジェットをターン末尾に表示する。

## 1. 状態判定

次の順で状態を判定する。

1. ユーザー意向が確定したか（説明希望 / 設定開始 / 現状確認）
2. 文脈があるか（organization/branch/event）
3. 開催場所があるか
4. イベント下書きがあるか
5. 下書き必須項目が埋まっているか
6. 予約できる時間が確認済みか
7. LP 下書きが作成済みか
8. 公開確認が済んでいるか

### 1.1 公開依存

LP公開は次の前提を満たしてから行う。

1. 開催場所
2. イベント下書き必須項目
3. 予約できる時間と休業日・受付時間変更
4. LP下書き
5. 公開確認

ユーザーの希望が「LP公開を急ぎたい」の場合でも、公開前提は省略しない。

## 2. 状態別アクション

### State: 文脈不足

- 意向が設定開始/現状確認なら `tc_client_navigate("/reservation-manager/events")`
- 不足文脈を1問で確認

### State: 開催場所なし

- ユーザーが新規登録を明示し、作成ツールと権限がある場合は、`tc_event_locations_list` で重複を確認して `tc_event_locations_create` で登録する。
- 登録に不足する情報だけを確認する。ツールや権限がない場合は画面操作を案内し、登録完了後に現在の候補を確認する。

### State: 下書きなし

- `tc_events_create_draft`
- 作成後 `tc_events_get` で内容確認

### State: 下書き不完全

- `tc_events_update_draft` で不足項目を補完
- 更新直後に `tc_events_get` で確認

### State: カレンダー未確認

- `tc_calendars_get_availability`
- `tc_calendars_list_exceptions`
- 必要なら `tc_calendars_create_exception`

### State: LP 未作成

- `tc_lp_tools_reference`
- 同じ担当AIが必要に応じて資料・教材・画像を参照し、本文とHTML/CSSを制作する。元版はイベントget/create結果のlpSourceVersionを使い、tc_events_update_draftへlp_draft_json_objectとexpected_updated_at/lp_source_etagを渡して保存・readbackまで進む。別の制作AI、事前の完全性検査、任意レビュー、固定の画像役割表を完成条件にしない。ユーザーの依頼と確認済み事実を守り、公開判断は利用者に委ねる。

### State: 公開待ち

- 確認後、保存済み下書きの `updated_at` を `expected_updated_at` に渡して `tc_events_publish(confirm=true, expected_updated_at=...)`

## 3. 質問設計

- 原則1問。
- 次の操作に必要な依存項目が複数ある場合のみ2問まで許容。
- 質問は選択式を優先し、自由記述を最小化する。
- 番号選択はテキスト入力で求めず、`tc_client_choice_prompt` を優先する。
- 選択肢は依存順序を誤解させない文面にする（例: LP公開を独立タスクとして提示しない）。

## 4. ターン出力テンプレート

結果を先に短い段落で伝える。途中報告はユーザーの判断に必要な進展、失敗、待ちがある場合だけ行い、widgetの内容や進捗を本文で繰り返さない。未完了の場合は再開に必要な入力または次の行動を短く示す。

### 4.1 出力の認知負荷ガード

- ユーザー向け回答では ID（`thr_*` / UUID / resource id）や capability 名（`tc_*`）を出さない。
- 必要情報は「名称」「状態」「次アクション」に変換して提示する。
- 内部識別子が不可避な場面でも、まず名称で説明し、識別子は原則省略する。

## 5. 終了条件

- 依頼された説明、現状確認、設定などの成果が得られた時点で完了とする。
- 公開までの支援を依頼された場合は、公開済み、または公開確認待ち。
- 以降は `feature-catalog.md` に基づく運用質問対応へ移行
