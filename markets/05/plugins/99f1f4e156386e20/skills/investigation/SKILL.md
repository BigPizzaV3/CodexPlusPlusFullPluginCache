---
name: investigation
description: Use when starting or governing an evidence-backed Microsoft security investigation.
---

Purpose: create a bounded case, plan safe pivots, and preserve facts, inferences, alternatives and approval boundaries.

Prerequisites: authenticated MCP caller and an explicit entity or case ID.

Inputs: entity value, objective, priority, lookback window.

Workflow: `start_security_investigation` → `run_investigation_plan` or domain hunts → evidence graph/timeline → quality, confidence and closure assessments.

Allowed tools: read-only hunting, local case/evidence/graph/report tools.

Security constraints: no external response execution; no raw-result persistence; no verdict from a single signal.

Output: case ID, reproducible evidence references, next safe action, gaps and stop condition.

Failure modes: unavailable tenant connector, insufficient scope, unknown schema, no safe template, contradictory evidence.

Tests: MCP workflow, evidence graph, confidence, closure readiness.
