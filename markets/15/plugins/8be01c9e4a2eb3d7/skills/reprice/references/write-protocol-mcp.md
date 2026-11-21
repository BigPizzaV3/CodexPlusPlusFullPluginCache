---
version: 1
---

# Write protocol

Patina has two kinds of write. Staged writes change nothing until the user approves. Direct writes run the moment you call them. Know which one you are holding before you call it.

## Staged writes

`propose_listing`, `propose_listing_update`, `propose_listing_end`, `propose_sale` and `propose_sale_reversal` change nothing. Each returns a proposal: an `operation_id`, an `expires_at` and a `preview`.

- Say in plain words what you intend and the values you will use before you stage it.
- Stage with thin inputs: the IDs, the destination, the price, and what the user said. Do not pad the call with fields the user did not give.
- Show the preview. Do not restate or reformat what the preview already shows.
- Call `confirm_operation` only on the user's clear yes to that preview, within 30 minutes of the proposal. Never confirm on your own judgment.
- On a no, call `decline_operation`. The request is then closed: do not stage it again unless the user asks again.
- One proposal per intent. If a proposal is waiting, wait on the user. Never stage the same change twice.
- One write per confirmation. Several changes go one at a time; let each resolve before the next.
- `operation_stale` means the record changed after the proposal: tell the user what changed, re-read it, and propose once with fresh values. Do not loop.
- `external_outcome_unknown` means the write is still running: check `get_operation` and do not confirm again.

## Direct writes

`add_inventory_watch`, `update_inventory_watch`, `record_watch_cost` and `update_sale` write when called. Confirm the values with the user first.

- Every direct write takes an `idempotency_key`: 8 to 128 characters of letters, digits, `.`, `_`, `:` and `-`. Use `<skill>-<16 hex>`, for example `intake-3f9a0c27b1d4e865`.
- One fresh key per intent. A repeat call with the same key and the same arguments returns the first result and writes nothing. Never reuse a key with different arguments: that returns `idempotency_mismatch`, and the fix is a new key for a genuinely new write, not a retry.
- On `internal_error` or a timeout, call `get_operation` with the returned `operation_id` before you repeat anything. With no `operation_id`, read the record back instead. Repeat only when the write did not take effect, and then with the same key and the same arguments.
- Every write result carries an `operation_id`. Keep it until the job is done.
