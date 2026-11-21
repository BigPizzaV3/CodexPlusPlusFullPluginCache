---
name: review-and-undo
description: Show what AI changed on a WordPress site and roll back specific changes. Use when the user asks what changed, wants to review recent edits, or wants to undo something.
---

# Review and undo changes

Before each operation, read `operation_help` with its exact name for complete field and safety guidance.

1. Identify the site (`sites_list`, or the default site if one is set).
2. Call `changes` with `limit: 20`. Summarise newest first, grouped by day: what changed, which page/post/setting, and whether it can be undone. Keep it short; offer details on request.
3. For a specific change the user asks about, call `change_detail` and explain the before/after in plain language.
4. To undo:
   - Confirm with the user which change, restating it in one line.
   - Call `undo` with that `change_id`.
   - If the site requires confirmation or approval in wp-admin, share its approval link and wait; retry the identical call after the person approves. Never send `confirm: true` or approve on the site's behalf.
5. Report the result, including anything the site flagged as not reversible.

Undo only what the user asked for. Never undo several changes on your own initiative.
