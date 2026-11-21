---
name: landit-prospects
description: Find existing Landit Pages, create personalized Pages for user-selected prospects and templates, or inspect Enrichment and PageRun outcomes.
---

# Landit prospects and Pages

Read [shared safety and identity](../../references/safety-and-identity.md) and [capabilities](../../references/capabilities.md). The AI may browse verified template previews, but MUST NEVER open prospect Page links, including indirect fetches, screenshots, HEAD requests, or link checks. Return Page links for the user to open themselves.

## Existing Pages

Use search_pages with only user-specified filters. Filters combine; follow next_page until null for complete results. integration and prospect_id must be paired. There is no arbitrary full-text, person-name, or LinkedIn-URL search parameter. Inspect returned records to establish identity; do not guess a slug or silently infer filters. Use existing results when the user asks to check for duplicates before creating; do not claim deduplication is automatic.

## Authorized creation

1. The user must explicitly select the template. Use list_templates to offer choices and get_template for the chosen slug and variable manifests; never choose a template on the user's behalf.
2. Confirm exact prospect LinkedIn person-profile URLs and required template values from supplied evidence. Clarify materially missing values. Put values directly on each prospect alongside linkedin_url. Use crm_provider: hubspot and crm_contact_id only as a paired, authorized association to the requesting user's connected HubSpot account. Page creation can write the Page URL back to that contact; explain that effect when included.
3. Use the requested batch name or generate a descriptive enrichment_name. Send the complete list in one enrich_prospects call within live request limits. The old 20-prospect cap is obsolete. Every submission creates a new Enrichment; corrections/expansion require a newly authorized batch, not a fabricated update parameter.
4. Preserve enrichment_uuid and every PageRun public_id. Use get_enrichment(enrichment_uuid) to inspect every associated run or get_page_run(run_id) for one. Do not assume a batch succeeded uniformly or associate runs by guessed row order.
5. Check run state before claiming completion. Report partial success/failure, component states, and useful failure detail. Check crm_writeback_state separately before saying a URL reached HubSpot. A completed Page can be reported while the batch remains enriching during its 30-minute intake/settlement window.
6. If the host cannot keep waiting, return durable IDs and actual states for continuation. Do not restart work because polling ended. Reconcile a lost response before repeating creation. For insufficient_credits, explain that generation cannot proceed with the current account credits; do not invent prices/balances or initiate a purchase.

Use returned final Page URLs only as user-facing links. Do not use them to verify rendering, availability, screenshots, or analytics. Report generated status separately from unverified live appearance. LinkedIn invitations/messages and general CRM edits are outside this plugin.
