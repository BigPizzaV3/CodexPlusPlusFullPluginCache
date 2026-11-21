---
name: wall-pilates
description: Use when the user wants a wall Pilates or home Pilates workout for the minutes they have ('a 15-minute beginner wall Pilates workout', '10 minutes for core, no mat'). Builds a timed, follow-along routine from 43 illustrated wall moves.
---

Wallform is wall Pilates the user follows along with in ChatGPT: routines built from Wallform's own library of 43 wall moves, each drawn as a moving illustration, and Wallform 28, a 28-day wall Pilates program of short sessions (also asked for as a 28-day wall Pilates challenge). Routines open in a card with a timed player: a count-in, then each move with its illustration, a countdown and form cues, and rests that show what's next. The user's own instructions come first.

## Inputs

- **A routine** (`build_routine`): the length in minutes (5-30, 15 by default), the level (beginner, intermediate or advanced), the focus (`full_body`, core, `legs_glutes`, `upper_body` or mobility), the equipment (`wall_and_mat`, or `wall_only` for standing moves only, as in "no mat", "standing" or "no equipment"), `adjust` (easier or harder) and `variation` (1-20, a different mix of moves for the same settings). Settings the user didn't mention can be left out.
- **A program day** (`open_program_day`): the day (1-28); without it, the user's next day. `adjust` and `equipment` work as for a routine.

## Flow

1. `build_routine` builds a routine with a warm-up, a main circuit and a cool-down, sized to the minutes asked for, and shows it in the card. Its result has the title, the `total_time` with rests, the moves by section and a summary. "Easier", "harder", "shorter", "standing only" and "a different mix" are the same tool again with `adjust`, the minutes, `equipment` or `variation` changed.
2. `open_program_day` opens a day of Wallform 28. Days 1-14 are beginner sessions of 10-15 minutes, days 15-28 intermediate sessions of 15-20 minutes, and every seventh day is a gentle stretch day. "The next day" or "continue my program" opens the day after the highest day the user finished, or day 1. Any day opens at any time.
3. The user taps Start in the card and follows the timed player. A session is saved when the player reaches its end, skipped moves included; both tools above are read-only and save nothing themselves.
4. `get_progress` shows the sessions this week and this month, the streak, the finished Wallform 28 days and the `next_program_day`. It counts finished sessions only.
5. `delete_my_progress` permanently erases the user's saved sessions, streak and finished days when they ask for it, and Wallform 28 starts again at day 1.

## Scope

- Wallform is general fitness content for healthy teens and adults. It has no guidance for pregnancy, the postpartum period, injuries, pain or medical conditions, which are questions for a doctor or a qualified professional, and it makes no promises about results such as weight or appearance. ChatGPT answers those questions itself.
- Every move is done at a wall. A `wall_only` routine uses standing moves only, so the user needs nothing but a wall.
- There is no account: Wallform keeps finished sessions under ChatGPT's anonymous user ID. Wallform is in English.
- Each result ends with a short summary suitable to show the user; the card shows the moves.
