# Audit and implementation method

## Establish coverage

Record:

- target user and task;
- routes and journey steps;
- role and permissions;
- data and lifecycle states;
- browser, viewport, zoom, text scale, and usable content width;
- official browser, device, and accessibility targets, or the fact that they are unresolved;
- privacy constraints for fixtures, captures, storage, logs, analytics, and telemetry;
- implementation owner and, when formal sign-off is required, the human acceptance owner;
- governing authority and branch;
- evidence that is inaccessible.

Inspect the primary broker task before peripheral polish. Admin, PDF, email, authentication, and off-app states still require coverage when they are in scope.

## Audit the real product

Inspect the rendered UI for:

- task and next-action clarity;
- hierarchy of labels, values, summaries, totals, statuses, warnings, and actions;
- terminology and copy consistency;
- typography, spacing, alignment, geometry, density, icons, color roles, borders, elevation, and surface use;
- default, hover, focus, pressed, selected, disabled, loading, empty, validation, error, success, stale, manual, and destructive states;
- responsive continuity, clipping, overflow, wrapping, sticky regions, drawers, dialogs, tables, and action reachability;
- keyboard operation, focus order and visibility, accessible names, target size, contrast, error identification, status announcements, reduced motion, and non-color cues;
- financial comparison, tabular alignment, units, data freshness, selection, and authoritative-state clarity.

Use screenshots for appearance, DOM and accessibility evidence for semantics, and code for implementation. Do not use one evidence type to claim what only another can prove.

## Findings

Use stable IDs such as TMC-UI-001.

For every P0 or P1 include:

- title and severity;
- system-wide or page-specific scope;
- exact route, step, role, viewport, usable container, data, and state;
- affected component;
- basis: observed, directly inferred, or unverified;
- evidence;
- user impact;
- supported likely cause or unknown;
- bounded repair that preserves product rules;
- reproducible verification with the expected outcome.

Use P0 only for blocked required tasks, hidden or materially misleading consequential information, credible wrong-action risk, or a serious accessibility barrier. Use P1 for material difficulty or ambiguity. Group related P2 polish under its shared root cause.

## Plan by root cause

Separate shared-system faults from local composition faults.

Prefer this order when the evidence supports it:

1. shared tokens and primitives;
2. application shell and workspace measures;
3. responsive context behavior;
4. page hierarchy and action locality;
5. interaction and asynchronous states;
6. accessibility repairs;
7. motion and decorative refinement.

Do not force this order when a P0 requires a local repair first.

Every implementation lane needs:

- exact owned files or component boundary;
- out-of-scope files and behavior;
- accepted visual and interaction outcome;
- realistic test data;
- required widths and states;
- applicable asynchronous failure, session, runtime, privacy, browser, and accessibility checks;
- focused tests and wider regression gates;
- rollback or clean removal route;
- a named implementation owner and, when formal sign-off is required, a named acceptance owner;
- representative broker acceptance when a major journey change requires it;
- completion evidence.

Include code-hygiene acceptance criteria for the lane: the canonical implementation to retain, superseded code expected to be removed, relevant static and runtime checks, and any suspected debt that is explicitly outside the lane.

## Implement safely

Before coding, inspect existing components, CSS architecture, tokens, tests, and related lanes. Reuse good existing patterns. Remove drift at its source when safe, but do not broaden a small page repair into a frontend rewrite.

During implementation:

- keep business and API behavior intact;
- preserve current data flow and server truth;
- avoid magic viewport assumptions when the available container drives layout;
- keep entered data, selected state, expansion, focus, and scroll context across approved layout transitions;
- use semantic HTML and existing accessible components;
- respect reduced motion;
- avoid unrelated dependency upgrades or formatting churn;
- add or update tests for behavior the change could break.

Use synthetic or approved test data. Do not copy production client data into fixtures, screenshots, bug reports, prompts, logs, or external services. Do not exercise destructive, email-sending, Provider-facing, or Case-creating production actions merely to verify the UI.

Do not leave the old implementation beside its replacement for convenience. Follow the scoped gate in [code-hygiene.md](code-hygiene.md), and remove code only when references, runtime behavior, and relevant tests make the removal safe.

Motion must have a job: explain change, reinforce causality, preserve spatial continuity, or acknowledge completion. Remove motion that delays work, competes with financial information, harms readability, or exists only to make the page look expensive.

## Reinspect after coding

Do not verify only the changed component in isolation. Repeat the affected task from its entry point and inspect adjacent states that share the same component or token.

Compare before and after at the same route, data, state, and width. Confirm the repair and look for new wrapping, overflow, focus, contrast, loading, or state-preservation problems.

Run focused automated tests first. Then run the repository's relevant type, lint, unit, integration, build, and end-to-end gates. Record commands and results. A green test suite does not replace rendered inspection.

Apply the relevant parts of [verification-matrix.md](verification-matrix.md). For asynchronous or authenticated work, test the failure and recovery sequence, not only the final success state. Inspect new console errors, unhandled promises, hydration warnings, and unexpected network failures. Distinguish defects introduced by the lane from confirmed pre-existing noise.

## Representative broker acceptance

Use representative-user acceptance for a major change to journey structure, terminology, decision order, navigation, or a consequential action. A domain owner can confirm product intent, but one familiar stakeholder does not by itself prove that ordinary brokers understand the journey.

Define the tasks and success criteria before the session. Use product-valid, non-production data. Record completion, wrong turns, misunderstandings, assistance required, and severe confidence or trust issues. Keep observations separate from stakeholder preferences and implementation decisions.

Do not require broker testing for a local spacing fix, mechanical refactor, or repair whose behavior and design outcome are already accepted. Do not contact or schedule a broker without authorisation. If required acceptance cannot be completed, report the implementation as technically verified but not representative-user validated; block release only when the governing authority makes that validation a release condition.

## Status inventory

When the user asks what remains, return a matrix with:

- area or route;
- authority;
- live branch or PR;
- complete, partial, missing, stale, conflicting, or unverified;
- strongest evidence;
- blocking dependency;
- next bounded lane.

Do not count a handoff or open PR as completed implementation. Do not count merged code as visually accepted without rendered verification.
