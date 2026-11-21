---
name: study-design-and-methods
description: Extract or classify study designs and methods from research papers, protocols, theses, and reports. Use for design, setting, recruitment, eligibility, randomization, masking, follow-up, measurements, analysis, registration, or study conduct.
---

# Study design and methods

Start with the supplied source. This skill complements `research-data-extraction`; follow its missingness, provenance, and non-fabrication rules.

## Procedure

1. Locate Methods and any explicit design subsection. Check a supplied protocol/registry only as a separate source. Prefer Methods, then design subsection, protocol description, abstract methods, title.
2. Record the author's design label verbatim if present. Give an assistant classification separately and only when supported. If uncertain, use `UNCLEAR` and state what evidence is missing.
3. Extract objective/question/hypothesis; setting/country/centers; recruitment and study period; sample-size rationale; eligibility; sampling; allocation/randomization/concealment/masking; procedures/exposure; outcome definitions; follow-up; statistical methods/covariates; missing-data approach; software/threshold; protocol and registration; funding/conflicts, when requested.
4. Apply design-specific fields in `../research-data-extraction/references/study-design-rules.md`.
5. Attach precise locations and distinguish facts not stated in the supplied article from details found in separately supplied protocol/registry documents.

## Design safeguards

- Do not classify from title/abstract alone when the methods section is available.
- Do not call an observational association causal. Do not assume randomization, blinding, or prospective follow-up from a label alone.
- Do not treat a missing methods description as proof that a procedure did not occur.
- Do not infer design-specific information from common practice or external background knowledge.
- Qualitative, diagnostic, protocol-only, animal, laboratory, and modeling studies need appropriate fields; do not force a clinical-trial template.

## Useful output

| Methods field | Extracted information | Source location | Confidence | Notes |
|---|---|---|---|---|

For a requested compact result, report author label, supported classification, design-defining evidence, key methods, unresolved ambiguity, and source locations.
