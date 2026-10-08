---
name: google-search-console-report
description: Report Google Search Console data for a brand. Use for clicks, impressions, CTR, average position, top search queries, top landing pages, or how published articles perform in Google. Do not use for GA4 sessions or conversions, which belong to google-analytics-report, and do not use for visibility inside AI assistant answers, which belongs to ai-visibility-report.
---

# Google Search Console report

Report what the brand's site did in Google search: who searched, what they saw, and what they clicked.

Every tool here is scoped to one brand and takes `brand_id`.

## Step 1: resolve the brand

Call `list_brands`. If more than one, ask which. Keep `brand_id` for every later call.

## Step 2: confirm Google is connected

Call `list_connectors`.

If Google is not connected for this brand, say so and stop. Tell the user to connect it in the brand's Connectors settings. Do not substitute another source and do not estimate.

## Step 3: refresh only if asked

`sync_search_console` pulls fresh data and takes time. Run it when the user wants current figures. Otherwise report what is stored, and say when it was last synced.

## Step 4: pull the numbers

- `get_search_performance` for clicks, impressions, CTR and average position over a period.
- `get_top_queries` for the searches bringing people in.
- `get_top_pages` for the pages receiving them.
- `get_published_content_urls` to tie performance back to articles produced in SearchFit.
- `get_audience_breakdown` for country and device splits.

## Step 5: report

State the date range and the site every number came from. A figure without its window cannot be checked.

Rules that keep the report honest:

- **Give clicks with impressions.** Impressions alone overstate reach. A page with 10,000 impressions and 12 clicks is a problem, not a success.
- **Search Console lags by roughly two to three days.** Never present the most recent two days as complete, and never read the dip there as a real decline. Say the window excludes them.
- **Average position is weighted across impressions.** It can move because a different mix of queries fired, not because any single ranking changed. When position moves and clicks do not, say that rather than implying the site moved.
- **Compare equal windows.** 30 days against 7 days is not a trend. If comparing, use matching lengths and say so.
- **CTR needs context.** A low CTR at position 3 is a title and description problem. The same CTR at position 30 is normal. Read them together.
- Never fill a gap with an estimate. If a query returned nothing, say it returned nothing.

## Step 6: say what to do about it

Close with a small number of specific actions tied to the data:

- High impressions and low CTR: rewrite the title and meta description for those queries.
- Position 5 to 15 on a valuable query: the page exists and nearly ranks, so improving it usually beats writing a new one.
- Queries with no matching page: a content gap. Hand off to the content-production skill.

## Boundaries

- Search Console measures Google only. If the user asks how the brand appears in ChatGPT, Perplexity or similar, that is the ai-visibility-report skill, and answering it with Search Console data would be wrong.
- For sessions, users, engagement or conversions, use the google-analytics-report skill.
- For a combined client or monthly report across several sources, use the performance-report skill.
