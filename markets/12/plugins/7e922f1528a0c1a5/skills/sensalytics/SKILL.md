---
name: sensalytics
description: Answer questions about store visitors, footfall trends and live occupancy using sensalytics data. Use when the user asks how busy a location is or was, compares days or weeks, or wants a footfall summary.
---

# Footfall analysis with sensalytics

Use the sensalytics tools to answer questions about visitor numbers at the user's locations.

## Pick the right tool

- **Right now or today so far** ("How full is the Berlin store?", "How many visitors so far today?") → `get_current_location_occupancy_and_visitors`
- **Past days** ("yesterday", "last week", "last Monday vs Tuesday") → `get_daily_location_metrics`
- **"Which locations do I have?"** → `get_current_location_occupancy_and_visitors` with no filter, then list the `locationName` values
## Dates

`get_daily_location_metrics` only accepts explicit dates (`YYYY-MM-DD`), not ranges.

1. Convert every relative reference to explicit dates, counting from today:
    - "yesterday" → one date
    - "last week" → the 7 days Monday–Sunday of the previous week
    - "last 3 days" → the 3 days before today
2. If the period is vague ("recently", "a while ago"), ask the user which days they mean before calling.
3. For comparisons, request all dates in one call.
## Locations

- Refer to locations by `locationName`, never by internal IDs.
- If the user names a location that doesn't match exactly, pick the closest match and say which one you used. If several match, ask.
- If a user has locations from several clients, group them by `clientName`.
## Presenting results

- Lead with the answer in one sentence ("Berlin Mitte had 1,284 visitors yesterday, 9% more than the day before.").
- For comparisons, add a small table: location, period, visitors, change in %.
- For live data, show occupancy as "42 of 120 (35%)" and mention if a location is closed, using `openFromBusinessLocal` / `openToBusinessLocal`.
- Round percentages to whole numbers. Don't invent metrics the tools didn't return.
## Don't

- Don't guess numbers when a tool call fails. Say the data isn't available and suggest trying again.
- Don't call `get_daily_location_metrics` for today. Use `get_current_location_occupancy_and_visitors`.
- Don't make claims about why footfall changed (weather, promotions) unless the user gives that context.
 