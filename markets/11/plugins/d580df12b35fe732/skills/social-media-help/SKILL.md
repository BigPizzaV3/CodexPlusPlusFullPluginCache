---
name: social-media-help
description: Explain what Windsor.ai for Social Media covers (Instagram, Facebook Pages, TikTok, YouTube, LinkedIn Pages, Threads, and Google Business Profile), what it does not, and which skill handles a request. Use when the user asks what the app can do or asks for something outside its scope.
---

# What Windsor.ai for Social Media can do

This app covers analyzing organic social performance on the seven social sources above and, after confirmation, publishing posts, replying to comments and reviews, and updating videos and listings. TikTok is read-only. Sources on this app: Instagram, Facebook Pages, TikTok, YouTube, LinkedIn Pages, Threads, and Google Business Profile
(connector ids instagram, facebook_organic, tiktok_organic, youtube, linkedin_organic, threads, google_my_business). It does not cover paid ads, web analytics, CRM, e-commerce, or finance data (each has its own Windsor.ai listing).

## Route the request
- Reports, rankings, comparisons, trends -> $social-media-insights
- Creating or publishing something new (confirmed) -> $social-media-create
- Connecting, reconnecting, adding an account -> $social-media-connect
- Recurring exports and syncs -> $social-media-export

## Answering "what can you do"
- Call get_connectors with include_not_yet_connected=True and answer from it: which of the seven sources are connected, which are available to connect, and (per connector) which write actions and options exist. Do not list capabilities the tool result does not show.
- Reads are available on the free plan; write actions need an account with permission and write actions enabled at https://onboard.windsor.ai/app/settings/account.

## Out of scope
- Data from sources outside this app: name the Windsor.ai listing that covers them instead of attempting the read.
- Generating creative assets, general advice unrelated to connected accounts, or anything about plans and pricing.
