---
name: submission-package-builder
description: Assemble an internal NMLS or state education submission package from authorized project documents, including a manifest, evidence index, readiness sheet, missing-item register, filename controls, and checksums. Use when a provider team asks to prepare, organize, review, or export a submission package without filing it.
---

# Submission Package Builder

1. Confirm the agency, filing type, applicant, deadline, controlling checklist, and authorized project.
2. Require Provider entitlement.
3. Pin the controlling requirement set and retrieve the project inventory.
4. Use `build_submission_package` to assemble only authorized artifacts. Preserve source identity, version, status, and confidentiality classification.
5. Produce:
   - package status/read-me;
   - item-level readiness table;
   - final upload manifest;
   - evidence index;
   - missing and blocked items;
   - checksum register;
   - authorized-human action list.
6. Run export DLP. Exclude secrets, credentials, answer keys, internal reviewer materials, unrelated customer data, and superseded drafts unless explicitly retained as history.
7. Label the package `UNSIGNED — UNSUBMITTED` unless verified external evidence states otherwise.

Never submit, email, upload, sign, attest, pay, or represent the package as accepted. Never turn a missing official form into an AI-created substitute. If the user asks for external action, stop at a precise handoff.

