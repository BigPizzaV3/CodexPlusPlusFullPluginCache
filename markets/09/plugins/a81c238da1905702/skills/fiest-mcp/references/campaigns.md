# Timed item campaigns

Examples: “Give coffee 15% off tomorrow from 14:00 to 16:00”, “Extend the lunch
offer until Friday”, “End that offer”, or “Link the promotion to the signboard task”.

1. Check connection capabilities. Campaign tools require a restaurant owner/admin
   grant and the enabled campaign workflow. Management organization MCP grants are
   not supported by this bridge yet. Management's built-in Ask Fiest uses its own
   session-bound campaign tools instead. Never work around a denied grant.
2. Read `read_item_campaigns`. Use returned item/campaign/task IDs and versions,
   not guessed IDs or a permanent menu-price edit. Ask which item when ambiguous.
3. Ask only for missing material terms: item, percentage and start/end time.
   One item, 1–90%, one continuous period of at most 31 days, Fiest app orders.
   Use returned currentTime and timeZone. Money fields ending in Cents are EUR
   cents; use offerPriceCents for the quoted offer price.
4. For edits, copy every unchanged field from the fresh campaign, including its
   taskId. For ending, use its current version. An expired or ended campaign is
   not editable. Use effectiveStatus rather than inferring activity from the
   stored status alone.
5. Link only existing returned tasks. Task lookup/linking requires
   `fiest.tasks.read` as well as campaign access. Use the separate reviewed tasks
   workflow to create a task, then reread and link it. A task never activates an offer.
6. Call `propose_item_campaign_change` with a UUID requestId retained for exact
   retries. Show the restaurant, item, original/offer price, percentage, local
   period, linked task and expiry. Send the returned reviewUrl. The offer is still
   unchanged until a human confirms on the review page.
7. After confirmation, reread to report the actual scheduled/active/ended state.
   A verbal yes or `confirmed: true` is not a campaign approval. There is no MCP
   confirm/apply tool. Pending proposals also include review links for resuming later.
8. On a timeout, reread pending proposals and reuse the exact request ID/content
   for reconciliation. Never generate a replacement because the outcome is unknown.

First-visit bonuses and recurring happy hours are separate features; these tools
manage timed percentage discounts on a single item only. Do not invent support
for euro discounts, free-product campaigns, POS promotions or stacking.
