---
name: manage-cost-tags
description: Find or create a Grid project cost tag through a confirmed preview, reusing active matches and keeping tag creation separate from budget changes.
---

# Find or create a cost tag

1. Resolve the project through `grid.list_projects` or an established project UUID. Call `grid.list_cost_tags` with the proposed name when available. Tags belong to the project and can be used across bids; absence on one budget row does not mean a tag is missing.
2. Reuse a unique active exact match. Present ambiguous matches for selection. Archived matches require a separate decision in Grid; these tools do not restore or rename them. Keep cost tags separate from free-text notes.
3. If a new tag is intended, call `grid.preview_cost_tag_create`. Show the project, normalized proposed name, scope, and any existing-match outcome. Stop at the preview when the user only asked to explore.
4. After confirmation, call `grid.create_cost_tag` with the exact name and project, returned `expected_revision`, a fresh `request_id` UUID, and `confirm_preview=true`. Preserve identical arguments and UUID on retry. A stale result or changed name requires a new preview and confirmation.
5. Return the canonical tag ID and actual creation/reuse result. If tagging budget details is also requested, regenerate `grid.preview_update_details` with that ID and obtain separate confirmation before `grid.apply_update_details`. Creating a tag does not itself authorize changing financial rows.
