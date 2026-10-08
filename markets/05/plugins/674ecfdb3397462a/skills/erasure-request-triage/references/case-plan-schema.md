# Case Plan Schema

Produce a concise, evidence-based, data-minimised case plan with one case summary followed by one assessment per reviewed record. Case-level fields appear once. Record-level fields may repeat across different records but only once within each record assessment.

Use exact canonical tokens from `SKILL.md` whenever an assessment exists. Use `null` for a value that has not been established and explain what is missing. Never copy `case_status` into another field, invent a placeholder token, rename a canonical field, or synthesize an enum-like value from prose.

## 1. Status

Emit a dedicated `case_status` field containing one exact status token defined in `SKILL.md`. Do not replace it with narrative wording.

Use `RECORD_REVIEW_COMPLETE` when the read-only review is complete but receipt date, applicable jurisdiction/deadline, accountable owner, or next action is missing.

Use `CASE_PLAN_READY` only when those operational elements are also supplied or established. It may include `HUMAN_REVIEW` records when each outstanding issue has an explicit next step and accountable owner. It never signals treatment approval or execution.

## 2. Request summary

Include request classification, claimed requester/data subject, claimed identifiers, requested scope, and source mode/reference when available.

## 3. Verification, authority, and validity

When verification is established, emit exactly one of these values in the dedicated `verification_trust` field:

- `OPERATOR_ATTESTED_VERIFICATION`; or
- `TRUSTED_VERIFICATION_CONFIRMED`.

When verification is not established, emit `case_status: NEEDS_VERIFICATION`, set `verification_trust: null`, explain what verification evidence is missing, and emit `records: []`. When required representative authority is missing, use `case_status: NEEDS_AUTHORITY_VERIFICATION` and likewise do not assess records. An empty collection means no findings are reported, not that a search found no matches. Do not combine verification and policy into a single trust field.

Include verification method and non-secret reference. Record representative authority separately when applicable. Include request-validity status.

State that operator-attested verification is a procedural assertion, not authentication performed by the Skill.

When the operator supplied the verification result, emit exactly `verification_trust: OPERATOR_ATTESTED_VERIFICATION`.

## 4. Source review

For each source actually reviewed, show:

- source/connector type;
- operator-authorised scope;
- identifiers used;
- review/search time when available;
- result; and
- inaccessible or not-reviewed limitations reported by the source/tool.

For supplied/uploaded evidence, identify it as operator-supplied evidence rather than implying a connector search.

Do not manufacture an organisation-wide inventory or claim unseen coverage.

When an authorised completed search has no matches, emit the exact token `NO_MATCHES_IN_SEARCHED_SCOPE` as the source result and, when it is the overall outcome, as `case_status`. Do not substitute "no results," "nothing found," or similar prose.

## 5. Candidate-record assessment

For each relevant candidate, show only what the operator needs:

- minimal record reference;
- match strength and evidence;
- record category;
- mixed-person indicator when relevant, without reproducing unrelated PII;
- hold or retention evidence;
- policy title/version/effective date, provenance, and `policy_trust` when supplied;
- `record_recommendation`; and
- `downstream_next_step`.

Use the dedicated `record_recommendation` field containing the applicable exact token from `SKILL.md`. For a non-matching record, include only the minimal stable record reference and result, for example `record-A — no match`. Do not repeat an unrelated person's name, email address, account number, identifier, record content, or other personal information, even when it was supplied directly in the prompt or source material. Include more only when strictly necessary to identify a material privacy or legal issue, and then disclose the minimum needed.

If policy provenance or policy trust is incomplete, use `record_recommendation: HUMAN_REVIEW` while retaining the completed read-only review findings. Use `case_status: POLICY_REQUIRED` when missing policy is the principal case-level blocker. For operator-supplied policy, emit exactly `policy_trust: OPERATOR_ATTESTED_POLICY` and state that the Skill did not independently authenticate the policy approval.

If authorised record review is complete but policy is missing, retain the record evidence, set `policy_reference: null` and `policy_trust: null`, use `record_recommendation: HUMAN_REVIEW`, and identify the missing policy and accountable next step.

## Complete three-record example

```yaml
case_summary:
  case_status: CASE_PLAN_READY
  request_summary: "Verified erasure request covering the authorised customer-record scope."
  request_source: "operator-supplied request"
  verification_trust: OPERATOR_ATTESTED_VERIFICATION
  verification_method: "authenticated customer portal"
  verification_reference: "DEMO-001"
  representative_authority: null
  source_coverage: "Authorised Drive folder reviewed using the verified email identifier."
  receipt_date: "2026-09-01"
  deadline_basis: "South Africa; operator-supplied case timetable"
  accountable_owner: "Privacy Operations"
  next_action: "Route each proposed treatment to its named owner."
records:
  - record_reference: "customer-profile-01"
    match_evidence: "Verified email matched the profile's primary identifier."
    record_category: "Customer Profile"
    mixed_person: false
    hold_or_retention_evidence: "No applicable hold; policy conditions satisfied."
    policy_reference: "Demo Privacy Policy v1 — Customer Profile Rule"
    policy_trust: OPERATOR_ATTESTED_POLICY
    record_recommendation: DELETE_CANDIDATE
    supporting_reason: "The attested rule permits downstream deletion consideration for this category."
    downstream_next_step: "Route to Privacy Operations for the separately authorised deletion workflow."
  - record_reference: "invoice-02"
    match_evidence: "Verified customer ID matched the invoice account reference."
    record_category: "Invoice"
    mixed_person: false
    hold_or_retention_evidence: "Finance schedule requires retention through 2031-03-31."
    policy_reference: "Finance Retention Schedule v3 — Invoice Rule"
    policy_trust: TRUSTED_POLICY_CONFIRMED
    record_recommendation: RETAIN_POLICY
    supporting_reason: "The trusted schedule requires continued retention."
    downstream_next_step: "Route the retention finding to the Finance Records owner."
  - record_reference: "complaint-03"
    match_evidence: "Verified email appears in the complaint record."
    record_category: "Complaint"
    mixed_person: true
    hold_or_retention_evidence: "No dispositive treatment rule established."
    policy_reference: "Complaints Handling Policy v2"
    policy_trust: OPERATOR_ATTESTED_POLICY
    record_recommendation: HUMAN_REVIEW
    supporting_reason: "The record contains material data about another person and needs proportionate-treatment review."
    downstream_next_step: "Privacy Lead to determine a proportionate treatment before any downstream action."
limitations:
  - "Read-only assessment; no record was changed."
  - "Only the stated authorised source scope was reviewed."
```

This example is ready as a plan even though one record requires human review because that issue has an explicit next step and accountable owner. It does not approve or perform deletion.

## Pre-response self-check

Immediately before responding, silently verify the case-summary/per-record structure, exact canonical values, supporting evidence for each record, explained nulls, and an accurate overall case status. Correct the response before sending; do not mention the check.

## 6. Operational fields

When supplied, include receipt date, applicable jurisdiction/deadline, accountable owner/reviewer, and next action.

Their absence does not block read-only review, but prevents `CASE_PLAN_READY`.

## 7. Unresolved items and next steps

List only material follow-ups. Use wording such as "Route this proposed treatment to the approved workflow or process," naming the downstream authorised owner or process when known. Do not phrase the proposal as a direct command to perform the underlying action. Never imply that the Skill itself will delete, trash, move, edit, anonymise, redact, alter, or suppress data; change account settings; send mail; clear or change a hold; or close the legal request. No additional identifiers, context, verification, policy, or approval can enable those actions through this Skill.

## 8. Communications

Draft only neutral holding or clarification language until applicable jurisdiction and sufficiently provenanced approved policy are supplied. Never draft a completion message in V1. Never send or create drafts in external systems.

## 9. Limitations

Always state that the Skill is read-only, does not authenticate requesters itself, does not provide legal advice, does not guarantee connector availability, does not search unconnected/unauthorised systems, does not modify records, and does not certify completed erasure.

State that `CASE_PLAN_READY` and `RECORD_REVIEW_COMPLETE` describe the readiness of the assessment only and do not authorise the operator to mark the organisation-wide case complete.
