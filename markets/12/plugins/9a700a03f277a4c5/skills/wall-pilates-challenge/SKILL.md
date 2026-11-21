---
name: wall-pilates-challenge
description: Use when the user wants the 28-day wall Pilates challenge or to continue it ('start the 28-day wall Pilates challenge', 'day 5 of Wallform 28', 'next day of my program'). Opens a day of Wallform 28, a program of short daily sessions.
---

Wallform 28 is a 28-day wall Pilates program, also asked for as the 28-day wall Pilates challenge. Each day is one short session in the same timed, follow-along player as a routine. The user's own instructions come first.

## Flow

1. `open_program_day` opens a day: the day number the user asks for (1-28), or without one the day after the highest day they finished, or day 1. Any day opens at any time.
2. Days 1-14 are beginner sessions of 10-15 minutes, days 15-28 intermediate sessions of 15-20 minutes, and every seventh day is a gentle stretch day. `adjust` (easier or harder) and `equipment` (`wall_only` for standing moves only) work as for a routine.
3. The user taps Start in the card. The day counts as done when the player reaches its end; opening a day saves nothing by itself.
4. To see which days are done, `get_progress` shows the finished days and the `next_program_day`.

## Scope

- General fitness content for healthy teens and adults; pregnancy, the postpartum period, injuries, pain and medical conditions are questions for a doctor or a qualified professional.
- The program promises no results such as weight or appearance; it is 28 short sessions in a row.
