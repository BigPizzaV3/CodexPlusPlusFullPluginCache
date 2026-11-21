# SEO Intelligence: every operation

Generated from the tools' own descriptions. "Tool" is the platform tool that runs the operation on grouped connections (operation=<name>, params=<arguments>); on connections that list every operation as its own tool, call the operation name directly.

## Read (changes nothing)

| Operation | Tool | Use it when |
|---|---|---|
| `seo_audit` | seo_read | Wants an SEO, speed and measurement-tag audit of one web page. |
| `seo_content_lint` | seo_read | Wants a free check of a draft text for the patterns that make content read as AI-written. |
| `seo_core_web_vitals` | seo_read | Wants Core Web Vitals and PageSpeed performance of a web page (free). |
| `seo_history` | seo_read | Wants the SEO add-on queries already run on this account, to reuse their results. |
| `seo_rank_history` | seo_read | Wants rank positions already measured and stored for this account (free). |

## Add (preview, then confirm)

| Operation | Tool | Use it when |
|---|---|---|
| `seo_ai_overview` | seo_create | Wants Google's AI Overview answer for a search and whether a domain is cited in it. |
| `seo_anchors` | seo_create | Wants a domain's backlink anchor texts with their referring domains. |
| `seo_backlink_list` | seo_create | Wants the individual backlinks of a domain. |
| `seo_backlinks` | seo_create | Wants a summary of a domain's backlink profile. |
| `seo_best_pages_by_links` | seo_create | Wants a domain's pages ranked by backlinks. |
| `seo_brand_monitor` | seo_create | Wants web mentions, sentiment and source domains for a brand. |
| `seo_broken_backlinks` | seo_create | Wants the backlinks that point to broken pages of a domain. |
| `seo_bulk_spam_score` | seo_create | Wants spam scores for a list of domains. |
| `seo_competitor_gap` | seo_create | Wants the keywords competitors rank for and the target domain does not. |
| `seo_content_brief` | seo_create | Wants a search-intent and topic brief for a target keyword before writing. |
| `seo_full_analysis` | seo_create | Wants one combined technical, visibility, backlink and keyword analysis of a domain. |
| `seo_geo_citations` | seo_create | Wants AI-answer mention and citation metrics for a brand or domain. |
| `seo_geo_tracker` | seo_create | Wants to measure brand mentions and cited sources for given prompts across selected AI engines. |
| `seo_keyword_research` | seo_create | Wants SEO keyword ideas with search volume, cost per click and difficulty. |
| `seo_keyword_trends` | seo_create | Wants the search-interest trend of keywords over time. |
| `seo_link_intersect` | seo_create | Wants the domains that link to several given domains, optionally excluding one. |
| `seo_local_listings` | seo_create | Wants a business's directory listings, ratings and reviews. |
| `seo_paid_keywords` | seo_create | Wants a competitor domain's paid search keywords and estimated spend. |
| `seo_rank_tracker` | seo_create | Wants to measure and store search positions for domain and keyword pairs. |
| `seo_ranked_keywords` | seo_create | Wants the organic keywords a domain ranks for, with their search volume. |
| `seo_referring_networks` | seo_create | Wants a domain's referring domains grouped by IP address or subnet. |
| `seo_reviews` | seo_create | Wants a business's ratings and reviews from review sources. |
| `seo_serp_analysis` | seo_create | Wants the current Google top results for a keyword. |
| `seo_site_crawl` | seo_create | Wants to start a technical crawl of a whole website or read its results. Starting a crawl uses SEO add-on credits; reading a started crawl by task_id does not start a new one. |
| `seo_site_technologies` | seo_create | Wants the technologies and public contact details detected on a website. |
| `seo_technical_audit` | seo_create | Wants technical, performance and on-page checks for one URL from the SEO add-on. |

## Change, pause or delete (preview, then confirm)

| Operation | Tool | Use it when |
|---|---|---|
| `seo_rank_untrack` | own tool | Wants to stop the daily re-measurement of tracked keywords or a domain. |
