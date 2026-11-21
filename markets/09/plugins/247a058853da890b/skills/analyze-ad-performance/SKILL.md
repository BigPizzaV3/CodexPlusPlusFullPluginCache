---
name: analyze-ad-performance
description: Pull and summarize synced Meta ads performance from AdStellar grouped by campaign, ad set, ad, or creative component over a date range. Use when the user asks how their ads, campaigns, or spend are performing, or wants ROAS, CPA, CTR, or budget breakdowns.
---

Use this skill when the user asks about the results of their Meta ads and their AdStellar account is connected.

## Steps

1. Call `list_ad_accounts` first. Note each account's currency and `last_synced_at`; if data is more than a day old, say so in the summary. If the team has several ad accounts and the user did not specify one, ask which one or report per account.
2. Call `query_performance` with:
   - `breakdown`: `campaign` (default), `ad_set`, or `ad` for entity levels, or one of the creative-component breakdowns listed in the tool's schema when the user asks about hooks, formats, or other creative elements.
   - A date range: `preset` (for example `last_7d` or `last_30d`; the tool schema lists the valid presets) or explicit `startDate` and `endDate` in YYYY-MM-DD.
   - `adAccount`, `campaignId`, or `adSetId` filters when the user names them, and `limit` when they want a top-N list.
3. Summarize what the numbers say: total spend, results, cost per result, ROAS, and the top and bottom performers by the metric the user cares about. Use the account's currency. Present rows in a compact table when there are more than three.
4. When comparing periods, run `query_performance` twice with the two ranges and compare like for like.

## Do not

- Do not spell the ad-set breakdown as adset or adgroup; the value is `ad_set`.
- Do not compute metrics that are not derivable from the returned rows, and do not mix currencies across accounts without saying so.
- Do not treat `purchases` or `results` as revenue; ROAS comes from the tool when Meta reports it.
- Do not pause, edit, or launch anything from this skill. When the user wants to act on the numbers, hand off to the optimize-campaigns skill, which previews and confirms every change.
