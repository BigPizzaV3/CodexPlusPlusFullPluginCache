# Conditional Implementation Translation

Use this reference after a product, software, feature, API, or system-design direction has been selected and implementation detail would materially improve the result. Translate a good decision into a buildable specification without turning every request into a giant technical document.

## Contents

1. Trigger and proportionality
2. Implementation sequence
3. Domain boundary and abstraction level
4. Domain model
5. State model
6. Invariants and business rules
7. Time and scheduling semantics
8. Conflict resolution
9. Source, trust, and verification
10. Permissions and abuse cases
11. User-visible states
12. Second-order system effects
13. API and data implications
14. Migration and backward compatibility
15. Acceptance criteria
16. Architecture challenge for feature design
17. Validation honesty

## 1. Trigger and proportionality

Run this pass when one or more of these conditions hold:

- the user asks how a feature should actually work
- the task asks for edge cases, behavior, architecture, data structures, technical implications, or implementation planning
- the result is clearly intended to guide later software construction
- a product decision would remain ambiguous or risky without implementation semantics
- an existing feature or specification is being audited for material implementation gaps

Skip or compress it when:

- the task is casual brainstorming or early idea generation
- the question is purely strategic and implementation would not change the decision
- the requested output is small writing, messaging, or unrelated creative work
- the user explicitly asks for concept-only scope
- the available context is too thin for responsible technical detail

Choose the smallest useful depth:

- **Compact**: domain boundary, key entities, critical states or rules, second-order effects, and a few acceptance criteria
- **Standard**: add conflict handling, trust or permissions, migration implications, and a more complete behavior matrix
- **Detailed**: add fields, API behavior, validation, indexes, caching, or rollout details only when the stack and system context justify them

Do not mechanically output every section in this reference. Select only dimensions that affect correctness, scope, implementation risk, or user value. Keep the pass internal unless a visible implementation section helps the user consume a substantial specification.

## 2. Implementation sequence

After selecting the product or architecture direction:

1. State the feature's domain boundary.
2. Identify the smallest semantic model that correctly represents the known domain and plausible near-term extensions.
3. Define important entities, relationships, states, and invariants.
4. Resolve time, conflicts, trust, permissions, and user-visible behavior where relevant.
5. Ask which assumptions elsewhere in the system stop being true.
6. Trace downstream data, UI, analytics, integration, and operational effects.
7. Add API, storage, migration, rollout, or observability implications only when useful and supportable.
8. Convert the selected behavior into observable acceptance criteria.
9. Validate the specification for contradictions, missing states, over-modeling, and untested claims.

The result should be implementation-ready at the level the user needs, not database-complete by default.

## 3. Domain boundary and abstraction level

Define:

- what the feature represents
- what it deliberately does not represent
- which near-term extensions fit the same model
- which future requests would require a different subsystem or redesign

Prefer domain truth over generic flexibility. Use the smallest abstraction that correctly models the known domain and plausible near-term extensions.

Reject both common failure modes:

- **Under-modeling**: a patch that works for the first example but corrupts semantics, cannot express important states, or fails on predictable edge cases
- **Premature platform building**: a universal rules engine, workflow engine, event system, plugin architecture, or arbitrary condition builder without evidence that the domain needs it

A boundary is stronger than a vague V1/V2 list because it explains why some cases belong and others do not.

## 4. Domain model

Start with semantic entities and relationships before database tables unless the technology stack is known.

For each important entity, consider only relevant concepts such as:

- identity and ownership
- target or subject
- behavior or effect
- validity and conditions
- schedule
- source and provenance
- verification or trust
- lifecycle state
- relationships to existing canonical records

Ask:

- Is this a new entity, a state of an existing entity, or a derived view?
- Which data remains canonical?
- Which values are temporary, contextual, calculated, or historical?
- Can the model express the normal case without hiding exceptions in free text?
- Does the model preserve existing semantics rather than overwriting them?

Do not invent stack-specific field types, table names, or ORM patterns when the stack is unknown.

## 5. State model

Identify meaningful lifecycle states and transitions only when state changes affect behavior, permissions, display, or history.

Possible state categories include:

- draft or pending
- scheduled or upcoming
- active
- paused or unavailable
- expired or completed
- cancelled or withdrawn
- disputed or conflicting
- stale or needing revalidation

Distinguish:

- internal system state
- user-visible presentation state
- derived state calculated from time, verification, or dependencies

For each important transition, ask:

- what causes it
- who or what may trigger it
- whether it is reversible
- what history must be retained
- which downstream behavior changes

Avoid storing a state that should be derived unless persistence is justified.

## 6. Invariants and business rules

Capture rules that must always remain true. These often matter more than individual fields.

Examples of invariant forms:

- temporary or contextual data must not overwrite canonical base data
- expired or invalid rules must not appear as currently active
- unverified data must not be presented as verified
- conflicting records must follow an explicit rule rather than silent arbitrary resolution
- historical records must remain interpretable after the current state changes
- a user-visible action must not be allowed when required permissions or dependencies are absent

For each invariant, identify:

- where it is enforced
- which operation could violate it
- what user-visible behavior follows from failure
- what test or acceptance criterion would detect a violation

## 7. Time and scheduling semantics

When behavior depends on time, inspect the actual domain rather than defaulting to only `start_at` and `end_at`.

Consider as relevant:

- start and end dates
- inclusive versus exclusive boundaries
- weekdays
- one or multiple daily time windows
- timezone and daylight-saving behavior
- windows that cross midnight
- recurrence and recurrence end
- exceptions, exclusions, closures, and holidays
- indefinite recurrence
- editing an active or future schedule
- stale recurring data that is never reconfirmed
- display behavior for active now, later today, upcoming, and expired

Define whether time state is calculated at read time, materialized, cached, or updated by jobs only when that decision matters.

## 8. Conflict resolution

When multiple rules or records can apply, define behavior explicitly.

Ask:

- Can multiple rules apply simultaneously?
- Are effects stackable, mutually exclusive, or independently visible?
- Is precedence based on specificity, priority, source, verification, time, or another domain rule?
- Can more than one result be valid?
- Should ambiguity create a review or disputed state?
- What should the user see when the system cannot resolve the conflict confidently?

Avoid silent last-write-wins behavior unless it is an intentional and defensible domain rule.

## 9. Source, trust, and verification

Use when data is crowdsourced, user-entered, partner-supplied, imported, or otherwise uncertain.

Consider:

- source type and provenance
- submitted by and submitted at
- verification status and verifier
- last confirmed time
- evidence or attachment where appropriate
- duplicate detection
- conflicting reports
- owner-provided versus community-provided information
- staleness and revalidation policy
- moderation or review queues

Do not imply that provenance alone proves truth. Define how trust changes display, precedence, moderation, or downstream use.

## 10. Permissions and abuse cases

When relevant, define who may:

- create
- edit
- publish or activate
- pause or deactivate
- verify
- resolve conflicts
- delete or restore
- view internal evidence or moderation history

Consider misuse such as spam, self-promotion, manipulation, duplicate submissions, malicious edits, privilege escalation, or gaming rankings and analytics.

Do not add a full authorization system to a simple feature unless permissions materially affect correctness or risk.

## 11. User-visible states

Translate domain behavior into what a real user sees.

Use progressive disclosure. Ordinary users should see clear states and conditions, not internal machinery.

Potential presentations include:

- active now
- active later today
- upcoming
- expired
- unavailable
- conditions apply
- unverified
- disputed or conflicting
- last confirmed at a meaningful time

Define display priority, labels, actions, empty states, and error or ambiguity behavior when those affect usability.

## 12. Second-order system effects

For every material product, software, or system-design change, ask:

> If we add this feature, which existing assumptions in the rest of the system stop being true?

Inspect only systems that plausibly exist or are evidenced in the supplied context. Common dependency areas include:

- analytics and funnels
- statistics, aggregates, rankings, and indexes
- search and filtering
- caching and invalidation
- reporting and exports
- notifications and scheduled jobs
- recommendation or personalization logic
- authorization and onboarding
- historical data and audit trails
- external APIs and integrations
- imports, synchronization, and deduplication
- billing, entitlements, or accounting
- moderation and support workflows

For every invalidated assumption, record:

- the old assumption
- why it becomes false
- the likely failure or contamination
- the required safeguard, migration, filter, new dimension, or regression test

This is not a generic risk list. Focus on assumptions whose failure would materially corrupt data, behavior, decisions, or user trust.

## 13. API and data implications

Use only when enough technical context exists.

Consider:

- new or changed entities and relationships
- canonical versus derived fields
- validation rules and error behavior
- query patterns and indexes
- versioning or compatibility of existing contracts
- idempotency and duplicate handling
- caching and invalidation
- audit history and observability
- API read and write behavior
- bulk operations, imports, or exports

Prefer semantic requirements over implementation syntax when the stack is unknown. Label illustrative schemas as proposals, not final code.

## 14. Migration and backward compatibility

Treat feature work in an existing product as a change to a living system, not greenfield.

Consider:

- existing records and defaults
- historical interpretation
- legacy fields and values
- current API contracts and clients
- current UI and reporting assumptions
- backfill requirements
- feature flags or staged rollout
- rollback and partial deployment behavior
- old and new data coexisting
- index, cache, and job changes

State when no migration is needed rather than inventing one.

## 15. Acceptance criteria

Convert important behavior, edge cases, invariants, and second-order protections into observable criteria. Prefer Given / When / Then or an equivalent testable form.

Good criteria:

- describe preconditions and data state
- identify the user or system action
- state one observable result
- cover normal, boundary, conflict, invalid, and downstream cases where material
- distinguish UI behavior from internal behavior
- avoid merely restating the requirement

Include only the criteria needed to make the design implementable and reviewable. A compact feature may need five strong criteria; a high-risk feature may need a fuller behavior matrix.

Acceptance criteria are proposed checks until they are actually executed against an implementation. Never describe them as passed tests merely because they were written.

## 16. Architecture challenge for feature design

When architecture is consequential and several approaches are genuinely viable, use the competitive three-way challenge before committing to the implementation model.

Generate approximately three domain-appropriate approaches. Common shapes may include a minimal patch, a broad generalized engine, and a domain-specific abstraction, but do not force those shapes when the domain suggests better alternatives.

Every option must plausibly satisfy the known requirements. Compare with the same criteria:

- domain correctness
- implementation complexity and cost
- data integrity
- UX clarity
- migration and compatibility impact
- operational burden
- maintainability
- plausible near-term extensibility
- risk of under-modeling
- risk of premature generalization

State a meaningful disadvantage and likely failure mode for every option. Select, combine, or reject them based on the rubric. Do not make one option an obvious winner by underdeveloping the others.

The selected architecture is still a candidate. Compare it separately against real project conventions, standards, or external products when those benchmarks are available and useful.

## 17. Validation honesty

Distinguish:

- a proposed domain model from implemented schema
- acceptance criteria from executed tests
- architecture review from runtime validation
- a migration plan from a completed migration
- an API proposal from a verified contract
- a UI-state specification from rendered interaction testing

When an implementation exists, run the relevant tests and inspect actual behavior. When it does not, say that implementation and runtime validation remain unperformed. A strong specification can pass as a specification while the built feature remains unvalidated.
