---
name: vestiaire-shopping-planner
description: Build coordinated, multi-item shopping plans with Vestiaire Collective catalog tools. Use for outfits, capsule wardrobes, gifts, or other pre-loved luxury shortlists that need several product searches or a shared budget. Do not use when the primary goal is a simple one-item search, one-product details, checkout, order support, or trend research.
---

# Vestiaire Shopping Planner

Create a coordinated shortlist with the Vestiaire Collective MCP tools `search`
and `getProduct`. Treat their current descriptions and schemas as the source of
truth for catalog fields, filters, and tool-level limitations.

## Build the shopping brief

Extract the information that the user already gave:

- The goal, occasion, or recipient.
- Two or more concrete item types and the requested quantity of each.
- The total budget, per-item limits, and currency.
- The buyer's market or shipping country.
- The relevant universe and stated sizes.
- Hard requirements and optional preferences.

Do not ask again for established information. Ask one concise follow-up question
when a missing value prevents a useful search. An open-ended styling request that
does not name an item type needs the item types, recipient or universe, and budget
before searching.

When the user gives only a total budget, create provisional per-item maximums
whose sum respects it. For "under" or "below," keep the sum strictly lower. For
"up to" or "at most," the sum can equal the limit. State the allocation before
the searches. Ask for confirmation only when the allocation could conflict with
a stated priority.

## Search by item type

1. Call `search` separately for each concrete item type. Do not combine unrelated
   categories into one query. When the user wants more than one of the same item
   type, use one search to produce enough candidates for the requested quantity.
2. Preserve the market, currency, and unchanged hard requirements across
   searches. Apply each size only to its relevant item type. Never carry a
   clothing size into shoes, bags, or accessories. Apply each provisional or
   user-supplied per-item maximum.
3. Follow the `search` tool description for query construction and typed fields.
   Do not invent filter values or sizing conversions.
4. If a result needs clarification, relay its question and pause that part of the
   plan. If a size is unresolved, state that the results are not size-filtered.
   A verbatim size request without nonempty explicit `sizes` tokens must not
   produce a filtering claim when `sizeResolution` is absent.
5. If a search has no results, identify the affected requirement. Suggest one
   possible refinement, but do not relax the requirement without user approval.
6. Present the returned products as candidate sets grouped by item type. Do not
   select a winner at this discovery stage. Ask the user which candidates they
   want to compare, or which search they want to refine.

## Complete the plan after selection

After the user selects candidates or asks for a comparison:

1. Call `getProduct` for each selected product id. Keep the market from its search.
2. Use only returned facts. Use each returned `url` exactly as supplied.
3. Follow the MCP comparison contract. Name a preferred match only when the facts
   support it. Otherwise, explain when each option fits without forcing a winner.
4. Add current prices only when all selected products use the same currency. Make
   clear that prices and availability can change.

Write the completed plan in this order:

1. **Shopping brief** — the confirmed goal, market, budget, sizes, and hard
   requirements.
2. **Selected plan** — one row per item with its name and exact link, current
   price, condition, listed size, and other returned facts that matter. Preserve
   the requested quantity of each item type.
3. **Budget status** — the current total in one currency and the remaining amount,
   or a clear reason that no total is available.
4. **Trade-offs and unknowns** — facts that affect the choice and missing details
   the user should verify.
5. **Styling notes** — optional opinion, clearly separate from catalog facts.

## Boundaries

- Do not buy an item, complete checkout, track an order, or contact a seller.
- Do not claim that an item is authentic from a fulfilment route or marketplace
  policy. Do not invent a certificate or item-level authentication evidence.
- Do not describe an item as discounted unless its returned original price is
  greater than its current price.
- Do not claim social popularity, trend ranking, quality, value, rarity, fit, or
  seller reliability without returned evidence.
- Do not treat missing data as a negative fact. Label it as unknown.
- Keep catalog facts separate from styling judgment.
