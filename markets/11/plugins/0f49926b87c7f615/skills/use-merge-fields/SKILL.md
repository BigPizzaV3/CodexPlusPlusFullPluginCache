---
name: use-merge-fields
description: Discover and use Grid merge tags in dynamic text, templates, and bid details; preview resolved values and save supported bid narrative changes through Grid MCP.
---

# Use Grid merge fields

Use the connected Grid tools and their current schemas. Merge tags are stored text references used across Grid UI surfaces. Keep the tag in the saved source so the displayed value can follow its current context; a rendered value is a preview, not a replacement for the tag unless the user asks for fixed text.

Resolve the project and selected bid using `grid.list_projects` and `grid.list_budgets`, reusing unambiguous conversation context. Use returned UUIDs. Discover globals with `grid.list_project_globals` in the selected bid context. Use each returned `merge_tag` exactly; inspect `effective`, `resolved_value`, `rendered_value`, unit, and resolution errors. Follow pagination when needed. Names and values can differ by project and bid: never invent a global or use an overridden project value for a bid.

For bid text, `grid.get_bid_settings` with `sections: ["narrative"]` (read `sections.narrative`) returns stored fields, rendered previews, unresolved tags, and available `bid_merge_fields`. For example, discovered tags might produce `Wardrobe 3 @ {global:Wardrobe Rate}` or `Shoot for {bid:Studio Shoot Days} day`. These example names are not guaranteed to exist. Use canonical returned global tags when authoring; preserve existing supported display-name or short-code aliases when editing unrelated prose.

Use the tool's rendered values for currency, percentages, time, and duration. Percentage globals use decimal storage (`0.10` renders as `10%`); zero is a real value. Preserve paragraphs, Markdown, punctuation, and omitted fields. Keep unresolved tags visible and explain which context or field is missing. Do not guess their values, silently remove them, or change the underlying globals merely to make a text preview resolve.

## Budget lines and cost-tag totals

Discover `budget_references` with `grid.get_bid_settings` with `sections: ["narrative"]` (read `sections.narrative`) for the explicit selected bid. Match lines by `line`/`label` and cost tags by `label`, then choose the intended Estimate or Running phase and amount basis. Each source/phase has `base-estimate` (Before fringes) and `cost-with-fringe` (With fringes) variants. Inspect `amount_basis_label`, `amount_basis_description`, and the live amount before choosing. Follow explicit user intent; ask when the basis is ambiguous. If the deployment does not return a requested basis, report that limitation rather than constructing a token. Use `grid.list_budgets` to distinguish multiple bids; `is_primary` identifies the primary but does not override a user-selected bid. If the target remains ambiguous, ask before selecting it. Each narrative context resolves only its selected bid; do not insert a sibling bid reference into that narrative.

Insert the exact returned `token` for value-only display, or `key_value_token` for label plus value. Inspect `formatted_value`, `display_label`, `key_value_formatted_value`, and `resolution_error`. A line can render `$900.00` or `Line 100: $900.00`; a cost tag can render `$900.00` or `Wardrobe: $900.00`. Do not construct ID/name/line-number aliases or use a null preview as zero. If the connected deployment does not return the requested display mode, report the limitation.

The UI uses `$` to open the picker for both lines and cost tags and double-click to switch display modes. MCP saves canonical `{budget:...}` or `{=budget:...}` tokens; `$Bid:100` and `#Wardrobe` are not budget merge tokens. Preserve the original bid and phase when bids transition; the amount stays dynamic within that original phase. Changing display mode must not change reference identity. Both bases include OT and detail adjustments; only `cost-with-fringe` includes fringes. Both exclude top-sheet fees and insurance. Preserve existing token bases unless asked to change them; individual allowance choices do not change the overall bid total. The UI selects bid → line/tag → phase → amount basis → format, skipping already determined bid/phase steps. MCP can select these from one discovery response. Overlapping cost tags must not be summed as disjoint totals.

## Preview Message Templates

For a reusable crew email, text message or task draft, discover purposes, supported
formats and templates with `grid.list_message_templates`. Resolve the exact project
and crew recipient first; use the project-member `crew_id` when a person has more
than one membership. Call `grid.render_message_template` with that explicit context,
the chosen `format`, and a purpose or selected template ID. Resolve multiple matching
templates explicitly rather than choosing silently.

Use the returned draft, resolved fields, source context and warnings. The tool uses
Grid's shared merge engine; do not perform independent substitutions or infer dates,
positions or rates. Missing, conflicting or unconfirmed context stays explicit. A
different recipient or project requires a new render. `task` is a title/body output
shape, not a delivery channel. Rendering does not send messages, save drafts, create
tasks, book crew, change availability or grant access. Those actions require their
own supported workflow and authorization.

## Edit saved Message Template content

When available, use `grid.get_message_template` with the exact saved UUID to read
raw subject/body, revision and edit authority. Seed slugs are not saved UUIDs.
Readability does not imply edit authority. Personal owners and company admins can
edit their templates; shared built-ins require platform-admin authority.

Use `grid.preview_message_template_update` with that revision and only requested
subject/body changes. Omitted fields stay intact; explicit null clears a field.
Keep custom prose, whitespace, raw tags and signatures. Show the complete before/
after and validation warnings, including unknown fields preserved literally and
fields unresolved without recipient context. Rates still require confirmed
recipient-specific deals; never substitute budget allowances.

After the user confirms the exact stored preview, call
`grid.apply_message_template_update` with its `preview_id`, a new `request_id`, and
`confirm_preview=true`. After uncertainty, retry the same preview and request IDs;
never create a replacement intent to resolve an uncertain save. An applied receipt
replays without overwriting later edits. Stale/expired previews require a fresh
read, preview and confirmation. To restore earlier content, use the receipt's
before-values through a new preview and confirmation. This does not send messages,
create bookings/invitations, edit defaults or change template ownership. If the
connected deployment lacks these tools, report the limit; do not claim a save.

## Save bid narrative text

Call `grid.preview_bid_narrative_change` with only the requested fields and raw tags intact. Present the before/after rendered text and any unresolved tags. This tool supports bid details and the narrative fields in its schema, not financial fees, schedule changes, OT settings, bid creation, or arbitrary document/template writes. The current MCP context resolves the selected bid’s budget references, globals and returned bid schedule tags; other UI-supported tags may remain unresolved in MCP. If a tool is unavailable in the connected deployment, report that limitation rather than claiming a preview or save occurred.

Apply the confirmed preview with `grid.apply_bid_narrative_change`, the identical proposed values, returned `expected_revision`, a fresh `request_id` UUID, and `confirm_preview=true`. If the text or underlying revision changes, preview again and confirm the new result. Retry a transient response failure with the identical request and UUID. Report the apply receipt's saved values; a preview alone does not save. To revert, submit returned `revert_values` through a fresh preview and confirmation.

For other text surfaces, use their available read/preview/write tools and supported field catalog. This shared tag convention does not imply that MCP can edit every place the UI uses tags.
