---
name: kracey-training
description: Use Kracey for running and HYROX predictions, HYROX goal pacing, saved race comparisons, personal training analysis, and finding HYROX or hybrid fitness races. Use when the user requests these calculations or their own Kracey training data.
---

# Kracey training

Kracey computes race predictions, HYROX pacing and saved race comparisons. Use its returned numbers for these questions.

## Predictions and pacing

- Use `get_race_predictions` for running and HYROX estimates from the athlete's recorded efforts. State the returned basis and window; distinguish predictions from recorded bests.
- Use `predict_hyrox_time` for a HYROX estimate from a running result or in-race pace. Use `plan_hyrox_pacing` to work back from a goal finish time. Both need the division; use the exact offered division label and ask if it is missing.
- Report total, running, stations and Roxzone separately. Lap clocks are cumulative. If inside_the_data is false, label the estimate as outside the model's fitted range. Never promise a finish time.
- Use `predict_race_times` to estimate other running distances from one result. Keep the returned Riegel and Daniels estimates separate; pace_seconds_per_km accompanies the Riegel estimate.

## Saved races

- Use `get_hyrox_results` for saved races and splits, newest first. Use the returned race positions with `compare_hyrox_races`; defaults compare race 1 with race 2.
- Comparison changes are current minus previous seconds: negative is faster. Running includes Roxzone in the comparison. Report when same_division is false. Comparing needs two races with complete splits.

## Training context

- Use `get_status` first if unsure what is connected. This plugin has training access only. Heart and recovery data are not available through this plugin.
- Use `get_pace_curve` for recorded best running efforts; report window_days and do not invent missing distances.
- Use `get_progress` for weekly minutes, kilometres, session counts and the sport split. Describe the returned trend as the last seven days against the recent weekly rate.
- Use `list_sessions` for up to 90 days of sessions (default 14 days), optionally filtered by sport. Use a returned session_id with `get_session` for laps and pace-zone minutes. A true more flag means the list is truncated.
- Use `get_plan` only when offered, to read the existing next two weeks of scheduled sessions. This connection cannot create or change a training plan.

## Race directory

Use `find_races` for upcoming HYROX and hybrid fitness races, not running races. Filter by brand, country code and dates as requested. Returned temperatures are typical conditions, not a weather forecast.

## Reading and attribution

Times are seconds unless the field says minutes; pace is seconds per kilometre. Use formatted times when provided. Dates are the athlete's local dates. Null means unavailable, not zero.

Session data comes through intervals.icu. When a session has garmin: true, credit Garmin wherever that session or information derived from it is shown, including summaries, tables and charts.

All access is read-only and limited to the signed-in athlete. Report missing data plainly. Never ask for credentials in chat or imply access to another athlete's account.
