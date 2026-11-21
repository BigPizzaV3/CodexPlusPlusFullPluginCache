---
name: expiration-and-event-calendar
description: Use when the user asks which options expirations, VIX expirations, exchange holidays or other scheduled exchange-calendar events fall in a date window (for example "what expires the week of Nov 2", "is the market open on Nov 3", "when is the next quarterly expiration"), or where SPX max pain sits for a given expiration. Reads get_market_calendar and get_max_pain from the SquawkFlow app and reports each date with the exchange document date it was checked against. Covers the exchange calendar only, not economic releases or earnings.
---

# Expiration and event calendar

SquawkFlow's calendar is read entry by entry off the official exchange holiday and expiration calendars. No
date is worked out from a rule (the third-Friday rule is wrong for June 2026,
when the standard expiration moved to Thursday June 18 for Juneteenth). This
skill answers "what falls in this window" and "where does max pain sit for this
expiration".

## Tools

- `get_market_calendar` (optional `date`, ISO): whether that date is a session,
  the next session after it, the next monthly, quarterly and VIX futures
  expiration, the SPX settlement rules in the exchange wording, and the upcoming
  exchange full-day closures.
- `get_max_pain` (optional `expiration`, ISO): the SPX max pain strike for one
  expiration, and the list of expirations the tool answers for.
- `search` and `fetch`: SquawkFlow's published calendar and glossary pages, for
  example a dated event-week page.

## Procedure

1. Fix the window as two absolute dates. If the user gives a relative window
   ("next week"), resolve it to dates and state them.
2. Call `get_market_calendar` with `date` set to the window start. Record:
   - "Calendar verified on" (the date the exchange documents were checked),
   - sessions and closures inside the window from the closure table,
   - the next monthly, quarterly and VIX expirations.
3. If a listed next expiration falls inside the window and the window extends
   past it, call `get_market_calendar` again with `date` set to the day after that
   expiration, until the window is covered. Stop at the end of the published
   table; a date past it is "not published", never computed.
4. When the user asks about max pain for an SPX expiration, call `get_max_pain`
   with that `expiration` (omit it for the nearest one) and report the strike,
   the expiration and "Captured (UTC)". Max pain covers SPX only.
5. If any response is a stale copy, report it as the last good reading with its
   own capture time and say the fresh call failed. If a call returns no reading,
   say no fresh reading was retrieved at that time and give the linked page,
   which shows the last published reading with its as-of time. Do not fill it in
   from memory.

## Answer shape

- The window, as absolute dates.
- A table: Date, Weekday, What (session closure, monthly expiration, quarterly
  expiration, VIX expiration), Source and checked date.
- For each SPX expiration the user asked about: the max pain strike with its
  capture time, described as where open interest sits, not as a forecast.
- One line on what this calendar does not cover (below).
- The citation URL(s) and "Not investment advice."

## What this calendar does not cover

- No scheduled economic releases (jobs, CPI, FOMC and so on) and no earnings
  dates. Say that plainly if the user asks; do not add dates from memory and
  present them as SquawkFlow's. SquawkFlow publishes a few dated event-week
  pages. Use `search` to find one for the window; if it exists, `fetch` it and
  cite that page with the date the page states for itself. If none exists, say
  so.
- No half sessions: they are not published, so a listed session may be a half
  session.
- No market hours: the calendar answers whole days, not whether the exchange is
  open at this moment.

## Rules

- Every date carries its source (the official exchange calendars via SquawkFlow) and the date it was
  checked. Every max pain figure carries its expiration and capture time.
- Never compute an expiration from a rule. If the table does not state it, it is
  "not published".
- Max pain is not a forecast of where SPX settles and not a target.
- Standard monthly SPX options are A.M.-settled at the open of expiration day;
  SPXW options settle at the 4:00 pm ET close (1:00 pm on a half day). Use the
  settlement wording the tool returns.
- Never use these figures to tell anyone whether to buy, sell, hold, enter, exit
  or wait on any position. No entry or exit levels, no setups, no level at which
  a trade becomes better or worse, and no "I would" or "I would not". Never say
  whether the data supports, favours or argues against any trade or position,
  and never frame the levels as inputs "to make that decision". When the user
  asks for a trade decision, decline that part in one sentence, then state only
  the dated levels and what each one measures.
- No advice, no trade calls, no predictions about what happens on any date.
- Dates are absolute. Say "Not investment advice." once.
