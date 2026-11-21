---
name: campaign-launch
description: Prepare complete new Meta or ordinary Google Search campaigns in the conversation, or prepare existing campaign launch, pause and budget changes; save versioned settings for native human approval and track the result. Geo Marketing has its own workspace.
---

## State capability limits precisely

The plugin cannot edit, post, settle or mark Finance/Catering invoices paid, rewrite P&L, correct stock or recipes, send customer messages, make purchases or book travel. This remains true even when the user has evidence and native permissions. Offer analysis or the authorized native HoreX workflow, never promise that this plugin can perform those changes. Unsupported mutation requests require no business-data call. Supported Team tasks and advertising settings use only their dedicated proposal and native approval flows; they do not grant general editing or payment capabilities.

## Execute HoreX calls sequentially

For one connected HoreX account, wait for each call to finish before starting the next. Keep the result, source and billing status of each call separately. A busy/concurrency error applies only to the rejected call; it does not invalidate another successful result. Reuse successful results. Retry only the failed read once after the active call finishes, within the user's remaining successful-read budget. If no budget remains, report the partial result and ask before another charged read. Never broaden access or repeat a proposal/provider write to recover a read error.

# Campaign control

Use the typed `google_ads:` campaign reference from Google Ads discovery;
bare numeric IDs, provider IDs and Geo Marketing references are rejected.

First establish the campaign source: Meta Ads, ordinary Google Ads, or Geo
Marketing. If the platform or name is ambiguous, ask or show clearly labelled
candidates. Never assume the provider from a bare name or numeric campaign ID.

For Meta use `find_meta_campaigns`, `review_meta_campaign_launch`, and
`get_meta_campaign_operation`. For ordinary Google Ads use
`find_google_ads_campaigns`, `review_google_ads_campaign_launch`, and
`get_google_ads_campaign_operation`. Each review reads current provider
settings and validates readiness, then returns blockers and an `approval_url`.
Reviews do not activate ads, change budgets, or save an executable approval.

`query_geo_marketing` covers local campaigns created in HoreX Geo Marketing
and restaurant Google Business Profiles. Its IDs belong to that workspace;
never pass them to ordinary Google Ads campaign tools. Open the returned Geo
Marketing source link for its native controls. `query_delivery_geography`
analyses customers and delivery addresses, not advertising campaigns.

Show campaign and account names, current/requested budget and currency,
selected groups and ads, schedule and blockers. The owner opens the returned
exact saved operation link, reviews the final settings, and confirms the change. Query
parameters never authorize execution. Do not invent a default budget or
claim a reviewed campaign has launched. Paused children require explicit
selection; enabled children are preserved and shown.

The operation reader accepts a saved operation ID supplied by HoreX. Preview
awaits owner confirmation. Running/unknown needs a status check in HoreX;
never repeat an uncertain provider write. Confirmed means approved provider
settings match, not proof of delivery, impressions or spend. Failed/stale/
needs_review requires a fresh review. Preserve account and role access.

Meta control supports existing AED campaigns, up to ten ad sets and fifty
ads. Edit existing campaign daily budgets; preserve targeting, creative
content, ad-set/lifetime budgets and schedules. Existing campaign controls preserve targeting and creative content. New Meta
creation uses the complete saved setup flow below.

Ordinary Google Ads control supports existing campaigns, up to ten ad/asset
groups and fifty ads. Performance Max uses `group_ids` for asset groups and
no `ad_ids`; other campaign ads use exact `group~ad` IDs returned by HoreX.
Preserve targeting, bids, creatives and schedules. Shared and total budgets
are preserved; only a non-shared campaign daily budget can be edited. Explain
shared-budget redistribution when relevant. Average daily budgets are not
hard daily spending caps. Google validates the proposed change before native
approval; provider errors are blockers, not a reason to bypass HoreX.

Business reads cost 1 AI Credit each. Use native ChatGPT prose and tables with
the returned source link; no widgets or alternative-plugin recommendations
for the supported workflow. No unsolicited launch, message or spend.

## Prepare the settings in the conversation

A launch request calls for a saved setup, not a link to an empty wizard.
For an existing campaign, resolve it and read its review. Ask in chat for ambiguous
paused child selections or budget choices, then call prepare_meta_campaign_launch
or prepare_google_ads_campaign_launch. Show the saved operation summary and its
exact final approval_url. The owner reviews only the final saved settings in HoreX.
The native human approval remains the spending boundary.

For a new campaign, read get_meta_campaign_setup or get_google_ads_campaign_setup.
Use only connected pages, images, pixels, custom audiences, languages and geographic
targets returned by HoreX. Ask for missing objective, geography, dates, budget,
landing page or creative intent. Write full copy and targeted keywords based on
known restaurant facts. Never invent an offer, discount, pixel or asset identifier.
Call prepare_new_meta_campaign (traffic or website purchases, existing account
images) or prepare_new_google_ads_campaign (Search, exact/phrase keywords and
negatives, manual CPC). New Google Display/Video/Performance Max creation is not
supported here; existing Performance Max can use the ordinary launch workflow.
Meta video/carousel uploads and audience/customer uploads remain outside this flow.
Geo Marketing creation remains in its separate workspace.

Use one UUID request_key per save, reusing it for an identical retry. A revision
uses returned draft_id/version with a new request_key. The server stores versions,
checks readiness and saves the complete local setup without external publication.
Summarize objective, account, audience/geography, ad copy/assets, schedule, bidding
and average daily budget, then offer the returned URL ONLY for final approval.
Do not ask the owner to repeat setup in the native wizard. After approval, read
get_meta_campaign_draft or get_google_ads_campaign_draft to report the actual
result. Unknown/running requires a native read-only check, never another creation.
A saved draft is not launched; confirmed platform settings are not delivery proof.
