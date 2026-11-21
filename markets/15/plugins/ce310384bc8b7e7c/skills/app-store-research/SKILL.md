---
name: app-store-research
description: Answer questions about how App Store apps are doing, such as revenue, downloads, growth, ratings and category leaders, with AppMoney's tools, and manage the user's AppMoney watchlist. Use when someone asks what an iPhone app earns, which apps lead a category, which are growing, or wants to track apps.
---

# App Store research with AppMoney

## Finding apps

- `search_apps` finds apps by name or publisher (`query`), by category id, and by ranges of revenue, downloads, growth, rating and reviews. It sorts by revenue, downloads, growth, rating, reviews or release date. Keep lists short (5 to 10) unless the user asks for more.
- For "how much does X make", search by name, pick the result whose name matches the app the user means, and call `get_app` with its id for the full profile.
- Category ids, with their names, are in the `category` parameter's description. Game subgenres have their own ids; pass every game id to cover all games.

## Reading the figures

- Every revenue and download figure is a modelled monthly estimate from licensed market data, not developer-reported financials. Say "estimated" when you quote one, and never present it as financial advice.
- A floored value such as "< $5k" or "< 5k" means the app is below what the data can measure. It is not zero, so never sum or average floored values.
- Growth compares the latest two months only. A null growth figure means there was nothing comparable, not 0%.
- Apps removed from the App Store are left out unless `availability` includes `removed`, and their figures stop at the last month measured.
- AppMoney covers Apple's App Store only. If asked about Google Play or another store, say so rather than substituting App Store figures.

## The watchlist

- `list_watchlist` shows the tracked apps and their folders. `add_to_watchlist` tracks an app and can file it in a folder; naming a new folder creates it.
- `remove_from_watchlist`, `rename_watchlist_folder` and `delete_watchlist_folder` change the list. Confirm with the user before removing an app or deleting a folder, unless they asked for exactly that.
- AppMoney cannot delete accounts, make purchases or contact developers. For account requests, point the user to appmoney.ai/support.
