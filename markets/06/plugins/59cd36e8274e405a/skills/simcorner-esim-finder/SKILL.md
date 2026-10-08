---
name: simcorner-esim-finder
description: Find and compare current SimCorner travel eSIM plans when a traveller provides destinations, trip length or dates, and a budget. Use for SimCorner eSIM discovery, plan comparison, data-fit questions, and device-fit checks; do not use for physical SIM recommendations or post-purchase support.
---

# Simcorner eSIM

Recommend the smallest sensible set of current SimCorner eSIM plans that covers the traveller's whole itinerary, service period, and data needs within budget.

## Get the trip brief

Require these essentials before making a final recommendation:

- Every destination where service is needed, including a layover only when the traveller wants connectivity there
- Trip dates or the number of service days
- Total budget and currency

Ask one concise combined question for missing essentials. Also use any supplied preferences: number of travellers, expected data use, hotspotting, calls/SMS or a local number, device model, and country of purchase. Do not force optional questions when the user wants a quick answer.

If data needs are unknown, offer a transparent estimate instead of pretending certainty. The current SimCorner FAQ frames light use as roughly 0.5–2 GB per day and heavy use as 3+ GB per day; verify this guidance live if it materially affects the recommendation.

## Verify the live SimCorner catalog

Browse official `simcorner.com` pages and localized SimCorner paths for every recommendation. Prefer the traveller's local storefront/currency when known. Use destination or regional collection pages to discover candidates, then open the exact product page and variant details.

For each candidate, verify:

- All included countries or regions
- Data allowance and any daily high-speed limit or throttled speed
- Validity and the plan-specific activation trigger
- Current variant price, sale status, and displayed currency
- Calls, SMS, phone-number, hotspot, speed, and top-up rules when relevant
- Availability and a direct product URL

Do not treat search snippets, cached prices, this skill's reference notes, or a similarly named plan as sufficient live evidence. Prices, promotions, variants, coverage, and plan rules can change. If the official page cannot be checked, say what remains unverified and do not label the result as current.

Read [references/catalog-guide.md](references/catalog-guide.md) when plan terminology, multi-country selection, activation, or company context affects the answer.

## Filter and rank

Apply hard constraints first:

1. Coverage must include every requested destination.
2. Validity must cover the full service period. If multiple plans are required, total their prices and explain the handoff.
3. Total price must include every traveller and every required plan, in the user's currency. Never silently compare different currencies.
4. The data model must fit the intended usage. Treat "unlimited" as product-specific and disclose every high-speed fair-use limit.
5. If traditional calls, SMS, or a local number are required, exclude data-only plans unless the traveller accepts app-based alternatives.

Among eligible plans, rank by full coverage, data adequacy, total price, less wasted validity/data, and setup simplicity. Prefer one regional or global eSIM over several country plans when the difference is small and the single plan still fits the budget. If nothing fits, state that clearly and show the closest verified option plus the exact budget gap; do not relax the budget silently.

## Present the answer

Lead with the best match and the reason. Show no more than three options in a compact comparison with:

- Plan and direct SimCorner link
- Destinations covered
- Validity and data model
- Current total price and budget fit
- The trade-off that distinguishes the option

State when prices were checked and which storefront/currency was used. Add only decision-relevant cautions, such as carrier-unlocked/eSIM-compatible device requirements, activation timing, daily high-speed limits, or missing voice service. Clearly separate verified facts from estimates.

The skill recommends; it does not place an order, add items to a cart, collect payment details, or claim that a displayed price is locked. Do not compare competitors unless the user explicitly asks.
