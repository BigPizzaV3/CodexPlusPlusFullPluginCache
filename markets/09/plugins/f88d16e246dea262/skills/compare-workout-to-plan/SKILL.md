---
name: compare-workout-to-plan
description: Compare a scheduled or planned workout with what was actually logged and explain meaningful differences. Use when the user asks how a workout compared to what was planned, whether they stuck to a schedule, or what changed between a plan and the real session.
---

# Compare a workout to its plan

Explain, in plain language, what was planned versus what actually happened for one workout. This skill only reads and compares; never call a scheduling tool from here.

## Find the plan and the session

- For a **lift**, the plan and the result live in the same completed record — no second record to find. `original_lift_plan` holds the frozen plan (exercise names, planned weight/reps per set); `lifts` holds what was actually logged. Fetch the one record (`fetch_records` / `get_record` on the `lifts` collection, `status` `completed`) and compare those two fields directly. `original_lift_plan` is only present on lifts that were scheduled through a path that writes it — if it's missing, say plainly that there's no preserved plan to compare against (the workout was likely logged directly, not scheduled first), rather than guessing at one.
- For a **run, swim, or bike**, the plan and the logged session are two separate records with **no stored link between them** — match them yourself by date. Use `list_run_workouts` / `list_swim_workouts` / `list_bike_workouts` to find the plan whose `scheduledFor` falls on the day in question, then use `fetch_records` on that sport's own collection (`run` / `swim` / `bike`, `status` `completed`) to find the logged session on that same calendar day. If more than one plan or more than one completed session that day is plausible, say so and ask which one rather than guessing. If either side is missing — no matching plan, or no completed session that day — say so plainly instead of fabricating a comparison.
- Note the plan's `status` when relevant. A plan still `pending` (never synced via the app's Sync Workouts screen) never actually reached Apple Fitness or the Watch, so even if a session was logged that day, the plan can't have directly guided it the way a `synced` one would have.

## Compare what matters

- For a **lift**, compare exercise by exercise and set by set: same exercise, planned weight/reps vs. actual. Call out exercises or sets that were skipped, added, or changed by more than a trivial amount — not every identical value.
- For **run/swim/bike**, the comparison is necessarily high-level, not step-by-step: the logged session carries overall totals (distance, duration, average heart rate, pace, power, when recorded), not the same warmup/block/cooldown structure the plan has. Compare total distance against the plan's summed distance goals, total duration against its time-based goals, and average heart rate/pace/power against any target alerts in the plan — and be explicit that this is an approximation of whether the plan was followed, not a verified segment-by-segment match.
- Don't invent precision the data doesn't support. If the logged session has no heart rate, pace, or power recorded, say that plainly rather than guessing whether a target alert was hit.

## Present the comparison

- State what was planned and what actually happened side by side, in plain language, then lead with the meaningful differences rather than restating every value that matched.
- Mention the plan's sync status when it affects how much weight to put on the comparison (see above).
- If no plan, no logged session, or no confident match between the two could be found, say so directly rather than presenting a guess as a real comparison.
