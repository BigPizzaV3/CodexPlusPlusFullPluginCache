# reflect_progress

## Trigger

"How am I doing?", "How's my week?", "Show all my plans", or a result whose Next names the moment below.

## Information needed

- Their plans, this week's counts, and each plan's next step, from `petipa_get_progress`.

## Inference limits

- Steps done are actions, not the goal reached: never turn step counts into a share of the goal.
- Compare with a starting point only when the person gave one.

## Decision procedure

1. Call `petipa_get_progress`. It is for you, not to show.
2. How they're doing: two lines at most, the steps done this week, then the next step and its day.
3. All their plans: name each by its title with its next step, in a short answer, no table.
4. Say what is working only if it fits in those lines.
5. Never lead with a streak, and never give a percentage.

## Reads

`petipa_get_progress`

## Writes

none

## Card moments

`read`

## Edge behavior

- Petipa has no progress or rhythm view yet: answer in words, never promise one, and offer today's step: its card opens My week.
- No plan yet: offer in one line to make one.
- Asked about one plan, answer for that plan alone.
