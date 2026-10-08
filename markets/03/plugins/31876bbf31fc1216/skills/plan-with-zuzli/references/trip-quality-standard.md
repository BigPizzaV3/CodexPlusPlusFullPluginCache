# Trip quality standard

Use the Paris family itinerary as the benchmark principle: a good trip is a sequence of usable moments with logistics and decisions, not a sparse list of famous places. The benchmark combined rich stops, short transitions, food, neighbourhood walks, hotel and luggage actions, hard deadlines, alternatives, and live changes without losing the day's story.

## Design the real day

- Start from the actual arrival point, hotel, or previous commitment.
- End at the real evening destination, hotel, station, airport, or next booking.
- Add check-in, luggage, breaks, meals, shopping errands, and transfer preparation when operationally important.
- Cluster places into a directional route. Avoid repeated crossings, unnecessary loops, and “back to the same area later” unless a fixed time requires it.
- Use transit or rideshare when it materially saves time or energy. Do not choose a mode only because two points look close on a map.
- Use realistic visit, queue, meal, and transition durations. Avoid false minute-level precision when conditions are uncertain.
- Protect tickets, reservations, closing times, sunset, transport departures, and airport targets with explicit buffers.
- Balance ambition with the group's ages, walking tolerance, weather, jet lag, meal rhythm, and desired pace.

## Research and verification

For every time-sensitive trip, browse current sources. Search in the local language when useful.

| Fact | Preferred evidence |
|---|---|
| Place identity and official name | Official site, official listing, authoritative map listing |
| Address and map position | Official contact page plus current mapping data |
| Opening on the trip date | Official calendar, ticketing page, or venue notice |
| Temporary closure or renovation | Official alerts and recent authoritative local notices |
| Reservation or ticket need | Official booking system; reputable reservation platform as support |
| Train, metro, road, or airport disruption | Official operator or authority service notice |
| Walking and travel duration | Current routing data for the selected mode |
| Weather-sensitive choice | Forecast close to the date; seasonal norms only for early planning |

Check the exact date, weekday, local timezone, holidays, seasonal schedules, last admission, kitchen hours, and special-event exceptions. Record uncertainty instead of converting it into a fact.

Revalidate all time-sensitive stops close to travel. Use approximately 72 hours as the default checkpoint, then recheck critical same-day facts during the trip.

## Make every stop useful

Populate every current-schema field that materially improves the experience. At minimum, aim to provide:

- Stable unique ID and planned start/end.
- Exact title, suitable emoji, subtitle, and category.
- Verified address, coordinates where supported, and a precise place lookup query or place ID.
- A short story explaining why the stop belongs in this trip.
- Specific “what to do” guidance, not a generic description.
- “What to order” for food and drink stops when useful.
- A practical tip covering entrance, queue, children, timing, viewpoint, or exit direction.
- Realistic duration, booking note, hard-deadline status, and meaningful fallback links.
- Official and map links supported by the schema.
- A place-specific image strategy, alt text, and correct attribution behavior. Prefer Google Places or official imagery; never copy an arbitrary web image.

Use the trip's locale for visible text even when historical schema fields end in `_he`.

## Use alternatives deliberately

Create a fallback only when it solves a real failure mode: closure, weather, long queue, dietary issue, fatigue, or missed timing. Place it near the same route and make the switch rule explicit. Do not double the itinerary with generic backup attractions.

## Run the quality audit

1. Plot the ordered stops mentally or with routing data and look for backtracking.
2. Recalculate each transition using the intended mode.
3. Check that arrival plus visit duration plus travel fits before the next hard deadline.
4. Check meal timing, breaks, children, accessibility, luggage, and end-of-day return.
5. Check duplicate or ambiguous places, duplicate coordinates, wrong branches, and map targets that land at a generic city or station.
6. Check that every stop has trip-specific content rather than boilerplate.
7. Check that every user must-do appears and every exclusion is respected.
8. Validate the complete trip, inspect warnings, save, and compare the canonical returned itinerary with the approved design.
