---
type: template-library
domain: Knowledge Governance / Game Design
status: active
version: 1.1
owner: Game Design
governance: Knowledge Steward
last_reviewed: 2026-08-25
scope: reusable reference; receiving-project policy takes precedence
---

# GDD Templates

## Purpose

Provide reusable structures conforming to [GDD Authoring Standard](gdd-authoring-standard.md). Start with the base template, then add only the extension sections relevant to the document type. Do not retain empty headings merely to appear complete.

## Base GDD template

```markdown
---
type: gdd | system-design | balance-methodology | balance-model | balance-roadmap | balance-validation-plan | game-design-catalog | balance-baseline | ux-behavior
project: <project-name>
domain: <canonical domain>
feature: <feature/system name>
status: active | temporary | review | deprecated
canonical: true | false
owner: <role or person>
reviewers:
  - <role or person>
validation: owner-approved | runtime-observed | runtime-validated | mixed | unverified
last_reviewed: YYYY-MM-DD
---

# <Feature/System Name>

## Summary

<One paragraph describing what the feature is, who interacts with it and its current design boundary.>

## At a glance

| Field | Value |
|---|---|
| Player value | ... |
| Primary actor | ... |
| Entry condition | ... |
| Main outcome | ... |
| Canonical owner | This note / another note |
| Structured data | [exact source] |
| Final UI/visual | [exact Figma/art source] |

## Design goals

- ...

## Scope

### Included

- ...

### Excluded

- ...

## Visual overview

<Use one compact diagram, table or referenced image only when it materially improves comprehension.>

<Add a short textual interpretation of the visual.>

## Core rules

1. ...

## States and flow

<Numbered flow, state table or Mermaid diagram.>

## Inputs, conditions and outcomes

| Input/condition | Behavior | Output/consequence | Failure/exception |
|---|---|---|---|
| ... | ... | ... | ... |

## Interactions and dependencies

| System/source | Interaction | Ownership |
|---|---|---|
| [[Related System]] | ... | ... |

## Edge cases

| Case | Expected behavior | Status/evidence |
|---|---|---|
| ... | ... | ... |

## Balance and configuration

- Intent and parameter meanings: ...
- Structured source: [exact Sheet/CSV/config link]
- Constraints/caps: ...

## UI/UX and visual references

| Artifact | Status | Purpose | Exact source |
|---|---|---|---|
| ... | Reference/Concept/Current/Target | ... | ... |

## Technical alignment

- Implemented source: ...
- Runtime observation: ...
- Known design/runtime drift: ...

## Analytics and validation

- Success signal: ...
- Event/data definition: ...
- Acceptance criteria: ...
- Test/playtest evidence: ...

## Open questions

| ID | Question | Owner | Impact | Status/revisit trigger |
|---|---|---|---|---|
| OQ-01 | ... | ... | ... | Open |

## Change authority

- Feature owner: ...
- Canonical owner: ...
- Required reviewers: ...

## Related notes

- [[...]]
```

## System GDD extension

Use for shared systems such as Item, Hero Stats, Ability or Economy.

```markdown
## Domain model

| Entity/concept | Responsibility | Key state | Canonical owner |
|---|---|---|---|
| ... | ... | ... | ... |

## Aggregation or processing order

1. ...

## Invariants

- <Rule that must remain true across all consumers.>

## Extension boundaries

- <What may vary by content/config.>
- <What requires a design or architecture decision to change.>
```

## Player-facing feature extension

Use for a bounded interaction or gameplay feature.

```markdown
## Player journey

| Step | Player action | System feedback | Exit/failure condition |
|---:|---|---|---|
| 1 | ... | ... | ... |

## Entry and exit conditions

- Entry: ...
- Success exit: ...
- Failure/cancel exit: ...
- Re-entry behavior: ...
```

## Progression or economy extension

```markdown
## Economy loop

<Compact flow showing sources, sinks and progression outcome.>

## Resource rules

| Resource | Source | Sink | Constraint | Live data owner |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## Formula model

`Output = ...`

| Variable | Meaning | Unit/source |
|---|---|---|
| ... | ... | ... |

**Example:** ...

## Abuse and failure cases

- Duplication/refund behavior: ...
- Partial payment/failure behavior: ...
- Cap/overflow behavior: ...
```

## Balance methodology extension

```markdown
## Model purpose

<Question the model answers and decisions it must not make automatically.>

## Inputs and evidence quality

| Input | Source | Confidence | Validation need |
|---|---|---|---|
| ... | ... | ... | ... |

## Assumptions

| ID | Assumption | Impact | Revisit trigger |
|---|---|---|---|
| A-01 | ... | ... | ... |

## Outputs

| Output | Interpretation | Allowed use |
|---|---|---|
| ... | ... | ... |
```

## UI behavior extension

```markdown
## Screen/state inventory

| State | Entry condition | Available actions | Exact Figma frame |
|---|---|---|---|
| ... | ... | ... | ... |

## Interaction rules

| Trigger | UI response | Game-state effect | Error/disabled behavior |
|---|---|---|---|
| ... | ... | ... | ... |

## Presentation ownership

- KB owns behavior and state transitions.
- The designated visual-design source owns final composition, spacing, typography, color and prototype (for example, exact Figma frames).
```

## Content-definition extension

Use for Hero, Weapon, Enemy, Ability, POI or other authored content families.

```markdown
## Content taxonomy

| Class/type | Identity | Shared rules | Allowed variation |
|---|---|---|---|
| ... | ... | ... | ... |

## Definition-to-runtime mapping

| Config field/group | Design meaning | Runtime consumer |
|---|---|---|
| ... | ... | ... |
```

## Pre-write confirmation pack template

Use this after source discovery when material decisions or publication authority remain unresolved. Existing explicit approval of a complete brief or scoped request is sufficient; do not create another confirmation round just to fill this template. When a pack is needed, its confirmation authorizes publication within its stated scope.

```markdown
# <Feature/System> Pre-write Confirmation

## Scope and intended artifacts

| Artifact | Canonical owner | Intended status | Canonical flag | Change |
|---|---|---|---|---|
| ... | ... | active/temporary/review | true/false | Create/Update |

## Confirmed source facts

| Claim/input | State | Source | Treatment |
|---|---|---|---|
| ... | Canonical/Observed | ... | Carry forward |

## Decisions required

| ID | Question | Recommended resolution | Trade-off/impact | Owner response |
|---|---|---|---|---|
| D-01 | ... | ... | ... | Pending |

## Temporary assumptions

| Assumption | Scope | Confidence | Revisit trigger | Authorized replacement boundary |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## Non-blocking unknowns

| Unknown | Owner | Impact | Validation requirement |
|---|---|---|---|
| ... | ... | ... | ... |

## Approval meaning

Explicit owner confirmation approves the decisions, assumptions, artifact list and metadata above. Reconfirmation is required only for a material departure.
```

## Migration brief template

```markdown
# <Feature> Migration Brief

- **Owner:**
- **Reviewers:**
- **Goal:**
- **Included:**
- **Excluded:**
- **Target canonical note:**
- **Sources:**
  - Figma:
  - Legacy GDD:
  - Sheets/CSV:
  - Repo:
- **Known conflicts:**
- **Open questions:**
- **Status:** Not Started | Analysis | Decision Ready | Blocked | Migrated
```

## Related notes

- [GDD Authoring Standard](gdd-authoring-standard.md)
- [GDD Review Checklist](gdd-review-checklist.md)
- [GDD Migration workflow](../skills/gdd-migration/SKILL.md)
- [Source of Truth](source-of-truth.md)
