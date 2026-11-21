# Awards, vehicles and recompetes

Use these tools to count and segment award spending, research a contract vehicle, and find work that is ending. Define the measure before you calculate anything. Obligations, potential value, ceiling and outlays are different numbers. Preserve currency, fiscal year and awarding versus funding agency. Never add a vehicle's ceiling to its task order obligations, and never double count modifications. A forecast, an expiring award and a recompete candidate are not open solicitations. Do not present them as one.

### `g2x_query`

Run one governed query over awards, opportunities, vehicles and protests. Prefer it for counts, totals and a bounded complete list instead of adding up a first page yourself.

- Inputs: `command` (required). Run `{"command": "help"}` first, then `"<source> --help"` for that source's filters. Verbs are `list`, `search`, `get`, `count` and, for awards, `aggregate`. Sources are `awards`, `opportunities`, `vehicles` and `protests`.
- Output: matching records, counts or totals with the exact total. Every list answer says when it was cut. A large answer returns its first page and saves the whole fetched set as a workbook in the user's G2X account to download. Say whether a workbook covers the whole query or a bounded subset. If exact totals are unavailable, label the analysis as a sample.
- Plan: all plans. Protests queries return data only from the Starter Team plan up; the protests help screen answers on every plan. This tool can save a new workbook file, so it is not read only and it is not on the research endpoint.
- Example: `{"command": "awards aggregate --by awarding_agency --naics 541512 --fy 2025"}`

### `g2x_expiring_awards`

List contract or IDV awards whose period of performance ends in a window. It is a listing, not a search; the returned total is the match count for the window.

- Inputs: `expiry_fiscal_year` or `pop_end_date_range` (one is required; a supplied range overrides the fiscal year); `dataset` (`contracts` by default, or `idvs`); `agency_code` and `funding_agency_code` (for example `9700` for the Department of Defense, `3600` for the Department of Veterans Affairs); `naics`, `psc`, `set_aside`, `recipient_uei`; `obligated_min`, `total_value_min` (dollar floors); `limit` (1 to 50, default 25); `cursor` (next page of the same listing; awards come soonest ending first).
- Output: award rows with G2X links, the total for the window and a cursor for the next page.
- Plan: all plans. Read only. On the research endpoint: yes.
- Example: `{"expiry_fiscal_year": 2027, "naics": ["541512"], "agency_code": "3600"}`

### `g2x_recompete_radar`

List contracts ending in a window, each with the open opportunities that could be its recompete. Candidates are possibilities, never findings. Keep the confidence band and the matching reasons with every row you report.

- Inputs: at least one scope is required: `recipient_uei` (the holder, yours or a competitor's), `office_code`, `naics` or `psc`; `months_ahead_start` (default 0) and `months_ahead_end` (default 12, up to 60); `sort` (`end_date` by default, or `value`); `limit` (1 to 50, default 20); `cursor` (next page with the same filters and sort).
- Output: contract rows with candidate recompete notices, a confidence band and the reasons each candidate matched. The result counts every contract in the window.
- Plan: all plans. Read only. On the research endpoint: yes.
- Example: `{"naics": ["541512"], "months_ahead_end": 12, "sort": "end_date"}`

### `g2x_vehicle_usage`

Show how one contract vehicle is used in award data. The figures are partial: records may not list every holder, and they are not the vehicle's ceiling. The program office publishes the holder list and the ceiling.

- Inputs: `identifier` (required, the vehicle's name or program acronym as G2X lists it, such as `OASIS+`, or its solicitation number); `candidate_cursor` (when one name fits several vehicles, the answer returns them to choose from; pass the cursor back with the same name to see more matches).
- Output: one answer with the contract holders on record, task orders and money obligated on them.
- Plan: all plans. Read only. On the research endpoint: yes.
- Example: `{"identifier": "OASIS+"}`
