---
name: v-marketing-kit
description: |-
  V-Kit (Marketing Kit): the user's own ad, analytics and subscription numbers through the v-marketing-kit connector — spend, impressions, clicks, installs, events, campaigns, conversions, MRR, trials, churn, revenue, App Store reviews. Use when the question is about marketing numbers, even if the source is not named ("how much did we spend", "how many installs", "what is wrong with the campaign", "App Store sales", "reviews", "Google Play installs", "search queries"). Tools are one per operation, named mk_<source>_<operation>: Meta Ads, Facebook Pages, Instagram, TikTok Ads, Apple Ads, Google Ads, GA4, Search Console, Google Play, AppsFlyer, RevenueCat, App Store Connect and the public App Store; plus mk_status and mk_feedback_send, mk_feedback_reply, mk_feedback_list, mk_feedback_get. Several clients (agencies): name the client in each call. Start with mk_status.
metadata:
  version: "1.23.4"
  title: v-marketing-kit
---

# V-Kit (Marketing Kit)

The user's own ad, analytics and subscription numbers, read through the v-marketing-kit
connector (server marketing-kit.app). Every operation is its own tool, named
`mk_<source>_<operation>` — for example `mk_ga4_report`, `mk_meta_insights`,
`mk_revenuecat_chart`, `mk_app_store_connect_sales`, `mk_apple_lookup`. Two operations
write (`mk_appsflyer_integration_copy`, `mk_app_store_connect_analytics_enable`); everything
else only reads. `mk_status` checks the connections, `mk_feedback_send` sends a note to the
developer (`mk_feedback_reply`, `mk_feedback_list`, `mk_feedback_get` — the replies and the history). In this file `mk_<source>_*` means the whole family of one source.

| Family | What it is for |
|---|---|
| `mk_meta_*` | Meta Ads (paid Facebook and Instagram ads): spend, impressions, clicks, installs as Meta counts them, campaigns, ad sets, ads, event counters, custom conversions |
| `mk_fb_pages_*` | Facebook Pages, organic: reach, posts, engagement, followers |
| `mk_instagram_*` | Instagram professional account, organic: reach, views, followers, posts and reels |
| `mk_tiktok_*` | TikTok Ads: spend, impressions, clicks, conversions; campaigns, ad groups, ads (no organic TikTok) |
| `mk_apple_ads_*` | Apple Ads (App Store search ads): spend, impressions, taps, installs by Apple's attribution; campaigns, ad groups, keywords, negative keywords, ads, search terms, impression share; read-only |
| `mk_google_ads_*` | Google Ads: GAQL reports and lists of campaigns, ad groups, ads, conversion actions |
| `mk_ga4_*` | Google Analytics 4: events and behaviour in the app and on the site, funnels, users and sessions, realtime, metadata |
| `mk_search_console_*` | Google Search Console: organic Google search — queries, pages, clicks, impressions, CTR, position; sitemaps; URL inspection |
| `mk_google_play_*` | Google Play Console: the user's own Android apps — installs and uninstalls, estimated sales, earnings after Google's fee, subscription counts, reviews, refunds, Android vitals (crashes, ANR); read-only; reports are 3–7 days late |
| `mk_appsflyer_*` | AppsFlyer: installs and in-app events by source, aggregate and raw reports, purchase duplicates between the app and RevenueCat (`mk_appsflyer_purchase_dedup`), copy of integration settings after confirmation (`mk_appsflyer_integration_copy`) |
| `mk_revenuecat_*` | RevenueCat: subscriptions — MRR, ARR, active subscriptions and trials, revenue, churn, trial conversion, LTV, refunds, products and offerings, one customer's subscription |
| `mk_app_store_connect_*` | App Store Connect: Apple's official numbers for the user's own apps — downloads, proceeds, subscription reports, the App Store funnel (impressions → page views → downloads), sessions, crashes, reviews with replies, versions, experiments; turning on Analytics Reports after confirmation; data arrives with a one-day delay |
| `mk_apple_*` (`mk_apple_lookup`, `mk_apple_reviews`, `mk_apple_charts`) | Public App Store data of any app, no key: version and release date, rating, reviews, chart positions by country |
| `mk_status` | Server status: versions, who is signed in, the account's clients (`clients`), which sources are authorised, API state |
| `mk_feedback_send` | A note to the V-Kit developer — a bug, something missing, an idea (only after the user says yes) |
| `mk_feedback_reply` | The user's answer to the developer's reply (`feedback_reply`) |
| `mk_feedback_list`, `mk_feedback_get` | The notes the user already wrote; one note with its whole thread |

The arguments of each tool are in its input schema; do not guess argument names outside it. With several clients on
the account, data tools also take `client` (see "Clients").

## Rules from the server

The general rules (start with `mk_status`, which client, do not call an unauthorised source, never invent
numbers, which tool to take, period and time zone, large results as links, writes only after
a plan and a confirmation in words, `api.state`, 424 errors as they are, keys never in the
chat, feedback invitations and the developer's reply) arrive from the connector's server in
its `instructions` when the connection starts and change with the server, not with this
plugin. This file is a reference for the sources: operations, fields, caveats. If you do not
have the server's rules, be careful: `mk_status` first, never invent numbers, never ask for
keys in the chat, write only after a confirmation that names the action and the object.

## Which source to take

- **Meta Ads** (`mk_meta_*`) — paid ads in Facebook and Instagram: spend, CPI, campaigns, ad sets, ads.
- **Facebook Pages** (`mk_fb_pages_*`) — organic page numbers: reach, posts, engagement, followers.
- **Instagram** (`mk_instagram_*`) — organic numbers of a professional account: reach, views, followers, posts and reels.
- **TikTok Ads** (`mk_tiktok_*`) — ad spend, impressions, clicks and conversions in TikTok. Organic TikTok (videos, followers) is not covered — say so, do not substitute ads for it.
- **Apple Ads** (`mk_apple_ads_*`) — the App Store search ads of the user's own ad accounts: spend, impressions, taps,
  installs by Apple's attribution, campaigns, ad groups, keywords and search terms, impression share. Not AppsFlyer
  (attribution across networks) and not App Store Connect (every store download): show them side by side, never merge.
- **Search Console** (`mk_search_console_*`) — organic Google search before the click: which queries find the site, clicks and impressions, CTR, average position, pages from search, indexing, sitemaps.
- **Google Play** (`mk_google_play_*`) — Google's official numbers for the user's **own** Android apps: installs and
  uninstalls, estimated sales and earnings after Google's fee (per currency), subscription counts, reviews, refunds
  (voided purchases), Android vitals (crashes, ANR). Reports are 3–7 days late. Not AppsFlyer (which campaign brought the
  install) and not RevenueCat (subscription billing across stores): show them side by side and say why they differ.
- **GA4** (`mk_ga4_*`) — behaviour after the click, in the app and on the site.
- **Google Ads** (`mk_google_ads_*`) — paid Google.
- **AppsFlyer** (`mk_appsflyer_*`) — attribution: installs and events by media source and campaign, non-organic against organic.
- **RevenueCat** (`mk_revenuecat_*`) — the money of app subscriptions: MRR, ARR, active subscriptions and trials, revenue, trial conversion, churn, refunds, LTV, cohorts, one customer's subscription.
- **App Store Connect** (`mk_app_store_connect_*`) — Apple's official numbers for the user's **own** apps: downloads, redownloads and updates by country and device, proceeds, subscription reports, the store funnel, sessions, crashes, reviews with replies, versions, Product Page Optimization. One-day delay; Apple counts days in Pacific time.
- **App Store, public** (`mk_apple_*`) — public data of **any** app without a key: rating, current version, chart positions, public reviews, competitors included.

Choices that the tool name does not settle: "ads in Instagram" is `mk_meta_*` (breakdown
`publisher_platform`), the reach of the account is `mk_instagram_*`; "traffic from search" is
`mk_search_console_*` before the click and `mk_ga4_*` after it. `mk_fb_pages_*` and
`mk_instagram_*` work through the Meta connection, `mk_search_console_*` through the Google
connection (`mk_google_play_*` has its own Google sign-in): an old connection answers `reauthorize: true` / `missing_scopes` — the user presses
"Authorize" for that provider once more at https://marketing-kit.app/connections; the provider's
other sources keep working.

## Start of a session: `mk_status`

Call `mk_status` once at the start of the session.

- **Versions.** Compare `server.version` with the version of this skill (`1.23.4`). The server is newer — say in one line that the plugin updates itself, and go on.
- **First step.** If `mk_status` returns `next_step`, say that phrase with its link before anything else.
- **Sources.** `authorized: false` for the source you need — follow the server's rules: do not call its tools, send the user to https://marketing-kit.app/connections (Google — GA4, Google Ads, Search Console; Google Play — its own Google sign-in; Meta — ads, Pages, Instagram; TikTok; Apple Ads; the keys of AppsFlyer, RevenueCat, App Store Connect) and say the source's `note` as it is.
- **No `mk_*` tools in this chat** (the connector is not connected or is switched off) — there is nothing to call, so do not look for workarounds and do not suggest other services first. Tell the user, in this order: connect the v-marketing-kit connector in the plugin or connector settings of the assistant, sign in with Google or Meta, press Allow, start a new chat; then add the sources at https://marketing-kit.app/connections. Help: https://marketing-kit.app/install. Never invent numbers without the tools.
- **Sign-in.** Signing in to V-Kit happens once, when the connector is connected: a marketing-kit.app page opens, sign in with Google or Meta. The answer "sign in required" or `source_not_authorized` — send the user to https://marketing-kit.app/connections. Do not ask the user to type account details into the chat.

## Clients (several customers in one account)

An agency or a freelancer can keep up to three **clients** in one V-Kit account: each is a named group of
connections and keys (one customer's Google, Meta, AppsFlyer and so on). `mk_status` lists them in
`clients: [{ slug, name, sources }]`; every data tool `mk_<source>_<operation>` takes an optional `client` argument; the `mk_<source>_reference` tools and the public App Store tools (`mk_apple_lookup`, `mk_apple_reviews`, `mk_apple_charts`) have none (they do not depend on the client); `mk_apple_ads_*` takes it like every other data tool.

- **One client** (`mk_status.clients` has one entry — most accounts): never mention clients and never pass `client`.
- **Several clients:** every data call carries `client` — the slug from `mk_status.clients` (the name works too).
  - The question names a customer ("Acme: spend last week") — pass that client.
  - It names none and no client was chosen in this chat yet — ask **once**, listing the names, then keep that client
    for the rest of the chat; the user can switch in words ("now Globex").
  - A name that is not in the list — show the list, do not guess.
  - The answer `client_required` (with the list `clients`) — the same: ask which client, do not repeat the call blindly.
  - `mk_status` without `client` answers `client_required: true` instead of the sources block; with `client` — the
    sources of that client.
- **Answers:** with several clients, name the client in the first line of every answer with numbers. Never add up
  numbers of different clients; to compare them, show them side by side.
- Clients are added, renamed and deleted only at https://marketing-kit.app/connections, not in the chat; more than three —
  https://marketing-kit.app/clients/more.
- To connect another Google, Meta, TikTok, Google Play or Apple Ads account for a client, the user presses "Copy link for another
  browser" on https://marketing-kit.app/connections and opens it where that account is signed in; never ask for
  account details in the chat.

Example — three clients: Main, Acme, Globex.

> **User:** How much did we spend on Meta last week?
> **Assistant:** Which client — Main, Acme or Globex?
> **User:** Acme.
> *(the assistant calls `mk_meta_insights` with `client: "acme"` and last week's dates)*
> **Assistant:** **Acme** — Meta Ads, 5–11 October: …
> **User:** And Globex?
> *(the same call with `client: "globex"`; the answer starts with **Globex**)*

> **User:** Acme: spend last week.
> *(no question — the client is named: `mk_meta_insights` with `client: "acme"` straight away)*

## API versions of the sources (`api`)

What to say when `api.state` is not `ok` is in the server's rules. For `api.breaking: unknown`
make one narrow control request, compare the result with the known number from the source's
`references/` file and decide `yes` or `no`; say what you decided.

## Refusals of the server

These are answers, not breakages — read the `message` and act:

- `source_not_authorized` — the source is not connected or its access was reset: send the user to https://marketing-kit.app/connections. With `reauthorize: true` / `missing_scopes` the provider named in `message` (Meta or Google) must be authorised again ("Authorize" on the same page); its other sources keep working.
- `source_not_configured` — the server is not configured by its owner for this source: say so, do not try to work around it.
- `appsflyer_token_missing`, `app_store_connect_key_missing` (and `app_store_connect_vendor_number_missing`), `revenuecat_key_missing` — the key is not saved: see the section on keys below.
- `google_play_bucket_missing` — the Google Play reports bucket id is not saved: Play Console > Download reports > Copy Cloud Storage URI, pasted on the Google Play card at https://marketing-kit.app/connections#google-play. Nothing finds it automatically.
- `invalid_args` — fix the arguments by `message` and the tool's input schema, once.
- `source_error` — the source refused; say `message` and `explanation` as they are, do not replace the numbers. `code: "SERVICE_DISABLED"` for GA4, Google Ads, Search Console or Google Play means the API is not enabled in the server's Google Cloud project: `message` names the API and the link for the owner; that is the owner's setting, reconnecting does not help.
- `proxy_error` — the server's answer did not arrive (a network page instead of the answer): repeat in a minute, then `mk_status`.

**Step-by-step guides** for every source are on the site, one link per source:
`https://marketing-kit.app/connections#<source>` — `ga4`, `google_ads`, `search_console`, `meta`,
`fb_pages`, `instagram`, `google-play`, `tiktok`, `apple-ads`, `appsflyer`, `revenuecat`, `app_store_connect`, `apple`. When the
user does not know how to connect a source or what an error means, give that link.

## Keys: AppsFlyer, RevenueCat, App Store Connect, Google Ads, Google Play

The user saves them on https://marketing-kit.app/connections (the server keeps them encrypted):

- **AppsFlyer** — API token V2 from AppsFlyer → profile menu → Security Center → AppsFlyer tokens (the one token is enough for reading and for `mk_appsflyer_integration_copy`). Guide: https://marketing-kit.app/connections#appsflyer.
- **RevenueCat** — a secret API key **V2** with read-only rights (RevenueCat → Project settings → API keys → + New secret API key, version V2, Charts & Metrics / Customer Information / Project Configuration — Read). v1 keys and public SDK keys do not work. Guide: https://marketing-kit.app/connections#revenuecat.
- **App Store Connect** — a team key: Issuer ID, Key ID and the `.p8` file (App Store Connect → Users and Access → Integrations → Team Keys) and the vendor number for sales and subscriptions. Saved only at https://marketing-kit.app/connections#app-store-connect; the `.p8` file is never sent in the chat. The Admin role covers everything; Sales and Reports or Finance is enough for sales, subscriptions and analytics, App Manager for apps, reviews and versions; turning on analytics needs Admin.
- **Google Play** — no key: "Connect Google Play" (its own Google sign-in, read-only) and the reports bucket id (Play Console > Download reports > Copy Cloud Storage URI), both on the Google Play card at https://marketing-kit.app/connections#google-play. Nothing finds the bucket automatically.
- **Google Ads** — nothing to enter: the server finds the manager account (MCC) itself. A login customer ID at https://marketing-kit.app/connections#google_ads (section Advanced) is needed only when the account is visible through several managers and a specific one is wanted.

Never ask for a token or key in the chat. On `appsflyer_token_missing` / `revenuecat_key_missing` / `app_store_connect_key_missing`, or `authorized: false` for `appsflyer` / `revenuecat` / `app_store_connect` in `mk_status`, say where to get it and where to save it (give the guide link), and wait until the user has done it.

## Tools by source

Each operation below is its own tool; its arguments are in the tool's input schema (required ones are marked `*`).

### Meta

- `mk_meta_accounts` — the source's available accounts. Arguments: none
- `mk_meta_insights` — performance report (spend, impressions, clicks, actions...), level/breakdowns/attribution windows, synchronous or as an async report. Arguments: period*, level, fields, breakdowns, action_attribution_windows, act_id, force_async, limit, after
- `mk_meta_objects` — campaigns/adsets/ads — status, objective, budgets (in minor units), targeting. Arguments: level, act_id, effective_status, limit, after
- `mk_meta_events` — event counts for a period with no source breakdown — actions from insights + pixel stats. Arguments: period*, act_id, pixel_id
- `mk_meta_conversions` — custom conversions of the ad account (cached, not fetched on every report). Arguments: act_id
- `mk_meta_reference` — Reference data for Meta Ads insights: the standard insights fields (spend, impressions, clicks, actions…) and the breakdowns (publisher_platform, country, age, gender…) with a note on combinations. Arguments: none

### Facebook Pages

- `mk_fb_pages_accounts` — Facebook Pages the user manages — id, name, category, followers, tasks (page tokens are never returned). Arguments: none
- `mk_fb_pages_page_insights` — page metrics per day for a period (reach, content views, engagements, followers); periods over 90 days are split. Arguments: period*, page_id*, metrics, metric_period
- `mk_fb_pages_posts` — published posts of a page for a period with reaction, comment and share counts. Arguments: period*, page_id*, limit
- `mk_fb_pages_post_insights` — insights for 1–25 posts of a page (reach, content views, clicks, reactions by type). Arguments: page_id*, post_ids*, metrics
- `mk_fb_pages_reference` — Reference data for Facebook Pages: live page and post metrics with their periods, the post fields, the deprecated metrics with replacements, and limits (100+ followers, 90 days per request). Arguments: none

### Instagram

- `mk_instagram_accounts` — Instagram professional accounts linked to the user's Facebook Pages — username, followers, media count. Arguments: none
- `mk_instagram_account_insights` — account metrics for a period (reach, views, engaged accounts, interactions, follows); windows of up to 30 days, optional breakdown and daily series. Arguments: period*, ig_user_id*, metrics, breakdown, time_series
- `mk_instagram_media` — posts, reels and carousels of an account published in a period with likes and comments counts. Arguments: period*, ig_user_id*
- `mk_instagram_media_insights` — insights for 1–25 media items (reach, views, saves, shares, interactions); unsupported metrics per media type are reported in errors. Arguments: media_ids*, metrics
- `mk_instagram_reference` — Reference data for Instagram insights: live account and media metrics with metric types and breakdowns, the media fields, the deprecated metrics with replacements, and data delays and limits. Arguments: none

### TikTok Ads

- `mk_tiktok_accounts` — advertisers authorized for the connection — advertiser_id, name, currency, timezone, status. Arguments: none
- `mk_tiktok_report` — ad performance report (spend, impressions, clicks, conversions...) by advertiser/campaign/ad group/ad, optional daily split; long periods are split into 30-day windows automatically. Arguments: period*, advertiser_id*, level, daily, metrics, campaign_ids, adgroup_ids
- `mk_tiktok_objects` — campaigns / ad groups / ads of an advertiser — status, objective, budget. Arguments: advertiser_id*, level, status
- `mk_tiktok_reference` — Reference data for TikTok Ads reports: report levels (advertiser, campaign, adgroup, ad) with their ids and name metrics, dimensions, metrics with descriptions, the default metrics, and notes. Arguments: none

### Apple Ads

- `mk_apple_ads_accounts` — Apple Ads ad accounts the grant covers — account_id, name, org, roles, currency, time zone, status. Arguments: none
- `mk_apple_ads_campaigns` — campaigns of an ad account — status, app (promotedObjectId), daily budget, bid strategy, schedule. Arguments: account_id, status, app_id
- `mk_apple_ads_adgroups` — ad groups of an ad account or campaign — status, pricing model, schedule. Arguments: account_id, campaign_id, status
- `mk_apple_ads_keywords` — keywords of a campaign or ad group — text, match type, bid, status. Arguments: account_id, campaign_id, adgroup_id, status
- `mk_apple_ads_negative_keywords` — negative keywords of a campaign (campaign and ad group level) or of an ad group — text, match type, status. Arguments: account_id, campaign_id, adgroup_id
- `mk_apple_ads_ads` — ads of an ad account, campaign or ad group — creative, status. Arguments: account_id, campaign_id, adgroup_id, status
- `mk_apple_ads_report` — App Store performance report by campaigns / ad groups / keywords / search terms / ads — spend, impressions, taps, installs, CPT, CPI; total or daily / weekly / monthly, optional split by country, device, age or gender. Arguments: period*, account_id, level, granularity, campaign_id, adgroup_id, group_by, metrics, time_zone
- `mk_apple_ads_impression_share` — impression share of an app by search term and country — share range, rank, search popularity; daily or weekly. Arguments: period*, account_id, app_id*, granularity, report_type, countries
- `mk_apple_ads_reference` — Reference data for Apple Ads reports: report levels with their split dimensions (group_by) and whether they need a campaign, granularity limits, metrics with descriptions, impression share fields and limits, and the Apple Ads API roles. Arguments: none

### Google Ads

- `mk_google_ads_accounts` — accessible customer_ids (customers:listAccessibleCustomers). Arguments: refresh
- `mk_google_ads_report` — arbitrary GAQL report via googleAds:search; a period and LIMIT are required. Arguments: period*, customer_id*, query*
- `mk_google_ads_objects` — reference lists: campaigns / ad_groups / ads / conversion_actions. Arguments: customer_id*, object*, status_filter, limit
- `mk_google_ads_reference` — Live GAQL field metadata from Google (googleAdsFields): for each field its category, data type, whether it can be selected, filtered or sorted, which fields it can be selected with, and enum values. Arguments: names, name_like

### Google Analytics 4

- `mk_ga4_report` — regular (Core) runReport report — dimensions/metrics/filters/orderBys, a period is required, offset/limit with auto-pagination for large volumes, returnPropertyQuota; the response flags sampling and thresholds. Arguments: period*, property_id*, dimensions, metrics*, dimension_filter, metric_filter, order_bys, offset, limit
- `mk_ga4_realtime` — runRealtimeReport for the last ~30 minutes, with its own (Realtime) quota separate from Core reports. Arguments: property_id*, dimensions, metrics*, dimension_filter, metric_filter, order_bys, limit
- `mk_ga4_metadata` — the property's available dimensions and metrics (getMetadata), including registered custom customEvent:/customUser: ones — check them before report/realtime when using non-public field names. Arguments: property_id*
- `mk_ga4_accounts` — the source's available accounts. Arguments: none

### Google Search Console

- `mk_search_console_sites` — Search Console properties of the Google account (URL-prefix and sc-domain) with the permission level. Arguments: none
- `mk_search_console_accounts` — same as sites, in the shared accounts shape. Arguments: none
- `mk_search_console_report` — Search Analytics — clicks, impressions, CTR and average position for a required period by date/query/page/country/device (search type web, image, video, news, discover, googleNews; filters; up to 50 000 rows, paged by 25 000); totals with impression-weighted position. Arguments: period*, site_url*, dimensions, search_type, filters, aggregation_type, data_state, row_limit, start_row
- `mk_search_console_sitemaps` — submitted sitemaps with errors, warnings, last download and submitted URL counts. Arguments: site_url*, sitemap_index
- `mk_search_console_inspect` — URL Inspection — Google index status of one URL (verdict, coverage, canonical, last crawl). Arguments: site_url*, url*, language_code
- `mk_search_console_reference` — Reference data for Search Console: metrics, dimensions, search types, filter operators and the data limits (delay, retention, row limits, time zone). Arguments: none

### Google Play

- `mk_google_play_apps` — apps of the Google Play developer account (package name, title) from the Play Developer Reporting API. Arguments: page_size, page_token
- `mk_google_play_installs` — installs, uninstalls and upgrades by day from the monthly Play Console statistics files, by one dimension (country, device, app version, OS version, carrier, language) plus daily totals; data is 3 to 7 days late. Arguments: package, month, date_from, date_to, dimension
- `mk_google_play_sales` — estimated sales per order from the monthly Play Console report (buyer-currency amounts before Google fees), totals per currency and financial status, never converted. Arguments: package, month, date_from, date_to, product_type
- `mk_google_play_earnings` — the monthly earnings report (charges, Google fees, taxes, refunds per transaction), totals per merchant currency and transaction type, never converted. Arguments: package, month
- `mk_google_play_subscriptions` — new, canceled and active subscription counts per product, base plan, offer and country; counts only, no revenue. Arguments: package, month, date_from, date_to, product_id
- `mk_google_play_reviews` — reviews of the last 7 days from the Google Play Developer API (rating, text, device, developer reply, paging, translation), or a whole month from the reports bucket with month. Arguments: package, max_results, page_token, translation_language, month
- `mk_google_play_refunds` — voided purchases (refunds and chargebacks) of the last 30 days with order id, time, source and reason. Arguments: package, date_from, date_to, max_results, page_token
- `mk_google_play_vitals` — Android vitals from the Play Developer Reporting API — crash and ANR rates by day or hour with dimensions (version, device, country, API level), end clamped to the latest data. Arguments: package, metric_set, aggregation, date_from, date_to, dimensions, metrics, user_cohort, page_size, page_token
- `mk_google_play_reference` — Reference data for Google Play Console: report files and columns (installs, sales, earnings, subscriptions), install dimensions, vitals metrics and dimensions, required Play Console permissions, data delays and limits. Arguments: none

### AppsFlyer

- `mk_appsflyer_accounts` — the account's apps (app_id, platform, name) — App list API (dev.appsflyer.com/hc/reference/app-list-ad-nets-api-get). Arguments: none
- `mk_appsflyer_aggregate` — aggregated Pull API reports (daily_report, partners_report, partners_by_date_report, geo_report, geo_by_date_report) — installs and in-app by media source/campaign/adset/geo; a period is required. Arguments: period*, app_id*, report*, timezone, media_source, category, currency, additional_fields, maximum_rows
- `mk_appsflyer_raw` — raw Pull API events row by row (installs_report, in_app_events_report, organic_installs_report, organic_in_app_events_report) — only with the Raw Data module in the plan; personal data (device IDs, customer user IDs, IPs) is never returned. Arguments: period*, app_id*, report*, timezone, media_source, event_name, geo, additional_fields, maximum_rows
- `mk_appsflyer_purchase_dedup` — purchase duplicates between the app (SDK) and server-to-server events (RevenueCat): raw in-app events for up to 31 days by Event Source and receipt validation, duplicate groups, signals and the recommended one-source-per-event scheme; counts only, no ids; needs the Raw Data module. Arguments: period*, app_id*, timezone, event_names, first_purchase_events, match_window_minutes, maximum_rows
- `mk_appsflyer_integration_copy` — Copy AppsFlyer partner-integration settings from one app to another for one platform. Arguments: pid*, platform*, from_app_id*, to_app_ids*, dry_run, confirm
- `mk_appsflyer_reference` — Reference data for AppsFlyer: the names of the aggregate and raw (in-app events, installs…) reports, example raw columns, what the purchase duplicate check returns, and notes on the Raw Data module. Arguments: none

### RevenueCat

- `mk_revenuecat_projects` — RevenueCat projects of the connection with their apps (App Store, Play, Stripe…). Arguments: none
- `mk_revenuecat_accounts` — same as projects, in the shared accounts shape. Arguments: none
- `mk_revenuecat_overview` — key subscription metrics now — MRR, active subscriptions, active trials, revenue, new customers and active users of the last 28 days. Arguments: project_id, currency
- `mk_revenuecat_revenue` — total revenue of the project for a required period — gross, net of taxes or proceeds. Arguments: period*, project_id, revenue_type, currency
- `mk_revenuecat_chart` — a RevenueCat chart for a required period (mrr, revenue, actives, trials, churn, conversion_to_paying, trial_conversion, ltv, refunds, cohorts…) by day/week/month with segments and filters; rows date × measure × segment. Arguments: period*, project_id, chart*, resolution, segment, limit_num_segments, filters, selectors, currency, totals_only
- `mk_revenuecat_chart_options` — segments, filters, resolutions and selectors available for one chart. Arguments: project_id, chart*
- `mk_revenuecat_products` — products of the project (store identifier, type, duration, trial). Arguments: project_id, app_id
- `mk_revenuecat_entitlements` — entitlements of the project with their products. Arguments: project_id
- `mk_revenuecat_offerings` — offerings and packages (which products the paywall shows), the current offering. Arguments: project_id
- `mk_revenuecat_customer` — one customer by app user id — active entitlements, subscriptions (status, renewal, period, revenue) and purchases; personal data is not returned. Arguments: project_id, app_user_id*, environment
- `mk_revenuecat_reference` — Reference data for RevenueCat: the list of charts with descriptions, overview metrics, resolutions, currencies, revenue types, subscription statuses, rate limits and notes. Arguments: none

### App Store Connect

- `mk_app_store_connect_apps` — apps of the App Store Connect team (Apple id, name, bundle id, SKU, primary locale). Arguments: none
- `mk_app_store_connect_accounts` — same as apps, in the shared accounts shape. Arguments: none
- `mk_app_store_connect_sales` — Apple's own Sales and Trends for a required period (up to 92 days daily, or monthly) — installs, redownloads, updates, in-app purchases, subscription units, refunds and proceeds per currency (never converted), by date/country/device/product/app/product type; reports are Pacific-time, D+1. Arguments: period*, app_id, group_by, frequency
- `mk_app_store_connect_subscriptions` — subscription reports for a required period (up to 92 days) — report=summary: active subscriptions, trials, billing retry and grace period by day (snapshot); report=events: Subscribe, trial starts and conversions, Cancel, Refund, Reactivate counts by event/date/country/subscription. Arguments: period*, report, group_by
- `mk_app_store_connect_analytics` — App Store Analytics Reports of one app — funnel (impressions, page views, downloads, conversion), by source, sessions, installs/deletions, crashes, or any report by name; says so when analytics_enable has not been run for the app. Arguments: period*, app_id*, report, report_name, category, group_by
- `mk_app_store_connect_analytics_enable` — Enable Analytics Reports for an App Store app: creates an ONGOING Analytics Reports request in App Store Connect. Arguments: app_id*, dry_run, confirm
- `mk_app_store_connect_reviews` — customer reviews of an app with developer responses, filtered by territory, rating, period and response; average rating and counts; read-only. Arguments: app_id*, territory, rating, period, has_response, limit
- `mk_app_store_connect_versions` — App Store versions of an app (state, release type and date) with optional localized texts, plus app infos (name, subtitle). Arguments: app_id*, platform, limit, include_localizations
- `mk_app_store_connect_experiments` — Product Page Optimization experiments with treatments and custom product pages of an app; the API gives no test results. Arguments: app_id*
- `mk_app_store_connect_reference` — Reference data for App Store Connect: Sales and Trends columns, product type identifiers, subscription report columns and events, Analytics Reports names, data latency, rate limit and what the API does not provide. Arguments: none

### App Store

- `mk_apple_lookup` — app metadata by ID (version, rating, release date). Arguments: id*, country
- `mk_apple_reviews` — latest user reviews. Arguments: id*, country, page
- `mk_apple_charts` — top apps by country and chart type. Arguments: country, chartType*, limit, genre, find_id, full

The source sections that follow explain how to read each source. Inside a section, a bare word
like `report`, `chart` or `accounts` names an operation: it is the tool `mk_<source>_<that word>`
of that section's source.

## Source: Meta (`mk_meta_*`)

`mk_meta_*` — Meta Marketing API (Graph, `ads_read`), read-only. Performance
reports (`mk_meta_insights`), campaign objects (`mk_meta_objects`), event counters
(`mk_meta_events`) and custom conversions (`mk_meta_conversions`).

**Sign-in.** Access goes through the Meta connection at https://marketing-kit.app/connections: the user signs in and presses "Allow", no tokens to enter. The source is not authorised (`authorized: false`, error `source_not_authorized`, including after the sign-in was reset) — send the user there. Do not suggest issuing system-user tokens.

**Ad account.** The ad account is set by the `act_id` argument (`act_…`); the list of available ones — `mk_meta_accounts`.

**Attribution.** By default Meta counts installs/conversions with a window of 7 days
after the click and 1 day after the view. The `7d_view`/`28d_view` windows are removed
from the request by the server itself (Meta no longer returns them) — see
`action_attribution_windows.dropped` in the `mk_meta_insights` answer. To reconcile with
AppsFlyer use `action_attribution_windows: ["1d_click"]`.

**Data keeps arriving.** The numbers of the last 1–3 days still change — do not
treat them as final without warning the user.

**`mk_meta_events` — counters without a source.** The count of each event for the
period is there (`insights.actions`/`app_custom_event.*` + pixel stats), but where it
came from — the app's SDK, the Conversions API or a partner (AppsFlyer) — is not
available programmatically. The answer of this tool has no event-source field; look
for double counting with AppsFlyer by reconciling the numbers, do not rely on a
single number as the truth.

**iOS/SKAN.** Part of the iOS conversions arrives through SKAdNetwork with a delay
of up to several days and without a breakdown below the campaign level — a sharp drop
in the last days on iOS is not an anomaly by itself.

**Budgets in `mk_meta_objects`.** `daily_budget`/`lifetime_budget` are in minor
units of the ad account's currency (for example, cents for USD); the answer marks this
with `budget_unit: "minor"`.

More detail and ready-made checks for discrepancies — `references/meta.md`.

**Reference data.** `mk_meta_reference` returns the standard insights fields and breakdowns: call it before choosing `fields` or `breakdowns` of `mk_meta_insights` instead of guessing names.

Source reference: `references/meta.md`.

## Source: Facebook Pages (`mk_fb_pages_*`)

`mk_fb_pages_*` — Facebook Pages (Meta Graph API), read-only: the user's pages
(`mk_fb_pages_accounts`), posts (`mk_fb_pages_posts`), page insights
(`mk_fb_pages_page_insights`) and post insights (`mk_fb_pages_post_insights`). Sign-in is
the same Meta authorisation as for ads; it needs the permissions `pages_show_list`,
`pages_read_engagement`, `read_insights`, and on the page the user needs the "Analyze"
task. If the answer contains `reauthorize: true` — ask the user to re-authorise Meta at
marketing-kit.app/connections (tick all the boxes in the Facebook dialog).

**Sign-in.** Access goes through the same Meta connection at https://marketing-kit.app/connections as for ads. The source is not authorised (`source_not_authorized`) — send the user there. If the answer has `reauthorize: true` or `missing_scopes` (Meta was connected without the Pages permissions) — tell the user to press "Authorize" for Meta once more at https://marketing-kit.app/connections and tick all the boxes; the old ads connection keeps working.

**Order.** First `mk_fb_pages_accounts` — it has the page `id`; `page_id` is required in
all the other tools. Page tokens are not shown in the answers and are not needed.

**Reach and views.** `page_total_media_view_unique` is reach (unique
people), `page_media_view` is content views. Meta removed the old `page_impressions*`,
`post_impressions*`, `page_fans*`, `page_fan_adds/removes` —
do not request them (answer 100 "invalid metric"); the replacements are in the tools' input schemas.
Daily reach cannot be added up into reach for the period: the sum of daily values
overstates it, tell the user so.

**Followers.** `page_follows` is the number of followers at the end of the day (a level);
`totals` takes the last value, not the sum; the increase is
`page_daily_follows_unique`.

**Limits.** Insights exist only for pages with 100+ followers; a period
longer than 90 days is split into chunks by the server itself. Data keeps arriving — the
last 1–2 days are incomplete. If `mk_fb_pages_accounts` returned an empty list but the
user does have pages, they may have been granted through a Business portfolio — say
so and suggest checking the access.

**Reference data.** `mk_fb_pages_reference` returns live page and post metrics, periods and deprecated metrics with replacements: call it before choosing metrics, or when Meta calls a metric invalid instead of guessing names.

## Source: Instagram (`mk_instagram_*`)

`mk_instagram_*` — Instagram (Meta Graph API, sign-in through Facebook), read-only:
accounts (`mk_instagram_accounts`), account insights (`mk_instagram_account_insights`),
media (`mk_instagram_media`) and media insights (`mk_instagram_media_insights`). Only
professional accounts (Business/Creator) linked to a Facebook page. Sign-in is the same
Meta authorisation as for ads; it needs `instagram_basic`,
`instagram_manage_insights`, `pages_show_list`, `pages_read_engagement`.
If the answer contains `reauthorize: true` — ask the user to re-authorise Meta at
marketing-kit.app/connections (tick all the boxes in the Facebook dialog).

**Sign-in.** Access goes through the same Meta connection at https://marketing-kit.app/connections as for ads. The source is not authorised (`source_not_authorized`) — send the user there. If the answer has `reauthorize: true` or `missing_scopes` (Meta was connected without the Instagram permissions) — tell the user to press "Authorize" for Meta once more at https://marketing-kit.app/connections and tick all the boxes; the old ads connection keeps working.

**Order.** First `mk_instagram_accounts` — it has `ig_user_id`; it is required in
`mk_instagram_account_insights` and `mk_instagram_media`, and the `media_ids` for
`mk_instagram_media_insights` are taken from `mk_instagram_media`.

**Metrics.** Instagram removed `impressions` — use `views` (views)
and `reach` (reach, unique accounts). `profile_views` and `website_clicks`
are removed too (the replacement is `profile_links_taps`); for media `plays` and
`video_views` are removed. Reach cannot be added up across windows: the server splits the
period into windows of up to 30 days and sums `total_value`, so the sum of `reach` for a
period longer than 30 days is overstated — tell the user so. Daily series —
`time_series: true` (`reach`, `follower_count`).

**Delay.** Insights arrive with a delay of up to 48 hours; they are kept for up to 90
days (media — up to 2 years). Accounts with fewer than 100 followers get an
incomplete set of metrics; an empty answer is not zero.

**Media types.** Some metrics are not available for albums, stories and the like — such
media are listed in `errors` of the `mk_instagram_media_insights` answer, the rest are returned.
Stories live 24 hours and need at least 5 viewers.

**Reference data.** `mk_instagram_reference` returns live account and media metrics, breakdowns and deprecated metrics with replacements: call it before choosing metrics, or when Meta calls a metric invalid instead of guessing names.

## Source: TikTok Ads (`mk_tiktok_*`)

`mk_tiktok_*` — TikTok API for Business (v1.3), read-only: advertisers
(`mk_tiktok_accounts`), performance reports (`mk_tiktok_report`) and campaign objects
(`mk_tiktok_objects`). Organic TikTok (videos, followers) is not covered by this
source — it needs a separate authorisation of the TikTok account, which is a
later step.

**Sign-in.** The "Authorize" connection for TikTok at https://marketing-kit.app/connections: the user signs in to TikTok and grants access, no tokens to enter. The source is not authorised (`source_not_authorized`) — send the user there. The answer `source_not_configured` means the owner of the service has not set TikTok up yet — say so and do not try to work around it.

**Where to start.** `mk_tiktok_accounts` returns the advertisers that granted access:
`advertiser_id`, name, currency and time zone. `advertiser_id` is required
in `mk_tiktok_report` and `mk_tiktok_objects` — do not guess it, take it from `mk_tiktok_accounts`.

**Currency and time zone.** Spend is in the advertiser's currency, report dates are in
its time zone (both are in `mk_tiktok_accounts` and in the `mk_tiktok_report` answer),
not in the user's time zone. When reconciling with other sources (Meta, AppsFlyer) take
the difference in time zones and currencies into account.

**Attribution.** TikTok counts conversions (`conversion`, `cost_per_conversion`)
by the advertiser's own attribution windows (by default 7 days after the click and
1 day after the view, depending on the event settings) — when reconciling with
AppsFlyer expect a discrepancy.

**Data keeps arriving.** The numbers of the last 1–3 days still change; conversions
arrive with a delay — do not treat recent days as final.

**Long periods.** The source gives no more than 30 days per request: the server itself
splits the period into 30-day windows. For a period longer than 30 days without `daily: true`
the server requests days and sums them per object (spend, impressions, clicks,
conversions; CTR, CPC, CPM and cost per conversion are recalculated). Reach
(`reach`) and other non-additive metrics are not returned with such summing — see
the `dropped_metrics` field in the answer.

**Identifiers.** `campaign_id`, `adgroup_id`, `ad_id` are long numbers given as
strings: do not turn them into numbers. Budgets in `mk_tiktok_objects` are in the
advertiser's currency.

**Reference data.** `mk_tiktok_reference` returns report levels, dimensions and metrics: call it before choosing the level or metrics of `mk_tiktok_report` instead of guessing names.

## Source: Apple Ads (`mk_apple_ads_*`)

`mk_apple_ads_*` — Apple Ads (the App Store search ads) through the Apple Ads Platform API 1.0, read-only: ad accounts
(`mk_apple_ads_accounts`), campaigns (`mk_apple_ads_campaigns`), ad groups (`mk_apple_ads_adgroups`), keywords
(`mk_apple_ads_keywords`), negative keywords (`mk_apple_ads_negative_keywords`), ads (`mk_apple_ads_ads`), performance
reports (`mk_apple_ads_report`) and impression share (`mk_apple_ads_impression_share`). It never changes campaigns, bids,
budgets or keywords. Apple Maps campaigns (business brands) are not covered. Not to be confused with the public App Store
tools (`mk_apple_lookup`, `mk_apple_reviews`, `mk_apple_charts`): Apple Ads is the user's own ad account and takes `client`
like every other data tool.

**Sign-in.** The user presses "Connect Apple Ads" at https://marketing-kit.app/connections#apple-ads and signs in with an
Apple Account that is an Account Admin or Campaign Group Manager in Apple Ads, picks the ad accounts and read-only access;
no keys to make or enter. The source is not authorised (`source_not_authorized`, also after the grant was revoked) — send
the user there. `source_not_configured` means the owner of the service has not set Apple Ads up yet — say so and do not
try to work around it. A sign-in whose grant has no readable ad account is refused on the site (`apple_ads_no_accounts`):
the user signs in again with an account that has an ad account role. Disconnect on the site does not revoke the grant at
Apple: that is Apple Ads → Account Settings → API → Manage API Access.

**Where to start.** `mk_apple_ads_accounts` returns the ad accounts the grant covers: `account_id`, name, org, roles,
currency and time zone. `account_id` may be left out only when the grant covers a single ad account; with several, take
it from `mk_apple_ads_accounts` — never guess it. The objects go top-down: `mk_apple_ads_campaigns` gives `campaign_id`
(and the app — `promotedObjectId`), `mk_apple_ads_adgroups` with `campaign_id` gives `adgroup_id`;
`mk_apple_ads_keywords` and `mk_apple_ads_negative_keywords` need `campaign_id` or `adgroup_id`. Identifiers are long
numbers: pass them as they are listed.

**Reports.** `mk_apple_ads_report` with `level` campaigns (the default), adgroups, keywords, searchterms or ads; every
level except campaigns needs `campaign_id`. `granularity`: TOTAL (the default, one row per object for the period), DAILY
(90 days or less), WEEKLY (at least 14 days), MONTHLY (at least 90 days). `group_by` is one split, allowed per level:
countryOrRegion and deviceClass everywhere but ads (countryOrRegion only), also ageRange, gender, adminArea and locality
for campaigns and ad groups. `metrics` takes Apple's names (`localSpend`, `impressions`, `taps`, `ttr`, `cpt`,
`tapInstalls`, `viewInstalls`, `totalInstalls`, `totalAvgCPI` and the rest); without it — all. `grand_total` is the
total of the whole period.

**Currency and time zone.** Amounts (`localSpend`, `cpt`, `cpm`, CPI, budgets, bids) are in the ad account's currency
(`currency` in the answer and in `mk_apple_ads_accounts`). Report dates are in the account's reporting time zone
(`time_zone: ORTZ`, the default) or in UTC; search terms are ORTZ only, impression share is UTC only — say which. Never
add up numbers of different ad accounts: show each account on its own line; with different currencies there is no total
at all.

**Attribution — Apple's, not AppsFlyer's.** Installs in `mk_apple_ads_report` are Apple Ads attribution: after a tap
(`tapInstalls`) and after a view (`viewInstalls`; `totalInstalls` is both), new downloads and redownloads counted
separately. AppsFlyer (`mk_appsflyer_*`) counts the same campaigns by its own attribution rules and SDK; App Store
Connect (`mk_app_store_connect_*`) counts every download of the app in the store, with or without an ad. When the user
compares them, show both numbers next to each other, say whose number is whose and why they differ; never merge them and
never "fix" one with the other.

**Impression share.** `mk_apple_ads_impression_share` needs `app_id` — the App Store app id (Adam ID), the
`promotedObjectId` of the campaigns. Per search term and country it gives a range
`lowImpressionShare`…`highImpressionShare` (equal for 1–90%; 0.91…1 means over 90%), `rank` (1 — the highest share)
and `searchPopularity1to5`. DAILY — 30 days or less; WEEKLY — Sunday–Saturday weeks, 4 weeks or less, the period starts
on a Sunday. Terms with few impressions are hidden by Apple. Give the share as a range, not as one number.

**Data keeps arriving.** The last days may still change — do not treat today and yesterday as final.

**When it fails.** 401 — the grant was revoked or has expired and the connection was reset: the user presses "Connect
Apple Ads" again. 403 — the grant's role does not reach this account or object (the message names the roles): an
Account Admin checks the access in Apple Ads → Account Settings → API (Manage API Access). 429 — Apple's rate limit:
wait a minute, then ask for a narrower period or level. `invalid_args` about the granularity, `campaign_id` or
`group_by` — fix the arguments by the message, once.

**Recipes.**
- "Spend and installs by campaign last week" -> `mk_apple_ads_accounts` (several — ask which, or show each on its own
  line), then `mk_apple_ads_report` with `level: "campaigns"`, last week's dates and `granularity: "TOTAL"`; per campaign
  `localSpend`, `impressions`, `taps`, `tapInstalls` / `totalInstalls`, CPI (`totalAvgCPI`), then `grand_total` — in the
  account's currency and time zone, named.
- "Search terms with installs" -> `mk_apple_ads_campaigns` (take `campaign_id`), then `mk_apple_ads_report` with
  `level: "searchterms"`, `campaign_id` and the period; sort by installs, leave out the rows without installs, and say
  that Apple hides low-volume terms.
- "Impression share" -> `mk_apple_ads_campaigns` (the app id is `promotedObjectId`), then
  `mk_apple_ads_impression_share` with `app_id`, a period of 30 days or less and, if asked, `countries`; per term and
  country — the range and the rank.
- "Which keywords spend without installs?" -> `mk_apple_ads_report` with `level: "keywords"` and `campaign_id`;
  `mk_apple_ads_negative_keywords` for what is already excluded.
- "Do Apple Ads installs match AppsFlyer?" -> `mk_apple_ads_report` (campaigns, the period) and `mk_appsflyer_aggregate`
  for the same days; two columns with the reason they differ, never one merged number.

**Reference data.** `mk_apple_ads_reference` returns the report levels with their splits, the granularity limits, the
metrics and the roles: call it before choosing the level, split or metrics of `mk_apple_ads_report` instead of guessing
names.

## Source: Google Ads (`mk_google_ads_*`)

`mk_google_ads_*` — the Google Ads API (REST, GAQL) directly, without a client
library. Read-only: there are no tools that change anything.

**Sign-in.** Access goes through the Google connection at https://marketing-kit.app/connections: once, for GA4, Google Ads and Search Console at the same time. The source is not authorised (`authorized: false`, error `source_not_authorized`) — send the user there; there is no tool that connects it. Which accounts are visible (the property in GA4, the customer_id in Google Ads) is decided by the rights of the connected Google account in the service itself.

**Accounts.** `mk_google_ads_accounts` — all the accounts this Google account can see:
both those accessible directly and those under manager accounts (MCC) — with name, status,
path (`direct` / `via_manager` with the MCC's id and name) and the `deactivated` mark for
cancelled ones. The manager account is found automatically and is sent as
`login-customer-id` with every request — there is no need to ask the user to enter a
login customer ID. The map is cached for an hour; `refresh: true`
rebuilds it. A login customer ID set by hand (override) takes precedence over the automatic one — it is needed only when the account is visible
through several MCCs and a specific one is wanted. `USER_PERMISSION_DENIED` even with an MCC found
means this Google account cannot see the account: let the user check the access in Google Ads.

**Fields.** Do not guess GAQL field names: look names up with `mk_google_ads_reference` (live GAQL field metadata: `names` for exact names, `name_like` for a substring; it shows which fields can be selected, filtered, sorted and combined) and use only fields from it or the Google Ads API documentation; on an error about a wrong field fix the query by the `message` once, do not try names at random.

#### Tools with data

- `mk_google_ads_report` — any GAQL through `googleAds:search`. Required:
  `customer_id`, `query` (`SELECT ... FROM <resource> [WHERE ...] LIMIT n`) and
  the period. **`LIMIT` in the query text is required explicitly** — without it
  the query is rejected before it is sent to the source; heavy queries (`LIMIT`
  over 10 000, several `FROM`, text that changes data) are also
  rejected in advance, with an explanation (the server writes it in Russian). A filter on `segments.date`
  does not have to be written by hand — the period is put into the query automatically;
  if the query text already has it, it is used as it is. The answer adds to
  every `*_micros` field a neighbouring field without the suffix — already divided by
  1 000 000 (the account currency is the `currency` field in the answer; `customer.currency_code`
  is added to the query automatically if it has `metrics.cost_micros`).
- `mk_google_ads_objects` — ready-made reference lists: `campaigns`, `ad_groups`, `ads`,
  `conversion_actions`. `status_filter` is an optional `WHERE` condition
  (for example, `campaign.status = 'ENABLED'`).

#### Conversions and money

- Conversions are counted by the **click date**, not by the conversion date; the
  attribution window is set in the conversion action itself
  (`references/google_ads.md`).
- `cost_micros` and any other `*_micros` field are micro-units of the account
  currency; do not divide by hand, the tool already returns the ready value
  next to it.

#### Access level and limits

Explorer access (production accounts, no manual application) — 2 880 operations a
day per account; for occasional interactive queries this is almost always
enough. When the quota runs out the source answers 429 — the server itself
repeats the request with a delay; if the limit has not lifted — a clear error, not an
empty answer. Explorer does not allow creating accounts or managing
users/billing — this source (read-only) does not need that.

Source reference: `references/google_ads.md`.

## Source: Google Analytics 4 (`mk_ga4_*`)

`mk_ga4_*` — Google Analytics Data API v1beta (`mk_ga4_report`, `mk_ga4_realtime`) and Admin
API v1beta (`mk_ga4_accounts`, `mk_ga4_metadata`). Data is counted per property (`property_id`
— the numeric GA4 ID, not the Measurement ID `G-XXXX`): the list — `mk_ga4_accounts`.

**Sign-in.** Access goes through the Google connection at https://marketing-kit.app/connections: once, for GA4, Google Ads and Search Console at the same time. The source is not authorised (`authorized: false`, error `source_not_authorized`) — send the user there; there is no tool that connects it. Which accounts are visible (the property in GA4, the customer_id in Google Ads) is decided by the rights of the connected Google account in the service itself.

**Specifics:**

- **`mk_ga4_report` is a Core report, `mk_ga4_realtime` has its own (Realtime) quota.** Do not
  mix one up with the other when reading `property_quota` in the answer.
- **Custom fields** — `customEvent:<param>` (event-scoped) and
  `customUser:<param>` (user-scoped). A request with an unregistered
  name fails — first `mk_ga4_metadata`, do not
  guess names.
- **Pagination — only `mk_ga4_report`.** `limit` in the arguments is the wanted number
  of rows in total, not the size of one network request: above 10 000 the tool itself
  goes to the source page by page through `offset`, each time no more than 10 000 per
  call to the source. `pages_fetched` in the answer — how many requests were made.
- **Sampling and thresholds — in every `mk_ga4_report`/`mk_ga4_realtime` answer:**
  `subject_to_thresholding` (small sample, part of the data may not have passed the
  privacy threshold), `sampling_metadatas` (the report is built on a sample, not on
  all events), `data_loss_from_other_row` (part of the dimension combinations is
  rolled up into `(other)` because of cardinality). If any of them is `true`/non-empty —
  say so when answering the user's question, do not present the numbers as
  exact without a word.
- **Data keeps arriving for 24–48 hours** after the event — "yesterday" may
  change on a repeated request.

Source reference: `references/ga4.md`.

## Source: Google Search Console (`mk_search_console_*`)

`mk_search_console_*` — Google Search Console, organic Google search, read-only:
properties (`mk_search_console_sites`), the Search Analytics report (`mk_search_console_report`),
sitemap files (`mk_search_console_sitemaps`) and URL inspection in the index
(`mk_search_console_inspect`); the scope is `webmasters.readonly`.

**Sign-in.** Access goes through the same Google connection at https://marketing-kit.app/connections as for GA4 and Google Ads. The source is not authorised (`source_not_authorized`) — send the user there. If the answer has `reauthorize: true` or `missing_scopes` (Google was connected without the Search Console permission — the connection is old or the box was unticked) — tell the user to press "Authorize" for Google once more at https://marketing-kit.app/connections and keep the Search Console box ticked; GA4 and Google Ads keep working. The error `SERVICE_DISABLED` ("Search Console API is not enabled in the Google Cloud project") is a matter for the owner of the service, not the user: say so and do not suggest reconnecting.

**When to use it.** Questions about organic Google search: which queries find
the site, clicks and impressions in the results, CTR, average position, which pages
get traffic from search, search countries and devices, whether a page is indexed,
what is wrong with the sitemap. Do not confuse with GA4: GA4 is behaviour on the site and in
the app (sessions, events, conversions) from all channels; Search Console is what
happened **before the click** in Google's results. Paid search is Google Ads.

**Order.** First `mk_search_console_sites` — it has `site_url` (a URL prefix with a trailing slash
`https://example.com/` or a domain property `sc-domain:example.com`); pass
it as it is. Then `mk_search_console_report` with a period.

**Report.** `dimensions` — `date`, `query`, `page`, `country`, `device`
(`hour`, `searchAppearance` — special cases). Without dimensions — the total for the period.
`search_type` — `web` by default; `discover` and `googleNews` have no `query`.
`filters` — a list of AND conditions (`dimension`, `operator`, `expression`), countries —
alpha-3 in lower case (`svn`). Rows are sorted by clicks; `row_limit` is 1000 by
default. `ctr` is a fraction (0.034 = 3.4 %); do not add up or average the position
without weights — take `totals.position` (weighted by impressions).

**Delay and bounds.** Data arrives after 2–3 days, dates are in
Pacific time, retention is 16 months. If the user asks about
"yesterday" — warn that the data may not be there yet. The API gives no more than
50 000 rows a day, anonymised queries are not returned — the sum over
queries is less than the property total, this is not an error.

**Errors.** `SERVICE_DISABLED` ("Search Console API is not enabled in the
Google Cloud project") is a setting of the owner of the service, not of the user: say
so plainly; GA4 and Google Ads keep working. A 403 on a property means the account has no
access to this site in Search Console.

**Reference data.** `mk_search_console_reference` returns metrics, dimensions, search types, filter operators and data limits: call it before choosing dimensions, search type or filters instead of guessing names.

## Source: Google Play (`mk_google_play_*`)

`mk_google_play_*` — Google Play Console data of the user's own Android apps, read-only: apps
(`mk_google_play_apps`), installs (`mk_google_play_installs`), estimated sales (`mk_google_play_sales`),
earnings after Google's fee (`mk_google_play_earnings`), subscription counts (`mk_google_play_subscriptions`),
reviews (`mk_google_play_reviews`), refunds (`mk_google_play_refunds`) and Android vitals
(`mk_google_play_vitals`). It reads Play Console reports with the user's own Google sign-in and never writes anything;
replies to reviews are not possible.

**Sign-in.** Google Play has its own Google sign-in, separate from the one for GA4, Google Ads and Search Console: the user
presses "Connect Google Play" at https://marketing-kit.app/connections#google-play and grants read-only access. The source is
not authorised (`source_not_authorized`) — send the user there. If the answer has `reauthorize: true` or `missing_scopes` — tell
the user to press "Connect Google Play" once more and keep every box ticked. The reports bucket id is a second step on the
same card: nothing finds it automatically, the user pastes it (answer `google_play_bucket_missing`). Never ask for it in the chat as a
secret and never guess it.

**When to use it.** Questions about the Android side of the store: installs and uninstalls, how much was sold, what was
earned after Google's fee, how many subscribers there are, what reviews say, refunds and chargebacks, crash and ANR rates.
Do not confuse with the neighbours: AppsFlyer is attribution (which campaign brought the install), RevenueCat is subscription
billing across stores, `mk_app_store_connect_*` is the Apple side. Installs counted by Google Play are not the installs of
AppsFlyer or Firebase (different definitions, SDK versus store, time zones): show both numbers next to each other, say why they
differ, never merge them.

**Order.** First `mk_google_play_apps` (package names), then the operation. `package` can be left out only when the account has a
single app. Installs, sales, earnings, subscriptions and reviews with `month` read monthly files from the reports bucket: if the
answer is `google_play_bucket_missing`, tell the user to open Play Console > Download reports, press "Copy Cloud Storage URI"
and paste it into the Google Play card on the connections page.

**Delay.** Report files are monthly with daily rows and are posted 3 to 7 days late; the earnings file comes by the 5th of the next
month. If the user asks about "yesterday" or "today", say the data is not there yet. Dates in the files are UTC (sales), Pacific
(earnings, daily vitals); say which.

**Operations.**
- `mk_google_play_installs`: `dimension` is one of country (default), device, app_version, os_version, carrier, language;
  `daily_totals` say in `totals_source` which file they came from. `current_*` and `total_*` are stocks, never add them across days.
- `mk_google_play_sales`: what buyers paid in local currency before fees; not for accounting. Totals are per currency and per
  financial status. Never convert or add currencies, never net refunds against charges, never mix with App Store numbers silently.
- `mk_google_play_earnings`: money after Google's fee. Totals per merchant currency and transaction type.
- `mk_google_play_subscriptions`: counts only (new, canceled, active). `active` is a daily snapshot, never sum it across days.
  The revenue of subscriptions is in sales and earnings.
- `mk_google_play_reviews`: the Developer API returns only the last 7 days, text reviews only; use `next_page_token` to page.
  For an older month pass `month` (reads the bucket file).
- `mk_google_play_refunds`: voided purchases of the last 30 days. No amounts there: look the `order_id` up in sales or earnings.
- `mk_google_play_vitals`: crash and ANR rates, DAILY (Pacific days) or HOURLY (UTC). Show the values as returned; Google does
  not say whether they are fractions or percents, so do not turn them into percentages. `distinct_users` is never summed.

**When it fails.** A 403 means the Google account lacks a Play Console permission: say which one (the message names it) and that
the Play Console account owner grants it in Users and permissions. Reports: "View app information and download bulk reports";
sales and earnings: "View financial data"; reviews: "Reply to reviews"; vitals: "View app information (read-only)".
`SERVICE_DISABLED` is the service owner's setting, not the user's. A missing month file is usually just the delay.

**Recipes.**
- "How many installs last month, by country?" -> `mk_google_play_apps` (get the `package`), then `mk_google_play_installs` with
  `package`, `month: "2026-09"`, `dimension: "country"`; say the data lag.
- "How much did we sell and earn in September?" -> `mk_google_play_sales` and `mk_google_play_earnings` with `month: "2026-09"`;
  report each currency on its own line, estimated sales (what buyers paid) separately from earnings (after Google's fee).
- "What do users write this week?" -> `mk_google_play_reviews` (last 7 days); for an older month pass `month`.
- "Were there refunds lately?" -> `mk_google_play_refunds`; the amount of an `order_id` is in sales or earnings of its month.
- "Is the latest version crashing?" -> `mk_google_play_vitals` with `metric_set: "both"`, `dimensions: ["versionCode"]`.

**Reference data.** `mk_google_play_reference` returns report files and columns, install dimensions, vitals metrics and
dimensions, the required Play Console permissions and limits: call it before choosing a dimension or metric instead of guessing names.

## Source: AppsFlyer (`mk_appsflyer_*`)

- An install = the first launch of the app with the AppsFlyer SDK; users without
  the SDK are not visible in AppsFlyer at all.
- Installs from the web on iOS are not always linked to the click — part of them go to
  organic; on Android linking through the Install Referrer is almost complete.
- In-app events are attributed to the install source, not to the last click.
- The period (`period: {start, end}`) is required in `mk_appsflyer_aggregate` and `mk_appsflyer_raw`. The time
  zone is explicit: data in the chosen time zone is available only from the moment it was
  set up in AppsFlyer, before that the source gives UTC — the time zone actually
  applied comes back in the answer as `requested_timezone`.
- `app_id` is a required parameter of `mk_appsflyer_aggregate`/`mk_appsflyer_raw`, its own for each
  platform (the App Store id or the Android package). One AppsFlyer connection
  may cover several apps of the account — do not guess `app_id`,
  ask the user for it or call `mk_appsflyer_accounts`.

#### Tools

- `mk_appsflyer_aggregate` — the reports `daily_report`, `partners_report`,
  `partners_by_date_report`, `geo_report`, `geo_by_date_report`: installs
  and in-app events by media source/campaign/ad set/geo.
- `mk_appsflyer_raw` — installs and in-app events row by row (`installs_report`,
  `in_app_events_report`, `organic_installs_report`,
  `organic_in_app_events_report`). **Available only with the Raw Data module in the
  plan** — without it the source answers with an error, and the tool returns
  a clear error "no Raw Data module" (the server writes it in Russian), not an empty result.
  Personal data (device/advertising IDs, IP, `customer_user_id`) is never
  returned by this connector.
- `mk_appsflyer_purchase_dedup` — purchase duplicates between the app (SDK) and
  server-to-server events (RevenueCat → AppsFlyer) for a period of up to 31 days;
  counts only, no ids. Needs the Raw Data module. The recipe is below.

#### Purchase duplicates AppsFlyer ↔ RevenueCat

When the user asks "purchases are doubled", "AppsFlyer shows more revenue than
RevenueCat", "are purchases set up correctly", "should we install the Purchase
Connector":

1. `mk_appsflyer_purchase_dedup`, arguments: `app_id` (iOS and Android — one
   call for each), `period` (up to 31 days, by default the last 7–14
   full days), the user's time zone. If the RevenueCat integration uses its own event
   names — pass them in `event_names` (and in `first_purchase_events` for the
   first purchase and the trial start).
2. For the same days and in the same time zone — `mk_revenuecat_chart`: `trials_new`,
   `actives_new` (new paid) and `revenue` (transactions), `resolution: day`.
   Compare with the `by_day` of `mk_appsflyer_purchase_dedup`: the client-side first purchases (`sdk_first_purchase`)
   should be about "new trials + new paid without a trial"; roughly
   twice as many events as RevenueCat has is a sign of a duplicate. The sources count
   differently (attribution, time zone, sandbox, delay) — show both numbers.
3. The answer to the user:
   - **are there duplicates, how many, where from** — from `duplicates` and `signals`:
     `sdk_s2s` (one purchase came from the app and from RevenueCat; extra
     events `extra_events`, extra revenue `double_revenue_usd`), `sdk_sdk`
     (two client-side events: a manual `af_purchase` + `validateAndLog` or the
     Purchase Connector, or a restore), `s2s_s2s`. `allowed` is not a duplicate: it is
     a RevenueCat event with a different name and without revenue, as intended;
   - **the "one event — one source" scheme** (`recommended_scheme`):

     | Event | Who sends it to AppsFlyer | How |
     |---|---|---|
     | first purchase, trial start (the user is in the app) | the app (SDK) | `validateAndLogInAppPurchase` in place of the manual `af_purchase` call |
     | trial conversion, renewals | RevenueCat S2S | the RevenueCat → AppsFlyer integration |
     | cancellations, refunds | RevenueCat S2S | the integration, negative revenue |
     | initial purchase and trial started in the RevenueCat integration | nobody | an empty event name (not sent) or a custom name without revenue |

   - **what to change in the app's code:** replace the manual `af_purchase` with
     `validateAndLogInAppPurchase` **in the same place** — this replaces the event
     with a validated one, it is not a second source; do not add the Purchase Connector
     next to it (with `validateAndLog` that again gives two client-side events; AppsFlyer:
     "one integration per app"). The form with `AFSDKPurchaseDetails`
     (`productId`, `transactionId`, `purchaseType`) — from SDK 6.17.8; the old
     form with price and currency is deprecated;
   - **what to change in RevenueCat:** Integrations → AppsFlyer — for Initial
     Purchase and Trial Started clear the event name or give it a custom name without
     revenue; leave renewals, conversions, cancellations and refunds as they are.
4. Pitfalls (mention those that apply to the answer):
   - a client-side event moves the SKAdNetwork conversion value and quickly reaches
     partners for optimisation; S2S events get into SKAN only if
     "Record in-app events sent by server-to-server API" is turned on in SKAN Conversion
     Studio, and even then only when the app is opened within the
     measurement window;
   - RevenueCat's own guide advises removing **all** client-side revenue
     logging — the scheme above does not contradict this only if RevenueCat's
     first purchase is turned off or sent without revenue;
   - a trial start with the full price in `af_purchase` overstates revenue
     (`trial_logged_with_revenue`): a trial has revenue 0;
   - restore purchases must not call `validateAndLog` — otherwise it is a repeat
     (`validated_twice`);
   - TestFlight and the sandbox do not pass the production validation: for tests —
     `useReceiptValidationSandbox = true` only in the test build;
   - without a network the client-side event may not arrive — the first purchase is then
     visible only in RevenueCat;
   - no S2S events at all (`no_s2s_events`) — the RevenueCat integration is
     turned off or `$appsflyerId` is not set: there are no renewals in AppsFlyer.
5. Without the Raw Data module (the error "no Raw Data module") — only indirectly:
   `mk_appsflyer_aggregate` `daily_report` (`af_purchase` events) against RevenueCat's
   `revenue` transactions by day; say that SDK and S2S cannot be told apart without Raw Data.

V-Kit only reads and advises here: it changes nothing in AppsFlyer,
in RevenueCat or in the app's code.

#### Write: only a copy of a partner integration

The only write surface of this source, a separate tool `mk_appsflyer_integration_copy`, by
the owner's decision. V-Kit does not create, change or read OneLink links — say
that this is done in the AppsFlyer dashboard. The write tool has `dry_run: true` by default —
it shows the object/fields/before → after and changes nothing; the change is applied
only with an explicit `confirm: true` (before that ask the user to confirm with a phrase that
names the action and the object, not a bare "yes"; a consent does not carry over from a
previous call); after applying, the tool
reads the object again itself and returns the new state; before/after are written to the server's log.

- `mk_appsflyer_integration_copy` — copies a partner's `general_params`/`in_app_postbacks_params`
  (including the postback event mapping) from one app to
  another, one platform per call. This is **cloning a configuration already set up in the
  UI**, not setting up a partner from scratch — the endpoint cannot do that
  (a limitation of the API, not of V-Kit).

#### Only in the AppsFlyer interface (do not look for a workaround through the API)

The public AppsFlyer API does not allow changing the following programmatically — if the
user asks for it, say plainly that they need to go to the AppsFlyer
dashboard:

- switching in-app postbacks to Meta and setting up event mapping "from scratch"
  (without `mk_appsflyer_integration_copy`) — Settings → Integrated Partners;
- attribution and re-attribution windows (attribution window) — App Settings;
- OneLink templates (redirect/deep linking logic) — OneLink Management;
- general App Settings not listed above as available through the API.

#### Rate limit and repeated requests

The tool does not reliably know the exact official Pull API limit figures —
the confirmed source (`dev.appsflyer.com`) gave no figures, only a third-party one did. When the limit is exceeded
the source answers 429, the server itself repeats the request with a delay; if the limit
has not lifted — a clear error, not an empty answer. Do not split a wide request into
many small ones without need: one request for the whole period is faster and less likely
to hit the limit.

**Reference data.** `mk_appsflyer_reference` returns aggregate and raw report names, example raw columns and notes: call it before choosing the report of `mk_appsflyer_aggregate` or `mk_appsflyer_raw` instead of guessing names.

Source reference: `references/appsflyer.md`.

## Source: RevenueCat (`mk_revenuecat_*`)

`mk_revenuecat_*` — RevenueCat, in-app subscriptions, read-only (REST API v2):
key metrics (`mk_revenuecat_overview`), revenue for a period (`mk_revenuecat_revenue`), charts
(`mk_revenuecat_chart`, `mk_revenuecat_chart_options`), the project's reference data
(`mk_revenuecat_projects`, `mk_revenuecat_products`, `mk_revenuecat_entitlements`,
`mk_revenuecat_offerings`) and one customer by app user id (`mk_revenuecat_customer`).

**When to use it.** Questions about the app's money and subscriptions: MRR, ARR, active
subscriptions and trials, revenue (gross / proceeds), trial-to-paid conversion, churn,
refunds, LTV, cohorts, which product or offering sells, what is going on with
a specific user's subscription. Do not confuse with AppsFlyer: AppsFlyer is where the
**installs** and in-app events came from (attribution by media sources and
campaigns); RevenueCat is what users **bought and renewed** (with no breakdown by
ad campaigns). App Store (`mk_apple_*`) is only the public listing:
rating, reviews, chart positions; there are no sales there. If the user asks "how much did we earn from
the campaign" — RevenueCat gives the revenue, AppsFlyer the installs by campaign; say
that they can be linked only through attribution.

**Order.** `mk_revenuecat_overview` — no arguments (the key's project is picked automatically). For trends —
`mk_revenuecat_chart` with a period, `chart` = `mrr`, `revenue`, `actives`, `trials`, `trials_new`,
`churn`, `conversion_to_paying`, `trial_conversion`, `refund_rate`… (the list is in the input schema of `mk_revenuecat_chart`); the chart's segments and filters — first `mk_revenuecat_chart_options`. Points with
`incomplete: true` are an unfinished period, do not use them in the trend; do not add segments up.

**Customer.** `mk_revenuecat_customer` by `app_user_id` — subscriptions, status, renewal, revenue.
Personal data (attributes like `$email`, aliases, store transaction ids) is never
returned by this connector.

**Key.** No key (`revenuecat_key_missing`) or RevenueCat did not accept it
(401 `authentication_error`) — a **secret API key V2** with read-only
rights is needed: RevenueCat → Project settings → API keys → + New secret API key →
version V2, Charts & Metrics / Customer Information / Project Configuration — Read
→ Generate; save it at https://marketing-kit.app/connections#revenuecat. v1 keys and public SDK keys (`appl_…`,
`goog_…`) do not work. Step by step: https://marketing-kit.app/connections#revenuecat.
The server keeps the key encrypted. 403 `authorization_error` — the key has no right to this
section or belongs to another project. Metrics and charts — no more than 25 requests a
minute per key.

**Reference data.** `mk_revenuecat_reference` returns the list of charts with descriptions, resolutions, currencies, statuses and rate limits: call it before choosing a chart, resolution or currency instead of guessing names.

## Source: App Store Connect (`mk_app_store_connect_*`)

`mk_app_store_connect_*` — the App Store Connect API, Apple's official data on **your** apps
(the team key is saved on the site): sales and downloads (`mk_app_store_connect_sales`), subscription reports
and their events (`mk_app_store_connect_subscriptions`), the App Store funnel and traffic sources, sessions, deletions,
crashes (`mk_app_store_connect_analytics`), reviews with replies (`mk_app_store_connect_reviews`), versions and states (`mk_app_store_connect_versions`),
Product Page Optimization experiments and custom product pages (`mk_app_store_connect_experiments`), the list of
apps (`mk_app_store_connect_apps`). The only write is a separate tool, `mk_app_store_connect_analytics_enable`.

**When to use it.** The numbers are needed from App Store Connect itself: how many installs, re-downloads
and updates by country and device, proceeds and refunds, active subscriptions and
trials, cancellations and trial conversion by Apple's reports, impressions → product page views →
downloads, reviews and the replies to them, what is in the App Store now by version. Do not confuse:
`mk_apple_*` is public data of **any** app without a key (rating, current version,
charts); `mk_appsflyer_*` is attribution by media sources and campaigns; `mk_revenuecat_*` is
subscriptions across all stores, MRR and metrics almost in real time. App Store Connect is
the user's own apps, a D+1 delay (the report for a day is ready at about 8:00 Pacific time
the next day), no MRR and no breakdown by ad campaigns.

**Order.** First `mk_app_store_connect_apps` — take the app's Apple id (`app_id`). `mk_app_store_connect_sales`: `period`
up to 92 days (daily reports) or `frequency: MONTHLY`; `group_by` — date, country, device,
product, app, product_type (up to two). Money in the answer is per payout and customer currency,
**not converted**; refunds are negative units; `missing_dates` lists the days without a
report (yesterday's report may not exist before 8:00 PT — say so, do not treat it as an error).
`mk_app_store_connect_subscriptions`: `report: summary` — a snapshot of active subscriptions by day (the total is taken for
the last date, not summed), `report: events` — events (new, trials, trial
conversion, cancellations, refunds, reactivations). `mk_app_store_connect_analytics`: `report` funnel, sources, sessions,
installs, crashes or custom; data for the last 2–5 days may be missing (lag),
small apps hit privacy thresholds (from 5 users). There is no ready retention
report in the API — do not make one up. `mk_app_store_connect_experiments`: test results (conversion,
confidence) are not in the API — only the setup and the state.

**Turning analytics on.** If `mk_app_store_connect_analytics` answers `enabled: false`, offer
`mk_app_store_connect_analytics_enable`. This is a write to the account: first call it with `dry_run` (the default), show
the user the plan and ask them to confirm with a phrase that names the action and the app
("Enable Analytics Reports for MyApp"), not a bare "yes" (to a bare "yes" ask once for such a
phrase); only then repeat with `dry_run: false` and `confirm: true`. A key with the Admin role is needed; the data appears in 1–2 days. If the request already
exists, the tool says `already_enabled` and creates nothing. Replies to reviews are not
supported yet.

**Key.** No key (`app_store_connect_key_missing`) — the key is saved once at
https://marketing-kit.app/connections#app-store-connect: Issuer ID, Key ID and the `.p8` file
(App Store Connect → Users and Access → Integrations → Team Keys). A team
key is needed, an individual key does not read sales. `mk_app_store_connect_sales` and `mk_app_store_connect_subscriptions` also need the vendor number
(`app_store_connect_vendor_number_missing`): Payments and Financial Reports, top left.
Roles: `mk_app_store_connect_sales`, `mk_app_store_connect_subscriptions`, `mk_app_store_connect_analytics` — Admin, Sales and Reports or Finance;
`mk_app_store_connect_analytics_enable` — Admin only; `mk_app_store_connect_apps`, `mk_app_store_connect_reviews`, `mk_app_store_connect_versions`, `mk_app_store_connect_experiments` — Admin,
App Manager, Developer or Marketing. One key for everything — Admin. 401 — Apple did not accept the
key (check the Issuer ID, the Key ID, whether it was revoked); 403 — the role is not enough (the text names
the needed one); 429 — the limit is about 3500 requests an hour per key.

**Reference data.** `mk_app_store_connect_reference` returns Sales and Trends columns, product type identifiers, subscription and Analytics report names, latency and limits: call it when reading the output of sales, subscriptions or analytics instead of guessing names.

## Source: App Store (`mk_apple_*`)

`mk_apple_*` — the public App Store APIs (iTunes Lookup, Customer Reviews RSS, Marketing Tools Charts). No keys and no authorisation needed.

**Specifics:**

- **Rating** — per App Store country; there is no global one. In countries where the app is rarely installed (for example, RU), the rating may be 0 — this is not an error.
- **Reviews** — only the latest ones (usually 3–5), not the full history.
- **Top apps** — two types: `top-free` and `top-paid`; the genre filter uses the legacy RSS API (main genres: 6013 = Health & Fitness, 6023 = Food & Drink). The `find_id` parameter finds the position of a specific app in the chart (for example, where the app ranks).

## Large results as links

A table of more than 200 rows, more than 50 KB, or a request with `save: true` comes back as a summary (`columns`, `row_count`, `totals`, `preview` — the first 20 rows) and the links `download.csv` and `download.json` (valid 24 hours, only for the signed-in user). Tables that return rows accept `save`. If the user wants the links even for a short table, repeat the request with `save: true`.

## Writes (`mk_appsflyer_integration_copy`)

Everything except AppsFlyer is read-only, and reading AppsFlyer is `mk_appsflyer_aggregate`
and the other `mk_appsflyer_*` tools. The write is a separate tool, `mk_appsflyer_integration_copy`:

1. Call it first with `dry_run: true` (the default) and show the user what exactly would change: object, field, **before → after**.
2. Ask the user to confirm **this** change in words that name the action and the object (for example "Copy the partner integration settings from app A to app B"), not with a bare "yes"; to a bare "yes" ask once for such a phrase. Only after it apply the change: `dry_run: false` and `confirm: true`. One confirmation, one change; a past consent does not carry over. Never set `confirm: true` yourself.
3. After applying, read the object again and tell the user the new state. An answer with `dry_run: true, applied: false` to a request with `confirm: true` means the server applied nothing — do not present it as done. A call that did not reach the server (blocked by the client) — offer to tell the developer (see "Feedback to the developer").

## Writes: turning on Analytics Reports (`mk_app_store_connect_analytics_enable`)

The only write in App Store Connect creates an ONGOING Analytics Reports request, without which
`mk_app_store_connect_analytics` answers `enabled: false`. Work like this:

1. Call it first with `dry_run: true` (the default) and show the user the plan.
2. Ask for a confirmation in words that name the action and the app (for example "Enable Analytics Reports for MyApp"), not a bare "yes"; to a bare "yes" ask once for such a phrase. Only after it repeat with `dry_run: false` and `confirm: true`. Never set `confirm: true` yourself. A key with the Admin role is needed. If the client blocked the call, offer to tell the developer.
3. Say that data appears in 1–2 days. Never turn analytics on by yourself, "while at it".

Replies to reviews are not supported — reviews are read-only.

## Feedback to the developer (`mk_feedback_send`)

When and how is in the server's rules; in short, so as not to diverge from them:

- **Offer it yourself, without `feedback_invite`,** if: a V-Kit tool call did not reach the server or returned nothing (blocked by the client or its safety check, permission refused, timeout, dropped); the user says it does not work or does not succeed; the same goal is not reached after 2 attempts. Once per problem in a chat, one line after the answer, in the user's language; `kind: bug`, and in `context` the `tool` and what happened (for example `"error_message": "blocked by the client before reaching the server"`).
- The periodic question ("what is missing, what is wrong") is asked only on `feedback_invite`: the server keeps the frequency. When a tool result contains `feedback_invite`, finish your answer with its `ask` in the user's language, on its own line after the answer proper; do not add a second offer of your own.
- The user agrees or asks "pass this to the developer…" — draft a short note in the user's language: what they tried, what went wrong, their words; with `kind: error` add the `context` from the invitation. Show the text and call `mk_feedback_send` only after their "yes". Do not put data from their accounts (numbers, campaign names, rows) into the note unless they ask for it.
- Screenshot: if you have the image bytes, pass `screenshot` (`{ data: base64, mime }`, PNG, JPEG or WebP up to 5 MB); if not, send the text and give the `add_screenshot_url` from the answer ("you can attach the screenshot here", in the user's language).
- "Don't ask again" — `mk_feedback_mute` with `mute_days: 30`; confirm briefly and do not offer again in this chat.
- After sending, one line ("Sent — thanks!" in the user's language), then back to the task. `too_many_feedback` — not more than 20 notes a day: say so.

### The developer's reply and the history of notes

Every operation is its own tool: `mk_feedback_send` (a new note, everything above), `mk_feedback_mute` ("don't ask again"), `mk_feedback_reply`, `mk_feedback_list`, `mk_feedback_get`.

- **`feedback_reply` in a tool result** (any tool, `mk_status` too) — the developer answered the user's note. The server delivers it once, with the first result after the reply appeared, and marks it delivered at once — it will not come a second time. Fields: `feedback_id`, `sent_on` (date of the note), `your_note` (its beginning), `reply`, `reply_on` (date of the reply), `ask`. First answer the user's question, then add in the user's language: "By the way: the V-Kit developer replied on {reply_on} to your note from {sent_on} ("{your_note}"): {reply}. You can answer right here — tell me what to send."
- **The user answers the developer** — `mk_feedback_reply`, `reply_to` = `feedback_id` (or an `id` from `mk_feedback_list`), `text` — only the user's own words: their answer is the consent. Do not invent, complete or retell the answer for them; no account data. After sending, one line, then back to the task.
- **"What did I write?"** — `mk_feedback_list`; when a time is named — `since`/`until` (`YYYY-MM-DD`, `until` includes the whole day; "last week" — work the dates out and say them). The answer: `items` — `id`, `sent_on`, `kind`, `channel`, `excerpt`, `replies`, `last` (`author`, `on`), `status` (`needs_answer` | `answered` | `delivered`). Retell dates, kinds, the beginnings of the notes and whether the developer answered. Empty — say so, invent nothing.
- **"Show me that note"** — `mk_feedback_get`, `id` from `mk_feedback_list`: the whole note and the whole thread (`replies`: `author` `developer` | `user`, `text`, `on`). `mk_feedback_list` does not mark a reply as delivered; `mk_feedback_get` does — reading the thread is the delivery.

## What not to do

- Do not use other services or a browser for data that these sources have. While the V-Kit tools are not there, do not offer such services first — only the way to connect the connector (see above).
- This connector does not return raw personal data (device IDs, IP addresses, `customer_user_id`, a RevenueCat customer's `$email`).
- Do not put numbers of different sources into one sum: attribution, time zones and store-against-SDK differences make them count differently — show both and say why.
- Do not set a confirmation flag (`confirm: true`) on your own, and do not take a bare "yes" as the confirmation of a write.
