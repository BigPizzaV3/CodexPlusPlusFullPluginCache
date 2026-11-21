---
name: hypd-get-started
description: Welcome users who are new to SEO & GEO by HYPD AI or ask how to get started, show the getting started steps and lead them to a first question about their organic search or AI visibility. Use when someone has just installed it or asks what to do first; a concrete SEO question goes straight to that task instead.
---

# Get started with SEO & GEO by HYPD AI

SEO & GEO by HYPD AI shows how a site is found in Google's organic results, in Google's AI Overviews and in AI answers. It reads the user's own Search Console (and Google Analytics, when connected), and researches any site or keyword: volumes, difficulty and intent, the results page, AI answers, competitors, backlinks and the pages themselves.

## Show the steps

Call `hypd_show_getting_started`. It returns the user's own steps: connect Search Console and select a property, ask a first question about their organic traffic, and check whether AI answers name their brand. A step the user has finished comes back marked done.

- Where the client renders MCP Apps, the steps appear as a widget with a button each. A click sends that step's prompt as the user's next message or opens the HYPD app. The user can already see every step, so one short sentence pointing to them is enough, and a step runs when the user clicks it.
- Elsewhere, list the steps with their links and prompts.
- If the tool is not available, `init` returns the guide, and `seo_gsc_list_sites` shows which properties are connected.

## When the user already knows what they want

If the user names a concrete task, such as a traffic drop, a keyword to research, a competitor or whether an AI Overview cites their site, start on that task instead of showing the steps. The research tools need no connection, so they work before Search Console is connected. Questions about HYPD itself, such as connecting accounts or privacy, are answered from `hypd_search_help`, citing the article.
