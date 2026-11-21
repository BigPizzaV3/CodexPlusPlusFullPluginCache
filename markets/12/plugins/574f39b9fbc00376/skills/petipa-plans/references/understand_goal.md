# understand_goal

## Trigger

A new goal or a vague wish, like "I want to get fit", "learn French", or "launch my product", before there is a plan; or a result whose Next names the moment below.

## Information needed

- The goal in the person's words, any date they gave, and what they can do today.
- What `petipa_prepare_plan` returns: the time they have, what their other plans already take, and how to shape the plan.

## Inference limits

- Never guess their level, their free time, or a date they didn't give.
- Ask only what the plan can't be made without. A simple goal needs no question.

## Decision procedure

1. Name what done looks like, and by when: an outcome to reach, or a routine to keep.
2. Note what they can do now and the limits they named.
3. If the goal could hurt them, follow What Petipa won't plan in the entry, and call no tool.
4. Call `petipa_prepare_plan` once, and follow its Next.
5. For a project or a launch, whose steps come from where the person stands, ask in one question where they are and what's left; a habit, a skill, or a distance needs no question. Then open design_feasible_plan.
6. Say back in one line what you understood, without listing a plan.

## Reads

`petipa_prepare_plan`

## Writes

none

## Card moments

`next_plan`

## Edge behavior

- Petipa shows no questions of its own and keeps no answers between plans: ask in words, and never promise it will remember them.
- A goal with no date: plan without one, or ask once if the date matters.
- A single errand, a reminder, or a list isn't a plan: answer without Petipa.
- Never a long survey for a simple goal.
