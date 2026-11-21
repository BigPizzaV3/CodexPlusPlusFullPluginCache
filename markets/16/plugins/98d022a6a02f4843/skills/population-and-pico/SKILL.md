---
name: population-and-pico
description: Extract study populations, participant characteristics, eligibility, baselines, interventions, comparators, and PICO/PICOS/PECO elements from scientific sources. Use for population or treatment/exposure question extraction.
---

# Population and question structure

Use the supplied source and the normalized definitions in `../research-data-extraction/references/extraction-schema.md`. Follow `research-data-extraction` for provenance and missingness.

## Population

- Extract target/source population, setting, recruitment, inclusion/exclusion criteria, enrolled N, analyzed N, number of groups, and group Ns as separate fields.
- For age, preserve reported summary type (mean/median), value, dispersion and range. For sex/gender retain the source's category labels/counts; do not infer identity categories or collapse them.
- Capture baseline characteristics, condition/stage/severity, comorbidities, subgroup definitions, and eligibility exactly as available.
- Keep screening, randomized/enrolled, treated, and analyzed numbers separate when the paper reports them. Reconcile totals only as a flagged check, not by changing source values.

## Intervention, exposure, and comparator

For each arm/exposure group retain group name, intervention/exposure name/type, dose or level, frequency, route, duration, procedures, co-interventions, and relevant control conditions. Extract comparator presence/name/type/description only from evidence. For no-comparator studies, use `NA` only where appropriate; otherwise `NR`/`UNCLEAR`.

## PICO, PICOS, PECO

- Use PICO/PICOS for intervention questions; use PECO when the principal contrast is an exposure.
- P: population, characteristics, setting, N, eligibility.
- I/E: intervention/exposure details.
- C: comparator/unexposed condition, if one exists.
- O: primary/secondary outcomes, method, and timepoint.
- S: source-supported study design.
- Do not force all letters into qualitative, descriptive, case, or single-arm research. Label truly inapplicable components `NA`; missing source details are `NR`.

## Output check

Make each group and its denominator identifiable. Preserve original labels and source locations; do not carry a value across papers or assume subgroup values represent the full population.
