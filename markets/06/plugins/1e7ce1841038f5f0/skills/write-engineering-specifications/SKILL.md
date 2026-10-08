---
name: write-engineering-specifications
description: Create implementation-ready engineering specifications, technical design documents, feature specifications, architecture briefs, and developer or coding-agent handoffs for software systems. Use when a website, app, SaaS product, API, database, automation, AI agent, game, tool, internal system, feature, migration, refactor, integration, or technical change must be documented precisely before implementation, including scope boundaries, affected files, interfaces, states, edge cases, tests, regression checks, risks, and verifiable acceptance criteria. Do not use for writing the implementation itself unless the user also requests coding.
---

# Engineering Specification Writer

Create a technical contract that lets a competent developer or coding agent implement the intended change without inventing product requirements, scope, architecture, or design decisions.

## Establish evidence and authority

Before drafting:

1. Identify the requested outcome, intended users, implementation audience, current system, and delivery format.
2. Inspect available repositories, files, schemas, routes, interfaces, screenshots, designs, logs, tests, and existing documentation. Do not describe uninspected internals as fact.
3. Classify information as `Verified`, `User decision`, `Proposed`, `Assumed`, `Unknown`, or `Requires approval`.
4. Record what may change, what must remain unchanged, affected dependencies, authorization limits, and recovery requirements.

When a missing decision materially changes behavior or architecture, stop specification of that section, state the ambiguity and impact, recommend a default if safe, and request the decision. Do not hide invented decisions inside confident technical prose.

## Choose specification depth

- **Contained change:** concise feature or bug-fix specification covering affected behavior, files, tests, and regression boundaries.
- **Cross-cutting feature:** full functional, data, interface, architecture, security, observability, migration, and test specification.
- **New system:** system context, components, data ownership, interfaces, deployment, operations, quality attributes, staged delivery, and acceptance.
- **Migration or refactor:** before/after architecture, invariants, compatibility, sequencing, data migration, rollback, and proof of equivalence.
- **Visual implementation:** load [ui-specification.md](references/ui-specification.md) and document every relevant state and responsive rule.
- **API or data change:** load [interface-and-data-contracts.md](references/interface-and-data-contracts.md).

Scale detail to risk and complexity. Avoid both vague briefs and ceremonial documents that add no implementation value.

For visual, experiential, 3D, or representation-sensitive work, also apply the shared [false-precision policy](../../shared/expert-system/false-precision-policy.md), [observable ownership model](../../shared/expert-system/observable-ownership.md), [representation strategy contract](../../shared/expert-system/representation-strategy-contract.md), and [decision-authority model](../../shared/expert-system/decision-authority-model.md).

For any product-facing or user-affecting scope, use the shared [Product Quality Principles](../../shared/expert-system/product-quality-principles.md) to identify only applicable requirements. Carry purpose, agency/recovery, responsibility/privacy, familiarity, supported-context flexibility, purposeful simplicity, craft and delight into traceable requirements or acceptance where material; do not turn them into boilerplate or invent product decisions.

## Audit the current state

Document only relevant existing:

- system context and architecture;
- routes, components, services, jobs, agents, data stores, and external integrations;
- current behavior and user flow;
- file or module ownership;
- interfaces and dependencies;
- constraints, known defects, risks, and protected behavior;
- baseline tests and observable performance where available.

Map each factual statement to inspected evidence using paths, symbols, route names, schema names, screenshots, or source references. Mark inaccessible areas `Not verified`.

## Define requirements precisely

For each requirement assign a stable ID such as `FR-001`, `NFR-001`, or `AC-001` and include rationale, priority, dependencies, and verification method.

Functional requirements must define trigger, preconditions, behavior, inputs, validation, outputs, state changes, permissions, errors, and postconditions. Non-functional requirements must be measurable or explicitly testable; never use “fast,” “secure,” “scalable,” “modern,” or “accessible” without a threshold, standard, workload, threat, or test.

Maintain traceability from problem → requirement → design element → implementation area → test → acceptance criterion.

## Specify the technical design

Use [specification-template.md](assets/specification-template.md) as the output skeleton and remove non-applicable sections rather than filling them with noise. Define as applicable:

- system context and boundaries;
- components and responsibilities;
- synchronous and asynchronous flows;
- APIs, events, schemas, state, persistence, ownership, and lifecycle;
- authentication, authorization, secrets, privacy, and abuse controls;
- error behavior, retries, idempotency, timeouts, rate limits, concurrency, and recovery;
- performance budgets, capacity assumptions, caching, and degradation;
- observability, audit logs, metrics, alerts, and support diagnostics;
- deployment, configuration, feature flags, migrations, compatibility, rollback, and removal plan;
- accessibility, localization, platform, browser, and device support;
- scope-relevant global readiness, search/discoverability, product longevity/currentness and maintenance triggers;
- for AI systems, model/prompt/tool/retrieval identity, behavioral evaluation sets and criteria, grounding/unknown/refusal behavior, adversarial safety, consequential-action control, observability and regression;
- affected files or modules and their exact intended change.

Use diagrams only when relationships or sequences are materially clearer visually. Label proposed architecture as proposed; do not imply it already exists.

## Control implementation scope

Create separate lists:

- `Create`
- `Modify`
- `Preserve unchanged`
- `Prohibited without approval`
- `Delete or deprecate`, only when explicitly authorized

For every affected file or module state its purpose, planned change, constraints, dependencies, and associated requirement IDs. When exact paths cannot be known before implementation, specify the module or responsibility and mark path assignment as an implementation decision bounded by the documented architecture.

Do not require a developer to follow a technically unsound implementation merely because an early path or library guess was made. Freeze product behavior, invariants, interfaces, and acceptance criteria; allow bounded engineering choices when evidence is insufficient, recording them in a decision log.

## Define behavior and edge cases

Describe main flows as precondition → trigger → validation → processing → persistence or side effect → response → UI/system update → observability. Cover relevant empty, loading, success, partial, error, offline, timeout, retry, duplicate, concurrent, stale, unauthorized, malformed, boundary, accessibility, and recovery states.

Do not create imaginary edge cases. Derive them from inputs, state transitions, dependencies, trust boundaries, and failure modes.

## Build the verification contract

Read [verification-and-handoff.md](references/verification-and-handoff.md). Define tests before implementation, including applicable unit, integration, contract, end-to-end, migration, performance, security, accessibility, responsive, compatibility, recovery, and regression checks.

Every acceptance criterion must be binary or objectively reviewable, identify its evidence, and trace to requirements. State the tested scope; never claim complete security, accessibility, performance, or regression coverage from a partial test.

## Prepare coding-agent instructions

End the document with an implementation directive that says:

- implement only approved scope;
- preserve named invariants and protected areas;
- do not add features or redesign interfaces;
- do not refactor unrelated code;
- follow existing repository conventions unless the specification explicitly changes them;
- surface conflicts between specification and repository evidence before proceeding;
- when a blocking decision is missing, report the issue, affected requirement, options, and recommendation, then await approval;
- run specified checks and report actual results without fabrication;
- provide a concise change manifest and residual risks.

This restriction does not prohibit routine local engineering judgment such as variable naming or equivalent internal structure when it does not alter documented behavior, architecture, interfaces, risk, or scope.

## Deliver

Provide:

1. implementation-ready specification;
2. decision and assumption log;
3. requirement-to-test traceability matrix;
4. unresolved blockers and approvals;
5. developer or coding-agent handoff prompt;
6. source/evidence index.

Use `$create-professional-documents` when the user requests a polished DOCX or PDF artifact. Use `$execute-premium-projects` only when implementation and verification are also requested; specification alone does not authorize code changes.

## Single specification and suite contribution

- `SINGLE SPEC` owns one contained engineering contract from evidence through document-level verification.
- `SPEC SUITE CONTRIBUTION` authors only the artifact and decision areas assigned by an approved Documentation Blueprint from `$architect-implementation-documentation`. Preserve suite IDs, metadata, sources, boundaries, dependencies, and precedence; do not redefine the suite.

Use suite-contribution mode only when the Blueprint identifies artifact, owned decisions, required inputs, target status, dependencies, and acceptance checks. Otherwise report the missing control information.

Do not mark a specification `FINAL` until its declared scope is approved, decision-complete, internally consistent, reference-resolvable, and document-level verified. In a suite, document finality does not imply whole-suite readiness.

For every area ask: **Could the developer make an unauthorized Class-1 decision or exercise Class-2 judgment without an approved role, target, bounds, evidence, checkpoint, and reviewer?** If yes, record `ENTSCHEIDUNGSLÜCKE` and obtain the responsible decision.

Do not freeze every visible parameter. Protect product, brand, architecture, interfaces, security, data, scope, invariants, and observable relationships with exact decisions where evidence supports them; classify the rest as `TARGET`, `BOUND`, `PROFESSIONAL_DISCRETION`, `ENGINEERING_DISCRETION`, `CALIBRATION_REQUIRED`, `VERIFY_AT_RUNTIME`, or `PERCEPTUAL_ACCEPTANCE`. A final visual specification may contain these controlled classes. Unsupported exactness is false precision, not readiness.

For important visible components define relationship specifications, one primary owner per material observable, the active representation method/status, applicable proof or remaining calibration, local checkpoints, perceptual acceptance, and independent review. List representation candidates only while the method is legitimately open; carry an applicable `METHOD_CLOSED` decision into the specification without reopening it. Correct compliance with a defective specification is not success.

Record artifact version, status, owner, date, source IDs, `extends`, `overrides`, `supersedes`, and downstream dependencies. For suite contributions, verify cross-document interfaces, terminology, versions, dependencies, and precedence. Route whole-suite readiness to `$project-specification-auditor`; never self-certify the package.
