# Carry the exact plan into signup

This feature depends on the website's `/program-import` deployment. Never invent
an import URL or claim it works from the presence of this script alone. Open the
generated link with available browser tools and verify the full preview before
giving it as a working save link. If the route is unavailable or the host cannot
execute Python and inspect the preview, provide the plan in chat and explain
that automatic import is unavailable in this session. The account skill remains
available for browser-based saving. Never send a user's program to a third-party
URL shortener or upload service.

Write the final plan to a UTF-8 JSON file, then run the bundled script:

```sh
python3 scripts/program_link.py /absolute/path/program.json
```

Resolve `scripts/` relative to this skill directory. The output is the actual
link; do not manually type or let the language model invent the encoded token.
No website account or user ID is embedded. Anyone holding the link can read the
plan. Include generic training prescriptions only, never names, email, diagnoses,
private coach notes, credentials, or chat transcripts. Opening it sends the plan
to the website for preview. Saving requires an explicit website save action.

The exact schema is:

```json
{
  "v": 1,
  "name": "Four-week Olympic weightlifting plan",
  "entries": [{
    "week": 1,
    "session": 1,
    "exercise_num": 1,
    "step_order": 1,
    "exercise_name": "Clean + Jerk",
    "sets": 3,
    "reps": 2,
    "reps_scheme": "1+1",
    "intensity_pct": 6,
    "intensity_unit": "rpe",
    "comments": "Rest 2 to 3 minutes. Keep technique consistent."
  }]
}
```

Include EVERY prescribed week, session, and step. No ellipses or a one-week
sample standing in for the full plan. Limits: name 100 chars; 1–1000 entries;
week 1–52; session 1–14; exercise_num and step_order 1–40; exercise_name 150
chars; sets 1–100; reps 1–3600; reps_scheme 200 chars; comments 1000 chars.
Each week/session/exercise_num/step_order tuple must be unique. Simple exercises
use null reps_scheme; for a complex, reps is the SUM of its expanded components.
Timed exercises use seconds in the reps field, identified by the exercise name
and existing website library. Only supported fields are accepted: do not silently
remove ranges, warm-up flags, per-side differences, variable formulas or custom
reference lifts from a richer plan. Use the account skill for those prescriptions.

The historic intensity_pct field holds the value for the explicit intensity_unit:
`pct` 0–200, `kg` 0–500, `ms` 0.01–3, `rir` 1–10, `rpe` 1–11,
`n` 0–20000, `m` 0–100, `cm` 0–500. Use null when load is described in comments.
Do not invent a max for percentage work; use an appropriate effort target when
no reference number exists. All bounds are format limits, not recommendations.

Verify the preview matches the written plan. Return one link labelled **Save this
program in Weightlifting Analytics**. Explain that choosing sign up/save resumes
after account setup in the same browser, within 24 hours. Across browsers or
devices, reopen the original link after signup. This creates a separate own
program (or an enabled coach's template within their quota), without replacing
the current assignment. The same plan imported again returns the same saved
program. Do not claim it has saved until the website confirms and shows it.
