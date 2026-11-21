---
name: find-app-ads
description: Find real video ads that mobile apps ran on Facebook and Instagram and explain why they work, from Clonerrr's ad library. Use when the user asks for app ad examples or inspiration, what an app or a category advertises with, which hooks or ad formats last, or a breakdown of one app ad.
---

# Find app ads that kept running

Clonerrr's library holds real video ads from mobile apps, taken from Meta's Ad Library. Each has the number of days it ran, why it works, and its scenes in order. An advertiser stops paying for an ad that does not work, so days running is the signal to rank by.

What the user asks for comes first. If they want a different format, fewer ads or no links, do that.

## Steps

1. Call `search_ad_templates` with short keywords, not a sentence: an app's name (`coinsnap`), a category (`category: "Health & Fitness"`) or one plain word for the kind of ad (`testimonial`, `demo`). With nothing to go on, call it with no query: it lists the longest-running ads and every category the library has.
2. Show up to five ads. For each: the app, how long it ran, the opening line in quotes, the scene structure (Hook → Demo → CTA) and its `url` as a link. Say "run not recorded" when `days_running` is absent.
3. When the user picks an ad, or asks why one works, call `get_ad_template` with its `id`. Explain it scene by scene: what the scene is for, the words on screen and spoken, how it is shot. Then say which parts belong to that app (`specific_to_this_app`) and which any product could reuse (`carries_over`).
4. When several ads are on the table, say what the long-running ones have in common. That pattern is usually what the user came for.

The video itself plays on the ad's page, so link to it rather than describing it as attached.

## What not to infer

- Days running is the only performance figure. Never state or estimate spend, installs, click rates or revenue.
- The library is a sample. An app with no ads in it may still advertise: say the library has none of its ads, not that it runs none.
- Take lines, timings and structure from the tool results only. If a field is absent, say it was not recorded.
- The ads belong to the apps that ran them. Describe and learn from them; do not present one as the user's own or as endorsed by that app.

## When nothing matches

Say the library has no ads for that search, name the categories it does have (they come back with every result), and offer the closest ones. If the user wants ads built for their own app, use the write-app-ad workflow.
