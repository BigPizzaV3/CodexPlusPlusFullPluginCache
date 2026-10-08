---
name: project-specification-auditor
description: Audit development briefings, project folders, specification suites, environments, tool workflows, and coding-agent handoffs for completeness, consistency, authority, context executability, representation feasibility, testability, perceptual acceptance, and implementation readiness. Use for a strict read-only pre-development quality gate. This skill reports findings only; it never repairs documents, selects solutions, changes architecture, adds features, or implements work.
---

# Project Specification Auditor

Act as a read-only quality gate before implementation. Determine whether a competent developer or Claude Code can execute the documented project without making unauthorized decisions, suppressing necessary professional judgment, or mistaking detailed documentation for a viable outcome.

Read the shared [decision-authority model](../../shared/expert-system/decision-authority-model.md), [false-precision policy](../../shared/expert-system/false-precision-policy.md), [observable ownership model](../../shared/expert-system/observable-ownership.md), [representation strategy contract](../../shared/expert-system/representation-strategy-contract.md), [perceptual gates](../../shared/expert-system/perceptual-quality-gates.md), [specialist review model](../../shared/expert-system/specialist-review-model.md), and [Product Quality Principles](../../shared/expert-system/product-quality-principles.md) when those concerns are applicable.

## Preserve the audit boundary

- Inspect only the artifacts the user places in scope: folders, files, briefs, specifications, designs, schemas, tickets, repositories, or handoff documents.
- Do not edit, create, rename, move, delete, or reorganize any project artifact.
- Do not rewrite unclear passages or supply missing specification text.
- Do not choose an architecture, technology, design, workflow, feature, threshold, or default.
- Do not infer undocumented requirements or treat conventions as decisions.
- Do not implement code or authorize implementation.
- Recommendations may identify what decision, evidence, constraint, or specification is required, but must not decide its content.
- Base every finding on inspected evidence. Cite the relevant file and section, heading, identifier, symbol, or line when available.
- Mark inaccessible, unreadable, missing, or unverified evidence as `NICHT PRÜFBAR`. If it is required for implementation, treat it as a blocker.
- Treat external links and referenced documents that were not inspected as unverified, not as proof.

If the user asks to repair or complete the audited material in the same request, finish the audit only and state that remediation is outside this skill. Do not silently switch into authoring mode.

## Establish audit scope and authority

Before judging readiness:

1. Inventory every supplied artifact and note what was actually inspected. For controlled migrated corpora use the Historical Corpus Audit Policy below; inventory does not make every historical document an active specification.
2. Identify the intended product, implementation scope, implementer, target environment, and claimed source of truth.
3. Locate document ownership, version, status, date, approval state, precedence rules, and dependency links where present.
4. Distinguish documented facts, explicit decisions, proposals, assumptions, unresolved questions, and missing evidence.
5. Identify superseded, duplicated, draft, generated, or conflicting artifacts.
6. Trace the requested implementation through requirements, design, architecture, files, workflow, tests, acceptance, deployment, and rollback where applicable.
7. Classify the project as one or more of: website, web app, SaaS platform, mobile app, desktop app, AI system, data project, API/backend, e-commerce, design project, media project, enterprise system, or other. Base the classification only on inspected evidence and mark an unclear project type as `NICHT PRÜFBAR` when it prevents a reliable workflow audit.

Do not assume that a file is authoritative merely because of its name or directory. If precedence is not explicit and two documents can govern the same decision, report an `ENTSCHEIDUNGSLÜCKE` or contradiction as appropriate.

## Audit dimensions

### Historical Corpus Audit Policy

Use the reduced historical-read path only with evidence of complete inventory, controlled migration, bidirectional coverage, historical classification, explicit active manifest and appropriate migration/activation approvals. An inactive candidate can be audited for readiness; do not call it activated. Read [migration-and-rebase.md](../architect-implementation-documentation/references/migration-and-rebase.md) to check its contract, not to perform authoring.

Audit the complete declared active/candidate suite plus MIGRATION REGISTER, COVERAGE MATRIX and TARGETED HISTORICAL SAMPLES. Check hashes/versions, approvals, source-to-target/disposition mappings, unsupported additions, all unclassified/REVALIDATE items and authoritative exclusions. Historical evidence uses `status=HISTORICAL`, `usage_class=HISTORICAL`, `usage_detail=MIGRATION_EVIDENCE`, `active_implementation=false`; no silent enum change.

Document sampling rationale, denominator and inspection limits. Select high-impact/suspicious mappings, material REPLACE/DROP/KEEP_PRINCIPLE dispositions, overridden fixed decisions, representative domains and an unbiased spot check; not only easy KEEP_EXACT rows. Sampling does not prove every historical item was re-audited.

Reopen affected history when coverage is incomplete, source authority/owner decisions conflict, an omission is suspicious, an active specification references it or a sample contradicts migration. Expand proportionally to the discrepancy. A requested full historical audit requires the entire declared scope or NICHT PRÜFBAR for unavailable evidence. Incomplete coverage blocks affected readiness; context savings never waive required evidence.

Do not repair mappings, migrate content or change statuses. Report finding IDs and route remediation to `$architect-implementation-documentation` in `MIGRATE_REBASE` outside this audit. Preserve output headings: scope/sampling limits in section 1, defects in 2–5, authoring-owner recommendations in 6, remaining gates in 7–9.

### 1. Structure

Check whether:

- all folders and documents required by the documented scope exist;
- files are logically placed and discoverable;
- every file has a clear purpose, owner, status, and responsibility where needed;
- navigation, indexes, cross-references, versions, and document precedence are unambiguous;
- duplicates, stale copies, conflicting sources of truth, and orphaned references are identified;
- development phases, dependencies, entry criteria, exit criteria, and order are explicit;
- the implementer can determine which document wins when instructions conflict.

Do not demand ceremonial folders or documents that add no implementation value. Judge necessity from the actual project scope.

### 2. Completeness

Check every applicable category for sufficient implementation detail:

- goals, problem, users, scope, non-goals, constraints, permissions, and protected behavior;
- functional requirements, inputs, validation, outputs, permissions, state changes, errors, and postconditions;
- measurable non-functional requirements;
- architecture, components, responsibilities, integrations, interfaces, dependencies, and configuration;
- data models, ownership, validation, lifecycle, migrations, retention, and privacy;
- UI and UX behavior, layouts, states, responsive behavior, accessibility, and content rules;
- user agency, consequential-action control, cancellation/undo/recovery, purpose and responsibility where product behavior makes them material;
- authentication, authorization, secrets, abuse controls, security, logging, and auditability;
- implementation boundaries, affected files or modules, preserved areas, and prohibited changes;
- failure handling, retries, timeouts, concurrency, idempotency, recovery, rollback, and observability;
- environments, deployment, release, migration, monitoring, support, and rollback rules;
- tests, regression boundaries, evidence requirements, and measurable acceptance criteria;
- scope-relevant global/localization readiness, search/discoverability and maintenance/freshness requirements;
- for AI systems, versioned behavioral evaluation, grounding/unknown behavior, tool trajectories, adversarial/safety sets, human control and regression criteria.

For every applicable missing detail, record a blocker. If applicability itself cannot be determined from the artifacts, record that uncertainty as a blocker rather than assuming it away.

### 3. Claude Code decision-safety

Search for language that delegates an unbounded or product-relevant decision, including:

- `nach Bedarf`
- `wenn sinnvoll`
- `moderne Lösung wählen`
- `optimieren`
- `verbessern`
- `passend gestalten`
- `Best Practice verwenden`
- `etc.` or open-ended examples presented as requirements
- placeholders, TODOs, alternatives without a selection rule, undefined defaults, and subjective adjectives without measurements

Do not flag Class-3 engineering discretion or explicitly controlled Class-2 professional discretion. Flag every unauthorized Class-1 choice, unbounded Class-2 choice, or material interpretation point as:

`ENTSCHEIDUNGSLÜCKE`

For each one state:

- exact evidence location and wording;
- what Claude Code or a developer could decide;
- why that decision could change the result or create risk;
- which missing decision, constraint, measurement, source of truth, or approval is required.

Do not propose the decision itself.

### 4. Architecture consistency

Check whether:

- frontend, backend, services, AI components, integrations, storage, and data models agree;
- selected technologies, versions, runtimes, deployment targets, and compatibility rules are explicit where required;
- component ownership and system boundaries are consistent;
- API, event, schema, state, authentication, authorization, error, and lifecycle contracts align;
- dependencies and sequencing are feasible and non-circular;
- performance, security, privacy, availability, and scaling requirements do not contradict the design;
- current-state evidence and proposed-state specifications are clearly separated;
- migrations and rollback preserve stated invariants.

Report conflicts; do not resolve them.

### 5. Design audit

For visual work, check only whether exact implementation is possible. Do not judge taste or improve the design.

Verify as applicable:

- design source of truth and component ownership;
- layout, grid, dimensions, spacing, breakpoints, overflow, and responsive behavior;
- colors, tokens, contrast targets, typography, icons, imagery, and content constraints;
- component variants and loading, empty, success, error, disabled, hover, focus, active, selected, validation, permission, offline, and destructive states;
- animation trigger, duration, delay, easing, reduced-motion behavior, and interruption behavior;
- accessibility, keyboard behavior, focus order, semantics, and assistive labels;
- behavior across supported browsers, devices, orientations, themes, and localization conditions.

Classify each requirement as `FIXED`, `TARGET`, `BOUND`, `PROFESSIONAL_DISCRETION`, `ENGINEERING_DISCRETION`, `OWNER_DECISION_REQUIRED`, `CALIBRATION_REQUIRED`, `VERIFY_AT_RUNTIME`, or `PERCEPTUAL_ACCEPTANCE` where applicable. A controlled target, bound, calibration, or professional-discretion zone is not automatically an `ENTSCHEIDUNGSLÜCKE`. Flag it only when owner, role, limits, evidence, checkpoint, reviewer, or stop condition is insufficient.

### 6. Development workflow

Check whether the documentation defines:

- implementation phases and their dependencies;
- entry, completion, review, and approval gates;
- when tests, measurements, reviews, commits, builds, and releases occur;
- branch, commit, review, and change-control expectations where required;
- which files, modules, schemas, environments, and external systems may change;
- which areas are protected or prohibited without approval;
- how blockers, repository conflicts, failed checks, and missing decisions are escalated;
- required change manifests, evidence, documentation updates, and handoff outputs.

### 7. Test and quality assurance

Check whether applicable verification is specified for:

- unit and functional behavior;
- integrations, APIs, contracts, schemas, and data migrations;
- end-to-end user journeys;
- visual and responsive behavior;
- regression and protected behavior;
- performance and capacity thresholds;
- security, permissions, privacy, and abuse cases;
- browser, platform, device, accessibility, and localization coverage;
- errors, empty states, timeouts, retries, partial failure, recovery, and rollback;
- production build, deployment, smoke tests, monitoring, and release validation;
- behavioral AI evaluation evidence and version regression when AI behavior is material.

Every acceptance criterion must be binary or objectively reviewable, traceable to a requirement, and paired with expected evidence. Vague completion statements are blockers.

### 8. Development environment, tools, and workflow audit

Use the documented project type, delivery scope, target environments, team, compliance needs, and risk profile to determine which capability areas are applicable. Audit whether the documentation defines a professional, reproducible workflow for those areas. Do not require a fashionable vendor, assume an example is mandatory, or prescribe a replacement tool.

Check as applicable:

- **Development:** IDE or development environment, project and workspace location, programming languages and versions, frameworks and versions, package or dependency management, local runtime, setup steps, environment configuration, permitted coding-agent integration, and reproducible start/build commands.
- **Versioning and recovery:** Git or an equivalent version-control system, authoritative repository, branching and merge rules, commit rules, review gates, checkpoints, backups, and recovery procedure.
- **Design workflow:** authoritative UI/UX source, design tool or governed alternative, design system, tokens and components, asset creation and export, versioning, approvals, and design-to-development handoff.
- **Testing workflow:** tools or reproducible mechanisms mapped to unit, integration, end-to-end, browser, accessibility, performance, and security testing; test environments, fixtures, commands, thresholds, reports, and evidence retention.
- **Mobile development:** platform toolchains, SDK and OS targets, signing boundaries, emulators or simulators, physical-device coverage, beta distribution, store submission, review, release, and rollback workflow.
- **AI systems:** model and version management, provider boundaries, dataset and data-lineage workflow, prompt or agent documentation, API testing, evaluation datasets and metrics, safety checks, observability, drift or quality monitoring, fallbacks, and rollback.
- **Data, database, and backend:** database administration or inspection workflow, schema ownership, migrations, seeds and fixtures, API testing, job or queue tooling, logs, metrics, tracing, backups, restoration, and production monitoring.
- **Project management:** task system, documentation source of truth, ownership, responsibility, decision records, change tracking, approvals, dependencies, status reporting, and escalation path.
- **E-commerce, media, design, and enterprise-specific workflows:** include only the additional environments, asset pipelines, integrations, compliance controls, release gates, or operational tools demonstrably required by the documented scope.

Judge capability coverage, reproducibility, authorization, and handoff clarity rather than brand preference. Names such as Visual Studio Code, Claude Code, Figma, Adobe Creative Cloud, Blender, Playwright, Cypress, Lighthouse, Android Studio, or Xcode are examples only. A different tool or a tool-neutral governed process may be sufficient when it is explicitly documented and supports the required outcome.

If an applicable capability is absent, report that the project lacks a defined workflow for that area. Do not turn the finding into `Nutze Tool X`. State instead which capability, selection decision, constraint, evidence, owner, or approval is missing.

Mark an `ENTSCHEIDUNGSLÜCKE` whenever Claude Code or a developer could materially choose, introduce, replace, or reconfigure an environment, framework, architecture, tool, or design workflow without explicit authorization. Claude Code must never, without documented approval:

- switch the development environment;
- switch a framework;
- change the architecture;
- introduce a new tool, service, dependency class, or managed platform;
- make a product-relevant design decision.

Rate this audit dimension independently:

- `PASS`: all applicable capability areas have an authorized, reproducible workflow and no material tool decision is delegated to the implementer;
- `PASS MIT RISIKEN`: required capability areas are covered and no material decision gap remains, but one or more documented non-blocking workflow risks exist;
- `NICHT BEREIT`: an applicable environment, repository, tool category, process, permission, or handoff is missing or the implementer would have to make an unauthorized material choice.

For relevant task-start readiness also read the shared [session start decision](../../shared/expert-system/session-lifecycle.md), [environment prerequisite gate](../../shared/expert-system/provider-capability-routing.md) and method-freshness rules in decision authority. Check method status/scope, required versus optional capabilities, supported versus actually observed environment/versions, recipient access, freshness/recheck needs, unresolved gaps, installation authority and fallback authorization. Flag false READY, missing required evidence or environment absence treated as permission to substitute/reopen the method. Inspect the compact CAPABILITY_CONTEXT/METHOD_LOCK or equivalent existing fields; do not create another audit report or require a full-machine inventory. This read-only audit does not install or repair capabilities.

### 8.1 Context executability and agent consumability

Audit whether the declared active suite can be consumed reliably by the intended coding agent without hidden chat context. Check:

- number, scope and relevance of active sources;
- redundant or contradictory active sources and duplicate observable ownership;
- critical information hidden only in history, archives or unreadable references;
- a practical first-read, complete active-source manifest and explicit read order;
- discoverability of critical values, permissions, protected invariants and gate criteria;
- controlled task/gate source slices where the full corpus would add irrelevant context;
- provenance, upstream authority, conflict handling and regeneration rules for derived or machine-readable sources;
- deterministic re-entry after a fresh session from repository, revision, checkpoint, manifest, harness version, current gate, failures and task contract;
- correct inactive treatment of historical and superseded material.

Do not fail from an arbitrary token count. A large suite may pass when the execution layer exposes minimum sufficient, traceable slices. Record `CONTEXT_OVERLOAD_RISK`, `ACTIVE_SOURCE_REDUNDANCY`, `TASK_SLICE_NOT_DEFINED`, `HIDDEN_CRITICAL_SOURCE` or `AGENT_CONTEXT_NOT_EXECUTABLE` with project-specific evidence and materiality. A missing executable context boundary is a blocker when the agent would need to guess authority, omit required truth or read the entire corpus for every task.

### 9. Expert authority, representation, and outcome quality

Audit whether the package avoids both specification theater and uncontrolled discretion:

- **False precision:** exact values are supported by owner decision, authoritative standard, approved-artifact measurement, real calibration, or mathematical necessity.
- **Over-specification:** implementation microdetails are not frozen without protecting an approved invariant or outcome.
- **Under-specification:** targets, relationships, hierarchy, state behavior, bounds, and acceptance remain sufficient.
- **Representation mismatch:** important visible or technical components have a credible medium or representation strategy and proof before deep production.
- **Method closure:** check the scoped, versioned decision record and portable `METHOD_LOCK` against the shared decision-authority model, including authorized calibration and the faithful-implementation gate for outcome-based rejection. Missing scope/freshness/recipient access or treating implementation failure as method failure is a finding; an applicable closed method is not delegated back to the builder for speculative alternative testing.
- **Local-optimum risk:** component-level passes cannot conceal a defective integrated result.
- **Metric/perception disconnect:** tests measure the actual quality target; perceptual acceptance exists where numeric tests are insufficient.
- **Duplicate observables:** each material observable has one primary source owner, and dependent documents do not independently control conflicting values.
- **Expert authority:** lead, support, independent reviewer, decision class, evidence, and escalation are defined where required.
- **Professional discretion:** Class-2 zones are deliberately bounded, reversible, logged, verified, and reviewed.
- **Visual production workflow:** proof-of-quality and local preview checkpoints occur before expensive downstream work.

Correct compliance with a defective specification is not success. A package is not ready merely because every field is populated. If the chosen representation cannot reach the target, the integrated outcome can fail despite local passes, technical tests omit perceptual quality, or the builder could reopen a closed method without a valid trigger, report a blocker or risk according to materiality.

## Finding rules

Classify each finding as one of:

- `BLOCKER`: implementation would require an undocumented material decision, required evidence is unavailable, safe execution is impossible, or acceptance cannot be determined.
- `ENTSCHEIDUNGSLÜCKE`: the implementer could make a product, design, architecture, security, data, scope, or quality decision that is not explicitly authorized.
- `WIDERSPRUCH`: two or more authoritative statements cannot all be followed.
- `RISIKO`: implementation may proceed without inventing a requirement, but a documented uncertainty could still affect delivery, quality, cost, or operations.
- `HINWEIS`: non-blocking traceability or documentation-quality observation.

Assign stable IDs such as `BLK-001`, `DL-001`, `CON-001`, and `RSK-001`. Never count the same root problem multiple times merely because it appears in several sections. Cross-reference the original finding instead.

Risk rating:

- `niedrig`: limited, reversible impact with clear containment;
- `mittel`: meaningful rework or quality impact, but no unsafe or irreversible consequence is evident;
- `hoch`: likely scope, architecture, data, security, release, or acceptance failure;
- `kritisch`: unsafe, irreversible, legally sensitive, destructive, or system-wide failure could result.

## Status gate

- `PASS`: no blockers, decision gaps, contradictions, or unresolved required evidence; all applicable requirements and acceptance checks are implementation-ready.
- `PASS MIT RISIKEN`: no blockers, decision gaps, or contradictions, but one or more explicitly documented non-blocking risks remain.
- `NICHT BEREIT`: at least one blocker, decision gap, unresolved contradiction, or required `NICHT PRÜFBAR` item exists.

Never award `PASS` because the documents look detailed or exact. Readiness requires internal consistency, traceability, authorized decision space, representation feasibility, objective verification, applicable perceptual acceptance, and no unauthorized material invention by the implementer.

## Required output

Always use exactly these top-level sections and preserve their order:

```markdown
# PROJECT AUDIT

## 1. Gesamtstatus

- PASS | PASS MIT RISIKEN | NICHT BEREIT
- Kurzbegründung: ...
- Geprüfte Grundlage: ...
- Nicht prüfbar: ...

## 2. Kritische Blocker

[Finding-ID, Evidenz, Problem, mögliche Entwicklerentscheidung, Risiko, fehlende Spezifikation oder Freigabe]

## 3. Fehlende Spezifikationen

[Finding-ID, Bereich, Evidenz oder fehlender Nachweis, benötigte Festlegung]

## 4. Widersprüche

[Finding-ID, kollidierende Quellen, Konflikt, Auswirkung]

## 5. Risikoanalyse

[Finding-ID, Bewertung: niedrig | mittel | hoch | kritisch, Evidenz, Auswirkung]

## 6. Änderungsempfehlungen

[Priorisierte Empfehlungen, die nur benennen, was geklärt, spezifiziert, belegt oder freigegeben werden muss. Keine Ersatztexte und keine eigenständigen Lösungen.]

## 7. Freigabevoraussetzungen

[Offene Entscheidungen, Nachweise, Freigaben und Verantwortliche, die vor der Entwicklerübergabe geklärt werden müssen. Keine eigenständigen Lösungen.]

## 8. Tool- und Workflow-Audit

- Projekttyp: Website | Web-App | SaaS-Plattform | Mobile App | Desktop-App | KI-System | Datenprojekt | API/Backend | E-Commerce | Designprojekt | Medienprojekt | Enterprise-System | anderes | NICHT PRÜFBAR
- Bewertung: PASS | PASS MIT RISIKEN | NICHT BEREIT
- Vorhandene Tools: [dokumentierte Werkzeuge, Umgebungen und Prozesse mit Evidenz]
- Fehlende Bereiche: [anwendbare, aber nicht ausreichend definierte Fähigkeiten oder Workflows]
- Risiken: [Finding-IDs, Bewertung und Auswirkung]
- Empfohlene Ergänzungen: [nur welche Festlegung, Fähigkeit, Einschränkung, Evidenz, Zuständigkeit oder Freigabe ergänzt werden muss; keine Toolauswahl]

## 9. Freigabe

Bereit für Claude Code
```

For a failing audit, the final line under section 9 must instead be exactly:

`Noch nicht bereit`

Use `Keine festgestellt` when a section has no findings. Do not omit a section. Keep findings specific, evidence-linked, deduplicated, and actionable without repairing the source material.

## Multi-document audit extension

For a specification suite, audit every declared active/candidate artifact and their relationships; historical inspection follows the Historical Corpus Audit Policy above. Keep usage classes `FULL`, `PARTIAL`, `REFERENCE`, `HISTORICAL`, `DO NOT IMPLEMENT` separate from lifecycle statuses such as `OVERRIDDEN`. For `PARTIAL`, require exact usable sections. Verify artifact identity, version, lifecycle status, owner, sources, `extends`, `overrides`, `supersedes`, downstream dependencies, and approval evidence where claimed. Record classification findings only; do not mutate file metadata.

Require a scope-specific precedence matrix wherever two files can control the same decision. Its absence is an `ENTSCHEIDUNGSLÜCKE`. Require one coding-agent first-read control document stating authoritative manifest, read order, usage, permissions, open decisions, current gate, QA, acceptance, and definition of done.

Simulate implementation area by area using only readable referenced artifacts. Ask explicitly: **Could the developer make an unauthorized Class-1 decision or use Class-2 judgment without an approved role, target, bounds, evidence, checkpoint, and reviewer?** If yes, identify the exact possible choice, risk, and missing specification. Qualitative visual, motion, interaction, or 3D language may be a controlled target or perceptual acceptance criterion; it is a gap only when the package lacks sufficient relationships, bounds, representation proof, review, or acceptance evidence.

Verify that every referenced file, asset, and required version exists and is readable. Report repairs as recommendations only; never perform gap closure inside this skill.
