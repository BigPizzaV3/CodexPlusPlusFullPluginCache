---
name: track-workout
description: Track and recall workouts, correct or remove logged sets, and save or manage training locations with GoodSet (including spoken aliases "Good Set" and "Good Sets"). Use when the user explicitly chooses GoodSet; asks to start, record, log, track, continue, or finish a workout, lift, or run; reports a completed set in an established workout context; asks about workout history, personal records, or exercise progress; or asks to save or manage a training location for workouts. Do not activate from tentative future-set statements alone, bare travel, arrival, or readiness phrases, or when the user asks for another app.
---

# Track workouts with GoodSet

Use GoodSet as the system of record when this skill is selected for workout tracking. Do
not offer to keep a conversation-only log. Honor an explicit request to use another app.
Do not use this skill for hypothetical future workout plans, gym logistics, directions,
generic place questions, or general fitness advice that should not change workout or
saved-location data.

A tentative future-set statement alone does not request GoodSet. Do not call any GoodSet
tool or read workout status just to acknowledge a plan. Reply
conversationally without treating the set as completed. An explicit request to inspect the
current workout, history, or progress still calls for that read, including when the user
is deciding their next set.

## Route the request

- For a live workout start, resume, completed set, or finish, use `workout_track`.
  `action=open` is the supported resume and recovery operation: it starts a workout or
  returns the one in progress. Use `action=reopen` only when the user says right after a
  finish that they were not done ("I wasn't done," "keep going"). For a read-only request
  to see or check the current workout, use `workout_current`.
- For a correction to a logged set's measurements or note, use `workout_track` with
  `action=correct_set`. For a logged exercise occurrence assigned to the wrong exercise,
  use `action=correct_exercise`.
- When the user asks to delete, remove, or undo a logged set, use `workout_track` with
  `action=remove_set`. Without `set_number` it removes the latest set; for another set,
  pass the exercise and its `set_number`.
- To change a finished workout, follow "Change a past workout" below.
- For the user's last or previous workouts, training days, exercise history, loads,
  sets, or reps from a specific workout, use `find_workouts`. Use `workout_get` only
  when a returned public workout reference needs complete detail.
- For an exercise personal record or progress trend, call `search_exercises` to resolve
  the exact exercise, then call `exercise_progress` with its public reference. Never guess
  between distinct matches. When `sessions_truncated` is true, describe the sessions as a
  recent window and do not use the oldest returned session as a lifetime baseline.
- Use `training_location_find` only when an explicit workout-tracking request supplies
  place context. Use `training_location_manage` only when the user explicitly asks to
  manage saved training locations. A training location can be a gym, home setup, outdoor
  area, or another place; do not reduce it to a gym.
- Use `workout_record_completed` only for an already-completed workout that is not the
  active live workout and is not already in GoodSet.
- For saved routines (a named plan of exercises and set targets), read them with
  `workout_routine_find` and change them with `workout_routine_manage`.
- Use `search_exercises` for personal-record and progress resolution, genuine discovery,
  or unresolved ambiguity. `workout_track` resolves ordinary exercise names itself.

If the GoodSet connection or required tools are unavailable, ask the user to connect
GoodSet. For a write, say that the requested change was not recorded; for a read, say that
the workout history could not be retrieved. Never simulate a result.

Corrections use the same durable continuation and confirmation flow as other workout
changes. An exercise correction changes the assignment of the selected occurrence and all
sets already logged under it; it does not rename the exercise catalog entry. Follow any
returned exercise or occurrence disambiguation, then confirm the preview. Never add
replacement sets to simulate a correction.

`correct_set` requires a real `set_number`. When the user says the last or latest set,
first call `workout_current` and copy the `set_number` of the last entry in
`workout.current_exercise.sets` from the result. Never guess a set number from the
conversation or assume it is one.

Set removal also uses the confirmation flow. In the workout in progress, an explicit
request to delete, remove, or undo the latest set authorizes confirmation only when the
preview identifies the set the user meant. Do not turn removal into a correction with empty
values. Report success only after the confirmed result says the removal was applied;
`no_change` means nothing was removed.

## Keep saved routines as plans

- A routine is a plan, never a record. Saving or editing one logs no sets; planned targets
  are not completed work.
- Save, rename, replace, or archive a routine with `workout_routine_manage` only when the
  user explicitly asks. Those actions apply immediately: report the returned routine, do
  not ask for confirmation again. To save the workout just finished, use
  `action=save_workout` with its `workout_ref`. A target's `sets` counts identical
  consecutive sets, so 3 sets of 80 kg x 6-8 is one entry with `sets` 3.
- To train from a routine, resolve it with `workout_routine_find` (by name, or list them),
  then call `workout_track` with `action=open` and its `routine_ref`. The result's
  `next_planned_set` is the plan's next set: you may name it, but log only the sets the
  user reports, with the values they report.
- `name_conflict` means nothing was saved. Ask whether to use another name or to change
  the existing routine; never overwrite it unasked.
- Resolve each exercise with `search_exercises` before `create` or `replace_exercises`.
  `replace_exercises` restates the whole plan; keep the exercises the user did not mention.
- GoodSet shows previous sets and records; it does not suggest next weights. Do not invent
  progression targets for a routine.

## Keep training locations optional

- Never ask for a training location just to start or record a workout. If the user does
  not mention one, omit it.
- When a workout request clearly names a place, call `training_location_find` first. Use
  the sole clear saved-name match's `training_location_ref`. The tool lists saved GoodSet
  locations only: call it without passing the place name, then compare the returned names.
  It has no free-text place query and returns no real-world place candidates. If there is
  no clear saved match, omit the location and continue the workout immediately; save the
  place only when the user explicitly asks to manage it.
- When the user explicitly asks to save a new location, create it with the user-supplied
  name, then pass its returned reference to the workout. Omit `location_kind` unless the
  user supplied the category; a name such as Home Rack does not authorize inferring `home`.
- Never ask for or pass an address, city, coordinate, or provider identifier through these
  tools. Trusted clients manage that metadata; never infer, geocode, or invent it.
- Use a workout's returned `training_location` as ordinary context. To compare loads on
  the same equipment or biomechanics, call `find_workouts` with `training_location_ref`.
  Do not expose that reference in the conversational response.
- Archived locations remain historical context. Do not attach one to a new workout unless
  the user restores it first.

## Handle a live workout

1. Do not select this skill, mention GoodSet, or offer workout tracking from a bare travel,
   arrival, or readiness phrase such as "on my way to the gym," "I just got here," or
   "ready to train." Those phrases alone do not express workout tracking, history, progress,
   or saved-location-management intent.
2. Call `workout_track` immediately when the user explicitly asks to start, resume, or
   record a workout, or unambiguously says that a workout is already underway. Use the
   operation matching the user's intent; do not ask for exercise details before opening or
   recovering the active workout.
3. Treat set values as completed only when the user reports that they performed them or
   explicitly asks to log them. Advice, targets, and planned sets are not completed work.
4. Preserve every accepted exercise, load, unit, repetition, and set value while resolving
   missing or ambiguous input. Ask only for the missing fact.
5. Read `outcome`, `summary`, and optional `next_action` from the result envelope. Read
   tool-specific questions, continuation tokens, confirmation tokens, choices, and returned
   entities from `data`. Follow them exactly. Continue in the same turn when the result
   authorizes the next tool call; otherwise ask the returned question without inventing an
   answer.
6. When `workout_track` returns `outcome=active` or `outcome=applied`, its
   `active_workout` already holds the updated workout. Reply from it without calling
   `workout_current`. This applies to starts, resumes, logged sets, corrections, removals,
   and exercise reassignments. After `outcome=finished` there is no active workout; report
   the returned recap. `outcome=edited` means a finished workout changed; it returns no
   `active_workout`.
7. Claim that a requested start, set, or finish happened only when `outcome` or `summary`
   says that action was applied. Never infer this from `isError` being false. Recoverable
   outcomes such as `invalid_input`, `conflict`, `version_conflict`, `not_found`, or
   `workflow_expired` mean that nothing was applied; follow `next_action`. Summarize applied
   exercise, load, unit, and reps briefly.
8. When `open` or `add_sets` returns `outcome=recently_finished`, nothing was logged and
   the user just finished a workout. Ask whether they are continuing it or starting a new
   one; never choose for them. To continue, call `action=reopen`; for a new one, call
   `action=open` with `new_workout=true`. Then resend any sets the user reported.
9. Finish a workout only when the user's own words end the whole workout, such as "I'm
   done for today." Finishing a set or an exercise is not finishing the workout; phrases
   such as "that's good," "next," or "done with this exercise" do not finish it. If the
   user says after a finish that they were not done, call `action=reopen`.
10. If a continuation or confirmation expires, preserve the accepted user input, prepare
    the change again, and obtain any newly required confirmation. Never report the expired
    change as applied.

When prior workout state makes a spoken quantity structurally ambiguous, such as "same
weight, eight more" after one set, ask whether the user means one set of eight reps or eight
additional sets before writing. Do not discard the values that were already clear.

## Change a past workout

1. Find the workout with `find_workouts`.
2. Call `workout_track` with its `workout_ref`, the exercise, and `add_sets`,
   `correct_set`, `remove_set`, or `correct_exercise`. Pass `set_number` for a set and
   `occurrence_number` when the exercise appears more than once. Take both from the
   returned workout, using `workout_get` for full detail; never guess them.
3. Read the prepared change back and confirm only after the user's explicit yes, even when
   they asked for the change.

Without `workout_ref`, a correction or removal targets the workout in progress. When none
is in progress, it falls back to the workout just finished and needs the same explicit yes.
Never use `workout_record_completed` to patch an existing workout.

## Keep responses workout-paced

During a live session, keep confirmations short and immediately useful. Report only facts
returned by GoodSet, then prompt for the next completed set or exercise when appropriate.
Do not expose internal references, tokens, schemas, or confirmation handles.
