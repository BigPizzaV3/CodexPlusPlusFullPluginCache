---
name: training
description: "Set up and follow Orendro workout plans, log sets or cardio, and review proposed changes to future workouts. Use for starting/resuming workouts, importing plans, short in-session logging replies, and training review."
---

Read [shared rules](references/shared-rules.md) before operating.

Use saved plans and live tool results. Preserve per-set targets and units.

When importing a new plan, extract the user's supplied exercises, order, sets,
reps and weights. Ask only about material ambiguities. Show the proposed plan
before saving a substantial new or replacement plan. Do not invent missing
exercises or silently overwrite an existing plan.

When starting a workout, use the appropriate session tool and handle an existing
active session from its result. Show the full returned workout plan once,
including per-set differences and missing-value labels, then the current set
or exercise choice. Avoid an extra status call when the start result is enough.

During an active workout:
- An exercise name/number selecting where to start is a selection, not a completed
  set. Use the reroute/selection tool.
- Interpret a short 'done' in a clear set context as a set log. Use the tool's
  stored defaults if allowed, and make the assumption visible briefly.
- After a saved set, use next_set/current_set and default flags already returned.
  Do not automatically call status or next-set again.
- If equipment is unavailable and the target exercise is unspecified, use the
  supported selection flow; do not silently choose a replacement.
- Ask a clarification when 'finished' could mean a set or the entire workout.

Finish only when the user intends to end the session. If planned work remains,
follow the required incomplete-workout confirmation. Honor any returned calorie
or baseline-review step. Recorded performance and future plan defaults are
separate: show the proposed baseline changes and save only those the user
chooses, using session_id and review_token from the displayed baseline_review.
Do not invent a review-version argument.

If a review becomes stale, show the refreshed proposal and obtain a new decision.
Declining a plan change needs no write and should not trigger repeated requests.
Direct plan edits should use the direct plan-edit tool with the provided details.

For cardio, preserve supplied activity, duration, distance and time. Do not force
workout-session setup for a simple completed walk or ride.

Output during activity: confirmed action plus the next set/choice. Show a fuller
summary at session completion or when requested. Do not attach unrelated food,
weight or setup questions to each set.
