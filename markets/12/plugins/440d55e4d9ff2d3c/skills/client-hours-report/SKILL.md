---
name: client-hours-report
description: Build a client hours report from TimeTackle - total hours per client, and per person for each client, for a billing period, as a ready-to-share table. Use when the user asks for client hours, a billing summary, or hours spent per client or account.
---

# Client hours report

Produce a clean, shareable table of hours per client for a period. Explicit instructions from the user (period,
clients, people, rounding, format) take priority over these steps.

## Input

- The billing period. If none is given, ask for it, offering last month as the default. Use exact `YYYY-MM-DD` dates.
- Optionally specific clients, specific people, or a per-person breakdown.

## Steps

1. Call `get_account` and read `syncRange`. If the period reaches outside it, say that data only exists from
   `syncRange.start` to `syncRange.end`.
2. Find the client property: call `get_properties` with `search: "Client"`.
   - If there is no match, try "Account" and "Customer", then ask the user which property holds clients; do not guess.
   - Note its `key` and `state`. If the user asked about specific clients, check that those names appear among the
     property's options (`children`); if a property has more options than returned, page with `parentId` and
     `optionsOffset`.
3. Call `get_meeting_analytics` with:
   - `measures: ["hours"]`
   - `groupBy: "primary_tag"` or `"secondary_tag"` (from the property's `state`), and `tagKey` set to its key
   - `splitBy: "user"` when the user wants hours per person per client
   - `dateFrom`, `dateTo`, and `timezone` (the user's, otherwise the `timezone` of their own calendar from
     `get_imported_calendars`; say which one you used)
4. Page with `offset` while `summary.nextOffset` is not null, and combine the rows.
5. Keep only the clients (and people) the user asked for, if they named any.

## Output

- A table with one row per client, sorted by hours: client, hours (one decimal unless the user asks for another
  rounding), share of the total. With a per-person breakdown, list each client's people under it with their hours,
  or use a client × person table if it stays readable.
- A total row, the exact period, and the timezone.
- A note that time not tagged with a client is not included.
- If the result has a `syncRangeWarning`, include it.

## Do not

- Do not calculate amounts, rates or invoices unless the user gives the rates; then show the calculation.
- Do not invent clients or hours. If a requested client has no hours, show it with 0 and say so.
- People are limited to those the user can access in TimeTackle.
