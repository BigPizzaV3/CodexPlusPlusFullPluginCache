---
name: plan-my-move
description: Use when someone is buying, selling, renting or letting a home and asks what moving will cost, what they need to do, or wants a moving checklist or budget.
---

Use the Homemove plugin's MCP tools directly for quotes and move plans. They require no Homemove login. Discover the connected Homemove tools if they are not immediately listed. Do not open or control the separate Homemove desktop application (`com.homemove.app`), use browser automation to obtain a quote, or ask the user to sign in to Homemove as a substitute for a missing MCP tool. If discovery still does not expose the required tool, clearly report that the plugin's tool connection is unavailable in this chat; do not invent a price or claim that reconnecting succeeded. Open a returned Homemove continuation or booking link only when the user wants to continue with that quote.

For a moving checklist or who to notify, use `homemove_moving_checklist`, not the pricing plan. Ask only for the situation (buying, selling, buying and selling, renting or landlord) if unknown, and use a moving date if supplied. No address, budget or mortgage details are needed for a checklist. For a council tax band, use `homemove_council_tax` with the postcode and first address line; do not claim it returns a bill or a Homemove service price. For mortgage repayment arithmetic, use `homemove_mortgage_repayments` with price, deposit, interest rate and term; explain that the result is illustrative, not advice or an offer. Do not infer income or report a loan-to-income ratio without the user's income. For insurance, mortgages or estate-agent service access, `homemove_quote` may show the corresponding website handoff; do not quote insurance premiums, recommend a lender or insurer, or complete a purchase. Only use the numbered pricing workflow below when the user asks for a move budget or service prices.

Set out the whole move with Homemove's quotes. The user's own instructions come first.

1. Find out what they are doing: buying, selling, both, renting (moving out of a rental) or letting a home out. Ask for the postcode of each home involved, and the first line of the address if they will give it, because the property record then fills in bedrooms and tenure.
2. For a purchase, ask the price and whether they are a first-time buyer, buying an additional home, and buying with a mortgage or in cash. For a sale, ask the expected price and whether there is a mortgage to pay off.
3. Call `homemove_move_plan` with what they told you. Never invent a price, a bedroom count or a household of furniture for them.
4. Tell them the total of the priced steps in one sentence, name any step still to price and offer to price it (removals need what they are moving; call `homemove_quote` with `items`). Say that stamp duty is paid to HMRC and is not part of Homemove's total.

Quotes are confirmed when they book on homemove.com. Do not give mortgage advice or recommend lenders.
