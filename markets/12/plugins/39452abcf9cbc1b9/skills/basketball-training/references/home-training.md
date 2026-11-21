# Training at home

What a player does between practices: a short plan of their own, made by the coach. Short and often beats long and rare.

## What a good home plan looks like

- Four to six exercises. Six fits on one printed page.
- Things a player can do alone: ball handling, footwork, form shooting close to the basket, finishing when there is a hoop.
- One focus the coach picked for that player, plus one thing the player enjoys.
- Countable goals instead of minutes: "20 makes from each side", "30 seconds with each hand".
- Something a parent can read in ten seconds and say "nice work" about.

## Ask about the setting, only when it matters

| Question | In the draft |
|---|---|
| Is there a hoop to train at? | `hoop`: without one, drills that need a hoop are left out |
| Is there someone to train with? | `training_partner`: without one, every drill is solo |
| Cones or other equipment? | `equipment`: drills that use it come first |

Don't ask all three by reflex. A coach who says "something for the driveway" has already answered the first one.

## For the coach, in Basketball Assistant

1. **The team's pool:** the drills the coach has marked as good for home training. Read it with `get_training_pool`; add or remove drills with `update_training_pool`. Find drills to add with `search_all`.
2. **A draft for one player:** `generate_training_plan` with the player, one to three focus areas and the setting. It picks from the pool first and fills in from the library. A draft is not saved, and the number of drafts each month is limited. Editing by hand is not.
3. **Save it:** `create_training_plan`. Each player has one current plan. When one exists, change it with `update_training_plan` and a short `change_summary`, so the history reads well.
4. **Hand it out:** `share_training_plan` gives a link to a page that prints well, good for sending to parents.

`list_training_plans` shows the whole team: who has a plan, and who doesn't yet.

When the draft holds a placeholder for a focus area, no drill fit. Say so, and suggest a custom exercise in the coach's own words.

## For players and parents

- A player reads their plan with `get_my_training_plan`. A parent reads their child's with `get_child_training_plan`.
- No plan yet: say so plainly. The coach makes the plan. Until then, suggest two or three simple things from the library for this week (`search_all`), such as ball handling that needs no hoop.
- Details about a player that the coach keeps private never go through the chat.
