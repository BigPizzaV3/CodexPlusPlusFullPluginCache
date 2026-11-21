# Weekly pipeline review

Goal: a review the team can act on: what moved, what is due, what is stale and what needs a decision.

## Steps

1. Calibrate with `g2x_calibrate_session`. Check `g2x_usage` when the user asks about remaining usage.
2. Read the board completely. Call `g2x_list_pipelines`, then `g2x_get_pipeline` for the chosen board. Page with the cursor until it is null. A partial board makes a partial review; say so if you stopped early.
3. Read pursuit context. For items the user wants to discuss, call `g2x_list_pipeline_notes`. For relationship context, read the CRM with `g2x_crm_find` and `g2x_crm_get_record`.
4. Bring fresh signals in, on request. Run the saved views with `g2x_list_saved_searches` and `g2x_run_saved_search`. Check the watchlist with `g2x_list_watchlist`. For strategic accounts, scan `g2x_recompete_radar` and `g2x_forecast_scan`. Present search results as current matches, not as a proven change set.
5. Propose, then apply approved changes. Show the proposed stage moves, notes and follow-ups first when the request was only to review. On approval, move items with `g2x_move_pipeline_item` using `expected_stage` from your read, add notes with `g2x_add_pipeline_note`, and set CRM next steps with `g2x_crm_set_follow_up` or tasks with `g2x_crm_add_task`. Read the pipeline back after moves. On a gate block, report the missing fields instead of overriding without instruction.
6. Prepare the week's meetings. For upcoming industry days, use `g2x_search_events` and `g2x_get_event`, then draft a short plan per [Forecasts and events](../references/forecasts-events.md).

## What to tell the user

Open with counts by stage and the items needing a decision this week, with deadlines. Follow with stale items, new matches worth triage, and the changes actually made, each with its G2X link. Keep proposed changes separate from applied changes. Removing an item needs confirmation; deleting a pipeline needs the owner's explicit confirmation and cannot be undone.
