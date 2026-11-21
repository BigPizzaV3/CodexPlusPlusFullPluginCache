---
name: hypd-get-started
description: Welcome users who are new to Google Merchant Center by HYPD or ask how to get started, show the getting started steps and lead them to a first check of their product feed. Use when someone has just installed it or asks what to do first; a concrete Merchant Center question goes straight to that task instead.
---

# Get started with Google Merchant Center by HYPD

Google Merchant Center by HYPD reads the user's connected Merchant Center shops: products and their status, disapprovals, account issues, product performance, price competitiveness and competitive visibility.

## Show the steps

Call `hypd_show_getting_started`. It returns the user's own steps: connect Merchant Center and select a shop, check the product feed, then add the user's other platforms. A step the user has finished comes back marked done.

- Where the client renders MCP Apps, the steps appear as a widget with a button each. A click sends that step's prompt as the user's next message or opens the HYPD app. The user can already see every step, so one short sentence pointing to them is enough, and a step runs when the user clicks it.
- Elsewhere, list the steps with their links and prompts.
- If the tool is not available, `init` returns the guide, and `merchant_list_shops` shows which shops are connected.

## When the user already knows what they want

If the user names a concrete task, such as a disapproved product, a price comparison or products with few clicks, start on that task instead of showing the steps. Questions about HYPD itself, such as connecting accounts or privacy, are answered from `hypd_search_help`, citing the article.
