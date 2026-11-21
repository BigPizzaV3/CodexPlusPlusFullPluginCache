# The coaching week

A volunteer coach's week has four moments. Each one has a small job, and each sets up the next. Suggest the one that fits the day, never all four at once.

## Before practice: plan it

1. Find the practice. `get_my_teams` when you don't know the team, then `get_upcoming_schedule` for that team. A practice that already has a plan shows the plan's name.
2. Pick one or two focus areas. Start from how the last practice went (see "After practice"). With nothing to go on, keep last week's focus and add one new thing.
3. Plan for that team and the time the practice has: `generate_practice_plan` with `team_id`, `duration_minutes` and `focus_areas`. Tell the coach what the draft assumed.
4. Save on a yes with `create_practice_plan`.
5. Put the saved plan on that practice with `update_event` (`practice_plan_id`). The calendar then shows the practice has its plan.

Planning two practices in one go: make the second build on the first. Same focus, one step further in the focus file's progression.

## Practice day: who is coming

- `get_attendance_for_event` shows each player's answer before practice: yes, no, or no answer.
- When the numbers change, change the plan to fit:
  - A big change, or a plan that isn't saved yet: `generate_practice_plan` again with the new `player_count`.
  - A saved plan: adjust the blocks with `update_practice_segment`. 4-on-4 becomes 3-on-3, and stations get fewer players each.
- Fewer players is good news for touches. Say so: more turns, shorter lines, more small-sided games.

## After practice: two minutes

1. Attendance: open the tracker with `get_attendance_for_event` so the coach can tap each player, or record what they tell you with `mark_attendance`.
2. `complete_event` marks the practice done. Its plan then counts as completed.
3. Ask one question: "How did it go?" On a clear answer, save it with `rate_practice_plan` (1 to 5, and a line on what worked).
4. Turn the answer into the next focus:

| The coach says | Next practice |
|---|---|
| "Passing was sloppy" | `passing` as the focus, starting one step back in its progression |
| "They got bored" | Shorter blocks, more games, fewer lines |
| "It was too hard" | The same focus, one step easier |
| "It went great" | The same focus, one step further, or one new focus beside it |

Then plan the next practice around it, from the top of this page.

## Game day

- Keep it to what the team practiced this week: one or two things, said in plain words.
- Every player gets real minutes. Plan the rotation before the game, not during it.
- One play to show the team: draw it with `render_diagram`, save it with `save_diagram` once the coach likes it, then share it with `share_diagram`. A diagram has to be saved before it can be shared. See `references/drawing-a-play.md`.
- After the game, name one thing the team did well before anything else.

## The reminder email

Once the practice days are on the calendar, you may ask once whether the coach wants an email the day before a practice that has no plan yet. Turn it on with `update_user_profile` (`practice_reminders: true`) only on a yes.
