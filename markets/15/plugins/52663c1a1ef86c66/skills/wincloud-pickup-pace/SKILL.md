---
name: wincloud-pickup-pace
description: Use when a user asks whether bookings are ahead or behind, about booking pace or pickup, how many bookings came in per day or week, lead time (how far ahead guests book), or how demand compares with the same period last year or last month. Measures booking activity from WinCloud's reservation analytics.
---

# Pickup and pace

Follow `wincloud-report-format`. Pace answers "are we booking faster or slower than usual?".

Resolve hotel names with `list_companies` before gathering data, and label every hotel by name in the output, as `wincloud` explains. For several hotels, use one row or series per hotel name.

## Pickup: bookings made over a period

1. Call `get_reservation_analytics` with `report` = `bookings`, `startDate`/`endDate` = the booking dates the user cares about (the date filter is the booking date). Add `roomTypeId` for one room type; ids come from `get_rate_plans`.
2. Each row is one reservation still on the books (cancelled and no-show reservations are left out; waitlisted and turned-away reservations are still included and carry no status, so say the figures may include them): booked date, arrival date, rooms (booked plus availed, as `wincloud` explains), lead time in days, ADR. Read every page and add up. Say if you stopped early.
3. Total **room-nights are not available** from these rows (one row per reservation, not per night). Report **rooms** and **reservations**, not room-nights.
4. Group by booked date for daily or weekly pickup; by arrival month for what the bookings are for; by lead-time band (booked after arrival, 0–7, 8–14, 15–30, 31–60, 61+ days) for how far ahead guests book.

## Pace: compared with another period

1. Pick two periods of equal length, the current one and the comparison (same dates last year, or the previous period). Say which.
2. Compare like with like: bookings made in each period, **for the same arrival window** (for example, rooms in the last 30 days for next January, versus the same 30 days a year earlier for the January before). Filter rows by arrival date after reading them.
3. Show the difference as a number and a percentage, and call it ahead or behind. If the base is small (under about 20 reservations), say the comparison is not reliable.

## Show

- **Headline:** rooms taken in the period, the change against the comparison, and the main reason visible in the data (a lead-time shift, a room type).
- **Chart:** bars for rooms per day or week, with the comparison period as a second series (green).
- **Second chart or table:** lead-time bands, and top room types or plans by rooms.
- **Caveats:** the hotel, both periods, the date fields used, pages read, and that bookings may include waitlisted and turned-away reservations.

## Limits

- The `bookings` report already leaves out reservations that are now Cancelled or NoShow, so its pickup is **net** of them. Don't subtract the `cancellations` report as well; that counts them twice. Gross pickup (including bookings later cancelled) can't be rebuilt, because cancellation rows carry no booked date.
- No guest names or reservation numbers come back from analytics; use `search_bookings` for those.
- Past trends don't guarantee the future. Don't call a pace figure a forecast.
