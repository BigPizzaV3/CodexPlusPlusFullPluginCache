---
name: propose-bike-workout
description: Propose a cycling workout using Lion Lift ride history, recent cross-training, the athlete's goals, and available time. Use when the user asks what ride to do; this skill does not schedule it.
---

# Propose a bike workout

Give one practical ride for the requested day. Make it specific enough to review and, if desired, pass to `schedule-bike-workout`.

## Gather context

- Ask for missing details that would change the ride: intended day, available time, focus (for example endurance, climbing, or intervals), trainer or road setting, terrain if relevant, available power or heart-rate sensors, and current fatigue, pain, or illness. If a minor detail is open, state a reasonable assumption.
- Use Lion Lift's read tools to discover available collections and fields. Review recent completed rides, normally 6–12 weeks, for frequency, duration, distance, comparable sessions, power, heart rate, cadence, effort, and notes when recorded. Review recent runs, swims, and lifts for total load and hard sessions, especially leg-intensive work or consecutive demanding days. Exclude scheduled or incomplete records from completed training totals.
- Retrieve only fields needed for the decision. Widen date queries around local-day boundaries when records use UTC timestamps. Treat implausible or inconsistent measurements as uncertain. Do not infer interval structure from ride totals alone.
- Use the athlete's stated goals and constraints. Do not assume a particular age, ability, threshold power, training plan, or personal file exists.

## Design the session

- Match the focus and duration to recent cycling fitness, the preceding 24–48 hours, upcoming commitments if known, and available time. Avoid abrupt jumps in duration or intensity. If history is sparse or recovery uncertain, favor a manageable easy aerobic ride.
- Specify warm-up, each work and recovery segment with repeat count, and cool-down. Use power or heart-rate targets only when reliable history and the athlete's equipment support them; otherwise use effort and a talk-test cue. Avoid treating road speed as a stable intensity target across changes in terrain, wind, or traffic.
- Allow practical flexibility for outdoor riding, including safe places to start intervals. Treat current pain, illness, dizziness, or other concerning symptoms as a reason to pause or modify training, not as data from which to diagnose a condition.

## Present the proposal

State a distinctive title, intended date, trainer or road setting, focus, expected duration and approximate distance if supportable, complete step sequence and recovery, targets, and the main evidence behind the choice. Distinguish logged facts from coaching judgment and mention material data gaps briefly. Include an easier adjustment or stop condition when recovery is uncertain.

This skill only proposes. Do not call a scheduling tool here. If the user wants it scheduled, hand the complete proposal to `schedule-bike-workout` for confirmation and creation.
