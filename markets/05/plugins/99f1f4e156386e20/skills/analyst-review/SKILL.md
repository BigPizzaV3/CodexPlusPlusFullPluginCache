---
name: analyst-review
description: Use when preparing or reviewing a reproducible security evidence package.
---

Purpose: hand a bounded investigation to a human analyst with facts, inferences, alternatives, and explicit response boundaries.

Prerequisites: an existing case and reproducible evidence references.

Inputs: case ID, evidence package, analyst decision, and evidence IDs.

Workflow: retrieve evidence package → assess quality and confidence → record analyst review → choose a bounded next step or closure recommendation.

Allowed tools: case evidence package, quality, confidence, review, closure-readiness, and outcome-agent brief tools.

Security constraints: no automated response, case closure, or verdict; human review remains required.

Output: review-ready package, recorded decision, evidence gaps, and next safe action.

Failure modes: missing evidence, inconsistent hypotheses, insufficient reviewer authority, or unresolved response proposal.

Tests: evidence package, review, confidence, closure-readiness, and autonomy-boundary tests.
