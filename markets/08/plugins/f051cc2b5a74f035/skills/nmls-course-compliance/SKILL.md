---
name: nmls-course-compliance
description: Audit a mortgage PE or CE course, outline, LMS design, or delivery process against current NMLS functional specifications, topics, timing, interaction, assessment, identity, attendance, marketing, retention, reporting, and format rules. Use for NMLS course compliance reviews and course-approval preparation.
---

# NMLS Course Compliance

1. Identify PE or CE, national or state-specific, course length, calendar year, and delivery format: classroom, classroom equivalent/webinar, OIL, or OSS. Do not infer the format.
2. Confirm Provider entitlement with `get_entitlements`.
3. Pin the current NMLS functional specifications, annual topics, provider policies, ROCS requirements, and relevant state-specific sources with `get_current_requirement_set`.
4. Inventory the outline, objectives, activities, assessments, timing evidence, identity/attendance flow, support, policies, certificate, reporting, and marketing copy.
5. Call `audit_course_compliance`. Require the tool to distinguish `PASS`, `FAIL`, `UNVERIFIED`, `NOT APPLICABLE`, and `CONFLICT`.
6. Report findings by requirement with source location, evidence, severity, remediation, owner, and retest method.
7. State separately what software tests establish and what still requires human duration, SME, regulator, or production validation.

Do not:

- claim course approval or SAFE credit;
- accept a green test suite as proof of regulatory compliance;
- expose course manuscripts, question banks, answer keys, assessment candidates, reviewer notes, or private evidence;
- invent missing timing, participation, identity, or completion controls;
- use a secondary source when a current primary source is available.

When sources conflict or the annual topic year is unclear, stop the affected conclusion and mark it for human review.

