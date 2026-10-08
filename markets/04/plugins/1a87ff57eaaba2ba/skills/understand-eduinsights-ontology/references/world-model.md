# The EduInsights world model

## Contents

- [The world in one sentence](#the-world-in-one-sentence)
- [Model facts before conclusions](#model-facts-before-conclusions)
- [The entity spine](#the-entity-spine)
- [Identifier rules](#identifier-rules)
- [Relationship meanings](#relationship-meanings)
- [Native level of detail](#native-level-of-detail)
- [Applicability](#applicability)
- [Coverage](#coverage)
- [Time and releases](#time-and-releases)
- [Storage layers](#storage-layers)
- [Map common questions to the graph](#map-common-questions-to-the-graph)

## The world in one sentence

EduInsights connects colleges to reported awards and catalog records; fields to careers; careers to tasks and skills; and each entity to separately published outcomes, pay, outlook, accreditation, industry, place, and observed AI use. Every connection retains its source, release, native level of detail, applicability, and coverage.

## Model facts before conclusions

An `Observation` is one source row and measure attached to the entity the publisher actually measured. An `EvidenceClaim` is a conclusion supported by observations. It keeps their distinct levels of detail instead of flattening them into one program fact.

The graph therefore separates three things:

1. **Entities:** the colleges, fields, careers, tasks, industries, and places being described.
2. **Observations:** what a named source reported for one entity, population, period, and measure.
3. **Relationships:** the direct, inherited, structural, or empirical path that makes an observation relevant to a question.

## The entity spine

### Colleges and identity

| Entity | Identity | Meaning |
|---|---|---|
| `Institution` | UnitID | A college or campus in the IPEDS identity system. |
| `InstitutionSnapshot` | UnitID × collection cycle × source release | The college's attributes at one historical point. Use it for historical facts. |
| `InstitutionContinuity` | From UnitID × to UnitID × effective period | An explicit merger, split, or successor link. Names alone never prove continuity. |
| `InstitutionMembership` | Parent UnitID × member UnitID × effective period | A time-bounded system or campus-family relationship. Membership is not identity. |
| `FederalAidEntity` | OPEID | A federal-aid entity or branch. One OPEID can cover several IPEDS campuses. |
| `ScoringCohort` | Cohort version | A reproducible internal set of colleges selected for one research or evaluation run. |

Keep UnitID and OPEID distinct. UnitID identifies an IPEDS institution. OPEID identifies a federal-aid entity or branch. Their bridge can be one-to-many.

### Programs and fields

| Entity | Identity | Meaning |
|---|---|---|
| `ProgramAwardCell` | UnitID × CIP version × CIP-6 × award level × cycle × release | Degrees a college reported in one field and award level. Positive completions establish reporting activity, not current catalog status. |
| `CatalogProgram` | UnitID × catalog year × source-stable program ID | A named program in an official catalog for a stated year, with source locators. |
| `ProgramFieldGroup` | Institution or OPEID × CIP level × credential or cohort × release | A broader source-published field group, such as a CIP-4 Scorecard cohort or PSEO cohort. |
| `CIPField` | CIP version × level × code | A versioned instructional field at CIP-2, CIP-4, or CIP-6. |

These entities answer different questions. A reported award cell cannot establish that a named program accepts students today. A catalog name does not map to one reported award cell without explicit resolution. A broader field outcome can inform a narrower question only with inherited applicability.

### Work, skills, industry, and place

| Entity | Identity | Meaning |
|---|---|---|
| `Occupation` | SOC version × SOC-6 | A detailed occupation used for comparison, pay, and outlook. |
| `DetailedOccupation` | O*NET version × O*NET-SOC | An O*NET specialization. Several specializations may roll into one SOC-6 occupation. |
| `Task` | Taxonomy × version × task ID | One source-defined part of a job. Tasks may belong to several detailed occupations. |
| `Skill` | Framework × version × skill ID | A skill in a named framework. Mappings retain their method and confidence. |
| `Industry` | NAICS version × code | What an employer produces. It is not the job a worker performs. |
| `Geography` | Publisher place type × code | A national, state, metro, county, or other publisher-defined place. |
| `PublisherClassification` | Publisher × classification system × version × code | A source-native category that is not silently recast as CIP or SOC. |

Keep SOC and O*NET-SOC distinct. Preserve O*NET specialization suffixes. Use an explicit bridge to roll specializations into SOC.

### Sources, time, and interpretation

| Entity | Meaning |
|---|---|
| `SourceRelease` | One accepted publisher component or release with collection cycle, stage, and publication date. |
| `PublicationSnapshot` | One immutable selected set of source releases used to reproduce a serving build. |
| `MeasureDefinition` | A versioned measure name, unit, population, method, and definition. |
| `ComparabilityAssessment` | Whether a measure is directly comparable, mapped, or broken across releases. |
| `CoverageAssessment` | Whether a component and cycle were collected and why a value may not be observed. |
| `Observation` | One publisher row and measure at the publisher's native level of detail. |
| `EvidenceClaim` | A versioned conclusion linked to its supporting observations. |
| `Accreditor` | A DAPIP institutional or programmatic accrediting agency. |
| `ConversationCluster` | A privacy-bucketed Anthropic conversation cluster at the publisher's hierarchy. |

## Identifier rules

| Identifier | Owner | Rule |
|---|---|---|
| UnitID | NCES IPEDS | Prefer the publisher identifier over name matching. Use a contemporaneous `InstitutionSnapshot` for historical facts. |
| OPEID | U.S. Department of Education | Preserve it as text, including leading zeros and branch suffixes. OPEID-to-UnitID resolution can be one-to-many. |
| CIP | NCES | Retain the taxonomy version and level. CIP-2, CIP-4, and CIP-6 are distinct levels of detail. |
| SOC | BLS | Retain the taxonomy version and hierarchy level. Use SOC-6 for detailed career comparisons. |
| O*NET-SOC | O*NET Resource Center | Preserve the specialization suffix and O*NET version. Resolve to SOC through an explicit versioned bridge. |
| NAICS | Census and OMB | Retain the version and code level. An industry code never substitutes for an occupation. |
| Geography code | Publisher-specific | Retain the place type with the code. National, state, metro, county, and other observations are not interchangeable. |

Never guess a canonical identifier from a name. Resolve names first and keep the readable label beside any identifier shown to a person.

## Relationship meanings

| Relationship | Safe meaning | Boundary |
|---|---|---|
| `cohort_includes_institution` | A versioned research or evaluation cohort contains a college. | Cohort membership is a reproducible selection, not a college attribute. |
| `publication_snapshot_selects_release` | A serving snapshot selects a versioned set of accepted source releases. | The snapshot version is not itself a measure release or reporting year. |
| `institution_has_snapshot` | A college has dated attributes for each collection cycle and release. | Current attributes do not overwrite historical facts. |
| `observation_uses_measure_definition` | A source observation uses one versioned measure definition. | Matching field names do not prove matching populations, units, or methods. |
| `institution_reported_award_cell` | A college reported degrees in that field, award level, cycle, and release. | It does not prove current catalog availability. |
| `award_cell_classified_as` | A reported award cell uses a specific CIP-6 field. | A CIP label is not necessarily the catalog program name. |
| `catalog_program_maps_to_award_cell` | A catalog program resolves to one or more reported award cells through evidence and confidence. | The mapping may be many-to-many. |
| `field_group_context_applies_to_award_cell` | A broader source-published field group informs a narrower award cell. | Present it as inherited context, not a direct program outcome. |
| `cip_prepares_for_occupation` | A versioned crosswalk says a field can prepare someone for a career. | It is not observed placement, probability, demand, or causation. |
| `detailed_occupation_specializes_occupation` | An O*NET specialization rolls into a SOC occupation through an explicit bridge. | Suffix stripping is not a valid bridge. |
| `occupation_has_task` | O*NET links a detailed occupation to a task. | A task can occur in several occupations. |
| `occupation_requires_skill` | A source or framework links a career to a skill. | Preserve the rating scale, framework, and release. |
| `program_teaches_skill` | Catalog or curriculum evidence supports a program-to-skill link. | The link requires direct evidence; a CIP label alone is insufficient. |
| `graduate_employment_flows_to_industry` | PSEO observed graduates working in an industry for participating cohorts. | Industry is not occupation, and participation and suppression limit coverage. |
| `institution_accredited_by` | DAPIP reports institutional accreditation for a dated grant. | DAPIP is a dated snapshot, not real-time status. |
| `program_is_accredited_by` | DAPIP reports programmatic accreditation linked to a college. | The CIP-family anchor is an EduInsights mapping with confidence. |
| `cluster_maps_to_task` | An Anthropic cluster maps to one or more O*NET tasks. | Bucketed prevalence is not individual or universal AI use. |
| `publisher_classification_maps_to_field` | A versioned bridge maps a source-native classification to CIP. | No bridge means the publisher code stays native. |
| `publisher_classification_maps_to_occupation` | A versioned bridge maps a source-native classification to SOC. | Similar labels never substitute for a bridge. |
| `observation_describes_entity` | A publisher observation describes an entity at its native level of detail. | The entity link does not make a broader observation more specific. |
| `claim_supported_by_observation` | A conclusion links to one or more inspectable observations. | Combined observations retain their separate populations, periods, and applicability. |

## Native level of detail

The native level of detail answers: what does one publisher row represent?

Examples:

- IPEDS completions: one college × native CIP-6 × award level × cycle × release.
- Scorecard field outcomes: one college × CIP-4 × credential cohort × pooled period.
- PSEO outcomes: one OPEID or aggregate × degree level × CIP level × cohort × geography × horizon.
- OEWS: one release × publisher package × place × industry × occupation × measure.
- O*NET task ratings: one release × detailed occupation × task × scale × category.
- Anthropic AI use: one release × product channel × occupation or task × period × publisher facet.

Joining a broader observation to a narrower entity does not change what the source measured. A repeated CIP-4 earnings value remains one broader field observation even when it appears beside several CIP-6 award cells.

## Applicability

Applicability describes how closely an observation fits the question.

| Value | Meaning |
|---|---|
| `direct` | The observation matches the entity and level asked about. |
| `inherited_from_cip4` | A CIP-4 field observation informs a narrower CIP-6 question. |
| `inherited_from_cip2` | A CIP-2 field observation informs a narrower field question. |
| `institution_fallback` | College-level context is used when no program-level measure exists. |
| `structural_prior` | A taxonomy or crosswalk says entities may relate. It is not an observed outcome. |
| `empirical_calibration` | Observed behavior in a bounded population informs a broader concept. |
| `narrative_context` | A macro or methodological observation frames the question without becoming an entity-level input. |

When Claude or Bing Copilot observations are the strongest relevant AI-use data, lead with what they show. Name the product, population, channel, period, and release. Do not turn usage into an employment, wage, productivity, capability, or displacement claim.

## Coverage

Coverage explains whether a value exists and why.

| State | Meaning |
|---|---|
| `observed` | The source reports a value. Numeric zero is valid here. |
| `suppressed` | The source or an explicit serving policy hides a small or protected cell. |
| `not_collected` | The source does not collect this measure or period. |
| `not_applicable` | The measure does not apply to this entity or population. |
| `not_participating` | The college, system, state, or cohort does not participate. |
| `stale_source` | The available release is older than the required decision period. |
| `unresolved_identifier` | A source identifier could not be resolved through a trusted bridge. |

A blank always keeps its reason. An absent row does not automatically establish any coverage state.

## Time and releases

Keep these concepts separate:

- **Collection cycle:** when a reporting component belongs in the publisher's system.
- **Reference period:** the period the measure describes.
- **Publication date:** when the publisher released the file.
- **Release stage:** provisional, final, revised, or late-revised status.
- **Publication snapshot:** the selected release set used for a serving build.

For IPEDS, canonical selection prefers late-revised, revised, then final. It uses provisional only when no final-family release exists for that component and cycle. Preserve the release stage whenever the canonical row may be provisional.

One comparable point describes a state. Two points show change. Three points can support a trend. Five consistently directed points can support a sustained trend. Stop arithmetic at a comparability break.

## Storage layers

| Layer | Purpose |
|---|---|
| `raw` | Source-faithful files, rows, sentinels, hashes, and ingestion records. |
| `ref` | Releases, taxonomies, dictionaries, labels, measure definitions, and version bridges. |
| `core` | Typed source entities and observations at native level of detail. |
| `bridge` | Explicit many-to-many mappings and identifier resolution with method and confidence. |
| `marts` | Question-oriented views that preserve identity, source, applicability, and coverage. |

A mart is a serving convenience. It does not authorize collapsing populations or turning a structural relationship into an observed outcome.

## Map common questions to the graph

| Person's question | Entity path | What the graph can establish |
|---|---|---|
| Does this college offer this program now? | `Institution` → `CatalogProgram` | Current catalog evidence is required. Reported awards alone answer only historical reporting. |
| How many degrees did this college report? | `Institution` → `ProgramAwardCell` → `CIPField` | Direct IPEDS completions for the named cycle and release. |
| What did graduates in this field earn? | `ProgramFieldGroup` outcome | Scorecard or PSEO at its published field, credential, cohort, and place. It may be broader than CIP-6. |
| Which careers can this field prepare someone for? | `CIPField` → `Occupation` | A structural preparation map from CIP-SOC. |
| Where did graduates work? | `ProgramFieldGroup` → `Industry` | PSEO industry flows for participating cohorts. It does not identify occupations. |
| What does this career involve? | `Occupation` → `DetailedOccupation` → `Task` or `Skill` | O*NET content and source-defined ratings. |
| How is AI used in this career? | `Occupation` or `DetailedOccupation` → AI-use observations → `Task` | Observed product-specific behavior with the named population and period. |
| Is AI causing jobs to grow or shrink? | AI-use observation plus employment outcome study | Current usage and projection sources cannot establish that causal link. |
