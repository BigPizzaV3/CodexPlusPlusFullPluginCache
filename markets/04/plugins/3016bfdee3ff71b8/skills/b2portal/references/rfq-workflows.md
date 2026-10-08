# RFQ workflows

Read only the sections relevant to the user's current task.

## New intake context

Call `get_intake_context` before creating a new intake. Use only an authorized
location it returns. If the user's wording identifies exactly one location,
use it; otherwise present the relevant location distinctions and ask for the
selection. Keep the returned `locationId` unchanged through that intake's
forwarding, upload, creation, and status calls.

For work on an existing RFQ, begin with the corresponding RFQ read tool and its
current authorized location. Change that location only through an exact,
current `RESOLVE_CUSTOMER_REVIEW` target when the user requests the correction
and B2 Portal authorizes the selected active location. Re-read the RFQ after the
action and use the location returned by the updated state. Do not substitute a
different location ID in unrelated calls. Do not restart new-intake setup unless
required information is genuinely unavailable.

## Original email

Use `prepare_email_forwarding` when the host can forward the original message
and original attachments through its existing email connection. Use a stable
idempotency key for that preparation. The returned marker is one-time and
short-lived: never display, log, reuse, or treat it as an upload token.

After forwarding, poll `get_rfq_intake_status` with the returned intake ID. Do
not create a second intake for the same message. Preserve any returned
`reviewUrl` exactly.

## Notes and standalone attachments

Use this path for pasted notes, meeting or phone summaries, and files that are
not being forwarded as an original email:

1. Create one caller-generated UUID `requestId` for the intake.
2. For each file, call `prepare_rfq_attachment_upload` with that `requestId`, a
   stable idempotency key for that file, its exact filename, allowed MIME type,
   and byte size. Never put file bytes in MCP JSON.
3. Have the signed-in operator complete the returned `uploadPageUrl`. Use
   multipart fields only through a separately certified adapter.
4. Pass each returned attachment object unchanged to `create_rfq_from_notes`
   with the same `requestId` and a new stable intake idempotency key. Respect
   the server's current file count and notes requirements.
5. Poll `get_rfq_intake_status`; report processing and hold states rather than
   creating a duplicate intake.

Do not substitute the forwarding path for standalone uploads or vice versa.

## Customer and contact resolution

Use `get_rfq_customer_resolution` for RFQ-scoped customer review. Keep its
extracted identity, current local record, and CoreBridge candidates distinct.
Use `search_accounts` for a bounded location-scoped search and
`search_contacts` only beneath one selected account.

An exact user-supplied identity or one unambiguous evidence-supported result may
be applied. Never select the first candidate by position. When candidates remain
plausible, explain the distinguishing facts and ask the operator to choose.

For an order-backed `CUSTOMER_CONFIRMATION`, use `existing_customer` with the
exact authorized local customer ID when retaining or replacing a local record.
When `search_contacts` returns the exact existing CoreBridge contact, use
`corebridge_contact` with that exact `coreBridgeContactId`. Use
`existing_contact` only for an authorized local B2 Portal contact, and include
its current `coreBridgeContactId` when retaining a known binding. For
`STALE_CONTACT_INFO`, select the current CoreBridge contact or ask the operator
to choose; do not invent a new contact. Directory IDs are canonical decimal
strings; when the draft-action schema requests a numeric CoreBridge ID, convert
the digits exactly to a positive integer and never round or infer the value. A
returned CoreBridge account may be linked with an existing or new account-scoped
contact when the correction contract permits it. Use `new_customer` only for a
pre-order `MISSING_CUSTOMER` review.

## Review and synchronized catalog

Read `get_rfq_review_context` immediately before triage or amendments.
`get_rfq_triage_context` is a compatibility alias and should not be introduced
into new operator guidance.

- `search_v2_catalog` performs bounded text search over synchronized local
  CoreBridge V2 data.
- `list_v2_quickproducts` provides deterministic pages; follow `nextCursor`
  only when the task requires more results or a complete list.
- `get_v2_quickproduct` reads one returned product and its bounded part pages.
- `search_rfq_line_quickproducts` ranks candidates for one exact, current RFQ
  line decision.

Treat product status, freshness, price provenance, dimensions, materials,
finishes, restrictions, and parts as evidence. A weak or stale candidate is not
an approval. If no supported match exists, use a catalog-gap or review action
rather than inventing a product.

## Commercial documents and amendments

Use the current review context to reconcile only the selected commercial
document lines supported by the action contract: exact line IDs, descriptions,
quantities, and unit prices. Do not infer that shipping, discounts, fees, tax,
or document totals are writable when the current tool schema does not expose
them.

An amendment changes the existing versioned draft; it is not a new intake.
Read the current customer-resolution or review target, apply the smallest
authorized correction, then read the updated context. Do not let a customer
amendment silently alter line pricing or let a line amendment silently alter
customer identity.

## Status and review links

Use the exact absolute `reviewUrl` returned by the latest intake, status,
customer-resolution, review, or draft-action result. Never build one from a
host, RFQ identifier, route, or query string. If a response lacks a URL, use
the relevant status or review read instead of manufacturing one.

CoreBridge push is not a status shortcut. Use the dedicated final-approval
workflow only after the latest review context reports no blocker.
