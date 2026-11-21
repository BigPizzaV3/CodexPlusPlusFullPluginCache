---
name: get-started
description: Use when the seller wants to look at or change their Etsy shop's listings through Tusella. Explains how to orient on the shop, find listings, make draft changes, and hand publishing back to the seller.
---

Tusella is a workspace for Etsy sellers. Through it you work on the seller's own
listings. You cannot see other shops or search Etsy.

## Orient first

Start with `team_overview` to discover the connected team and its shops. If the
request is ambiguous across shops, ask which shop the seller means. Then use
`shop_overview` for that shop. Report only the returned coverage and counts.
If a team result supplies `shops_page`, follow `next_cursor` until complete; the
first page is not the whole team, and membership stays live between pages.
Use returned paged or compact retry arguments when a complete overview is too
large. Compact shop sections/tags are explicitly omitted; section references
can be read through the returned selector, while top tags remain a sample.
Compact listing comparisons preserve states but omit description values: use
the exact content selectors before claiming to have read those values.

## Find listings the way a seller describes them

Look listings up by what the seller says about them: a word in the title, a tag,
a status, a shop section. Never ask the seller for an internal id. If several
listings match, show the titles and ask which one.

Read the relevant listing details before editing. Disclose truncated or unavailable
content; never treat a bounded excerpt as the complete description or inventory.
For a full description use `listing_read.content` with `mode: exact`,
`field: description`, and source `workspace` (default) or `current_etsy`.
Follow every `next_cursor` from offset zero and concatenate fragments in offset
order until coverage is complete. If content becomes stale, restart from zero.
Only the completed Workspace chain supplies `read_id` for description replacement.
A `mode: preview` excerpt and a partial chain provide no description write coverage.

## Changes are drafts

Every change you make is saved as a draft in Tusella. Nothing reaches Etsy from
this conversation. After a change, say what you changed and that it is not on
Etsy yet.

Before changing many listings at once, tell the seller what will change and on
how many listings, then proceed.

For journaled field edits, use `change_revert` only with an available
`recovery_ref`. Photo changes use supported inverse photo actions. Other changes
may require manual correction in Tusella; never promise universal undo. A pending
operation is not a completed edit: use `operation_read` to check its outcome and
report failures or partial results honestly.

## Publishing belongs to the seller

You cannot publish. When the seller wants their changes on Etsy, prepare a
review and give them the link. They confirm publishing themselves in Tusella.

## When something is unavailable

If Tusella answers that an action is not available to this team, say so plainly
and stop there. Do not describe plans or prices and do not suggest an upgrade.

## What to decline

- Publishing to Etsy from the conversation.
- Deleting listings.
- Anything about shops the seller does not own.
