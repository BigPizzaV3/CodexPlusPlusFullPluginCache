# AI governance evidence: a worked invoice-agent example

An AI governance evidence bundle connects a decision to its context, accountable owner, controls, observations and unresolved questions. It helps another reviewer understand what was assessed and what still needs to be established. A valid file format is only one part of that evidence.

This walkthrough uses PALO's existing fictional invoice-exception case. It is an educational example with synthetic data and no payment, supplier or production connection. The reported sample outcome is not a measurement of a deployed system.

## What should an AI governance evidence bundle contain?

For this review, preserve the intended decision, the agent's permitted and prohibited actions, the expected effects, the observations used to check those effects, and an accountable review decision. Keep expectations separate from observations. If a required observation is unavailable, record the gap and its consequence for the decision.

| Record | What the invoice example provides | What a real review still needs |
|---|---|---|
| Scope and owner | A fictional invoice-exception scenario and an educational owner label | A named accountable owner, affected parties and the actual system boundary |
| Authority | Permission to read synthetic metadata and draft a summary; three prohibited actions | Enforced tool permissions and checks for alternative paths that could bypass them |
| Expected effects | A draft should exist and payment should remain unreleased | An agreed baseline, observation window and checks for all prohibited effects |
| Observations | A synthetic authority and expected-effect record | Dated observations from appropriate authoritative systems, with provenance and coverage limits |
| Human review | An illustrative `proceed-with-conditions` decision | Reviewer identity, decision rationale, unresolved gaps and follow-up responsibilities |

This is a review checklist for the worked case, not a universal compliance checklist or a claim that the sample contains production evidence.

## Start with the decision and authority boundary

The question is whether an agent may collect invoice-exception evidence and draft a proposed resolution while a named person retains release authority.

The sample permits reading synthetic invoice metadata and drafting an exception summary. It prohibits releasing a payment, changing supplier data or contacting the supplier. These distinctions belong in the record before the agent acts; an instruction to "handle the invoice" would leave the boundary unclear.

[Open the worked case in PALO Assessment Path](../PALO_AssessmentPath.html?sample=agentic-invoice#assessment-form) or inspect the [source Case File](../evidence-pack/cases/agentic-invoice-exception.case.json).

## Follow the six governance phases

| Phase | Question for the reviewer | Evidence to preserve |
|---|---|---|
| Frame | What use is intended, who is affected and who owns the decision? | Purpose, system boundary, owner and explicitly prohibited actions |
| Classify | Which risk route is plausible, and what context still needs review? | Screening assumptions, source references and unresolved classification questions |
| Assess | What could go wrong for people or delegated actions? | Impact questions, authority boundaries and oversight requirements |
| Control | What prevents or detects actions outside that boundary? | Proposed tool restrictions, reviewer identity and verification requirements |
| Measure | What observation would show that the intended effect occurred? | An expected draft and an independently checked, unchanged payment state |
| Prove and review | What can the evidence support, and what remains open? | Dated records, provenance, limitations, reviewer decision and follow-up |

The framework's phases organize the review. They do not make the sample's proposed controls production controls.

## Separate permission from the observed result

A policy decision allowing `draft_exception` says what may be attempted. It does not prove that the agent produced the right draft or avoided every prohibited effect.

The sample's expected post-state is:

```json
{
  "draftCreated": true,
  "paymentReleased": false
}
```

A reviewer should also consider the other prohibited effects: supplier data must remain unchanged and no external supplier message should be sent. In a real implementation, the verification method, observation source and its trust boundary need separate validation. A tool's own success message is not independent evidence of all external effects.

## How can a reviewer check the source record?

Open the [downloadable Case File](../evidence-pack/cases/agentic-invoice-exception.case.json) and compare the following paths. The paths identify fields in this specific JSON example; they are not additional evidence.

| JSON path | Value or content to inspect | What it supports |
|---|---|---|
| `caseId` | `case-gold-agentic-invoice` | Identifying the example being discussed |
| `context.exampleStatus` | `educational-non-production` | The declared educational scope |
| `context.declaredAuthority` | Allowed and prohibited actions | The stated authority boundary, not proof of enforcement |
| `evidence[0].content.expectedPostState` | `draftCreated: true`, `paymentReleased: false` | The intended post-state, not an observed execution result |
| `assessments[0].data.conditions` | Tool exclusion, reviewer identity and independent verification | Conditions that a real deployment would need to establish |

The evidence item's `status: ready` does not turn its expected post-state into an observed result. The file contains no production execution receipt, authenticated reviewer approval or authoritative observation of a payment system.

To adapt the example, first define the real authority boundary and expected effects. Next, identify the observation source for each permitted and prohibited effect, including supplier changes and external messages. Then collect and link the observations to the same scoped action and time window. Finally, record the review decision and any remaining uncertainty. If coverage is incomplete, the record must not claim that every prohibited effect was excluded.

## Read the example decision carefully

The source case records `proceed-with-conditions`. Its conditions are to keep payment release outside the agent's tool set, require reviewer identity and verify the post-state independently.

That record is an illustrative decision, not an approval of your use case. Reviewers must establish whether those controls exist, are effective in the intended environment and cover the actual risks. Missing evidence should remain visible rather than becoming an implicit pass.

## Export and hand over a useful record

Use the Assessment Path to connect the context, screening and impact questions to controls and indicators. Export the local evidence bundle and review its version, source references, assumptions and unresolved questions before sharing it.

Keep the original Case File and subsequent observations distinguishable. A schema-validation receipt proves that the file conforms to a contract; it does not establish legal compliance, security effectiveness or production authorization.

The [Case File and Evidence Bundle guide](p1-case-file-and-migration.md) describes the interoperable record. Use the [board review template](../templates/board-review.md) to structure an accountable handover and the [indicator examples](ai-governance-kpi-kri-examples.md) to plan follow-up measurement.

## Sources and related methodology

The worked facts above come from the [versioned PALO sample](../evidence-pack/cases/agentic-invoice-exception.case.json). The sample references the [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) as a starting point. Its inclusion is not an endorsement or a certification of PALO.

For the wider operating model, read the [PALO lifecycle guide](../PALO_Guide.html), [semantic foundation](palo-v3-semantic-foundation.md) and [agentic governance modality](../PALO_AgenticGovernance.html).

## Compare the case with an impact-assessment record

[Download the fictional public-service FRIA record](../examples/fria/public-service-readiness.example.json) and inspect it in the [FRIA tool](../PALO_FRIA.html). Save any current work before importing. Its context, affected groups, illustrative ratings, mitigation notes and halt decision show what an incomplete evidence base looks like. It is a separate teaching case, not an assessment of the invoice agent above.

Use the [worked indicator register](../templates/ai-governance-indicator-register.example.csv) to inspect formulas and denominators alongside review actions. These samples are educational inputs; they are not an executed runtime evidence bundle.

## Authorship and revision

Written and maintained by [Fabrizio Degni](../PALO_Community.html#creator) for PALO Framework. Article revision 1.1, updated 23 October 2026, adds the review checklist and field-level source walkthrough. The source Case File uses schema version `1.0.0` and retains its own recorded dates; this article update is not a new execution or validation of the sample.

To cite this walkthrough, use: Fabrizio Degni, *AI governance evidence: a worked invoice-agent example*, PALO Framework, revision 1.1, 23 October 2026, [canonical article](https://paloframework.org/docs/ai-governance-evidence-worked-example.html). Cite the separate source Case File when referring to its fields.
