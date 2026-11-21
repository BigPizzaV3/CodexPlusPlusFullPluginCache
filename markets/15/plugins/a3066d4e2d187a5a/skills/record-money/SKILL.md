---
name: record-money
description: Record requested Futoroku income, expenses, received reimbursements or account transfers with exact money, clear scope and duplicate-safe retries.
---

Read [the shared MCP contract](references/mcp-safety.md). Resolve the Space, ledger, account and category with `choose-space` before writing.

For an income or expense, use `create_transaction_record` with `body`. Supply the resolved ledger/account/category IDs, type, exact decimal amount string, account denomination and timestamp with UTC offset. Resolve missing date/timezone, account, currency or ambiguous category before saving; do not silently accept schema defaults. Use `get_finance_context` capabilities for current constraints. Respect the user's budget-inclusion choice. Omit attribution to use the authenticated creator; resolve a different payer through `list_transaction_members`.

For an account transfer, use `create_transfer_record`, with source and destination account IDs. This records money movement; it does not move funds at a bank. For different account currencies, obtain exact `amount`, `currency`, `to_amount`, `to_currency` and any fee from the user or a reviewed source. Do not calculate received money from an assumed exchange rate. `exchange_rate` must be omitted or 1 in this version. Preserve RM versus MYR as distinct denominations. A transfer is one transfer record, not an extra expense plus income.

Use `create_finance_batch` only for a user-requested coherent set of 1–100 combined entries, counting nested reimbursements. Review the complete set first; any invalid entry rolls back the set. Larger jobs require a separate reviewed manifest workflow; do not silently split work to bypass a limit.

Only money already received belongs in reimbursements. Use inline reimbursements for a new expense or `create_received_reimbursements` for a reviewed existing expense; do not record an IOU as received income.

Before each new write, retain a fresh UUID `request_id`, the explicit Space and exact arguments. Reuse all of them after a lost acknowledgement. A `client_uuid` identifies a single domain row and does not replace `request_id`; batch entries do not support it. If earlier work may already exist without a retained request identity, use narrow `search_transactions` and review candidates before adding another record. A similar record can also be a legitimate repeat: ask when uncertain, and never delete it automatically.

Report the saved record ID and key values only after a successful tool response. An uncertain result stays uncertain until reconciled. Do not interpret a ledger transfer as a payment instruction or initiate checkout.
