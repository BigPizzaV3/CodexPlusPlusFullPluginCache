---
name: run-meta-ads
description: Launch and run a Facebook and Instagram ad campaign on the user's own Meta ad account. Use when the user asks to put an ad on Facebook or Instagram, boost a post, launch, pause or turn on a Meta campaign, check what an audience would reach, or see how their Meta ads are doing.
---

# Run my Meta ads

Use this skill to build a Meta campaign from the user's own creative, show it before any money moves, and read
back how it is doing. Every campaign is created paused and spends nothing until the user turns it on.
Explicit instructions from the user always take priority over this skill, including the account, objective,
budget, audience, dates and wording they name.

## Before you start
1. Call `list_meta_pages`. It lists the connected Facebook Pages, linked Instagram accounts and ad accounts. If Meta
   is not connected, say so and that it is connected in the Hermoso app under Connectors, in the sidebar.
   Never ask for a password or token in the chat.
2. If there are several ad accounts or Pages, ask which to use.

## Launch a campaign
1. Work out the creative: a file made in this conversation, one from `list_library`, or the user's own file made
   into a link with `upload_file`. To promote a post that is already published, use its id as `boostPostId`.
2. Agree the objective, the daily budget in the ad account's own currency, the country or cities, and the age range
   and interests if the user has them. Ask for any of these the user did not give; do not pick a budget for them.
3. Call `estimate_meta_reach` with that targeting. It is free and creates nothing. Tell the user the reach range,
   and say plainly if Meta warns the audience is too narrow.
4. Call `create_meta_ad` with the creative, copy, targeting and budget. It builds the campaign, ad set and ad, all
   paused, and reads them back from Meta. Show the summary it returns and its preview links. `preview_meta_ad`
   shows any other placement the user asks about.
5. Turning it on starts real ad spend. Show the campaign name and its daily budget, ask for an explicit yes, then
   call `set_meta_campaign_status` with `status` set to ACTIVE and `confirm` set to true. Pausing needs no confirm.
6. Report the status from what the tool read back.

## How it is doing
Call `meta_insights` with the ad account, and the campaign as `objectId` when the user names one. Pass
`breakdowns` when they ask who it worked on or where (age and gender, placement, country). Quote only numbers the
tool returned; a metric Meta did not report is missing, not zero. A campaign with little delivery so far is "not
enough data yet".

## Credits and spend
Building and managing campaigns uses no Hermoso credits. The ad spend is billed by Meta to the user's own ad
account.

## Do not
- Do not turn a campaign on, or raise a budget, without the user's explicit yes to the exact name and amount.
- Do not say a campaign, ad set or ad exists, or what its status is, unless a tool read it back.
- Do not choose a special ad category, audience or budget the user did not agree to.
