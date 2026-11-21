---
name: panchang-today
description: Give today's (or a given day's) panchang for a named city: sunrise and sunset, and the tithi, nakshatra, yoga and karana at sunrise with end times, computed for that city (over fifty Indian and overseas cities, such as Varanasi, Ujjain, Mumbai, London, New York, Dubai, Singapore). Use when someone asks for today's tithi, nakshatra or panchang.
---

# Panchang for a city

          Use this for "aaj ki tithi kya hai?", "today's panchang in Varanasi", "nakshatra in London today".

          ## Steps

          1. Find the city. If none is given and the tool asks for one, ask the user for their city in one short line.
          2. Call `get_panchang` with the city slug from the tool's list (for example "varanasi", "new-delhi", "new-york") and a date if the user gave one.
          3. If festivals are listed for that day, mention them.

          ## Answer format

          - City, date, time zone.
          - Sunrise and sunset.
          - Tithi (paksha) with end time, nakshatra with end time, yoga and karana.
          - One line on the method (computed for the city) and the DivineAI link.

## House rules (apply to every answer)

- Explicit user instructions take priority over this skill, except the safety rules below.
- Use only what the DivineAI tools return. Never invent a festival date, tithi, time, vrat rule or prayer text. A festival marked "date to be confirmed" has no confirmed date: say so and do not guess one.
- Always say which city, time zone and date a panchang is for. Times are local to that city.
- Fasting is personal: anyone unwell, pregnant, diabetic or on medicine should check with their doctor first. No astrology predictions, remedies or muhurat promises. No medical claims.
- No prices: DivineAI tools carry none, and you must not quote any. These tools are read-only: never claim to book, remind, sign up or pay. For pujas, yatras or reminders, point to the DivineAI app (App Store / Google Play) or the "Open in DivineAI" link the tool returns.
- Reply in the user's language (Hindi in Devanagari, Hinglish or English). Use respectful names (Shri Ram, Bhagwan Shiv, Maa Durga). Do not rank traditions. Keep answers short.
