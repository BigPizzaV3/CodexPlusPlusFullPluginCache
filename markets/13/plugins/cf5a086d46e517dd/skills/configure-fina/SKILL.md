---
name: configure-fina
description: Set up, connect, or resume Fina personal finances, including accounts, cards, subscriptions, income and optional debts or assets. Use for first use, incomplete setup discovered by another Fina workflow, connection help, or a request to continue setup. Reuse saved progress instead of restarting.
---

# Configure Fina

Read [Fina's shared workflow](references/fina-core.md). Connect the user to their saved financial context with a brief, friendly introduction and one useful next step. Do not ask permission to start after an explicit setup request.

## Read before asking

1. Discover the connected Fina tools and call `get_setup_status`. If tools are missing, follow the host's existing connection flow; never claim a connection from installation alone.
2. Use `conversation_guidance`, `onboarding.current_step`, statuses, `incomplete_accounts`, `incomplete_commitments` and saved income drafts. Keep existing IDs and values. A configured user proceeds directly to their requested task.
3. Resolve profile currency, locale and timezone from saved or reliable user context. Ask only for genuinely missing preferences in everyday language; never infer currency from language, ask for a card timezone or fabricate technical identifiers.

## Collect one block together

Follow the backend's current step order. Offer text, screenshots or a PDF in each relevant block; explain briefly what the information helps with. Extract all supported information already supplied and group the remaining questions in one message. Do not ask one field at a time.

| Block | Information and supported operations |
| --- | --- |
| Bank accounts / wallets | Institution where relevant, alias, currency, last four digits for banks, balance and observation date. Read `list_accounts`; use `create_account`, `record_balance_snapshot`, and `update_account` for existing records. |
| Credit cards | Alias, institution, currency, last four digits, dated total debt, credit limit, cutoff and due timing. Use the same identity/balance operations; use `record_card_statement` for an actual statement and its exact dates. Total debt, statement amount, minimum, no-interest payment and remaining due are separate. |
| Subscriptions | Service, price per charge, currency, frequency, next renewal and usual paying account. Read `list_commitments` before `upsert_commitment`. Detected recurring charges need explicit confirmation. |
| Expected income | Payer/source, net amount per payment, currency, frequency, arrival timing and receiving account. Save incomplete entries through `update_profile.income_drafts`, preserving other drafts; use `upsert_commitment` with `draft_id` to promote a completed draft. |
| Optional loans, properties and investments | Offer the blocks returned by setup without requiring every asset. Start with identity and dated value; read `get_account_details` guidance, use `update_account_details` for conditions and `record_account_observation` for evidence. The wealth-and-debt skill covers deeper work. |

Every account has one currency; reuse accounts rather than recreating them for a new statement. Wallet/virtual/physical digits can identify instruments of one account: use `link_instrument` only with an established association. Never change historical denomination or assume USDC equals USD.

Unknown fields stay pending, including required bank/card last digits. Save supported partial information without manufacturing zeros. Clear income instructions already authorize saving; clarify only an ambiguous monthly total, installment distribution, currency or timing. Twice monthly, every 14 days and every two months differ. A date agreed for an approximate forecast stays `date_precision=approximate` with its timing note.

## Save progress honestly

Read the current profile before changing statuses. Use `update_profile` and the live schema:

- Bank/card/optional wealth statuses: pending while collecting; completed only after the user's requested records and necessary data are saved; none only for an explicit declaration; skipped only when the user chooses later.
- Subscriptions: confirmed for saved chosen subscriptions or explicit none; skipped for later.
- Income: persist pending/completed/none/skipped, retaining unresolved drafts on deferral. Saving one income does not declare the block finished.
- Do not set history coverage from setup completion. Only the user's explicit coverage assertion can establish it.

Re-read `get_setup_status` after each block. Returned missing fields override a stale completion flag. Honor an explicit request to return to a deferred block; never reopen it merely because another chat begins.

## Documents, channels and handoff

A setup document can provide several blocks at once. Save only the requested setup facts. If it also contains purchases, offer importing them separately; the import-financial-data skill handles the preview. Confirm potential subscriptions independently of past-purchase import.

WhatsApp and phone capture are optional. Offer the existing [connection settings](https://mcp.finamoney.co/connections) when relevant, using the user's language. Do not claim a phone automation, WhatsApp pairing or capture is active without returned evidence. Do not require either channel before using the MCP.

End with what is saved and the relevant remaining step. Resume the original dashboard, review or planning request after setup; do not make the user repeat it. If a required field or connection remains missing, say exactly what is needed, without pretending the dependent workflow finished.
