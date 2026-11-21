---
name: run-tiktok-ads
description: Launch and run a TikTok ad campaign on the user's own TikTok Ads account. Use when the user asks to advertise on TikTok, turn a video into a TikTok ad, launch, pause or turn on a TikTok campaign, or see how their TikTok ads are doing.
---

# Run my TikTok ads

Use this skill to build a TikTok campaign from the user's own video, show it before any money moves, and read back
how it is doing. Everything is created paused and spends nothing until the user turns it on. Explicit instructions from
the user always take priority over this skill, including the account, objective, budget, audience and wording
they name.

## Before you start
1. Call `list_tiktok_ads_accounts`. TikTok Ads is a separate connection from posting to TikTok; if it is not
   connected, say so and that it is connected in the Hermoso app under Connectors, in the sidebar. Never ask for a
   password or token in the chat. If there are several advertiser accounts, ask which to use.
2. Call `list_tiktok_ads_identities`. The ad appears publicly as one of these TikTok accounts, so show the list and
   let the user choose. If it is empty, no TikTok account is set up on that advertiser yet; say so.

## Launch a campaign
1. Work out the video: one made in this conversation, one from `list_library`, or the user's own file made into a
   link with `upload_file`. Call `upload_tiktok_ads_creative` with its link. If it says the video is not usable in
   ads, say why (usually it is too small) and offer to make a larger version. Keep the video id and cover image id.
2. Agree the objective, the daily budget in the ad account's own currency, the countries and the age range. Ask
   for anything missing; do not pick a budget for the user.
3. Call `create_tiktok_ads_campaign` with the objective, then `create_tiktok_ads_ad_group` with the budget,
   locations and targeting, then `create_tiktok_ads_ad` with the video id, the cover image id in `imageIds`, the
   chosen identity, the ad text and the landing page. All three are created paused and read back.
4. Turning it on starts real ad spend. Show the campaign name and daily budget and ask for an explicit yes. Then
   call `set_tiktok_ads_status` with `confirm` set to true for the campaign, the ad group and the ad: each level is
   paused until it is turned on. TikTok reviews a new ad before it shows.

## How it is doing
Call `tiktok_ads_report`. For who saw it, use the audience report with age, gender or country. Quote only numbers
the tool returned; a report with no rows means nothing has delivered yet.

## Credits and spend
Building and managing campaigns uses no Hermoso credits. The ad spend is billed by TikTok to the user's own account.

## Do not
- Do not turn anything on, or raise a budget, without the user's explicit yes to the exact name and amount.
- Do not choose the identity, budget or audience for the user.
- Do not say a campaign exists, or what its status is, unless a tool read it back.
