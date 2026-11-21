# Agencies, forecasts and events

Forecasts are planned buys that are not open solicitations yet. Events come from the public G2X events calendar. Registration happens on the organizer's site, not in G2X. Keep listed speakers separate from likely attendees. A sponsorship or speaker listing does not prove that a specific person will be in the room. Preserve unknown dates, times, time zones and prices as unknown.

For agency spending questions, use the award query in [Awards, vehicles and recompetes](awards-vehicles.md) and the company ranking in [Companies](companies.md).

### `g2x_forecast_scan`

Find agencies' published procurement forecasts.

- Inputs: `agency` (agency acronyms, up to 5, such as `DHS` or `VA`); `naics_codes` (6-digit exact, shorter means prefix); `keyword`; `status` (up to 5); `fiscal_year`; `award_date_after` (default today, so only buys still coming), `award_date_before`; `include_awarded` (also list forecasts already awarded, cancelled or exercised as an option, and past award dates); `page` (a result's next cursor names the next page); `limit` (1 to 50, default 10).
- Output: forecast rows, each linked to its G2X record, with the total and the next page.
- Plan: all plans. Read only. On the research endpoint: yes.
- Example: `{"agency": ["DHS"], "keyword": "cloud", "fiscal_year": 2027}`

### `g2x_search_events`

Search upcoming conferences, industry days, matchmaking and agency events on the G2X calendar.

- Inputs: `query` (words from the title, organizer or location); `start_date_from` (default today), `start_date_to` (before today searches past events); `state` (two-letter US state code); `virtual` (true for virtual only, false leaves virtual events out); `limit` (1 to 25, default 10); `cursor` (next page of the same search); `order` (`newest_first` or `oldest_first`).
- Output: event rows with dates, place, organizer and the G2X event page, plus the total. When nothing matches every filter, rows marked as alternatives say what the calendar holds instead. Present them as alternatives, never as matches. A provisional result means the calendar could not be checked fully; never claim the event is not listed.
- Plan: all plans. Read only. On the research endpoint: yes.
- Example: `{"query": "industry day", "state": "VA"}`

### `g2x_get_event`

Read one event by the slug an event search returned.

- Inputs: `slug` (required, the row id from an event search).
- Output: one event with its dates, place, organizer, registration link, the write-up summary, the speakers it names, and how many agenda days and sponsors it lists, with its G2X page. Send the user to the official registration link to register.
- Plan: all plans. Read only. On the research endpoint: yes.
- Example: `{"slug": "<slug from an event search>"}`

To prepare for an event, say why it fits, name the relevant sessions and the organizations to research, and list questions to ask. Resolve possible partners with [Companies](companies.md). Do not turn a matching name into a confirmed contact. An event plan does not authorize outreach, a ticket purchase or a CRM write.
