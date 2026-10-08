---
name: balance-analysis
description: Use for the receiving project's balance modeling, audits, calibration, scenario comparison, pass generation, or validation across Weapon, Hero, Equipment, Enemy, progression, economy, and player-loadout power.
---

# Balance Analysis Skill

Apply the [receiving-project contract](../../references/project-context.md). Resolve the actual game systems, configuration owner, active balance phase, and promotion gates from the project; the domains listed in the description are examples.

## Goal
Produce traceable, non-destructive balance decisions from explicit scenarios, formulas, assumptions, evidence tiers, and exit gates without confusing configured values, model outputs, runtime behavior, and final accepted balance.

## Trigger
Use for balance design/modeling, quantitative audits, pass comparisons, calibration, target budgets, TTK/DPS analysis, or validation. Activate `knowledge-steward` when durable KB state changes and `runtime-audit` when code/runtime semantics must be verified.

## Authority boundaries
- Balance process, methodology, accepted design intent, exit gates → canonical balance docs/roadmap.
- Structured config and live numeric values → the project's designated live configuration, Sheets, or CSV (for example, a project may use `BlueprintData`).
- Experimental calculations/workbooks → designated balance workbooks; they are evidence/work artifacts, not automatic canonical truth.
- Implemented runtime behavior → the designated repository/runtime evidence.
- Playtest observations → designated playtest logs.
- Production outcomes → the project's designated analytics source.

## Core loop
1. Define the exact balance question, player experience, scenario, and metric.
2. Lock the test boundary; avoid changing unrelated variable families at the same time.
3. State formulas, units, assumptions, expected ranges, confidence, and provisional dependencies.
4. Preserve accepted sources; create non-destructive variants/passes for experiments.
5. Validate data integrity before interpreting outputs.
6. Use the highest available evidence tier: config/formula → code/runtime semantics → controlled test → loadout/encounter test → structured playtest → production telemetry.
7. Compare model with evidence and separate model error, implementation error, and tuning error.
8. Decide: accept, revise, reject, or keep temporary.
9. Promote structured values only after the relevant exit gate is explicitly accepted.
10. Persist durable methodology/decisions and update compact context/working state without copying whole workbooks into the KB.

## Scenario discipline
- Never present a scalar as final Player/Hero/Equipment Power unless that model is explicitly assigned and accepted.
- Preserve scenario names and reference fixtures so comparisons remain reproducible.
- State occupied-cell/spatial assumptions when backpack opportunity cost matters.
- Separate direct stat contribution from ability/passive/behavior realization when evidence differs.
- Label inherited provisional baselines; downstream calculations do not upgrade their evidence quality automatically.

## Output discipline
A canonical balance artifact should make clear: question, scope/exclusions, source ownership, scenario fixtures, formulas/evaluation order, assumptions/confidence, evidence tier, findings, accepted decision or temporary decision, exit/revisit trigger, and links to numeric workbooks/config.

Large matrices and live numeric tables stay in their owned workbook/config. The KB stores interpretation, methodology, constraints, and accepted decisions.

## Current project process
Follow the receiving project's active balance roadmap, deferred gates, evidence ladder, and non-destructive-pass rules. The source project's `Game Balance Roadmap.md`, numeric fixtures, and M4/M5 milestones remain project-owned; they are not prerequisites or default state for another game.
