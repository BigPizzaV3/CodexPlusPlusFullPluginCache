---
name: xdr-hunting
description: Use when translating user intent into bounded, validated Microsoft Defender XDR KQL and running it through the direct API.
---

Purpose: translate user intent into KQL, execute it through the direct OAuth-protected API, and return bounded evidence.

Prerequisites: a concrete investigative question and OAuth authorization for the user's tenant.

Inputs: entity or validated KQL, lookback, selected fields and result cap.

Workflow: translate intent → preview/validate KQL → execute bounded read-only query → summarize result → save compact case fact.

Allowed tools: KQL translation, validation, direct API execution, entity templates and evidence tools.

Security constraints: no management commands, external data, wildcard search/union, raw result persistence or automated verdict.

Output: bounded result summary, source query, evidence reference and next review pivot.

Failure modes: quota, missing table, insufficient role, no data, unsafe query or schema mismatch.

Tests: KQL validator, direct API and result-summary tests.
