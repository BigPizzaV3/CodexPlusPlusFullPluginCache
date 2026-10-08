---
name: runtime-audit
description: Verify or reconcile canonical game design against code, designated live configuration, synced CSV, builds, logs, and runtime evidence.
---

# Runtime Audit Skill

Apply the [receiving-project contract](../../references/project-context.md) to resolve canonical sources, project paths, and companion skills.

## Goal
Verify what the game actually does without silently converting implementation evidence into design intent, and surface actionable drift between canonical design, structured config, release artifacts, and runtime behavior.

## Trigger
Use for code inspection, config/runtime verification, mapping checks, implementation audits, build/test evidence, or design↔runtime reconciliation. Activate `knowledge-steward` when findings change durable KB knowledge.

## Evidence roles
- Canonical KB → accepted design intent/rules.
- Designated live configuration (for example, `BlueprintData` in a project that uses it) → current structured configuration used by the game; proves configured values, not final design/balance approval.
- Synced repository CSV → release-build artifact expected to match an approved Sheet snapshot; mismatch is a sync observation unless another owner establishes a design defect.
- The designated repository/code → implemented behavior and schemas.
- Build/log/test → observed runtime behavior for the tested version/environment.

## Required workflow
1. Read the available project guide, current state and relevant domain context resolved through the receiving-project contract, then the smallest canonical document set.
2. State the exact audit question and expected canonical behavior.
3. Read only the code/config paths required to answer it; avoid broad repository scans unless dependency discovery requires expansion.
4. Capture exact evidence: file/path, class/method/system, config table/row/field, build/test version, or log reference as applicable.
5. Classify each finding as `Matches design`, `Config drift`, `Implementation drift`, `Unspecified runtime behavior`, `Design ambiguity`, or `Validation gap`.
6. Do not silently choose a winner when sources conflict. Apply Source-of-Truth ownership and surface unresolved intent to the owner.
7. Distinguish a runtime defect from an outdated GDD, provisional config, release-sync issue, or intentionally deferred implementation.
8. For approved corrections, update the smallest authoritative source(s), then read back and record any remaining validation requirement.

## Audit report minimum
Include question, canonical expectation, evidence locations, observed behavior/config, classification, impact, recommended owner/action, confidence/evidence level, and whether the finding changes current `_Context.md` or `PROJECT_STATE.md`.

## Safety against re-derivation
Once a verified runtime semantic has been compiled into an active canonical/current-state artifact, do not re-audit it on every task. Reopen code/config when the implementation changed, evidence is stale/uncertain, a conflict appears, or the task explicitly requires verification.
