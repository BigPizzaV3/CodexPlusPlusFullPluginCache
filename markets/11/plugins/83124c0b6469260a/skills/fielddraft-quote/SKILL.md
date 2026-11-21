---
name: fielddraft-quote
description: Turn a contractor's job-site description into an itemized draft quote from their own price book and push it to Jobber. Use when a tradesperson describes work they need to quote (panel upgrades, EV chargers, generator inlets, HVAC repair or replacement, service calls) or asks what they charge for something.
---

# Drafting a quote with FieldDraft

FieldDraft never invents prices. Every line comes from the contractor's own Jobber products & services list. Your job is to capture what they said accurately, let the tool do the matching, and surface what still needs the contractor's decision.

## Workflow

1. **Capture the job in the contractor's words.** If they gave a voice-style ramble, keep quantities, locations, run lengths, equipment sizes and site conditions. Do not pad it with work they did not mention.
2. **Call `draft_quote`** with `jobDescription`, plus `clientName` if it was mentioned. If they shared photos as public URLs, pass up to six in `photoUrls`.
3. **Read the result.** Lines marked `[NO PRICE BOOK MATCH]` have no price. Lines marked `[check match]` were a best guess. Report both plainly. List the open questions.
4. **For unmatched lines**, call `search_price_book` with a short query to offer the closest items. If the contractor names a price or picks an item, call `update_quote_lines` with the full corrected line list (all lines, not just the changed one).
5. **Only after the contractor explicitly says to send it to Jobber**, call `push_quote_to_jobber`. It needs the customer's name; if the draft has none, ask for the name, email and job site address first and pass them in the call. Email or address lets FieldDraft reuse an existing Jobber client instead of creating a duplicate. It creates a draft quote in Jobber; they still send it from Jobber. Never push on your own initiative.
6. If a tool reports that Jobber is not connected or the monthly draft limit is reached, pass on the tool's message as written and stop.

## Style

- Show the quote as a short table or list with quantities, unit prices and line totals, then subtotal, tax and total.
- Keep assumptions and exclusions visible; they protect the contractor.
- Prices are the contractor's. If they ask "is this a fair price?", say FieldDraft uses their price book and does not benchmark the market.
- Never mention subscriptions, plans or upgrades inside the conversation.
