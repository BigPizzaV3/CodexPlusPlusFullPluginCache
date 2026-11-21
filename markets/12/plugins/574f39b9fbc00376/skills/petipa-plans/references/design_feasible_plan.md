# design_feasible_plan

## Trigger

The goal is clear and the person wants a plan to keep, or a result whose Next names the moment below.

## Information needed

- What understand_goal found: the outcome, the date, what they can do now, and their limits.
- What `petipa_prepare_plan` returned in this conversation: how to shape the plan, and the time it may take.

## Inference limits

- Size every step by what `petipa_prepare_plan` returned, never by free time you guess.
- A date you chose for them is provisional: say so in the note.

## Decision procedure

1. Work back from the goal, then forward from what they can do today.
2. Start small: a light first week, and each step one concrete action.
3. Never split one activity into several steps that aren't real, and never pack the first week.
4. Leave room to rest and to catch up between harder steps.
5. Add a plan B for hard days, and a short note on how you shaped the plan for them.
6. Check it as validate_plan says, then save it with `petipa_create_plan`.
7. Write one short line, like "Saved." Where the card shows, it shows the plan, so never list its steps, days, or times.
8. Start it only when the person taps the card or asks: open activate_plan.

## Reads

`petipa_prepare_plan`

## Writes

`petipa_create_plan`

## Card moments

`plan_saved`

## Edge behavior

- Milestones, categories, a personal why, and a long roadmap view aren't in Petipa yet: put the stages in the steps and the note, and never promise them.
- Where no card shows, your reply is the plan's only view: give it briefly.
- A plan refused with its fixes listed: fix them all and call again.
- At Free's limit the result says so: follow Free's limit in the entry.
