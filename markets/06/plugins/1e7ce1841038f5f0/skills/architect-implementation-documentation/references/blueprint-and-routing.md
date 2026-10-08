# Documentation blueprint and routing

## Blueprint entry

For every planned document define:

- artifact ID and title;
- implementation area and exact purpose;
- primary authoring skill or accountable owner;
- required inputs and source IDs;
- required sections and out-of-scope content;
- decisions the document owns;
- upstream and downstream dependencies;
- overlaps and precedence relationships;
- target status and usage class;
- document-level acceptance tests;
- suite-level readiness dependencies.

## Document selection

Create only documents needed to remove real implementation ambiguity. Typical candidates include product requirements, functional specification, technical architecture, data model, API contracts, AI system specification, UI/UX specification, content/assets specification, security/privacy specification, operations/deployment specification, test plan, migration/rollback plan, and implementation roadmap.

Do not create every candidate by default. Split documents when they have different owners, release cadences, authorities, or review methods. Merge when separate files would only repeat the same decisions.

## Routing boundaries

| Need | Primary skill | Neighbor / non-trigger |
|---|---|---|
| Coordinate project workstreams | `orchestrate-projects` | Does not own document-suite authority. |
| Run end-to-end premium execution | `execute-premium-projects` | Does not replace the suite architecture. |
| Architect a complex specification suite | `architect-implementation-documentation` | Not for a single contained spec. |
| Author one engineering specification | `write-engineering-specifications` | Contributes to a suite only under a Blueprint. |
| Audit readiness | `project-specification-auditor` | Read-only; never closes gaps. |
| Architect reusable repository harness | `architect-coding-agent-harness` | Does not control live tasks or install automatically. |
| Control ongoing coding-agent work | `orchestrate-coding-agent-execution` | Does not rebuild the harness or own project strategy. |
| Verify an intermediate gate | `verify-implementation-checkpoint` | Read-only; not a repair or final release gate. |
| Verify final production release | `verify-production-implementation` | Final release only; does not absorb normal checkpoints. |
| Format approved content | `create-professional-documents` | Layout does not create implementation truth. |
| Transfer ordinary chat state | `handoff-work-between-chats` | Not a substitute for a large controlled spec pack. |
| Preserve long-term recoverability | `build-continuity-second-brain` | Indexes authoritative suite artifacts; does not duplicate them. |
| Build company operating structure | `build-company-operating-system` | Indexes complex developer packs; does not author duplicates. |

## Planning Master minimum

Record purpose, users, outcomes, scope, non-goals, constraints, confirmed decisions, assumptions, unknowns, source coverage, workstreams, phases, gates, owners, critical path, risks, acceptance, and definition of done. The Planning Master coordinates; it does not override specialist specifications unless the precedence matrix explicitly grants that authority for a named field.
