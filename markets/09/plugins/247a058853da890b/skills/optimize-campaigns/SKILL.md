---
name: optimize-campaigns
description: Pause, resume, archive, or re-budget live Meta campaigns, ad sets, and ads in AdStellar with a preview-then-confirm flow. Use when the user wants to turn ads on or off, cut or scale budgets, stop a losing creative, or act on performance results.
---

Use this skill when the user wants to change something that is live on Meta. Every change goes through a two-step confirmation: the first tool call returns a preview and a `confirmationToken`; nothing changes until you call again with that token after the user explicitly agrees.

## Resolve the target first

- Campaigns: call `lookup_campaign` with a name fragment to get the Meta campaign id. Never guess an id.
- Ad sets and ads: call `query_performance` with `breakdown` `ad_set` or `ad` so you have the entity id from synced data. Targets that are not in the team's synced data cannot be changed.
- If several results match, list them and ask which one.

## Tools

- `pause_campaign`, `resume_campaign`, `archive_campaign` take `campaignId` and an optional `campaignName` for the preview.
- `update_campaign_budget` takes `campaignId` and `dailyBudget` in the ad account's currency. On a CBO or Advantage+ campaign it sets the shared budget; on an ABO campaign it sets every ad set to that amount, so use `update_ad_set_budget` to change one ad set.
- `pause_ad_set`, `resume_ad_set`, `update_ad_set_budget` take `adSetId`; `pause_ad` and `resume_ad` take `adId`.

## Flow

1. Call the tool without `confirmationToken`. It returns a preview: the target, its ad account, whether the change is reversible, and the new budget when relevant.
2. Show the user exactly what will happen in one or two lines and ask for a yes. For budget changes state the new amount and currency; for archive say it cannot be undone from AdStellar.
3. On a yes, call the same tool with identical arguments plus `confirmationToken`. Report the tool's message. Tokens expire after 10 minutes and are bound to the exact target and amount, so a change of mind means starting again.
4. For several changes (for example pausing three ad sets), run the preview for each, get one approval covering the list, then execute each with its own token.

## Do not

- Do not call a mutation tool with `confirmationToken` before the user has approved that specific change.
- Do not archive when the user says pause; prefer `pause_campaign` and offer archive only when asked.
- Do not change budgets by more than the user asked for, and do not infer a budget from performance data without stating the number and getting approval.
- Do not create standing rules from this skill; use the automate-optimization skill for "whenever X, do Y" requests.
