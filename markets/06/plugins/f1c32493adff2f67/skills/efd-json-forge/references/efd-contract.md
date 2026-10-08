# EFD 2.1 authoring contract

Use `efd-2.1.schema.json` as the normative structural contract. This note defines the engineering meaning that must survive generation, validation, and repair.

## Required root projections

The document requires `schemaVersion`, `workspace`, `project`, `organizationUnits`, `positions`, `process`, `layout`, and `drawioMapping`. Optional participant registries include authority levels, AI workers, external parties, and system actors.

`process` contains stages, nodes, and semantic edges. `layout` contains geometry. `drawioMapping` contains editor interoperability identities. Never infer business responsibility from the latter two.

## Stable identity

Use stable identifiers matching the schema pattern. Prefer meaningful type prefixes such as `ORG-`, `PRJ-`, `UNIT-`, `POS-`, `PROC-`, `STG-`, `TASK-`, `DEC-`, `EVT-`, `ART-`, `EXC-`, `SYS-`, and `AIW-`. Renaming a display name must not change its stable identifier.

## Responsibility

An organization unit defines the responsibility boundary. A position defines the participating function or job. RACI belongs to a specific node and references a participant by ID. Color is visual identity only and never determines responsibility.

Every executable TO-BE task should have an `R` and normally exactly one human `A`. Missing facts may be preserved for AS-IS discovery but must be surfaced as warnings. Never fabricate an accountable position.

## Flow semantics

Edges carry a semantic type such as sequence, decision outcome, exception, escalation, rework, information, or document flow. A reversed arrow changes business direction; it is not merely styling.

Decision nodes require explicit outcomes. Exceptions need a route to notification, ownership, correction, verification, recovery, or closure as established by the source.

## Evidence and AI

Artifacts are files, forms, records, datasets, notices, or reports. Evidence requirements prove the basis, execution, or result of work. Do not treat an output file or AI answer as sufficient evidence without source support.

AI participation must state scope, permissions, oversight, stopping conditions, and acceptance where the schema supports them. AI is not the default final accountable party.

## Layout projection

Generate readable deterministic geometry after semantics are complete. Stages form the vertical process progression and organization units form horizontal responsibility lanes. Avoid overlap and use orthogonal paths. Layout values must not change organization, position, RACI, or edge direction.

## Validation order

1. JSON parsing.
2. JSON Schema validation.
3. stable-ID uniqueness.
4. reference integrity.
5. start/end and reachability checks.
6. decision branch checks.
7. node-level responsibility warnings.
8. layout and draw.io mapping integrity.

Errors block delivery. Warnings and pending facts must be reported plainly.
