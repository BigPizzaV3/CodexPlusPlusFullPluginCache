---
name: flexible-dates
description: "Find the cheapest day to fly within a date range by comparing several TravelYalla flight searches. Use when the travel dates are flexible, for example \"cheapest day in November\", \"any weekend next month\", \"±3 days\" or أرخص يوم للسفر / تواريخ مرنة."
---

# Flexible-date flight search

Tool: `search-flights`, called once per candidate date or date pair. Follow the `find-flights` skill for airport codes, date format, passengers, nationality, currency and language.

## 1. Choose candidate dates

Each search takes about 20–30 seconds, so search **at most 5 dates**, or 5 date pairs for a round trip. Tell the user which dates you will check before you start.

- "±N days": the requested date plus a spread around it, for example −2, −1, 0, +1, +2.
- "A month" or "any time in": spread the dates across the period. Prefer days the user mentioned, then weekdays, which are often cheaper (Tuesday to Thursday). Say that this is a sample, not every day.
- "Weekends": the next few Friday–Sunday pairs in the period, or Thursday–Saturday if that suits the user's region better.
- For a round trip, keep the user's trip length fixed and move both dates together.

Never include past dates.

## 2. Search

Call `search-flights` for each candidate with `limit: 3`. Use the same passengers, cabin, nationality and currency for every search so the prices are comparable.

If a search fails, retry it once. If it fails again, mark that date "no result" and carry on.

## 3. Compare

Show one table with a row per date and these columns:

- date or dates
- cheapest price and currency
- airline
- stops
- duration

Mark the cheapest date. If the cheapest option has worse stops or a much longer duration, mention the next-best date with a better flight.

## 4. Next step

Offer the full option list for the chosen date, following `find-flights` step 3, and give that date's booking link from the `find-flights` reference.
