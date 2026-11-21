---
name: performance-drop-diagnosis
description: "Diagnoses a drop in advertising performance through the Pilot MCP server: checks data freshness first, locates the drop by platform and campaign, then looks for the cause in recent changes, auction pressure, search terms, delivery issues, rejected ads and site traffic. Use when the user reports that conversions, revenue, clicks or ROAS fell, or asks why performance dropped. Triggers: performance drop, why did conversions fall, sudden decline. Déclencheurs : baisse de performance, pourquoi les conversions baissent, chute des résultats, diagnostic d'une baisse."
compatibility: "Requires the Pilot MCP server (https://app.pilot.braike.com/mcp) connected in the client and authorized on a workspace with Google Ads, Meta Ads or Google Analytics 4 attached."
metadata:
  pilot-mcp-server: "https://app.pilot.braike.com/mcp"
  pilot-mcp-tools: "pilot_data_freshness pilot_cross_platform_overview google_list_accounts google_get_campaign_performance google_get_change_history google_get_auction_insights google_get_search_terms_report meta_list_accounts meta_compare_periods_performance meta_get_ad_account_activities meta_check_account_issues meta_get_ad_rejections google_analytics_run_report"
  pilot-mcp-read-only: "true"
---

# Performance drop diagnosis

Find where a drop happened and what most likely caused it, with evidence, before anyone changes a campaign. Answer in the user's language.

## Requirements

- **Required MCP server:** Pilot MCP (`https://app.pilot.braike.com/mcp`), authorized on the workspace concerned.
- **Optional MCP servers:** a team messaging server to share the diagnosis, a note-taking server to log it. None is needed.
- **Read-only:** never call a tool that creates, updates, pauses or deletes anything. The diagnosis ends with actions for a person to take.

## Tools

- `pilot_data_freshness`: rules out a data gap before diagnosing a drop.
- `pilot_cross_platform_overview`: locates the drop by platform.
- `google_list_accounts`: the Google Ads accounts attached to the workspace.
- `google_get_campaign_performance`: locates the drop by Google Ads campaign.
- `google_get_change_history`: what changed in the account, and when.
- `google_get_auction_insights`: competitors gaining impression share on search and shopping.
- `google_get_search_terms_report`: queries that changed.
- `meta_list_accounts`: the Meta ad accounts attached to the workspace.
- `meta_compare_periods_performance`: Meta results before and after.
- `meta_get_ad_account_activities`: what changed in the Meta account.
- `meta_check_account_issues`: limits, restrictions and delivery problems.
- `meta_get_ad_rejections`: ads stopped by review.
- `google_analytics_run_report`: whether site traffic or key events fell too.

## Steps

1. Call `pilot_data_freshness`. If a platform has a collection gap, the "drop" may be missing data: report it and stop there unless the live tools show the same drop.
2. Call `pilot_cross_platform_overview` for the recent period and the previous one of the same length (for example `days: 7` and `days: 14`). Name the platform where the drop sits.
3. Google Ads: `google_list_accounts`, then `google_get_campaign_performance` on both periods (`start_date` and `end_date`), to find the campaigns behind the drop. Then `google_get_change_history`, `google_get_auction_insights` and `google_get_search_terms_report` on those campaigns.
4. Meta Ads: `meta_list_accounts`, then `meta_compare_periods_performance`, `meta_get_ad_account_activities`, `meta_check_account_issues` and `meta_get_ad_rejections`.
5. If a Google Analytics 4 property is attached, call `google_analytics_run_report` on both periods with `dimensions: ["sessionDefaultChannelGroup"]` and `metrics: ["sessions", "keyEvents"]`. A drop on every channel points to the site or the tracking, not the ads.
6. Rank the candidate causes by how well the dates and the size of the change match.

## Output

1. **Where**: the platform, accounts and campaigns behind the drop, with figures for both periods.
2. **Most likely cause**: one cause, the evidence, and how sure you are.
3. **Other candidates**: causes that remain possible, and the data that would settle them.
4. **What to do**: actions for a person to take, and what to check first.

## Rules

- Rule out a data gap before anything else.
- Compare periods of equal length and say which days they cover.
- Correlation of dates is evidence, not proof: say how sure you are.
- A ratio with an empty denominator is not available, not zero.

## Examples

- "Our conversions dropped this week, why?"
- "Le ROAS de Meta a chuté depuis lundi : qu'est-ce qui a changé ?"
- "Diagnostique la baisse de clics sur Google Ads ce mois-ci."
