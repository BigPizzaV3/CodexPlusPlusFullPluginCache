# Normalized study extraction schema

Use only requested fields. If the user supplies a schema, preserve it exactly and flag incompatible requests instead of silently changing it. Use one study ID per independently reported study; companion reports may share a parent cohort identifier while retaining separate report IDs.

## Core record

```json
{
  "study_id": "string",
  "bibliographic_information": {
    "title": "string|NR", "authors": "array|NR", "journal": "string|NR",
    "publication_year": "integer|NR", "publication_date": "string|NR",
    "doi": "string|NR", "pmid": "string|NR", "pmcid": "string|NR",
    "trial_registration": "string|NR", "country": "array|NR",
    "funding_source": "string|NR", "conflict_of_interest": "string|NR"
  },
  "study_identification": {
    "study_type": "string|UNCLEAR", "study_design": "string|NR",
    "study_objective": "string|NR", "research_question": "string|NR",
    "hypothesis": "string|NR", "setting": "string|NR",
    "number_of_centers": "integer|NR", "recruitment_period": "string|NR",
    "follow_up_duration": "string|NR"
  },
  "population": {
    "target_population": "string|NR", "sample_size_total": "number|NR",
    "sample_size_analyzed": "number|NR", "number_of_groups": "number|NR",
    "group_sample_sizes": "object|NR", "age": {"reported_measure":"string|NR","value":"number|string|NR","dispersion":"string|NR","range":"string|NR"},
    "sex_or_gender": {"reported_categories":"object|NR"},
    "inclusion_criteria": "array|NR", "exclusion_criteria": "array|NR",
    "baseline_characteristics": "object|NR", "disease_or_condition": "string|NR",
    "disease_stage_or_severity": "string|NR", "comorbidities": "array|NR"
  },
  "intervention": {"groups": [{"group_name":"string","intervention_name":"string|NR","intervention_type":"string|NR","dose":"string|NR","frequency":"string|NR","route":"string|NR","duration":"string|NR","co_interventions":"array|NR"}]},
  "comparator": {"comparator_present":"boolean|UNCLEAR","comparator_name":"string|NR","comparator_type":"string|NR","description":"string|NR"},
  "outcomes": {"primary_outcomes": [], "secondary_outcomes": [], "exploratory_outcomes": [], "safety_outcomes": [], "patient_reported_outcomes": []},
  "results": [], "statistical_methods": {}, "bias_and_quality": {},
  "author_interpretation": {}, "assistant_notes": {}
}
```

## Outcome definition object

For each outcome retain its name, operational definition, measurement tool, unit, timepoint, and source location when reported. Do not collapse outcomes that use different definitions or instruments. Label primary/secondary/exploratory/safety/patient-reported status only when the source or protocol identifies it; otherwise use `UNCLEAR` and explain.

## Methods, bias evidence, interpretation, and notes

- `statistical_methods`: sample-size calculation; statistical tests; regression models; covariates; multiple-testing adjustment; missing-data method; software; significance threshold.
- `bias_and_quality`: randomization; allocation concealment; participant/personnel/outcome-assessor blinding; attrition; missing outcome data; selective-reporting information; protocol/registration availability. These are extraction fields, not automatic judgments.
- `author_interpretation`: author conclusion; author-reported limitations; future-research recommendations.
- `assistant_notes`: extraction uncertainties; conflicting values; possible reporting errors; fields requiring manual review.

If a user explicitly requests a formal risk-of-bias judgment under a named, current, appropriate instrument and provides enough evidence, structure each assessment as: `domain`, `source_evidence`, `source_location`, `judgment` (`low`, `some_concerns`, `high`, or `unclear` where that instrument uses these labels), `confidence` (`high`, `medium`, `low`), and `reason`. Otherwise return evidence only and mark judgment `UNCLEAR`; do not mix judgment categories across tools.

## Result row

Each row represents one outcome × timepoint × group/contrast × analysis population × adjustment status. Include `outcome`, `timepoint`, `group`, `n_analyzed`, `result_type`, `estimate`, `unit`, `standard_deviation`, `standard_error`, `confidence_interval`, `p_value`, `event_count`, `total_count`, `effect_measure`, `effect_size`, `adjusted`, `adjustment_variables`, `analysis_population`, and `source_location` when available. Use separate rows for ITT/per-protocol, adjusted/unadjusted, subgroup/overall, and each distinct follow-up.

## PICO / PICOS / PECO

- **P — Population:** condition, participant characteristics, age, sex/gender as reported, setting, sample size, and eligibility.
- **I/E — Intervention or Exposure:** name/type, dose or level, frequency, duration, route/protocol, or measured exposure.
- **C — Comparator:** placebo, usual care, active comparator, no intervention, historical comparator, unexposed group, or `NR`/`NA`/`UNCLEAR` as appropriate.
- **O — Outcomes:** primary/secondary outcomes, measurement method, and timepoint.
- **S — Study design:** design label supported by methods.

Do not force a PICO comparator into single-arm or qualitative research. Mark absent elements `NA` only when truly inapplicable; otherwise `NR` or `UNCLEAR`.

## Missingness and provenance

- `NR`: searched the available source but the information is not reported.
- `NA`: the field genuinely does not apply to this design/question.
- `UNCLEAR`: information may be present but is ambiguous, illegible, or conflicting.
- `NOT_EXTRACTED`: deliberately outside the user's selected scope.
- Attach a source location and confidence to critical values: `HIGH` explicitly stated; `MEDIUM` requires minor interpretation; `LOW` ambiguous or interpretation-dependent. Confidence is about extraction support, not study quality.
