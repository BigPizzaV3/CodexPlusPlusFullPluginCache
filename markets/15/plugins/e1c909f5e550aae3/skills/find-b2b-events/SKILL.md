---
name: find-b2b-events
description: Use this when the user wants to find, compare or look up upcoming B2B trade shows, industry conferences or expos by topic, country, continent, event type or date. Explains which Exporb Events tool to call, how to turn dates and places into filters, and how to present the results. Not for consumer events, concerts, sports or ticket purchases.
---

# Find B2B trade shows

Use the Exporb Events tools to answer questions about upcoming B2B trade shows, industry conferences and exhibitions.

## Choose the tool

1. Coverage or ranking question ("which countries have the most trade shows?") -> `list_countries`. It takes no input.
2. Finding events -> `search_events`.
3. Details of one named event -> call `search_events` first to get its `slug`, then `get_event` with that slug. Do not guess slugs.

## Set the filters in `search_events`

- `query`: the topic or part of the event name, for example `robotics`, `fintech` or `packaging`.
- `country`: the English country name, for example `Germany` or `United Arab Emirates`.
- `continent`: for example `Europe` or `Asia`.
- `event_type`: for example `Trade Show` or `Conference`.
- `date_from` and `date_to`: ISO dates `YYYY-MM-DD`. Convert phrases such as "next quarter", "in November" or "between January and March" using today's date. Leave `date_from` empty to start from today.
- `include_past`: set to `true` only when the user asks for events that already ended.
- `limit`: up to 10 results per page. Use 10 when the user wants a list.
- `page`: pages 1 to 3 exist. Ask the user to narrow the topic, country or dates instead of paging further.

## Present the results

- List events soonest first with name, dates, city, country and the Exporb link from the result.
- Report only what the tools returned. Never invent events, dates, venues or websites.
- If nothing matches, say so and suggest a broader topic, another country or a wider date range.
- Remind the user to confirm dates and venue on the official event website before booking travel or spending money.

## Out of scope

The tools only read a public events directory. They cannot sell tickets, book travel or register anyone for an event, and they are not meant for consumer events, concerts or sports.
