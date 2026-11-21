---
name: set-up-delegent
description: Set up Delegent. Use when the user asks to set up Delegent, its routines or schedules, or when delegent_get_setup_status says setup should be offered.
---

# Set up Delegent

Delegent works best when a few routines keep it current. This app runs the schedules; Delegent records what is set up.

## 1. Check status

Call `delegent_get_setup_status`.
- `declined`: do not offer again unless the user asks.
- `set_up`: show what is running and offer only `missing_recommended`.
- `not_set_up` or `unknown`: continue.

## 2. Show value first

If the user has not used Delegent here yet, run one piece now on real data, for example today's `plan-my-day-and-week` or `follow-up-atron`. People set up routines after they have seen the result.

## 3. Recommend the core set

| Routine | When (default) | What it does |
|---|---|---|
| Morning brief | Weekdays 07:30 | Today's meetings with prep, due tasks, follow-ups. Mondays add the week ahead. |
| Daily wash-up | Weekdays 18:00 | Tells you what happened and keeps Delegent up to date. |

Optional: midday check (13:00), weekly review (Fri 16:00), delegation chase (Tue and Thu 10:00), monthly SteerCo prep (first Monday).

Two scheduled tasks cover the core. Some plans cap active scheduled tasks, so fewer, bundled routines are better.

Say this once: **scheduled runs work well on a faster, lower-cost model.** If this app lets you choose a model for scheduled tasks, pick one.

## 4. Ask for settings in one message

Timezone; times; which routines; for the wash-up, the auto-save level (see `routine-daily-wash-up`).

## 5. Create the schedules

For each routine the user picks, use this app's scheduling feature with the self-contained run instruction from its routine skill:
- `routine-morning-brief`
- `routine-daily-wash-up`
- `routine-midday-check`
- `routine-weekly-review`
- `routine-delegation-chase`
- `routine-monthly-steerco`

Name the app's integrations explicitly in the instruction (Delegent, plus mail or calendar if used), so unattended runs can reach them.

## 6. Record it

After the app confirms each schedule, call `delegent_save_routine_setup` with the routines, schedules and host. If the user says no, record `declined: true`.

Tell the user:
- when the first run is,
- that unattended runs cannot ask questions, so anything needing a decision appears under **Needs you** in the run's output, where they can reply, and
- how to pause, change or delete a routine.

If this app has no scheduler, or cannot reach Delegent in unattended runs, say so. Offer the run instructions as prompts to use manually. Record nothing as scheduled.
