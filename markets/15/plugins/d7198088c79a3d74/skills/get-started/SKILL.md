---
name: get-started
description: Set up loopthink for Google Search Console and Google Ads, or work out why it returns no data. Use when the user has just added loopthink, asks what it can do, gets a "connect it at …" message, or cannot find one of their properties or accounts.
---

# Get started with loopthink

loopthink reads Google Search Console and Google Ads through the properties and
accounts a workspace has connected, and only the ones the signed-in person's
member group was granted. The tools are always the same:

- `loopthink_status`: what is connected, and the link to connect the rest (optional `goal`: the user's request)
- `gsc_list_sites`, `gsc_search_analytics`, `gsc_sitemaps`
- `google_ads_list_accounts`, `google_ads_report`

## 1. Find out what is connected

Call `loopthink_status` and pass the user's request in one sentence as `goal`
(optional, but it tells loopthink which data source the user needs).

- **A source shows `connected: true`.** Use its list tool (`gsc_list_sites` or
  `google_ads_list_accounts`) and pass the `siteUrl` or `customerId` exactly as
  returned to the report tools.
- **A source shows `connected: false`.** Give the user its `connectUrl` and
  continue with step 2.

## 2. Connect a source

Send the user to the link. Do not try to do it for them: it needs a Google
sign-in in their browser.

1. Sign in to loopthink and add Google Search Console or Google Ads.
2. Sign in with the Google account that has access to the properties or accounts.
3. Pick the ones the team may use.

Then ask the question again. The tools do not change, so nothing needs
refreshing in ChatGPT.

## 3. A property or account is missing

- It was not picked when the source was connected: an admin adds it on the
  server in the loopthink web app.
- The person's member group was not granted it: an admin grants it.
- The Google account behind the connection cannot see it.

## Notes for answering

- Search Console query data (the `QUERY` dimension) is only available when the
  workspace enabled it on the connection. Without it, group by page, country,
  device or date.
- Search Console data lags by about two days. For the most recent days pass
  `dataState: "all"` and say that those numbers can still change.
- Google Ads cost comes as `cost_micros`: divide by 1,000,000 for the account's
  currency.
- Everything is read-only. loopthink cannot change campaigns, budgets or
  keywords, submit sitemaps or add properties.
