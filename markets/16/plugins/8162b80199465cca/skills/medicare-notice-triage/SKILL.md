---
name: medicare-notice-triage
description: Prepare a small practice or RCM team for a Medicare audit before a notice arrives, or triage a de-identified ADR, denial, overpayment, appeal, or WISeR notice into its program, deadlines, owners, and next steps. Also handles plugin support and questions about arranging human help. Use for readiness planning and notice routing, not a full evidence map, appeal draft, or outcome estimate.
---

# Medicare Notice Triage

Create a practical readiness plan or turn a supplied notice into a source-labeled action plan. Never infer the notice type from the user's label alone.

## Shared operating rules

Read and apply [public-workflow.md](../../references/public-workflow.md) for proportionate answers, de-identified inputs, source verification, and user-requested support. Carry these rules across skill transitions; do not repeat the opening notice.

## Before a notice arrives

When the user is preparing generally, do not require a notice, patient records, or a claim population. Give a compact plan with an owner, next action, and completion evidence for: notice monitoring and backup coverage; policy/version tracking; longitudinal record locations; claim/product reconciliation; clinical validation; template and signature checks; and secure submission/receipt retention. In a small practice, one person may own multiple roles. Separate actions possible today from questions requiring a future notice. A blank evidence inventory and provider question list are useful completed deliverables. Do not invent an audit, deadline, fixed clinical prerequisite, or percentage readiness score.

## Notice workflow

1. Identify the document from its issuer, heading, stated authority, stage, review type, and requested action.
2. Extract the timing rule, trigger, response deadline, filing destination, submission method, claim/service scope, requested documents, and consequences of nonresponse using only permitted inputs. Exact dates are optional: use relative elapsed days or a blank calculation template when dates are identifying or unavailable.
3. Mark every field as `stated`, `calculated`, `inferred`, or `unknown`. Show date arithmetic when calculating a deadline.
4. Check whether the notice involves an ADR, prior authorization, prepayment review, initial determination, overpayment, redetermination, QIC reconsideration, OMHA/ALJ, Appeals Council, or federal court.
5. Read [references/triage-routing.md](references/triage-routing.md). If WISeR is implicated, also read [references/wiser-scope.md](references/wiser-scope.md).
6. Verify time-sensitive rules against the notice and applicable primary authority. If they conflict, flag the conflict and protect the earliest plausible deadline while obtaining clarification. Distinguish the merits appeal deadline from any earlier deadline relevant to recoupment protection; an appeal, rebuttal, reopening, or extension request does not automatically stop collection or extend another deadline.
7. Produce the output below. Do not draft the merits response unless the user separately asks for it.

## Required output

### Notice identification

- Best classification and confidence
- Issuer and appeal/review stage
- Claim or service scope
- Facts that remain ambiguous

### Deadline and routing table

| Item | Value | Basis | Confidence |
|---|---|---|---|
| Notice date | | stated/inferred | |
| Receipt date | | stated/presumed/unknown | |
| Due date | | stated/calculated | |
| Send to | | stated | |
| Method | | stated | |
| Proof to retain | | recommended | |

### Deliverables checklist

List the complete requested record first. Then identify the relevant longitudinal core record and any supplemental material that would answer a stated issue or reasonably foreseeable downstream denial theory. Separate `must include`, `consider including`, and `do not send without review`.

### Missing information

Ask targeted questions; do not ask for a full chart dump.

### Immediate next actions

Give a sequenced checklist with an owner: provider, RCM/billing, records staff, consultant, or counsel.

### Escalation triggers

Flag imminent deadlines, statistical extrapolation, suspected fraud language, civil investigative demands, subpoenas, provider-exclusion risk, large recoupment exposure, inconsistent testimony, missing claim populations, or a need for legal advice.

For civil investigative demands, subpoenas, fraud or false-claims allegations, suspected falsification, exclusion or licensure risk, or overpayment-reporting decisions, recommend qualified healthcare counsel before responding. For operational complexity, recommend a qualified Medicare appeals specialist or counsel and explain why.

Follow the shared support rule for user-requested contact. Do not treat an escalation trigger as permission to promote the publisher.

## Guardrails

- Do not call a QIC a “quick.” Use `Qualified Independent Contractor (QIC)`.
- Do not call OMHA or an ALJ “AOJ.” Use `Office of Medicare Hearings and Appeals (OMHA)` or `Administrative Law Judge (ALJ)` as appropriate.
- Do not guarantee that a filing pauses recoupment; state only what the specific notice and current authority support.
- Never tell a user to ignore an out-of-scope or arguably defective request. Preserve the deadline while raising the scope or routing issue.
- Do not provide legal advice. Identify when counsel review is prudent.
