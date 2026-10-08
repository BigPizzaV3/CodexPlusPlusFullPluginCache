---
name: site-audit-triage
description: Triage a brand website's AEO health — technical, content, and AI-optimization issues that stop AI engines from crawling, understanding, and citing the site — and produce a prioritized fix plan. Use when the user asks to audit their site, asks why AI answers don't cite their pages, or wants technical/content/AEO issues found and ranked. Not for visibility analytics (use the visibility report) or for writing articles.
---

# Site Audit Triage

Turn ChatFeatured's site audit data into a prioritized, actionable fix plan.

## Steps

1. **Resolve the brand** via `list_organizations` → `list_brands`.
2. **Get the lay of the land** with `query_site_audit` `query: "overview"` — audit status, page counts, average scores, and open-issue counts by category. If no audit has run yet (check `run_status` when the overview looks empty), tell the user to start one from the ChatFeatured dashboard and stop.
3. **Enumerate the problems:**
   - `open_issues` — open issues grouped by category and check; run it per category (`technical`, `content`, `aeo`) if the user cares about one area.
   - `pages_needing_improvement` — the lowest-scoring pages with open issues.
4. **Drill into the worst pages** with `page_detail` for the 3–5 lowest scorers (pass each `pageUrl`) to see exactly which checks fail on them.
5. **Also check crawler access** with `query_crawler_analytics` (`stats`, then `top_pages`): if AI bots barely crawl the site, access problems outrank on-page fixes.
6. **Deliver a fix plan** ordered by impact:
   - Blockers first: anything stopping AI crawlers from reaching or reading pages (robots rules, timeouts, thin/duplicate content on key pages).
   - Then high-traffic pages with low scores — fixes there pay off fastest.
   - Then category-wide patterns (e.g. missing structured data across the blog) as a single batch item, not per-page noise.
   - For each item: what's wrong, which pages, and the concrete fix.

## Boundaries

- This skill reads audit data; it cannot start audits or change the website. Say so when the user asks you to "fix" something — hand them the exact change to make instead.
- Score numbers and issue counts come from the tool responses verbatim; don't estimate scores for unaudited pages.
- If the user wants new content to fix content gaps, route them to the content-gap workflow.
