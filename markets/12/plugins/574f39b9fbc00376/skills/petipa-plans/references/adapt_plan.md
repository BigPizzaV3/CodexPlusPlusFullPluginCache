# adapt_plan

## Trigger

Steps moved again and again, a change in the time they have, faster progress than planned, a date that no longer fits, or the person unhappy with the plan, like "Why do I delay Fridays?". Also a result whose Next names one of the moments below.

## Information needed

- The plan's steps, their states, and their moves, from `petipa_get_progress`.
- For a bigger change, what `petipa_prepare_plan` returns about their time.

## Inference limits

- Name only signals you saw in Petipa's results or their words, and say what is uncertain.
- One event is not a pattern.
- Never rewrite their plan on your own.

## Decision procedure

1. Name the signals you saw, plainly.
2. Offer a likely reason, as a guess.
3. Offer one change that can be undone, with its trade off, like the date against the workload.
4. Wait for their yes. Then make the change with its own tool: `petipa_edit_steps`, `petipa_add_steps`, `petipa_remove_steps`, or `petipa_edit_plan` for the date, name, note, or plan B. On `plan_changed`, say in one line what changed, never the card's steps or times.
5. On `date_at_risk`, say early, in one line, that the steps left no longer fit before the plan's date, and offer Next's two ways: a new `target_date`, or keeping the must haves.
6. When they come back to the plan later, ask once whether the change helps.

## Reads

`petipa_get_progress`, `petipa_prepare_plan`

## Writes

`petipa_edit_steps`, `petipa_add_steps`, `petipa_remove_steps`, `petipa_edit_plan`

## Card moments

`date_at_risk`, `plan_changed`

## Edge behavior

- Petipa keeps no record of a proposal yet: it is only your words until their yes.
- A no is final until they ask again.
- Steps done or skipped can't change.
