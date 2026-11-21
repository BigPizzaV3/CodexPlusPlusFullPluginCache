---
name: shape-plan-training
description: Plan, create, import, reschedule, pair or remove workouts in the user's connected Shape calendar. Use for requests to save a training week, build structured running/cycling/swimming sessions, move workouts, or match completed sessions to their plans. A request for ideas alone does not authorize calendar changes.
---

# Plan training in Shape

Use the connected Shape tools and their current input schemas. Follow the user's stated scope, dates, units and constraints. Do not request API tokens or use a separate connection. If the tools are unavailable, explain that Shape needs to be connected and stop before claiming a calendar change. If a tool answers that no device is connected or nothing is synced, switch to `connect_device` (see the shape-setup skill) before planning anything.

## Establish the plan

- Resolve dates in the athlete's local calendar. Ask when a date, sport or material target is ambiguous. Keep titles short and workout-specific.
- For a new block or a change to planned training, call `get_training_status` with no `from` or `to`. Read readiness drivers, load and the existing projection. Use `list_activities` over the affected date range to avoid scheduling conflicts or duplicating sessions; page through results if `total` exceeds the returned count.
- Respect the athlete's stated restrictions, availability and race priorities. Ask for missing constraints when they materially affect the plan.
- A request to create or move a specified workout authorizes that change. When the user asks only for advice or a proposed plan, present the proposal and wait for an instruction to save it. Clarify the exact affected workouts before an ambiguous deletion. Do not repeat a confirmation already supplied for the same identified change.

## Create and change workouts

- Use `create_activity` for one session and `batch_create_activities` for several. Use `update_activity` or `batch_update_activities` for existing sessions, sending their actual ids and only fields that should change. Keep each batch between 1 and 100 entries.
- `date`, `title` and `sportType` are required to create a workout. `date` is `YYYY-MM-DD`. Include `startTime` as local `HH:mm` only when the user specifies a start time; do not infer one or attach an offset.
- Sport values include `run`, `bike`, `swim`, `hike`, `yoga`, `tennis`, `skiing`, `nordicski`, `strength`, `surf` and `other`. Use values accepted by the live schema.
- Convert distance to meters and duration to seconds before saving. Choose `target: "distance"` for a distance target, `"time"` for a duration, `"pace"` when both are specified, and `"steps"` for a structured interval session. A target alone supplies no distance or duration.
- Set `completed: false` for a planned session. Mark a workout completed only when the user says it was done. Do not turn a planned prescription into an invented recording.
- Rest days have no workout. Skip them when importing a plan; do not add zero-distance rest placeholders. Simple easy sessions do not need invented interval steps.
- Set an estimated `load` for planned endurance workouts so they appear in the projection. Use `(duration_seconds / 3600) × effort² × 100`: recovery 0.25, easy 0.5, tempo 0.75, threshold 1.0, VO2 1.25, race 1.5. A 60-minute easy run is 25. Label estimates as estimates. If duration or intended effort cannot reasonably be established, ask rather than silently assigning one. Do not overwrite a completed workout's recorded load with this estimate.
- Recompute planned load when changing duration or intensity. Moving only the date does not require a new load estimate. For structured workouts with several intensities, estimate the component loads rather than treating every minute as the hardest interval.
- Before writing structured intervals or a swim, read [Workout details](references/workout-details.md) for repeat groups, pace targets and swim-specific fields.

## Pair and remove sessions

- A completed row's `plannedActivityId` points to its separate prescription. Read that planned row with `get_activity` when comparing or editing the plan. Do not assume the completed row contains planned steps.
- Use `pair_activities` with `completedActivityId` and `plannedActivityId` to match a performed workout to the plan it fulfills. Resolve both ids from returned data and verify their completed/planned states. If an existing pairing conflicts, explain it and obtain authorization before removing it.
- Use `unpair_activity` with `activityId` to remove an identified pairing without deleting either workout.
- Use `delete_activity` for one identified workout, or `batch_delete_activities` with `ids` for several. Individual deletion removes its pairing; batch deletion does not remove links on surviving paired workouts. If a counterpart will remain, include the pairing removal in the described deletion scope and use `unpair_activity` first when authorized.
- Calendar changes may also affect workouts on the user's connected devices. Report a saved change as saved; do not claim device delivery unless a returned result establishes it.

## Check and report

After creating, moving, changing or deleting planned workouts, call `get_training_status` again without a history range. Explain the returned next-week `series` and peak `projection` where relevant. Shape labels ratios above 1.5 as High; explain the change without treating that band as a medical verdict. Readiness cannot be projected into the future.

Report the workouts actually saved, moved, paired or removed, with dates and readable units. Preserve any unrelated sessions. If a write fails, stop dependent steps. If its outcome is uncertain, inspect the affected calendar before retrying a creation so a repeated call does not create duplicates. Relay connection, access and missing-data messages rather than claiming success.
