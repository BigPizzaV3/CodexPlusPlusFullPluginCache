---
name: sky-keepsake
description: Real Moon phases for any date (birthdays, anniversaries, two dates whose moons complete each other, monthly moon calendars) and printable star map or moon posters of the real sky over a city, with find_moon_phase, generate_star_map and generate_moon_poster.
---

# Moon & Star Map

Pick the tool from the request:

- **find_moon_phase**: "what was the moon on my birthday", "moon phase tonight", "do our moons complete each other / make a full moon", "moon calendar for July". Pass `dates` as `YYYY-MM-DD` (add `THH:MM` if the user gives a time), `labels` for names, `month` as `YYYY-MM` for a calendar, and `city` when the user names a place (it sets the time zone and hemisphere). With no dates and no month it answers for right now.
- **generate_star_map**: a star map or night-sky poster for a date and place. Needs `city` and `date`; pass `time` (local HH:MM) when given, otherwise 21:00 is used and the reply says so. Optional `title`, `message`, `theme` (midnight, black, paper, ink), `constellations`, `labels`, `show_moon`.
- **generate_moon_poster**: a printable moon print: `kind=moon` (one date), `kind=pair` (two dates, e.g. a couple), `kind=year` (lunar calendar of `year`).

Rules:

1. Never ask for or pass latitude/longitude. Use the city name, adding a state or country when it is ambiguous ("Paris, Texas", "Portland, Maine"). Say which city was matched.
2. Convert spoken dates to `YYYY-MM-DD` yourself ("July 14, 1998" -> `1998-07-14`). Ask only if the year is missing.
3. Report the numbers from the tool as given (phase, illumination %, moon age, exact phase times with the time zone). For two dates, relay the verdict and the honest explanation; it is a playful idea, not astrology.
4. Share the PDF/SVG download links and the share page link for posters. Mention that posters are decorative keepsakes, not for navigation.

Do not use this skill for horoscopes or astrology readings, eclipse predictions, planet positions, tides, moonrise times, or telescope pointing.
