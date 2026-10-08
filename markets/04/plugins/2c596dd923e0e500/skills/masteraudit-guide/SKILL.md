---
name: masteraudit-guide
description: Guide users through MasterAudit retrospective evidence-coherence review, supported task types, technical evidence interpretation, and human-review boundaries.
---

Use this skill when a user asks whether MasterAudit fits a retrospective evidence review, wants to understand supported review types or compliance declarations, or wants help interpreting an audit event, ledger, certificate, or unresolved result.

## Workflow

1. For a new review question, call `masteraudit_knowledge_map` first and explain whether the requested retrospective evidence-coherence review fits the public MasterAudit scope.
2. When the user asks what can be reviewed, call `masteraudit_task_types` and report only the task types returned by the service.
3. When the user asks about compliance posture, call `masteraudit_compliance` and label every declaration as a published profile statement, not independent certification.
4. For questions about certificates, legal admissibility, truth, guilt, or liability, call `masteraudit_legal_evidence_policy` and explain the technical-evidence and human-review limits. Do not provide an individual legal ruling.
5. For audit events, ledgers, certificates, or unresolved results, call `masteraudit_result_interpretation_contract`. Distinguish integrity binding and bounded review findings from factual correctness or legal conclusions.

## Boundaries

- The public MasterAudit tools provide guidance and interpretation only. They do not retrieve private evidence, execute audits, create certificates, send reports, or control external systems.
- Do not request, accept, or forward API keys, passwords, MFA codes, private evidence, private tenant data, or login credentials.
- Do not claim that coherence, integrity, or a certificate proves truth, guilt, liability, legal validity, or independent certification.
- Do not use MasterAudit guidance for live actuation, blocking a controller, or other production control.
- If a request requires private data, authentication, an audit run, certificate creation, or external delivery, explain that it is outside this public plugin and do not call a tool.
- If the user asks for unrelated writing or productivity help, do not activate this skill.

## Response requirements

Use returned tool data as the source of truth. State the evidence scope, review boundary, and need for human review in plain language. Never invent a task type, audit result, certificate, or external authority.
