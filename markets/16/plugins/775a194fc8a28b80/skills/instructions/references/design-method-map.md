# Design-specific appraisal: what each checklist can and cannot say

A **reporting guideline** checks transparency/completeness, **risk-of-bias tool** evaluates credibility of a result, **certainty framework** evaluates confidence in a body of evidence, and **critical appraisal checklist** guides questions. They are not interchangeable; don't produce one numerical “quality score” from all of them.

| Research type | Reporting reference | Appraisal/risk-of-bias focus |
|---|---|---|
| Randomized intervention trial | CONSORT 2025 and relevant extension; protocol/registration | RoB 2 per outcome; random sequence/concealment, deviations, missing data, outcome measurement, selective reporting |
| Nonrandomized intervention | STROBE as appropriate, RECORD where applicable | ROBINS-I where fit; confounding and time-zero, selection, immortal-time bias, interventions/estimands |
| Cohort/case-control/cross-sectional | STROBE or applicable extension | Selection, confounding, time order, measurement, missingness; JBI/NOS selectively with rationale, avoid crude totals |
| Diagnostic accuracy | STARD 2015 (verify if updated) | QUADAS-3 (2026) risk of bias/applicability; patient spectrum, index test, target condition/reference standard, analysis; sensitivity/specificity & CI |
| Prognostic/diagnostic prediction model | TRIPOD+AI 2024 and relevant extensions | PROBAST / PROBAST+AI where appropriate; discrimination, calibration, missingness, external validation, leakage |
| Systematic review/meta-analysis | PRISMA 2020 + domain extensions | AMSTAR 2 review-method confidence; RoB for primary studies; GRADE certainty for relevant outcome and question |
| Network meta-analysis | PRISMA-NMA and relevant updates | Transitivity, coherence, connected network, heterogeneity, inconsistency, rankings with uncertainty, CINeMA/GRADE as appropriate |
| Guideline | RIGHT for reporting | AGREE II for guideline rigor; GRADE Evidence-to-Decision for recommendations if relevant |
| Qualitative research | COREQ / SRQR where appropriate | Recruitment, saturation/information power, reflexivity, credibility, analytic transparency |
| AI/LLM study | Depending on task: TRIPOD+AI, TRIPOD-LLM (2025), CLAIM and appropriate design checklist | Dataset shift/leakage, external validation, representative cohorts, uncertainty, fairness, reproducibility, clinical evaluation |

## Important distinctions
- CONSORT 2025 is a trial *reporting* standard; it does not itself replace RoB 2.
- PRISMA 2020 is a systematic review *reporting* standard; it is not a substitute for AMSTAR 2/GRADE.
- QUADAS-3 appeared in 2026. Do not automatically label older QUADAS-2 assessments fraudulent; evaluate their date and context.
- GRADE is generally for outcome-specific bodies of evidence, not a universal one-paper score.
- A preprint, personal review, technical note, clinical opinion, guideline and original empirical study need different expectations.
- An RCT's internal validity is not the same as its real-world applicability. Appraise both.
- Distinguish primary/secondary outcome, prespecified/post hoc comparisons, per protocol vs intention to treat, association vs causation.
- When unable to view protocol/supplement, label judgments provisional; avoid claiming exact completion of complex tools without domain signalling answers.

## Authoritative entry points (links for verification, not reproduced checklists)
- EQUATOR reporting guideline registry: https://www.equator-network.org/
- CONSORT 2025 statement (PubMed): https://pubmed.ncbi.nlm.nih.gov/40245901/
- PRISMA 2020 official: https://www.prisma-statement.org/prisma-2020
- Cochrane RoB 2: https://methods.cochrane.org/bias/resources/rob-2-revised-cochrane-risk-bias-tool-randomized-trials
- Cochrane Handbook: https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current
- QUADAS-3 (2026): https://doi.org/10.7326/ANNALS-25-02104
- TRIPOD-LLM (2025): https://doi.org/10.1038/s41591-024-03425-5
- GRADE official: https://www.gradeworkinggroup.org/
- AGREE II: https://www.agreetrust.org/

For any “current guideline” claim, verify the current release; this is a method map as of 2026-10, not proof that no later update exists.
