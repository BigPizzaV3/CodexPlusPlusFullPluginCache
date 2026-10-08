# BAZI method pack

This procedure-only reference is generated from reviewed OMDS school profiles and method cards. Returned canonical facts remain authoritative; source notes do not supply missing facts or interpretations.

# Runtime-selectable profiles

Select exactly one section from the reading contract. `bazi.school.strength-balancing.v1` is the default only when no supported override is explicit: it is the one Bazi school whose method card the current manifest activates, which is an activation-state fact and not a resolution of the unresolved `bazi.dispute.useful-god-concepts`. An explicit `bazi.school.ziping-structure.v1` or `bazi.school.climate-adjustment.v1` override selects only that isolated section for the turn; the current manifest activates no card in those sections, so such a turn keeps every one of their obligations an explicit limitation.

# Explicit override profile: `bazi.school.ziping-structure.v1`

Apply these cards in the declared order below only when this profile is selected. This default profile is isolated; do not merge cards from another profile.

## Profile source locators and revisions

- Source `jinchenma94-bazi-skill`
  - Locator: `references/classical-texts.md#L130-L149`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Zi Ping structure vocabulary is adapted into evidence procedures; rank, success, and adversity assertions are excluded.
- Source `jinchenma94-bazi-skill`
  - Locator: `SKILL.md#L170-L173`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: The source's separate analysis phase is retained as provenance for the six-card workflow; unsafe downstream procedures are independently excluded.

## Method card `bazi.method.verify-chart.v1`

- Method card ID: `bazi.method.verify-chart.v1`
- School profile ID: `bazi.school.ziping-structure.v1`
- Topic: `verify-chart`
- Version: `1`
- Status: `school-specific`

### Requires

- `bazi.school.ziping-structure.v1`

### Workflow

1. First verify pillars and time basis: require schemaVersion === omds.bazi-profile.v1, system === bazi, BaziProfile.schoolProfileId === bazi.school.ziping-structure.v1, and exactly four pillars ordered year, month, day, hour. Require a validated MethodSelectionContext with calculationConventionSchoolProfileId === BaziProfile.schoolProfileId and selectedMethodSchoolProfileId === bazi.school.ziping-structure.v1; stop the pack as unavailable when any envelope or method-selection condition fails.
2. For every pillar require a canonical stemId, branchId, non-empty hiddenStemIds, occurrence-aligned tenGodIds, and a nayinId. Enforce NON_DAY_VISIBLE_TEN_GOD:=tenGodIds[0], NON_DAY_HIDDEN_TEN_GOD[index]:=tenGodIds[index+1] aligned to hiddenStemIds[index], and DAY_HIDDEN_TEN_GOD[index]:=tenGodIds[index] because the day master has no visible Ten God entry. Preserve duplicate identities as separate visible and hidden occurrences; do not reconstruct or deduplicate values from labels or prose.
3. Cross-check dayMasterId === pillars[2].stemId and pillars[2].position === day; treat any mismatch as a chart-integrity conflict and do not repair it by choosing a preferred result.
4. Read assumptions before analysis and report whether true-solar correction was applied. Treat display.input.localDateTime and display.input.correctedDateTime as non-canonical audit metadata only; never let display text replace canonical pillar IDs.
5. Inspect the birth time, timezone, longitude, standardLongitude, calendar, and correction statements that are actually present. If a boundary or time-basis choice is missing, record that limitation; do not invent a location, daylight-saving rule, early-Rat/late-Rat rule, or alternate pillar set.
6. Validate each luck-pillar record structurally: step must preserve source order, startYear must not exceed endYear, and adjacent ranges must be inspected for overlap or gaps. This is an integrity check only and does not label a period favorable or adverse.
7. Require non-empty provenance and identify the exact calculation-library and methodology revisions separately. A source citation establishes traceability, not agreement among schools and not evidence for a life claim.
8. Emit the verified canonical envelope, time-basis statement, integrity conflicts, missing inputs, provenance summary, and explicit gate to the next card without interpreting strength, structure, domain, personality, or timing.

### Supporting indicators

- None declared.

### Counter-indicators

- None declared.

### Output obligations

- `envelope-integrity`
- `pillar-integrity`
- `time-basis`
- `luck-pillar-integrity`
- `provenance`
- `conflicts-and-limits`

### Report mapping

| Output obligation | Existing report field |
| --- | --- |
| `envelope-integrity` | `structuralDiagnosis` |
| `pillar-integrity` | `structuralDiagnosis` |
| `time-basis` | `structuralDiagnosis` |
| `luck-pillar-integrity` | `structuralDiagnosis` |
| `provenance` | `structuralDiagnosis` |
| `conflicts-and-limits` | `limitations` |

Preserve supporting, counter, conflict, and unavailable states separately. Never fill an unavailable prerequisite from memory or source narrative.

### Safety policy

- Do not activate methodology outside `bazi.school.ziping-structure.v1` or the method cards explicitly declared in `requires`.
- Do not present death, financial, incarceration, legal, or medical claims as any outcomes.
- Do not perform cross-school mixing from undeclared methods.
- Do not perform deterministic outcome from verify-chart evidence.
- Do not perform diagnosis, prognosis, or treatment from verify-chart evidence.
- Do not perform numeric outcome scoring from verify-chart evidence.
- Do not perform personality or destiny assertion from verify-chart evidence.
- Do not perform professional advice from verify-chart evidence.
- Do not perform remediation or purchase prescription from verify-chart evidence.
- Do not perform retrospective fitting from known events.

### Source locators and revisions

- Source `jinchenma94-bazi-skill`
  - Locator: `SKILL.md#L131-L142`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Source insistence on deterministic calculation before analysis is adapted to the canonical calculator boundary; its Python implementation is not imported.
- Source `jinchenma94-bazi-skill`
  - Locator: `SKILL.md#L143-L154`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Source input fields become envelope and missing-input checks; implementation-specific CLI details are not adopted.
- Source `jinchenma94-bazi-skill`
  - Locator: `SKILL.md#L156-L158`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Minimum date-input and runtime prerequisites become availability checks without importing the upstream executable.
- Source `jinchenma94-bazi-skill`
  - Locator: `SKILL.md#L159-L164`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Calculator output precedence and time-boundary warnings become integrity checks without alternate chart reconstruction.
- Source `jinchenma94-bazi-skill`
  - Locator: `SKILL.md#L166-L169`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Canonical facts retain precedence over methodology references, and the separator closes the inspected calculation phase.
- Source `jinchenma94-bazi-skill`
  - Locator: `SKILL.md#L231-L240`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Boundary cases become explicit missing-input and time-basis limitations rather than alternate charts or inferred corrections.
- Source `jinchenma94-bazi-skill`
  - Locator: `references/shichen-table.md#L20-L30`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: The source's disputed Rat-hour convention is recorded as provenance only; the card does not override calculator facts.

**End method card:** `bazi.method.verify-chart.v1`

## Method card `bazi.method.seasonal-strength.v1`

- Method card ID: `bazi.method.seasonal-strength.v1`
- School profile ID: `bazi.school.ziping-structure.v1`
- Topic: `seasonal-strength`
- Version: `1`
- Status: `school-specific`

### Requires

- `bazi.school.ziping-structure.v1`
- `common.element.wood`
- `common.element.fire`
- `common.element.earth`
- `common.element.metal`
- `common.element.water`
- `common.stem.jia`
- `common.stem.yi`
- `common.stem.bing`
- `common.stem.ding`
- `common.stem.wu`
- `common.stem.ji`
- `common.stem.geng`
- `common.stem.xin`
- `common.stem.ren`
- `common.stem.gui`
- `common.branch.zi`
- `common.branch.chou`
- `common.branch.yin`
- `common.branch.mao`
- `common.branch.chen`
- `common.branch.si`
- `common.branch.wu`
- `common.branch.wei`
- `common.branch.shen`
- `common.branch.you`
- `common.branch.xu`
- `common.branch.hai`
- `bazi.ten-god.friend`
- `bazi.ten-god.rob-wealth`
- `bazi.ten-god.eating-god`
- `bazi.ten-god.hurting-officer`
- `bazi.ten-god.indirect-wealth`
- `bazi.ten-god.direct-wealth`
- `bazi.ten-god.seven-killings`
- `bazi.ten-god.direct-officer`
- `bazi.ten-god.indirect-resource`
- `bazi.ten-god.direct-resource`

### Workflow

1. After chart verification, establish month command and seasonal Qi from the month pillar only: MONTH_COMMAND_BRANCH := pillars.find(position === month).branchId and MONTH_MAIN_QI_STEM := that pillar.hiddenStemIds[0]; if either value is absent, mark this card unavailable rather than substituting a lunar month label.
2. Use STEM_ELEMENT_POLARITY_MAP exactly: common.stem.jia=>common.element.wood+yang, common.stem.yi=>common.element.wood+yin, common.stem.bing=>common.element.fire+yang, common.stem.ding=>common.element.fire+yin, common.stem.wu=>common.element.earth+yang, common.stem.ji=>common.element.earth+yin, common.stem.geng=>common.element.metal+yang, common.stem.xin=>common.element.metal+yin, common.stem.ren=>common.element.water+yang, common.stem.gui=>common.element.water+yin.
3. Use BRANCH_ELEMENT_MAP exactly: common.branch.zi=>common.element.water, common.branch.chou=>common.element.earth, common.branch.yin=>common.element.wood, common.branch.mao=>common.element.wood, common.branch.chen=>common.element.earth, common.branch.si=>common.element.fire, common.branch.wu=>common.element.fire, common.branch.wei=>common.element.earth, common.branch.shen=>common.element.metal, common.branch.you=>common.element.metal, common.branch.xu=>common.element.earth, common.branch.hai=>common.element.water. Preserve hiddenStemIds order as main, middle, residual Qi and do not attach numeric weights.
4. Use GENERATION_CYCLE exactly: common.element.wood->common.element.fire, common.element.fire->common.element.earth, common.element.earth->common.element.metal, common.element.metal->common.element.water, common.element.water->common.element.wood. Use CONTROL_CYCLE exactly: common.element.wood->common.element.earth, common.element.earth->common.element.water, common.element.water->common.element.fire, common.element.fire->common.element.metal, common.element.metal->common.element.wood.
5. Derive Ten God identity only from dayMasterId versus a candidate stem using element direction and polarity: same element same polarity=>bazi.ten-god.friend; same element opposite polarity=>bazi.ten-god.rob-wealth; candidate generates day master same|opposite=>bazi.ten-god.indirect-resource|bazi.ten-god.direct-resource; day master generates candidate same|opposite=>bazi.ten-god.eating-god|bazi.ten-god.hurting-officer; candidate controls day master same|opposite=>bazi.ten-god.seven-killings|bazi.ten-god.direct-officer; day master controls candidate same|opposite=>bazi.ten-god.indirect-wealth|bazi.ten-god.direct-wealth. Cross-check derived identities against emitted tenGodIds and record conflicts.
6. Then identify day-master support, control, output, and drain by grouping emitted evidence exactly: SUPPORT_RESOURCE:=bazi.ten-god.direct-resource+bazi.ten-god.indirect-resource; SUPPORT_PEER:=bazi.ten-god.friend+bazi.ten-god.rob-wealth; OUTPUT_DRAIN:=bazi.ten-god.eating-god+bazi.ten-god.hurting-officer; CONTROL_PRESSURE:=bazi.ten-god.direct-officer+bazi.ten-god.seven-killings; CONTROLLED_WEALTH:=bazi.ten-god.direct-wealth+bazi.ten-god.indirect-wealth. Expand occurrences with NON_DAY_VISIBLE_TEN_GOD:=tenGodIds[0], NON_DAY_HIDDEN_TEN_GOD[index]:=tenGodIds[index+1], and DAY_HIDDEN_TEN_GOD[index]:=tenGodIds[index]; preserve duplicate IDs at different positions and never count or score force.
7. Compare the month-command element, day-master element, exposed stems, and hidden stems qualitatively. Record supporting, controlling, output, and controlled candidates side by side; repeated occurrence is evidence to inspect, not a numeric magnitude and not a categorical strong-or-weak conclusion.
8. Counter-check every provisional pattern against missing hour or time-basis data, conflicting generated Ten Gods, exact day-master hidden-stem occurrences outside the month branch, and relationFacts that join or oppose participants. Set ROOT_STATUS:=unavailable because BaziProfile has no reviewed root fact and the excluded life-stage table cannot be reconstructed from hidden-stem identity. Keep mixed evidence unresolved and hand the evidence matrix to the structure card without naming a useful god.

### Supporting indicators

- None declared.

### Counter-indicators

- None declared.

### Output obligations

- `month-command`
- `day-master-map`
- `support-control-output-drain`
- `visible-and-hidden-evidence`
- `relation-counterchecks`
- `unresolved-strength-evidence`

### Report mapping

| Output obligation | Existing report field |
| --- | --- |
| `month-command` | `structuralDiagnosis` |
| `day-master-map` | `structuralDiagnosis` |
| `support-control-output-drain` | `structuralDiagnosis` |
| `visible-and-hidden-evidence` | `structuralDiagnosis` |
| `relation-counterchecks` | `structuralDiagnosis` |
| `unresolved-strength-evidence` | `limitations` |

Preserve supporting, counter, conflict, and unavailable states separately. Never fill an unavailable prerequisite from memory or source narrative.

### Safety policy

- Do not activate methodology outside `bazi.school.ziping-structure.v1` or the method cards explicitly declared in `requires`.
- Do not present death, financial, incarceration, legal, or medical claims as any outcomes.
- Do not perform cross-school mixing from undeclared methods.
- Do not perform deterministic outcome from seasonal-strength evidence.
- Do not perform diagnosis, prognosis, or treatment from seasonal-strength evidence.
- Do not perform numeric outcome scoring from seasonal-strength evidence.
- Do not perform personality or destiny assertion from seasonal-strength evidence.
- Do not perform professional advice from seasonal-strength evidence.
- Do not perform remediation or purchase prescription from seasonal-strength evidence.
- Do not perform retrospective fitting from known events.

### Source locators and revisions

- Source `jinchenma94-bazi-skill`
  - Locator: `references/wuxing-tables.md#L14-L33`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Exact stem element and polarity identities are retained in an explicit lookup map without interpretive attributes.
- Source `jinchenma94-bazi-skill`
  - Locator: `references/wuxing-tables.md#L34-L52`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Exact branch element identities are retained in an explicit lookup map without zodiac, direction, or personality interpretation.
- Source `jinchenma94-bazi-skill`
  - Locator: `references/wuxing-tables.md#L100-L112`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Ten God derivation is retained mechanically; asserted personality and social-role meanings are excluded.
- Source `jinchenma94-bazi-skill`
  - Locator: `references/wuxing-tables.md#L128-L133`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Five-element generation and control cycles are retained mechanically without symbolic or outcome interpretation.
- Source `jinchenma94-bazi-skill`
  - Locator: `references/wuxing-tables.md#L157-L173`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Hidden-stem identities and order are retained; the excluded following line's approximate weights never enter qualitative evaluation.
- Source `jinchenma94-bazi-skill`
  - Locator: `references/classical-texts.md#L61-L67`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Month command and assistance remain counter-checked evidence dimensions, while root status is unavailable without the excluded life-stage rule and cannot become categorical strength truth.
- Source `jinchenma94-bazi-skill`
  - Locator: `references/classical-texts.md#L68-L71`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Flow and obstruction language is adapted into qualitative element-cycle evidence without prescribing a bridging result.

**End method card:** `bazi.method.seasonal-strength.v1`

## Method card `bazi.method.ziping-structure.v1`

- Method card ID: `bazi.method.ziping-structure.v1`
- School profile ID: `bazi.school.ziping-structure.v1`
- Topic: `ziping-structure`
- Version: `1`
- Status: `school-specific`

### Requires

- `bazi.school.ziping-structure.v1`
- `common.element.wood`
- `common.element.fire`
- `common.element.earth`
- `common.element.metal`
- `common.element.water`
- `bazi.ten-god.friend`
- `bazi.ten-god.rob-wealth`
- `bazi.ten-god.eating-god`
- `bazi.ten-god.hurting-officer`
- `bazi.ten-god.indirect-wealth`
- `bazi.ten-god.direct-wealth`
- `bazi.ten-god.seven-killings`
- `bazi.ten-god.direct-officer`
- `bazi.ten-god.indirect-resource`
- `bazi.ten-god.direct-resource`

### Workflow

1. Consume the verified month pillar and build MONTH_HIDDEN_INVENTORY := month.hiddenStemIds.map((stemId, index) => ({ stemId, qiOrder: index, tenGodId: month.tenGodIds[index + 1], exposedAt: non-day pillars whose stemId equals stemId and whose NON_DAY_VISIBLE_TEN_GOD:=tenGodIds[0] equals tenGodId })). The month is non-day, so enforce NON_DAY_HIDDEN_TEN_GOD[index]:=tenGodIds[index+1]; elsewhere enforce DAY_HIDDEN_TEN_GOD[index]:=tenGodIds[index]. Preserve duplicate Ten God occurrences and every ordered hidden item, and make the card unavailable on a length or alignment conflict.
2. To determine a structure candidate set, first compute ELIGIBLE_ORDINARY_CANDIDATES:=MONTH_HIDDEN_INVENTORY.filter(exposedAt.length > 0), then map only eligible items with ORDINARY_STRUCTURE_MAP exactly: bazi.ten-god.direct-officer=>direct-officer-structure-candidate, bazi.ten-god.seven-killings=>seven-killings-structure-candidate, bazi.ten-god.direct-wealth=>direct-wealth-structure-candidate, bazi.ten-god.indirect-wealth=>indirect-wealth-structure-candidate, bazi.ten-god.direct-resource=>direct-resource-structure-candidate, bazi.ten-god.indirect-resource=>indirect-resource-structure-candidate, bazi.ten-god.eating-god=>eating-god-structure-candidate, bazi.ten-god.hurting-officer=>hurting-officer-structure-candidate. Friend or rob-wealth is inventory evidence but has no ordinary candidate in this map.
3. Apply exposure outcomes exactly: ZERO_EXPOSURES=>ordinary-structure-unavailable; ONE_EXPOSURE=>retain-that-candidate; MULTIPLE_EXPOSURES=>retain-all-eligible-candidates+precedence-unresolved; UNEXPOSED_HIDDEN_STEM=>inventory-only-not-ordinary-candidate. Preserve qiOrder for inventory and candidates, but never promote main-Qi order, repetition, or convenience into a winner rule.
4. Enforce the exposure boundary with these executable cases: CASE_ZERO_EXPOSED:=month-hidden[bazi.ten-god.direct-officer,bazi.ten-god.direct-wealth]+visible[]=>ordinary-structure-unavailable; CASE_MAIN_UNEXPOSED_SECONDARY_EXPOSED:=month-hidden[main:bazi.ten-god.direct-officer,secondary:bazi.ten-god.direct-wealth]+visible[bazi.ten-god.direct-wealth]=>retain-secondary-direct-wealth-only; CASE_MULTIPLE_EXPOSED:=month-hidden[main:bazi.ten-god.direct-officer,secondary:bazi.ten-god.direct-wealth]+visible[bazi.ten-god.direct-officer,bazi.ten-god.direct-wealth]=>retain-both-in-qiOrder+precedence-unresolved. These cases preserve all inventory entries but never turn an unexposed entry into an ordinary candidate.
5. Use STRUCTURE_CONDITION_MAP exactly for each retained candidate: bazi.ten-god.direct-officer=>support:bazi.ten-god.direct-resource|bazi.ten-god.indirect-resource,counter:bazi.ten-god.hurting-officer; bazi.ten-god.seven-killings=>support:bazi.ten-god.eating-god|bazi.ten-god.direct-resource|bazi.ten-god.indirect-resource,counter:unavailable; bazi.ten-god.direct-wealth|bazi.ten-god.indirect-wealth=>support:unavailable,counter:bazi.ten-god.friend|bazi.ten-god.rob-wealth; bazi.ten-god.direct-resource=>support:unavailable,counter:unavailable; bazi.ten-god.indirect-resource=>support:unavailable,counter:bazi.ten-god.eating-god; bazi.ten-god.eating-god=>support:unavailable,counter:bazi.ten-god.indirect-resource; bazi.ten-god.hurting-officer=>support:unavailable,counter:bazi.ten-god.direct-officer. DIRECT_OFFICER_ASSISTANT_PATTERN is the bounded Resource-star assistant example: match both canonical Resource Ten Gods as occurrence evidence, retain Hurting Officer as the counter, and do not import the source's rank, success, failure, favorable, adverse, personality, or outcome claims. Unlisted support or counter conditions are unavailable and must not be supplied from memory.
6. Evaluate the mapped support and counter IDs against every exact emitted visible and hidden Ten God occurrence, preserving pillar position, visibility, duplicates, and simultaneous supporting and countering occurrences. Record present or absent evidence only; do not infer force, cancellation, rank, success, favorable status, adversity, personality, or outcome from a mapped condition.
7. Keep bazi.method.useful-god.structure as this profile's only active lens. Record bazi.method.useful-god.balance=>prohibited-in-this-profile, bazi.method.useful-god.climate-adjustment=>prohibited-in-this-profile, and bazi.method.useful-god.bridging=>prohibited-and-no-selectable-school-profile. They remain parallel proposed dispute positions, never supporting votes, fallback rules, or implicit defaults.
8. At the required phase inspect climate adjustment and bridging as separate lenses by reporting status only, not executing either lens: climate adjustment is inactive here and executable only through bazi.school.climate-adjustment.v1; bridging is unresolved, non-selectable, and has no school or card. Do not derive their candidates, import their mappings, or let the calling Skill override prohibitedMixing.
9. Counter-check each retained candidate against the full month-hidden inventory, exact visible exposure occurrences, the candidate-specific STRUCTURE_CONDITION_MAP, relationFacts, missing time-basis facts, and bazi.dispute.useful-god-concepts. The pinned source gives no precedence rule among multiple eligible exposed candidates, so a winner remains unavailable unless a future reviewed source adds an explicit rule.
10. Return the ordered month-hidden inventory, eligible ordinary candidates or unavailable status, exact exposure evidence, mapped support and counter occurrences or unavailable fields, inactive/prohibited/unavailable lens statuses, missing prerequisites, and unresolved precedence and dispute positions. Do not emit a server-calculated structure, balance, climate, bridging, useful-god, personality, domain, or event conclusion.
11. This workflow implements bazi.claim.ziping-structure-candidates.v1, approved by the normalization-safety-review at revision task-1-claim-rule-review.2026-09-03 (standards/reviews/bazi/ziping-domain-claim-rules.yaml).

### Supporting indicators

- None declared.

### Counter-indicators

- None declared.

### Output obligations

- `ordered-month-hidden-inventory`
- `eligible-ordinary-candidates-or-unavailable`
- `exposure-eligibility-and-precedence`
- `mapped-support-and-counter-occurrences`
- `inactive-and-prohibited-useful-god-lenses`
- `unresolved-disputes-and-limits`

### Report mapping

| Output obligation | Existing report field |
| --- | --- |
| `ordered-month-hidden-inventory` | `structuralDiagnosis` |
| `eligible-ordinary-candidates-or-unavailable` | `structuralDiagnosis` |
| `exposure-eligibility-and-precedence` | `structuralDiagnosis` |
| `mapped-support-and-counter-occurrences` | `structuralDiagnosis` |
| `inactive-and-prohibited-useful-god-lenses` | `limitations` |
| `unresolved-disputes-and-limits` | `limitations` |

Preserve supporting, counter, conflict, and unavailable states separately. Never fill an unavailable prerequisite from memory or source narrative.

### Safety policy

- Do not activate methodology outside `bazi.school.ziping-structure.v1` or the method cards explicitly declared in `requires`.
- Do not present death, financial, incarceration, legal, or medical claims as any outcomes.
- Do not perform cross-school mixing from undeclared methods.
- Do not perform deterministic outcome from ziping-structure evidence.
- Do not perform diagnosis, prognosis, or treatment from ziping-structure evidence.
- Do not perform numeric outcome scoring from ziping-structure evidence.
- Do not perform personality or destiny assertion from ziping-structure evidence.
- Do not perform professional advice from ziping-structure evidence.
- Do not perform remediation or purchase prescription from ziping-structure evidence.
- Do not perform retrospective fitting from known events.

### Source locators and revisions

- Source `jinchenma94-bazi-skill`
  - Locator: `references/classical-texts.md#L39-L45`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: All month-hidden stems remain inventory evidence, but only an exact Ten God visibly exposed in a non-day heavenly stem is eligible; the listed candidate-specific support and counter conditions are retained without personality, rank, valence, or outcome claims.
- Source `jinchenma94-bazi-skill`
  - Locator: `references/classical-texts.md#L130-L149`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: The Direct Officer assistant example is bounded to Direct Resource and Indirect Resource occurrence evidence; status rank, force, favorable or adverse labels, and life outcomes are excluded.
- Source `jinchenma94-bazi-skill`
  - Locator: `references/classical-texts.md#L85-L88`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Ordinary and special structure category names are retained only to bound candidate availability, without source outcome claims.
- Source `jinchenma94-bazi-skill`
  - Locator: `references/classical-texts.md#L89-L93`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: The source separately lists balance, climate adjustment, and bridging; structure is separately sourced at references/classical-texts.md#L130-L149, while following tendency remains unavailable with no selectable school or executable card.
- Source `jinchenma94-bazi-method-authority`
  - Locator: `references/classical-texts.md#L39-L45`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Owner-attested method authority backing bazi.claim.ziping-structure-candidates.v1 (standards/reviews/bazi/ziping-domain-claim-rules.yaml).

**End method card:** `bazi.method.ziping-structure.v1`

## Method card `bazi.method.relations.v1`

- Method card ID: `bazi.method.relations.v1`
- School profile ID: `bazi.school.ziping-structure.v1`
- Topic: `relations`
- Version: `1`
- Status: `school-specific`

### Requires

- `bazi.school.ziping-structure.v1`
- `bazi.relation.combination`
- `bazi.relation.clash`
- `bazi.relation.punishment`
- `bazi.relation.harm`
- `bazi.relation.destruction`
- `bazi.relation.stem-combination`
- `bazi.relation.branch-trine`

### Workflow

1. After the structure candidate, inspect combinations, clashes, punishments, harm, and destruction by iterating BaziProfile.relationFacts exactly once, while also retaining stem combinations and complete trines. Only the first four plus stem combinations and trines are source-backed here; partition bazi.relation.destruction into a proposed source-gap channel before synthesis.
2. Use RELATION_KIND_MAP exactly: bazi.relation.combination=>branch-pair, bazi.relation.clash=>branch-opposition, bazi.relation.punishment=>branch-punishment, bazi.relation.harm=>branch-harm, bazi.relation.destruction=>branch-destruction, bazi.relation.stem-combination=>stem-pair, bazi.relation.branch-trine=>complete-branch-trine. Do not infer half-trines or un-emitted meetings.
3. Set DESTRUCTION_STATUS:=proposed for every bazi.relation.destruction fact: this family is absent from the pinned Jinchenma source, cannot support a source-checked conclusion, cannot activate a timing or transformation rule, and must be carried only to the proposed-source-gap-relations output with its calculator provenance. Do not infer a missing pair or promote the static-table proposal through repetition.
4. For each fact, require participantIds length to match pillarPositions length, verify that every participant ID occurs at the paired pillar position, and preserve multiple facts even when they share participants. A failed check is an integrity conflict, not permission to reconstruct a relation.
5. Treat transformedElementId === null as unconfirmed transformation. A source-listed associated element is metadata only; do not replace null from the source's traditional association, from a label, or from a preferred school. If a future profile emits non-null, still require its documented transformation conditions before using it.
6. Build a participant matrix by pillar position and record coexisting relation kinds. Counter-check a source-backed combination or trine against source-backed clashes, punishments, harm, missing participants, and unresolved time basis; list proposed destruction beside but outside that source-checked counter-check. No single relation automatically cancels another and no relation is inherently favorable or adverse.
7. Carry the prior structure candidate beside the relation matrix, but do not let a relation rename the structure or useful-god lens. Note whether relation evidence supports, complicates, or is irrelevant to a specific procedural condition, always citing participant IDs and positions.
8. Then synthesize the natal structure as a conditional evidence summary containing the month command, day-master evidence groups, structure candidate, exposures, relation matrix, counter-patterns, and unresolved conditions. Synthesis is performed by the Skill, not emitted as a calculator fact.
9. Output every relation fact and counter-check before handing the conditional natal summary to domain analysis; withhold personality, family, profession, health, legal, financial, or event conclusions from relation names alone.

### Supporting indicators

- None declared.

### Counter-indicators

- None declared.

### Output obligations

- `emitted-relations`
- `participant-integrity`
- `transformation-status`
- `coexisting-relations`
- `proposed-source-gap-relations`
- `relation-counterchecks`
- `conditional-natal-synthesis`

### Report mapping

| Output obligation | Existing report field |
| --- | --- |
| `emitted-relations` | `structuralDiagnosis` |
| `participant-integrity` | `structuralDiagnosis` |
| `transformation-status` | `structuralDiagnosis` |
| `coexisting-relations` | `structuralDiagnosis` |
| `proposed-source-gap-relations` | `limitations` |
| `relation-counterchecks` | `structuralDiagnosis` |
| `conditional-natal-synthesis` | `scenarios` |

Preserve supporting, counter, conflict, and unavailable states separately. Never fill an unavailable prerequisite from memory or source narrative.

### Safety policy

- Do not activate methodology outside `bazi.school.ziping-structure.v1` or the method cards explicitly declared in `requires`.
- Do not present death, financial, incarceration, legal, or medical claims as any outcomes.
- Do not perform cross-school mixing from undeclared methods.
- Do not perform deterministic outcome from relations evidence.
- Do not perform diagnosis, prognosis, or treatment from relations evidence.
- Do not perform numeric outcome scoring from relations evidence.
- Do not perform personality or destiny assertion from relations evidence.
- Do not perform professional advice from relations evidence.
- Do not perform remediation or purchase prescription from relations evidence.
- Do not perform retrospective fitting from known events.

### Source locators and revisions

- Source `jinchenma94-bazi-skill`
  - Locator: `references/wuxing-tables.md#L53-L64`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Exact stem-combination pairs are retained, while associated elements remain metadata and transformation requires unavailable conditions.
- Source `jinchenma94-bazi-skill`
  - Locator: `references/wuxing-tables.md#L65-L68`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Exact branch clashes are retained as source-backed facts without inherent valence or event meanings.
- Source `jinchenma94-bazi-skill`
  - Locator: `references/wuxing-tables.md#L69-L76`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Complete trine members are retained while half-trine force and automatic transformation claims are excluded.
- Source `jinchenma94-bazi-skill`
  - Locator: `references/wuxing-tables.md#L86-L88`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Exact branch combinations are retained, disputed associated elements remain metadata, and transformation stays unconfirmed.
- Source `jinchenma94-bazi-skill`
  - Locator: `references/wuxing-tables.md#L89-L94`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Exact triple, pair, and self-punishment families are retained without importing their adverse traditional labels.
- Source `jinchenma94-bazi-skill`
  - Locator: `references/wuxing-tables.md#L95-L99`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Exact harm pairs are retained; destruction's absence from the complete inspected relation section remains an explicit source gap.
- Source `jinchenma94-bazi-skill`
  - Locator: `references/classical-texts.md#L152-L162`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: The source warning against mechanical rules is adapted into explicit conflict preservation without importing medicinal metaphors.

**End method card:** `bazi.method.relations.v1`

## Method card `bazi.method.domain-analysis.v1`

- Method card ID: `bazi.method.domain-analysis.v1`
- School profile ID: `bazi.school.ziping-structure.v1`
- Topic: `domain-analysis`
- Version: `1`
- Status: `school-specific`

### Requires

- `bazi.school.ziping-structure.v1`
- `bazi.ten-god.friend`
- `bazi.ten-god.rob-wealth`
- `bazi.ten-god.eating-god`
- `bazi.ten-god.hurting-officer`
- `bazi.ten-god.indirect-wealth`
- `bazi.ten-god.direct-wealth`
- `bazi.ten-god.seven-killings`
- `bazi.ten-god.direct-officer`
- `bazi.ten-god.indirect-resource`
- `bazi.ten-god.direct-resource`

### Workflow

1. Require an explicit user question or named domain, then map only the requested domain as user-provided context; if it is absent, ambiguous, medical, legal-merits, investment-selection, or another professional-advice request, record the boundary and ask for a safe reflective scope rather than choosing one.
2. Build EXHAUSTIVE_CANONICAL_EVIDENCE:=all Ten God occurrence records+all emitted relationFacts before considering the question. Expand every pillar with NON_DAY_VISIBLE_TEN_GOD:=tenGodIds[0], NON_DAY_HIDDEN_TEN_GOD[index]:=tenGodIds[index+1], and DAY_HIDDEN_TEN_GOD[index]:=tenGodIds[index]; preserve duplicate IDs as separate visible and hidden occurrences with pillar positions.
3. Treat domain-specific Ten God taxonomy unavailable: the pinned source derives Ten God identities but does not provide a reviewed exhaustive mapping from those identities to modern work, budget, learning, collaboration, relationship, or wellbeing domains. Do not invent, remember, or close such a taxonomy in this card.
4. Use the explicit user-provided context only to frame safe questions, never to filter out canonical evidence or assign a Ten God to a domain. When a reviewed structural condition or relation participant is relevant to the user's wording, cite that condition exactly; otherwise mark the connection unavailable rather than filling it with a traditional meaning.
5. Connect the exhaustive facts to the conditional natal synthesis only through cited structure conditions and exact relation participants. Record whether each condition is supported, countered, conflicted, or unavailable; do not convert frequency into importance, infer a meaning from a label, or select a conclusion by majority.
6. Inspect counter-evidence from every emitted Ten God occurrence, every emitted relationFact, missing time-basis detail, unresolved useful-god dispute, and absent user context. A single Ten God, stem, branch, pillar, or relation can never support a major domain statement by itself.
7. Form reflective observations as evidence-bounded questions about the user's stated context, distinguishing canonical fact, school procedure, inference, and user-provided information. Do not turn traditional kinship, gender, status, wealth, profession, or personality labels into assertions about a real person.
8. For work or resources, avoid professional recommendations and forecasted gains or losses. For collaboration or relationships, avoid compatibility verdicts and role stereotypes. For any wellbeing context, do not map symptoms, diagnoses, treatment, risk, lifespan, or accident claims.
9. Return the normalized user question, exhaustive canonical evidence, cited structural links or unavailable status, supporting and counter-conditions, unresolved alternatives, safety boundary, and questions for user reflection without adding a fate narrative or domain outcome.

### Supporting indicators

- None declared.

### Counter-indicators

- None declared.

### Output obligations

- `requested-domain`
- `exhaustive-canonical-evidence`
- `structural-links-or-unavailable`
- `supporting-and-counter-conditions`
- `unresolved-alternatives`
- `safety-boundary-and-reflection`

### Report mapping

| Output obligation | Existing report field |
| --- | --- |
| `requested-domain` | `domainAnalysis` |
| `exhaustive-canonical-evidence` | `structuralDiagnosis` |
| `structural-links-or-unavailable` | `structuralDiagnosis` |
| `supporting-and-counter-conditions` | `domainAnalysis` |
| `unresolved-alternatives` | `limitations` |
| `safety-boundary-and-reflection` | `domainAnalysis` |

Preserve supporting, counter, conflict, and unavailable states separately. Never fill an unavailable prerequisite from memory or source narrative.

### Safety policy

- Do not activate methodology outside `bazi.school.ziping-structure.v1` or the method cards explicitly declared in `requires`.
- Do not present death, financial, incarceration, legal, or medical claims as any outcomes.
- Do not perform cross-school mixing from undeclared methods.
- Do not perform deterministic outcome from domain-analysis evidence.
- Do not perform diagnosis, prognosis, or treatment from domain-analysis evidence.
- Do not perform numeric outcome scoring from domain-analysis evidence.
- Do not perform personality or destiny assertion from domain-analysis evidence.
- Do not perform professional advice from domain-analysis evidence.
- Do not perform remediation or purchase prescription from domain-analysis evidence.
- Do not perform retrospective fitting from known events.

### Source locators and revisions

- Source `jinchenma94-bazi-skill`
  - Locator: `references/wuxing-tables.md#L100-L112`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Ten God identity derivation supports exhaustive canonical occurrence retrieval, while no unsupported modern domain taxonomy, personality, kinship, status, or outcome meaning is imported.
- Source `jinchenma94-bazi-skill`
  - Locator: `SKILL.md#L179-L183`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: The instruction to list pillar Ten Gods is narrowed to exhaustive source-attributed facts; source importance rankings, kinship assertions, personality meanings, and outcomes are excluded.

**End method card:** `bazi.method.domain-analysis.v1`

## Method card `bazi.method.timing.v1`

- Method card ID: `bazi.method.timing.v1`
- School profile ID: `bazi.school.ziping-structure.v1`
- Topic: `timing`
- Version: `1`
- Status: `school-specific`

### Requires

- `bazi.school.ziping-structure.v1`
- `common.element.wood`
- `common.element.fire`
- `common.element.earth`
- `common.element.metal`
- `common.element.water`
- `common.stem.jia`
- `common.stem.yi`
- `common.stem.bing`
- `common.stem.ding`
- `common.stem.wu`
- `common.stem.ji`
- `common.stem.geng`
- `common.stem.xin`
- `common.stem.ren`
- `common.stem.gui`
- `common.branch.zi`
- `common.branch.chou`
- `common.branch.yin`
- `common.branch.mao`
- `common.branch.chen`
- `common.branch.si`
- `common.branch.wu`
- `common.branch.wei`
- `common.branch.shen`
- `common.branch.you`
- `common.branch.xu`
- `common.branch.hai`

### Workflow

1. Require a user-supplied target date or target year and the conditional natal/domain synthesis. Select exactly one BaziProfile.luckPillars record whose startYear &lt;= target year &lt;= endYear; overlapping matches are a data conflict and no match makes luck-pillar analysis unavailable.
2. First apply the selected luck pillar before year activation. Construct occurrence records with stable source identities OCCURRENCE_KEYS:=natal:year|natal:month|natal:day|natal:hour|luck:&lt;step>|year:&lt;target>; populate the four natal records and selected luck:&lt;step> now, preserving equal stem or branch IDs at different sources rather than deduplicating them. Inventory step, stemId, branchId, startYear, and endYear without favorable or adverse labels.
3. Use SOURCE_BACKED_PAIR_LOOKUP exactly: COMBINE_BRANCHES:=common.branch.zi+common.branch.chou|common.branch.yin+common.branch.hai|common.branch.mao+common.branch.xu|common.branch.chen+common.branch.you|common.branch.si+common.branch.shen|common.branch.wu+common.branch.wei; CLASH_BRANCHES:=common.branch.zi+common.branch.wu|common.branch.chou+common.branch.wei|common.branch.yin+common.branch.shen|common.branch.mao+common.branch.you|common.branch.chen+common.branch.xu|common.branch.si+common.branch.hai; COMBINE_STEMS:=common.stem.jia+common.stem.ji|common.stem.yi+common.stem.geng|common.stem.bing+common.stem.xin|common.stem.ding+common.stem.ren|common.stem.wu+common.stem.gui. A candidate requires matching IDs on two distinct occurrence records.
4. Use HEAVENLY_STEM_CONTROL_LOOKUP from canonical identities exactly. TIMING_STEM_ELEMENT_MAP:=common.stem.jia|common.stem.yi=>common.element.wood, common.stem.bing|common.stem.ding=>common.element.fire, common.stem.wu|common.stem.ji=>common.element.earth, common.stem.geng|common.stem.xin=>common.element.metal, common.stem.ren|common.stem.gui=>common.element.water. TIMING_CONTROL_CYCLE:=common.element.wood->common.element.earth|common.element.earth->common.element.water|common.element.water->common.element.fire|common.element.fire->common.element.metal|common.element.metal->common.element.wood. For every two distinct stem occurrence records, emit one directional controller and controlled participant only when their mapped elements match the cycle; preserve every competing match and attach no favorable or adverse label, event meaning, or transformation.
5. Use SOURCE_BACKED_MULTI_BRANCH_LOOKUP exactly: PUNISHMENT_TRIPLES:=common.branch.yin+common.branch.si+common.branch.shen|common.branch.chou+common.branch.xu+common.branch.wei; PUNISHMENT_PAIR:=common.branch.zi+common.branch.mao; SELF_PUNISHMENTS:=common.branch.chen+common.branch.chen|common.branch.wu+common.branch.wu|common.branch.you+common.branch.you|common.branch.hai+common.branch.hai; HARMS:=common.branch.zi+common.branch.wei|common.branch.chou+common.branch.wu|common.branch.yin+common.branch.si|common.branch.mao+common.branch.chen|common.branch.shen+common.branch.hai|common.branch.you+common.branch.xu; COMPLETE_TRINES:=common.branch.shen+common.branch.zi+common.branch.chen|common.branch.hai+common.branch.mao+common.branch.wei|common.branch.yin+common.branch.wu+common.branch.xu|common.branch.si+common.branch.you+common.branch.chou; COMPLETE_TRINE_ASSOCIATED_ELEMENTS:=common.branch.shen+common.branch.zi+common.branch.chen=>common.element.water|common.branch.hai+common.branch.mao+common.branch.wei=>common.element.wood|common.branch.yin+common.branch.wu+common.branch.xu=>common.element.fire|common.branch.si+common.branch.you+common.branch.chou=>common.element.metal. Associated elements are metadata only.
6. Match triple punishments and complete trines only when all three branch IDs occur on three distinct occurrence records. Match a self-punishment only from two distinct occurrence records carrying the same listed branch; if a branch occurs three or more times, enumerate every combination of two sources. For every family retain every competing match, including candidates that share one or more occurrence records; never collapse natal, luck, and year sources into a set of branch names.
7. Run every lookup over the natal-plus-luck records, but emit only LUCK_CANDIDATE_SCOPE:=occurrenceKeys includes luck:&lt;step> and at least one natal:*. Preserve the exact family plus sorted occurrence-key set as the candidate identity, exclude pre-existing all-natal matches from the luck layer, and snapshot every matched identity as PRE_YEAR_MATCH_KEY_SETS before annual evidence is appended.
8. Verify luck scoping against these executable examples: CASE_LUCK_PAIR_POSITIVE:=natal:year=zi+luck:&lt;step>=chou=>include; CASE_LUCK_PAIR_NEGATIVE:=natal:year=zi+natal:month=chou+luck:&lt;step>=mao=>exclude-old-natal-pair; CASE_LUCK_SELF_POSITIVE:=natal:year=chen+luck:&lt;step>=chen=>include; CASE_LUCK_SELF_NEGATIVE:=natal:year=chen+natal:month=chen+luck:&lt;step>=mao=>exclude-old-natal-self; CASE_LUCK_TRIPLE_POSITIVE:=natal:year=yin+natal:month=si+luck:&lt;step>=shen=>include; CASE_LUCK_TRINE_POSITIVE:=natal:year=shen+natal:month=zi+luck:&lt;step>=chen=>include; CASE_LUCK_STEM_CONTROL_POSITIVE:=natal:year=common.stem.jia+luck:&lt;step>=common.stem.wu=>include(controller=natal:year,controlled=luck:&lt;step>); CASE_LUCK_STEM_CONTROL_UNRELATED_NEGATIVE:=natal:year=common.stem.jia+luck:&lt;step>=common.stem.yi=>exclude-no-control. These cases specify source distinctness and layer membership, not an outcome.
9. annual stemId and branchId are not emitted by BaziProfile. Require a separate deterministic calendar fact carrying the exact target date, time basis, annual stemId, annual branchId, and provenance; if it is absent, ambiguous around the applicable solar-term boundary, or supplied only as a display label, mark year activation unavailable and do not calculate it from memory.
10. When valid annual facts are supplied, append exactly one year:&lt;target> occurrence only after completing the natal-plus-luck matrix, then rerun every source-backed lookup over natal, luck, and year records. Emit only YEAR_CANDIDATE_SCOPE:=occurrenceKeys includes year:&lt;target> and at least one natal:*|luck:&lt;step>. Compare family plus sorted occurrence-key identity against PRE_YEAR_MATCH_KEY_SETS; do not reclassify or duplicate an old occurrence-key set. Retain participant IDs, exact source keys, relation family, and every new competing match. Associated elements remain metadata and transformedElementId === null remains unconfirmed.
11. Verify year scoping against these executable examples: CASE_YEAR_TRIPLE_POSITIVE:=natal:year=yin+luck:&lt;step>=si+year:&lt;target>=shen=>include; CASE_YEAR_TRINE_POSITIVE:=natal:year=shen+luck:&lt;step>=zi+year:&lt;target>=chen=>include; CASE_YEAR_PAIR_POSITIVE:=luck:&lt;step>=zi+year:&lt;target>=chou=>include; CASE_YEAR_SELF_POSITIVE:=natal:year=chen+year:&lt;target>=chen=>include; CASE_YEAR_UNRELATED_NEGATIVE:=natal:year=zi+luck:&lt;step>=chou+year:&lt;target>=mao=>exclude-old-natal-luck-pair; CASE_YEAR_STEM_CONTROL_POSITIVE:=luck:&lt;step>=common.stem.geng+year:&lt;target>=common.stem.jia=>include(controller=luck:&lt;step>,controlled=year:&lt;target>); CASE_YEAR_STEM_CONTROL_UNRELATED_NEGATIVE:=natal:year=common.stem.jia+luck:&lt;step>=common.stem.yi+year:&lt;target>=common.stem.ren=>exclude-no-year-control. The annual occurrence must participate in every emitted year candidate.
12. Keep destruction outside activation lookup: destruction is proposed and unsourced by Jinchenma, so never construct natal-to-luck, natal-to-year, or luck-to-year destruction from this card. Existing natal bazi.relation.destruction facts may be displayed only under proposed-source-gap evidence with their calculator provenance and cannot support a source-checked timing conclusion.
13. Counter-check each timing candidate against unresolved natal structure, the useful-god dispute, missing domain context, coexisting relation candidates, occurrence multiplicity, and source-boundary assumptions. The sequence identifies evidence layers; it does not turn a relation into an event, date promise, causal claim, or transformation.
14. Do not use historical event calibration, retrospective chart tuning, or user confirmation of past events to select a structure, useful god, luck pillar, annual fact, or relation. New biographical information may be recorded as user context but never as training or backfitting evidence.
15. Finally present counter-indicators and limits beside the selected luck-pillar facts, optional annual facts, layer-by-layer relation candidates, provenance, missing prerequisites, and uncertainty. Return candidate windows only as reflective context and never as a predicted outcome.

### Supporting indicators

- None declared.

### Counter-indicators

- None declared.

### Output obligations

- `target-and-prerequisites`
- `selected-luck-pillar`
- `luck-to-natal-candidates`
- `annual-fact-status`
- `year-activation-candidates`
- `proposed-source-gap-evidence`
- `counter-indicators-and-limits`

### Report mapping

| Output obligation | Existing report field |
| --- | --- |
| `target-and-prerequisites` | `timeline` |
| `selected-luck-pillar` | `timeline` |
| `luck-to-natal-candidates` | `timeline` |
| `annual-fact-status` | `timeline` |
| `year-activation-candidates` | `timeline` |
| `proposed-source-gap-evidence` | `limitations` |
| `counter-indicators-and-limits` | `limitations` |

Preserve supporting, counter, conflict, and unavailable states separately. Never fill an unavailable prerequisite from memory or source narrative.

### Safety policy

- Do not activate methodology outside `bazi.school.ziping-structure.v1` or the method cards explicitly declared in `requires`.
- Do not present death, financial, incarceration, legal, or medical claims as any outcomes.
- Do not perform cross-school mixing from undeclared methods.
- Do not perform deterministic outcome from timing evidence.
- Do not perform diagnosis, prognosis, or treatment from timing evidence.
- Do not perform numeric outcome scoring from timing evidence.
- Do not perform personality or destiny assertion from timing evidence.
- Do not perform professional advice from timing evidence.
- Do not perform remediation or purchase prescription from timing evidence.
- Do not perform retrospective fitting from known events.

### Source locators and revisions

- Source `jinchenma94-bazi-skill`
  - Locator: `references/dayun-rules.md#L64-L79`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Ten-year ranges are consumed from canonical calculator facts; the source example is not used as an outcome template.
- Source `jinchenma94-bazi-skill`
  - Locator: `references/dayun-rules.md#L86-L94`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Natal, luck, and annual layering is retained as procedure while favorable-adverse labels and event forecasts are excluded.
- Source `jinchenma94-bazi-skill`
  - Locator: `references/dayun-rules.md#L95-L98`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Disputed split-decade handling remains a separate unresolved position and is not adopted by this timing card.
- Source `jinchenma94-bazi-skill`
  - Locator: `references/dayun-rules.md#L99-L99`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Luck-to-natal heavenly-stem combination and control plus branch combination and clash become occurrence-aware candidate lookups without favorable, adverse, or event labels.
- Source `jinchenma94-bazi-skill`
  - Locator: `references/wuxing-tables.md#L14-L33`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Exact canonical stem-to-element identities supply the mechanical operands for the heavenly-stem control lookup without adding direction, season, personality, or outcome meanings.
- Source `jinchenma94-bazi-skill`
  - Locator: `references/wuxing-tables.md#L53-L64`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Exact stem-combination pairs support occurrence-aware candidate lookup only; transformation and life-event meanings remain unconfirmed.
- Source `jinchenma94-bazi-skill`
  - Locator: `references/wuxing-tables.md#L65-L68`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Exact branch clashes support occurrence-aware timing candidates without adverse or event meanings.
- Source `jinchenma94-bazi-skill`
  - Locator: `references/wuxing-tables.md#L69-L76`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Complete trines require all three distinct occurrence sources; half-trine force and transformation are excluded.
- Source `jinchenma94-bazi-skill`
  - Locator: `references/wuxing-tables.md#L86-L88`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Exact branch combinations support occurrence-aware timing candidates while disputed associated elements remain metadata only.
- Source `jinchenma94-bazi-skill`
  - Locator: `references/wuxing-tables.md#L89-L94`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Exact triple, pair, and self-punishment families support multiplicity-aware candidate matching without adverse labels.
- Source `jinchenma94-bazi-skill`
  - Locator: `references/wuxing-tables.md#L95-L99`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Exact harm pairs support occurrence-aware lookup; destruction is omitted and therefore cannot be a source-backed activation.
- Source `jinchenma94-bazi-skill`
  - Locator: `references/wuxing-tables.md#L128-L133`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: The exact five-element control cycle supplies directional controller and controlled roles without favorable, adverse, causal, or event labels.

**End method card:** `bazi.method.timing.v1`

# Default profile when no explicit override: `bazi.school.strength-balancing.v1`

Apply these cards in the declared order below only when this profile is selected. This opt-in profile is isolated; do not merge cards from another profile.

## Profile source locators and revisions

- Source `jinchenma94-bazi-skill`
  - Locator: `references/classical-texts.md#L61-L67`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Support and assistance remain qualitative evidence dimensions without numeric weights or categorical thresholds; root status is unavailable because no reviewed emitted fact establishes it.
- Source `jinchenma94-bazi-skill`
  - Locator: `references/classical-texts.md#L89-L93`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Strength balancing remains an opt-in proposed position in the unresolved useful-god dispute.

## Method card `bazi.method.strength-balancing.v1`

- Method card ID: `bazi.method.strength-balancing.v1`
- School profile ID: `bazi.school.strength-balancing.v1`
- Topic: `strength-balancing`
- Version: `1`
- Status: `school-specific`

### Requires

- `bazi.school.strength-balancing.v1`
- `bazi.ten-god.friend`
- `bazi.ten-god.rob-wealth`
- `bazi.ten-god.eating-god`
- `bazi.ten-god.hurting-officer`
- `bazi.ten-god.indirect-wealth`
- `bazi.ten-god.direct-wealth`
- `bazi.ten-god.seven-killings`
- `bazi.ten-god.direct-officer`
- `bazi.ten-god.indirect-resource`
- `bazi.ten-god.direct-resource`

### Workflow

1. Require schemaVersion === omds.bazi-profile.v1, BaziProfile.system === bazi, BaziProfile.schoolProfileId === bazi.school.ziping-structure.v1, exactly four ordered pillars, a canonical dayMasterId equal to the day stemId, and non-empty provenance. Require a validated MethodSelectionContext with calculationConventionSchoolProfileId === BaziProfile.schoolProfileId and selectedMethodSchoolProfileId === bazi.school.strength-balancing.v1. If any fact or selection gate fails, return this card as unavailable; never switch to or combine another method school.
2. Expand emitted Ten Gods into occurrence records with the contract exactly: NON_DAY_VISIBLE_TEN_GOD:=tenGodIds[0]; NON_DAY_HIDDEN_TEN_GOD[index]:=tenGodIds[index+1] aligned to hiddenStemIds[index]; DAY_HIDDEN_TEN_GOD[index]:=tenGodIds[index] because the day master has no visible Ten God entry. Preserve duplicate identities at visible and hidden positions as separate evidence; do not deduplicate or turn frequency into a score.
3. Use BALANCE_GROUP_MAP exactly: SUPPORT_RESOURCE:=bazi.ten-god.direct-resource+bazi.ten-god.indirect-resource; SUPPORT_PEER:=bazi.ten-god.friend+bazi.ten-god.rob-wealth; OUTPUT_DRAIN:=bazi.ten-god.eating-god+bazi.ten-god.hurting-officer; CONTROL_PRESSURE:=bazi.ten-god.direct-officer+bazi.ten-god.seven-killings; CONTROLLED_WEALTH:=bazi.ten-god.direct-wealth+bazi.ten-god.indirect-wealth. Keep every occurrence's pillar position and visible-or-hidden origin.
4. Build three separate evidence fields without numeric weights. DAY_MASTER_HIDDEN_OCCURRENCES:=hiddenStemId === dayMasterId records exact hidden identity and position only, never a root conclusion. PEER_RESOURCE_ASSISTANCE_OCCURRENCES:=tenGodId in SUPPORT_PEER|SUPPORT_RESOURCE records each visible or hidden assistance occurrence with origin. ROOT_STATUS:=unavailable because BaziProfile emits no reviewed root fact and the life-stage/root table is excluded. Enforce CASE_RESOURCE_ONLY_HIDDEN:=hiddenStem tenGodId in SUPPORT_RESOURCE=>assistance-evidence,not-root; the same boundary applies to peer assistance, repeated IDs, and exact day-master hidden occurrences.
5. Apply only bazi.method.useful-god.balance in this profile. Compare SUPPORT_RESOURCE plus SUPPORT_PEER beside OUTPUT_DRAIN, CONTROL_PRESSURE, and CONTROLLED_WEALTH qualitatively as an evidence inventory, not as a classifier or threshold. Structure, climate adjustment, and bridging are prohibited alternative positions, not confirming votes or fallback procedures.
6. Do not infer an ordinary strong, weak, balanced, or mixed category in this card: ordinary or mixed evidence=>unresolved. Activation requires a condition established by a separate reviewed method rather than occurrence counts or an invented threshold. Encode the only pinned extreme cases exactly: EXTREME_STRONG_CONDITION:=separately-established-reviewed; EXTREME_STRONG=>OUTPUT_DRAIN and explicitly not CONTROL_PRESSURE. EXTREME_WEAK_CONDITION:=separately-established-reviewed; EXTREME_WEAK=>SUPPORT_RESOURCE and explicitly not SUPPORT_PEER. If neither exact condition is established, return no balance candidate.
7. Counter-check the candidate against the month branch, every visible stem, every hidden stem, duplicated occurrences, separate assistance evidence, ROOT_STATUS:=unavailable, relationFacts with shared participants, time-basis assumptions, missing hour confidence, and the unresolved useful-god dispute. Associated relation elements and transformedElementId === null cannot manufacture support, root status, or transformation.
8. Return the verified calculation-and-selection gate, occurrence ledger, day-master hidden occurrences, peer/resource assistance occurrences, unavailable root status, qualitative support-versus-drain inventory, separately established extreme-condition status or unresolved status, exact permitted candidate if any, counter-evidence, prohibited alternative lenses, sources, and limits. ChatGPT may explain this school procedure reflectively, but neither this card nor the server emits or derives root status, a strength threshold, useful-god, personality, domain, or event conclusion.
9. This workflow implements bazi.claim.strength-balancing-evidence.v1, approved by the normalization-safety-review at revision task-1-claim-rule-review.2026-09-03 (standards/reviews/bazi/strength-balancing-claim-rules.yaml).

### Supporting indicators

- None declared.

### Counter-indicators

- None declared.

### Output obligations

- `calculation-and-selection-gate`
- `visible-and-hidden-occurrences`
- `day-master-hidden-occurrences`
- `peer-resource-assistance`
- `root-status-unavailable`
- `qualitative-evidence-inventory`
- `extreme-condition-and-candidate-or-unresolved`
- `counter-evidence-and-limits`

### Report mapping

| Output obligation | Existing report field |
| --- | --- |
| `calculation-and-selection-gate` | `structuralDiagnosis` |
| `visible-and-hidden-occurrences` | `structuralDiagnosis` |
| `day-master-hidden-occurrences` | `structuralDiagnosis` |
| `peer-resource-assistance` | `structuralDiagnosis` |
| `root-status-unavailable` | `limitations` |
| `qualitative-evidence-inventory` | `structuralDiagnosis` |
| `extreme-condition-and-candidate-or-unresolved` | `structuralDiagnosis` |
| `counter-evidence-and-limits` | `limitations` |

Preserve supporting, counter, conflict, and unavailable states separately. Never fill an unavailable prerequisite from memory or source narrative.

### Safety policy

- Do not activate methodology outside `bazi.school.strength-balancing.v1` or the method cards explicitly declared in `requires`.
- Do not present death, financial, incarceration, legal, or medical claims as any outcomes.
- Do not perform cross-school mixing from undeclared methods.
- Do not perform deterministic outcome from strength-balancing evidence.
- Do not perform diagnosis, prognosis, or treatment from strength-balancing evidence.
- Do not perform numeric outcome scoring from strength-balancing evidence.
- Do not perform personality or destiny assertion from strength-balancing evidence.
- Do not perform professional advice from strength-balancing evidence.
- Do not perform remediation or purchase prescription from strength-balancing evidence.
- Do not perform retrospective fitting from known events.

### Source locators and revisions

- Source `jinchenma94-bazi-skill`
  - Locator: `references/classical-texts.md#L61-L67`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Exact hidden day-master occurrences and peer/resource assistance are kept separate; root status remains unavailable because the required life-stage rule is excluded, and categorical strength and outcome claims are not imported.
- Source `jinchenma94-bazi-skill`
  - Locator: `references/classical-texts.md#L68-L71`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Only the source's two explicit extreme cases are retained behind separately established reviewed conditions; ordinary thresholds are not inferred and bridging remains a separate unresolved position.
- Source `jinchenma94-bazi-skill`
  - Locator: `references/wuxing-tables.md#L100-L112`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Ten God derivation groups support explicit occurrence classification, while personality and social-role meanings are excluded.
- Source `jinchenma94-bazi-skill`
  - Locator: `references/wuxing-tables.md#L128-L133`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Five-element generation and control cycles support qualitative counter-checks without outcome interpretation.
- Source `jinchenma94-bazi-skill`
  - Locator: `references/wuxing-tables.md#L157-L173`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Hidden-stem identity and order support exact occurrence records only, not root status; the following approximate percentage weights are excluded from the method.
- Source `jinchenma94-bazi-method-authority.strength-balancing`
  - Locator: `references/classical-texts.md#L61-L67`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Owner-attested method authority backing bazi.claim.strength-balancing-evidence.v1 (standards/reviews/bazi/strength-balancing-claim-rules.yaml).

**End method card:** `bazi.method.strength-balancing.v1`

# Explicit override profile: `bazi.school.climate-adjustment.v1`

Apply these cards in the declared order below only when this profile is selected. This opt-in profile is isolated; do not merge cards from another profile.

## Profile source locators and revisions

- Source `jinchenma94-bazi-skill`
  - Locator: `references/classical-texts.md#L16-L24`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Climate-adjustment conditions are retained as questions about explicit seasonal facts, not as universal element prescriptions or promised outcomes.
- Source `jinchenma94-bazi-skill`
  - Locator: `references/classical-texts.md#L89-L93`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Climate adjustment remains an opt-in proposed position in the unresolved useful-god dispute.

## Method card `bazi.method.climate-adjustment.v1`

- Method card ID: `bazi.method.climate-adjustment.v1`
- School profile ID: `bazi.school.climate-adjustment.v1`
- Topic: `climate-adjustment`
- Version: `1`
- Status: `school-specific`

### Requires

- `bazi.school.climate-adjustment.v1`
- `common.element.wood`
- `common.element.fire`
- `common.element.earth`
- `common.element.metal`
- `common.element.water`
- `common.stem.jia`
- `common.stem.yi`
- `common.stem.bing`
- `common.stem.ding`
- `common.stem.wu`
- `common.stem.ji`
- `common.stem.geng`
- `common.stem.xin`
- `common.stem.ren`
- `common.stem.gui`
- `common.branch.zi`
- `common.branch.chou`
- `common.branch.yin`
- `common.branch.mao`
- `common.branch.chen`
- `common.branch.si`
- `common.branch.wu`
- `common.branch.wei`
- `common.branch.shen`
- `common.branch.you`
- `common.branch.xu`
- `common.branch.hai`

### Workflow

1. Require schemaVersion === omds.bazi-profile.v1, BaziProfile.system === bazi, BaziProfile.schoolProfileId === bazi.school.ziping-structure.v1, exactly four ordered pillars, dayMasterId equal to the day stemId, a month branch, complete visible and hidden stem IDs, and non-empty provenance. Require a validated MethodSelectionContext with calculationConventionSchoolProfileId === BaziProfile.schoolProfileId and selectedMethodSchoolProfileId === bazi.school.climate-adjustment.v1. If any fact or selection gate fails, return this card as unavailable; never borrow or combine structure or strength-balancing output.
2. Construct a climate evidence inventory from emitted facts only. Use STEM_ELEMENT_MAP exactly: common.stem.jia|common.stem.yi=>common.element.wood, common.stem.bing|common.stem.ding=>common.element.fire, common.stem.wu|common.stem.ji=>common.element.earth, common.stem.geng|common.stem.xin=>common.element.metal, common.stem.ren|common.stem.gui=>common.element.water. Preserve pillar position and visible-or-hidden origin without scores or percentage weights.
3. Use BRANCH_SEASON_MAP exactly for the month branch: common.branch.yin|common.branch.mao|common.branch.chen=>spring, common.branch.si|common.branch.wu|common.branch.wei=>summer, common.branch.shen|common.branch.you|common.branch.xu=>autumn, common.branch.hai|common.branch.zi|common.branch.chou=>winter. This is a lookup for source conditions, not a temperature measurement, diagnosis, or conclusion that an element is strong.
4. Use SOURCE_BACKED_CLIMATE_CONDITIONS exactly: summer fire strong=>inspect common.element.water; winter water strong=>inspect common.element.fire. BaziProfile does not emit a strong-fire or strong-water conclusion, so report these generic conditions as unavailable unless a separately reviewed deterministic fact establishes the stated condition; month season or occurrence count alone cannot satisfy it.
5. Use SOURCE_BACKED_EXAMPLES exactly and only when dayMasterId plus month branch match: common.stem.jia+common.branch.yin=>common.stem.bing then common.stem.gui; common.stem.jia+common.branch.you=>common.stem.ding then common.stem.bing; common.stem.geng+common.branch.zi=>common.stem.bing then common.stem.jia then common.stem.ding. Preserve listed order as source order, then mark each candidate present-visible, present-hidden, absent, or conflicted from the evidence inventory.
6. For every other day-stem and month-branch pair, record mapping unavailable and do not extrapolate a twelve-month table, interpolate from element cycles, substitute a similar season, or use an LLM's remembered rule. Absence of a listed stem is an evidence status, not a recommendation to add, buy, wear, name, locate, or ritually remedy anything.
7. Apply only bazi.method.useful-god.climate-adjustment. Keep structure, strength balancing, and bridging as prohibited parallel positions in the unresolved dispute; do not combine their candidates, count agreement, rank the four positions, or claim that this opt-in school is default truth.
8. Counter-check exact input basis, source coverage, visible and hidden candidate occurrence, relationFacts, transformedElementId === null, missing time details, and competing source conditions. Return the profile gate, season lookup, exact matched rule or mapping unavailable, candidate occurrence evidence, counter-evidence, dispute status, provenance, and limits without a climate, useful-god, domain, or event conclusion.
9. This workflow implements bazi.claim.climate-adjustment-lookup.v1, approved by the normalization-safety-review at revision task-1-claim-rule-review.2026-09-03 (standards/reviews/bazi/climate-adjustment-claim-rules.yaml).

### Supporting indicators

- None declared.

### Counter-indicators

- None declared.

### Output obligations

- `profile-and-source-gate`
- `month-season-and-element-inventory`
- `matched-source-rule-or-unavailable`
- `candidate-occurrence-evidence`
- `unresolved-dispute`
- `counter-evidence-and-limits`

### Report mapping

| Output obligation | Existing report field |
| --- | --- |
| `profile-and-source-gate` | `structuralDiagnosis` |
| `month-season-and-element-inventory` | `structuralDiagnosis` |
| `matched-source-rule-or-unavailable` | `structuralDiagnosis` |
| `candidate-occurrence-evidence` | `structuralDiagnosis` |
| `unresolved-dispute` | `limitations` |
| `counter-evidence-and-limits` | `limitations` |

Preserve supporting, counter, conflict, and unavailable states separately. Never fill an unavailable prerequisite from memory or source narrative.

### Safety policy

- Do not activate methodology outside `bazi.school.climate-adjustment.v1` or the method cards explicitly declared in `requires`.
- Do not present death, financial, incarceration, legal, or medical claims as any outcomes.
- Do not perform cross-school mixing from undeclared methods.
- Do not perform deterministic outcome from climate-adjustment evidence.
- Do not perform diagnosis, prognosis, or treatment from climate-adjustment evidence.
- Do not perform numeric outcome scoring from climate-adjustment evidence.
- Do not perform personality or destiny assertion from climate-adjustment evidence.
- Do not perform professional advice from climate-adjustment evidence.
- Do not perform remediation or purchase prescription from climate-adjustment evidence.
- Do not perform retrospective fitting from known events.

### Source locators and revisions

- Source `jinchenma94-bazi-skill`
  - Locator: `references/wuxing-tables.md#L14-L33`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Exact stem element identities support the card's closed evidence inventory without importing directions, personality, or seasonal destiny claims.
- Source `jinchenma94-bazi-skill`
  - Locator: `references/wuxing-tables.md#L34-L52`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Exact branch element and month identities support a season lookup without using zodiac, colloquial time, or interpretive attributes.
- Source `jinchenma94-bazi-skill`
  - Locator: `references/classical-texts.md#L16-L24`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: The two generic seasonal conditions are retained only as conditional inspections because the profile does not emit a strength conclusion.
- Source `jinchenma94-bazi-skill`
  - Locator: `references/classical-texts.md#L25-L31`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Three examples become closed exact lookup cases; promised outcomes, medicinal metaphors, and a fabricated complete table are excluded.
- Source `jinchenma94-bazi-method-authority.climate-adjustment`
  - Locator: `references/wuxing-tables.md#L14-L33`
  - Revision: `112a5d84cd1a001a0038cafca3be68d93e4c0cc9`
  - Normalization note: Owner-attested method authority backing bazi.claim.climate-adjustment-lookup.v1 (standards/reviews/bazi/climate-adjustment-claim-rules.yaml).

**End method card:** `bazi.method.climate-adjustment.v1`
