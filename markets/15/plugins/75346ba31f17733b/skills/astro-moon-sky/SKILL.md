---
name: astro-moon-sky
description: "Use for the Moon and the sky: today's Moon phase and sign, the next new and full Moon, Mercury retrograde and other retrogrades, eclipses, and the sign of every planet on any date."
---

# Moon and sky

## 1. Get the sky

Call `get_moon_and_sky` with `date` (the date the user asks about as YYYY-MM-DD, or today's date for the user) and `started_from` as the tool describes it.

For every retrograde period or eclipse in a whole year, call `get_horoscope` with `period` `year`, a date in that year and the user's sign (any sign works when you don't know it: the dates are the same for every sign), and use its `retrogrades` and `eclipses`.

Use only the data the tools return. Times are in UTC; convert them only when you know the user's time zone.

## 2. Write the answer

- Answer the question first, in one or two sentences, for example: "The Moon is full in Cancer on December 24, 2026 (01:34 UTC), and Mercury is not retrograde."
- Then add only what helps: the phase's meaning, when the Moon changes sign that day, the next new or full Moon, retrogrades, Mercury retrograde dates or the next eclipse.
- For questions about a planet's sign, give the sign and degree from `planets`.
- Keep astrological meanings short and light: they are traditions for reflection, while the positions are real astronomy.
- Reply in the user's language.

## 3. Close

Offer one next step, for example: "Want to know what this Full Moon means for your sign?"
