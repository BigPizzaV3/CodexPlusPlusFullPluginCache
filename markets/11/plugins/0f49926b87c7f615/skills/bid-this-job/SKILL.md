---
name: bid-this-job
description: Start a Grid estimate from a blank bid or independent copy, then preview supported bid settings, budget costs, and production qualifications.
---

Use the connected Grid tools for an explicitly selected existing project. Discover
projects and bids before choosing a source; resolve ambiguity with the user.

Distinguish **overage estimates** (`bids.bid_kind=overage`) from **overage
requests** (`commitments.type=overage`, an item-linked client approval form).
For a request, create or reuse a draft commitment instead of copying the base bid.
Use `grid.list_commitments` with type `overage`, then
`grid.list_commitment_items` and its preview/apply pair to link existing
cost UUIDs. Create a missing draft with commitment header preview/apply and
explicitly review `tax_percent` (request markup), `markup_includes_fringes` and
currency. Request item tools expose billability changes and derived totals;
they preserve phase, classification, approval and bid membership. Saving does
not send or approve the request. Follow returned constraints and stable request
IDs; resolve stale previews before applying.

For a blank estimate use `grid.preview_bid_create`; for an independent same-project
Estimate copy use `grid.preview_bid_duplicate`. Supply a fresh destination `bid_id`
UUID, name, project ID, and the explicit source bid ID for duplication. Display
returned defaults, copied/shared/excluded scope and warnings. Do not promise to
copy published snapshots, operational actuals, attachments or shared cost details
when the tool reports them unsupported.

Apply only the reviewed intent after confirmation, with the returned
`expected_revision`, identical IDs and values, `confirm_preview=true`, and a stable
UUID `request_id`. A changed plan or stale preview needs renewed review; an exact
retry uses the same request ID. Read the resulting bid back before reporting saved
work. A preview does not create a bid or publish a share.

Use `grid.get_bid_settings` and its preview/apply pair for supported schedule,
fee and OT settings. Percentage rates are decimals: 8% is 0.08. Use narrative
preview/apply for production qualifications and textual insurance requirements;
use budget item/detail tools for costs. These are separate confirmed actions.

Distinguish user-provided rates, existing Grid rates, and proposed estimates. Do
not present inferred prices as verified vendor quotes. Preserve canonical dynamic
merge tokens returned by discovery; plain numeric prose does not update itself.
Settings receipts provide values for a separately confirmed revert. Creation does
not authorize deletion, publication, delivery to clients or changing the primary bid.
