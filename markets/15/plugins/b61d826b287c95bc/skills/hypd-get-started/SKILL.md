---
name: hypd-get-started
description: Welcome users who are new to HYPD.AI Social Ads or ask how to get started, show the getting started steps and lead them to a first look at their Meta campaigns. Use when someone has just installed it or asks what to do first; a concrete question about their Meta ads goes straight to that task instead.
---

# Get started with HYPD.AI Social Ads

HYPD.AI Social Ads reads the user's connected Meta ad accounts across Facebook and Instagram: campaigns, ad sets and ads, performance reports, creatives, audiences, pixels and catalogs.

## Show the steps

Call `hypd_show_getting_started`. It returns the user's own steps: connect Meta Ads and select an ad account, then a first look at their campaigns. A step the user has finished comes back marked done.

- Where the client renders MCP Apps, the steps appear as a widget with a button each. A click sends that step's prompt as the user's next message or opens the HYPD app. The user can already see every step, so one short sentence pointing to them is enough, and a step runs when the user clicks it.
- Elsewhere, list the steps with their links and prompts.
- If the tool is not available, `init` returns the guide, and `fb_list_ad_accounts` shows which ad accounts are connected.

## When the user already knows what they want

If the user names a campaign, an ad set, a creative or a date range, start on that task instead of showing the steps. Questions about HYPD itself, such as connecting accounts or privacy, are answered from `hypd_search_help`, citing the article.
