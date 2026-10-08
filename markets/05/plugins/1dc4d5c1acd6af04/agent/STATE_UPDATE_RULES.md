# STATE_UPDATE_RULES.md

**Status:** Canonical state-update protocol  
**Version:** 1.0

## Ownership

Only the orchestrator persists canonical negotiation state. Specialists propose patches against a specific `state_version`.

## Update sequence

For each material event:

1. identify the source event (`NEW_FACT`, `COUNTERPART_MESSAGE`, `OFFER_RECEIVED`, `CONCESSION_*`, `USER_CORRECTION`, etc.);
2. extract propositions without changing their certainty;
3. assign evidence status where material;
4. detect contradictions with current state;
5. reconcile any specialist patch against the current `state_version`;
6. apply permitted `ADD`, `UPDATE_WITH_EVIDENCE`, `SUPERSEDE` or `FLAG_CONTRADICTION` operations;
7. increment `state_version` for material change;
8. append a material history event;
9. recompute affected derived strategy judgements;
10. detect whether the change must be surfaced to the user.

## Evidence promotion

`UNKNOWN → HYPOTHESIS` when a plausible possibility is identified.  
`HYPOTHESIS → SUPPORTED_INFERENCE` only with identifiable support.  
`SUPPORTED_INFERENCE → KNOWN` only with direct/reliable confirmation.

Conflicting KNOWN propositions create a contradiction; do not silently choose the convenient one.

A user correction supersedes the earlier user-supplied proposition and triggers review of dependent strategy.

## Stale patches

If a specialist responds from v8 and the canonical state is v9:
- do not apply automatically;
- identify fields changed between versions;
- apply only non-conflicting conclusions that remain valid, or rerun the specialist;
- never let a stale target/BATNA/offer overwrite newer state.

## Protected history

### Concessions
The concession ledger is append-only. A regretted or withdrawn concession remains in history with later status/event.

### Proposals
Maintain proposal history even when `current_*_offer` changes.

### Targets/floors
Material target or least-acceptable-boundary changes require basis. In STANDARD/FULL, surface the change if it alters strategy.

### Pre-commitment
Never overwrite an acceptance criterion. Record previous value, new value, new evidence, reason, user approval and timestamp.

### Deal review
A later user override does not change an earlier `FAIL` to `PASS`.

## Role-play / red-team isolation

F06 role-play content does not enter the evidence register as fact. Reconcile significant findings as:
- `ACCEPT` — supported/material strategy finding;
- `TEST` — plausible hypothesis/research question;
- `REJECT` — inconsistent with evidence;
- `DEFER` — immaterial now.

Only independent evidence can promote a simulated counterpart statement to KNOWN.

## Material-change notification

In STANDARD/FULL notify the user where the update materially changes:
- current strategy;
- user BATNA;
- material target/floor;
- decision authority;
- deal-review result/recommendation.

State the new evidence, prior working view and changed recommendation succinctly.

## Persistence threshold

LIGHT: conversational state by default.  
STANDARD: explicit state artefact when material or expected to continue across exchanges.  
FULL: explicit state artefact unless platform limitations prevent it; if so, preserve a concise canonical snapshot in the available state mechanism.

## Close/pause

`PAUSED`, `CLOSED` and `NO_DEAL` require a material event/user decision. Closing does not delete history, deal review or overrides.
