---
name: meta-ads-creative-audit
description: "Audits Meta Ads creatives and audiences through the Pilot MCP server: best and worst ads, creative fatigue, ad sets with too little volume to judge, audience setup and account issues, then returns what to refresh, keep or stop for a person to apply. Use when the user asks about Meta or Facebook and Instagram ads, creatives, ad fatigue or audiences. Triggers: Meta ads audit, creative fatigue, best performing ads, Facebook ads review. Déclencheurs : audit Meta Ads, fatigue des créas, meilleures publicités, audiences Meta, revue Facebook Ads."
compatibility: "Requires the Pilot MCP server (https://app.pilot.braike.com/mcp) connected in the client and authorized on a workspace with a Meta ad account attached."
metadata:
  pilot-mcp-server: "https://app.pilot.braike.com/mcp"
  pilot-mcp-tools: "meta_list_accounts meta_check_account_issues meta_get_account_insights meta_get_adset_insights meta_get_top_performing_ads meta_get_worst_performing_ads meta_list_adsets meta_list_campaigns meta_list_ad_creatives meta_list_custom_audiences"
  pilot-mcp-read-only: "true"
---

# Meta Ads creative audit

Tell the user which Meta ads and creatives work, which are tiring, which ad sets cannot be judged yet, and what to do next. Answer in the user's language.

## Requirements

- **Required MCP server:** Pilot MCP (`https://app.pilot.braike.com/mcp`), authorized on the workspace that holds the Meta ad account.
- **Optional MCP servers:** a file storage server to save the audit, a team messaging server to send it to the creative team. None is needed.
- **Read-only:** never pause, edit or duplicate an ad, ad set or campaign. Recommendations are for a person to apply.

## Tools

- `meta_list_accounts`: the Meta ad accounts attached to the workspace.
- `meta_check_account_issues`: limits, rejections and restrictions.
- `meta_get_account_insights`: results of the account, by ad set with `level: "adset"`, week by week with `time_increment: 7`.
- `meta_get_adset_insights`: results of one ad set, for a closer look.
- `meta_get_top_performing_ads`: the best ads on a metric.
- `meta_get_worst_performing_ads`: the weakest ads on a metric.
- `meta_list_adsets`: ad sets of the account, with their status and budget.
- `meta_list_campaigns`: campaigns of the account.
- `meta_list_ad_creatives`: the creatives of the account.
- `meta_list_custom_audiences`: custom audiences and their state.

## Steps

1. Call `meta_list_accounts` and pick the account (ask if several). Use its ID as `account_id`.
2. Call `meta_check_account_issues`: a restricted account explains more than any creative.
3. Call `meta_get_account_insights` with `level: "adset"` and `date_preset: "last_7d"`. Set aside every ad set with too little volume to judge: fewer than about 50 results of its optimization goal over these 7 days, the volume Meta usually needs to leave the learning phase. Do not judge them.
4. Call `meta_get_top_performing_ads` and `meta_get_worst_performing_ads` with `date_preset: "last_30d"`, on the metric that matches the goal (cost per result, ROAS, click-through rate).
5. For the ad sets that remain, call `meta_get_account_insights` with `level: "adset"`, `date_preset: "last_30d"` and `time_increment: 7`, and compare frequency, click-through rate and cost week by week: rising frequency with falling click-through rate is fatigue. Call `meta_get_adset_insights` for an ad set that needs a closer look.
6. Call `meta_list_adsets` and `meta_list_campaigns` to name each ad set and its campaign, with its status and budget.
7. Call `meta_list_ad_creatives` to link the best and worst ads to their formats and messages.
8. Call `meta_list_custom_audiences` to spot audiences too small or not ready.

## Output

1. **Summary**: account state, the creatives that carry the results, the main risk.
2. **Keep**: best ads, with their figures.
3. **Refresh**: tired ads, with the fatigue evidence.
4. **Stop or rework**: weak ads, with their figures.
5. **Not readable yet**: ad sets with too little volume, and when to look again.
6. **Audiences**: issues found.

## Rules

- Never judge an ad set set aside at step 3 for too little volume.
- Name the period, the metric and the currency.
- A ratio with an empty denominator is not available, not zero.

## Examples

- "Which Meta ads are tiring and should be refreshed?"
- "Fais l'audit des créas Meta du dernier mois."
- "Quelles publicités Facebook marchent le mieux sur le coût par achat ?"
