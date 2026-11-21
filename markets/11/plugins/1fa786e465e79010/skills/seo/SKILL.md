---
name: seo
description: SEO and AI-search visibility with Opus Growth - keyword research and trends, rankings and rank tracking, competitor keyword gaps and paid keywords, backlinks, technical crawls and page audits, Core Web Vitals, content briefs, Google AI Overviews and AI-engine citations (GEO), brand mentions, local listings and reviews. Use for organic search, SEO audits, competitor research or "does ChatGPT or Google AI mention us" questions. Covers how to reuse earlier results instead of running the same check again.
---

# SEO and AI-search visibility

Follow the `opus-growth` skill. Most `seo_` operations use SEO add-on credits; a few are free:
`seo_core_web_vitals`, `seo_audit`, `seo_content_lint`, `seo_rank_history`, `seo_history`.
Before running a paid query, check `seo_history`: the same domain or keyword may already have
been analysed and its result can be reused.

Search Console (`gsc_performance` and the other Search Console operations, `analytics-search` skill) is the site's own Google data and
free; use it first for the user's own site. SEO add-on data estimates any domain, including
competitors.

## Common tasks

| Task | Operations |
|---|---|
| Overall picture of a domain | `seo_full_analysis` |
| Keyword ideas with volume, CPC and difficulty | `seo_keyword_research`, trends `seo_keyword_trends` |
| What a domain ranks for | `seo_ranked_keywords` |
| Competitor gap (they rank, we do not) | `seo_competitor_gap` |
| Competitor's paid keywords and spend | `seo_paid_keywords`; their live ads `ad_library_competitor_ads` |
| Today's Google top results for a keyword | `seo_serp_analysis` |
| Track positions over time | `seo_rank_tracker` (measures and stores), `seo_rank_history` (free), stop with `seo_rank_untrack` |
| Technical health of a whole site | `seo_site_crawl` (start, then read by task id) |
| One page: speed, SEO, tags | `seo_audit`, `seo_core_web_vitals`, `seo_technical_audit` |
| Backlinks | `seo_backlinks`, `seo_backlink_list`, `seo_anchors`, `seo_broken_backlinks`, `seo_best_pages_by_links`, `seo_referring_networks`, `seo_link_intersect`, `seo_bulk_spam_score` |
| Before writing content | `seo_content_brief`; after drafting `seo_content_lint` |
| Local presence | `seo_local_listings`, `seo_reviews` |
| Brand mentions on the web | `seo_brand_monitor` |
| Technologies a site uses | `seo_site_technologies` |

## AI search (GEO)

- `seo_ai_overview`: Google's AI Overview for a search and whether the domain is cited.
- `seo_geo_citations`: mention and citation metrics for a brand across AI answers.
- `seo_geo_tracker`: runs given prompts on selected AI engines and records whether the brand is
  mentioned and which sources are cited. "Found but not cited" means the engine knows the brand
  but points to other pages: those pages are the content gap.
AI answers vary run to run; judge on repeated measurements, not one answer.

## Reading SEO numbers honestly

- Search volumes and traffic are estimates from third-party data; present them as ranges and
  trends, not exact visits. Search Console clicks are the real numbers for the user's own site.
- Keyword difficulty is relative; a new site wins long, specific queries first.
- Spam score is a signal, not a penalty. Do not advise disavowing links on that alone.
- Backlink counts differ between tools; compare a domain with its competitors in the same tool.

## Turning findings into work

1. Quick wins first: pages on positions 8-20 with many impressions (`gsc_performance`), titles
   with low CTR, broken pages that still have backlinks (redirect them).
2. Technical blockers next: noindex or canonical mistakes, slow pages (Core Web Vitals), broken
   internal links from the crawl.
3. Content gaps last: topics competitors rank for, written to the content brief's intent.
On WordPress apply fixes with the `wordpress` skill; on AI Server sites with the `ai-server`
skill; ask Google to recrawl with `gsc_request_indexing`.

## Every operation

The complete list of this area's operations, what each is for and the tool that runs it: `references/operations.md`.
