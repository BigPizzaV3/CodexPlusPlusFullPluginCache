---
name: meta-ads-manager
description: Reports on and manages a client's Meta (Facebook and Instagram) ads through the Agency Autopilot connector — spend, reach, clicks and conversions by campaign, pausing or enabling campaigns and ads, changing budgets, building whole campaigns (campaign, ad set and ads with images, a carousel or a video) created paused, adding ad sets and ads, and editing an ad's text or link. Use for "how are the Facebook ads doing", "pause the Meta campaign", "what's our Meta spend", "build a Meta campaign", "add an ad", "change the ad's link". Every change is previewed before it applies.
---

# Meta ads management

## Always
- `meta_list_accounts` first; use the `act_…` id it returns. Note whether the account can currently spend.
- `meta_list_pages` when a campaign needs a Page. If it says the connection predates Page access, the agency disconnects and reconnects Meta once on the dashboard (Meta re-approved Page access on 23 Oct 2026).
- Name the date range in every number.

## Reporting
`meta_insights` with `level: "campaign"` and either `date_preset` (`last_7d`, `last_30d`, `this_month`) or `since`/`until`. Report spend, reach, impressions, clicks, CTR, CPC and conversions per campaign. For "which ad is winning", rerun at `level: "ad"`.

## Changes — preview, confirm, apply
- `meta_set_campaign_status` (PAUSED or ACTIVE) — the preview shows the campaign's current state; activating resumes spend, say so.
- `meta_set_campaign_budget` — the preview shows the current and proposed daily budget; large increases are refused until acknowledged.
- `meta_set_ad_status`, `meta_set_ad_set_budget` — the same preview and confirm, one ad or ad set at a time.
- `meta_update_ad` — change an ad's text, headline, link, button or phone number. The ad keeps its history; Meta reviews the new version.
Show the preview, get an explicit yes, then call again with `confirm: true`.

## Building a campaign — the whole thing, here
- `meta_build_campaign` builds the campaign, one ad set (goal, daily budget, locations, ages) and 1-5 ads (text, headline, button, link, with one image, a 2-10 image carousel or a video) from the client's Facebook Page, in one step. Everything is created **paused**, and the tool cannot turn anything on.
- Before it: `meta_list_pages` for the Page; `meta_find_locations` for the area; for a website-leads goal, `meta_list_pixels` and use a pixel that fires on the client's thank-you page (it counts the Lead event). A calls goal needs a CALL_NOW button and a phone number.
- The preview downloads and checks every image and has Meta check the campaign. Show the person the budget, the audience and every ad word for word, and confirm only on their yes. If a step fails, the tool removes only what that same call created.
- Build the whole campaign in one go rather than leaving parts to finish in Ads Manager. Instant Forms (the form inside Facebook) are not available yet: send people to the client's site, ideally a page for that one service.
- To grow an existing campaign: `meta_create_ad_set` (paused) and `meta_create_ad` (paused), each previewed. `meta_create_campaign` makes an empty campaign only; prefer `meta_build_campaign`.
- After building: the campaign stays paused until the person asks to start it (`meta_set_campaign_status`, previewed).

## Rules
- Never activate a campaign, ad set or ad, or raise a budget, without an explicit instruction naming it.
- Report currency as the account's currency.
- If the account isn't linked to a client on the dashboard, the connector refuses; say how to link it.
