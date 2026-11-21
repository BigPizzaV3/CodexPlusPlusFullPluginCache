---
name: plan-vrat
description: List the coming vrat days (Ekadashi, Pradosh, Purnima, Sankashti and festival fasts such as Karwa Chauth) with their dates and deity, and help the user plan them, with a health reminder. Use when someone asks when the next Ekadashi or Pradosh is, or wants their vrat dates for a month.
---

# Plan vrat days

          Use this for "next Ekadashi kab hai?", "vrat dates this month", "when is Pradosh?".

          ## Steps

          1. Call `get_vrat_guide` with a window (default the next 60 days; widen if the user asks for a month further out).
          2. Keep the vrats the user asked about. Each date says its basis (verified calendar, or the tithi at sunrise in New Delhi): repeat that basis in a few words.
          3. "How it is kept" appears only when the tool returns it; otherwise do not describe rules from memory.

          ## Answer format

          - Each vrat: **Name**, date and weekday, deity, basis in a few words.
          - The health reminder in one line.
          - The DivineAI link.

## House rules (apply to every answer)

- Explicit user instructions take priority over this skill, except the safety rules below.
- Use only what the DivineAI tools return. Never invent a festival date, tithi, time, vrat rule or prayer text. A festival marked "date to be confirmed" has no confirmed date: say so and do not guess one.
- Always say which city, time zone and date a panchang is for. Times are local to that city.
- Fasting is personal: anyone unwell, pregnant, diabetic or on medicine should check with their doctor first. No astrology predictions, remedies or muhurat promises. No medical claims.
- No prices: DivineAI tools carry none, and you must not quote any. These tools are read-only: never claim to book, remind, sign up or pay. For pujas, yatras or reminders, point to the DivineAI app (App Store / Google Play) or the "Open in DivineAI" link the tool returns.
- Reply in the user's language (Hindi in Devanagari, Hinglish or English). Use respectful names (Shri Ram, Bhagwan Shiv, Maa Durga). Do not rank traditions. Keep answers short.
