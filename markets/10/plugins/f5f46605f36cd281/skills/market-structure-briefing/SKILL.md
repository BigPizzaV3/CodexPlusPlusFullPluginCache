---
name: market-structure-briefing
description: Use when the user wants a dated, cited market structure brief, for example "give me the market structure going into this week", "what does the VIX curve and max pain look like", or "how are futures traders positioned in the S&P". Builds one brief from the SquawkFlow app (get_market_calendar, get_max_pain, get_vix_term_structure, get_positioning), with every figure carrying its source and as-of time. Descriptive only; no trade ideas, targets or forecasts.
---

# Market structure briefing

A brief is a set of dated readings, each from a different dataset with a
different vintage. The value of the brief is that every line says how old it is.
Never merge readings into one "as of" time they do not share.

## Tools and what each reading is

| Section | Tool | Vintage to report |
| --- | --- | --- |
| Calendar | `get_market_calendar` | Answered-as-of date and the date the calendar was verified |
| Max pain | `get_max_pain` | Expiration and Captured (UTC); open interest is a settlement figure |
| VIX futures curve | `get_vix_term_structure` | Settlement date |
| Futures positioning | `get_positioning` | CFTC report date (the Tuesday the positions are as of) and release date |

## Procedure

1. Max pain covers SPX only. If the user names another symbol, say so and skip
   that section rather than substituting a figure.
2. Call the tools one at a time, in this order, and keep each response:
   1. `get_market_calendar` with no date (whether the next day is a session, the
      next monthly, quarterly and VIX expirations).
   2. `get_max_pain` (the default is the nearest SPX expiration).
   3. `get_vix_term_structure`.
   4. `get_positioning` with `contract` set to `sp500` (or the index future the
      user asked about; omit `contract` to list the published ones).
   The app spaces calls one second apart; do not re-call a tool whose result is
   already in the conversation.
3. For each response, check for `STALE COPY, NOT A FRESH READING` before using it.
   A stale copy is the last good reading: use it with its own capture time and
   the words "last good reading, the fresh call failed". If a call returns no
   reading at all, say no fresh reading was retrieved at that time and give the
   linked page, which shows the last published reading with its own as-of time.
   Never fill a section from memory or from an older brief.
4. Write the brief in the shape below. Keep it short: one to three lines per
   section.

## Brief shape

```
Market structure brief, compiled <retrieval time UTC>
Source: SquawkFlow (squawkflow.com), delayed and derived data. Not investment advice.

Calendar (verified <date>): <session status, next monthly / quarterly / VIX expiration>
Max pain (<expiration>, captured <UTC>): <strike>, <distance from spot>
VIX futures (settled <date>): <contango/backwardation>, M1 <x>, M2 minus M1 <x>
Futures positioning (CFTC, positions as of <date>): asset managers net <x>, leveraged funds net <x>, change on the week <x>

Caveats: max pain describes where open interest sits, CFTC data is weekly and lagged, nothing here is real time.
Links: <one citation URL per section>
```

## Rules

- Every number carries its source and its date or capture time. If you cannot
  state both for a number, leave the number out.
- Never use these figures to tell anyone whether to buy, sell, hold, enter, exit
  or wait on any position. No entry or exit levels, no setups, no level at which
  a trade becomes better or worse, and no "I would" or "I would not". Never say
  whether the data supports, favours or argues against any trade or position,
  and never frame the levels as inputs "to make that decision". When the user
  asks for a trade decision, decline that part in one sentence, then state only
  the dated levels and what each one measures.
- Do not synthesize across sections into a call. No "bullish", "bearish",
  "expect", "likely to", "target", "support will hold", "fade", "buy" or "sell".
  Each section describes one dataset; the brief does not conclude.
- Max pain describes where open interest sits for one expiration. It is not a
  magnet and not a forecast of the settlement.
- The VIX curve is a set of settlement prices. Its shape says what futures
  settled at, not what volatility will do.
- CFTC positioning is reported weekly for positions as of a Tuesday and
  released later. Say both dates. It does not say why anyone is positioned.
- Nothing here is real time. Never write "live" or "right now" about a reading;
  write its capture time.
- Dates are absolute (2026-10-05), never "today" or "yesterday".
- One brief line: "Not investment advice."
