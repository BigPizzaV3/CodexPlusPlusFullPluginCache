---
name: manage-companies
description: Find, create, or update Grid company records through reviewed previews, including hierarchy, contact information, address choices, and admin versus pending-review outcomes.
---

# Manage Grid companies

Use current Grid MCP schemas and preserve the user's requested fields and scope.

1. Search with `grid.search_companies` using supplied name, domain, or contact facts. Distinguish matched, suggested, conflicting, and unmatched results; ask about ambiguous identities. Read a selected record with `grid.get_company`. For a lookup-only request, return approved information and stop.
2. For creation, reuse an explicitly selected visible company where appropriate. Use `grid.preview_company_create` with the supported action and company ID: an existing ID for reuse, or a newly generated UUID for a new company. Keep that ID through the approved creation. Do not invent a parent relationship or create an organization merely because a search returned no accessible match.
3. For edits, use `grid.preview_company_update` with the current company revision from `grid.get_company` and a request UUID. Send only intended changes, preserving omitted values. Show current and proposed fields and any hierarchy or contact changes.
4. Address previews contact Google. Show normalization, corrections, and verification choices. Obtain corrected input for a fix verdict; if the provider is unavailable, let the user choose retry or explicit `save_unverified`. Preview selected candidate fields again. Carry only the signed confirmation bound to the approved fields. A stored address `target_id` belongs to its existing owner; copy address fields without that ID when proposing a separate owned address.
5. After confirmation of the displayed proposal, call `grid.create_company` with `confirm_create=true` or `grid.update_company` with `confirm_update=true`, using the exact reviewed fields and relevant revision/confirmation evidence. A stale revision requires a fresh read, preview, and confirmation. Preserve the original request identity for an identical retry.
6. Report each field's actual outcome. Authorized admins may update approved values directly; other changes may remain pending for review. Never describe a pending suggestion as an approved directory change.

## Notes and insurance requirements

Read `update_details` before editing. `notes.state=available` with `value=null` means empty; `inaccessible` or omitted values never mean empty. Private notes require active company-admin or platform-admin access. Never replace unseen notes. `notes_append` preserves existing bytes and appends one newline and the supplied text; it cannot coexist with `updates.notes`. A string in `updates.notes` replaces exactly; null (or empty string) clears; omission preserves.

Use `coi_holder_profile` patches with canonical `coi_holder_text`, `coi_description`, and `insurance_requirements` (the UI's Insurance Needs). Missing profile and inaccessible profile are distinct states. Omitted fields and existing `source` are preserved. Keep requirement modality, conditions, source/document references, and applicability in the existing free-text requirements field. This is not a policy, proof of coverage, or issued certificate. Never copy private booking URLs, tokens, or unrelated contract details into directory requirements. Select the exact venue company; do not apply its requirements to the parent or other venues.

Show preview `target` and every `field_changes` current/proposed value. Non-admin profile corrections become canonical COI-profile review suggestions; pending proposals do not change approved UI values. Inspect each receipt outcome, then call `grid.get_company` again for actual readback. Its revision covers company, notes, canonical profile (including absence), and existing review/contact context. Intervening changes require fresh read/preview/confirmation and a new request UUID; identical retries retain their UUID and intent.

## Add an existing company as a project vendor

Company directory reuse and project membership are separate operations. `grid.create_company` with `use_existing` does not attach the company to a project.

Resolve the project with `grid.list_projects`, search with `grid.search_companies`, and resolve ambiguous candidates explicitly. Read `grid.list_project_vendors` with the project and optional directory `company_id`; include archived memberships when checking existing relationships and follow pagination. It returns project membership UUIDs separately from directory company UUIDs and includes other project roles to reveal conflicts.

Use `grid.preview_project_vendor_link` with the selected `project_id`, directory `company_id`, and `company_role: vendor`. Show the exact project/company identities, before/after memberships, billing-parent effects and blockers. Ask for explicit decisions before setting `restore_archived`, `replace_role`, `promote_to_manual`, or `include_billing_parent`; then obtain a fresh preview. Never change global directory classification to accomplish project linking. Duplicate/ambiguous memberships must be resolved in Grid.

After explicit confirmation of the complete unblocked preview, call `grid.apply_project_vendor_link` with its `preview_id`, `revision`, a stable caller-minted `request_id` UUID and `confirm_preview: true`. Preserve all four fields for an identical retry after an uncertain response. Changed intent, expired or stale previews require fresh preview and confirmation. Verify the returned IDs through `grid.list_project_vendors` using the returned readback selectors. A replay receipt records the original outcome; current readback may reflect later edits. This operation creates no booking, financial record, invitation or communication.
