---
name: check-curriculum
description: Browse verified state standards and check teacher-authorized lessons only where analysis is approved.
---

# CurriculumProof — expanding national standards library

Use the **actually installed** CurriculumProof MCP tools. The permanent state-neutral tools are `curriculumproof_coverage`, `curriculumproof_access`, `curriculumproof_check`, `free_browse_standards` and `free_get_standard`. Legacy state-specific lookup tools may appear temporarily; they are not required for future state releases.

## Determine current capabilities from the live tools

1. For a request, use the state, grade (currently Grades 3–5), and subject (English language arts, mathematics, science, social studies) the user provides. Ask only for an essential missing detail. Distinguish **standards lookup** from **lesson-alignment analysis**. Both capabilities have different release gates.
2. **Never use a fixed state list embedded in this skill to decide availability.** Texas and Virginia were the initial Free state releases, but the approved catalog may grow without a plugin ZIP update. For each requested scope, call the installed `free_browse_standards({scope_id,limit,cursor})` or `free_get_standard({scope_id,id})` and respect the server's current allowlist and status. `scope_id` follows the accepted format such as `VA-G04-SOCIAL_STUDIES`. If `SCOPE_NOT_AVAILABLE`, explain that this scope has not been published; do not fabricate records or substitute a nearby state. Use the exact record ID returned by browse; use a native code only when unambiguous.
3. Present approved **factual metadata** as returned: identifiers, code, source URL, source locator, edition, current source status, and hierarchy. Preserve `lesson_alignment: NOT_ASSESSED` for Free factual records. Merely listing standards never establishes lesson alignment or official approval. Do not quote protected government standards prose not supplied for redistribution.
4. For a teacher-authorized lesson check, use `curriculumproof_coverage` / `curriculumproof_access` as needed to verify **current, specific** grade/subject analysis readiness, then call `curriculumproof_check` only when the user supplies eligible curriculum text without student personal information. The **initial** approved Free lesson-analysis slice was Texas Grade 4 Social Studies geography/map skills; this is historical release context, **not** a permanent prohibition or approval for other scopes. Follow the latest actual tool disposition; if analysis is unavailable, abstain instead of evaluating standards from general model knowledge.
5. Preserve exact tool findings, scoped student-performance excerpts, `SUPPORTED` / `PARTIALLY_SUPPORTED` / superficial classifications, citations and limitations. Objectives-only statements, negation, teacher-only exposition, or whole-document keyword matches are not positive evidence of learner performance. Do not upgrade partial findings to full support, and never claim blanket compliance with a state's standards from a bounded check.

## Release, privacy and commercial boundaries

- The same five national tool names serve all currently approved states. Adding an eligible state must change the **governed backend release allowlist**, not add another per-state public tool pair. A state absent from today's tool results must fail closed, even if a past description said a large national catalog was planned.
- Do not request, transmit, or analyze student names, IDs, test results, individual grades, health information or other student personal data. Ask for redacted, teacher-authorized lesson material where appropriate.
- Never infer missing parent relationships; use returned parent ID/code exactly, preserving known source exceptions. Never fabricate source provenance, teacher review or agency endorsement.
- The public Free experience must not disclose private Paid Audit, Requirements, or HARDENED Evidence payloads. Do not promise paid features, purchases, subscriptions or settlements through this plugin.
- If the installed plugin does **not** expose `free_browse_standards` or `free_get_standard`, report that national Free lookup is unavailable in that client. Backend checks, a scan on the publisher dashboard and legacy Texas-only tools cannot substitute for real installed-client national acceptance.
