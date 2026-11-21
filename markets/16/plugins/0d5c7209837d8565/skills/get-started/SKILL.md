---
name: get-started
description: Set up Google Analytics by Loopthink or work out why it returns no data. Use when the user has just added the app, asks what it can do, gets a "connect it at …" message, or cannot find one of their GA4 properties.
---

# Get started with Google Analytics by Loopthink

The app reads the GA4 properties the user connected in Loopthink, and only the
ones their member group was granted. The tools are always the same:

- `connection_status`: whether Google Analytics is connected, and the link to connect it
- `ga4_list_properties`: the properties the user can query
- `ga4_report`: a report on one property
- `ga4_realtime_report`: what is happening on one property right now
- `ga4_metadata`: the dimensions and metrics one property offers

## 1. Find out what is connected

Call `connection_status`.

- **`connected: true`.** Call `ga4_list_properties` and pass the `propertyId`
  exactly as returned to the other tools.
- **`connected: false`.** Give the user the `connectUrl` and continue with step 2.

## 2. Connect Google Analytics

Send the user to the link. Do not try to do it for them: it needs a Google
sign-in in their browser.

1. Sign in to Loopthink and add Google Analytics.
2. Sign in with the Google account that has access to the GA4 properties.
3. Pick the properties the app may read.

Then ask the question again. The tools do not change, so nothing needs
refreshing or reconnecting in ChatGPT.

## 3. A property is missing

- It was not picked when Google Analytics was connected: an admin adds it on
  the server in the Loopthink web app.
- The person's member group was not granted it: an admin grants it.
- The Google account behind the connection cannot see it. Universal Analytics
  properties are not supported, only GA4.

## Notes for answering

- Use GA4 API names: metrics such as `sessions`, `totalUsers`, `conversions`,
  dimensions such as `date`, `landingPage`, `sessionDefaultChannelGroup`.
  When unsure whether a name exists, call `ga4_metadata` first.
- The app is read-only: it cannot change events, conversions or settings.
