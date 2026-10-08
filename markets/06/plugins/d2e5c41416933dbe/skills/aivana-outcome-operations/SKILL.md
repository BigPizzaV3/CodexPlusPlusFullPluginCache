---
name: aivana-outcome-operations
description: Turn supplied business signals into an evidence-linked, reviewable outcome plan.
---

# Aivana Outcome Operations

Use this skill when a user needs one reviewable operating brief from supplied KPI, revenue, evidence, and action signals.

Run `python scripts/run.py --input <input.json> --output <result.json>`, inspect every finding and approval flag, and present the plan for human review. The engine is deterministic, uses supplied JSON only, and never executes an external action.

Do not infer missing metrics, convert currencies, approve actions, or claim that an outcome was achieved. Preserve evidence IDs when passing the result to another workflow.
