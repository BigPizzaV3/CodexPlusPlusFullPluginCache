---
name: manage-recurring-finances
description: View, add, correct or stop tracking Fina subscriptions and expected recurring income, and reconcile them with recorded purchases or receipts. Use for renewals, paydays, recurring charges or saved subscription cleanup; changes affect Fina records, not the merchant or bank.
---

# Recurring finances

Read [Fina's shared workflow](references/fina-core.md). Check or reuse setup, then read `list_commitments` and relevant accounts before changing a record. Fina membership is separate from the subscriptions tracked here.

## Add or update

Collect missing service/payer, amount per occurrence, currency, recurrence, next known or agreed approximate date and the paying/receiving account together. Use existing account and merchant IDs returned by Fina; never invent an association. A known merchant intermediary is not necessarily the underlying service.

Use `upsert_commitment` for the user's explicit request. Existing entries require their exact ID and current `expected_version`; patch only changed fields. If the user deliberately leaves account association for later use `account_status=deferred`; otherwise keep it pending. Explain the practical forecast gap briefly.

weekly is every seven days; biweekly is every fourteen days; semimonthly is twice each calendar month; bimonthly is every two months; quarterly is every three calendar months. Amount is per charge/payment. Clarify ambiguous "quincenal" or "bimensual" and ambiguous monthly-total allocations; do not assume equal installments. Semimonthly requires two valid increasing `month_days`; use two monthly commitments for genuinely unequal dates/amounts when supported by the user's instructions.

Persist incomplete income in `update_profile.income_drafts`, preserving all other current drafts. Set approximate dates and timing notes honestly. Promote a complete draft atomically with `draft_id`. Do not present drafts as incoming money.

## Discovered recurrence and reconciliation

Potential subscriptions from statements, receipts, Gmail or Fina suggestions remain candidates until confirmed. Importing old purchases does not authorize creating a subscription. Read saved commitments to avoid duplicates; present only the relevant evidence and missing fields. Do not infer next renewal from an old isolated charge.

Use `resolve_subscription_suggestion` with its current version to resolve against the actual saved active commitment, or dismiss only on the user's explicit rejection. Silence is not rejection. Follow the backend's existing reconciliation; use `match_commitment` only for supported user-directed associations with existing transactions and the right occurrence. Expected money is not received money, and matching must not create a duplicate transaction or rewrite observed currencies.

## Stop tracking

If the user wants to stop a saved forecast, update the corresponding commitment's `active` state through `upsert_commitment`. If they ask to cancel the real service, explain that this happens with the provider; do not silently deactivate the Fina record as a substitute. An explicit complete instruction to stop tracking needs no redundant confirmation, but an ambiguous service or target does.

Confirm the saved change briefly, with next date, native amount/currency and account when useful. Refresh the relevant projection only when the user needs its consequence. Do not alter unrelated onboarding statuses or claim all subscriptions/incomes are now complete.
