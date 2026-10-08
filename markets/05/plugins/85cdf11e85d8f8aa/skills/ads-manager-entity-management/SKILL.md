---
name: ads-manager-entity-management
description: "Create or update Ads Manager campaigns and ad groups and update existing ads through a minimal-diff, confirmed, read-back-verified workflow. Use for explicit campaign-only or ad-group-only creation without new ads, or changes to an existing campaign, ad group, or ad. Do not interpret a vague “create a campaign” request as campaign-only work. Do not use for new-ad creation, account onboarding, account administration, reporting, or delivery diagnosis."
allowed-tools:
  - list_ad_accounts
  - list_custom_audiences
  - get_custom_audience
  - get_ads_manager_route_link
  - list_product_feeds
  - search_geo_locations
  - list_conversion_event_settings
  - list_campaigns
  - get_campaign
  - show_campaign_delivery
  - create_campaign
  - update_campaign
  - list_ad_groups
  - get_ad_group
  - list_conversion_event_settings
  - create_ad_group
  - update_ad_group
  - list_ads
  - get_ad
  - preview_existing_ad
  - preview_existing_ad_collection
  - update_ad
  - upload_image
  - upload_image_file
---

# Ads Manager Entity Management

Coordinate direct campaign and ad-group creation and edits to existing entities. Keep factual list, get, preview, reporting, and readiness requests outside this mutation workflow. A request whose outcome is a new ad belongs to `$ads-manager-ad-creation`, even when it also needs parent campaign or ad-group creation.

## Main Workflow

Treat entity management as one confirmed state-transition workflow:

1. Classify the request as direct campaign/ad-group creation, an existing-entity update, a status-only change, or an explicitly scoped multi-entity change. If the user is asking which entity should change, why delivery is blocked, or what would improve performance, route that diagnostic or recommendation work first rather than selecting a mutation target here.
2. Resolve exactly one account, then the requested audience or hierarchy: campaign, ad group, then ad. Use list tools for discovery, name resolution, ambiguity, and pagination; use the matching get tool after an exact target is known. Ask the user to choose by visible names only when live results leave real ambiguity, and keep every later call scoped to the selected account.
3. Before planning past the active branch, read and follow every linked reference whose condition matches that branch. When multiple conditions match, load all of them before acting; do not load unrelated references merely because they exist.
4. Read the current target and every parent needed to interpret the requested change immediately before proposing it. Do not infer campaign mode, bidding type, product-feed ownership, creative type, currency, current status, or current nested settings from names, sibling entities, earlier conversation, or performance ranking.
5. Build the smallest safe plan that satisfies the request, show the exact user-visible proposal, and obtain explicit confirmation immediately before the first consequential write.
6. Execute only the approved ordered writes. Preserve successful returned resource and file ids privately, stop dependent work after a failed or ambiguous parent or upload, and never turn a partial failure into permission for a broader write.
7. Read changed entities back and report only proven outcomes. Reconcile ambiguous results with fresh reads before considering any retry, and follow the shared safety contract for corrected payloads or partial outcomes.

- Before planning confirmation, writing, retrying, or reconciling any direct create or update, read and follow [write-safety.md](references/_shared/write-safety.md).
- For saved-audience targeting and bid adjustments, or web handoffs for audience creation or changes, read and follow [audiences.md](references/_shared/audiences.md).
- Before proposing, confirming, or creating a campaign or ad group, or drafting or reviewing changes to context hints, ad copy, or landing-page alignment, read and follow [ads-structure-and-context-playbook.md](references/_shared/ads-structure-and-context-playbook.md). A status-only or name-only update does not trigger this playbook.
- Before proposing or confirming a campaign objective, budget period, timing, or ad-group bidding strategy, read and follow [auction-readiness-playbook.md](references/_shared/auction-readiness-playbook.md).
- Before proposing, confirming, or creating a conversions campaign, or assessing measurement readiness for a requested change, read and follow [measurement-readiness-playbook.md](references/_shared/measurement-readiness-playbook.md).
- Before proposing, confirming, or creating a campaign with `bidding_type=conversions` or requested geographic targeting, exclusions, or platform targeting, read and follow [campaign-create-preflight.md](references/_shared/campaign-create-preflight.md), including its conditions for reusing or refreshing results through confirmation and create.
- When deciding whether product-feed mode fits a requested create, planning product sets or filter changes, or assessing feed-ad launch quality, read and follow the Planning Guidance section of [product-feed-contract.md](references/_shared/product-feed-contract.md#planning-guidance). A status-only or name-only update does not trigger this section.
- Before discovering feeds, planning, creating, or updating any product-feed campaign or ad group, read and follow the Operational Rules section of [product-feed-contract.md](references/_shared/product-feed-contract.md#operational-rules).
- Before selecting, generating, validating, uploading, applying, retrying, or reconciling an existing-ad image replacement, read and follow both the [shared image asset contract](references/_shared/image-asset-contract.md) for `ad-creative` and [write-safety.md](references/_shared/write-safety.md).

### 1. Resolve scope and the exact target set

For a single target, resolve its account and parent hierarchy before proposing any change. For an explicitly requested multi-entity change, enumerate every exact target from live reads, follow required pagination, and show the complete target set before confirmation. Never silently include similarly named entities, later pages, inferred siblings, or a performance-ranked target the user did not explicitly approve.

- If a request only asks to list, inspect, open, or preview entities, answer connector-native and stop; a read does not authorize a later write.
- If no accessible account exists, explain that the requested entity change needs an account and offer Onboarding; do not invoke `$ads-manager-onboarding` or create anything unless the user explicitly requests setup.
- Route standalone campaign planning, product-feed suitability questions, and reviews of supplied context hints to `$ads-manager-help`. Keep account health reviews, rankings, and blocked-delivery diagnosis with Review or Delivery Recovery. Return here only for an explicit create or update; keep drafting and review of that requested change in this workflow.
- If the user asks to create a new ad, including while also asking for a campaign or ad group, keep the end-to-end flow in `$ads-manager-ad-creation`. This skill may create only a directly requested campaign or ad group and must not create an ad.

### 2. Plan a direct campaign or ad-group creation

For a direct campaign create, resolve the selected account and its currency. Follow the applicable conversion, geographic-targeting, or explicit-platform checks in [campaign-create-preflight.md](references/_shared/campaign-create-preflight.md). Propose the smallest schema-valid payload: required fields plus only optional fields the user selected or the campaign mode requires. For a standard campaign, omit `mode` and `product_feed_id`. Omit targeting and conversion settings unless approved, and never send unrequested optional fields as `null`, empty arrays, or empty objects.

Only look up locations or discuss geographic options when the user requests geographic targeting or exclusions, or when the saved-audience geography check in [audiences.md](references/_shared/audiences.md) requires it. Obtain approval for any geographic change. If no targeting is approved, use Ads Manager's default targeting and omit `targeting`.

Show the proposed name, status, budget type and amount, resolved currency when available, objective or bidding type, and any timing, targeting, or product-feed selection. Prefer paused unless the user explicitly requests active. Explain the objective's CPC-versus-CPM consequence using the live action guidance. If the user asked only for a campaign, create only that campaign and explain that an ad group and then an ad are required later.

For a direct ad-group create, resolve and read the exact parent campaign first. Propose the smallest schema-valid ad-group payload: required fields plus only optional fields the user selected or the verified parent campaign requires. Omit `description`, `context_hints`, and `product_set` unless they are part of the approved create. Never send absent optional fields as `null`, empty arrays, or empty objects. Show the name, status, bid strategy, billing event, and product set only when applicable. Show a maximum bid with resolved currency only for manual bidding. Match the billing event to the verified parent campaign's bidding type, and never infer a product feed from sibling ad groups. Use the fresh parent data for the tool-owned daily-budget preflight and strategy eligibility checks. Use `list_conversion_event_settings` when needed; fetch or ask instead of guessing or silently changing the strategy. For an approved automatic strategy, omit the manual bid fields and supply the required stable idempotency key. Never retry with manual bidding without approval. If the request also includes creating a new ad, route the whole outcome to `$ads-manager-ad-creation` instead of creating parents here and handing off mid-write.

When the user has no bidding preference, recommend automatic bidding for an eligible daily-budget clicks or conversions parent and offer manual bidding as an alternative. Label the recommendation `Maximize Clicks` or `Maximize Conversions` to match the parent objective. Confirm the strategy before creation. Do not change the existing campaign's objective, budget period, or conversion goal to make automatic bidding eligible; explain any conflict and ask the user to choose.

- For a product-feed campaign create, use only a confirmed account-linked feed selected under the Operational Rules section of [product-feed-contract.md](references/_shared/product-feed-contract.md#operational-rules).
- For a product-feed ad-group create, reuse only the verified parent campaign feed and keep any product set consistent with it.
- For a standard campaign or ad group, do not send product-feed-only fields.

### 3. Plan an existing-entity update as a minimal safe diff

After a confirmed delivery-related fix and read-back, use `show_campaign_delivery`
with `request.view="detail"` for that account and campaign when available. Do not
claim a successful write proves delivery resumed. During proposal/confirmation,
focus on the proposed change instead of repeating the widget.

For every update, read the current entity immediately before planning, compare the user's requested end state with that live state, and send only fields needed for the requested change. If the requested state already exists, report a no-op instead of writing. A status-only request should send only the requested status; never infer active status or combine it with unrelated cleanup.

Treat every supplied nested object or list as potentially replacement-shaped unless the live action explicitly proves field-level patching. For a platform-only campaign update, send only `targeting: {platforms: ...}` so geo and audience siblings remain unchanged; omit `platforms` to preserve an existing restriction, and use `platforms: null` only to remove it after approval. When any other requested change requires sending budget, targeting, conversion settings, bidding configuration, product set, or creative, preserve every unrequested sibling value from the live entity in the proposed end state, or omit that entire structure. Never use “minimal diff” as permission to erase unmentioned filters, targeting, bidding fields, creative fields, or destination data.

- Campaign updates may change only the requested campaign fields. For spend-capable changes, show the exact amount, resolved currency when available, budget type, status, and any timing or targeting consequence before confirmation.
- For campaign-wide URL tracking or UTM changes, use `update_campaign` with `body.landing_page_configuration`, following the live tool's field guidance.
- For geographic targeting updates, read and follow the Geo targeting section of [campaign-create-preflight.md](references/_shared/campaign-create-preflight.md) for intent, query construction, refinement, and result reuse. Resolve only places needed for the requested change and reuse suitable matches across approved targets in the same account and relevant targeting context. If saved audiences remain, also check the new geography under [audiences.md](references/_shared/audiences.md). Preserve existing targeting that the user did not ask to change; it does not need fresh name resolution. The create-default rule does not apply to updates.
- Ad-group updates must preserve the existing product set unless the user explicitly asked to change it. When changing bidding or product-set fields, read the parent campaign first so the proposal respects its bidding type and verified feed.
- For ad-group creates and bid updates using manual bidding (`strategy="fixed_bid"`), confirm the bid's basis (CPM, CPC, or oCPC bid per conversion) and resolved account currency. For oCPC, explain that billing remains per click and the bid does not guarantee a cost per conversion (CPA). For an approved CPM amount, prefer `max_cpm` when exposed by the live action and omit `max_bid_micros`; follow the live action's unit guidance when only the raw bid field is available. When preserving an unchanged raw bid from a read, keep its units and value unchanged.
- Existing-ad updates must preserve every unrequested ad and creative field. A request to change title, body, destination, status, or image is not permission to create a replacement ad or silently rewrite the rest of the creative.

### 4. Handle an existing-ad creative image replacement

For an existing `chat_card` image replacement, accept only a user-supplied or explicitly approved candidate: a direct public image URL, provided attachment, accessible existing image, or generated standalone creative after the user explicitly chooses generation. Never pass a webpage URL or raw local path to an upload action, never generate an ad-placement mockup, and never treat a selected or generated image as uploaded.

1. Read and follow the linked image and write-safety references before image choice, generation, validation, upload, or retry.
2. Show the exact candidate image and the complete creative end state, including every preserved unrequested creative field, before confirmation.
3. When the approved candidate needs upload, upload it once for that approved update. Continue only when the upload succeeds and returns a non-empty opaque `file_id`; preserve that token privately and pass it unchanged in the exact confirmed creative update. When the live read already exposes a usable file id for the exact approved existing image, reuse that token unchanged instead of uploading the same image again.
4. Do not upload or attach custom imagery for a product-ad template whose feed supplies imagery.
5. After updates are verified, use `preview_existing_ad` for one requested live result or `preview_existing_ad_collection` once for 2 to 50 requested live results in one account; if the collection tool is unavailable, call `preview_existing_ad` for each requested result when available. Do not create another ad or use a new-ad preview as proof of the update.

### 5. Confirm, write, verify, and report

The confirmation must identify the selected account, exact target or complete multi-target set, current values that will change, proposed values, monetary authority when present, status, and ordered writes. Use plain language rather than raw tool names, request fields, internal ids, or connector JSON.

- For dependent creates such as an explicitly requested campaign followed by an ad group, create the parent first, require a proven returned id, reuse it for the child, and stop if the parent fails or is ambiguous.
- For updates, read the target back and compare the requested changed fields with the confirmed end state. Do not claim success from an empty, missing, or ambiguous response.
- For an ambiguous update or unkeyed upload, reconcile current state before any retry and never blindly repeat the write. For an ambiguous create, use only the retry behavior permitted by [write-safety.md](references/_shared/write-safety.md).
- For a multi-target request, report each target independently as succeeded, failed, or not attempted. Preserve successful results and do not repeat them while repairing another target.
- Use returned entity deep links when available, and report only connector-proven state.

## Scope And Tool-Owned Rules

Use only fields, enum values, validation, permissions, response fields, numeric constraints, and backend errors exposed by the live actions. Do not restate or override tool schemas, budget or bid formulas, ID validation, URL validation, product-filter operators, or backend behavior in this skill. Never broaden a requested diff, infer spend authority, infer active status, choose a mutation target from performance, create a new ad, or turn a direct entity edit into reporting, diagnosis, or recommendation work.
