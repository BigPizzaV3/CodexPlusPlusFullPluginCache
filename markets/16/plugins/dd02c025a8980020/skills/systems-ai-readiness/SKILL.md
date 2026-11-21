---
name: systems-ai-readiness
description: Assess process maturity and design responsible automation or AI support with human ownership, privacy controls, and explicit decision boundaries.
---
# Systems and AI Readiness

Use when a user wants to document, automate, or apply AI to a business process. A diagram or recommendation does not mean the system exists or has been implemented.

## Readiness sequence

1. Define the customer or operating outcome and the manual process that currently achieves it.
2. Confirm that the process is real, stable enough to document, and has a named accountable owner.
3. Map inputs, decisions, outputs, exceptions, handoffs, and failure consequences. Distinguish rules from judgment.
4. Identify suitable low-risk administrative assistance. Keep high-impact judgment with qualified humans unless a separately validated and governed system is approved.
5. Define data purpose, minimum necessary fields, provenance, access, notice/consent, retention, deletion, security, and vendor handling.
6. Specify human review, override, correction, escalation, stop controls, logging, and responsibility for errors.
7. Test realistic edge cases and failure modes before limited deployment; define ongoing monitoring and rollback criteria.
8. Verify available tools and integrations before claiming technical capability. Do not invent connections, permissions, or performance.

## Decision boundary

AI should not independently make consequential safety, eligibility, diagnosis, legal, financial, hiring, or service-commitment decisions based solely on an unvalidated workflow. Require qualified human judgment, explicit controls, and appropriate domain review. Keep customer-facing actions human-approved unless the process has been separately authorized and governed.

## Standard output

Provide the current maturity and evidence status, process map, potential assistance points, excluded decisions, owner/reviewer, data controls, failure handling, validation plan, and a bounded recommendation such as **DOCUMENT MANUALLY FIRST**, **READY TO TEST A LIMITED ASSIST**, or **NOT READY**.
