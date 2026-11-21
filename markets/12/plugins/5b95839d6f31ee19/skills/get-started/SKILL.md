---
name: get-started
description: How to use Camberstack to read a Google Ads account, Search Console, Google Analytics 4, Merchant Center and Tag Manager, and make only the changes the user approves. Use at the start of any Google Ads, Search Console, GA4, Merchant Center or Tag Manager task.
---

# Using Camberstack

Camberstack connects the user's Google Ads account and, optionally, Search Console, Google Analytics 4, Merchant Center (for products and Shopping, start with `merchant_accounts`, not `list_accounts`) and Tag Manager (for tags and conversion tracking, start with `tag_manager_containers`).

1. **Start with `list_accounts`.** Answer questions with `account_overview` and `run_gaql` (read-only GAQL `SELECT`).
2. **To change something:** call the `propose_` tool for that change (`propose_pause_campaign`,
   `propose_set_daily_budget`, `propose_mark_key_event`, …), show the user the summary, including any ⚠ line, and ask
   for approval. Only then call `apply_changes`.
3. **Never call `apply_changes` unless the user has explicitly approved that specific proposal in this conversation.**
   Applied proposals can be reversed with `propose_undo`, which makes a reversing proposal to approve and apply, except
   deletions Google can't reverse: their summary says so with a ⚠, so tell the user before they approve;
   `change_history` lists what was applied.
4. **Each Google service is added separately.** When a result says Search Console, Analytics, Merchant Center or Tag Manager isn't part of the
   connection, give the user its `grant_url` (one click adds it). Never tell them to reconnect.
5. For `keyword_ideas` and `keyword_metrics`, pass the account's own market: `location_ids` default to the United States.
6. **Search Console:** lead with `search_console_summary` (per-query rows leave out rare queries). Sitemaps and
   properties change through proposals (`propose_submit_sitemap`, `propose_delete_sitemap`, `propose_add_site`,
   `propose_remove_site`). Camberstack can't request indexing or verify a property; the user does those in Search Console.
7. **Tag Manager:** `tag_manager_setup` checks a container's tags and lists tracking `issues`. Tag changes
   (`propose_add_conversion_linker`, `propose_pause_tag`, …) stay in the workspace until `propose_publish_container`
   is approved and applied; say so when proposing them.
8. **Account 000-000-0001 is a demo** with sample data: anyone can try every tool on it, and changes there never
   touch Google. Always say when you are using it.
