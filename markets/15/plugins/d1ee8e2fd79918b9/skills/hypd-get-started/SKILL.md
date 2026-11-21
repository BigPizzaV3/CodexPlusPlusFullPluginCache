---
name: hypd-get-started
description: Welcome users who are new to HYPD.AI Competitor Ads or ask how to get started, show the getting started steps and lead them to a first look at a competitor's ads. Use when someone has just installed it or asks what to do first; a question that names a competitor or a keyword goes straight to that task instead.
---

# Get started with HYPD.AI Competitor Ads

HYPD.AI Competitor Ads shows the ads competitors run, from public data: Facebook and Instagram ads from Meta's library, Google ads on Search, YouTube, Shopping, Maps and Play, who advertises on a Google search, competing sites and landing pages. Nothing needs to be connected.

## Show the steps

Call `hypd_show_getting_started`. It returns the user's own steps: look up a competitor's Facebook and Instagram ads, then see who advertises on a Google search. A step the user has finished comes back marked done.

- Where the client renders MCP Apps, the steps appear as a widget with a button each. A click sends that step's prompt as the user's next message or opens the HYPD app. The user can already see every step, so one short sentence pointing to them is enough, and a step runs when the user clicks it.
- Elsewhere, list the steps with their links and prompts.
- If the tool is not available, `init` returns the guide; ask for the competitor and the country, then look up its ads.

## When the user already knows what they want

If the user names a competitor, a keyword or a landing page, start on that task instead of showing the steps. Questions about HYPD itself, such as connecting accounts or privacy, are answered from `hypd_search_help`, citing the article.
