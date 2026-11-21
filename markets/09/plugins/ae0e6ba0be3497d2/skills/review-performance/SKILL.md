---
name: review-performance
description: Review how the user's marketing is performing and manage their paid campaigns. Use when the user asks which posts, hooks or formats work best on a channel, how their organic social is doing, how their paid campaigns are doing and what to scale, pause, fix or test next, or asks to pause, resume or change the budget of a campaign on their own ad account. Launching a campaign on Meta, Google or TikTok has its own skill.
---

# Review performance

Use this skill to answer "what is working?" with the user's own numbers. It reads and recommends; it changes
nothing. Explicit instructions from the user always take priority over this skill, including the date range,
channels, platforms and goal they name.

## Organic posts
Call `post_performance` for the brand. By default it groups results by hook; pass a different grouping when the
user asks about subjects, formats, channels or posting hours, and pass `days` or `channel` when they name them.
- Compare posts only within one channel. A LinkedIn impression and a TikTok view are different units; never add
  them up or rank across channels.
- Describe a post by what it showed (the creative and its format), not by its caption.
- If the tool holds back a verdict because a group has too few posts or readings, say so and say what would make
  it readable. Do not fill the gap with a guess.

## Paid campaigns
Call `analyze_campaigns`, with `days` (14 is a good default) and the user's `goal` if they gave one (for example
lowest cost per acquisition). It reads every ad account connected to the workspace and returns one table plus four
lists: scale, pause, fix and test next, and a list of rows with too little data.
- Present each recommendation with the row's own numbers as evidence, the reason, and the concrete next move with
  the number in it ("raise the daily budget from 25 to 40 and re-read cost per acquisition in 3 days").
- Rows with too little delivery are "not enough data yet", never "pause it".
- A platform that could not be read is named as unreadable. Its numbers are missing, not zero.
- A metric a platform does not report is unmeasured. Never show it as 0.
- Each platform defines a conversion its own way. Say so when you compare cost per acquisition across platforms.

## Applying a recommendation
The review itself changes nothing in the ad accounts and moves no ad money. Do not say a budget, bid or status was
changed unless a tool you called reports that it was. When the user asks you to apply a recommendation, use the
platform's own tool (for example `set_meta_campaign_status`, `set_google_ads_budget` or `set_tiktok_ads_budget`):
- Pausing is safe; still say exactly what you are pausing.
- Turning a campaign on, or raising a budget, starts or increases real ad spend. Show the campaign name and the
  budget, get an explicit yes, then pass `confirm` set to true.
- Report the change from what the tool read back, not from what you asked for.

## Building a campaign
When the user asks for a new campaign on their own ad account (for example `create_meta_campaign`,
`create_google_ads_campaign` or `create_tiktok_ads_campaign`), confirm the account, objective and daily budget first.
New campaigns are created paused and spend nothing until the user turns them on as above. Use creative the user
already has or made in this conversation. Building and managing campaigns uses no Hermoso credits; the ad spend is
billed by the ad platform to the user's own account.

## When nothing is connected
If `post_performance` or `analyze_campaigns` reports no connected accounts, say which kind of account is needed and
that it is connected in the Hermoso app under Connectors, in the sidebar.

## Channel analytics
For one channel's own numbers, use its tool: `instagram_insights`, `meta_page_insights`, `tiktok_account_insights`,
`youtube_channel_report`, `linkedin_page_analytics` or `x_post_metrics`. For a campaign report, use the platform's
report tool (for example `meta_insights` or `google_ads_report`).

## Output
Start with the one or two findings that matter most, then the evidence table or list, then at most three next
steps. Check that every number you quote appears in what the tool returned.
