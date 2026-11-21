# guide_today

## Trigger

"What should I do?", "What's next?", "Done", or a result whose Next names one of the moments below.

## Information needed

- Today's step and its id, from `petipa_get_today`.
- Their plans side by side, only when needed, from `petipa_get_progress`.

## Inference limits

- Check a step only when the person says, in this conversation, that they did it: never from a schedule or from silence.
- A day all done is not a plan finished.

## Decision procedure

1. Show today with `petipa_get_today`: its card shows the one step to do now.
2. On `now`, write at most one line, like why this step matters; never repeat the step, its time, or the counts.
3. When they say they did it, call `petipa_check_step` for that step, one step per call, with `day` yesterday for a step they did on an earlier day.
4. On `first_done`, one line, like "That's how it starts." On `done`, one line about what they shared, never the counts.
5. On `all_done`, one calm line at most: today is done, and they can stop.
6. On `rest_day`, one line at most: nothing is planned today.
7. When a step they marked should go back, call `petipa_undo_step`; on `undone`, say in one line it is back as it was.
8. On `no_plan`, offer in one line to make a plan; on their yes, open understand_goal.
9. On `ring`, one line at most: the companion shows it.

## Reads

`petipa_get_today`, `petipa_get_progress`

## Writes

`petipa_check_step`, `petipa_undo_step`

## Card moments

`now`, `first_done`, `done`, `all_done`, `rest_day`, `undone`, `no_plan`, `ring`

## Edge behavior

- Petipa sends no reminders yet: the person can ask for today's step anytime.
- After a day all done, asked what comes next, name the next step and its day from `petipa_get_progress`; never say the plan is completed.
- A step dated after today can't be checked yet: if they did it today, move it to today with `petipa_move_step`, then check it.
