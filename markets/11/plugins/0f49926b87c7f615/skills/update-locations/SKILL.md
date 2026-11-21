---
name: update-locations
description: Preview and confirm edits to existing Grid location descriptions and technical specifications, preserving omitted fields and distinguishing canonical edits from pending suggestions.
---

# Update an existing Grid location

Use `grid.search_locations` to find the existing location and resolve ambiguous matches with the user. This workflow uses an existing master-location ID; creating a facility or stage belongs to the location-import workflow.

1. Read the current schemas of `grid.preview_location_update` and `grid.update_location`. Prepare only supported requested text fields and technical specifications. Do not route unsupported address changes through these tools.
2. Call `grid.preview_location_update` with the selected `master_location_id`, a fresh intent `request_id` UUID, and requested updates. Preserve supplied units and uncertainty. Omitted fields remain unchanged; null clears only supported optional fields. Do not infer missing measurements or clear unrelated technical specifications.
3. Show current and proposed field differences, warnings, technical conflicts, and the direct-edit or pending-suggestion disposition. Resolve conflicts with the user and preview again if the intent changes.
4. After confirmation, pass the returned plan unchanged to `grid.update_location` with `confirm_preview=true`. Do not edit the plan's submitter, expected state, revision, or disposition to bypass a rejection.
5. For an identical retry, reuse the same plan and request identity. If state or authority changed, obtain a fresh preview and confirmation. Report the receipt's actual status, including pending review, unchanged, or approved; a successful pending submission is not a canonical edit.
