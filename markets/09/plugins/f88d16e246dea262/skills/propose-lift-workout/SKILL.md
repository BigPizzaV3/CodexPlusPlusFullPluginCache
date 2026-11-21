---
name: propose-lift-workout
description: Propose a strength-training session using Lion Lift lift history, recent swim/bike/run load, goals, equipment, and available time. Use when the user asks what to lift; this skill does not schedule it.
---

# Propose a lift workout

Give one practical session for the requested day. Explain the muscle groups and training purpose in plain language, then provide a plan specific enough to review and, if desired, pass to `schedule-lift-workout`.

## Gather context

- Ask for missing details that would change the session: intended day, available time, goal, equipment, exercise preferences or limitations, and current soreness, pain, illness, or unusual fatigue. If a minor detail is open, state a reasonable assumption.
- Use Lion Lift's read tools to discover collections and fields. Review recent completed lifts, normally 6–12 weeks, for exercise selection, sets, reps, loads, frequency, notes, and performance on comparable movements. Review recent runs, rides, and swims for total load and hard sessions, particularly work that stresses the same muscles. Exclude scheduled or incomplete records from completed training totals.
- Retrieve only fields needed for the decision. Widen date queries around local-day boundaries when records use UTC timestamps. Distinguish completed reps and loads from planned ones. Treat implausible or inconsistent entries as uncertain.
- Use the athlete's stated goals and constraints. Do not assume a particular age, lifting experience, training split, or personal file exists.

## Design the session

- Choose the muscle groups and exercises based on recent lifting, recovery, cross-training, and upcoming commitments if known. Prefer familiar movements unless the user wants variety. Include a short warm-up, exercise order, sets, reps, rest, and a realistic time estimate. Balance the session so it fits the available time.
- Choose one main focus and explain it simply: **strength** means practicing heavier efforts with fewer reps and ample rest; **hypertrophy** means enough challenging work to support muscle growth; **muscular endurance** means sustaining repeated efforts with lighter loads or more reps. Explain **progressive overload** as a gradual increase in a suitable variable, such as reps, load, or total work, when prior performance and recovery support it. Do not imply every session must be harder than the last.
- Use recent comparable sets to suggest loads or a bounded starting range when evidence supports it. Otherwise prescribe an effort target, such as finishing with a few good reps available, and explain how to choose the load. Avoid invented maxes, abrupt load jumps, and training to failure by default. Offer an easier adjustment when recovery is uncertain.
- Treat current pain, illness, dizziness, or other concerning symptoms as a reason to pause or modify training, not as data from which to diagnose a condition.

## Present the proposal

State a distinctive title, intended date, focus, muscle groups, expected duration, and a brief reason this session fits the athlete's recent training. Show each exercise with sets, reps, suggested load or load-selection cue, and rest. Separate logged facts from coaching judgment and mention material data gaps briefly.

This skill only proposes. Do not call a scheduling tool here. If the user wants it scheduled, hand the complete proposal to `schedule-lift-workout` for confirmation and creation.
