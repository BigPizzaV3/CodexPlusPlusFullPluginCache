---
name: wincloud-adr-revpar
description: Use when a user asks about average daily rate (ADR), revenue per available room (RevPAR), pricing performance, which room types earn the most, how prices have changed over time, or how current rates compare with what guests actually paid. Works from WinCloud's night-audit performance figures, reservation analytics, tariffs and room counts.
---

# ADR, revenue and pricing performance

Follow `wincloud-report-format`.

Resolve hotel names with `list_companies` before gathering data, and label every hotel by name in the output, as `wincloud` explains. For several hotels, use one row or series per hotel name.

## ADR from bookings

1. Call `get_reservation_analytics` with `report` = `bookings`, a date range and optionally `roomTypeId`. Read all pages.
2. Each row has rooms (booked plus availed, as `wincloud` explains) and an ADR, which is the reservation's tariff as WinCloud stores it. Average ADR = Σ(ADR × rooms) ÷ Σ(rooms). Don't take a plain average of the row ADRs. Cancelled and no-show reservations are already left out; waitlisted and turned-away reservations are still included and carry no status, so say the figures may include them.
3. Group by arrival month, room type, or meal plan for a trend or breakdown. The range filter is the **booking date**, so say that the figures cover bookings made in the range, not stays in it. For ADR of stays in a period, widen the booking range and keep only rows arriving in the period, as `wincloud` explains.
4. Rows are per reservation, not per night, so ADR here is the booking's rate, not a night-weighted figure.

## Current pricing versus bookings

- `search_room_tariffs` gives the prices and restrictions set for dates. Use `get_rate_plans` first for the room type and rate type ids. Weekend tariffs are not included, so say the picture covers weekdays only.
- Name the exact rate plan you compared against. For a "standard price", follow `wincloud` and never pick a plan silently.
- Compare the **rate on the calendar** with **ADR on the books** for the same room type and arrival month. A large gap suggests discounted channels, packages or old rates; say it is a possible reason, not a finding.

## Actual revenue, occupancy and RevPAR (past dates)

- `get_room_performance` gives the night-audit figures for a past period: occupancy %, ADR, RevPAR, room revenue, total revenue with room tax and room nights sold, plus month to date, financial year to date, a split by room type and the change against the previous period, month or year. Use it whenever the question is about actual performance, and label its figures "actual (night audit)".
- Its ADR is room revenue ÷ room nights sold, so it differs from the booking ADR above. Don't mix the two in one chart; name which one each figure is.
- Quote its "Limitation" lines in the caveats.

## RevPAR for future dates

- `get_room_performance` has no future dates. For a future period give an **indicative** figure: Occupancy on the books × ADR, with occupancy from `wincloud-occupancy-forecast` Step 1. Label it "indicative RevPAR, based on bookings on the books, not actual revenue".

## Show

- **Headline:** average ADR for the period, the change against the previous period, and the top and bottom room type.
- **Chart:** ADR by arrival month (line) or by room type (sorted horizontal bars).
- **Table:** room type, rooms, ADR, with the calendar rate beside it when you fetched it.
- **Caveats:** the hotel, the date field, pages read, the currency, whether RevPAR is actual or indicative, and that bookings may include waitlisted and turned-away reservations. Analytics rows carry no currency: use the location's base currency from `list_companies`, or the currency `search_room_tariffs` returns, and say which.
