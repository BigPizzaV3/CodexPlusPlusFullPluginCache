# Choosing tools and evidence

Call a tool only when the answer depends on data, account state or saved context that the conversation does not already contain. Then use the smallest set of calls that answers the question, and fetch evidence instead of asking the runner to repeat it. Local stored history comes first. General questions and follow-ups answered by earlier results need no new call.

| Question | Start with | Add only if needed |
|---|---|---|
| Latest or last few runs | `get_runs` with a small `limit` (1-5) | `get_run_detail` for the run being discussed |
| A specific past run ("my 21 km last spring") | `search_local_activities` with date and distance bounds | `get_run_detail` |
| Totals, rankings, "how far this week/month/year" | `get_local_stats` | `search_local_activities` to list the runs behind a total |
| Laps, splits, recorded intervals, best efforts | `get_run_detail` | `get_run_streams` when laps are missing or the question is about a point in the run |
| Fading, drift, pacing within a run, cadence or heart rate over time | `get_run_streams` | `get_run_detail` for laps and context |
| Trends, fitness, consistency over weeks | `get_local_stats` and a bounded `search_local_activities` | detail or streams for two or three comparable runs, not every run |
| Setup, access, missing data, imports, Garmin, trial | `get_account_status` | `get_onboarding_diagnostics` where it is available |
| Saved goal, preferences or plan (only where these tools exist) | `get_runner_context` / `get_training_plan` when the question depends on them | The write tools, only on the runner's explicit request (see the running-analysis Skill) |

## Enhanced responses

Some tools accept an optional `response_version`. Use `response_version: 2` only when the tool's own schema lists it and the question needs the extra evidence:

- `get_local_stats` v2: exact windows in the runner's time zone (`timezone`, an IANA name), ISO weeks (`group_by: "week"`), exact totals with counts of missing values, and coverage. Use it for "this week", for month or year totals near midnight in a non-UTC time zone, and whenever completeness matters.
- `get_local_stats` v2 also gives `coverage.by_source` (activities per source label, for the source line) and, with both bounds, `coverage.periods`: every week or month in the window oldest first, the empty ones, and whether the first or last is partial.
- `get_run_streams` v2: `stream_provenance`, covering acquisition route, time-axis facts (spacing, gaps, repeated timestamps), units, nulls and carried-forward values, and `stream_splits`: per-kilometre split times and paces, heart rate, cadence and altitude, with an altitude summary. Use it before interpreting sampling, cadence, gaps or point-in-run figures.
- `get_runs` v2, `search_local_activities` v2 and `get_run_detail` v2: pass `timezone` and each activity gains `facts` with its local date, weekday and time, distance in km, moving time and pace per km as text. Use them whenever you state a date, weekday or pace.

If the tool does not offer `response_version`, call it in its original form and do not add the argument. v2 bounds must be real calendar dates (YYYY-MM-DD) or date-times with `Z` or an offset.

## Remote Strava recovery

`find_strava_activities` and `sync_strava_activities` reach Strava and change stored data. Use them only when:

- the runner asks to find or import an activity that local search did not find, or that is missing detail;
- their account status says Strava is connected.

Search first, then import only the activities the runner wants. Never use them to answer an ordinary analysis question, never call them "just in case", and never send them a Garmin or archive ID. There is no remote Garmin sync and no Garmin history request. If these tools are not present in the session, say that retrieval is not available here.

## Limits

- Keep `limit` small for recent-run questions; widen only when the question needs it.
- Do not dump whole activity lists or raw arrays into the answer. Summarise.
- One stream request per run you actually analyse.
