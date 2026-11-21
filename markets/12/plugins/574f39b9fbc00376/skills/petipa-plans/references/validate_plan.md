# validate_plan

## Trigger

Before you send a new plan or a big change to one, and when a result's Next names the moment below.

## Information needed

- The plan you are about to send, and what `petipa_prepare_plan` returned for it.
- For a change, the plan's steps and ids from `petipa_get_progress`.

## Inference limits

- A plan Petipa accepts is no proof the goal is doable: check it yourself.
- Never invent a clash with their week: Petipa sees only its own plans.

## Decision procedure

1. Before sending, check that every step leads to the goal, the first step is easy, and no step jumps far past the one before.
2. Check that the time fits what all their plans already take, that the limits they named hold, and that there is room to rest and catch up.
3. Check that each step is concrete and sanely sized, comes in a working order, could hurt no one, and fits before the target date.
4. Fix what you can before sending. Ask the person only about a real trade off, in one sentence.
5. After the save, fix its `self_fix` warnings with `petipa_edit_steps` in one call, or `petipa_remove_steps` for a step to drop: they are slips in how you wrote the plan, not the person's choices.
6. Its `ask` warnings are the person's: say what to change in one plain sentence, never a list of steps, and change the plan only once they agree.

## Reads

`petipa_prepare_plan`, `petipa_get_progress`

## Writes

`petipa_edit_steps`, `petipa_remove_steps`

## Card moments

`plan_warnings`

## Edge behavior

- Petipa doesn't check how the plans fit the person's week yet: rely on what `petipa_prepare_plan` returned and what they told you.
- On Keep it as it is, change nothing.
- A write refused with its fixes listed: fix them all and call again.
