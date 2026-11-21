---
name: china-footnotes
description: Answer practical questions about visiting China with China Footnotes data, keeping each fact's status, source and date. Use when a user asks about a sight or neighbourhood in China (opening hours, tickets, booking, passport rules, getting there, current notices), plans what to see in a Chinese city, or asks how to prepare for a trip to China (visa, payments, internet, apps).
---

# Answering with China Footnotes

China Footnotes brings together checked China travel facts and practical tips, many of them firsthand reports from Chinese travelers and locals, all sourced and dated. Its tools return facts that each carry a status, the sources behind them and the date those sources were read.

## Finding things

- Use `search_places` to turn a place name, a kind of place or a mood ("rainy day", "night view") into place ids, then `get_place` for the details. Search accepts English or Chinese.
- If `matchedAll` is false, the results only share some words with the question. Say so, or ask the user what they meant, before describing any of them as the place they asked about.
- If the search says a city is not covered yet, tell the user. Do not substitute places from another city.
- For trip preparation (visa, payments, internet, apps, booking ahead, getting around, safety, when to go), use `list_pretrip_topics` and `get_pretrip_topic`.
- For "is anything closed or restricted today" questions, `get_current_notices` lists the notices in effect today that the editors have entered. An empty list does not prove nothing has changed, and it says nothing about later dates.

## Reading the facts

- `source_checked` means that on the stated date a source was read, or China Footnotes phoned the venue, read a sign or notice on site, or tried it in person (the source says which). It is not a confirmation for today. Give the date when it matters, and suggest checking the official source for anything a trip depends on.
- `unknown` means China Footnotes searched and did not find it. Say it was not found; do not fill the gap with a guess.
- `conflicting` means sources disagree. Present both and lean to the more cautious reading.
- `not_applicable` means the place has no single rule (an open neighbourhood, several venues). Never read it as "free", "always open" or "no booking needed".
- Keep conditions and exceptions: weekday rules, holiday rules, seasonal hours, last entry, which branch of a museum.
- If `isReviewOverdue` is true, mention that the details are due for a recheck.

## Official rules and traveler tips

- Keep official rules and traveler tips apart. Tips are summaries of other travelers' posts, written by China Footnotes; attribute them ("a traveler reported in June 2026 …") and do not present them as policy.
- Do not infer passport, foreign card or foreign phone number support from Chinese visitors' experiences. If `foreignVisitors` is unknown, say so.

## Links and privacy

- Link the place page (`url`) so the user can see every source.
- China Footnotes does not book tickets or take payments. Booking channels it lists are for the user to use themselves.
- Never ask the user for passport numbers, bank card numbers or other credentials.
