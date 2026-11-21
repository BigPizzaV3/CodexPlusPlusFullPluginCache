---
name: visit-a-swiss-attraction
description: Plan a visit to a named Swiss attraction or excursion destination with the Swiss Activities tools — Jungfraujoch, Titlis, Pilatus, Rigi, Rhine Falls, Gornergrat and more: hours, tickets and prices, the train there and the weather. Use when someone asks how to get to, what it costs or when to visit a specific attraction in Switzerland.
---

# Visit a Swiss attraction

1. **The attraction:** `get_point_of_interest` with its name — what it is, the operating or opening hours (first and last ride for mountain railways), whether it runs today, and the tickets we sell with their `id`.
2. **The day:** `get_weather` for the place and date; on the summit, clouds matter more than rain.
3. **Tickets:** `check_availability` with the ticket `id`, the date and the group for free times and the group price.
4. **Getting there:** `plan_journey` from where the user starts to the valley station, arriving well before the last ride up.
5. **Answer** with the day in order — train, ride up, time on top, ride down — the prices from the tools and the booking link. Never invent hours or prices.
