---
name: daily-review
description: Prepare HoreX daily restaurant reviews, open saved review cards and subscribe at the user chosen Dubai time. Use for morning briefs and recurring P&L reviews, not unsolicited broadcasts.
---

## State capability limits precisely

The plugin cannot edit, post, settle or mark Finance/Catering invoices paid, rewrite P&L, correct stock or recipes, send customer messages, make purchases or book travel. This remains true even when the user has evidence and native permissions. Offer analysis or the authorized native HoreX workflow, never promise that this plugin can perform those changes. Unsupported mutation requests require no business-data call. Supported Team tasks and advertising settings use only their dedicated proposal and native approval flows; they do not grant general editing or payment capabilities.

## Execute HoreX calls sequentially

For one connected HoreX account, wait for each call to finish before starting the next. Keep the result, source and billing status of each call separately. A busy/concurrency error applies only to the rejected call; it does not invalidate another successful result. Reuse successful results. Retry only the failed read once after the active call finishes, within the user's remaining successful-read budget. If no budget remains, report the partial result and ask before another charged read. Never broaden access or repeat a proposal/provider write to recover a read error.

A daily review uses the canonical HoreX P&L for the previous complete Dubai day. Include revenue, cost of goods sold, accounting profit and the source cost coverage. Invoice COGS is the default; use itemized COGS only when explicitly chosen. Do not rename all COGS as food cost or treat the report as operational sales. Daily events currently cover P&L only. Extra invoice, stock or receivables sections require their own permitted tools and successful reads each cost 1 AI Credit; do not promise those sections in a single scheduled report.

For a one-time report choose get_pnl with explicit dates. Widget view is paused. Present the saved or live facts in a native answer in the current AI application using text and tables, with the exact Open in HoreX source link. The free open_restaurant_workspace tool returns workspace facts.

For recurring delivery, first obtain the user's daily hour and minute in Asia/Dubai, permitted branch or all accessible branches, and any explicit COGS preference. Tell the user that each successfully generated daily P&L costs 1 HoreX AI Credit, failed reads are free, and reopening the same saved review is free. Do not choose a time, activate a subscription or send messages to other people without the user's request. Discover daily_review.ready through events/list and use the host's native event-subscription flow, which supplies its verified callback. Do not invent callback URLs or secrets, use a local automation as a substitute, or claim home-page recommendations are guaranteed.

When a daily_review.ready event arrives, inspect status and period. For ready events call get_daily_review with the exact review_id to open the free dated card. Clearly identify the report as a saved snapshot, preserve its period and COGS basis, and note any settlement_pending status. Do not request get_pnl again just to render that snapshot. An unavailable event has no report figures: explain its message and do not invent values or retry paid reads unless asked. Subscriptions expire with their HoreX connection or configured TTL. Current permissions are rechecked before generation, delivery and opening; reconnect and resubscribe if necessary. Stopping a review uses the host's unsubscribe flow with the same chosen arguments and destination. Never claim a subscription is active until the host confirms it.

Host compatibility: Claude does not support the ChatGPT events extension or MCP resource subscriptions. In Claude, provide on-demand reports and open a saved review only when its ID is already known. Do not call events/list or invent a scheduled-delivery callback, create a subscription, or promise automatic delivery into Claude. Explain this limitation when asked for recurring delivery.
