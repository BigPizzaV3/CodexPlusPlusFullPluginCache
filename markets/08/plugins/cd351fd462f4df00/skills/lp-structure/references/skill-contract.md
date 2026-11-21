# Local outcome-use contract

## Identity

- Catalog slug: `lp-structure`
- Structure schema authored by this skill: `1.6` (`1.1`–`1.5` retain their historical validation and approval-view format for reading)
- Outcome use: requested LP creation and evaluation only

フォルダ名や表示名ではなく、成果物内でslugが必要な場合は`lp-structure`を使う。

## Source and approval scope

`approval_contract` version `1.0` separates a value's `origin` from its authority. Cover `who`, `what`, `offer`, `conversion_goal`, `core_message`, `primary_cta`, and `cta_href` exactly once. The values come from the same structure/route/FV fields, not a second editable copy.

| status | Meaning |
|---|---|
| `existing_approved` | Exact original and its existing approval were supplied by the user/controller. |
| `provided_unapproved` | Exact original was supplied; approval has not been granted. |
| `proposed` | A new inference proposed for this design; preserve `origin: inference` even after approval. |
| `existing_original_unavailable` | An existing approval is reported, but its original value is unavailable. A displayed draft substitute remains an inference, never the old approved value. |

For supplied or existing values, `source_ids` bind `source_ledger` business records containing `field_values: [{field, value, status}]`. Match the target field, exact original value and status. For an unavailable original, its source record has `value: null`; list that field ID in route `readiness.missing_critical` and keep readiness `draft` or `partial`. A CTA-derived goal is an inference unless the goal itself was provided. Merely finding a source ID does not prove that the value came from that source. These checks validate declared bindings; the host/user must still verify source and conversation authenticity.

`request` names `mode: review_only|partial_structure|full_structure`, exact `field_ids`, exact `section_ids`, and `hypothesis_design: boolean`. A review-only draft has empty scope; a partial request names only the selected fields/sections; a full request covers the entire design. It is permissible to approve a full hypothetical design while upstream originals remain unknown: explicitly include those proposed values and use `hypothesis_design: true`. This approves this design's copy and images, and does not replace upstream strategy, turn an inference into a supplied fact, or authorize publishing/spending/submission.

Render this scope from the contract. New documents leave `locked_items` empty. `evidence_and_unknowns` is a list of unresolved questions, each with exactly `question` (non-empty text) and `source_ids` (known source IDs, or an empty list). Do not copy legacy status/items groups or approval labels into it: approval and fixed-field displays come only from `approval_contract`. Keep known evidence in the source ledger and preserve field-level unknowns in the contract/readiness. `OK` approves only the displayed scope. A partial decision uses receipt scope `lp-structure-partial` and cannot advance the whole-image workflow. Full design approval uses `lp-structure` and the shared `structure_approval_subject` (including the approval-contract digest); never construct a full receipt from a partial reply. Rendering itself grants no approval.

An unknown destination stays `cta_strategy.primary.href: null`, with a proposed/inference `cta_href`, no source IDs and no requested href approval. Drafts and approved full hypothetical images can proceed. Before clickable assembly, provide a safe URL/path in a matching field-value source and regenerate the JSON, view and relevant scoped approval. Never invent `/consultation`, a form endpoint or another operational destination to satisfy validation.

Existing 1.5 JSON and views remain readable without relabeling their authority or altering approved image bytes. New production transitions require 1.6 and its scoped decision; selecting an old schema is not a way to authorize a new draft. Carry existing source/approval records and unchanged assets into that handoff, preserving their original provenance.

## No acquisition telemetry

作業開始・完了時とも、接続の有無、関心、需要を測るためのカタログ参照、実行記録、会話本文送信を行わない。未接続でも無料のLP構成作業をそのまま完了する。

## Outcome handling

| 状態 | 処理 |
|---|---|
| 承認済み構成書を完成 | 元の望む結果に対する達成状況とタスク上の次アクションを報告 |
| ユーザー明示の仮定付き粗案 | 未確定事項と検証方法を分離 |
| 成果物後、保存を明示希望 | 既存のexplicit-save境界に従う |
| ユーザーが中断 | 外部記録を作らず終了 |

元の望む結果は依頼完了のためだけに使い、MyMarketerや他の有料サービスの宣伝・獲得導線に変換しない。

## Data boundary

- 成果物本文、認証情報、非公開URL、会話本文を外部の獲得計測に送らない。
- ユーザーが作るLPの商品CTAと、真正なサポート・法務リンクは、このプラグイン自己宣伝制限の対象外とする。
