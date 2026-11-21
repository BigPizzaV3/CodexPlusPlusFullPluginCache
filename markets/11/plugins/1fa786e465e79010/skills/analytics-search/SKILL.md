---
name: analytics-search
description: Google Analytics 4, Google Search Console and YouTube with Opus Growth - traffic and key events by channel, source and landing page, organic queries and pages, index status and crawl requests, sitemaps, YouTube channel performance, and how paid and organic fit together. Use for website traffic, SEO performance in Search Console, indexing problems or YouTube channel questions.
---

# Analytics, Search Console and YouTube

Follow the `opus-growth` skill. These sources are read mostly; the few writing tools (key events,
Ads links, sitemaps, crawl requests, property setup) keep the preview and confirm step.

## Google Analytics 4

- Properties: `ga4_list_properties`. Overview KPIs: `ga4_overview`. Breakdowns: `ga4_report`
  (channel, source / medium, landing page, country, device, date, event).
- `conversions` in GA4 is the sum of every key event. To compare with an ad platform, split by
  `dimension='event'` and pick the one event that platform counts (`ga4_list_conversions` shows
  which events are key events).
- Which traffic converts: `ga4_report` by channel or source/medium with sessions and key events.
- Landing pages with traffic but no key events are a conversion problem on the site, not an ad
  problem (`marketing_insights` lists them with Search Console and Ads findings).
- Link GA4 and Google Ads (`ga4_list_ads_links`, `ga4_link_google_ads`) to import GA4 key events
  and audiences; avoid importing an event that Google Ads already counts with its own tag.
- `ga4_realtime` proves whether a new tag or event fires right now.
- GA4 numbers are lower than ad clicks: consent, ad blockers, bounces before the tag loads.

## Search Console

- `gsc_list_sites` lists properties; the site URL must match exactly (domain property
  `sc-domain:example.com` or URL prefix `https://www.example.com/`).
- Queries and pages: `gsc_performance` (dimension query, page, country, device, date, or
  `page,query` to see which page ranks for which term; two pages on the same query is
  cannibalization). Data lags about 2 days.
- Quick wins: pages at positions 8-20 with many impressions (page 2), titles with high
  impressions and low CTR.
- Index status: `gsc_url_inspect` (one URL), `gsc_inspect_urls` (several). Not indexed is usually
  a quality, duplicate or canonical issue, not a submission issue.
- `gsc_request_indexing` asks Google to crawl (about 200 URLs a day; the connected Google account
  must be an owner of the property). It is a crawl hint, not an indexing guarantee. Sitemaps:
  `gsc_sitemaps`, `gsc_submit_sitemap`.

## Paid and organic together

`marketing_overview` gives one funnel view of connected Google sources (Ads, Search Console, GA4,
YouTube, Business Profile) with the exact accounts it used. When a brand ranks first
organically, brand search ads still often protect the click from competitors; test before
cutting them, do not assume.

## YouTube

`youtube_channels`, `youtube_overview` (views, watch time, average view duration, subscribers),
`youtube_top_videos`, `youtube_traffic_sources`. Average view percentage and the first 30 seconds
decide reach; compare videos on those rather than raw views. YouTube ad campaigns are managed in
Google Ads (Demand Gen, video), not here.

## Every operation

The complete list of this area's operations, what each is for and the tool that runs it: `references/operations.md`.
