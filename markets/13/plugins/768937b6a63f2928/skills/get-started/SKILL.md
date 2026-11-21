---
name: get-started
description: Set up AI Fitness Coach with a minimal training profile, optional bodyweight, and an optional user-provided workout program.
---

# Get started with AI Fitness Coach

Keep onboarding short. The user should be able to start logging immediately.

## Minimal setup

Ask for or infer only information that is useful to training and that the user willingly provides:
- preferred weight unit;
- experience level: beginner, intermediate, or advanced;
- primary training goal in a short phrase;
- height only if the user wants mechanical-work estimates;

Save explicit profile values with `setup_profile`. Do not require every field.

Bodyweight is optional. If the user provides a real measurement, save it with `set_bodyweight`. Do not estimate or store bodyweight by default.

## Program setup

If the user already has a program:
1. Ask them to paste or upload it.
2. Preserve its structure with `import_program`.
3. Activate it with `activate_program` on the start date they choose.

Do not invent a replacement program when the user already has one. Do not redistribute a third-party program as a built-in catalog item unless AI Fitness Coach has rights to do so.

If the user has no program, they can still use AI Fitness Coach as a freeform workout logger and progressive-overload coach.

## First workout

After setup, tell the user they can simply write sets naturally, for example:

"DB bench: 50 lbs x 8 reps for 3 sets."

Use `log_workout` to store the structured facts. Never invent omitted values.
