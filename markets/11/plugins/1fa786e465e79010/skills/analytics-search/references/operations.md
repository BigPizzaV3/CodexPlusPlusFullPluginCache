# Analytics, Search Console and YouTube: every operation

Generated from the tools' own descriptions. "Tool" is the platform tool that runs the operation on grouped connections (operation=<name>, params=<arguments>); on connections that list every operation as its own tool, call the operation name directly.

## Read (changes nothing)

| Operation | Tool | Use it when |
|---|---|---|
| `ga4_list_ads_links` | google_analytics_read | Wants the Google Ads accounts linked to a Google Analytics 4 property. |
| `ga4_list_conversions` | google_analytics_read | Wants the key events (conversions) of a Google Analytics 4 property. |
| `ga4_list_data_streams` | google_analytics_read | Needs Google Analytics 4 data streams and their measurement IDs (G-…). |
| `ga4_list_properties` | google_analytics_read | Wants the Google Analytics 4 properties of the connected account. |
| `ga4_overview` | google_analytics_read | Wants Google Analytics 4 headline numbers: sessions, users, conversions and engagement. |
| `ga4_realtime` | google_analytics_read | Asks how many people are on their website right now (Google Analytics 4). |
| `ga4_report` | google_analytics_read | Wants Google Analytics 4 sessions, users or conversions broken down by channel, source, page, country, device or event. |
| `gsc_inspect_urls` | search_console_read | Wants the Google index status of many URLs at once. |
| `gsc_list_sites` | search_console_read | Wants the Search Console properties of the connected account. |
| `gsc_performance` | search_console_read | Wants organic Google Search clicks, impressions, CTR and position by query, page, country or device from Search Console. |
| `gsc_sitemaps` | search_console_read | Wants the sitemaps submitted to a Search Console property and their status. |
| `gsc_url_inspect` | search_console_read | Asks whether one URL is indexed by Google, and why. |
| `youtube_channels` | youtube_read | Wants their connected YouTube channels with subscribers and views. |
| `youtube_overview` | youtube_read | Wants YouTube channel views, watch time and subscriber changes over a period. |
| `youtube_top_videos` | youtube_read | Wants the most-watched videos of a YouTube channel. |
| `youtube_traffic_sources` | youtube_read | Asks how viewers find their YouTube videos. |

## Add (preview, then confirm)

| Operation | Tool | Use it when |
|---|---|---|
| `connect_ga4` | google_ads_create | Wants to connect Google Analytics 4. |
| `connect_search_console` | google_ads_create | Wants to connect Google Search Console. |
| `connect_youtube` | google_ads_create | Wants to connect a YouTube channel for its view and audience reports. |
| `ga4_create_conversion` | google_analytics_create | Wants to mark a Google Analytics 4 event as a key event (conversion). |
| `ga4_create_custom_dimension` | google_analytics_create | Wants a Google Analytics 4 custom dimension for an event or user parameter. |
| `gsc_add_site` | search_console_create | Wants to add a website property to Search Console. |
| `gsc_submit_sitemap` | search_console_create | Wants to submit or resubmit a sitemap to Google. |

## Change, pause or delete (preview, then confirm)

| Operation | Tool | Use it when |
|---|---|---|
| `ga4_link_google_ads` | own tool | Wants to link a Google Analytics 4 property to a Google Ads account. |
| `gsc_delete_sitemap` | search_console_edit | Wants to remove a submitted sitemap from Search Console. |
| `gsc_request_indexing` | search_console_edit | Wants Google to crawl new or updated pages now. |
| `select_google_resource` | google_ads_edit | Wants to switch which Business Profile location, Search Console property, Google Analytics property, YouTube channel or Tag Manager container Opus Growth works on. |
