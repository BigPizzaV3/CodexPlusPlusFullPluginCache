---
name: communication-drafting
description: Use when an approved negotiation strategy needs to be turned into an email, message, meeting opening, agenda, call note, offer wording, response, or other communication without changing the commercial position.
---

# Communication Drafting

## Overview

Turn an **approved strategy** into usable wording. Drafting is a `[DESIGN]` implementation layer, not a separate Freeman method.

**Interface:** accept `schemas/SKILL_REQUEST.md`; return `schemas/SKILL_RESPONSE.md` with an optional `deliverable`. Never persist state.

## Method

1. **Read the approved move.** Identify objective, audience, current offer, conditions, evidence status, relationship tone and any recorded user override.
2. **Run a strategy-diff check.** Compare requested wording with canonical targets, BATNA, concessions, conditions and deal-review status.
3. **Flag strategic drift.** If wording would reduce price, accept scope/risk, alter programme/liability, remove a condition, grant a right or otherwise create an unapproved concession, warn the orchestrator. Do not silently insert the change.
4. **Preserve conditionality.** An approved “X if Y” trade remains conditional in the draft.
5. **Preserve evidence certainty.** Do not turn inference/hypothesis into asserted fact or invent leverage, offers, deadlines, authority, benchmarks or resource constraints.
6. **Match tone to strategy.** Use relationship-aware firmness without aggression theatre or artificial niceness.
7. **Draft.** Return the usable communication in `deliverable` plus any material warnings/findings.

## Override handling

If canonical state records an informed user override, draft that chosen strategy accurately without re-litigating the settled issue. An unrecorded conflict returns a warning and may offer a strategy-consistent draft alternative; it does not change strategy itself.

## Boundaries

F07 may not change targets, BATNA, concessions, evidence status or deal-acceptance recommendation. Strategy changes return to the orchestrator/F02/F03; acceptance belongs to F08.

## Output

Return canonical `skill_response` with `deliverable.kind` appropriate to the requested communication and `deliverable.content` containing the finished draft.

## Stop condition

Stop when the wording faithfully executes the approved move and introduces no unapproved strategic change.
