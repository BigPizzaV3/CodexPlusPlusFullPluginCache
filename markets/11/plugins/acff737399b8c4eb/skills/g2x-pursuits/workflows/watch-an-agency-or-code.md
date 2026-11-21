# Watch an agency, a code or a record

Goal: a watch or saved search that matches the user's intent, with its real notification state stated plainly.

## Steps

1. Calibrate with `g2x_calibrate_session`. Confirm what "watch this agency" means in filters: which codes, notice types, set-asides and dates.
2. Prove the filters return the right records. Run the equivalent search first: `g2x_search_records` for a dataset, or `g2x_search_opportunities` for open notices. Show a few matches before saving anything.
3. Save the search on request. Call `g2x_save_search` on the right surface with that page's filter keys, for example `{"surface": "opportunities", "name": "VA cyber", "filters": {"search": "cybersecurity", "agency": "VA", "naics_code": "541512"}}`. Set `notify_cadence` only when the user wants updates and the plan allows them. Read it back with `g2x_list_saved_searches`, then run it once with `g2x_run_saved_search` to confirm it behaves.
4. Watch codes when the code is the signal. Call `g2x_watch_codes` with up to five NAICS or PSC codes, for example `{"action": "watch", "codes": [{"code_type": "naics", "code": "541512"}]}`. Use `action: "unwatch"` to stop. This tool may not be offered on every connection or account; if refused, save a search instead and say the difference.
5. Watch single records when the record is the signal. Call `g2x_watch_records` with the ids and titles as returned. Check the result with `g2x_list_watchlist`. Remove with `g2x_unwatch_records`.
6. Change a saved search carefully. Read it with `g2x_list_saved_searches`, then send `g2x_update_saved_search` with every filter to keep plus `expected_updated_at`. New filters replace all old filters.

## What to tell the user

Name the view or watch, its filters, whether updates are on and at what cadence, and its G2X link. A saved search with updates off is not an alert. Running a search once does not prove what is new since last time. Do not change notification settings as a side effect of research, and do not promise future checks that were not turned on.
