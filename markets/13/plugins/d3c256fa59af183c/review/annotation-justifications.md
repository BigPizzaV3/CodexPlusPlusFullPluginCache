# PlugMind tool annotation review

Reviewed 2026-11-02 against [OpenAI plugin guidelines](https://developers.openai.com/plugins/plugin-guidelines#correct-annotation) and [tool annotation reference](https://developers.openai.com/plugins/reference#annotations). Generated from the real SDK tools/list response, including dynamic registrations, with provider callbacks disabled. This is a local catalog audit, not proof of production deployment or reviewer approval.

The rejection email requested justifications, so this document provides them even though the current guidelines say they are no longer required. No nonstandard justification fields are added to MCP annotations.

Hints cover the entire tool, including confirmed=true, optional URL inputs and already-active objects. A preview option or explicit confirmation does not make a write tool read-only. Background token refresh, rate-limit bookkeeping and access checks are operational maintenance; the separate account-discovery tools explicitly advertise their persisted catalog replacements. Read-only idempotency concerns business effects, not identical responses as metrics change. Write tools conservatively make no blanket retry guarantee.

## Resubmission notes

Corrected openWorldHint on live campaign/ad/ad-set edits and public URL validation paths. Corrected Google targeting to account for immediate effects on running campaigns. Corrected account discovery to disclose saved-catalog overwrites. All 76 tools expose four explicit boolean hints.

The earlier flagged create_google_search_campaign remains readOnly=false, destructive=false, openWorld=false: its actual implementation atomically adds a separate private budget and a PAUSED campaign. It neither replaces a budget nor activates spend. The flagged update_google_responsive_search_ad and update_meta_ad are readOnly=false, destructive=true, openWorld=true because they can replace already-serving content.

For the rejected submission, upload the corrected versioned ZIP to the existing plugin. Deploy the server revision separately, reconnect if MCP status is unavailable, and scan when the dashboard allows it. Verify the discovered definitions and provide these justifications with the review materials before resubmitting. A package upload does not deploy hosted tools. Do not claim the revision is deployed or approved until checked.

## archive_meta_ad

Overwrites the owned object status to ARCHIVED, removing it from normal use and stopping eligible delivery. Limited to an authorized private account object.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **true** — Can overwrite existing state, remove objects, interrupt delivery, or affect live delivery/spend as described above; reversibility is not used to classify it as safe.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## archive_meta_ad_set

Overwrites the owned object status to ARCHIVED, removing it from normal use and stopping eligible delivery. Limited to an authorized private account object.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **true** — Can overwrite existing state, remove objects, interrupt delivery, or affect live delivery/spend as described above; reversibility is not used to classify it as safe.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## archive_meta_campaign

Overwrites the owned object status to ARCHIVED, removing it from normal use and stopping eligible delivery. Limited to an authorized private account object.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **true** — Can overwrite existing state, remove objects, interrupt delivery, or affect live delivery/spend as described above; reversibility is not used to classify it as safe.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## create_google_ad_group

Adds a new PAUSED ad group under an owned campaign; does not edit existing groups or activate delivery.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **false** — Additive asset/record creation or its execution bookkeeping; no overwrite of existing advertising content, removal, activation or spend.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## create_google_campaign_targeting

Adds location/language criteria, including exclusions, to an existing campaign. Criteria are not paused and can immediately restrict or expand live public delivery and spend.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **true** — Can overwrite existing state, remove objects, interrupt delivery, or affect live delivery/spend as described above; reversibility is not used to classify it as safe.
- openWorldHint: **true** — Can affect public ad delivery or submit caller-selected public URLs for provider processing, including validation.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## create_google_keywords

Adds PAUSED keyword criteria. Optional caller-selected public landing URLs are submitted to Google for validation. Does not enable the criteria or overwrite existing keywords.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **false** — Additive asset/record creation or its execution bookkeeping; no overwrite of existing advertising content, removal, activation or spend.
- openWorldHint: **true** — Can affect public ad delivery or submit caller-selected public URLs for provider processing, including validation.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## create_google_responsive_search_ad

Adds a new PAUSED ad. Google receives caller-selected public landing URLs for validation. Does not replace an existing ad or enable delivery.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **false** — Additive asset/record creation or its execution bookkeeping; no overwrite of existing advertising content, removal, activation or spend.
- openWorldHint: **true** — Can affect public ad delivery or submit caller-selected public URLs for provider processing, including validation.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## create_google_search_campaign

Atomically adds a new private daily budget and a new PAUSED Search campaign. Does not overwrite an existing budget, activate delivery, or incur ad spend. A separate enable tool is required.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **false** — Additive asset/record creation or its execution bookkeeping; no overwrite of existing advertising content, removal, activation or spend.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## create_meta_ad

Adds a new PAUSED ad using owned ad-set and creative IDs; does not replace an existing ad or activate delivery.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **false** — Additive asset/record creation or its execution bookkeeping; no overwrite of existing advertising content, removal, activation or spend.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## create_meta_ad_set

Adds a new PAUSED ad set. App IDs and store URLs must match the authorized account app catalog. Does not activate delivery or overwrite existing ad sets.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **false** — Additive asset/record creation or its execution bookkeeping; no overwrite of existing advertising content, removal, activation or spend.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## create_meta_campaign

Adds a new PAUSED campaign to the authorized account; does not modify existing campaigns or activate delivery.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **false** — Additive asset/record creation or its execution bookkeeping; no overwrite of existing advertising content, removal, activation or spend.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## create_meta_image_creative

Adds an immutable creative without assigning it to a live ad. Meta can fetch the caller-selected public image URL and inspect the destination URL. No existing creative is overwritten.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **false** — Additive asset/record creation or its execution bookkeeping; no overwrite of existing advertising content, removal, activation or spend.
- openWorldHint: **true** — Can affect public ad delivery or submit caller-selected public URLs for provider processing, including validation.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## delete_meta_ad

Deletes the owned Meta advertising object via its DELETED status. Potentially irreversible removal, limited to an authorized private account object.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **true** — Can overwrite existing state, remove objects, interrupt delivery, or affect live delivery/spend as described above; reversibility is not used to classify it as safe.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## delete_meta_ad_set

Deletes the owned Meta advertising object via its DELETED status. Potentially irreversible removal, limited to an authorized private account object.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **true** — Can overwrite existing state, remove objects, interrupt delivery, or affect live delivery/spend as described above; reversibility is not used to classify it as safe.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## delete_meta_campaign

Deletes the owned Meta advertising object via its DELETED status. Potentially irreversible removal, limited to an authorized private account object.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **true** — Can overwrite existing state, remove objects, interrupt delivery, or affect live delivery/spend as described above; reversibility is not used to classify it as safe.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## enable_google_ad

Overwrites the owned object status to ENABLED/ACTIVE. Can publish ads to public audiences and incur spend when the hierarchy permits delivery; prior impressions and spend cannot be undone.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **true** — Can overwrite existing state, remove objects, interrupt delivery, or affect live delivery/spend as described above; reversibility is not used to classify it as safe.
- openWorldHint: **true** — Can affect public ad delivery or submit caller-selected public URLs for provider processing, including validation.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## enable_google_ad_group

Overwrites the owned object status to ENABLED/ACTIVE. Can publish ads to public audiences and incur spend when the hierarchy permits delivery; prior impressions and spend cannot be undone.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **true** — Can overwrite existing state, remove objects, interrupt delivery, or affect live delivery/spend as described above; reversibility is not used to classify it as safe.
- openWorldHint: **true** — Can affect public ad delivery or submit caller-selected public URLs for provider processing, including validation.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## enable_google_campaign

Overwrites the owned object status to ENABLED/ACTIVE. Can publish ads to public audiences and incur spend when the hierarchy permits delivery; prior impressions and spend cannot be undone.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **true** — Can overwrite existing state, remove objects, interrupt delivery, or affect live delivery/spend as described above; reversibility is not used to classify it as safe.
- openWorldHint: **true** — Can affect public ad delivery or submit caller-selected public URLs for provider processing, including validation.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## execute_meta_ads_batch

Starts durable work, updates execution progress and adds creatives and PAUSED ads for the approved saved plan. Meta processes public destination URLs. It never enables delivery or replaces existing ads. A retry may dispatch work if no run ID was saved; no unconditional idempotency guarantee is advertised.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **false** — Additive asset/record creation or its execution bookkeeping; no overwrite of existing advertising content, removal, activation or spend.
- openWorldHint: **true** — Can affect public ad delivery or submit caller-selected public URLs for provider processing, including validation.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## get_google_ad_group_details

Returns one ad group's settings and performance plus its ads, keywords, and search terms after validating account ownership. Reads authorized account/workspace data or a bounded provider catalog; does not mutate advertising objects, persist a user artifact, enqueue work, or browse arbitrary destinations.

- readOnlyHint: **true** — Retrieval, computation or non-persisting validation only; no business-state mutation.
- destructiveHint: **false** — No destructive business-state effects.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **true** — Repeating the read/validation has no additional business-state effect.

## get_google_ads_overview

Returns the selected Google Ads account's last-30-day totals: spend, impressions, clicks, CTR, conversions, conversion value, and ROAS. Reads authorized account/workspace data or a bounded provider catalog; does not mutate advertising objects, persist a user artifact, enqueue work, or browse arbitrary destinations.

- readOnlyHint: **true** — Retrieval, computation or non-persisting validation only; no business-state mutation.
- destructiveHint: **false** — No destructive business-state effects.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **true** — Repeating the read/validation has no additional business-state effect.

## get_google_campaign_details

Returns one campaign's configuration, budget, diagnostics and performance plus its ad groups, ads, keywords, and search terms. Use the exact campaign ID returned by the campaign list tool. Reads authorized account/workspace data or a bounded provider catalog; does not mutate advertising objects, persist a user artifact, enqueue work, or browse arbitrary destinations.

- readOnlyHint: **true** — Retrieval, computation or non-persisting validation only; no business-state mutation.
- destructiveHint: **false** — No destructive business-state effects.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **true** — Repeating the read/validation has no additional business-state effect.

## get_google_performance_breakdown

Returns aggregate performance split by day, device, and ad network for an account, campaign, or ad group. Campaign and ad-group levels require the exact object ID. Reads authorized account/workspace data or a bounded provider catalog; does not mutate advertising objects, persist a user artifact, enqueue work, or browse arbitrary destinations.

- readOnlyHint: **true** — Retrieval, computation or non-persisting validation only; no business-state mutation.
- destructiveHint: **false** — No destructive business-state effects.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **true** — Repeating the read/validation has no additional business-state effect.

## get_meta_ad_details

Shows the inline Meta/Facebook ad preview card with the actual creative, headline, copy, CTA, destination, status, and reporting-period performance. Use for show my ad, preview this creative, and how is this ad performing. Discover the numeric ad ID through campaign or ad-set details if the user supplied a name; users do not need to know IDs or tool names. Returns tracking and conversion specifications and nested creative fields after verifying account ownership. Displays actual Meta media only inside the inline card. Never use web/image search, generated illustrations, landing-page images, Markdown image embeds, or image carousels to supplement this result. If unavailable, report preview unavailable. Use only returned media; never generate or substitute a website image as the creative. This is not a placement-rendered preview; video and dynamic variations may require the original links. Reads authorized account/workspace data or a bounded provider catalog; does not mutate advertising objects, persist a user artifact, enqueue work, or browse arbitrary destinations.

- readOnlyHint: **true** — Retrieval, computation or non-persisting validation only; no business-state mutation.
- destructiveHint: **false** — No destructive business-state effects.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **true** — Repeating the read/validation has no additional business-state effect.

## get_meta_ad_set_details

Returns one ad set's full readable configuration and saved audience targeting, its aggregate performance, and its ads with nested creatives and performance. Configured targeting is not the same as actual delivery. Reads authorized account/workspace data or a bounded provider catalog; does not mutate advertising objects, persist a user artifact, enqueue work, or browse arbitrary destinations.

- readOnlyHint: **true** — Retrieval, computation or non-persisting validation only; no business-state mutation.
- destructiveHint: **false** — No destructive business-state effects.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **true** — Repeating the read/validation has no additional business-state effect.

## get_meta_ads_batch

Read saved per-item stages, creative IDs and ad IDs. Queued/running/waiting plans are executed by PlugMind in the background. Waiting includes available_at for the next attempt. Completed IDs are retained. Never recreate completed or uncertain items. Reads authorized account/workspace data or a bounded provider catalog; does not mutate advertising objects, persist a user artifact, enqueue work, or browse arbitrary destinations.

- readOnlyHint: **true** — Retrieval, computation or non-persisting validation only; no business-state mutation.
- destructiveHint: **false** — No destructive business-state effects.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **true** — Repeating the read/validation has no additional business-state effect.

## get_meta_ads_overview

Returns account-level last-30-day Meta totals, including spend, impressions, reach, clicks, CTR, CPC, results, conversion value, and ROAS. Reads authorized account/workspace data or a bounded provider catalog; does not mutate advertising objects, persist a user artifact, enqueue work, or browse arbitrary destinations.

- readOnlyHint: **true** — Retrieval, computation or non-persisting validation only; no business-state mutation.
- destructiveHint: **false** — No destructive business-state effects.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **true** — Repeating the read/validation has no additional business-state effect.

## get_meta_campaign_details

Returns one campaign's full readable configuration, performance, ad sets with saved targeting and optimization settings, and ads with nested creative configuration. Use this for a complete campaign audit, then call the delivery-breakdown tool for actual audience delivery. Reads authorized account/workspace data or a bounded provider catalog; does not mutate advertising objects, persist a user artifact, enqueue work, or browse arbitrary destinations.

- readOnlyHint: **true** — Retrieval, computation or non-persisting validation only; no business-state mutation.
- destructiveHint: **false** — No destructive business-state effects.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **true** — Repeating the read/validation has no additional business-state effect.

## get_meta_campaign_performance

Returns last-30-day performance for one numeric campaign ID after verifying that it belongs to the selected Meta ad account. Reads authorized account/workspace data or a bounded provider catalog; does not mutate advertising objects, persist a user artifact, enqueue work, or browse arbitrary destinations.

- readOnlyHint: **true** — Retrieval, computation or non-persisting validation only; no business-state mutation.
- destructiveHint: **false** — No destructive business-state effects.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **true** — Repeating the read/validation has no additional business-state effect.

## get_meta_delivery_breakdown

Returns aggregate actual delivery and performance by age/gender, country, region, placement, and device for one campaign, ad set, or ad. Use this to answer who actually received delivery; do not infer actual delivery from saved targeting alone. Reads authorized account/workspace data or a bounded provider catalog; does not mutate advertising objects, persist a user artifact, enqueue work, or browse arbitrary destinations.

- readOnlyHint: **true** — Retrieval, computation or non-persisting validation only; no business-state mutation.
- destructiveHint: **false** — No destructive business-state effects.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **true** — Repeating the read/validation has no additional business-state effect.

## get_meta_lead_form_leads

Retrieves leads from one authorized Page form. Personal field answers are omitted by default and are returned only when the user explicitly requests them with includeFieldData=true. Reads authorized account/workspace data or a bounded provider catalog; does not mutate advertising objects, persist a user artifact, enqueue work, or browse arbitrary destinations.

- readOnlyHint: **true** — Retrieval, computation or non-persisting validation only; no business-state mutation.
- destructiveHint: **false** — No destructive business-state effects.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **true** — Repeating the read/validation has no additional business-state effect.

## get_meta_page_insights

Reads aggregate Page impressions, post engagement, and follower totals for an authorized Page. Unsupported metrics are reported as warnings instead of fabricated values. Reads authorized account/workspace data or a bounded provider catalog; does not mutate advertising objects, persist a user artifact, enqueue work, or browse arbitrary destinations.

- readOnlyHint: **true** — Retrieval, computation or non-persisting validation only; no business-state mutation.
- destructiveHint: **false** — No destructive business-state effects.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **true** — Repeating the read/validation has no additional business-state effect.

## get_meta_permission_readiness

Checks the live Meta OAuth grant against every permission PlugMind uses. Returns required, granted, missing, ready, storedScopes, and storedGrantMatchesLive exactly. Always use this tool when the user asks about Meta permissions, scopes, OAuth readiness, or App Review readiness. Reads authorized account/workspace data or a bounded provider catalog; does not mutate advertising objects, persist a user artifact, enqueue work, or browse arbitrary destinations.

- readOnlyHint: **true** — Retrieval, computation or non-persisting validation only; no business-state mutation.
- destructiveHint: **false** — No destructive business-state effects.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **true** — Repeating the read/validation has no additional business-state effect.

## get_meta_reconnect_link

Only computes a PlugMind reconnect link. It does not initiate OAuth, revoke access or change the connection; the user must follow the link.

- readOnlyHint: **true** — Retrieval, computation or non-persisting validation only; no business-state mutation.
- destructiveHint: **false** — No destructive business-state effects.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **true** — Repeating the read/validation has no additional business-state effect.

## list_google_ad_groups

Lists ad groups with campaign ownership, serving diagnostics, bidding settings, and performance. Optionally scopes results to one campaign. Reads authorized account/workspace data or a bounded provider catalog; does not mutate advertising objects, persist a user artifact, enqueue work, or browse arbitrary destinations.

- readOnlyHint: **true** — Retrieval, computation or non-persisting validation only; no business-state mutation.
- destructiveHint: **false** — No destructive business-state effects.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **true** — Repeating the read/validation has no additional business-state effect.

## list_google_ads

Lists ads with campaign and ad-group ownership, serving and policy diagnostics, destination URLs, responsive-search-ad copy, ad strength, and performance. Reads authorized account/workspace data or a bounded provider catalog; does not mutate advertising objects, persist a user artifact, enqueue work, or browse arbitrary destinations.

- readOnlyHint: **true** — Retrieval, computation or non-persisting validation only; no business-state mutation.
- destructiveHint: **false** — No destructive business-state effects.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **true** — Repeating the read/validation has no additional business-state effect.

## list_google_ads_accounts

Fetches authorized accounts and overwrites the workspace accessible-customer catalog via update_google_ads_runtime. This persisted catalog controls account resolution; it is not merely a transient read. Does not select another account or edit ads.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **true** — Can overwrite existing state, remove objects, interrupt delivery, or affect live delivery/spend as described above; reversibility is not used to classify it as safe.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## list_google_ads_campaigns

Lists up to 100 campaigns from the selected account with status, channel and bidding configuration, budget, diagnostics, schedule, and performance for the requested period. Reads authorized account/workspace data or a bounded provider catalog; does not mutate advertising objects, persist a user artifact, enqueue work, or browse arbitrary destinations.

- readOnlyHint: **true** — Retrieval, computation or non-persisting validation only; no business-state mutation.
- destructiveHint: **false** — No destructive business-state effects.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **true** — Repeating the read/validation has no additional business-state effect.

## list_google_campaign_targeting

Returns the exact positive and excluded locations and languages configured on one owned campaign, including canonical location details and criterion IDs. Reads authorized account/workspace data or a bounded provider catalog; does not mutate advertising objects, persist a user artifact, enqueue work, or browse arbitrary destinations.

- readOnlyHint: **true** — Retrieval, computation or non-persisting validation only; no business-state mutation.
- destructiveHint: **false** — No destructive business-state effects.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **true** — Repeating the read/validation has no additional business-state effect.

## list_google_keywords

Lists positive and negative Search keywords with match type, approval and serving state, bids, quality components, destination URLs, and performance. Reads authorized account/workspace data or a bounded provider catalog; does not mutate advertising objects, persist a user artifact, enqueue work, or browse arbitrary destinations.

- readOnlyHint: **true** — Retrieval, computation or non-persisting validation only; no business-state mutation.
- destructiveHint: **false** — No destructive business-state effects.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **true** — Repeating the read/validation has no additional business-state effect.

## list_google_languages

Lists targetable Google Ads language constants and their exact IDs and codes for campaign targeting. Reads authorized account/workspace data or a bounded provider catalog; does not mutate advertising objects, persist a user artifact, enqueue work, or browse arbitrary destinations.

- readOnlyHint: **true** — Retrieval, computation or non-persisting validation only; no business-state mutation.
- destructiveHint: **false** — No destructive business-state effects.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **true** — Repeating the read/validation has no additional business-state effect.

## list_google_search_terms

Lists actual user search terms with their matched keyword, campaign and ad-group ownership, status, and performance. Use this for negative-keyword and query-quality analysis. Reads authorized account/workspace data or a bounded provider catalog; does not mutate advertising objects, persist a user artifact, enqueue work, or browse arbitrary destinations.

- readOnlyHint: **true** — Retrieval, computation or non-persisting validation only; no business-state mutation.
- destructiveHint: **false** — No destructive business-state effects.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **true** — Repeating the read/validation has no additional business-state effect.

## list_meta_ad_sets

Lists ad sets from the selected account or one campaign, including budgets, bid strategy, optimization, promoted object, schedules, saved targeting, learning state, and performance. Reads authorized account/workspace data or a bounded provider catalog; does not mutate advertising objects, persist a user artifact, enqueue work, or browse arbitrary destinations.

- readOnlyHint: **true** — Retrieval, computation or non-persisting validation only; no business-state mutation.
- destructiveHint: **false** — No destructive business-state effects.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **true** — Repeating the read/validation has no additional business-state effect.

## list_meta_ads_accounts

Fetches authorized accounts and overwrites the workspace accessible-account catalog via update_meta_ads_runtime. This persisted catalog controls account resolution; it is not merely a transient read. Does not select another account or edit ads.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **true** — Can overwrite existing state, remove objects, interrupt delivery, or affect live delivery/spend as described above; reversibility is not used to classify it as safe.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## list_meta_ads_campaigns

Find Meta/Facebook campaigns by their returned names when the user asks to see an ad, preview a creative, or review campaign performance without IDs. Lists up to 100 campaigns from the selected Meta account with deep campaign configuration and performance. Use the returned numeric ID with get_meta_campaign_details to load its ad sets, targeting, ads, and creatives. Reads authorized account/workspace data or a bounded provider catalog; does not mutate advertising objects, persist a user artifact, enqueue work, or browse arbitrary destinations.

- readOnlyHint: **true** — Retrieval, computation or non-persisting validation only; no business-state mutation.
- destructiveHint: **false** — No destructive business-state effects.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **true** — Repeating the read/validation has no additional business-state effect.

## list_meta_apps

Lists apps this ad account can advertise, including exact Meta application IDs, names, store URLs, supported platforms, and install-tracking metadata. Use before preparing App Promotion or in-app purchase ad sets. Match the requested app by name and ID and choose its iOS or Android store URL; never guess an app ID or replace purchase optimization with installs. Eligibility for the requested event is checked by create_meta_ad_set validation, not inferred from this list. Reads authorized account/workspace data or a bounded provider catalog; does not mutate advertising objects, persist a user artifact, enqueue work, or browse arbitrary destinations.

- readOnlyHint: **true** — Retrieval, computation or non-persisting validation only; no business-state mutation.
- destructiveHint: **false** — No destructive business-state effects.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **true** — Repeating the read/validation has no additional business-state effect.

## list_meta_assets

Returns Meta OAuth permission readiness (required, granted, missing, ready, and storedGrantMatchesLive) together with managed Facebook Pages, promotable Pages, available ad identities, Pixels, and ad images. Use this as the compatibility fallback when the dedicated permission-readiness tool is not exposed by the MCP client. Reads authorized account/workspace data or a bounded provider catalog; does not mutate advertising objects, persist a user artifact, enqueue work, or browse arbitrary destinations.

- readOnlyHint: **true** — Retrieval, computation or non-persisting validation only; no business-state mutation.
- destructiveHint: **false** — No destructive business-state effects.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **true** — Repeating the read/validation has no additional business-state effect.

## list_meta_audiences

Lists available Custom and Lookalike Audience definitions, subtypes, aggregate size ranges, retention, lookalike specifications, and delivery/operation status where Meta makes them available. It never returns individual audience members. Reads authorized account/workspace data or a bounded provider catalog; does not mutate advertising objects, persist a user artifact, enqueue work, or browse arbitrary destinations.

- readOnlyHint: **true** — Retrieval, computation or non-persisting validation only; no business-state mutation.
- destructiveHint: **false** — No destructive business-state effects.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **true** — Repeating the read/validation has no additional business-state effect.

## list_meta_business_assets

Lists the Business portfolios available to the signed-in user and their owned/client ad accounts and Pages. Use this to verify agency client ownership and workspace boundaries. Reads authorized account/workspace data or a bounded provider catalog; does not mutate advertising objects, persist a user artifact, enqueue work, or browse arbitrary destinations.

- readOnlyHint: **true** — Retrieval, computation or non-persisting validation only; no business-state mutation.
- destructiveHint: **false** — No destructive business-state effects.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **true** — Repeating the read/validation has no additional business-state effect.

## list_meta_lead_forms

Lists lead-generation forms belonging to an authorized Facebook Page. This does not return personal lead answers. Reads authorized account/workspace data or a bounded provider catalog; does not mutate advertising objects, persist a user artifact, enqueue work, or browse arbitrary destinations.

- readOnlyHint: **true** — Retrieval, computation or non-persisting validation only; no business-state mutation.
- destructiveHint: **false** — No destructive business-state effects.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **true** — Repeating the read/validation has no additional business-state effect.

## list_meta_pages

Lists the Facebook Pages managed by the signed-in person, reads Page identity metadata, and shows which Pages can be promoted by the selected ad account. Use selectablePages for ad identity candidates, including verified business-owned managed Pages omitted by promote_pages. Candidates require Meta validation of the exact ad payload; an empty promotablePages list alone does not mean no Page is usable. Reads authorized account/workspace data or a bounded provider catalog; does not mutate advertising objects, persist a user artifact, enqueue work, or browse arbitrary destinations.

- readOnlyHint: **true** — Retrieval, computation or non-persisting validation only; no business-state mutation.
- destructiveHint: **false** — No destructive business-state effects.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **true** — Repeating the read/validation has no additional business-state effect.

## list_workspaces

Lists every active PlugMind client workspace available to the authenticated user, including role and connected ad platforms. Call this before using ad tools when no exact workspace ID is known. Reads authorized account/workspace data or a bounded provider catalog; does not mutate advertising objects, persist a user artifact, enqueue work, or browse arbitrary destinations.

- readOnlyHint: **true** — Retrieval, computation or non-persisting validation only; no business-state mutation.
- destructiveHint: **false** — No destructive business-state effects.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **true** — Repeating the read/validation has no additional business-state effect.

## open_meta_image_upload

Only returns the upload-picker UI and resolved workspace/account references. Opening it performs no upload; upload buttons call separately annotated write tools.

- readOnlyHint: **true** — Retrieval, computation or non-persisting validation only; no business-state mutation.
- destructiveHint: **false** — No destructive business-state effects.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **true** — Repeating the read/validation has no additional business-state effect.

## pause_google_ad

Overwrites the owned object status to PAUSED, stopping eligible delivery. Operates on an existing private account object and does not publish content or fetch arbitrary URLs.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **true** — Can overwrite existing state, remove objects, interrupt delivery, or affect live delivery/spend as described above; reversibility is not used to classify it as safe.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## pause_google_ad_group

Overwrites the owned object status to PAUSED, stopping eligible delivery. Operates on an existing private account object and does not publish content or fetch arbitrary URLs.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **true** — Can overwrite existing state, remove objects, interrupt delivery, or affect live delivery/spend as described above; reversibility is not used to classify it as safe.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## pause_google_campaign

Overwrites the owned object status to PAUSED, stopping eligible delivery. Operates on an existing private account object and does not publish content or fetch arbitrary URLs.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **true** — Can overwrite existing state, remove objects, interrupt delivery, or affect live delivery/spend as described above; reversibility is not used to classify it as safe.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## pause_meta_ad

Overwrites the owned object status to PAUSED, stopping eligible delivery. Operates on an existing private account object and does not publish content or fetch arbitrary URLs.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **true** — Can overwrite existing state, remove objects, interrupt delivery, or affect live delivery/spend as described above; reversibility is not used to classify it as safe.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## pause_meta_ad_set

Overwrites the owned object status to PAUSED, stopping eligible delivery. Operates on an existing private account object and does not publish content or fetch arbitrary URLs.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **true** — Can overwrite existing state, remove objects, interrupt delivery, or affect live delivery/spend as described above; reversibility is not used to classify it as safe.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## pause_meta_campaign

Overwrites the owned object status to PAUSED, stopping eligible delivery. Operates on an existing private account object and does not publish content or fetch arbitrary URLs.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **true** — Can overwrite existing state, remove objects, interrupt delivery, or affect live delivery/spend as described above; reversibility is not used to classify it as safe.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## prepare_meta_ads_batch

Validates creative payloads with Meta and inserts a new saved plan in PlugMind. Public destination URLs are passed to Meta for validation. Does not create Meta ads or overwrite another plan.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **false** — Additive asset/record creation or its execution bookkeeping; no overwrite of existing advertising content, removal, activation or spend.
- openWorldHint: **true** — Can affect public ad delivery or submit caller-selected public URLs for provider processing, including validation.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## resolve_workspace

Resolves a client name or workspace slug to a stable workspace ID. If more than one workspace matches, returns the candidates instead of guessing. Reads authorized account/workspace data or a bounded provider catalog; does not mutate advertising objects, persist a user artifact, enqueue work, or browse arbitrary destinations.

- readOnlyHint: **true** — Retrieval, computation or non-persisting validation only; no business-state mutation.
- destructiveHint: **false** — No destructive business-state effects.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **true** — Repeating the read/validation has no additional business-state effect.

## resume_meta_ad

Overwrites the owned object status to ENABLED/ACTIVE. Can publish ads to public audiences and incur spend when the hierarchy permits delivery; prior impressions and spend cannot be undone.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **true** — Can overwrite existing state, remove objects, interrupt delivery, or affect live delivery/spend as described above; reversibility is not used to classify it as safe.
- openWorldHint: **true** — Can affect public ad delivery or submit caller-selected public URLs for provider processing, including validation.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## resume_meta_ad_set

Overwrites the owned object status to ENABLED/ACTIVE. Can publish ads to public audiences and incur spend when the hierarchy permits delivery; prior impressions and spend cannot be undone.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **true** — Can overwrite existing state, remove objects, interrupt delivery, or affect live delivery/spend as described above; reversibility is not used to classify it as safe.
- openWorldHint: **true** — Can affect public ad delivery or submit caller-selected public URLs for provider processing, including validation.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## resume_meta_campaign

Overwrites the owned object status to ENABLED/ACTIVE. Can publish ads to public audiences and incur spend when the hierarchy permits delivery; prior impressions and spend cannot be undone.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **true** — Can overwrite existing state, remove objects, interrupt delivery, or affect live delivery/spend as described above; reversibility is not used to classify it as safe.
- openWorldHint: **true** — Can affect public ad delivery or submit caller-selected public URLs for provider processing, including validation.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## search_google_geo_targets

Resolves human location names to exact Google geo-target constant IDs, canonical names, country codes, types, status, and estimated reach. Use these IDs before proposing campaign location targeting. Reads authorized account/workspace data or a bounded provider catalog; does not mutate advertising objects, persist a user artifact, enqueue work, or browse arbitrary destinations.

- readOnlyHint: **true** — Retrieval, computation or non-persisting validation only; no business-state mutation.
- destructiveHint: **false** — No destructive business-state effects.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **true** — Repeating the read/validation has no additional business-state effect.

## update_google_ad_group

Overwrites an existing ad group name or CPC bid without pausing it. Live bidding and public delivery can be affected.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **true** — Can overwrite existing state, remove objects, interrupt delivery, or affect live delivery/spend as described above; reversibility is not used to classify it as safe.
- openWorldHint: **true** — Can affect public ad delivery or submit caller-selected public URLs for provider processing, including validation.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## update_google_campaign

Overwrites name, private budget or dates on an existing campaign without pausing it. Active campaigns can immediately change public delivery or spend.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **true** — Can overwrite existing state, remove objects, interrupt delivery, or affect live delivery/spend as described above; reversibility is not used to classify it as safe.
- openWorldHint: **true** — Can affect public ad delivery or submit caller-selected public URLs for provider processing, including validation.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## update_google_keyword

Overwrites an existing keyword bid or status; ENABLED is accepted. Can start delivery or affect live bidding and spend.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **true** — Can overwrite existing state, remove objects, interrupt delivery, or affect live delivery/spend as described above; reversibility is not used to classify it as safe.
- openWorldHint: **true** — Can affect public ad delivery or submit caller-selected public URLs for provider processing, including validation.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## update_google_responsive_search_ad

Overwrites the complete landing URL, headline, description and path configuration of an existing ad without pausing it. This can replace already-public creative, and Google can inspect the supplied destination URL.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **true** — Can overwrite existing state, remove objects, interrupt delivery, or affect live delivery/spend as described above; reversibility is not used to classify it as safe.
- openWorldHint: **true** — Can affect public ad delivery or submit caller-selected public URLs for provider processing, including validation.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## update_meta_ad

Overwrites an ad name or its creative assignment without pausing it. Swapping the creative of an active ad can change what the public sees.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **true** — Can overwrite existing state, remove objects, interrupt delivery, or affect live delivery/spend as described above; reversibility is not used to classify it as safe.
- openWorldHint: **true** — Can affect public ad delivery or submit caller-selected public URLs for provider processing, including validation.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## update_meta_ad_set

Overwrites existing ad-set budget, bids, schedule or targeting without pausing it. Can immediately affect public delivery, audiences and spend.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **true** — Can overwrite existing state, remove objects, interrupt delivery, or affect live delivery/spend as described above; reversibility is not used to classify it as safe.
- openWorldHint: **true** — Can affect public ad delivery or submit caller-selected public URLs for provider processing, including validation.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## update_meta_campaign

Overwrites an existing campaign name, budgets or bid strategy without pausing it. Active delivery and spend can be affected.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **true** — Can overwrite existing state, remove objects, interrupt delivery, or affect live delivery/spend as described above; reversibility is not used to classify it as safe.
- openWorldHint: **true** — Can affect public ad delivery or submit caller-selected public URLs for provider processing, including validation.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## upload_meta_image

Adds supplied PNG/JPEG bytes to the authorized private Meta image library. Does not replace an image, publish a post or attach it to an active ad; accepts no arbitrary download URL.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **false** — Additive asset/record creation or its execution bookkeeping; no overwrite of existing advertising content, removal, activation or spend.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## upload_meta_image_file

Downloads one explicitly supplied ChatGPT file through restricted handoff hosts and adds it to the authorized private Meta image library. Does not accept arbitrary web hosts, replace existing media or publish ads.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **false** — Additive asset/record creation or its execution bookkeeping; no overwrite of existing advertising content, removal, activation or spend.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## upload_meta_image_files

Downloads explicitly supplied ChatGPT files through restricted handoff hosts and adds them to the authorized private Meta image library. Partial successes are retained; no arbitrary web fetch, overwrite or ad publication.

- readOnlyHint: **false** — At least one supported path persists or changes state, uploads data, or dispatches work.
- destructiveHint: **false** — Additive asset/record creation or its execution bookkeeping; no overwrite of existing advertising content, removal, activation or spend.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **false** — No unconditional retry guarantee: calls can add records, dispatch jobs, or reapply changes against evolving provider state. Follow tool-specific retry guidance.

## validate_meta_ad

Checks owned ad-set/creative IDs and submits a PAUSED proposal with Meta validate_only. Does not persist a plan, create an ad, assign a creative or activate delivery.

- readOnlyHint: **true** — Retrieval, computation or non-persisting validation only; no business-state mutation.
- destructiveHint: **false** — No destructive business-state effects.
- openWorldHint: **false** — Confined to authorized private workspaces/accounts, supplied files or a bounded provider catalog; external hosting alone is not open-world.
- idempotentHint: **true** — Repeating the read/validation has no additional business-state effect.

