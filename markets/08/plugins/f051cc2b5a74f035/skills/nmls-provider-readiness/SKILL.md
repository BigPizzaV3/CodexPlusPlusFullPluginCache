---
name: nmls-provider-readiness
description: Assess an NMLS course-provider application or renewal package for completeness, evidence support, current-source alignment, contradictions, expirations, and human-action gates. Use for provider readiness, provider application checklists, renewal preparation, provider-policy packages, or questions about whether a provider submission is ready.
---

# NMLS Provider Readiness

Assess readiness; do not predict approval.

1. Establish the applicant, application type, education category, delivery format, target date, and controlling checklist version. Ask only for missing facts that change the assessment.
2. Call `get_entitlements` for `nmls_provider_readiness`. This server capability requires Provider. If unavailable, return the safe upgrade-required response without protected findings.
3. Call `get_current_requirement_set` for NMLS provider standards and the target date. Use `search_official_sources` when the controlling document is missing or potentially superseded.
4. Inventory every submitted document. Treat a filename or user assertion as an inventory fact, not proof of content.
5. Call `assess_provider_readiness` with the pinned requirement set and authorized document references.
6. Classify each item as `READY`, `NEEDS DOCUMENT`, `NEEDS HUMAN EVIDENCE`, `NEEDS CURRENT SOURCE`, `REVIEW REQUIRED`, `BLOCKED`, or `NOT APPLICABLE`.
7. Return a readiness table, top blockers, source/effective-date list, contradictions, expirations, and the exact next human actions.
8. Offer a controlled export only when the plan permits it.

Never:

- claim or imply NMLS approval;
- sign, attest, submit, email, upload, or pay;
- treat coaching, mentoring, curriculum work, or supervision as direct classroom or virtual instructor-led teaching evidence;
- expose another project, reviewer-only material, credentials, or private StateCourse evidence;
- mark an item READY without evidence and a current controlling source.

If the user asks to submit or sign, prepare a handoff checklist and state that an authorized human must perform the external action.
