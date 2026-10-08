---
type: standard
domain: Knowledge Governance / Game Design
status: active
version: 1.1
owner: Game Design
governance: Knowledge Steward
last_reviewed: 2026-08-25
scope: reusable reference; receiving-project policy takes precedence
---

# GDD Authoring Standard

## Purpose

Define how game design documents are written so both people and AI agents can understand, navigate, verify and maintain them reliably. Neither audience is primary. A conforming GDD must be readable without tool-specific assumptions and structured enough that an agent can distinguish accepted design, runtime evidence, examples and unresolved work.

This standard governs authoring quality. [GDD Migration workflow](../skills/gdd-migration/SKILL.md) governs migration workflow, [GDD Templates](gdd-templates.md) provides reusable structures, and [GDD Review Checklist](gdd-review-checklist.md) defines the activation gate.

## Core principles

1. **Dual-readable:** optimize comprehension for people and deterministic interpretation for agents.
2. **One canonical owner:** each durable rule has one authoritative note; related notes link instead of copying it.
3. **Current design first:** canonical sections describe the accepted current state. History belongs in the receiving project's decision records or archive.
4. **Intent is not implementation:** design rules and runtime observations are labeled separately. Drift is reported, not silently resolved.
5. **Data stays live:** large numeric tables remain in the designated Sheet/CSV; the GDD explains meaning, relationships and design intent.
6. **Visuals carry meaning:** use a table, diagram, chart or image when it materially reduces ambiguity or reading time.
7. **No visual-only rules:** every essential visual has a textual summary, caption or rule table so meaning survives search, accessibility limits and unavailable images.
8. **Unknown remains unknown:** unresolved claims stay visible as open questions with an owner and impact.

## Required metadata

New GDDs and substantial rewrites use YAML frontmatter:

```yaml
---
type: gdd | system-design | balance-methodology | balance-model | balance-roadmap | balance-validation-plan | game-design-catalog | balance-baseline | ux-behavior
project: <project-name>
domain: <canonical domain>
feature: <feature/system name>
status: draft | review | active | temporary | deprecated
canonical: true | false
owner: <role or person>
reviewers:
  - <role or person>
validation: unverified | owner-approved | runtime-observed | runtime-validated | mixed
last_reviewed: YYYY-MM-DD
---
```

Rules:

- `status: active` requires explicit feature-owner approval and a passed [GDD Review Checklist](gdd-review-checklist.md). Explicit confirmation of a pre-write confirmation pack satisfies approval when the published result remains within that pack.
- `status: temporary` is allowed for an owner-approved working artifact only when its revisit trigger and non-promotion boundary are explicit.
- Use `status: review` only when a material decision remains unresolved, the result departs materially from the approved scope, or the owner explicitly requests a checkpoint.
- `canonical: true` identifies ownership, not implementation correctness.
- Lifecycle status and evidence quality are independent. An active canonical note may contain labeled provisional, unknown or runtime-unvalidated claims.
- `validation` describes evidence state. Use `mixed` when different claims have different validation levels and explain them in the document.
- Existing notes may retain compatible metadata until their next substantial review; do not churn metadata only for cosmetic conformity.

## Knowledge-state language

Use explicit labels when a claim is not a normal accepted design rule:

| Label | Meaning | Canonical treatment |
|---|---|---|
| **Design rule** | Owner-approved intended behavior | May appear as current specification |
| **Runtime observation** | Behavior evidenced in code/build | Must not be promoted to design intent without confirmation |
| **Temporary decision** | Approved working assumption | Record a revisit trigger |
| **Open question** | Unresolved material point | Include owner, impact and status |
| **Example** | Illustration of a rule | Must not introduce a new rule |
| **Deprecated** | Retired behavior | Keep out of current-state rules; retain a replacement link |

For a complex or disputed area, use a claim table:

| Claim | State | Evidence/source | Owner | Status |
|---|---|---|---|---|

Avoid vague phrases such as “normally,” “probably,” “as needed” or “should work” unless the uncertainty is intentional and labeled.

## Document architecture

A GDD uses progressive disclosure. Sections may be omitted only when genuinely not applicable.

### Layer 1 — Orientation

- Summary.
- Player experience/design goal.
- Scope and exclusions.
- At-a-glance facts.
- One visual overview when the system has meaningful relationships or sequence.

### Layer 2 — Normative design

- Core rules.
- States and flow.
- Inputs, conditions, outputs and failure handling.
- Formulas with variable definitions and at least one worked example when non-trivial.
- Interactions and dependencies.
- Edge cases.

### Layer 3 — Evidence and operations

- Structured configuration links.
- Exact Figma frames or visual references.
- Repository paths and runtime drift.
- Analytics and acceptance criteria.
- Open questions, validation state and change authority.

The first two layers must explain the feature without requiring the reader to open every external source. The third layer must make important claims traceable without copying live data or final visual assets.

## Writing rules

- Follow the receiving project's language policy (English by default for KB content); preserve exact identifiers and player-facing localized terms when relevant.
- Define an important term once and use it consistently. Do not alternate synonyms for the same system concept.
- Wrap config IDs, class names, fields, events and formulas in backticks.
- Use numbered rules when order matters; bullets when order does not matter.
- State the actor and condition explicitly. Prefer “When the player confirms the upgrade…” over “When confirmed…”.
- Separate rule, rationale and example. An example cannot be the only definition of behavior.
- Keep paragraphs focused on one claim or relationship.
- Link the canonical owner on first meaningful reference to an external system.
- Never place a material decision only in chat, a comment or an image.

## Visual decision standard

Choose the smallest representation that makes the relationship clearer:

| Information shape | Preferred representation | Ownership rule |
|---|---|---|
| Exact mappings, comparisons or condition/result rules | Markdown table | KB owns the rule |
| Ordered behavior with branching | Mermaid flowchart | KB owns logical behavior |
| State lifecycle and transitions | Mermaid state diagram | KB owns state logic |
| Cross-system dependency or stat routing | Compact Mermaid diagram | KB owns system relationship |
| Numeric trend, curve or composition | Chart generated from source data | Sheet/CSV owns values; GDD owns interpretation |
| UI layout, spatial hierarchy or prototype | Exact artifact from the visual-design source (for example, a Figma frame) | The designated visual-design source owns final composition |
| Player-facing appearance, VFX or art target | Image/video/reference with caption | Figma/art source owns final asset |
| Simple fact or one-step rule | Text | Do not force a visual |

### Diagram rules

- Give every diagram one question to answer.
- Keep labels short and use canonical terms/IDs.
- Prefer top-down flow for multi-stage systems.
- Split a diagram when it mixes unrelated concerns or becomes difficult to scan.
- Put detailed conditions in adjacent prose or a table instead of overloading node labels.
- Follow every diagram with a short textual interpretation of the important path and exceptions.

### Table rules

- Give columns stable, specific names.
- Put one semantic entity per row.
- Do not merge cells or encode meaning only through color.
- State units in headers or values.
- Use `—` for not applicable and `Unknown` for unknown; do not leave ambiguous blanks.

### Formula and chart rules

- Define every variable and unit.
- State clamping, rounding and evaluation order where they matter.
- Include one worked example for a non-trivial formula.
- Link the live dataset/config and record the snapshot date for a static chart.
- Do not manually copy a frequently changing balance table into the GDD.

### Image and Figma rules

- Provide meaningful alt text and a caption.
- Label the asset as `Reference`, `Concept`, `Current`, `Target` or `Deprecated`.
- Link the exact source frame/file and identify the owner.
- Do not rely on text embedded inside an image as the only statement of a rule.
- Prefer a linked Figma frame for final UI composition; use a KB snapshot only when it supports offline reading or a durable comparison.

## AI-readability requirements

- Headings must describe content rather than use generic names such as “Other” or “More.”
- Critical terms, IDs and states must exist as text, not only inside images.
- Tables must use literal headers and consistent row structure.
- Each external link must say what it contains and which facts it owns.
- Every open question includes an owner, impact and status.
- Runtime evidence includes a repo path, class/method or test/build reference when available.
- If a diagram and prose conflict, the normative rule/table wins until the conflict is resolved; fix both during review.
- Avoid hidden meaning through color, position, emoji or formatting alone.

## Source and authority rules

| Knowledge | Canonical source |
|---|---|
| Design intent, stable rules and accepted behavior | KB GDD |
| Numeric configuration and large balance tables | Designated Sheet/synced CSV |
| Implemented behavior and schemas | Designated repository/runtime evidence |
| Final UI/UX layout and prototype | Designated visual-design source |
| Raw telemetry and analytics data | Designated analytics source |
| Historical or superseded material | Archive/Decision Log |

When sources disagree, record the conflict. Do not merge incompatible claims into apparently certain prose.

## Pre-write confirmation

For new GDDs, substantial rewrites and migrations, complete the relevant source discovery and analysis before the first canonical KB write. Match the result to existing explicit approval: an approved brief or scoped user request already authorizes its stated content and artifacts. Do not require a new confirmation pack solely because the work is substantial. When material decisions, conflicts or publication authority remain unresolved, present one consolidated pack containing:

- Confirmed canonical/config/runtime facts that will be carried forward.
- Material ambiguities, conflicts and decisions required from the owner.
- Recommended resolutions with relevant trade-offs.
- Temporary assumptions with confidence, scope and revisit trigger.
- Non-blocking unknowns and their validation requirement.
- Exact files, ownership boundaries, lifecycle statuses and canonical flags to publish.

Ask follow-up questions only for material points. If the feature owner explicitly confirms the pack, that confirmation is the approval evidence for its exact scope. Publish directly with the final approved metadata. A second document-level approval is required only when material content changes after confirmation.

Use a KB draft or `status: review` checkpoint only when the owner cannot yet resolve a material point, both parties intentionally defer the decision, or the owner explicitly requests a durable checkpoint. Working notes that do not need durable collaboration should remain outside the canonical KB.

## Review and activation

Run [GDD Review Checklist](gdd-review-checklist.md) against the analyzed content and existing approval evidence (or a confirmation pack when needed) before publication. A confirmed result may be written directly as `active` when:

- Blocking conflicts are resolved or explicitly excluded from scope.
- Design rules are separated from runtime observations.
- Required source links and visual context are present.
- Essential behavior remains understandable in text/structured form.
- Existing explicit approval covers the exact content and artifact scope; any material departure has been resolved.
- The written artifacts are read back and verified immediately after publication.

Readback is technical verification and does not create a new approval round. If the readback reveals a material departure from the approved scope, correct it or return only that difference to the owner.

Non-blocking open questions may remain in an active GDD when their scope, owner, impact and revisit trigger are explicit. Their uncertainty belongs in claim-level evidence and `validation`, not automatically in the document lifecycle status.

## Related notes

- [GDD Templates](gdd-templates.md)
- [GDD Review Checklist](gdd-review-checklist.md)
- [GDD Migration workflow](../skills/gdd-migration/SKILL.md)
- [Knowledge Steward](../skills/knowledge-steward/SKILL.md)
- [Source of Truth](source-of-truth.md)
- the receiving project's accepted governance decisions
