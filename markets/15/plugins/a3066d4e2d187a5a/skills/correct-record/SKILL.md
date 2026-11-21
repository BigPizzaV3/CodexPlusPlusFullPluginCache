---
name: correct-record
description: Correct explicitly identified Futoroku financial records or delete confirmed targets while checking identities, current revisions and reimbursement effects.
---

Read [the shared MCP contract](references/mcp-safety.md). Resolve the approved Space, find candidates with `search_transactions`, then use `get_transaction_record` to read each exact target. Ask the user to select when candidates are ambiguous. A statement, receipt suggestion or search match does not independently authorize an edit.

For an authorized edit, use `update_transaction_record` with `update.transaction_id`, the freshly returned `expected_updated_at` and only requested fields in `update.changes`. Omission preserves a field; blank tag/remark clears it, and explicit null can have a distinct effect. Do not send a whole record as a patch. Transaction type cannot change; income/expense currency cannot change through this edit. Transfer account/currency changes must satisfy the exact received-leg rules. Never work around validation by deleting and recreating a record without a separate request.

For 1–100 explicitly reviewed records, `update_transaction_records` performs an atomic batch. Keep an individual current revision per item. Changes must satisfy reimbursement constraints in request order; review their consequences instead of quietly removing linked income. Do not fan out writes after an atomic failure.

Before permanent deletion, show the exact IDs, dates, amounts and consequences and obtain explicit confirmation for those records. Then re-read their identities/revisions and call `delete_transaction_records` with each `transaction_id`, `client_uuid`, `expected_updated_at`, `confirmed: true`, explicit `space_id` and a retained UUID `request_id`. Linked reimbursements can block expense deletion; discuss the separate requested action. Never delete a suspected duplicate merely because it looks similar.

To link an existing received income, review both records and timestamps, obtain confirmation, then use `link_received_reimbursement`. To remove a received reimbursement use the tool's reviewed identities, timestamps and confirmation; explain that it deletes the linked income and changes reports. Do not record expected future money as received.

On `stale_revision`, stale identity or a changed relationship, re-read, present the changed state and obtain renewed review before constructing a new operation with a new UUID. On an uncertain acknowledgement, keep the original UUID, Space and exact arguments; do not change the request or switch Spaces. Report only confirmed outcomes and include the resulting record ID or deleted IDs.
