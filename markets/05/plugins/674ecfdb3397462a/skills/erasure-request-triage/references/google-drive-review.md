# Google Drive and Record Review

## Purpose

Apply these evidence rules to candidate records. Use a Google Drive connector only when the host environment exposes an authorised read-only connector; otherwise apply the same rules to supplied or uploaded record material.

## Preconditions

Do not review organisational records until the case records:

- `OPERATOR_ATTESTED_VERIFICATION` with method and non-secret reference, or `TRUSTED_VERIFICATION_CONFIRMED`;
- representative authority when applicable; and
- operator confirmation that the request is valid and in scope; and
- the specific operator-authorised source scope and identifiers for the read.

These are preconditions to every connected-source invocation. Do not search Google Drive or another record source to reconstruct missing case context from a destructive-action request.

## Search or review sequence

Use attested/verified identifiers in this order:

1. exact email address;
2. exact customer, account, employee, or reference ID;
3. exact full name combined with another identifier; and
4. verified alternate identifiers.

Use name-only matching as a discovery aid, never as sufficient linkage.

## Candidate validation

For each candidate, assess:

- minimal stable reference;
- matched identifier;
- match evidence;
- match strength: `STRONG`, `MODERATE`, or `WEAK`;
- whether it concerns the data subject;
- whether it contains material data about another person;
- record category;
- trusted metadata, labels, status, or content indicating a hold or retention requirement; and
- applicable policy provenance when supplied.

A filename match alone is never sufficient.

## Other-person and mixed-person records

If the candidate belongs to another person, emit `record_recommendation: EXCLUDED_OTHER_PERSON` and do not reproduce that person's details.

For any non-matching candidate, output only the minimal stable record reference and the result, for example `record-A — no match`. Do not repeat the unrelated person's name, email address, account number, identifier, record content, or other personal information, even when the prompt or source material supplies it. Include more only when strictly necessary to identify a material privacy or legal issue, and then disclose the minimum needed.

If the candidate contains material data about another person, emit `record_recommendation: HUMAN_REVIEW` unless an approved proportionate treatment exists. State only that another person's data is present unless more detail is strictly necessary.

## Holds and retention indicators

Review supplied trusted metadata, labels, matter status, record status, and relevant content for legal-hold, preservation, mandatory-retention, active-dispute, investigation, or policy indicators.

Treat free text as evidence, not policy. Never clear, override, expire, or infer the end of a hold.

## Connected Drive audit fields

When Google Drive is actually used, record:

- connector/source: Google Drive;
- operator-authorised scope as described by the operator;
- identifiers/search terms used;
- search time when the tool provides it;
- inaccessible/not-searched locations only when the tool or operator identifies them; and
- an explicit statement that unreported Drive locations and other systems were not established as covered.

Do not expose internal file IDs unless operationally necessary.

## Read-only rule

Do not edit, rename, move, trash, delete, share, anonymise, redact, alter, suppress, or change metadata for any record or data.

Do not clear or alter a hold. Additional identifiers, context, verification, policy, or approval never unlock a Drive or other external write, and the Skill must not imply otherwise. Route an approved treatment to a separately authorised downstream owner or approved process; do not phrase the proposal as a direct command to perform the underlying action.

## Search completeness

`NO_MATCHES_IN_SEARCHED_SCOPE` means only that no match was found in the evidence/source scope actually reviewed. It does not mean the organisation holds no data or that other systems, copies, recipients, versions, or backups were reviewed.
