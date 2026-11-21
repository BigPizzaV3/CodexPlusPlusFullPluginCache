---
name: reconcile-financial-records
description: Investigate missing, duplicated or incorrect Fina records; correct purchases, link refunds, resolve review items and associate completed own-account transfers or debt payments. Use for record discrepancies and corrections, preserving evidence and existing history.
---

# Review and correct records

Read [Fina's shared workflow](references/fina-core.md) and [financial facts](references/financial-facts.md). Check or reuse setup; missing setup must not prevent repairing the facts needed to complete it.

## Find the actual record

Start with bounded `search_transactions(detail=summary)` for the specified date/account/concept. Use the literal `query` when the user quotes a label; `merchant` alone cannot search concepts. If an expected record is absent, inspect relevant `list_events` / `get_event` for received, processing, omitted or review activity. An empty search does not prove data was never received. Read full evidence and versions only for candidates that matter.

Do not convert processing delay into a request for the user to re-enter everything. Explain relevant excluded review items; category-only uncertainty does not mean a recorded purchase is excluded. Read actual evidence before claiming a duplicate.

## Use the narrow operation

| User's intent | Operation and boundary |
| --- | --- |
| Correct a recorded purchase/payment/income | `correct_transaction` with current transaction version and the supported patch. Keep independent evidence and unchanged fields. |
| Resolve a received event missing facts | `resolve_event` with current event version and evidence-supported extraction. |
| Remove/restore a record's effect in Fina | `cancel_transaction` / `restore_transaction`, current version and reason. This does not reverse a bank charge or create a refund. |
| Relate existing refund to purchase | `link_refund`, current refund version and the actual original transaction; no duplicate refund. |
| Confirm/reject possible duplicate evidence | `resolve_transaction_match`, current event version and the supported target or null; never merge across owners or based solely on approximate FX. |
| Retry a failed received event | `reprocess_event` after reading the failure and determining a retry can help; reuse the event instead of resubmitting it. |
| Link a completed own transfer or card payment | `link_account_transfer` with observed legs and current versions, as described below. |
| Remove an incorrect transfer link | `unlink_account_transfer` with returned link ID/version and reason; preserve independent observed evidence. |
| Dismiss an incorrect card-payment suggestion | `dismiss_card_payment_suggestion` with current version, only on explicit rejection. |
| Link an existing movement to a loan | `propose_debt_payment`, then `resolve_debt_payment_suggestion` for the user's supported confirm/dismiss decision. `record_debt_payment_evidence` requires an actual observation, not an inferred principal allocation. |

For a linked transaction requiring correction/cancellation, inspect and unlink the existing relationship first when required by the live contract. Do not erase evidence to make totals agree. Resolve version conflicts with a re-read; never blindly overwrite newer facts.

## Own-account transfers and debt payments

Search the other account for the counterpart first. Prefer two existing observed legs with their exact IDs and versions. Preserve both amounts and currencies. If the other leg does not exist, `counterpart_evidence` is permitted only for a completed transfer with explicit full user/document evidence: amount, currency, date, account and reason. Never invent a leg, fixed stablecoin parity or issuer settlement.

If the user already identified the pair, reuse that authorization to correct missing direction/type and link the observed records without asking again. Backend automatic links are existing facts, not pending proposals. `automatic_debt_payment_notices` with `requires_confirmation=false` need no new confirmation. Relevant unresolved suggestions can be raised briefly once; matching a statement minimum/total is not proof of purpose or settlement. Dismissal requires an actual rejection.

Confirm the resulting change from the returned result and a focused refreshed read. Explain any remaining uncertainty, especially statement settlement or principal/interest allocation. Stop when the specific discrepancy is resolved; do not turn one correction into an unsolicited audit.
