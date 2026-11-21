---
name: listing-seo-refresh
description: Use when the seller wants better titles, tags, or descriptions for Etsy search, on one listing or a batch. Drafts changes and submits them for approval.
---

1. Load each listing with `get_listing`. Keep the product facts (garment, material, sizes, personalization) unchanged.
2. Draft: title 120–140 characters, most important search phrase first, readable; exactly 13 tags, each 20 characters or fewer, no repeats of title words where a new phrase fits; description opening that restates the key phrase naturally.
3. Never use trademarked brand, celebrity, or franchise names in titles or tags.
4. Submit one listing with `propose_listing_update`; several with one `propose_bulk_listing_update`. Report the status and point the seller to the approval card.
