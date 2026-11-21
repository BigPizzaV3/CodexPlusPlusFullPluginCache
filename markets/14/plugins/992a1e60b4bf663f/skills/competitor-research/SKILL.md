---
name: competitor-research
description: Brief a competitor's Shopify store, covering its profile and traffic, best-selling products, biggest and fastest-growing ads, email marketing, and similar stores. Use when the user names a competitor's brand or domain and asks how it sells, advertises or emails, or asks who a store's competitors are.
---

# Brief a competitor

Use the tools of the SellWinners connector. Tool calls use the user's SellWinners credits (`usage_get` shows what is left).

These steps and answer formats are defaults. When the user explicitly asks for a different format, order, number of results or SellWinners tool, follow the user. The rules on confirmations, public links, the plan and the monthly quota always apply.

## Steps

1. If the user gave a name that could match several brands, call `lookup` with it and confirm which one they mean. A domain needs no lookup. `analyze_shop_emails`, `search_emails`, `find_similar_shops`, `shop_report` and `compare_shops` take a domain or a shop id, not a name: for a brand name, call `lookup` first and pass the domain or shop id it returns.
2. For a full brief, call `brief_competitor` with `competitor` set to the domain, name or shop id. With no `sections` it returns all of them: `profile`, `products`, `ads`, `emails`, `similar`. Its ads are the biggest by reach. To see the ads gaining rank instead, pass `ad_rank_sort` `rank_delta` and `ad_rank_window` `7d`, `14d` or `30d`.
3. When the user asks about one area only, skip the full brief and answer that question alone: for its emails, `analyze_shop_emails` (below); for its competitors, `find_similar_shops`; for its ads or its products, `brief_competitor` with `sections` set to just `ads` or `products` (step 2's rank options apply to the ads). Otherwise go deeper only where the user's question needs it:
   - **Email strategy:** `analyze_shop_emails` with `shop` gives the sending rhythm, the days, the campaign types and the latest subjects. `search_emails` with `shop` and `intent` (`promo`, `welcome`, `abandoned_cart`, `newsletter` or `all`) finds specific emails, and `get_email_html` returns one email's HTML.
   - **The brand's ad accounts:** `search_advertisers` with the brand name as `query` lists its Facebook pages, not its ads. `scan_advertiser` with one page's `advertiser_id` reads that page in full.
   - **More competitors:** `find_similar_shops` with `shop`, sorted by `monthlyVisits`, `activeAds` or `growth30d`.
   - **One part of the store in depth:** `shop_report` with `shop` and a `report`: `products` (best sellers first), `advertisers` (its Facebook pages), `feed` (its newest ads and emails), `ad_ranking` (its Meta ads ranked over the last 7, 14 or 30 `days`) or `creative_tests` (its ads grouped by launch day).
   - **Several stores side by side:** `compare_shops` with up to 10 `shops` and a `metric`: `metaReach`, `googleLiveAds` or `tiktokPosts`.
   - **What the store runs on:** `detect_shopify_store` with its `url` says whether it is on Shopify, its theme and the Shopify apps it loads.

## Answer

Write a full brief in this order, and leave out any part the data doesn't cover:

1. **Snapshot:** traffic, main markets, active ads, product count.
2. **What they sell:** top products with prices and links.
3. **How they advertise:** main angles, formats and offers, with links to the top ads.
4. **How they email:** how often, which days, which campaign types, typical offers.
5. **Takeaways:** three to five concrete opportunities for the user.

When an answer carries `restrictions`, the user's plan shortened it. Say what was left out. Don't paste raw JSON.

When a tool says a request is outside the user's plan (`plan_not_eligible`), don't try to get the same data another way, with other brands or other SellWinners tools. Tell the user in one sentence what the message says, with the link it gives, and answer the rest of the question with what the plan covers.

A tool named here can be missing from the connector when the user's plan doesn't include it. Then say so in one sentence and answer with the tools that are there.

When a tool answers that the plan's credits are used up, or that the plan doesn't include MCP access, stop calling SellWinners tools for this request. Tell the user in one sentence, with the renew date, the wait or the link the message gives.
