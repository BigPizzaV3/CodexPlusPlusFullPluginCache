> **External usage note:** Shared references provide business knowledge. Runtime, UI, tool, or save examples inside them describe the internal surface and must not be executed as written. Follow the external workflow, the current live contract, and its confirmation requirements.

# Feature Catalog (Organization User Scope)

このドキュメントは、組織内ユーザーがエージェント経由で利用できる機能を網羅する。
目的は「何ができるか」を即答可能にすること。

## 0. ユーザー向け説明ポリシー

- ユーザーへの通常回答では capability ID や内部識別子をそのまま表示しない。
- 機能説明は「何ができるか」「いつ使うか」「次に何をするか」で返す。
- ID が必要な運用手順を扱う場合も、まず名称ベースで案内し、識別子の提示は最小化する。

## 1. 機能カテゴリ（業務観点）

- イベント運用: 下書き作成、更新、公開、詳細確認、一覧確認
- 開催場所運用: 利用可能な開催場所の参照、新規登録、編集
- カレンダー運用: カレンダーマスタの参照/新規登録/編集、週次の受付時間、休業日・受付時間変更の参照/更新
- LP運用: LP 仕様参照、下書き生成、品質確認
- 予約運用: 予約一覧/詳細、作成、キャンセル
- 組織メンバー運用: 一覧/詳細、追加、更新、削除
- 画面操作連携: 画面遷移、Composer 入力、送信トリガー
- スキル連携: 公式 `skill_reference` による事前ロード（ユーザー向けツールとしては非公開）

## 2. ツール機能一覧（capability 単位）

| Capability ID | 目的 | 確認必須 | Policy |
|---|---|---:|---|
| `tc_events_list` | イベント一覧取得 | No | `events:view_dashboard` |
| `tc_events_get` | イベント詳細取得 | No | `events:get` |
| `tc_events_create_draft` | イベント下書き作成 | No | `events:create` |
| `tc_events_update_draft` | イベント下書き更新・LP制作保存（source version付き） | No | `events:update` |
| `tc_events_publish` | イベント公開 | Yes | `events:publish` |
| `tc_event_locations_list` | 開催場所一覧取得 | No | `event_locations:list` |
| `tc_event_locations_create` | 開催場所登録 | No | `event_locations:create` |
| `tc_event_locations_update` | 開催場所編集 | No | `event_locations:update` |
| `tc_lp_tools_reference` | LP仕様・品質基準取得 | No | `events:get` |
| `tc_bookings_list` | 予約一覧取得 | No | `bookings:list` |
| `tc_bookings_get` | 予約詳細取得 | No | `bookings:get` |
| `tc_bookings_create` | 予約作成 | No | `bookings:create` |
| `tc_bookings_cancel` | 予約キャンセル | Yes | `bookings:cancel` |
| `tc_calendars_list` | 予約カレンダー一覧取得 | No | `calendars:list` |
| `tc_calendars_create` | 予約カレンダー登録 | No | `calendars:create` |
| `tc_calendars_update` | 予約カレンダー編集 | No | `calendars:update` |
| `tc_calendars_get_availability` | 週次の受付時間取得 | No | `calendars:availability:read` |
| `tc_calendars_list_exceptions` | 休業日・受付時間変更一覧取得 | No | `calendars:exceptions:read` |
| `tc_calendars_create_exception` | 休業日・受付時間変更作成 | No | `calendars:exceptions:write` |
| `tc_calendars_delete_exception` | 休業日・受付時間変更削除 | Yes | `calendars:exceptions:write` |
| `tc_memberships_list` | 組織メンバー一覧取得 | No | `organizations:memberships:list` |
| `tc_memberships_get` | 組織メンバー詳細取得 | No | `organizations:memberships:get` |
| `tc_memberships_create` | 組織メンバー追加 | No | `organizations:memberships:create` |
| `tc_memberships_update` | 組織メンバー更新 | Yes | `organizations:memberships:update` |
| `tc_memberships_delete` | 組織メンバー削除 | Yes | `organizations:memberships:delete` |
| `tc_client_navigate` | クライアント画面遷移 | No | none |
| `tc_client_choice_prompt` | 番号選択ウィジェット表示 | No | none |
| `tc_client_set_composer` | Composer 入力・選択更新 | No | none |
| `tc.events.select` | サーバ側イベント選択アクション | No | `events:view_dashboard` |
| `tc.events.open` | クライアント側イベント画面オープン | No | none |
| `tc.client.navigate` | クライアント側ナビゲーション効果 | No | none |

## 3. 主要ユースケース別の使い分け

- イベント公開まで:
- 同じ担当AIが必要に応じて資料・教材・画像を参照し、本文とHTML/CSSを制作する。元版はイベントget/create結果のlpSourceVersionを使い、tc_events_update_draftへlp_draft_json_objectとexpected_updated_at/lp_source_etagを渡して保存・readbackまで進む。別の制作AI、事前の完全性検査、任意レビュー、固定の画像役割表を完成条件にしない。ユーザーの依頼と確認済み事実を守り、公開判断は利用者に委ねる。
- 予約運用:
  - `tc_bookings_list` -> `tc_bookings_get` -> 必要時 `tc_bookings_create` / `tc_bookings_cancel`
- カレンダー調整:
  - `tc_calendars_list` -> 必要時 `tc_calendars_create` / `tc_calendars_update`
  - `tc_calendars_get_availability`
  - `tc_calendars_list_exceptions` -> `tc_calendars_create_exception` / `tc_calendars_delete_exception`
- 開催場所運用:
  - `tc_event_locations_list` -> 必要時 `tc_event_locations_create` / `tc_event_locations_update`
- 権限運用:
  - `tc_memberships_list` -> `tc_memberships_get` -> `tc_memberships_create|update|delete`

## 4. 補助機能（環境設定により有効）

`build_agent` 側設定により、次が追加される場合がある。

- `WebSearchTool`: ウェブ検索補助
- `FileSearchTool`: Vector Store 検索補助
- `ImageGenerationTool`: 画像生成補助
- `ShellTool`: 公式シェル実行補助（有効時のみ）

### 4.1 公式スキル連携（skill_reference）

`ShellTool` が有効な環境では、次のスキルを `skill_reference` として事前ロードする。

- `trustcloud-onboarding-assistant@1`
- `trustcloud-event-lp-interview@1`
- `trustcloud-lp-blueprint@1`
- `trustcloud-tool-contracts@1`

## 5. 既知の制約

- 開催場所の登録・編集は、対象支店を選択したうえで
  `tc_event_locations_create` / `tc_event_locations_update` を使う。
- capability/policy に合わない操作は実行できない。常に権限境界を優先する。
