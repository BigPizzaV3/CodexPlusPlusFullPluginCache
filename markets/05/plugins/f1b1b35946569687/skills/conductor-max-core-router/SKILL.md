---
name: conductor-max-core-router
description: Select the smallest sufficient subset of the user's core engineering plugins for repository understanding, implementation, architecture, PR work, benchmarking, runbooks, and trivial edits. Explicit plugin requests override automatic selection. Do not trigger for ordinary non-project chat.
---

# Conductor Max Core Router

Act as the single engineering entrypoint. Route the current task; do not physically enable, disable, install, uninstall, or configure plugins.

## Routing contract

Classify the available core capabilities for every in-scope task as:

- **REQUIRED** — necessary for this task.
- **OPTIONAL / CONDITIONAL** — use only when its condition is present.
- **OFF FOR THIS TASK** — everything else.

Core invariant: use the **smallest sufficient subset**. Never fan out to the full stack just because it is installed.

An explicit user request overrides automatic selection. For example, `@pstack review this architecture` selects pstack. An explicitly named capability is limited to the current task; it does not make it permanently required.

The router selects only among these capabilities:

- Selective Intelligence
- PMC
- pstack
- gstack Workflows
- Riqor
- Develoop
- PR Completion
- Generate Runbook
- Progressive Clarity
- CompText Benchmark
- CompText Context
- CompText Evidence
- CompText Guard

If a selected capability is unavailable, continue with the smallest available subset where possible. State the missing capability only when it prevents the requested outcome. Never claim that a plugin was used unless it was available and invoked (or its instructions were loaded).

## Default routes

### Repository understanding

- REQUIRED: Selective Intelligence; CompText Context
- OPTIONAL / CONDITIONAL: PMC for durable or stale project state

### Normal non-trivial implementation

- REQUIRED: Selective Intelligence; CompText Context; Riqor
- OPTIONAL / CONDITIONAL: pstack for architecture; CompText Guard before relevant operations; CompText Evidence after mutation

### Architecture design

- REQUIRED: Selective Intelligence; pstack
- OPTIONAL / CONDITIONAL: gstack Workflows for an engineering review; CompText Context when project context materially affects the design

### PR review

- REQUIRED: Selective Intelligence; Riqor; Develoop
- OPTIONAL / CONDITIONAL: none by default
- OFF FOR THIS TASK: PR Completion unless landing or completion is explicitly requested

### PR completion

- REQUIRED: Riqor; Develoop; PR Completion
- OPTIONAL / CONDITIONAL: CompText Evidence for final proof

Preserve every explicit merge-approval gate.

### Benchmark

- REQUIRED: CompText Benchmark; CompText Evidence
- OPTIONAL / CONDITIONAL: Riqor when specialist interpretation is needed

### Operational runbook

- REQUIRED: Generate Runbook
- OPTIONAL / CONDITIONAL: CompText Guard for relevant operations; Riqor for repository evidence

### Trivial edit

- REQUIRED: only the minimal capability actually required
- OPTIONAL / CONDITIONAL: none by default

## Safety and reporting

- Read state first when repository or host state is uncertain.
- Do not merge, deploy, publish, delete, change access, or perform another external effect without the precise authority required.
- Preserve unrelated dirty work.
- A mutation invalidates earlier evidence for its changed boundary.
- For ordinary work, execute rather than narrating the routing decision. If asked which workflow is active, report only REQUIRED and OPTIONAL / CONDITIONAL capabilities with the reason for each.

Read `references/routing.md` only when the request spans multiple phases or has a routing conflict.
