# Evidence records and outputs

## Logical records

These fields are an internal evidence contract, not a mandatory raw JSON response. Unknown values stay null or Unknown. Export structured records only when requested or useful.

| Record | Fields |
|---|---|
| Run | assessment_date, mode, N, sources, user_constraints, limitations |
| Source | source_id, type, filename_or_URL, known_version_or_date, inspected_extent |
| Fact | fact_id, claim, source_id, location, role/context, known_dates, conflict_state |
| Requirement | requirement_id, employer_text, source_location, tier, importance, logical_alternatives, deadline, category |
| Match row | requirement_id, fact_ids, evidence_class, requirement_status, gap_type, impact, explanation |
| Assessment | functional_fit, eligibility, confidence, strengths, gaps, qualification_axes, material_questions |
| Opening | employer, title, requisition_id, URLs, source_kind, location, arrangement, pay, posting_date, checked_at, availability_evidence, assessment, constraint_status, comparison, admission_decision |
| Draft claim | draft_location, text, fact_ids, transformation, unresolved_state |

Facts may support multiple requirements without becoming multiple years or achievements. Evaluate OR as one logical condition retaining its satisfied branch; report independent AND requirements separately.

## Assessment output

Lead with functional fit, eligibility, confidence, and a short decision explanation. Then provide:

1. Mandatory requirements: Requirement / Evidence / Status. If none specified, say so rather than implying universal eligibility.
2. Strongest matches: Employer need / Candidate evidence / Why it matters.
3. Weakest areas: Gap / Classification / Impact / Action.
4. Qualification level: Axis / Level / Evidence and a short synthesis.
5. Up to five high-value improvements and only material questions.

For only blockers, show blockers and consequential unknowns. Do not force five improvements or three strengths when fewer exist.

## Alternatives

Use Rank / Job and source link / Fit / Eligibility and constraints / Versus original / Main evidence and tradeoff. Include check times and stated pay/location next to each job. Keep conditional/unverified leads outside N. State count, actual search scope, and limitations. Never present fixtures as real openings.

## Targeted resume

Deliver one complete draft or file. Keep change log and questions outside it. Clearly identify review drafts with unresolved fields. Retain source IDs internally or in a requested appendix, not as clutter in an application-ready resume.
