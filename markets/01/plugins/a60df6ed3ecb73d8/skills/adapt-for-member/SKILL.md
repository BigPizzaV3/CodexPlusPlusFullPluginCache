---
name: adapt-for-member
description: >
  Recommends or adapts Hyperhuman workouts and programs for a stated member profile.
  Use when the user asks to personalize, recommend the next session, adapt intensity,
  swap equipment, or reshape a plan for goals, level, or duration.
  Not for medical advice, clinical rehab plans, pricing, checkout, or social drops.
---

# Adapt for a member

## Goal

Produce a safer, science-informed next session or plan change from explicit user inputs.

## Steps

1. Collect only what the user provides: goal, level, duration, equipment, constraints, optional source workout/plan id.
2. If no source id: call `recommend_workouts` or `recommend_plans` with the stated filters.
3. If a workout id is known: call `adapt_workout` with profile fields the user gave.
4. If a program/plan id is known: call `adapt_plan`.
5. Optional: call `generate_workout` only when they ask for a new session (not a tweak).
6. Summarize: what changed, why (short), and one clear next step.

## Output

- Recommended or adapted item name + id
- 2–4 change bullets (duration, difficulty, equipment, substitutions)
- Explicit non-medical disclaimer when health context appears

## Guardrails

- Movement support only. Not medical care. Refuse diagnosis/treatment/prescription.
- GLP-1 / weight management = adherence and lean-muscle movement support, not clinical guidance.
- Do not invent end-user health records or pull insights digests.
- Prefer conservative adaptations when constraints are unclear.
- See [references/safety-guardrails.md](references/safety-guardrails.md).
