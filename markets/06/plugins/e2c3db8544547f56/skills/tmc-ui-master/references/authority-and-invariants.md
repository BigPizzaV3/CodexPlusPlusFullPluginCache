# Authority and protected behavior

## Source order

Use this order when sources disagree:

1. The user's explicit current decision for the task.
2. Current documents marked active, accepted, locked, or implementation authority in 18 Max/UI.
3. The accepted page or lane handoff for the exact work.
4. Current backend contracts and business authority for behavior the UI presents.
5. Live frontend code as implementation fact.
6. Current rendered behavior as evidence of what users receive.
7. Historical documents, old handoffs, screenshots, comments, and generic design guidance.

Live code can prove what exists. It cannot overrule an accepted product decision. A design document cannot prove an API behavior. When two applicable authorities conflict, report the exact conflict and stop that decision rather than choosing whichever is easier to implement.

## Current authority discovery

Start in the TMC Drive, especially 18 Max/UI. Verify document status and modification context rather than assuming every matching title remains current.

Search connected sources first. Do not make Max repeatedly provide a Drive link, repository, branch, or preview URL that the available tools can resolve. If discovery fails, name the exact missing access or artifact instead of asking for a broad information pack.

Likely core documents include:

- 00 - TMC UI Direction and Visual System
- 01 - Responsive Workspace and Quote Context Spec
- 02 - TMC UI Branch Implementation Map and Acceptance Checklist
- 03 - TMC Pre-Launch Visual Quality, Motion and Experience Master Plan
- 04 - Parallel UI Build, Breakpoint and Visual QA Execution Plan
- 08 - Wave 2 Broker Journey Ease Audit and Product Decisions
- the current page-specific Wave 2 handoff or later accepted replacement

Treat titles as discovery leads. A later document may supersede them. Read the relevant sections, not only search snippets.

For work that may make a support, accessibility, privacy, or release-readiness claim, also resolve when available:

- officially supported browsers, device classes, minimum widths, zoom, and text-scaling expectations;
- the accessibility standard, version, conformance level, and test method TMC has accepted;
- client-data rules for URLs, browser storage, screenshots, logs, analytics, telemetry, and test fixtures;
- the human owner who accepts the lane and whether representative broker acceptance is required.

Separate an official target from a temporary test sample. If no authority defines a target, propose one for approval and label it provisional. Do not invent a support promise, accessibility conformance claim, privacy policy, or release sign-off.

## Repository and branch guard

The normal frontend repository is the-moving-chain/tmc-frontend.

Before edits:

- fetch current remote state;
- inspect the task's required base branch and commit;
- confirm the checked-out worktree and target branch;
- inspect uncommitted changes and preserve work that belongs to the user or another lane;
- read the active handoff and the components it owns;
- identify parallel UI lanes and likely merge conflicts.

If the start commit is locked and the live state differs, report the mismatch before changing code. Never solve a branch mismatch with destructive reset or by silently starting from another branch.

Backend repositories and APIs are read-only context during ordinary UI work. Modify them only under separate explicit authority.

## Product principles

Reconfirm these against current authority:

- Ease comes before decoration.
- Trust and state clarity come before motion.
- Static hierarchy, spacing, geometry, responsive composition, and accessibility come before delight.
- TMC should feel like a coherent finance product, not a collection of generated cards.
- One local decision should have one obvious primary action.
- Actions should sit near the object they affect.
- Financial values, status, selected Provider, saved state, and submission outcome must remain unambiguous.
- Navigation and Quote context are separate concepts.
- Quote context adapts through the currently approved full, compact, ribbon, drawer, and mobile patterns according to usable workspace.
- Motion may explain change and continuity. It must not delay real state, fabricate values, hide errors, or override reduced-motion preferences.

These principles guide presentation. Exact current page decisions still come from the live authority.

## Protected invariants

Treat the following as outside ordinary UI authority:

- authoritative money and its calculation;
- immediate referral-fee repricing behavior;
- Provider eligibility and broker-visible availability rules;
- saved Quote and pricing-version behavior;
- Instruction idempotency and atomic Case creation;
- frozen submitted money;
- tenant isolation, role permissions, invitation and authentication rules;
- session expiry and reauthentication semantics;
- client-data retention, browser storage, analytics, telemetry, and privacy rules;
- audit history and admin publication rules;
- production data and deployment controls.

Test that UI work did not change them. Do not claim they are correct merely because the page renders.

## Scope and mutation rules

A request to review, audit, assess, plan, or report is read-only.

A request to fix, implement, build, apply, or complete the UI authorises scoped code changes and safe verification. It does not authorise a merge into a shared or protected branch, a production deployment, production-data mutation, or unrelated backend work.

It also does not authorise contacting brokers, scheduling user tests, enrolling analytics, sending client data to a new service, or installing an unplanned dependency. Prepare those steps when relevant, but obtain the required approval before the external action or new commitment.

When product intent is genuinely unclear and different answers would materially change the journey, ask one focused question or leave the decision blocked. Do not invent behavior to keep coding.
