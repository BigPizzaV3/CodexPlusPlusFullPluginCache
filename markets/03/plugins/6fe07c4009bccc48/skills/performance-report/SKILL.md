---
name: performance-report
description: Generate a complete performance report for a brand across AI visibility, Google Search Console, Google Analytics and content. Use for a monthly report, a client report, a quarterly review, an executive summary, or "how are we doing overall". Do not use for a single metric lookup, which belongs to the focused skill for that source.
---

# Performance report

Produce the report an agency sends a client, or a marketing lead takes into a review: several sources, one narrative, with the AI surface alongside classic search.

Every tool here is scoped to one brand and takes `brand_id`.

## Step 1: agree the shape before gathering

Ask for, or confirm sensible defaults on:

- **Which brand.** Call `list_brands`. If more than one, ask.
- **The period.** Default to the last full calendar month, not the last 30 days, because a report that spans two part months cannot be compared with the next one.
- **The comparison.** Default to the equivalent previous period.
- **The audience.** A client report leads with outcomes. An internal review can carry the detail behind them.

Gathering everything first and asking afterwards wastes the user's time and credits, so settle this first.

## Step 2: check what is actually available

Call `list_connectors`.

Report on the sources that are connected and name the ones that are not. A report missing GA4 is still useful. A report that quietly omits GA4 without saying so is misleading, and the reader has no way to know.

## Step 3: gather

Work through the sources that are connected. Skip any that return nothing rather than padding.

**AI visibility**, the part most reports do not have:
- `get_visibility_overview` for share of tracked prompts where the brand appears.
- `get_competitor_analysis` for how rivals place on the same prompts.
- `get_visibility_insights` for the gaps worth acting on.
- `list_scans` to confirm more than one scan exists before describing any movement.

**Google search:**
- `get_search_performance` for clicks, impressions, CTR, position.
- `get_top_queries` and `get_top_pages` for what drove it.

**Analytics:**
- `get_ga4_metrics` for users and sessions.
- `get_ga4_traffic_breakdown` for channels.
- `get_ga4_events` for conversions.

**Content shipped in the period:**
- `list_content` and `list_publications` for what went live.
- `get_published_content_urls` to tie articles to their search performance.

**Site health**, when a technical audit is in scope:
- `get_audit_issues` for what is still broken.

## Step 4: write it

Structure:

1. **Headline.** Three or four numbers with their direction: AI visibility, clicks, users, conversions.
2. **What changed and why.** Tie movement to work done. "Published 6 articles, 4 now ranking, driving 340 of the 1,200 new clicks" is a report. "Traffic is up 12%" is a number.
3. **AI visibility.** Where the brand appears in AI answers, which competitors take the prompts it loses, and what would close the gap.
4. **Search performance.** Queries and pages that moved, with position and CTR read together.
5. **Audience and conversions.** What the traffic did.
6. **Next period.** Three or four specific actions drawn from the data, each naming the page, query or prompt it applies to.

## Step 5: rules that keep it trustworthy

A report is read by people who will not check the tools, so the burden of accuracy sits here.

- **Label every window and source.** Each number carries its date range and where it came from.
- **Never describe a trend from one measurement.** With a single AI visibility scan, report the position and say a trend needs a second scan.
- **Exclude the incomplete tail.** Search Console lags two to three days and GA4's current day is partial. Say the window excludes them.
- **Never invent a number, and never fill a gap to make the report look complete.** Say what is missing and why.
- **Report bad results plainly.** 0% AI visibility, a traffic fall, an article that did nothing: state it, then say what to do. A report that only carries good news is worthless, and the reader will discover the truth anyway.
- **Separate correlation from cause.** Traffic rising in the same month as a publishing push is not proof the push caused it. Say what the data supports and what it only suggests.
- **Compare like with like.** Equal length periods, same property, same market.

## Boundaries

- This skill reads and assembles. It does not publish content, start scans or delete anything. If the report shows work is needed, hand off to content-production, ai-visibility-report or technical-site-audit.
- A large scan or crawl mid report costs credits and time. Ask first, and say the report will otherwise use existing data.
- For one metric, use the focused skill instead. This one is for the whole picture.
