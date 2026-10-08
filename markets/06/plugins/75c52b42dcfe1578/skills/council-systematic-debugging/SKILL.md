---
name: council-systematic-debugging
description: Use for bugs, broken automations, integration failures, unexpected behavior, performance problems, bad outputs, or repeated failed attempts in the Executive Council.
---

# Council Systematic Debugging

The current Google Drive Source of Truth, domain rules, platform/system instructions, and Samuel's explicit current request override this skill.

## Protocol
PARAR → preserve last valid state → locate bottleneck → form one hypothesis → change only what tests it → test → verify.

## Phase 1 — Reproduce and localize
1. State the observed symptom without interpretation.
2. Reproduce if possible.
3. Read the full error, log, or output already available.
4. Identify recent relevant changes.
5. Map component boundaries.
6. Find the first layer where expected input/output diverges.

## Phase 2 — Hypothesis
State one falsifiable hypothesis:
"I think X is failing because evidence Y; test Z distinguishes it."

Do not stack speculative fixes.

## Phase 3 — Minimal test
Change the smallest reversible variable that discriminates the hypothesis.
Record the result.
If false, discard the hypothesis and use the new evidence.

## Phase 4 — Correct
Fix the root cause, not the visible symptom.
Preserve rollback when the change is persistent or material.

## Phase 5 — Verify
Use `council-verification-gate` before claiming success.

## Three-failure gate
After three materially different failed fixes:
- stop adding patches;
- question the architecture or assumed layer;
- recover from the last valid state;
- escalate only the exact architectural decision that now requires authority.

## Prohibited
- random command sequences;
- blind reinstall/reset/restart as a reflex;
- changing multiple variables when causal attribution matters;
- discarding valid work and starting over merely because debugging became difficult.
