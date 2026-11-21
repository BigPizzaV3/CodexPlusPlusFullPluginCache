---
name: aso-atlas
description: App Store Optimization with ASO Atlas. Use for App Store and Google Play keyword research (popularity, difficulty, who ranks), tracking an app's keyword rankings per storefront, competitor keyword gaps, metadata (title, subtitle, keyword field) drafts, and questions like "how is my app doing" answered from App Store Connect data. Requires the ASO Atlas MCP server (asoatlas.com/mcp).
---

# ASO Atlas

ASO Atlas is an App Store Optimization tool for App Store and Google Play apps. Its MCP server exposes the user's own account: tracked apps, keywords per storefront with position, popularity and difficulty, competitors, keyword lists, a metadata optimizer and (when connected) private App Store Connect performance. `research_keywords`, `keyword_suggestions` and `app_ranking_keywords` also look up public App Store and Google Play data for any keyword or app.

## Start here

1. `list_tracked_apps` first. Every app-scoped tool takes the `app_id` it returns, not the App Store id.
2. `get_dashboard` for a one-screen status across apps; `get_app` for one app in depth (keywords, ranks, competitors, keyword gap).
3. `research_keywords` for terms the user is considering (up to 50 per call, one storefront). `keyword_suggestions` expands a seed term with autocomplete ideas. `app_ranking_keywords` reverse-looks-up what any App Store app (by `itunes_id`) ranks for.

## Reading the numbers

- **Popularity** is a 0-100 index of App Store search demand for a term in that storefront. 60+ is a head term, 20-40 is a realistic long-tail target, and the useful opportunities usually sit in the 30-55 band.
- `popularity_source` tells how the number was obtained: `asa`/`dictionary` is Apple-reported, `estimate` is a calibrated estimate that may be upgraded later, `below_floor` with a `null` popularity means demand exists but sits under the measurable threshold. Report that as "<10", never as missing data.
- **Difficulty** is 0-100, lower is easier. It weighs how many top results carry the term in their title and how strong those apps are.
- A keyword with `pending: true` has not been measured yet (research is queued). Say "not measured yet", then call again in a moment.
- Storefronts are two-letter country codes (`us`, `pl`, `de`...). The same term can be tracked in several markets.
- **Google Play** (`platform: "android"`, apps identified by package name in `store_id`): Google publishes no search volume, so Play keywords carry an estimated `demand` band (Very low to Very high) and `popularity` is always `null`. Present the band, never a number.

## Recommending keywords

Prefer terms with popularity in the 30-60 band and difficulty under ~40 that match what the app actually does. A term that equals a ranking app's name is brand navigation: real demand, but not targetable. Check the app's current metadata coverage with `get_app_optimizer` before proposing a subtitle or keyword field; it reports missing terms ranked by popularity and character budgets.

## Acting on the account

`track_app`, `add_keywords`, `add_competitor`, `create_keyword_list`, `add_keyword_to_list` and `save_metadata_draft` change the account but nothing on the App Store; a draft is only a draft. `refresh_app` queues a fresh rank check. `remove_*`, `untrack_app` and `change_app_market` delete history, and `save_metadata_draft` and `set_keyword_note` overwrite the previous draft or note: confirm with the user before calling them.

## Performance questions

If the user's App Store Connect account is connected, `get_app_performance` returns the acquisition funnel (impressions, page views, downloads, conversion), monetization, health and top territories with period-over-period deltas. Use `get_performance_series` to drill into one metric's daily history, optionally split by `source_type`, `territory`, `device` or `app_version`. Metadata-change impacts are correlational; say so.

## Connecting

If tools return 401, the connection needs signing in again: the client reopens the ASO Atlas consent screen (headless clients use a personal access token from Settings → Connect your AI on asoatlas.com instead). A 402 means the account has no active subscription: say so plainly and do not push an upgrade.
