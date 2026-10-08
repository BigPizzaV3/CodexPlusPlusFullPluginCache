---
name: magister-paid-ads
description: Review paid advertising performance and create new campaigns safely through Magister — Google Ads, Meta Ads, and TikTok Ads reporting, plus creating Meta or TikTok campaigns that are always paused. Use when the user asks how their ads are performing, what campaigns are running, wants to create or launch a campaign, or wants to stop ad spend.
---

# Paid advertising through Magister

This connector can **read** advertising performance across the user's connected
platforms and **create new Meta or TikTok campaigns in a paused state**. It
cannot start ad spend. Be precise about that boundary — it is the single most
important thing to get right here, because the user's money is involved.

Resolve `project_id` from `list_projects` first; never guess one.

## Reading performance

- `list_social_accounts` — which advertising and social accounts are connected.
- `list_ad_campaigns` — campaigns on those accounts.
- `get_ad_analytics` — performance metrics for one advertisement.

These read from the connected ad platforms and change nothing.

## Creating a campaign

`create_ad_campaign` supports **Meta and TikTok only**, and every campaign it
creates is **paused at creation** and verified paused before the call returns.

Two things to handle before calling it:

1. **A connected account can front more than one ad account.** When it does, the
   tool asks which one to bill. That is expected behavior, not an error — put
   the choice to the user rather than picking one. Billing the wrong ad account
   is a real financial mistake.
2. **Confirm the budget with the user** in the same message you confirm the
   platform and the audience.

If the user asks for LinkedIn, X, Pinterest, Google, or any other platform, say
directly that campaign creation supports only Meta and TikTok here, and that
reporting is still available for their other connected platforms. Do not
substitute a different platform to satisfy the request.

## This connector cannot launch a campaign

There is **no activation tool**. A campaign created here stays paused until a
person activates it in the Magister app or in the ad platform itself.

Say so plainly when you create one. Never imply the campaign is live, never
promise it will start on its own, and never describe a paused campaign as
"launched" or "running."

## Stopping spend

`pause_ad_campaign` stops further spend on a running campaign. It is reversible
by activating the campaign again in the ad platform, so it is safe to use when
the user asks to stop something. If a user is worried about spend, pausing is
the correct immediate action.

## Do not infer

- Never state spend, impressions, conversions, or ROAS the tools did not return.
- Never estimate what a campaign "should" cost or perform and present it as
  measured data.
- Never claim a campaign is active. Nothing on this surface can make it active.
