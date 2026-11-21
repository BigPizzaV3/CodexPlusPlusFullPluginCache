---
name: wincloud-daily-briefing
description: Use when a user asks for today's picture at a hotel, such as a morning briefing, "how are we doing today", today's arrivals and departures, in-house guests, how full the hotel is now, or what needs attention today. Builds a one-screen summary from WinCloud's live bookings and room status.
---

# Daily briefing

Follow `wincloud-report-format`.

Resolve hotel names with `list_companies` before gathering data, and label every hotel by name in the output, as `wincloud` explains. For a briefing across hotels, repeat the steps below per hotel and show one row or series per hotel name.

## Gather (all for today's date, yyyy-MM-dd)

1. **Rooms now:** `get_inventory`: occupied and vacant by room type. Add the room types up for the total. Page through if more than one page.
2. **Arriving today:** `search_bookings` with `arrivalFrom` and `arrivalTo` = today. Read the status of each booking; count those still expected (Confirmed, Tentative, Provisional) and those already CheckedIn.
3. **Departing today:** `search_bookings` with `departureFrom` and `departureTo` = today. Count CheckedIn versus already CheckedOut.
4. **In-house:** `search_bookings` with status `CheckedIn`. Take the count from the first line of the result ("N booking(s)"); read more pages only if you need the list.
5. **Cancelled today:** `search_bookings` with `cancelledFrom` and `cancelledTo` = today.
6. **Booked today (pickup):** `search_bookings` with `startDate` and `endDate` = today.
7. **Room counts:** `get_booking_summary` with `fromDate` = today gives rooms still expected to arrive, rooms checked out and in-house rooms still due to leave. Its rooms arrived, walk-ins and guests come from the night audit and may read 0 for today, so take arrived-today from step 2. Steps 2 and 3 count bookings, this counts rooms; say which each KPI uses.

Run independent calls together. Take counts from each result's first line ("N booking(s)") and only fetch extra pages when you list people.

## Show

- **Headline:** occupied of total rooms, arrivals and departures still to come, and the one thing that stands out.
- **KPI row:** Occupied %, Arrivals (expected / arrived), Departures (expected / left), In-house, New bookings today, Cancellations today.
- **Chart:** occupied versus vacant by room type, as horizontal bars.
- **Table:** today's arrivals, 15 rows at most: guest, room type, plan, nights, status.
- **Attention list**, only items the data supports: arrivals not yet checked in, departures not yet checked out, cancellations today, a room type with no vacancy, rooms counted as neither occupied nor vacant, and in-house bookings whose departure date has passed.

## Limits

- `get_inventory` is a snapshot of right now, so say the time you read it. It can't show tonight's or tomorrow's availability.
- Occupied % is occupied rooms divided by total rooms from `get_inventory`. If a room count comes back as "-", say it's missing; don't treat it as zero.
- Show occupied, vacant and "other or unavailable" (total minus both) so the three add up to total rooms, as `wincloud` explains.
- No payment details, and no guest contact details in a briefing.
