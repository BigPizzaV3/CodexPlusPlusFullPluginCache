# Important EduInsights marts

## Contents

- [Discover before selecting](#discover-before-selecting)
- [Start with these marts](#start-with-these-marts)
- [Choose point-in-time or history deliberately](#choose-point-in-time-or-history-deliberately)
- [Use these specialist families when the headline mart is too broad](#use-these-specialist-families-when-the-headline-mart-is-too-broad)
- [Fast routing examples](#fast-routing-examples)

## Discover before selecting

This is a curated map, not the complete deployed inventory. Mart availability, fields, and releases follow the serving snapshot.

For every current-data question:

1. Call `edu_describe_data` without a topic.
2. Read its routing guidance and `semantic_views`.
3. Choose the smallest suitable `marts.*` relation.
4. Inspect it with `topic: table:marts.<relation>` before writing SQL or describing its fields.

The overview can highlight only common starting views even when more marts are deployed. A direct table description decides whether a curated relation is available. Do not query `marts.semantic_catalog` directly.

## Start with these marts

| Mart | What one row represents | Start here for | Main boundary |
|---|---|---|---|
| `marts.institution` | One college or campus by UnitID | Identity, current headline characteristics, cost, broad outcomes, Carnegie context, and institutional accreditation | Current convenience view. Use historical institution snapshots for past facts. OPEID-family values are attributes, not campus totals to sum. |
| `marts.program_award_cell` | One college × CIP-6 × award level × reporting year | Reported degrees plus attached broader-field outcomes | Positive completions show reporting activity, not a current named program. Scorecard earnings and debt are inherited from CIP-4 and repeat across CIP-6 children. |
| `marts.field` | One CIP-6 field | National reported degrees, college counts, and structural career context | Career measures are crosswalk-weighted preparation context, not observed graduate destinations. |
| `marts.field_award_benchmark` | One CIP-6 × Scorecard credential level | National earnings and debt benchmarks with cohort-aware weighting | Underlying outcomes are CIP-4 field cohorts. Use this mart instead of averaging or summing program medians. |
| `marts.occupation` | One SOC-6 occupation | Headline employment, wages, outlook, preparation, and observed AI-use measures | Sources have different releases and populations. AI use and employment projections remain separate observations. |
| `marts.occupation_task` | One SOC-6 × O*NET task | What a career involves and which tasks show observed Claude use | Task penetration is product-specific behavior, not universal capability or automation potential. |
| `marts.field_occupation_edge` | One CIP-6 × SOC-6 relationship | Careers a field can prepare someone for | Structural relationship only. It is not placement, probability, demand, or observed flow. |
| `marts.institution_enrollment` | One college × reporting year × enrollment facet | Current enrollment totals and demographic composition | Facets overlap. Filter to one facet before summing colleges; facet `1` is all students. |
| `marts.program_accreditation` | One college × accreditor × programmatic grant | Specialized accreditation for programs | DAPIP is dated. The CIP-family anchor is an EduInsights mapping with confidence, not a publisher code. |
| `marts.pseo_program_outcome` | One normalized PSEO outcome row at the publisher's cohort grain | Earnings and industry-flow outcomes from one normalized surface | Filter `outcome_family`. Preserve OPEID, degree, CIP level, cohort, geography, horizon, participation, and suppression. |
| `marts.detailed_occupation_ai_use` | One product channel × O*NET-SOC specialization × period | Latest detailed occupation AI-use facets | Keep Claude.ai and API channels separate. Do not collapse specializations without a declared weighting method. |
| `marts.macro_ai_signal` | One year × indicator × series | National or macro AI context | It has no college, CIP, or SOC key. Cite it as context; never join it to an entity. |

## Choose point-in-time or history deliberately

### Reported degrees

- `marts.program_award_cell`: convenient headline surface combining direct IPEDS completions with broader Scorecard context.
- `marts.program_award_cell_longitudinal`: native completion history with collection cycle, reference period, release, coverage, publication snapshot, and row provenance.
- `marts.program_award_cell_latest_final`: newest accepted final or revised completion cell for a point-in-time answer.
- `marts.program_award_cell_harmonized`: CIP-harmonized history with native and target codes, mapping weights, ambiguity, and crosswalk release.
- `marts.program_award_cell_unharmonized`: diagnostic native cells that lack a target-vintage mapping.

Use native history by default. Use harmonized history only when the question requires comparable fields across CIP vintages. State the mapping and retained residuals.

### Enrollment

- `marts.institution_enrollment`: convenient current enrollment facets.
- `marts.institution_enrollment_longitudinal`: history joined to contemporaneous college attributes and full release context.
- `marts.institution_enrollment_latest_final`: newest final or revised point for each college and facet.
- `marts.institution_enrollment_provisional_context`: newer provisional evidence kept separate for release audits.

Use one facet per aggregation. Historical rows already contain contemporaneous college identity; do not overwrite it with today's roster.

### Curated IPEDS measures

- `marts.ipeds_measure_longitudinal`: definition-backed aid, finance, price, and outcome measures by college and cycle.
- `marts.ipeds_constant_dollar_series`: nominal and constant-dollar values with price-index release and base cycle.
- `marts.ipeds_measure_comparability`: direct, mapped, or break assessments between releases.
- `marts.ipeds_component_coverage`: accepted release or explicit coverage state for each expected component and cycle.
- `marts.ipeds_canonical_source_release`: the selected release for each component and cycle.
- `marts.ipeds_source_release`: accepted append-only IPEDS release records.
- `marts.ipeds_publication_snapshot`: the release-selection set behind the current serving build.

Do not call a file latest because its date looks newest. Follow the canonical release selector and preserve the release stage.

## Use these specialist families when the headline mart is too broad

### Distance education and completion demographics

| Need | Mart family | Boundary |
|---|---|---|
| Student participation in distance education | `marts.ipeds_distance_enrollment_longitudinal` and `marts.ipeds_distance_enrollment_latest_final` | Student level and metric are part of the row identity. Exclusive, some, and no-distance categories can overlap under source definitions. |
| College distance-course or distance-program offering flags | `marts.ipeds_distance_offering_longitudinal` and `marts.ipeds_distance_offering_latest_final` | College-level offering context is not current named-program modality. |
| Field and award-level distance availability | `marts.ipeds_distance_program_longitudinal` and `marts.ipeds_distance_program_latest_final` | Direct for the published field and award cell, not a catalog program. Preserve native CIP vintage. |
| Completion demographics | `marts.ipeds_completion_demographic_longitudinal` and `marts.ipeds_completion_demographic_latest_final` | These rows have college-total or award-level scope without a CIP key. They are not program demographics. |

### Graduate outcomes and education-to-work context

| Need | Mart | Boundary |
|---|---|---|
| PSEO earnings | `marts.pseo_earnings_evidence` | Published institution or aggregate, degree, CIP level, cohort, place, and horizon remain part of the meaning. |
| PSEO graduate industry flows | `marts.pseo_industry_flow_evidence` | Observed industry flow for participating cohorts. Industry is not occupation. |
| PSEO participation | `marts.pseo_institution_participation` | Determine participation from the lookup and release metadata, not the presence of an outcome row. |
| North Carolina cohort outcomes | `marts.nc_tower_program_outcome` | Campus and program identifiers are still publisher-native. Suppressed `-1` is never zero. |
| Population degree-to-career context | `marts.acs_degree_occupation_context` | Weighted population context, never a named-college or named-program outcome. |
| Graduate field and job alignment | `marts.nscg_degree_occupation_alignment` | Publisher classifications remain native unless an explicit bridge exists. |
| National bachelor's cohort context | `marts.nces_bandb_national_cohort_context` | Published national aggregates have no college, CIP, or SOC key. |

### Careers, pay, requirements, and regional context

| Need | Mart | Boundary |
|---|---|---|
| Wages and employment by place | `marts.oews_area_occupation` | Place type is part of the key. Suppression and wage top-coding stay measure-specific. |
| Every published OEWS package | `marts.oews_all_published_observations` | Packages overlap and are not additive. Retain package and row provenance. |
| State career outlook | `marts.state_occupation_projection` | States publish different base and projected periods. Preserve the source SOC vintage and bridge. |
| Job requirements | `marts.occupation_requirement` | ORS releases are independent survey waves, not automatically a time series. |
| Regional industry employment | `marts.qcew_regional_industry_context` | Industry and establishment context is not occupation demand or graduate outcomes. |
| Regional workforce flows | `marts.qwi_recent_workforce_context` | Employer and worker flows are industry context, not named-program outcomes. |

### Observed AI use

| Need | Mart | Boundary |
|---|---|---|
| Latest Anthropic detailed occupation facets | `marts.detailed_occupation_ai_use` | Product channel and O*NET specialization stay separate. |
| Anthropic occupation history | `marts.aei_detailed_occupation_history` | Release, channel, specialization, and month are key dimensions. |
| Anthropic task history | `marts.aei_task_history` | Older text-based observations can map to several occupation-specific tasks. Inspect match method and cardinality. |
| Anthropic conversation clusters | `marts.aei_conversation_cluster_history` | Privacy-bucketed prevalence is not individual or population-wide use. |
| Microsoft Bing Copilot occupation measures | `marts.microsoft_occupation_ai_use` | A second product-specific calibration, not universal AI use or replacement risk. |

When more than one AI-use source applies, present them as separate observed populations before comparing their measures.

## Fast routing examples

| Question | First mart | Why |
|---|---|---|
| What did this college report in computer science? | `marts.program_award_cell` | The question names a college, CIP-6 field, and reported degree activity. |
| How have bachelor's completions changed since 2018? | `marts.program_award_cell_longitudinal` | The question requires cycle and release-aware history. |
| What do graduates in this broader field earn? | `marts.field_award_benchmark` or a PSEO mart | The correct choice depends on the requested population, cohort, and geography. |
| Which careers relate to this field? | `marts.field_occupation_edge` | The question asks for the structural preparation relationship. |
| What does this career pay and how is it projected to change? | `marts.occupation` | The headline occupation view carries national wages and outlook with separate releases. |
| What parts of this career show AI use? | `marts.occupation_task` | The question is at task level. |
| Where do graduates work? | `marts.pseo_industry_flow_evidence` | PSEO observes industry flows for participating cohorts. |
| Is this named program offered online now? | No serving mart is sufficient | Current catalog and modality evidence is required. IPEDS field availability is not a named catalog program. |
