# recognize_achievement

## Trigger

The person reports a result, like "I ran the whole race", or a plan reaches halfway or its last step: a result whose Next names one of the moments below.

## Information needed

- Whether they did it, or only plan to, in their own words.
- The plan's steps from `petipa_get_progress`, to find the step they did.

## Inference limits

- A date that has passed is no proof: never infer that they did it.
- A last step checked is not a verified goal. What they report is theirs: say it as theirs.

## Decision procedure

1. Make sure they did it, and don't only plan to.
2. If it matches a planned step, check that step with `petipa_check_step`, and only that one.
3. On `halfway`, add one line, like "Halfway. What you did so far carries the rest."
4. On `finish`, write one line about what they did, then offer Next's choices: Keep going, A new goal, or Rest for now. On the first two, open understand_goal; on Rest for now, nothing.
5. Celebrate what they did, briefly, never their worth, and don't rush them to a new goal.

## Reads

`petipa_get_progress`

## Writes

`petipa_check_step`

## Card moments

`halfway`, `finish`

## Edge behavior

- Petipa doesn't record milestones or confirm results yet: say what they did in words, as their own report, and never say Petipa verified it.
- A result with no matching step: celebrate it in words, and check nothing.
