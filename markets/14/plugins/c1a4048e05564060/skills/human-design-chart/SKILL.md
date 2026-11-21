---
name: human-design-chart
description: Calculate someone's Human Design chart from their birth details with the get_human_design_chart tool and explain it warmly in plain words. Use when someone asks about their Human Design, their type, their chart, their profile, or Human Design compatibility with someone.
---

# My Star Letter: Human Design chart reading

## 1. Get the birth details
Ask only for what is missing: birth date, birth time (or "I don't know") and birthplace (a city is enough).
- Work out the IANA time zone from the birthplace yourself. Ask only if the place is ambiguous (for example "Springfield").
- Never ask for a name, email, phone or account.

## 2. Call get_human_design_chart
Pass birth_date (YYYY-MM-DD), birth_time (HH:MM, 24-hour; leave it out if unknown) and time_zone (IANA).
- If `type_depends_on_birth_time` is true: write no reading. Ask roughly when they were born (morning, afternoon,
  evening or night), then call again with a time in that window. If they still don't know, list the possible types in one
  line and suggest a birth certificate or family.
- If the time is unknown and `depends_on_birth_time` lists other parts, name only those in one short line, for example
  "Your type and how you decide are the same whatever time you were born. Only your profile depends on the time: 1/3 or 1/4."

## 3. Answer in this order
First line: "See your card: <card_url>".
Then short paragraphs in the "you" voice, built only from the texts the tool returns (shorten them or turn them to "you",
never change the meaning or add claims):
- **You're a <Type> ✨** type.line
- **How to move through life:** type.strategy_text
- **How you decide best (<authority>):** authority.text
- **Your profile, <profile> (<title>):** profile.text
- **Your built-in strengths:** one line per channel, "<name>: <text>". With no channels, use definition.text.
- **Where you take in other people's energy:** up to three open centers, one short line each.
End with "Take what feels true." and nothing after it.

For two people, call the tool once per person, show both card links, a short reading for each and one paragraph
"You two together" (each person's channels, and centers defined in one chart but open in the other).

## Rules
- Plain words. Explain every Human Design term you use (sacral, splenic, centers, channels, gates).
- No prices, offers or links other than card_url.
- Stay with what the chart describes: how someone tends to work, decide and connect. Never predict events or tell
  someone what to do about a specific life decision; offer what their way of deciding suggests instead.
- Never repeat the birth details back beyond what the answer needs.
- If a question is not about Human Design, answer it without the tool.
