# Readiness, gap closure, and clean-room handoff

## Audit boundary

Run `$project-specification-auditor` over the complete declared suite. The auditor reports only. It must not change a source, choose a solution, resolve a contradiction, or promote a status.

For controlled migration, audit the complete active/candidate suite with migration register, bidirectional coverage matrix and justified historical samples under the auditor's Historical Corpus Audit Policy. Do not reactivate historical directives by including them in the active first-read. Missing coverage, source conflicts or failed samples reopen relevant historical inspection and block affected readiness.

For every finding, create a gap record with severity, affected implementation area, source evidence, missing decision or specification, responsible owner/authoring skill, dependencies blocked, closure acceptance, and re-audit result.

## Gap closure

Close a finding only in the responsible source artifact through its legitimate authoring path. Never patch only the handoff to hide a defect in an upstream specification. Preserve prior versions and update control registers. Re-audit all affected documents and cross-document relationships.

Stop when a critical decision lacks an authorized owner, a required source is unavailable, two approved sources conflict without precedence, or closure requires an unapproved external/destructive action.

## Coding-agent first-read

The first-read must state:

1. exact project and implementation scope;
2. authoritative source manifest with versions, status, and usage class;
3. mandatory read order;
4. precedence matrix and conflict rule;
5. permitted, protected, and prohibited changes;
6. open decisions and blocked areas;
7. implementation sequence and current gate;
8. test commands or verification procedures;
9. acceptance criteria and definition of done;
10. required evidence, change log, and stop/escalation conditions.
11. project expert matrix and current lead, support, and independent review roles;
12. decision-authority model and logged Class-2 decisions;
13. last approved visual checkpoint and current perceptual status where applicable;
14. current task execution contract and representation strategy where applicable.
15. gate-specific source slices or compiled artifacts, including provenance, upstream authority, conflict handling and regeneration triggers, when the suite uses them.

It must instruct the coding agent not to change environment, framework, architecture, tools, UX/design, data contracts, or scope without explicit documented authority.

## Clean-room test

Give an independent reader only the first-read and referenced accessible artifacts. For each implementation area, verify that the reader can identify what to build, why, allowed files/modules, protected behavior, interfaces, requirement classes, controlled professional and engineering discretion, tests, perceptual acceptance, dependencies, conflicts, and when to stop.

Fail if hidden chat context is needed, a reference is missing or unreadable, a version is ambiguous, a Class-1 choice is unresolved, Class-2 judgment lacks role/bounds/evidence/review, representation feasibility is unproven where material, observables conflict, active sources overload the task without a usable controlled slice, a derivative lacks traceable authority, or the reader can make an unauthorized product, architecture, design, data, security, governance, or scope decision. Report the exact gap; do not simulate a confident implementation.
