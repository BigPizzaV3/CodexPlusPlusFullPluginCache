---
name: wincloud-cancellations
description: Use when a user asks about cancellations or no-shows, the cancellation rate, how late guests cancel, which room types or dates lose the most bookings, or how to reduce lost revenue from cancelled or unused bookings. Analyses WinCloud's cancellation, no-show and booking data.
---

# Cancellations and no-shows

Follow `wincloud-report-format`.

Resolve hotel names with `list_companies` before gathering data, and label every hotel by name in the output, as `wincloud` explains. For several hotels, use one row or series per hotel name.

## Gather

1. **Cancellations:** `get_reservation_analytics`, `report` = `cancellations`. Its date filter is the **cancellation date**. Each row has arrival date, cancelled date, days before arrival and rooms cancelled.
2. **No-shows:** same tool, `report` = `no-shows`. Its date filter is the **arrival date**.
3. **Bookings, for a rate:** `report` = `bookings`, with its **booking date** filter. It leaves out reservations that are now Cancelled or NoShow, so it is not the total that was booked. It still includes waitlisted and turned-away reservations, which carry no status, so say the rate's base may include them. To compute a rate:
   - Read the bookings and cancellations reports over a date range wide enough to cover every booking for the arrivals in question. If you can't, give counts, not a rate, and say why.
   - Keep only rows from all three reports that arrive in the same window.
   - Total = rooms on the bookings rows (booked plus availed) + rooms cancelled + no-show rooms.
   - Cancellation rate = rooms cancelled ÷ total; no-show rate = no-show rooms ÷ total.
4. Read every page and add the rows up. Say if you stopped early.

## Measure

- **Counts:** rooms cancelled, no-show rooms, reservations affected.
- **Lead time of cancellations:** bands (same day, 1–3, 4–7, 8–14, 15+ days before arrival). Late cancellations (7 days or fewer, the first three bands) are the costly ones: they leave rooms hard to resell.
- **Where it concentrates:** by room type, arrival month or week.
- **Reasons and sources:** `get_reservation` shows the cancellation reason and source for one booking. For a pattern, sample 5–10 recent cancellations from `search_bookings` (`cancelledFrom`/`cancelledTo`, status `Cancelled`), and say it is a sample.

## Show

- **Headline:** rooms cancelled, the rate if it can be computed, and the main pattern (for example "40% were cancelled within a week of arrival").
- **Chart:** cancellations by lead-time band (bars); trend by week if the range is long.
- **Table:** top room types or dates, with rooms cancelled and, where possible, rate.
- **Suggestions**, as options for the manager to consider, not decisions: tighter cancellation terms for the heaviest bands, reconfirmation for late arrivals, overbooking only with the hotel's own policy. Say these depend on the hotel's contracts and policy.

## Limits

- Analytics rows name no guests and no reservation numbers.
- A cancellation date and an arrival date answer different questions; always say which you used.
- Don't tell the user to take payment, refund or change a booking. WinCloud tools here are read-only.
