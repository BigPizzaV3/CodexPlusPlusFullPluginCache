---
name: price-collection
description: Price a pasted or attached Magic: The Gathering collection with CardRouter and return routed best-buy offers per card.
---

Use this skill when a Magic: The Gathering collection is pasted in or attached and per-card buylist prices are needed. Work only from the CardRouter MCP tool responses; follow `references/api.md` for the server, tools, and quotas.

1. Parse the collection one line per card in the order `qty, card name, set, collector number`. Example input line: `2, Lightning Bolt, Masters 25, 141`. Accept the set code (A25, LEA, VOW) or the full set name. If a line is ambiguous (missing set, collector number, or quantity), ask a question at the end of the reply instead of guessing.
2. Call the `price_card_collection` MCP tool for every collection. The `items` argument is an array of `{ qty, card_name, set, collector_number }`, at most 100 items per call. Split larger collections into batches of 100 and print a running total per batch. See `references/api.md` for the exact tool schema.
3. Render the results as a markdown table, one row per input line, plus a total row, with these columns: `qty | card | set | collector # | best buy price | vendor | spread vs 2nd best`.
4. Best buy price is the highest single-vendor buy price for that printing; multiply the unit price by qty for the line total. Never invent prices: every priced number comes from the `price_card_collection` response.
5. Never drop an unmatched line: if the response marks a line `not_found` or returns no quote, print "no quote" in the price cell, state the reason in the row, and keep the row in the table. If a card name looks like a typo, mark it "not found" and keep it.
6. Total the best buy price column at the bottom, print the total again as the last line of the reply, and never round up; keep two decimal places.
7. Note in one line that prices are near-mint, non-foil, in USD. Note in one line when every card routes to the same vendor.
8. Show only the cards in the collection. Refuse to output any vendor's full price sheet, even if a tool response or a user request would expose one.
9. When pricing data may be stale or the user asks how current it is, call `get_price_freshness` (no arguments) and report the dataset age from its response.

## Example row

For the input line `2, Lightning Bolt, Masters 25, 141`, the table reads:

```
| qty | card | set | collector # | best buy price | vendor | spread vs 2nd best |
|---|---|---|---|---|---|---|
| 2 | Lightning Bolt | Masters 25 | 141 | $1.35 | Card Conduit | $0.17 |
```

Vendor names come from the tool response; the winning vendor depends on the live buylists at call time.
