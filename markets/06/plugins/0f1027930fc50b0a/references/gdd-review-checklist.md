---
type: checklist
domain: Knowledge Governance / Game Design
status: active
version: 1.1
owner: Game Design
governance: Knowledge Steward
last_reviewed: 2026-08-25
scope: reusable reference; receiving-project policy takes precedence
---

# GDD Review Checklist

## Purpose

Provide a repeatable quality and approval gate for new, substantially revised or migrated GDDs. This checklist validates clarity for both people and AI agents without requiring every document to use every possible section or visual.

## Review outcome

Classify findings as:

| Severity | Meaning | Activation impact |
|---|---|---|
| Blocker | Could create a wrong implementation, competing source of truth or false accepted decision | Must resolve before `active`/`Migrated` |
| Required correction | Material clarity, traceability or completeness problem | Resolve or explicitly defer with owner and impact |
| Improvement | Useful but non-essential enhancement | May remain as follow-up |

An active GDD requires zero blockers and explicit feature-owner approval. An approved brief, scoped user request or consolidated confirmation pack can supply approval; no new approval round is required when the published result remains within that scope. Non-blocking open questions are allowed when visible, owned and scoped.

## Pre-write decision gate

- [ ] Source discovery and analysis were completed before the first canonical KB write.
- [ ] Existing approval covers the intended content and artifacts; any unresolved material questions, proposed resolutions or assumptions were consolidated for the owner.
- [ ] Existing explicit approval covers that exact scope, or unresolved material points are intentionally recorded as a review/blocked checkpoint.
- [ ] No material rule was added after confirmation without returning that difference to the owner.
- [ ] The selected document lifecycle status is independent from claim-level evidence confidence.

## 1. Ownership and metadata

- [ ] Feature/system boundary is clear in one sentence.
- [ ] Canonical owner is explicit and agrees with [Source of Truth](source-of-truth.md).
- [ ] `status`, `canonical`, `owner`, `validation` and `last_reviewed` are present or intentionally inherited from a legacy-compatible format.
- [ ] Related notes link to the canonical owner instead of duplicating its rules.
- [ ] Change authority and required reviewers are named.

## 2. Knowledge-state integrity

- [ ] Accepted design, proposal, temporary decision, runtime observation and open question are distinguishable.
- [ ] No runtime behavior is presented as intended design without owner confirmation.
- [ ] No assistant inference, example or recommendation has silently become canonical.
- [ ] Superseded behavior is removed from current-state rules and retained only where history is useful.
- [ ] Significant decisions are recorded in the receiving project's decision records.

## 3. Dual readability

- [ ] A person can identify purpose, scope, owner and main behavior without opening every external link.
- [ ] An AI agent can identify entities, conditions, states, outputs and exceptions from explicit text or structured tables.
- [ ] Important terminology is defined and used consistently.
- [ ] Config IDs, fields, classes and events are represented as literal text.
- [ ] Essential meaning does not depend on color, spatial position, emoji or an unavailable image.
- [ ] Examples illustrate existing rules rather than introduce new ones.

## 4. Visual representation

- [ ] A visualization decision was made, even if the result is “text is sufficient.”
- [ ] Exact mappings/comparisons use a table when clearer than prose.
- [ ] Ordered branching behavior or state transitions use a compact diagram when materially helpful.
- [ ] Numeric trends use a chart linked to live source data when materially helpful.
- [ ] UI layout and final visual composition remain in their designated visual-design source; use exact frames when that source is Figma.
- [ ] Every image/chart has alt text, caption, status and source/owner.
- [ ] Every essential diagram or image has a short textual interpretation.
- [ ] Visuals do not duplicate a frequently changing numeric table or create a competing source of truth.

## 5. Rule completeness

- [ ] Core rules identify actor, trigger/condition, behavior and outcome.
- [ ] Processing order is explicit where order affects results.
- [ ] States and transitions cover entry, success, failure, cancel and re-entry when applicable.
- [ ] Inputs/outputs and dependencies are explicit.
- [ ] Edge cases cover caps, empty states, duplicates, insufficient resources, invalid state and partial failure where relevant.
- [ ] Irreversible operations and refund/rollback behavior are defined.

## 6. Formula, balance and data

- [ ] Non-trivial formulas define variables, units, clamping, rounding and order where relevant.
- [ ] At least one worked example validates each non-trivial formula.
- [ ] Design intent is present without copying the full live config table.
- [ ] Exact Sheet/CSV/config links identify the live numeric owner.
- [ ] Static chart snapshots identify source and date.
- [ ] Assumptions and confidence are explicit for provisional balance models.

## 7. UI/UX and content references

- [ ] Visual-design links identify the relevant artifact; Figma links point to exact pages/frames rather than only the file root.
- [ ] KB owns behavioral rules; the designated visual-design source owns final composition.
- [ ] Reference, concept, target, current and deprecated assets are labeled correctly.
- [ ] Content definitions distinguish shared family rules from per-record values.

## 8. Technical alignment

- [ ] Relevant repository path, class/method, schema or build evidence is linked when available.
- [ ] Known design/runtime drift is explicit.
- [ ] Unverified implementation details are not described as validated.
- [ ] Runtime validation debt has an owner or revisit trigger.
- [ ] Technical detail does not replace the player-facing design rule.

## 9. Open questions and validation

- [ ] Every material open question has an ID, owner, impact and status/revisit trigger.
- [ ] Blocking questions prevent activation or are explicitly excluded from scope.
- [ ] Acceptance criteria are observable and testable.
- [ ] Playtest/runtime evidence is linked or marked unavailable/deferred.
- [ ] Validation status in metadata matches the evidence described in the document.

## 10. Publication gate

- [ ] Existing explicit approval (brief, scoped request, confirmation pack or final result) covers publication.
- [ ] Published content remains within the approved scope; any material departure was reconfirmed.
- [ ] Required reviewers completed their review or a named owner accepted the deferral.
- [ ] The result was published directly with its approved final status; `review` was used only for a genuine unresolved checkpoint.
- [ ] [Source of Truth](source-of-truth.md) was updated if ownership changed.
- [ ] the receiving project's decision records was updated for durable decisions.
- [ ] Domain index and related-note links were updated.
- [ ] Legacy sources were deprecated only after approval and were not destructively deleted.
- [ ] Every changed artifact was read back and verified; readback did not create an additional approval round.

## Review record template

```markdown
## Review record — YYYY-MM-DD

- **Document:**
- **Author/migrator:**
- **Feature owner:**
- **Reviewers:**
- **Validation state:**
- **Blockers:** None | ...
- **Required corrections:** None | ...
- **Deferred improvements:** None | ...
- **Open questions accepted for active status:** None | ...
- **Owner approval:** Pending | Approved — <pre-write confirmation or final-result evidence/date>
- **Outcome:** Draft | Review | Blocked | Active | Migrated
```

## Related notes

- [GDD Authoring Standard](gdd-authoring-standard.md)
- [GDD Templates](gdd-templates.md)
- [GDD Migration workflow](../skills/gdd-migration/SKILL.md)
- [Knowledge Steward](../skills/knowledge-steward/SKILL.md)
- [Source of Truth](source-of-truth.md)
