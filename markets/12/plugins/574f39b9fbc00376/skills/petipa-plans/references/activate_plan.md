# activate_plan

## Trigger

The person asks to start a saved plan, like "Start now" or "Let's begin", or a result whose Next names one of the moments below.

## Information needed

- Which plan, and that it is saved and not started yet: from the last result or `petipa_get_progress`.
- Whether they want to begin right now, or at the planned time.

## Inference limits

- Never start a plan they haven't asked to start.
- Never mark the first step done because the plan started.

## Decision procedure

1. Name the plan by its title, and make sure it isn't started yet.
2. Pass `start_now` true only when they want to begin right now; Petipa moves a short first step to now.
3. Call `petipa_start_plan`, with their time zone when you know it.
4. On `started`, write one short line: when the first step is today, like "Go. Tap I did it when you're back."; otherwise, when it comes.
5. On `not_started`, write at most one line: the plan starts when they tap the card or ask you to.

## Reads

`petipa_get_progress`, `petipa_get_today`

## Writes

`petipa_start_plan`

## Card moments

`not_started`, `started`

## Edge behavior

- Several plans not started, and none named: ask which, by title.
- A plan already started: show today's step with `petipa_get_today` instead.
- A first step too long to begin now: it starts at its planned time; say when it comes.
