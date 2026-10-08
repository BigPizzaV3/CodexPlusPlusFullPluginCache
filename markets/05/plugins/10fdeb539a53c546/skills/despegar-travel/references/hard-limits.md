# Hard limits — Despegar travel skill

These rules override convenience. If a user asks for something that would break
them, refuse the violating approach and offer an allowed alternative.

## Forbidden: flight date scanning

**Date scanning** means probing many calendar dates by calling `flight-search`
(or equivalent fixed-date search) in a loop, batch, or parallel fan-out to find
the cheapest or “best” day.

### Examples of forbidden behavior

- “I’ll check every Friday in March” → many `flight-search` calls with different dates
- Sliding windows: date, date+1, date+2, … until a price target is met
- Comparing N dates by issuing N `flight-search` calls in one turn
- Using tool retries or “let me try again” as a cover for another date probe
- Asking the user to wait while you “scan the calendar” via tools

### Allowed instead

| User intent | Allowed action |
|-------------|----------------|
| Exact dates known | One `flight-search` with those dates |
| “Flexible / cheapest week / anytime in March” | One `flight_flexible_search`, **or** one `flight-price-trend`, **or** one `flight-deals`; then ask the user to pick concrete dates |
| User names a new specific date after seeing results | One new `flight-search` for that date (still not a grid) |
| User asks “which day is cheaper, the 10th or the 17th?” | At most **two** `flight-search` calls, only for those two named dates — then stop. Prefer flexible/trend tools if more than two candidates |

### Caps

- **Default:** ≤ 1 `flight-search` per user message.
- **Named A vs B comparison:** ≤ 2 `flight-search` calls total for that turn.
- **Never:** ≥ 3 `flight-search` calls in one turn for date discovery.
- Flexible / trend / deals tools: ≤ 1 call of that exploratory tool per turn unless the user changes origin/destination criteria.

## Other prohibitions

- Do not invent or round-trip invent inventory, prices, taxes, or baggage rules.
- Do not scrape despegar.com or third-party OTAs for live inventory.
- Do not chain `execute-product-action` without a real `actionId` from a prior tool result.
- Do not drop or rewrite `session.chatId` when continuing to checkout from a search that returned a session block.
- Do not use this skill for non-Despegar / non-travel automation.

## Refusal template (date scan)

If the user asks to scan many dates:

> I can’t run many flight searches across the calendar. Share exact dates for one
> search, or I can run a single flexible-dates / price-trend / deals lookup so you
> can pick a day — then we’ll search that date once.
