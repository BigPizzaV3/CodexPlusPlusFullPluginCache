---
name: seminai-operations
description: Prepare and review Seminai operation drafts with explicit product quantities, supporting evidence and user approval.
---

Identify the authorized company, production units and products. Require explicit total quantities and units; distinguish totals from per-hectare rates. Use applicable source documents and avoid inventing agronomic rates or certifying conformity.

Prepare a structured proposal with a stable requestId. Saving the draft itself requires a user click; read its status after the approval receipt. Applying it is a separate approval. When READY, use seminai_execute_operation_proposal to prepare the approval card if available. The user reviews quantities, current labels and applicable rules and confirms with its button. Otherwise use the authenticated Seminai review link.

Use seminai_start_task only for the explicitly advertised check kinds. Starting or requesting cancellation requires a user click. Poll status no faster than pollAfterMs and distinguish PARTIAL, OUTCOME_UNKNOWN and CANCEL_REQUESTED from completed or actually cancelled work. A check never applies its suggested changes.

If evidence or quantities change, prepare a new proposal and approval. Do not reuse an expired or stale approval, invoke hidden confirmation tools as the model, or repeat an uncertain execution with a new requestId.
