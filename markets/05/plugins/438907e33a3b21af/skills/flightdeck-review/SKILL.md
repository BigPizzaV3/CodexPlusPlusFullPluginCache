---
name: flightdeck-review
description: Audit a codebase, plugin, service, or release candidate for evidence-backed release and submission readiness. Use for code reviews, pre-release checks, marketplace or app submissions, packaging audits, security and privacy reviews, reviewer test preparation, or when the user asks whether a project is genuinely ready to ship. Make bounded fixes only when the user asks to make the project ready.
---

# FlightDeck Review

Return a defensible ship decision. Treat repository state, executed checks, live endpoints, and published artifacts as separate evidence sources.

## Establish the review contract

1. Read repository guidance, handoffs, release instructions, and committed verification configuration before judging the code.
2. Inspect git status and preserve unrelated or pre-existing work.
3. Identify the exact submission or release target, the artifact users receive, and the current public requirements from primary sources when they may have changed.
4. State material scope assumptions. Do not invent account access, identity verification, domain control, approval, publication, pricing, or legal attestations.

## Audit the deliverable

Cover the relevant surfaces:

- architecture and entrypoints;
- user-visible claims, buttons, links, and error paths;
- inputs, schemas, permissions, and side-effect annotations;
- authentication, authorization, secret handling, path boundaries, subprocesses, and network behavior;
- data collection, retention, subprocessors, privacy policy, terms, support, and live URL status;
- dependency and supply-chain exposure;
- package metadata, version lockstep, build reproducibility, installability, and artifact/source parity;
- tests, lint, type checks, security checks, and repository-defined verification;
- reviewer-facing copy, logo, prompts, positive tests, negative tests, availability, and release notes.

Run the cheapest decisive checks first. Use an isolated or clean workspace for build/install tests when practical. Never convert an absent test, skipped check, stale result, or dirty tree into a pass.

## Record findings

Report a finding only when it has concrete evidence:

- severity and user/reviewer impact;
- exact file and line, live URL, command output, or failing input;
- why the current behavior violates the stated contract or submission rule;
- the smallest defensible remediation.

Distinguish:

- code-fixable;
- publisher or account gated;
- architecture gated;
- external-review gated.

Do not bury a release blocker among style notes. Treat warnings as warnings unless they are tied to an actual rejection or failure mode.

## Make bounded fixes when authorized

If the user asks to make the project ready:

1. Fix only verified defects in scope.
2. Preserve existing behavior and branding unless the requirement demands a change.
3. Add or update regression tests for every behavior change.
4. Re-run the narrow checks, then the full repository-defined verification.
5. Rebuild and reinstall the user-facing artifact. Recheck live URLs after deployment.
6. Never publish, submit, accept attestations, or change account identity unless the user explicitly authorized that external action.

## Return the decision

Lead with one verdict:

- **READY** — required checks passed and no required gate remains.
- **READY WITH DISCLOSED GAPS** — the artifact is sound, but named external or optional checks remain.
- **NOT READY** — a required technical, policy, legal, identity, or architecture gate is unresolved.

Then give:

1. release blockers;
2. verified passes with exact commands or evidence;
3. changes made and their tests;
4. remaining gates by owner;
5. a submission checklist and five positive plus three negative reviewer cases when marketplace review is in scope.

Never call a draft submitted, a submission approved, or a release live until that state is directly observed.
