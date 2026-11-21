---
name: import-talent
description: Preview and import a supplied talent list into a Grid project, reviewing parsed fields, exact-email contact reuse, exclusions, and confirmation before creating memberships.
---

# Import talent into Grid

Use the connected Grid MCP tools and their current schemas.

1. Resolve the destination with `grid.list_projects` or an established project UUID. Obtain the supplied talent text. If working from a spreadsheet, convert supplied rows into the supported text format: one person per blank-line-separated block, starting with the name and followed by their supplied contact and talent details. Preserve information; do not invent emails or roles.
2. Call `grid.prepare_talent_import`. Show parsed people, roles, validation problems, and every proposed contact create/reuse decision. Exact-email reuse is distinct from similarity by name. Do not choose between ambiguous contacts or force a different contact ID into a returned decision.
3. Ask the user to correct invalid or ambiguous rows or explicitly exclude them. Use the tool's 1-based `exclude_indexes` and prepare again after changes. Keep the returned row fingerprints and decisions associated with the exact reviewed text.
4. Obtain confirmation of the included people and create/reuse choices. Call `grid.apply_talent_import` with the same project, text, exclusions, returned `contact_decisions`, and `confirm_preview=true`. Do not fabricate revision or retry-key parameters absent from this tool's schema. If matching has changed, prepare again and show the new decisions before applying.
5. Report the actual created/reused contacts and project memberships, skipped rows, and errors from the result. An import does not send messages or establish that talent has accepted a booking. Do not claim success from the prepare response.
