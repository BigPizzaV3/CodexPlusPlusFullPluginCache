---
name: get-started
description: Set up Google Search Console by LT or work out why it returns no data. Use when the user has just added the app, asks what it can do, gets a "connect it at …" message, or cannot find one of their properties.
---

# Get started with Google Search Console by LT

The app reads the Search Console properties the user connected in Loopthink,
and only the ones their member group was granted. The tools are always the same:

- `connection_status`: whether Search Console is connected, and the link to connect it
- `gsc_list_sites`: the properties the user can query
- `gsc_search_analytics`: clicks, impressions, CTR and position for one property
- `gsc_sitemaps`: the submitted sitemaps of one property

## 1. Find out what is connected

Call `connection_status`.

- **`connected: true`.** Call `gsc_list_sites` and pass the `siteUrl` exactly
  as returned to the other tools.
- **`connected: false`.** Give the user the `connectUrl` and continue with step 2.

## 2. Connect Search Console

Send the user to the link. Do not try to do it for them: it needs a Google
sign-in in their browser.

1. Sign in to Loopthink and add Google Search Console.
2. Sign in with the Google account that has access to the properties.
3. Pick the properties the app may read.

Then ask the question again. The tools do not change, so nothing needs
refreshing or reconnecting in ChatGPT.

## 3. A property is missing

- It was not picked when Search Console was connected: an admin adds it on the
  server in the Loopthink web app.
- The person's member group was not granted it: an admin grants it.
- The Google account behind the connection cannot see it.

## Notes for answering

- `siteUrl` is either a URL prefix property (`https://www.example.com/`) or a
  domain property (`sc-domain:example.com`). Use it exactly as listed.
- Pick `dimensions` by question: `QUERY`, `PAGE`, `COUNTRY`, `DEVICE`, `DATE`.
- Search Console data lags two to three days behind.
- The app is read-only: it cannot submit sitemaps or request indexing.
