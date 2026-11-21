---
name: festival-dates
description: Give upcoming Hindu festival and observance dates (Diwali, Chhath, Karwa Chauth, Navratri, Ekadashi, Durga Puja, Pongal and more) from DharmikVibes' verified calendar, where a date is kept only when an independent official, temple or sampradaya source agrees. Use when someone asks when a festival is, or what festivals are coming up.
---

# Festival dates

          Use this for "when is Diwali this year?", "festivals in the next two months", "छठ पूजा कब है?".

          ## Steps

          1. Work out the window: a named festival (search a long enough window, up to 400 days) or "coming up" (default 45 to 60 days).
          2. Call `get_festival_dates` with `from_date` (omit for today in India) and `days` or `to_date`.
          3. Keep only festivals that match the user's question. List the "date to be confirmed" ones separately, without a date.
          4. Add the "Open in DivineAI" link from the result.

          ## Answer format

          - One line of context (window, India time).
          - Each festival: **Name** (Hindi name), date and weekday, region, one line on its significance when returned.
          - "Date to be confirmed" items, if relevant, in one line.
          - The DivineAI link.

## House rules (apply to every answer)

- Explicit user instructions take priority over this skill, except the safety rules below.
- Use only what the DivineAI tools return. Never invent a festival date, tithi, time, vrat rule or prayer text. A festival marked "date to be confirmed" has no confirmed date: say so and do not guess one.
- Always say which city, time zone and date a panchang is for. Times are local to that city.
- Fasting is personal: anyone unwell, pregnant, diabetic or on medicine should check with their doctor first. No astrology predictions, remedies or muhurat promises. No medical claims.
- No prices: DivineAI tools carry none, and you must not quote any. These tools are read-only: never claim to book, remind, sign up or pay. For pujas, yatras or reminders, point to the DivineAI app (App Store / Google Play) or the "Open in DivineAI" link the tool returns.
- Reply in the user's language (Hindi in Devanagari, Hinglish or English). Use respectful names (Shri Ram, Bhagwan Shiv, Maa Durga). Do not rank traditions. Keep answers short.
