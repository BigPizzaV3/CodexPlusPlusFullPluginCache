---
name: council-external-ai-handoff
description: Use when work can be delegated to another AI, model, or platform to save cost, tokens, or time while the Executive Council retains specification, authority, and validation.
---

# Council External AI Handoff

## Goal
Use the cheapest/simplest adequate external AI for bounded work without outsourcing judgment, secrets, authority, or Source of Truth.

## Workflow
1. Define the exact work unit to delegate.
2. Decide whether delegation is actually cheaper/faster than doing it here.
3. Choose platform/model based on current capability, limits, privacy, and cost when those facts matter.
4. Remove all context not required for the task.
5. Never send passwords, tokens, full health/relationship history, full financial state, or sensitive documents when a redacted extract will do.
6. Build the handoff:
   - Objective
   - Inputs
   - Constraints
   - Required output format
   - What must not be assumed
   - Acceptance criteria
   - Examples only when they materially improve reliability
7. If an authorized connector/tool exists, execute the handoff.
8. If no connector exists, give Samuel one copy-paste payload and only the unavoidable manual step.
9. On return, validate the output against acceptance criteria and canonical facts.
10. Promote only verified results into Council work/state.

## Model selection
Prefer a free or lower-cost model when it satisfies the quality threshold.
Use a stronger model for:
- ambiguous synthesis;
- high-risk reasoning;
- difficult code/debugging;
- long-context accuracy;
- tasks where rework costs more than model savings.

## Good candidates for delegation
- first-pass extraction;
- reformatting;
- classification with a clear schema;
- boilerplate;
- broad ideation;
- draft code under tests;
- source collection to be independently verified.

## Keep final authority inside the Council
Do not outsource final authority for:
- clinical/health decisions;
- legal conclusions;
- material financial authorization;
- irreversible relationship decisions;
- final Source-of-Truth updates;
- acceptance/verification itself.

## Failure rule
External AI output is untrusted work product until validated.
