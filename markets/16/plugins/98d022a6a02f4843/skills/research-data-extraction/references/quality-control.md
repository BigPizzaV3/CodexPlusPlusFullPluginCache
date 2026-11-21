# Quality-control checklist

Before replying, verify:

- Every requested field was addressed; intentionally omitted fields are marked `NOT_EXTRACTED` only when useful.
- Missing data is `NR`, true non-applicability is `NA`, and ambiguity/conflict is `UNCLEAR`; none was silently set to zero.
- Study design comes from methods evidence; author label and assistant classification remain distinct when they conflict.
- Enrollment and analyzed sample size, group totals, units, groups, baselines and follow-up are not conflated.
- Primary, secondary, exploratory, safety, and patient-reported outcomes remain distinct.
- Every outcome/timepoint/group/analysis population/adjustment stratum remains separate.
- Statistical measure, estimate, CI, p-value symbols, precision, denominator, adjustment covariates, and source are preserved.
- Tables retain row/column labels, footnotes, units and denominators; figures retain caption/axes/legend and uncertainty, and unlabeled values are not invented.
- Citations/identifiers are source-present or verified; no inferred DOI/PMID.
- Author interpretation/limitations are separated from assistant analysis.
- Calculated values are explicitly requested, reproducible, and labeled `CALCULATED_FROM_REPORTED_DATA`.
- Conflicts and possible duplicate reports are surfaced with evidence, not silently resolved.
- Bias-related comments describe source evidence and limits; unsupported formal judgments are withheld.
- Any external lookups are clearly labeled and cited separately from the supplied-source extraction.
