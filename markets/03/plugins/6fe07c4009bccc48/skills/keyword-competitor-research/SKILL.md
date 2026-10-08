---
name: keyword-competitor-research
description: Research keywords and competitors for a brand. Use for finding keyword ideas, tracking keywords, checking ranking history, comparing against competitors, or reviewing backlinks and referring domains. Do not use for AI assistant visibility, which belongs to ai-visibility-report, and do not use for writing articles.
---

# Keyword and competitor research

Find the terms worth winning, track them, and see who else is winning them.

Every tool here is scoped to one brand and takes `brand_id`.

## Step 1: resolve the brand

Call `list_brands`. If more than one, ask which. Keep `brand_id` for every later call.

## Step 2: see what is already tracked

Call `list_keywords`. Start here so you extend the existing set rather than duplicating it.

If metrics look stale, `refresh_keyword_metrics` updates volume and difficulty.

## Step 3: find new terms

Call `discover_keywords`:

- `seed` generates ideas around a term.
- `location` scopes them to a market.
- `limit` caps the count, maximum 50.

Present ideas with their volume and difficulty, and say which are realistic for the brand rather than listing the highest volume terms. A term the brand cannot rank for is not an opportunity.

Add the approved terms with `add_keywords`. Use `update_keyword` to adjust one, `delete_keyword` to drop one.

## Step 4: track position over time

`get_keyword_ranking_history` shows movement for a tracked keyword.

Only describe a trend when the history holds more than one point. A single measurement is a position, not a direction.

## Step 5: compare against competitors

- `list_competitors` for the current set, `add_competitor` and `remove_competitor` to change it.
- `sync_competitor_metrics` to refresh their numbers before comparing.

Compare like for like: the same keywords, the same location, the same dates. Say which are covered.

## Step 6: authority

`get_backlinks` and `get_referring_domains` show which sites link to the brand, and `sync_backlinks` refreshes them. Referring domains matter more than raw link count, because many links from one domain count for far less than links from many.

## Reporting rules

- Give volume and difficulty together. Volume alone reads as opportunity when it is often just competition.
- Say when data was last synced. Stale numbers presented as current lead to bad decisions.
- Never invent a number for a keyword that returned none. Say it returned none.
- Do not name the third party data sources behind backlink or keyword metrics. Refer to the data, not the vendor.

## Boundaries

- `delete_keyword` and `remove_competitor` change what is measured over time and break comparability with earlier reports. Confirm first.
- If the user wants an article for a keyword, hand off to the content-production skill.
- If the user asks how they appear in AI assistant answers, that is the ai-visibility-report skill, and it is a different measurement entirely.
