---
name: fix-failed-listings
description: Find and fix listings a marketplace rejected (wrong size, brand, category, price or wording) and resend them. Use when the user asks why a listing failed, says items didn't post, or wants rejected listings fixed.
---

# Fixing rejected listings

1. Call `list_drafts` with `status: "failed"` (add `channel` if the user named a marketplace).
2. For each draft, say which marketplace refused it and its `reason`, in plain words.
3. Choose corrected values only from the product's own details, and only for fields marked
   `editable: true`. For a `select` field, use one of its `options`. Never invent a size or brand. If
   the right value isn't in the product, ask the user.
4. Show the proposed edits and **ask for confirmation**, then call `approve_draft` with `draft_id` and
   `edits`.
5. Read `state`: `listed` means it's live. `pending` means it's accepted and publishing shortly, so
   don't resend it. `failed` comes back with a new `message`, so try once more at most, then explain.
6. For a failure the drafts don't explain, ask `ask_intesa`. It can read the listings log.
