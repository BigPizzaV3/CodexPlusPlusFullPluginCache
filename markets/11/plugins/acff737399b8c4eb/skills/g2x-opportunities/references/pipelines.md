# Pipelines, watchlists and saved searches

These tools work on the signed-in user's own G2X objects. A research request does not authorize a watch, pipeline or saved search change. A specific request to make that change does. Before a consequential or destructive change, identify the exact target and consequence and get the user's confirmation. Keep canonical IDs from read results. After an uncertain response, read back before retrying. Do not duplicate a write.

### `g2x_watch_records`

Add up to five opportunities or companies to the user's watchlist. It does not change the records themselves. An already watched record is skipped, never updated.

- Inputs: `items` (required, 1 to 5 items, each with `record_type`, the `id` G2X returned and its `title` as returned).
- Output: the records added, and any that were skipped with the reason.
- Plan: all plans. Write. On the research endpoint: no.
- Example: `{"items": [{"record_type": "opportunity", "id": "<id from search>", "title": "<title as returned>"}]}`

### `g2x_watch_codes`

Watch or stop watching up to five NAICS or PSC codes, so new opportunities and awards in a watched code (and forecasts for a NAICS code) reach the user's watchlist alerts. Repeating the same call changes nothing further.

- Inputs: `action` (required: `watch` or `unwatch`); `codes` (required, 1 to 5 items, each with `code_type` (`naics` or `psc`), `code` (NAICS is 6 digits; PSC is 4 letters or digits) and optional `title` to show on the watchlist).
- Output: the codes watched or no longer watched, each with its G2X page, and any that were skipped with the reason.
- Plan: when the connection offers it, and G2X still refuses accounts without code watches. Write; `unwatch` removes. On the research endpoint: no.
- Example: `{"action": "watch", "codes": [{"code_type": "naics", "code": "541512"}]}`

### `g2x_unwatch_records`

Remove up to ten records from the user's watchlist. A record that is not watched is reported, not an error.

- Inputs: `items` (required, 1 to 10 records, each with `record_type` and `id`; `title` is optional).
- Output: what was removed and what was skipped, with reasons.
- Plan: when the connection offers it. Write. On the research endpoint: no.
- Example: `{"items": [{"record_type": "opportunity", "id": "<id from the watchlist>"}]}`

### `g2x_list_watchlist`

List the records on the user's watchlist, optionally one record kind.

- Inputs: `record_type` (only this record kind); `limit` (1 to 50, default 25); `cursor` (next page).
- Output: watched records with G2X links. When there are more, the answer says so and gives a cursor.
- Plan: when the connection offers it. Read only. On the research endpoint: no.
- Example: `{"limit": 25}`

### `g2x_save_search`

Save a search as a Saved View on a G2X list page, using that page's own filter keys.

- Inputs: `surface` (required: `contracts`, `opportunities`, `grants`, `forecasts`, `idvs` or `vehicles`); `name` (required; saving the same name on the same page updates that view, but never its filters); `filters` (required, the page's filter keys to text; unknown keys are refused); `notify_cadence` (`daily` or `instant`; turns on the page's updates for the view, paid plans).
- Output: the saved view and where it shows in G2X. A save with different filters under an existing name is refused; use the update tool to change filters. A saved view is not by itself a recurring alert unless updates are on.
- Plan: when the connection offers it; updates need a paid plan. Write. On the research endpoint: no.
- Example: `{"surface": "opportunities", "name": "VA cyber", "filters": {"search": "cybersecurity", "agency": "VA", "naics_code": "541512"}}`

### `g2x_list_saved_searches`

List the user's Saved Views, newest first, optionally for one list page.

- Inputs: `surface` (only views on this page); `limit` (1 to 50, default 25); `cursor` (next page).
- Output: each view's filters and G2X link. Keep each view's `updated_at`; a filter change needs it.
- Plan: when the connection offers it. Read only. On the research endpoint: no.
- Example: `{"surface": "opportunities"}`

### `g2x_update_saved_search`

Change a Saved View's name, filters or updates. New filters replace all of the view's filters. Read the view first, send every filter to keep, and pass its `updated_at`. The change is refused if the view changed since you read it.

- Inputs: `saved_search_id` (required); `name`; `filters` (replaces all filters); `expected_updated_at` (required with `filters`); `notify` (true or false); `notify_cadence` (`daily` or `instant`).
- Output: the updated view. Turning updates on needs a paid plan.
- Plan: when the connection offers it. Write. On the research endpoint: no.
- Example: `{"saved_search_id": "<id from the list>", "filters": {"search": "cybersecurity", "agency": "VA", "naics_code": "541512,541519"}, "expected_updated_at": "<updated_at from the list>"}`

### `g2x_run_saved_search`

Run one Saved View the way its page does, with today's clock. Views on pages that only run in G2X answer with the page to open. Running a view once cannot by itself establish what is new since last time; say so when the user asks for a change set the result does not carry.

- Inputs: `saved_search_id` (required); `limit` (1 to 50, default 10); `page` (1 to 200, default 1).
- Output: the page's rows with G2X links, plus the view's own page in G2X.
- Plan: when the connection offers it. Read only. On the research endpoint: no.
- Example: `{"saved_search_id": "<id from the list>"}`

### `g2x_list_pipelines`

List pipelines with their stages, owner and edit rights. Owned boards come first, then editable, then view only.

- Inputs: `scope` (`mine`, `editable`, or `all` by default); `limit` (1 to 50, default 25); `cursor` (next page).
- Output: pipeline rows with stages and the user's rights on each. If the context gives one clear target pipeline, proceed with it. Otherwise ask which one.
- Plan: when the connection offers it. Read only. On the research endpoint: no.
- Example: `{"scope": "mine"}`

### `g2x_get_pipeline`

Read one pipeline as the user sees it, a page at a time. This is also the readback after adding, moving or removing an item.

- Inputs: `pipeline_id` (required, from the pipeline list); `limit` (1 to 50, default 25); `cursor` (next page; pass it back until it is null to read every item).
- Output: items with stage, agency, value, last change, when each item moved to its current stage and G2X links. Resolve stage and item IDs from this read, never from memory.
- Plan: when the connection offers it. Read only. On the research endpoint: no.
- Example: `{"pipeline_id": "<id from the pipeline list>"}`

### `g2x_add_to_pipeline`

Add up to ten G2X records, or pursuits by name, to one pipeline. A record already on the board is reported with its existing item, never added twice or moved. It requires edit access.

- Inputs: `pipeline_id` (required); `records` (required, 1 to 10 items with `record_type`, `title` and, unless `manual`, the record `id`; optional `agency`, `naics`, `solicitation_number`); `stage` (stage id or name); `operation_id` (your id for this write, such as a UUID; retry with the same id after a lost reply and G2X will not apply it twice).
- Output: the added items and any already on the board. A manual pursuit by name is not a verified government notice; say so.
- Plan: when the connection offers it. Write. On the research endpoint: no.
- Example: `{"pipeline_id": "<pipeline id>", "records": [{"record_type": "opportunity", "id": "<record id>", "title": "<title as returned>"}]}`

### `g2x_move_pipeline_item`

Move one pipeline item to a stage named by id or name. Stage gates apply. Moving an item to its current stage changes nothing.

- Inputs: `pipeline_id`, `item_id`, `stage` (all required); `expected_stage` (the stage the item was in when you read it; a move from a stale read is refused); `override_rationale` (an editor's reason for moving past a blocked gate); `operation_id` (retry with the same id after a lost reply).
- Output: the item in its new stage, or the missing fields and open checklist items when a gate blocks the move. On a conflict, read the pipeline again and reconcile.
- Plan: when the connection offers it. Write. On the research endpoint: no.
- Example: `{"pipeline_id": "<pipeline id>", "item_id": "<item id>", "stage": "<stage name from the pipeline>", "expected_stage": "<stage you read>"}`

### `g2x_add_pipeline_note`

Add a note to one pipeline item, authored by the user. Each call starts its own note; nothing deduplicates a repeat, so do not resend the same note after an uncertain response without reading the notes first. It requires comment access.

- Inputs: `pipeline_id`, `item_id`, `content` (all required; content up to 4000 characters).
- Output: the new note on the item.
- Plan: when the connection offers it. Write. On the research endpoint: no.
- Example: `{"pipeline_id": "<pipeline id>", "item_id": "<item id>", "content": "Incumbent is not bidding. Confirm at industry day."}`

### `g2x_list_pipeline_notes`

List the notes on one pipeline item, newest first, with their authors.

- Inputs: `item_id` (required); `limit` (1 to 50, default 25).
- Output: note rows for the item.
- Plan: when the connection offers it. Read only. On the research endpoint: no.
- Example: `{"item_id": "<item id from the pipeline>"}`

### `g2x_remove_from_pipeline`

Remove one item from a pipeline. Only the pipeline entry goes; the G2X record stays.

- Inputs: `pipeline_id`, `item_id` (required); `confirm` (required, true; ask the person first).
- Output: the removed item. It requires edit access.
- Plan: when the connection offers it. Write. On the research endpoint: no.
- Example: `{"pipeline_id": "<pipeline id>", "item_id": "<item id>", "confirm": true}`

### `g2x_create_pipeline`

Create a pipeline owned by the user. Each call creates a new pipeline; nothing deduplicates by name, so list pipelines first. The account's plan sets how many pipelines it can have.

- Inputs: `name` (required); `stages` (stage names from the account's stage list, 1 to 20; leave out to get the default stages a new G2X pipeline gets).
- Output: the new pipeline's id, its stages with ids and names, and its G2X link.
- Plan: when the connection offers it. Write. On the research endpoint: no.
- Example: `{"name": "FY27 Civilian Pursuits"}`

### `g2x_delete_pipeline`

Delete one pipeline the user owns and every item on it. The G2X records stay. This cannot be undone and only the owner can do it.

- Inputs: `pipeline_id` (required); `confirm` (required, true; ask the person first and name the pipeline).
- Output: confirmation that the pipeline is gone. Read the pipeline list to verify.
- Plan: when the connection offers it. Write. On the research endpoint: no.
- Example: `{"pipeline_id": "<pipeline id>", "confirm": true}`

Finish every change by naming the changed records, the resulting watch, view or stage, and the G2X links. Do not promise future checks or alerts unless updates were actually turned on.
