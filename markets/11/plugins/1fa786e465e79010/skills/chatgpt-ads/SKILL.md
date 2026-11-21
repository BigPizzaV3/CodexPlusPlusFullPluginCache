---
name: chatgpt-ads
description: ChatGPT Ads (OpenAI Ads) with Opus Growth - connecting an ad account with its API key, campaigns, ad groups, context hints, bids, chat card ads, spend limits, conversion pixels and events, insights and delivery diagnosis. Use for any ChatGPT Ads or OpenAI Ads question or change. Covers who sees ChatGPT ads, how matching works without keywords, and why an ad gets no impressions.
---

# ChatGPT Ads

Follow the `opus-growth` skill for preview, confirm, dates and budgets. Structure: campaign
(objective clicks, reach or conversions; daily or lifetime budget; locations; schedule) → ad
group (max bid, context hints) → ad (chat card: title, body, image, target URL). Budgets and bids
are in the account currency.

## Connecting

`connect_chatgpt_ads` takes the account's Ads API key from OpenAI Ads Manager > Settings > Ads API
key. Each key belongs to one ad account; connect one key per account. `manage_chatgpt_ads_accounts`
lists, checks or changes the default of connected accounts.

## How ChatGPT ads are matched and shown

- According to OpenAI's help center, ads appear for logged-in adult users on the Free and Go plans, in the countries OpenAI has
  opened (`chatgpt_ads_geo_lookup` shows where the account can advertise). Plus, Pro, Business,
  Enterprise and Edu users do not see ads; sensitive conversations (for example health and
  mental health) show none.
- Selection is a relevance-weighted auction: the most relevant ad wins, not simply the highest
  bid. Relevance comes from the context hints, the landing page, the ad's title and body, and the
  conversation.
- **Context hints are not keywords.** Write short, natural sentences about the product, use case
  or need ("Lightweight trail running shoes for rocky terrain"), not audiences ("California
  customers") and not single words ("Shoes"). A hint matches conversations in its own language:
  for several countries, write hints in each language buyers chat in. Up to 2000 per ad group.
- Hints are a list on the ad group. `update_chatgpt_ads_ad_group` adds, replaces, removes or
  clears them; to add one hint, use add mode rather than sending a shorter full list.
- Send clicks to the page that matches the hint, not the homepage; a generic destination loses
  relevance.

## Building

1. `create_chatgpt_ads_campaign` (paused unless `activate=true`; activating starts spending).
2. `create_chatgpt_ads_ad_group` with `max_bid` and context hints. A bid can never exceed the
   campaign's daily budget.
3. `create_chatgpt_ads_ad`: a chat card needs an image (`image_url`, uploaded for you). Creating
   an ad submits it for OpenAI review. `chatgpt_ads_ad_preview` shows the card.
4. Conversions objective: a pixel and a standard event must exist and fire
   (`chatgpt_ads_conversion_setup`, `create_chatgpt_ads_event_setting`); custom events can only be
   measured, not optimized for.
5. Activate with `chatgpt_ads_status` on request. Archiving cannot be undone through the API.

## No impressions?

Run `diagnose_chatgpt_ads_delivery` first. It follows OpenAI's troubleshooting order: account
(status, brand review, integrity review, account spend limit, prepaid balance), campaign
(status, schedule, budget left, locations, conversion events), ad group (bid vs budget type,
`bid_too_low`, hint count and language), ad (review status, landing page reachability and
redirects), then an hourly timeline that spots every campaign stopping at the same hour (an
account-level cause).
- OpenAI does not evaluate `bid_too_low` until 24 hours after an ad group edit. Do not raise
  bids again before then.
- Account spend limits: `chatgpt_ads_spend_limits` reads them, `manage_chatgpt_ads_spend_limit`
  changes them. Raising one commits real money: only on the user's explicit request.
- Health and clinic advertisers need manual approval from OpenAI and are limited to pilot
  countries; no bid, budget or hint change fixes that.

## What practitioners report (2026)

- Daily budgets pace more evenly than lifetime budgets.
- Delivery comes in pulses (a few active days, then quieter days); judge over at least a week.
- Long, wordy context hints have reduced delivery in tests; prefer many short, specific hints.
- Conversions are attributed through the `oppref` click parameter; the site must keep it
  (server-side) until the conversion, or sales show up as direct traffic.

## Changing budgets

A campaign has one budget type. Switching a lifetime-budget campaign to a daily budget cannot be
undone (a lifetime budget would need a new campaign); the preview says so. Insights:
`chatgpt_ads_insights`, details `chatgpt_ads_details`.

## Every operation

The complete list of this area's operations, what each is for and the tool that runs it: `references/operations.md`.
