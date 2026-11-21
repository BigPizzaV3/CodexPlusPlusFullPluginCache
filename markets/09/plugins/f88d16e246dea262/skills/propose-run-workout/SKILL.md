---
name: propose-run-workout
description: Propose a specific run using Lion Lift workout history, recent training load, and the runner's goals and constraints. Use when the user asks what run to do; this skill does not schedule it.
---

# Propose a run workout

Give one practical run the user could do on the requested day. The result should be specific enough to review and, if desired, pass to `schedule-run-workout`.

## Gather context

- Ask only for missing details that would materially change the workout: intended day, available time, goal, running environment, and current pain, illness, or unusual fatigue. If the user leaves a minor detail open, make a stated, reasonable assumption.
- Use the connected Lion Lift read tools to discover available collections and fields. Review recent completed runs, normally 6–12 weeks, for frequency, volume, longest run, comparable sessions, pace, heart rate, and effort when recorded. Review recent lifts, rides, and swims for total load and hard sessions. Exclude scheduled or incomplete records from completed training totals.
- Retrieve only fields needed for the decision. Expand the date window around local-day boundaries if records use UTC timestamps. Treat missing, implausible, or inconsistent measurements as uncertain rather than filling them in.
- Use the user's stated goals and constraints. Do not assume a particular age, ability, training plan, or personal file exists.

## Design the session

- Match the session to recent training, the preceding 24–48 hours, upcoming commitments if known, and available time. Avoid abrupt increases in volume or intensity. If recent history is thin, favor an easy, conservative session and use effort targets.
- Give warm-up, each work and recovery segment with its repeat count, and cool-down. Set pace or heart-rate targets only when the data supports them; otherwise use effort or a conversational cue. Include an easier alternative or stop condition when recovery is uncertain.
- Treat current pain, illness, dizziness, or other concerning symptoms as a reason to pause or modify training, not as data from which to diagnose a condition.

## Present the proposal

State the workout title, intended date, indoor or outdoor setting, expected duration and approximate distance, complete step sequence, targets, and the main evidence behind the choice. Distinguish logged facts from coaching judgment and mention material data gaps briefly.

This skill only proposes. Do not call a scheduling tool here. If the user wants it scheduled, hand the complete proposal to `schedule-run-workout` for confirmation and creation.
