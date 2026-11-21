---
name: plan-a-day-in-switzerland
description: Plan a day out, a family outing or a short trip in Switzerland with the Swiss Activities tools — activities and tickets, free places with opening hours, hikes, weather and public-transport connections. Use when someone asks what to do somewhere in Switzerland, wants ideas for kids or bad weather, or wants a day planned.
---

# Plan a day in Switzerland

1. **Know the frame.** Place, day, who comes along (children and their ages), budget, car or public transport. Ask only for what is missing and matters; a place and a day are usually enough to start.
2. **Check the weather first** with `get_weather` for the place and day. Rain or a warning → prefer `indoor` activities and indoor places; sun → outdoor activities and hikes.
3. **Collect options in parallel:**
   - `search_activities` for bookable activities and tickets (`for_families` with children, `indoor` in bad weather, `max_price_chf` for a stated budget).
   - `search_places` for free places — `kids` for children, `museums` on rainy days, `viewpoints` or `mountain-railways` for views.
   - `search_hikes` when walking fits — `for_kids` for theme trails, `trail_class: wanderweg` for easy hikes, `max_minutes` for the time available.
   - `get_point_of_interest` when the user names an attraction (Titlis, Pilatus, Rhine Falls): operating hours, whether it runs today and its tickets.
4. **Check the facts before recommending:** age limits against the children's ages, `rain_ok` and `setting` against the weather, opening hours with `get_place_details`, free start times and the group price with `check_availability`.
5. **Get there:** `plan_journey` from the start point to the first stop and between stops, in Swiss local time.
6. **Answer** with a short plan in time order: what, when, how long, what it costs, how to get there, and the link for every bookable item. Never invent prices, times or opening hours — a value the tools do not return is unknown; say so and link the page.
