# Versioned draft actions

Read the latest `get_rfq_review_context` or
`get_rfq_customer_resolution` result immediately before writing. Copy one
complete target unchanged, keeping its `type`, `id`, and `version` paired.

Call `apply_rfq_draft_actions` with:

- the authorized location and RFQ identity from current B2 Portal state;
- one target domain per call;
- a stable idempotency key for the exact semantic request;
- only fields accepted by the action discriminator;
- a concise reason and one to five concrete evidence strings; and
- current decision and QuickProduct versions where required.

Do not expose hidden reasoning as evidence. Use observable facts from the
request, source material, current RFQ, user decision, or synchronized catalog.

## Action selection

| Action | Contract |
| --- | --- |
| `MATCH_QUICKPRODUCT` | Use the exact line decision and QuickProduct identities and versions. |
| `ADD_CUSTOM_LINE` | Add a new description and quantity with an explicit or nullable unit price and the current line-items fingerprint. |
| `SEND_AS_CUSTOM_LINE` | Convert an existing line using its exact decision version and nullable unit price. Do not send description or quantity; the source decision owns them. |
| `CORRECT_LINE_ITEM` | Replace the source description and quantity. Send it alone, then re-read because it rebuilds the line decision. |
| `EXCLUDE_LINE_ITEM` | Exclude one exact current line decision with evidence. |
| `SET_EXPLICIT_PRICE` | Apply a positive operator- or source-authorized price to the exact selected QuickProduct and line versions. |
| `MARK_CATALOG_GAP` | Record that the synchronized catalog does not support the required product. |
| `HOLD_FOR_REVIEW` | Preserve the line for an operator decision with a specific reason. |
| `RESOLVE_CUSTOMER_REVIEW` | Apply the exact customer/contact/account/location correction supported by the latest customer-resolution target. A location correction is valid only when the current target and tool contract authorize the selected active location; re-read before later calls. |
| `RECONCILE_COMMERCIAL_DOCUMENT` | Reconcile selected document lines using current line IDs and supported description, quantity, and unit-price corrections. |
| `RESOLVE_QUICKPRODUCT_BUNDLE` | Apply the current bundle decision as `approve_bundle` or `review_individual_lines`. |

Custom-line pricing has distinct paths. Use `ADD_CUSTOM_LINE` for a new line,
`SEND_AS_CUSTOM_LINE` when the existing extracted line retains its description
and quantity, and `SET_EXPLICIT_PRICE` when an already selected QuickProduct
needs an explicit price. Do not attach a price to `CORRECT_LINE_ITEM`; read the
replacement decision before applying the appropriate pricing action.

## Concurrency and verification

On a stale target, changed decision, or version conflict, discard the old write
payload and read current state. Do not retry stale content with a new
idempotency key.

After an applied action, read the latest review context. Report the returned
state, changed fields, blockers, readiness, and exact `reviewUrl`. `APPLIED`
means the B2 Portal draft changed; it does not mean CoreBridge changed.
