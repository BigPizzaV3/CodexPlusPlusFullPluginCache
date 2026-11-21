---
name: measurement
description: Conversion tracking with Opus Growth - auditing and fixing Google Ads conversion actions, Google Analytics 4 key events and the Ads link, Google Tag Manager tags and publishing, Meta pixel and Conversions API, TikTok pixel and events, LinkedIn Insight Tag conversions, Microsoft UET goals, ChatGPT Ads pixels, offline CRM conversions and click-fraud checks. Use when conversions look wrong, are missing, or tracking needs to be set up.
---

# Measurement and conversion tracking

Follow the `opus-growth` skill. Bad tracking makes every other decision wrong, so check it before
judging performance and before turning on conversion-based bidding.

## Audit, per platform

| Platform | Check | Typical finding |
|---|---|---|
| Google Ads | `google_ads_conversion_tracking_health`, `google_ads_list_conversion_actions`, `google_ads_get_conversion_settings`, `google_ads_list_conversion_goals` | Primary action silent for days; duplicate actions counting the same lead twice; a page-view action set as Primary |
| GA4 | `ga4_list_conversions`, `ga4_list_data_streams`, `ga4_list_ads_links`, `ga4_realtime` | Key event not marked; no link to Google Ads; stream not receiving |
| Tag Manager | `list_gtm_tags`, `list_gtm_triggers`, `gtm_workspace_status` | Tag built but never published |
| Meta | `list_meta_pixels` (last fired), `list_meta_custom_conversions` | Pixel not firing; purchase event without value |
| TikTok | `list_tiktok_pixels` | Pixel events missing |
| LinkedIn | `list_linkedin_conversions` | Conversion not attached to the campaigns |
| Microsoft | `list_microsoft_uet_tags`, `list_microsoft_conversion_goals` | Tag not installed, so no goals record |
| ChatGPT Ads | `chatgpt_ads_conversion_setup` | No standard event for a conversions campaign |

## Setting up a pixel or tag

1. Check first: `list_meta_pixels` and `list_tiktok_pixels` list the existing pixels. Meta
   refuses a second pixel on an ad account that has one, and LinkedIn allows one Insight Tag per
   ad account; `create_meta_pixel` and `create_linkedin_insight_tag` then return the existing
   pixel or tag instead of creating another, without using credits.
2. Create what is missing: `create_meta_pixel`, `create_linkedin_insight_tag`,
   `create_tiktok_pixel`.
3. Install the code on every page: a Tag Manager Custom HTML tag firing on all pages
   (`create_gtm_tag`, then `publish_gtm_container` on approval), or the site's own Meta,
   LinkedIn or TikTok integration.
4. Define what counts: `create_meta_custom_conversion` (URL or event on the pixel) and
   `create_linkedin_conversion` (page URL rule or event), then `attach_linkedin_conversion` for
   the LinkedIn campaigns that should report it.
5. Confirm it fires: `list_meta_pixels` shows the last fired time; a new tag can take a while to
   show its first event.

## Google Ads rules

- What bidding optimizes for is the Primary actions, shown by `include_in_conversions_metric`.
  Secondary actions are observed only; a Secondary action at zero is not an alarm.
- Count leads "one per click", purchases "every". Two Primary actions for the same lead (a form
  tag plus a GA4 import of the same submit) double-count.
- Changing which actions are Primary changes the Conversions column and restarts Smart Bidding
  learning; tell the user before doing it (`google_ads_update_conversion_action`,
  `google_ads_update_conversion_goal`).
- Tag install: `google_ads_get_conversion_tags` gives the conversion id and label (send_to) for
  the site or for a Tag Manager tag.
- Calls: with account call reporting on (`google_ads_set_call_reporting`), calls from ads are
  counted by Google's default action; do not build a duplicate.
- CRM sales and qualified leads: try `google_ads_upload_offline_conversions` (needs the click id
  stored with the lead). Google refuses this upload through the Google Ads API for integrations it
  has moved to its Data Manager API; when the tool answers that Google requires the Data Manager
  API, the user uploads the file in the Google Ads interface instead. Refunds and value
  corrections still work with `google_ads_upload_conversion_adjustments`, and Microsoft offline
  upload works (`upload_microsoft_offline_conversions`).
- Enhanced conversions for leads is a Google Ads interface setting; the API cannot switch it on.

## Tag Manager workflow

1. Read the workspace (`list_gtm_tags`, `list_gtm_triggers`, `list_gtm_variables`).
2. Build in a workspace (`create_gtm_tag`, `create_gtm_trigger`, `create_gtm_variable`;
   `enable_gtm_builtin_variables` for Click URL, Form ID and similar).
3. Review pending changes with `gtm_workspace_status`.
4. Publish only on explicit approval (`publish_gtm_container`); it goes live on the site at once.
   `rollback_gtm_version` restores the previous version if something breaks.
Tags respect consent: a consent-gated tag fires only after the visitor accepts cookies, so
numbers lower than sessions are expected.

## Server-side events

Meta Conversions API (`send_meta_conversion_event`) and TikTok Events API
(`send_tiktok_conversion_event`) send events from the server. Use the same event id as the pixel
event so the platform deduplicates; without it the conversion counts twice.

## Click fraud (Google Ads)

`click_fraud_setup` gives a tracking tag for the site; `click_fraud_scan` then analyzes captured
clicks (it detects, it does not block). Block confirmed sources with
`google_ads_block_ip_addresses` (Google allows a limited number of IP exclusions per campaign).
Google already filters most invalid clicks and refunds them as "invalid clicks"; treat a scan as
evidence, not proof.

## Expected gaps between tools

Platforms, GA4 and the CRM never match exactly: different attribution windows, models, time zones
and consent. Each ad platform credits itself. Explain the gap instead of calling one source wrong;
investigate only when the difference is large or suddenly changes.
