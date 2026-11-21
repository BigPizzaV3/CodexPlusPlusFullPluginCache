# Bias-related evidence and quality support

This plugin helps extract evidence and organize questions; it is not a substitute for a protocol, trained reviewer, or official instrument. Do not issue a final overall risk-of-bias or certainty-of-evidence grade by default. If the user explicitly requests a judgment, first identify the design, exact outcome/result, chosen instrument/version, protocol rules, and adequate source evidence; otherwise return a domain-evidence table and mark judgment `UNCLEAR`.

## Evidence-first record

For every possible domain, provide: domain/question; exact paper evidence or concise faithful paraphrase; source location; what the source does not report; extraction confidence (`HIGH`/`MEDIUM`/`LOW`); and provisional judgment only if explicitly requested and supported. Keep source evidence separate from assistant interpretation. Do not present a reporting omission itself as proof of a specific bias mechanism.

## Common domains to look for

- RCT result-level evidence: randomization process; deviations from intended interventions; missing outcome data; outcome measurement; selection of reported result. RoB 2 assessments concern a particular result, not a single undifferentiated study label.
- Non-randomized intervention evidence: confounding; participant selection; intervention classification; deviations; missing data; outcome measurement; selective reporting. ROBINS-I has versioned guidance; verify the current version before applying it.
- Observational exposure, diagnostic, prognostic, qualitative, animal, and laboratory work: instrument/domain choices differ. Do not map them automatically to RCT domains. Ask for the review's chosen instrument or report source evidence without assigning formal scores.

## Cautious flags (not automatic verdicts)

Flag only with precise source support: unclear randomization/concealment or masking; attrition/missing outcomes; outcome-definition ambiguity; no comparator; very small sample; short follow-up; multiple testing without stated adjustment; selective subgroup reporting; missing protocol/registration; funding/conflict declarations; inconsistent sample sizes or outcomes. Explain why each is a question for human review rather than a conclusion.

## Method references

- Cochrane Handbook Chapter 8 describes RoB 2 as result-specific and domain-based: https://training.cochrane.org/handbook/current/chapter-08
- ROBINS-I resources and version notices: https://www.riskofbias.info/welcome/home
- PRISMA 2020 is a reporting guideline for systematic-review reporting, not a risk-of-bias instrument: https://www.prisma-statement.org/prisma-2020
- Diagnostic study reporting context (STARD explanation/elaboration): https://doi.org/10.1136/bmjopen-2016-012799

These references are starting points, not exhaustive or universally applicable. Use the exact current instrument selected by the user's protocol; do not reproduce proprietary or licensed tools wholesale.
