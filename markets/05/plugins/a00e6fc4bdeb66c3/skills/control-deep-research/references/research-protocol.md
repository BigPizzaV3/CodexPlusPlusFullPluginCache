# Research protocol

## Claim ledger

Track material claims with:

| Field | Meaning |
|---|---|
| Claim | Exact proposition being supported |
| Status | Verified / inferred / disputed / unknown |
| Source | Direct page or record actually consulted |
| Authority | Primary / institutional / secondary / community |
| Date | Publication and relevant event/effective date |
| Scope | Jurisdiction, population, product version, or conditions |
| Confidence | High / medium / low with a brief reason |

## Research stopping criteria

Stop when:

- every decision-critical question has sufficient evidence or is explicitly unresolved;
- important claims have current authoritative support;
- major contradictions are represented;
- additional sources repeat known evidence without changing the decision;
- the user’s requested depth and time constraints are met.

## Production-method research

When the research will inform a material method decision, classify the reference evidence as `REFERENCE_QUALITY`, `MECHANISM_VERIFIED`, `APPLICABILITY_TO_PROJECT` and `EVIDENCE_LIMITS`. Pass those fields, source/guidance version, actual verification date and first-party guidance type into the existing scoped method record owned by the shared [decision-authority model](../../../shared/expert-system/decision-authority-model.md). Persist or explicitly deliver that record with a stable ID/revision for later reuse and targeted revalidation. Do not label an interesting reference as a verified mechanism, and do not decide or reopen the method from research evidence alone.

For freshness-triggered research, use the canonical method-freshness fields and comparison loop in that same decision-authority model. Identify the changed claim, scoped source/version/date and observed validation context separately from vendor documentation. Return whether material change is evidenced, applicability, unresolved limits and the authorized next step; preserve the closed method when no material change is established. Persist only under existing write authority, with prior revision retained. Do not stamp a whole method/toolchain CURRENT from one checked page or create a new production-knowledge register.

## Red flags

- Undated pages for fast-changing facts.
- Vendor claims presented as independent evidence.
- A secondary article contradicting a newer primary source.
- Citations that support a nearby topic but not the actual claim.
- Precise numbers without methodology, population, currency, tax basis, or date.
- “Latest” conclusions without an explicit research date.
