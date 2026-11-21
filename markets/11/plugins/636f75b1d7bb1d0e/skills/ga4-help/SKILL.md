---
name: ga4-help
description: Explain what this Windsor.ai app for Google Analytics 4 covers (read-only website and app analytics for the user's own GA4 properties), what it does not (advertising cost or ROAS, property settings, other analytics platforms), and which skill handles a request. Use when the user asks what the app can do or asks for something outside its scope.
---

# What this app can do

This app reads report data for the user's own connected Google Analytics 4 properties through Windsor.ai (connector id `googleanalytics4`): sessions, users, new users, engagement rate, bounce rate, pageviews, average session duration, event count, conversions (key events), and revenue, broken down by date, default channel group, source and medium, campaign, landing page, device category, or country. It is read-only. It does not change property settings or create key events, has no advertising cost or ROAS data (that lives in the ad-platform listings such as Windsor.ai Google Ads), and does not read other analytics platforms.

## Route the request
- Reports, rankings, comparisons, trends -> $ga4-insights
- Connecting, reconnecting, adding a property, or asking what is connected -> $ga4-connect
- Recurring exports and syncs -> $ga4-export
- What the app covers and does not -> $ga4-help

## Answering "what can you do"
- Call get_connectors with include_not_yet_connected=True and answer from it: which properties are connected and which options exist. Do not list capabilities the tool result does not show.
- Reads are available on the free plan.

## Out of scope
- Data from other platforms: name the Windsor.ai listing that covers them instead of attempting the read.
- Generating content, general marketing advice unrelated to the connected properties, or anything about plans and pricing.
