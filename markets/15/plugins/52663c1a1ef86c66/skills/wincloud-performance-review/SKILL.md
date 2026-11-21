---
name: wincloud-performance-review
description: Use when a user asks for a performance review, management or owner report, summary, dashboard, scorecard or "how did we do" for a period such as a week, month, quarter or year to date, for one hotel or all their hotels, or asks to compare hotels or compare one period with another. Builds a KPI and chart report from WinCloud occupancy and revenue, bookings, cancellations, no-shows and rates, and ends with what to act on. Use it even when the user doesn't say "report" or "chart".
---

# Performance review

Follow `wincloud-report-format`. This is the report an owner or area manager reads: a few KPIs, a few charts, and what to do next.

Resolve hotel names with `list_companies` before gathering data, and label every hotel by name in the output, as `wincloud` explains. For several hotels, use one row or series per hotel name.

## Scope

- **Locations:** the hotel the user names, or every location they can see when they say "my hotels", "both" or "all". Repeat the gathering below per location.
- **Period:** exact `yyyy-MM-dd` dates; say which you used. For "versus last year" or "versus last quarter", use the same dates a year earlier or the previous period of equal length.

## Gather (per location, per period)

1. **Bookings made, by month:** `search_bookings` with `startDate` and `endDate` for each month, `pageSize` 1. Take the count from the first line ("N booking(s)"). This counts every status, by booking date.
2. **Net bookings, rate and lead time:** `get_reservation_analytics`, `report` = `bookings`. Read every page (up to 15). Each row is one reservation still on the books (waitlisted and turned-away reservations are still included and carry no status, so say the figures may include them); rooms are booked plus availed, as `wincloud` explains. Work out rooms, ADR (weighted by rooms), lead-time bands (the bands in `wincloud-pickup-pace`) and the top room types.
3. **Cancellations:** same tool, `report` = `cancellations`. Dated by the cancellation date. The first line gives the number of reservations; for rooms, read every page and add them up.
4. **No-shows:** same tool, `report` = `no-shows`. Dated by the arrival date. Count reservations and rooms as for cancellations.
5. Say in the KPI labels whether each figure counts reservations or rooms.
6. **Actual occupancy and revenue:** `get_room_performance` with `fromDate` and `toDate` = the period (at most 366 days) and `comparisonPeriod` matching the comparison asked for. Gives occupancy %, ADR, RevPAR and revenue from the night audit, by room type.
7. Run independent calls together. For a rate of cancellation or no-show, use the method in `wincloud-cancellations`; without it, give counts.

## Show

- **Headline:** which hotel or period leads, by how much, and the one thing that stands out.
- **KPI row, per hotel:** occupancy %, RevPAR and room revenue (when `get_room_performance` is available), bookings made, net bookings, cancellations, no-shows, ADR, average lead time.
- **Charts, one comparison each:**
  - bookings made per month, hotels side by side (grouped bar);
  - cancellations and no-shows per hotel, in separate charts because their date bases differ;
  - top room types per hotel (horizontal bars);
  - lead-time bands (bars), when you read the analytics rows.
- **Table:** one row per hotel with the KPIs, plus the comparison period when there is one.
- **What to look at:** up to 3 items the numbers support, for example a hotel whose no-shows are well above the other's, or a month that dipped.

## Limits

- Bookings made counts every status; net bookings leave out cancelled and no-show reservations. Say which one the headline uses and don't subtract one from the other.
- Revenue comes only from `get_room_performance`, for past dates. The analytics ADR is the booking's rate, not room revenue ÷ nights; label which ADR each figure is. No payment figures come from these tools.
- If you stopped before the last page, say the figures cover only what you read.
