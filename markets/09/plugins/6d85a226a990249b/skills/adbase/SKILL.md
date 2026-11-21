---
name: adbase
description: Research competitors' ads with AdBase. Use when the user asks what ads competitors are running on Facebook, Instagram or Google, wants ad inspiration or a swipe file, wants a video ad's hook and script broken down, or wants to compare competitor landing pages, offers or email newsletters. Requires a connected AdBase workspace.
---

# Competitor ad research with AdBase

## Start

1. Call `list_library_watchlist` to see which brands the workspace tracks. If the user has
   several workspaces, `get_account` lists them; pass the chosen one as `organization_id`.
2. If the brand the user asks about isn't tracked, ask for its website, Facebook page,
   Instagram profile or Google Ads advertiser URL and call `watch_library_advertiser`.
   Collecting its first ads takes a few minutes; check back with `list_library_watchlist`.

## Find ads

- `search_library_ads` filters by brand, platform (Meta, Google), status, format, keyword and
  tags: `creative_style`, `angle`, `offer_type`, `industry`. Sort `oldest` surfaces the
  longest-running ads, which advertisers usually keep because they perform.
- `list_library_activity` answers "what changed": new ads, stopped ads, new landing pages.
- Open only the ads worth a closer look with `get_library_ad`. It returns the full copy, the
  video breakdown (hook, spoken transcript, visual transcript with on-screen text, contact
  sheets) and ad library details for Meta ads (EU reach, targeting). A refresh can use one of
  the workspace's daily lookups.

## Landing pages and emails

- `get_library_advertiser` lists a brand's landing pages and newest emails.
- `get_library_landing_page` returns the page text and screenshots: offers, pricing, claims,
  structure.
- `list_library_emails` and `get_library_email` cover newsletters: cadence, offers, subject lines.

## Show the results

Do the analysis with the data tools first. Then show the few items that support the answer with
`show_library_ads`, `show_library_landing_pages` or `show_library_emails`, passing their ids.

## Useful outputs

Summaries of what competitors are testing, patterns across hooks, angles and offers, creative
briefs, and new hook or script ideas grounded in the ads you read. Quote the ads you base a
claim on.
