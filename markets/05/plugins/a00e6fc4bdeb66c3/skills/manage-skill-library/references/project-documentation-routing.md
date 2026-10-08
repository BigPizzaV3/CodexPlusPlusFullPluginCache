# Project and documentation routing matrix

| Capability | Primary owner | Neighbor boundary | Non-trigger | Upstream | Downstream |
|---|---|---|---|---|---|
| Project orchestration | `orchestrate-projects` | Coordinates specialists; does not own spec-suite truth. | A single document request. | Objective and authority. | Workstreams and artifact register. |
| Premium execution | `execute-premium-projects` | Owns lifecycle/quality, delegates documentation architecture. | Trivial or read-only requests. | Evidence and scope. | Implementation and verification. |
| Documentation architecture | `architect-implementation-documentation` | Owns multi-document lifecycle, not domain implementation. | Single bug-fix spec, normal handoff, Company OS, Second Brain, simple DOCX. | Sources, decisions, plan. | Controlled suite and first-read. |
| Engineering specification writing | `write-engineering-specifications` | Owns one spec or Blueprint-assigned contribution. | Pure PM or read-only audit. | Evidence or approved Blueprint. | Implementable technical contract. |
| Readiness audit | `project-specification-auditor` | Strictly read-only. | Authoring or gap repair. | Declared briefing/suite. | Findings and gate result. |
| Handoff | `handoff-work-between-chats` | Ordinary portable state; large coding packs route to documentation architect. | Authoring missing specs. | Current verified state. | Receiving chat/agent. |
| Continuity | `build-continuity-second-brain` | Indexes canonical specs; does not duplicate their truth. | One-session handoff. | Authoritative artifacts. | Recoverable operating memory. |
| Company OS | `build-company-operating-system` | Organizes company records; indexes developer packs. | Technical spec-suite creation. | Company evidence. | Operating workspace. |

Lifecycle flow for a complex build: project orchestration/premium execution → documentation architecture → specialist specification writing → readiness audit → author-owned gap closure → first-read handoff → implementation → QA → continuity/company indexes as applicable.
