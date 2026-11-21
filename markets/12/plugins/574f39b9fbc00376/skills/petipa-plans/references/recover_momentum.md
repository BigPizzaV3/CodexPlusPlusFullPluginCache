# recover_momentum

## Trigger

The person comes back after a break, like "I've been away", or a result whose Next names one of the moments below.

## Information needed

- Whether they have been away, from `catch_up` and `days_away` in `petipa_get_progress`.
- The plan's id, and what is left to do.

## Inference limits

- Never count the days away out loud, and never judge the break.
- Everything they did stays done.

## Decision procedure

1. Say "Good to see you" in your own words.
2. After a few days away, on `comeback`, offer Next's choices as the way back in. Start from today calls `petipa_start_from_today`, so the earliest step left is today; Just the next step changes nothing.
3. After two weeks or more, on `fresh_start`, offer a fresh start in one line; on their yes, call `petipa_restart_plan` with a lighter restart week.
4. On `restarted`, say in one line that the plan picks up from the restart Monday with a lighter week, and that everything done stays.
5. Keep the first step back small.

## Reads

`petipa_get_progress`

## Writes

`petipa_start_from_today`, `petipa_restart_plan`

## Card moments

`comeback`, `fresh_start`, `restarted`

## Edge behavior

- Never rebuild every past step as a list to catch up on.
- Change the plan only after their yes; a no is final until they ask again.
- Never offer deleting a plan after a break.
