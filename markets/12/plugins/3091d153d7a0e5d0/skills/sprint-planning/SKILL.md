---
name: sprint-planning
description: Plan, fill, check and start a team's sprint in Project Simple. Use when the user wants to create or fill a sprint, asks whether a sprint can start, asks about capacity or who is on time off, or wants to start or halt a sprint.
---

Sprints belong to a team, not to a project, and are numbered rather than named. A team runs one
sprint at a time. Follow the `project-simple-rules` skill for references, links and confirmations.

## See where the team stands

1. `get_current_sprint` for the running sprint of each team the user is on; `list_sprints` for
   planned and past ones; `get_sprint` for one sprint's items and dates.
2. Report items with their status and the link that opens them in Project Simple.

## Plan and fill a sprint

1. If there is no planned sprint, `create_sprint` for the team. Keep the team's usual cycle and
   WIP defaults unless the user asks for different ones.
2. Find candidate work with `search_items` using `scope=BACKLOG` and `onlyOpen`, in backlog order.
3. Show the user the items you intend to move and wait for a yes. Then `move_items_to_sprint`
   in one call for several items, or `move_item_to_sprint` for one.
4. Check capacity before over-filling: `get_sprint_capacity` for an existing sprint, or
   `estimate_sprint_capacity` for dates that have no sprint yet. Capacity comes from the team's
   engineers, the working days in the sprint, the time off booked for them and the sprint's
   utilization ratio.

## Time off

- `list_time_off` and `get_time_off_summary` show who is away and when.
- `schedule_time_off` books time off and changes the capacity of every sprint those dates fall
  in. Say so when you report it. `update_time_off` and `cancel_time_off` adjust a booking.

## Start a sprint

1. Call `get_sprint_readiness` first. A sprint will not start until every item in it is broken
   down into tasks and estimated, and no other sprint of that team is running.
2. If it is not ready, list exactly what is in the way: which items lack tasks or estimates, or
   which sprint is still running. Offer to add tasks with `add_item_tasks` or estimates with
   `update_item`. Do not call `start_sprint` until readiness passes.
3. When it is ready, confirm with the user, then `start_sprint`.

## Halt a sprint

`halt_sprint` ends the sprint, carries unfinished work over and cannot be undone. Explain that,
get an explicit yes, and only then call it. Report what was carried over.

## Estimating with the team

`invite_to_story_poker` asks a team to vote on an item's story points. Each invitee gets a TODO,
votes stay hidden until the session completes, and inviting again replaces an open session, so
check `get_story_poker_history` and confirm before re-inviting. `submit_story_poker_vote` records
the signed-in user's own vote.
