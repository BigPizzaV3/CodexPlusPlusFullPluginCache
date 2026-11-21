---
name: hypd-get-started
description: Welcome users who are new to Keyword Research by HYPD AI or ask how to get started, show the getting started steps and lead them to a first keyword search. Use when someone has just installed it or asks what to do first; a concrete keyword question goes straight to the research-keywords workflow instead.
---

# Get started with Keyword Research by HYPD AI

Keyword Research by HYPD AI finds keyword ideas, search volumes, competition, bids and advertising forecasts for a market. No Connection is needed to start. With a connected Google Ads Account, ideas and volumes come from Google Keyword Planner instead of market estimates.

## Show the steps

Call `hypd_show_getting_started`. It returns the user's own steps: a first keyword search, connecting Google Ads for Google's own numbers, then adding the user's other platforms. A step the user has finished comes back marked done.

- Where the client renders MCP Apps, the steps appear as a widget with a button each. A click sends that step's prompt as the user's next message or opens the HYPD app. The user can already see every step, so one short sentence pointing to them is enough, and a step runs when the user clicks it.
- Elsewhere, list the steps with their links and prompts.
- If the tool is not available, ask for one or two seed keywords and a target country, then follow `$research-keywords`.

## When the user already knows what they want

If the user names keywords, a market or a budget, follow `$research-keywords` instead of showing the steps. Questions about HYPD itself, such as plans, lookup limits or privacy, are answered from `hypd_search_help`, citing the article.
