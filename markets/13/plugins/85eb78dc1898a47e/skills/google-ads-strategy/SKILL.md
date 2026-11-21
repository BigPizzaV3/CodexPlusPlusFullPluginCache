---
name: google-ads-strategy
description: Review a Google Ads account's structure, bidding and ad copy with Toffu. Use when the user asks how to set up or improve Google Ads campaigns, which bidding strategy to use, or for responsive search ad headlines and descriptions.
---

Use the Toffu tools. Never apply a change the user has not confirmed.

1. Call `get_account_context`. If a platform has several accounts, ask which one. Pass the ids as `account_ids` to `query_campaign_performance`, and as `account_id` to the other tools.
2. Read data with `query_campaign_performance` (daily rows: `time_increment` "1"), `list_campaigns`, `list_ad_sets` and `list_ads`.
3. To change something, call `propose_update_campaign`, `propose_update_ad_set` or `propose_update_ad`, and show the preview. Call `apply_change` only after the user confirms that change.

Search terms, keywords, Quality Score and extensions are not readable here. Say so when the advice depends on them, and base the review on campaign data.

# Google Ads Strategy & Optimization

## Account Structure
- **Branded campaigns**: isolate brand terms. These have highest ROAS and lowest CPC.
- **Non-branded campaigns**: segment by product/service category or funnel stage.
- **Competitor campaigns**: bid on competitor terms selectively. Expect lower quality scores.
- Keep ad groups tightly themed — 5-15 keywords per ad group maximum.

## Keyword Match Types
- **Exact match**: highest intent, lowest volume. Use for proven converters.
- **Phrase match**: balances reach and relevance. Primary workhorse for most accounts.
- **Broad match**: only with Smart Bidding. Google's AI needs conversion data to make broad work.
- Layer match types deliberately — don't run the same keyword in all three types in the same campaign.

## Bidding Strategies
- **tCPA** (target Cost Per Acquisition): use when you have a clear CPA goal and 30+ conversions/month.
- **tROAS** (target Return On Ad Spend): use for e-commerce with variable order values.
- **Maximize conversions**: good for ramping new campaigns. Transition to tCPA once data accumulates.
- Never switch bidding strategies during high-traffic periods. Give algorithms 2-3 weeks to learn.

## Quality Score Optimization
- Three components: **expected CTR**, **ad relevance**, **landing page experience**.
- Improve CTR: test headlines aggressively, use keyword insertion where appropriate.
- Improve relevance: ensure ad copy mirrors the keyword theme.
- Improve landing page: fast load time, mobile-friendly, content matches ad promise.

## Negative Keyword Management
- Build negative keyword lists at account and campaign level.
- Review search terms report weekly. Add irrelevant queries as negatives immediately.
- Use shared negative lists across campaigns to prevent wasted spend consistently.

## Ad Extensions
- **Sitelinks**: 4-6 per campaign, link to high-value pages.
- **Callouts**: highlight USPs (free shipping, 24/7 support).
- **Structured snippets**: list product categories or service types.
- Extensions improve ad rank and CTR at no extra cost — always populate them.

## Audience Layering
- Layer in-market and custom intent audiences as **observation** mode first.
- Increase bids on high-performing audience segments.
- Use RLSA (remarketing lists for search ads) to bid more aggressively on past visitors.

## Responsive Search Ad Copy Constraints
- **Headlines: hard cap 30 characters each (including spaces and punctuation).** Count before output. Never propose, suggest, or display a headline over 30 chars, even in chat. Regenerate until every headline fits.
- **Descriptions: hard cap 90 characters each (including spaces and punctuation).** Count before output. Same rule: regenerate, do not truncate or "round up to fit later".
- Provide 3-15 headlines and 2-4 descriptions per RSA.
- Avoid em-dashes; use periods or commas. They consume characters and inflate counts.
- When presenting copy in tables/markdown, include a Chars column so the limit is auditable at a glance.
- If the user adds extra constraints (banned words, no price/budget mentions, theme focus), apply them on top of the length caps; never let added constraints push you over the caps.
