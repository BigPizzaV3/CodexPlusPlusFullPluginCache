---
name: launch
description: Plan and build a new ad campaign with Opus Growth on Google Ads, Meta, TikTok, LinkedIn, Microsoft or ChatGPT Ads - choosing the platform and campaign type, budget, locations, landing page, tracking, structure, ads and extensions - created paused, read back and launched only on request. Use when the user wants to start advertising, create a campaign or copy a working setup to another platform.
---

# Launching a campaign

Follow the `opus-growth` skill and the platform skill (`google-ads`, `meta-ads`, `tiktok-ads`,
`linkedin-ads`, `microsoft-ads`, `chatgpt-ads`) for that platform's rules.

## 1. Ask only what is missing (one short message)

- What is advertised and the landing page URL (a specific page, not the homepage when a better
  page exists).
- The goal: sales, leads (form, call, WhatsApp/message), store visits, app installs, awareness.
- Where: countries, cities or a radius around the business.
- Daily budget in the account currency, and the language(s) of the customers.

Do not ask for anything you can read: connected accounts (`get_connection_status`), existing
campaigns (`account_snapshot`), conversion setup (`measurement` skill).

## 2. Pick the platform and type

- People already search for it → Google Ads Search (plus Microsoft for extra reach at lower CPCs).
- It sells on visuals or impulse, local services, events → Meta; younger audiences, video-native
  products → TikTok.
- B2B with a clear job title or industry and a high deal value → LinkedIn.
- People ask ChatGPT about this kind of product → ChatGPT Ads, in the countries where it runs.
- Budget too small to split: one platform, one campaign. A budget spread across many campaigns
  and ad sets never leaves learning.

## 3. Check before building

- **Tracking**: the conversion the campaign will optimize for must exist and fire. Without it,
  start with clicks or landing page views and set tracking up in parallel (`measurement` skill).
- **Landing page** loads, matches the ad and works on mobile.
- **Account health**: billing set up, no account-level spending limit already reached, platform
  verification done (Meta, TikTok business verification).

## 4. Build, paused

Create campaign → ad group or ad set → ads, each with a preview the user approves. Write ad copy
in the customers' language, with the offer, a reason to choose this business and a clear action.
For Google Search add extensions; for Meta and TikTok prepare 2-3 creatives, not one.
Everything is created paused (LinkedIn as draft).

## 5. Read back, then launch on request

Read the new objects back (targeting, budget, status, ad review status). Give the user a short
summary: what was built, the daily budget, where it shows, what it optimizes for, and that it is
paused. Enable only when they say so, with the platform's status tool.

## 6. After launch

Tell the user when to look again: after about 3 days check delivery and disapprovals, after 7-14
days judge results. Changes in the first week restart learning.

## Copying a setup to another platform

Read the source campaign fully first (targeting, budget, ads, extensions). Translate concepts,
not fields: Google keywords become Microsoft keywords directly, but become Meta or TikTok interests
and audiences only loosely. Say what could not be carried over.
