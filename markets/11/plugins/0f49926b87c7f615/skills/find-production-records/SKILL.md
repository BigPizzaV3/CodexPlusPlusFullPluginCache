---
name: find-production-records
description: Find contacts, companies, locations, and stored addresses in Grid, resolve ambiguous matches, and inspect approved company or project-contact details without changing records.
---

# Find Grid production records

Use only the connected Grid read tools for a lookup request.

- For people, use `grid.search_contacts` with supplied names, email, phone, or profile facts. To inspect project roles and contact details, resolve the project with `grid.list_projects` and call `grid.get_project_contact` using the returned contact and project IDs.
- For project vendor/company rosters, use `grid.list_project_vendors` with the resolved project ID, optional directory company ID, and archive filter. Follow `pagination.next_after` while `has_more` is true. Directory company IDs and project membership IDs are distinct; this read creates no membership.
- For project rosters, resolve the project with `grid.list_projects`, then use `grid.list_project_contacts`. It includes Crew, Talent, and Other by default; optionally filter `role`. Follow `next_cursor` with the same filters until `has_more=false`, even after an empty page. Roster results omit representation by default (representation=null). Set include_representatives=true only when the request needs person-level agent/manager representation, and preserve that choice on every page. Use returned `contact_id` with `grid.get_project_contact` for details or `grid.get_contact_representatives` to refresh representation. Representation from those tools is person-level; project-member-specific links are separate. A blank project `dp_id` does not mean there is no DP in Crew.
- For organizations, use `grid.search_companies`, then `grid.get_company` for approved contact channels, direct hierarchy, and a Grid URL.
- For facilities or stages, use `grid.search_locations`, then `grid.get_master_location` with each candidate's exact `master_location_id`. Keep project-location IDs distinct from master-location IDs. Inspect canonical identity, revision, description, operating-status evidence, parent/facility context, approved company roles and public booking channels before choosing a same-name candidate. A Forum under LACMA with an inherited Los Angeles address is not PNE Forum in Vancouver; a NorthShore website at `northshorestudios.us` is distinct evidence from the Canadian operator at `nsstudios.ca`. Do not infer identity from the name or shared operator alone.
- The master detail read separates direct contact/address ownership from inherited facility context. Follow `hierarchy.children.next_offset` with the same master ID and `children_limit` until `has_more=false`. Other sections have fixed caps with `truncated`/`has_more`; read the owning parent directly or narrow discovery rather than claim completeness. Missing/deleted/inaccessible IDs are indistinguishable. Treat inaccessible references, incomplete ancestry, failed reads and capped channels as unknown, never blank or evidence of absence. Public booking contacts are directory-only; a missing result in that scope says nothing about private contacts. Use `grid.get_location_photo_sets` for media and `grid.get_project_location` with separately authorized project and project-location IDs for private notes/quotes/contacts. No mutation preview or Chrome is required just to inspect existing catalog facts.
- For a stored address, use `grid.search_addresses` before external lookup. Preserve entity/owner scope and heed `has_more`; narrow the search or use the supported limit instead of claiming a truncated list is exhaustive.

Show the distinguishing facts behind candidate matches. Use the selected ID for matched results; ask the user to select among suggestions or conflicts before a downstream action. An unmatched result means no accessible reusable record was found, not that the entity does not exist.

Return only supplied or tool-returned facts and links. Missing/private fields are unknown, not permission to infer them. A directory match does not establish ownership, availability, a booking, or address verification. Do not create, merge, link, or message records unless the user separately requests a supported workflow.

When the user requests a write, use the operation-specific preview:

- `grid.preview_create_contact`: create a standalone person with supplied name,
  channels, structured addresses, initial notes and explicitly selected canonical professional `position_ids` (primary first); `contact.action` is `create`.
- `grid.preview_link_project_contact`: link an existing person to an existing
  project with crew/talent/other role and optional position.
- `grid.preview_link_company_contact`: affiliate an existing person with an
  existing directory company, using its company ID rather than a project-vendor
  membership ID.
- `grid.preview_link_contact_representative`: link an existing representative to
  an existing represented person with a canonical rep:* role.
- `grid.preview_remove_contact_representative`: remove an exact person-level
  representation relationship. Explain that the change affects all projects.

Link and removal tools require `contact.action: reuse` and the selected contact
ID. Each business apply supports only its named operation. For a new person and
one requested project link, use `grid.preview_contact_project_approval` to review
both together. Discover canonical positions with `grid.get_pipeline_options`
(catalog=positions, authorized owner). Profile positions and the project's position
are separate: one profile selection defaults the visible editable project position;
multiple selections require an explicit project position. Resolve duplicate choices
first; create_distinct requires the user's explicit distinct-person decision.

Show the entire bundle and obtain one explicit approval covering both operations.
Call `grid.apply_create_contact` with operations.create_contact.preview_id, then
`grid.apply_link_project_contact` with operations.link_project_contact.preview_id.
Each still requires confirm_preview=true and its own stable request_id. The future
contact is bound to the first receipt; never substitute another identity. If creation
succeeds and linking fails, report contact_created_project_link_pending and the
remaining preview ID. Retry only the unchanged authorized remainder; stale or
expired remainder requires a fresh project-link preview and approval. Never delete
the created person as compensation. A request for a standalone person uses only
the ordinary creation pair. Existing-contact reuse uses only the ordinary link pair.

Show normalized details, duplicate candidates, destinations, positions,
relationship changes and warnings. Resolve plausible duplicates explicitly.
After confirmation, call the matching `grid.apply_*` tool with preview_id,
request_id and confirm_preview=true. Preserve request_id on retries. Changed
intent or stale state requires a fresh preview and confirmation. Do not modify
reused person details through these tools; use the contact-update workflow.
Report persisted IDs and verify project links with grid.get_project_contact or
representation with grid.get_contact_representatives. A retry receipt describes
the original apply rather than later edits.

Read owner-authorized canonical contact addresses with `grid.get_contact_notes` for both standalone and project-linked people. It returns saved row IDs, label, structured fields, precision and provider expiry. Project identity visibility alone does not grant private address access. Home City is an active address labeled `Home City`, not an agency/billing fallback or a separate city field. For authorized edits, use exact IDs in `grid.preview_contact_update` → explicit confirmation → `grid.apply_contact_update` → current read-back. Search/Google lookup results are discovery evidence, not saved data or permission to reassign a row.
