---
name: ad-creative-research
description: Research ad creatives on Meta (Facebook and Instagram), Google and TikTok, with their hooks, copy, calls to action and landing pages. Use when the user wants ad inspiration, asks what ads a brand or niche is running, which creatives are scaling, or wants to study one ad in detail.
---

# Research ad creatives

Use the tools of the SellWinners connector. Tool calls use the user's SellWinners credits (`usage_get` shows what is left), so prefer the tools that answer in one call.

These steps and answer formats are defaults. When the user explicitly asks for a different format, order, number of results or SellWinners tool, follow the user. The rules on confirmations, public links, the plan and the monthly quota always apply.

## Pick the tool

- **Inspiration for a niche or product:** `creative_inspiration_pack` with `niche`, `keywords`, `max_ads` and `focus`: `reach` for the biggest ads, `new` for ads launched in the last 14 days, `long_running` for ads running 30 days or more. Each ad comes with its hook, copy, call to action and landing page.
- **One brand's Meta ads:** call `lookup` with the brand name or domain to get its shop id, then `search_ads` with `filters` `{"websiteIds": [<shop id>]}`. That returns all of the brand's ads, not one per brand.
- **Meta ads across brands:** `search_ads` with `query` or `keywords`, `status` `active`, and a `sort_by`: `reach` for the biggest, `reachGrowth7d` or `rankDelta7d` for the ones scaling now, `longestRunning` for proven winners, `newest` for fresh tests. Narrow with `media_type` (image, video, carousel, dco, dpa) and `country`. Results keep one ad per brand unless `filters` raise `maxAdsPerBrand`.
- **One ad in full:** `scan_ad` with the ad's `id` from `search_ads` as `ad_identifier`. It returns the creative, copy, video transcript and hook, spend, rank, the linked shop and the page's history. It also takes the id of a Google ad from `search_google_ads_library` or of a TikTok post from `search_tiktok_library`.
- **One advertiser's Facebook page:** `scan_advertiser` with the page id (`advertiser_id`) from `search_advertisers` or `lookup` gives the page's reach, spend, platforms and newest ads.
- **Google ads:** `search_google_ads_library`.
- **TikTok ads and organic posts:** `search_tiktok_library` with `type` `ad`, `organic` or `all`, and `domain` or `handle` to keep one brand.

Search tools answer with `data` and `pagination`. Ask for the next `page` only when the user wants more.

`create_ad_share_link` makes a public link that anyone holding it can open. Call it only when the user asks for a shareable link, and pass `confirm=true` once they have agreed that the ad will be public.

## Answer

- Group the ads by angle or hook rather than listing them one by one.
- For each ad give the brand, the hook (its opening line), the format, how long it has run or its reach signal, the call to action, the landing page, and a link to the creative.
- Close with what is working across the set: recurring hooks, offers, formats and lengths.
- When the user wants their own ads, write new hooks and scripts from those patterns in their brand's voice; don't copy a competitor's copy word for word. When they want SellWinners to draft the opening lines, `write_ad_hooks` takes the `niche`, the `product`, an `angle` and the `platform`, and returns three hooks.
- When an answer carries `restrictions`, the user's plan shortened it. Say what was left out.

When a tool says a request is outside the user's plan (`plan_not_eligible`), don't try to get the same data another way, with other brands or other SellWinners tools. Tell the user in one sentence what the message says, with the link it gives, and answer the rest of the question with what the plan covers.

A tool named here can be missing from the connector when the user's plan doesn't include it. Then say so in one sentence and answer with the tools that are there.

When a tool answers that the plan's credits are used up, or that the plan doesn't include MCP access, stop calling SellWinners tools for this request. Tell the user in one sentence, with the renew date, the wait or the link the message gives.
