---
name: study-budget
description: Plan, compare or adjust the cost of studying in Germany with the StayinDE budget board (monthly, yearly, whole-stay totals and the amount to save vs. the blocked account).
---

# Study budget in Germany

Use this when someone plans to study (or is studying) in Germany and asks what it costs, how much to save, how much the blocked account (Sperrkonto) needs, or how a choice (city, housing, eating out, gym, travel, flights home, scholarship, part-time work) changes the budget.

## Which tool

- `open_budget_board`: when the user wants to plan or play with a budget. It shows the interactive board. The user can also open it themselves as the "Budget Board" tab beside the conversation.
- `calculate_budget`: for a quick number or a comparison ("Munich vs Leipzig", "what if I cook instead of eating out"). Call it once per scenario and compare the results.

## Filling in the answers

- Pass only what the user said or clearly implied; leave the rest out. Defaults are a two-year master in a shared flat with middle-of-the-road habits.
- Always pass `language` as the BCP 47 code of the language the user writes in (Chinese → `zh-TW`; the board shows Traditional Chinese).
- City: use the listed keys (`muenchen`, `berlin`, `leipzig`, …). For a German city not in the list use `other` (national average) and say so.
- Months: 6 (exchange, language course), 12, or 24 (two-year master). For a three-year bachelor, use 24 and tell the user the board covers two years.
- Flights home: set `flightEurPerTrip` from where home is when the user says it (typical return fares from Germany: Turkey or Morocco €250–400, India or Pakistan €600–900, East Asia €900–1,300, Latin America €900–1,400). Say it is a rough figure.
- Rent: pass `rentEur` only when the user already has a place and gives the real rent.

## Talking about the result

- The board already shows the numbers. Don't repeat them line by line; answer what the user asked, pick out the two or three lines that matter, and suggest which dial to try.
- When the board is open, its current state arrives as context ("Budget board the user is adjusting…"). Use those numbers, not older ones.
- "Save before you go" includes a city buffer and is a recommendation. The legal minimum is what the German mission asks for (in 2026: €992 a month, €11,904 a year for most student visas). Tell the user to confirm the amount with their mission.
- Part-time work lowers what the student pays each month, never the amount to save, because a visa cannot count on future wages.
- These are estimates from public 2026 prices, not financial or visa advice. Method and sources: https://rechner.stayinde.de/methode

## Out of scope

Opening a blocked account, booking housing, visa applications, and costs outside Germany. Say so and answer from general knowledge if you can, without calling the tools.
