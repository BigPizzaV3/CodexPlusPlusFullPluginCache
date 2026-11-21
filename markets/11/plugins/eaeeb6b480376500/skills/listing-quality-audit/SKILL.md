---
name: listing-quality-audit
description: Use when the user asks how good their Amazon product listings are, which listings need work, or what a listing's content problems are. Produces a listing-quality audit with the weakest listings and their specific findings.
---

# Listing-quality audit

1. Call `list_accounts` and choose an account whose `available_tools` include `listing_quality` (seller or vendor accounts).
2. Call `listing_quality` with `view=summary` for the account-level score, the scan freshness and the most common findings.
3. Call `listing_quality` with `view=items` to find the lowest-scoring listings. For each listing you discuss, call `view=item` with its `asin` to get the specific findings.
4. If the user asks about pending changes, use `view=updates` (and `view=update` with an `update_id`) to show the Amazon update queue. The tool is read-only: it reports findings and update status, it does not edit listings.
5. Answer with the overall score, the three to five listings that need the most work, the specific fix for each (title, bullets, images, description, attributes), and when the listings were last scanned.
