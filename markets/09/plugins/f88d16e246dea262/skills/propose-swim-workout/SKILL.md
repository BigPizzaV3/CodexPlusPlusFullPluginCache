---
name: propose-swim-workout
description: Propose a pool swim using Lion Lift swim history, recent cross-training, the athlete's goals, and available time. Use when the user asks what swim to do; this skill does not schedule it.
---

# Propose a swim workout

Give one practical pool session for the requested day. Make it specific enough to review and, if desired, pass to `schedule-swim-workout`.

## Gather context

- Ask for missing details that would change the session: intended day, time in the water, pool length and units, preferred strokes, focus (for example technique, endurance, or speed), equipment access, and current fatigue, pain, or illness. If a minor detail is open, state a reasonable assumption.
- Use Lion Lift's read tools to discover available collections and fields. Review recent completed swims, normally 6–12 weeks, for frequency, distance, duration, stroke mix, comparable sets, recorded pace or effort, and notes. Review recent runs, rides, and lifts for total load and hard sessions, especially shoulder-intensive lifting or consecutive demanding days. Exclude scheduled or incomplete records from completed training totals.
- Retrieve only fields needed for the decision. Widen date queries around local-day boundaries when records use UTC timestamps. Treat implausible or inconsistent measurements as uncertain. Do not infer interval structure from session totals alone.
- Use the athlete's stated goals and constraints. Do not assume a particular age, ability, training plan, or personal file exists.

## Design the session

- Match the focus and volume to recent swim fitness, the preceding 24–48 hours, upcoming commitments if known, and available pool time. Allow realistic time for rest and transitions. If history is sparse or recovery uncertain, favor a manageable technique or easy aerobic session.
- Specify warm-up, drills where useful, main set, work and recovery for each repeat, and cool-down. Make distances practical for the stated pool length. Use the athlete's pool units in the proposal and label them clearly.
- Use pace or send-off targets only when comparable swim data supports them. Otherwise prescribe effort and explicit rest. Do not treat an estimated pace or an uncalibrated device metric as a measured threshold.
- Treat current pain, illness, dizziness, or other concerning symptoms as a reason to pause or modify training, not as data from which to diagnose a condition.

## Present the proposal

State a distinctive title, intended date, pool length and units, focus, expected duration and total distance, complete set sequence with strokes and rest, any supported targets, and the main evidence behind the choice. Distinguish logged facts from coaching judgment and mention material data gaps briefly. Include an easier adjustment or stop condition when recovery is uncertain.

This skill only proposes. Do not call a scheduling tool here. If the user wants it scheduled, hand the complete proposal to `schedule-swim-workout` for confirmation and creation.
