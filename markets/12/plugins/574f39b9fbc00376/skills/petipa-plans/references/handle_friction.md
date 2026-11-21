# handle_friction

## Trigger

"That's too hard", "I'm busy", "Not now", "Tomorrow instead", or a result whose Next names one of the moments below.

## Information needed

- The step, its id, and its next open slot, from `petipa_get_today`.
- The plan's plan B and the step's past moves, from `petipa_get_progress`.

## Inference limits

- Never ask why, and never ask for a long story.
- Before you check a step, make sure they did it, or did the short version.

## Decision procedure

1. Later: move the step with `petipa_move_step` to the day and time they name, or to its next open slot. On `not_now`, say in one line when it moved.
2. Too hard, even the first time: offer one smaller step that still leads to the goal, or another time. On their yes, change the step with `petipa_edit_steps`, then say in one line what changed.
3. On `moved_twice`, offer the two smaller versions Next gives, worded for this step, and change it only on their pick.
4. On `short_counts`, today's read says the plan B short version counts as today's step: one line, like "Either one keeps it going."; never mention the step left open. When they did the short version, check the step with `petipa_check_step`.
5. Say what they actually did. Never say they did the full step when they did less.

## Reads

`petipa_get_today`, `petipa_get_progress`

## Writes

`petipa_move_step`, `petipa_check_step`, `petipa_edit_steps`

## Card moments

`not_now`, `moved_twice`, `short_counts`

## Edge behavior

- Petipa doesn't keep a smaller effort apart from a full one yet: the short version counts as today's step, and your words say what was done.
- After a slip, offer a smaller step or a fresh start, never deleting the plan.
- A no is final until they ask again.
