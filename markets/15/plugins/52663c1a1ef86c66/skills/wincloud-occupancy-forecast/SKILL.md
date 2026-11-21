---
name: wincloud-occupancy-forecast
description: Use when a user asks how full the hotel will be, for an occupancy forecast, expected rooms or occupancy for coming days, weeks or months, which dates are weak or sold out, or how many rooms are still to sell. Estimates future occupancy from the reservations already on the books in WinCloud, optionally adding typical late bookings from the past.
---

# Occupancy forecast

Follow `wincloud-report-format`. This is an estimate. Say so in the headline area and again in the caveats.

Resolve hotel names with `list_companies` before gathering data, and label every hotel by name in the output, as `wincloud` explains. For several hotels, use one row or series per hotel name.

## Capacity

Total rooms = the sum of total rooms across room types from `get_inventory` (or `list_room_types`). `list_companies` also gives each location's room count; if the two differ, use the room-type sum and say so. Use one figure for the whole window, and say that out-of-order rooms are not known.

## Step 1: Rooms on the books, per night

1. Choose the window (default: next 30 days, at most 90). Turn it into exact dates.
2. Call `search_bookings` with `departureFrom` = window start and `arrivalTo` = window end. This returns every stay that touches the window, including ones that began earlier. Read all pages; if there are more than 15, say the forecast covers only the pages read and narrow the window.
3. Keep only Confirmed, Tentative, Provisional and CheckedIn; drop every other status (Cancelled, NoShow, TurnAway, WaitingList, CheckedOut, Unknown).
4. For each booking, count its rooms on every night from arrival up to, but not including, departure. Add them up per night. A night is occupied from the arrival date; the departure date is free.
5. On-the-books occupancy per night = rooms on the books ÷ total rooms.

Mark Tentative and Provisional separately (a lighter shade): they may not convert.

## Step 2 (optional): Likely late bookings

Only if the user wants a fuller forecast and you can afford the calls:

1. Do Step 1 for the same dates one year earlier (or the last comparable period), but **keep CheckedOut** as well: those nights are past, so the guests who stayed now show as CheckedOut. Count only bookings made at least as many days before each night as today is before the forecast night. That is last year's position at the same point.
2. Compare it with last year's final result for those nights (CheckedOut and CheckedIn bookings: the stays that actually happened). The gap is last year's late pickup. Bookings cancelled since then no longer count, so last year's position is slightly understated; say so.
3. Add that gap, as a share of last year's position, to this year's on-the-books figure. Cap the result at 100%.

If last year is missing, too thin, or unlike this year (an event, a closure), skip Step 2 and say why. Don't invent a pickup.

## Show

- **Headline:** the average occupancy for the window, the strongest and weakest dates, and the number of rooms still to sell.
- **Chart:** line or bars by date: on-the-books occupancy solid; the estimate with late bookings (if you did Step 2) dashed or lighter. Mark Tentative on its own if significant.
- **Table:** weeks or the 7 weakest dates with rooms on the books, rooms still to sell and occupancy.
- **Caveats:** the method, the window and hotel, the pages read, and:
  - walk-ins and late bookings are not predicted unless Step 2 was done;
  - events, holidays, price changes and overbooking are not known;
  - the figure is an estimate to verify before it drives pricing or staffing.

## Limits

- `get_inventory` is today's snapshot, so it is not a source of future availability. Future occupancy always comes from bookings.
- Group blocks and allotments may not appear as bookings; the forecast can understate them.
- Don't present a forecast as a promise or as the hotel's official figure.
