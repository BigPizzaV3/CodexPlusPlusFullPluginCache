# Study design and methods extraction

## Classification priority

Determine design from explicit methods, not title wording alone. Inspect in this order: Methods section, design subsection, cited protocol, abstract methods, title. If evidence does not support a defensible label, output `UNCLEAR` and say what is missing. Preserve the authors' label separately from assistant classification if they differ.

## Supported design families

Randomized controlled trial; non-randomized controlled trial; prospective or retrospective cohort; case-control; cross-sectional; case series; case report; diagnostic accuracy; prognostic; qualitative; mixed methods; systematic review; meta-analysis; scoping review; narrative review; laboratory; animal; in-vitro; survey; economic evaluation; modeling study; protocol; preprint; other. These are routing labels, not an exhaustive ontology; preserve the source wording and clarify mixed/ambiguous designs.

## Design families and fields

- Randomized / non-randomized intervention: allocation unit, sequence/randomization, concealment, arms, masking, intended intervention, adherence/deviations, outcomes, analysis population, and follow-up.
- Cohort: prospective/retrospective direction, eligibility and sampling, exposure, comparator, outcome ascertainment, follow-up, attrition, and confounding adjustment.
- Case-control: case/control definitions, source population, selection, exposure ascertainment, matching, and adjusted analyses.
- Cross-sectional/survey: sampling frame, recruitment, response rate when reported, measures, timing, weighting, and analysis.
- Case report/series: case count, inclusion basis, intervention/exposure, outcome and follow-up; do not imply a comparator or causal inference.
- Diagnostic accuracy: intended use/role, index test, reference standard, threshold, participant spectrum, blinding, flow, and accuracy measures when reported.
- Prognostic: population/time origin, predictors, outcome, follow-up, model development/validation, calibration/discrimination, and handling of missingness when reported.
- Systematic/scoping/narrative review or meta-analysis: review question, sources/search date, eligibility, screening, extraction, synthesis method, included-study count, and protocol/registration as reported.
- Qualitative/mixed methods: approach, sampling, context, data collection, analytic method, reflexivity/trustworthiness, integration for mixed methods, and theme/quote provenance.
- Laboratory, animal, in-vitro, economic, modeling, protocol, or other: extract the stated unit, conditions, model/specimen, comparator, assumptions, endpoints, and validation details. Do not force human-participant fields onto non-human designs.

## Methods fields

When requested, extract objective/research question/hypothesis, country/setting/centers, recruitment period, sample-size calculation, inclusion/exclusion criteria, sampling, randomization/concealment/blinding, interventions and co-interventions, measures, follow-up, data collection, statistical tests/models/covariates, multiple-testing adjustment, missing-data handling, software, significance threshold, protocol/registration, funding, and declared conflicts. Record `NR` rather than importing a protocol detail that the supplied article does not report.

## PICO compatibility

Use PICO/PICOS for suitable intervention questions, PECO for exposure questions, and a question-appropriate structure for descriptive, qualitative, diagnostic, or review designs. Leave genuinely inapplicable elements `NA`; never invent a comparator to complete a template.
