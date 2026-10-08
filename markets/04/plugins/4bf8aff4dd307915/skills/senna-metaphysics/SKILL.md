---
name: senna-metaphysics
description: Use the Senna closed-source BaZi and LiuYao tools for traceable Chinese metaphysics calculation and bounded traditional interpretation. Apply when a user asks for a BaZi chart or LiuYao reading; do not use for generic horoscope, tarot, dream interpretation, or factual professional advice.
---

# Senna Metaphysics

Use the Senna engine as the calculation authority. The model may clarify input and explain returned fields, but must not silently recalculate or replace pillars, hexagrams, six relations, shi/ying positions, yongshen, verdicts, evidence, or confidence.

## Route the request

- Use `senna_bazi_analyze` for a birth-chart request based on a person's birth details. Read [references/bazi.md](references/bazi.md) before collecting or passing input.
- Use `senna_liuyao_analyze` for one concrete question cast at a defined time. Read [references/liuyao.md](references/liuyao.md) before collecting or passing input.
- If the user asks only for an explanation of an already returned Senna result, explain that result without calling again unless recalculation is necessary.
- Do not choose a tool merely because the request mentions fate, luck, auspiciousness, or traditional culture.

## Before calling

Ask only for missing required facts. Do not invent identity, location, coordinates, historical UTC offset, DST, casting values, stroke count, question context, or success criterion.

If required facts remain missing, state exactly what is needed. Do not fill gaps from stereotypes or silently use the model's current location or time.

## Present the result

1. Treat `calculation` as immutable engine output.
2. Present `interpretation` as traditional-rule interpretation, not verified reality.
3. Preserve counter-evidence, conflicts, `needs review` states, and low confidence. Do not upgrade uncertainty because the prose sounds decisive.
4. Use `report` as a concise summary, then add structured details only when useful.
5. Keep Engine Revision, Ruleset Version, and protocol identifier available for audit when the user asks or when results are compared.
6. Never describe development tests, same-source regression, retrospective replay, or an unverified case count as independent predictive accuracy.

## Safety and factual boundaries

- Separate the traditional reading from real-world facts and professional judgment.
- For health, death, self-harm, legal disputes, criminal allegations, investments, debt, employment, immigration, or other high-stakes decisions, do not give a deterministic prediction or instruct action based on the reading. Encourage appropriate factual checks or qualified professional help.
- Do not assert hidden motives, guilt, illness, pregnancy, infidelity, paternity, or another person's private state as fact.
- Do not use a reading to override urgent safety action, medical symptoms, legal deadlines, financial risk controls, or verified evidence.
- Never expose local paths, secrets, internal thresholds, weights, scores, private calibration cases, P11 blind data, or server implementation details.

## Repeated readings and comparison

Do not recast the same question simply to seek a preferred answer. Follow the returned `recast_policy`. A genuinely narrowed stage, changed material facts, or a new time window may justify a new request; explain what changed.

When comparing two Senna results, first compare protocol, engine revision, ruleset version, normalized input, and calculation facts. Attribute differences to these fields before interpreting them.
