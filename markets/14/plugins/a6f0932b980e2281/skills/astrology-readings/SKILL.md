---
name: astrology-readings
description: Answer astrology questions with FreeAstroAPI's calculation tools. Use when someone asks about a birth chart, horoscope, transits, compatibility, the Moon, Vedic astrology, BaZi or numerology.
---

# Astrology readings with FreeAstroAPI

## Gather only what the calculation needs

- A birth chart needs the birth date, the birth time and the birthplace. Ask for the time if it is missing, and accept "I don't know".
- When the birth time is unknown, say that houses, the Ascendant and the Moon's exact position are approximate. Pass `time_known: false` (or `time_unknown: true` for chart comparisons).
- A sign horoscope needs only the zodiac sign. Don't ask for birth details unless the person wants a personal reading.
- Don't repeat birth details back more than needed, and don't ask for details about other people beyond what a comparison requires.

## Pick the tool

| Question | Tool |
| --- | --- |
| Ambiguous or uncommon birthplace | `search_city`, then pass its lat/lng and timezone on |
| Birth chart, Sun, Moon or rising sign | `calculate_natal_chart` |
| Horoscope for a sign | `get_sign_horoscope` |
| Horoscope from a birth chart | `get_personal_horoscope` |
| What's influencing a chart now or on a date | `get_current_transits` |
| Compatibility of two people (Western) | `compare_birth_charts` |
| Birthday-year outlook | `calculate_solar_return` |
| Moon phase, or the next new or full Moon | `get_moon_phase` |
| Vedic chart, lagna, nakshatras | `calculate_vedic_chart` |
| Current Vedic planetary period | `get_vimshottari_dasha` |
| Vedic marriage matching | `check_vedic_compatibility` |
| Tithi, nakshatra or Rahu Kalam for a day | `get_panchang` |
| Chinese Four Pillars | `calculate_bazi_chart` |
| Life path and name numbers | `calculate_numerology_profile` |

## Present the results

1. Lead with the calculated facts from the tool result: signs, degrees, dates and scores.
2. Then give the interpretation, and label it as interpretation.
3. Frame readings as entertainment and self-reflection. Never present them as certain predictions.
4. Don't base medical, legal, financial, hiring or relationship decisions on a chart. Suggest a qualified professional when someone asks for that kind of advice.
5. Decline requests for lottery numbers, bets or other gambling picks without calling a tool.
6. If a tool returns an error, explain what was missing or invalid and ask for it, rather than guessing values.
