# Checkpoints and resume

Keep a compact checkpoint in the host's existing private working artifact/session persistence, with a reference the user can reopen. Do not create a Grid database/table, shadow ledger or new task merely for this workflow. If durable host storage is unavailable, return the checkpoint to the user and explicitly report that automatic cross-session resume is unavailable. Grid's records and durable action receipts remain authoritative; a checkpoint stores navigation/retry identities, never balances or authorization.

The optional `scripts/resume.py` helper validates an ID-only checkpoint and returns a readback/resume inventory. Run with `python3 <skill-directory>/scripts/resume.py <checkpoint.json>`. It makes no network calls or writes, cannot approve/apply actions, and cannot verify Grid state. An inventory is not permission to skip a step. This resource is packaged alongside the skill for hosts with Python; other hosts can follow this contract directly.

Checkpoint format, version 1:

- `project_id`: verified Grid project UUID.
- `records`: only known IDs. Canonical UUID fields: `payee_id`, `project_company_id`, `bid_id`, `document_id`, `file_id`, `prior_document_id`, `payable_id`, `commitment_id`, `payment_id`, `transaction_id`; UUID arrays: `detail_ids`, `application_ids`. Opaque nonempty ID fields: `thread_id`, `draft_id`, `message_id`, `summary_artifact_id`.
- `stages`: entries from `attachment`, `import`, `po`, `payment`, `application`, `reconciliation`, `remittance`, `send`. Each has `status`: `pending`, `applied`, `blocked`, `uncertain`, or `not_requested`. Optional `idempotency_key` and `preview_id` retain attachment retry identity. Optional `request_id` is a stable UUID for the exact intent, and `receipt_id` is a returned opaque receipt/audit ID. `reason` is a short blocker code, never invoice/bank contents. “Applied” is a historical checkpoint assertion pending fresh readback. Preview alone remains pending.

Keep the exact approved tool request and preview tokens in the host's existing private action history referenced by request ID, without putting sensitive payloads in a general checkpoint. If exact prior arguments are lost, read records and supported receipts first; do not reconstruct an uncertain write under a new request identity. Do not copy credentials or financial source documents into checkpoints. Never serialize a reusable email-send approval.

Readback requirements:

| Stage | Re-read before advancing |
| --- | --- |
| attachment | Authorized document/file and active target evidence; confirm actual copied/reused outcome |
| import | Fresh import context, saved detail IDs and allocations, AP and document-family evidence |
| po | Commitment/header and context, internal/unissued status and any item-link limitations |
| payment | Payment, payee/currency/method and source evidence; inspect duplicates |
| application | Both payment and payable, active applications and canonical remaining balance |
| reconciliation | Payment and bank transaction, allocation and matching relationship |
| remittance | Exact sanitized summary artifact and saved draft, verified original thread/recipients |
| send | Sent message ID and exact thread/attachment; uncertain result must be checked before retry |

On resume:

1. Load the checkpoint and inspect the current user intent/restrictions. A missing checkpoint is not permission to re-create records; rediscover existing records by source family and canonical identities.
2. Resolve all uncertain outcomes before dependent work. For financial/import mutations with receipt replay, retry only the identical authorized request with its original UUID; replay can recover a committed receipt even after preview expiry. Then read current state. For uncertain email sends, inspect sent/draft state and stop if it remains unknown; never blindly resend.
3. Read back saved IDs, relationships and source revision. Deleted/inaccessible/changed records are unresolved; the checkpoint does not override them. Reread source files after a draft-to-final transition; align the final family version rather than treating a changed filename as a fresh invoice.
4. Mark only currently verified matching work as reusable. Preview each outstanding supported mutation, show its actual impacts and obtain the approval required by its skill. Renew preview/confirmation when intent, state or expiry changes. Keep successfully applied earlier stages if a later stage blocks.
5. Report the last verified stage, pending IDs/uncertainty, capability/blocker code, and the next supported action. Resume a blocked method/thread/bank step only after verifying the capability/data now exists. Never convert a blocked stage to success because a sibling stage succeeded.
