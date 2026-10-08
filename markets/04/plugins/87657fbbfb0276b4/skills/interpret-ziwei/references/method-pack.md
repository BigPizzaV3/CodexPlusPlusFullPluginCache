# ZIWEI method pack

This procedure-only reference is generated from reviewed OMDS school profiles and method cards. Returned canonical facts remain authoritative; source notes do not supply missing facts or interpretations.

# Selected profile: `ziwei.school.zhongzhou.v1`

Apply these cards in the declared order below only when this profile is selected. This default profile is isolated; do not merge cards from another profile.

## Profile source locators and revisions

- Source `linden-ziwei-doushu-skill`
  - Locator: `README.md#L69-L78`
  - Revision: `a842dd65dabdc4ce42ec9688b88ae876858a9977`
  - Normalization note: Zhongzhou wholeness and evidence-chain principles are adapted as the default method pack; other named schools require separate explicit selection.
- Source `linden-ziwei-doushu-skill`
  - Locator: `SKILL.md#L50-L73`
  - Revision: `a842dd65dabdc4ce42ec9688b88ae876858a9977`
  - Normalization note: The source's Zhongzhou-first declaration supports the school boundary, while mixed-school auxiliary use is rejected unless a separate reviewed profile is selected.

## Method card `ziwei.method.verify-chart.v1`

- Method card ID: `ziwei.method.verify-chart.v1`
- School profile ID: `ziwei.school.zhongzhou.v1`
- Topic: `verify-chart`
- Version: `1`
- Status: `school-specific`

### Requires

- `ziwei.school.zhongzhou.v1`

### Workflow

1. First verify deterministic chart and time basis: require schemaVersion === omds.ziwei-profile.v1, system === ziwei, schoolProfileId === ziwei.school.zhongzhou.v1, exactly twelve palaces, one life palace, one body palace, and non-empty provenance. Stop as unavailable rather than repairing a mismatch.
2. Require a validated method-selection context whose calculation convention and selected method school are both ziwei.school.zhongzhou.v1. Treat a different selected school as an isolated pack, never as permission to merge its rules into this workflow.
3. Verify every palace has canonical palaceId, stemId, branchId, oppositePalaceId, two trinePalaceIds, and a star array. Verify lifePalaceId and bodyPalaceId resolve to the flagged palaces; retain all conflicts instead of choosing a preferred value.
4. Inspect assumptions and provenance for the actual calendar, birth-time boundary, and calculation-library revision. The display metadata is non-canonical audit context only; do not reconstruct a chart, infer true-solar correction, or replace canonical facts from a display label.
5. Report missing timezone, place, longitude, minute precision, or correction evidence only as missing time-basis context when applicable. The deterministic calculator result remains authoritative for its declared convention, while unsupported alternate conventions remain unavailable.
6. Apply MAJOR_CLAIM_GATE:=at-least-two-distinct-methodological-indicator-groups+explicit-counter-indicator-check. Distinct groups mean separately retrieved chart structures and not statistical independence; verification alone satisfies no life claim, and insufficient or conflicting evidence must remain explicit.
7. Apply QUALIFYING_SUPPORT_GROUP:=group.status===SUPPORTING and CONFLICT_GROUP:=retain-for-disclosure-and-counter-review+exclude-from-supporting-group-count. A group containing any classified counter alongside support remains conflict and cannot satisfy the major-claim threshold.
8. Emit envelope integrity, palace integrity, time-basis evidence, provenance, conflicts, missing inputs, and the gate to global analysis. Do not infer a personality, profession, domain outcome, event, or temporal outcome from successful verification.

### Supporting indicators

- None declared.

### Counter-indicators

- None declared.

### Output obligations

- `envelope-integrity`
- `palace-integrity`
- `time-basis`
- `provenance`
- `conflicts-and-limits`

### Report mapping

| Output obligation | Existing report field |
| --- | --- |
| `envelope-integrity` | `structuralDiagnosis` |
| `palace-integrity` | `structuralDiagnosis` |
| `time-basis` | `structuralDiagnosis` |
| `provenance` | `structuralDiagnosis` |
| `conflicts-and-limits` | `limitations` |

Preserve supporting, counter, conflict, and unavailable states separately. Never fill an unavailable prerequisite from memory or source narrative.

### Safety policy

- Do not activate methodology outside `ziwei.school.zhongzhou.v1` or the method cards explicitly declared in `requires`.
- Do not present accident-injury, death, financial, incarceration, legal, medical, or self-harm claims as any outcomes.
- Do not perform cross-school mixing from undeclared methods.
- Do not perform deterministic outcome from verify-chart evidence.
- Do not perform diagnosis, prognosis, or treatment from verify-chart evidence.
- Do not perform numeric outcome scoring from verify-chart evidence.
- Do not perform professional advice from verify-chart evidence.
- Do not perform remediation or purchase prescription from verify-chart evidence.
- Do not perform retrospective fitting from known events.
- Do not perform single-indicator conclusion from verify-chart evidence.

### Source locators and revisions

- Source `linden-ziwei-doushu-skill`
  - Locator: `SKILL.md#L83-L99`
  - Revision: `a842dd65dabdc4ce42ec9688b88ae876858a9977`
  - Normalization note: Input collection and confirmation are adapted into fact-availability checks without importing the upstream MCP contract or performing alternate chart calculation.
- Source `linden-ziwei-doushu-skill`
  - Locator: `SKILL.md#L287-L292`
  - Revision: `a842dd65dabdc4ce42ec9688b88ae876858a9977`
  - Normalization note: The source's evidence, uncertainty, and non-alarmist requirements become explicit integrity and limitation outputs; no interpretation is performed by this card.

**End method card:** `ziwei.method.verify-chart.v1`

## Method card `ziwei.method.global-star-system.v1`

- Method card ID: `ziwei.method.global-star-system.v1`
- School profile ID: `ziwei.school.zhongzhou.v1`
- Topic: `global-star-system`
- Version: `1`
- Status: `school-specific`

### Requires

- `ziwei.school.zhongzhou.v1`

### Workflow

1. After verification, inspect the whole star system before any target palace. Build GLOBAL_STAR_INVENTORY from every ZiweiProfile.palaces entry and every ZiweiStarFact, retaining palaceId, starId, typeId, scopeId, brightnessId, and transformationId without labels as identity.
2. Partition evidence methodologically as SAME_PALACE_CONFIGURATIONS, LIFE_BODY_AXIS, PALACE_NETWORKS, and TRANSFORMATION_OCCURRENCES. These are retrieval groups for later comparison, not calculated interpretations and not statistical samples.
3. Preserve every major, minor, and adjective star occurrence. Do not rank a star by label, count a repeated star as independent corroboration, or infer a traditional star system that is not explicitly represented by canonical occurrence relationships.
4. Record brightness only where brightnessId is non-null, and transformation only where transformationId is non-null. Missing brightness or transformation is unavailable evidence, not a weak, neutral, adverse, or absent influence.
5. Apply MAJOR_CLAIM_GATE:=at-least-two-distinct-methodological-indicator-groups+explicit-counter-indicator-check. The groups are not statistical independence; two stars in the same palace configuration remain one group, and conflicts or unavailable groups cannot be silently counted as support.
6. Apply QUALIFYING_SUPPORT_GROUP:=group.status===SUPPORTING and CONFLICT_GROUP:=retain-for-disclosure-and-counter-review+exclude-from-supporting-group-count. Keep every supporting and counter occurrence inside a conflict group for audit, but never count that group toward the gate.
7. Produce a whole-chart inventory and a neutral map of supporting, countering, conflicting, and unavailable evidence before selecting any requested palace or domain. No source prose may supply a missing star fact, relation, strength, pattern, or outcome.
8. Pass only canonical occurrence groups, provenance, conflicts, and unavailable evidence to the Life-Body card. Do not issue a personality, profession, destiny, domain, or event conclusion from one star, one palace, a raw count, or a remembered pattern.
9. This workflow implements ziwei.claim.global-star-system.v1, approved by the normalization-safety-review at revision task-1-claim-rule-review.2026-09-04 (standards/reviews/ziwei/zhongzhou-domain-claim-rules.yaml).

### Supporting indicators

- None declared.

### Counter-indicators

- None declared.

### Output obligations

- `whole-chart-inventory`
- `methodological-evidence-groups`
- `brightness-and-transformations`
- `supporting-and-counter-evidence`
- `conflicts-and-unavailable-evidence`

### Report mapping

| Output obligation | Existing report field |
| --- | --- |
| `whole-chart-inventory` | `structuralDiagnosis` |
| `methodological-evidence-groups` | `structuralDiagnosis` |
| `brightness-and-transformations` | `structuralDiagnosis` |
| `supporting-and-counter-evidence` | `structuralDiagnosis` |
| `conflicts-and-unavailable-evidence` | `limitations` |

Preserve supporting, counter, conflict, and unavailable states separately. Never fill an unavailable prerequisite from memory or source narrative.

### Safety policy

- Do not activate methodology outside `ziwei.school.zhongzhou.v1` or the method cards explicitly declared in `requires`.
- Do not present accident-injury, death, financial, incarceration, legal, medical, or self-harm claims as any outcomes.
- Do not perform cross-school mixing from undeclared methods.
- Do not perform deterministic outcome from global-star-system evidence.
- Do not perform diagnosis, prognosis, or treatment from global-star-system evidence.
- Do not perform numeric outcome scoring from global-star-system evidence.
- Do not perform professional advice from global-star-system evidence.
- Do not perform remediation or purchase prescription from global-star-system evidence.
- Do not perform retrospective fitting from known events.
- Do not perform single-indicator conclusion from global-star-system evidence.

### Source locators and revisions

- Source `linden-ziwei-doushu-skill`
  - Locator: `SKILL.md#L130-L150`
  - Revision: `a842dd65dabdc4ce42ec9688b88ae876858a9977`
  - Normalization note: The global-before-local order is adapted, while named source patterns and their outcome meanings are withheld unless separately normalized into canonical procedures.
- Source `linden-ziwei-doushu-skill`
  - Locator: `references/xingyao.md#L617-L626`
  - Revision: `a842dd65dabdc4ce42ec9688b88ae876858a9977`
  - Normalization note: Interaction principles are narrowed to whole-chart evidence retrieval, per-star brightness preservation, and non-isolated analysis without adopting positive star meanings.
- Source `linden-ziwei-method-authority`
  - Locator: `SKILL.md#L130-L150`
  - Revision: `a842dd65dabdc4ce42ec9688b88ae876858a9977`
  - Normalization note: Owner-attested method authority backing ziwei.claim.global-star-system.v1 (standards/reviews/ziwei/zhongzhou-domain-claim-rules.yaml).

**End method card:** `ziwei.method.global-star-system.v1`

## Method card `ziwei.method.life-body-axis.v1`

- Method card ID: `ziwei.method.life-body-axis.v1`
- School profile ID: `ziwei.school.zhongzhou.v1`
- Topic: `life-body-axis`
- Version: `1`
- Status: `school-specific`

### Requires

- `ziwei.school.zhongzhou.v1`
- `ziwei.palace.life`

### Workflow

1. After the whole-chart inventory, evaluate the Life-Body axis. Resolve LIFE_PALACE by lifePalaceId and isLifePalace === true, and BODY_PALACE by bodyPalaceId and isBodyPalace === true; a missing, duplicate, or mismatched resolution is a conflict that stops this card.
2. Inventory both palaces independently with their canonical branchId, stemId, stars, oppositePalaceId, and trinePalaceIds. If lifePalaceId === bodyPalaceId, preserve co-location as one structural fact rather than inventing two independent indicators.
3. Evaluate the Life-Body axis only as a relationship between two deterministic palace records. Do not assign innate or acquired personality meanings, age thresholds, strength labels, or life-purpose claims absent from ZiweiProfile.
4. Carry forward same-palace star configurations, non-null brightness and transformations, plus each palace network as separate methodological groups. Repeated star IDs, shared network palaces, and co-located Life-Body facts must be disclosed as overlap.
5. Apply MAJOR_CLAIM_GATE:=at-least-two-distinct-methodological-indicator-groups+explicit-counter-indicator-check. This is not statistical independence; overlapping facts cannot satisfy two groups, and conflict, missing axis facts, or unavailable counter-evidence keeps synthesis insufficient.
6. Apply QUALIFYING_SUPPORT_GROUP:=group.status===SUPPORTING and CONFLICT_GROUP:=retain-for-disclosure-and-counter-review+exclude-from-supporting-group-count. Preserve conflict occurrences across the axis, but only a resolved supporting group may qualify for the threshold.
7. Compare supporting and counter-indicators across the axis without collapsing disagreement. Record which exact canonical occurrences support, counter, conflict with, or leave unavailable any bounded observation; never infer from palace or star names alone.
8. Emit axis integrity, Life palace evidence, Body palace evidence, overlap disclosure, supporting and counter-evidence, and limits. Then pass the resolved target candidates to palace-network analysis without forming a person-level verdict.
9. This workflow implements ziwei.claim.life-body-axis.v1, approved by the normalization-safety-review at revision task-1-claim-rule-review.2026-09-04 (standards/reviews/ziwei/zhongzhou-domain-claim-rules.yaml).

### Supporting indicators

- None declared.

### Counter-indicators

- None declared.

### Output obligations

- `axis-integrity`
- `life-palace-evidence`
- `body-palace-evidence`
- `overlap-and-dependencies`
- `supporting-counter-and-limits`

### Report mapping

| Output obligation | Existing report field |
| --- | --- |
| `axis-integrity` | `structuralDiagnosis` |
| `life-palace-evidence` | `structuralDiagnosis` |
| `body-palace-evidence` | `structuralDiagnosis` |
| `overlap-and-dependencies` | `structuralDiagnosis` |
| `supporting-counter-and-limits` | `structuralDiagnosis` |

Preserve supporting, counter, conflict, and unavailable states separately. Never fill an unavailable prerequisite from memory or source narrative.

### Safety policy

- Do not activate methodology outside `ziwei.school.zhongzhou.v1` or the method cards explicitly declared in `requires`.
- Do not present accident-injury, death, financial, incarceration, legal, medical, or self-harm claims as any outcomes.
- Do not perform cross-school mixing from undeclared methods.
- Do not perform deterministic outcome from life-body-axis evidence.
- Do not perform diagnosis, prognosis, or treatment from life-body-axis evidence.
- Do not perform numeric outcome scoring from life-body-axis evidence.
- Do not perform professional advice from life-body-axis evidence.
- Do not perform remediation or purchase prescription from life-body-axis evidence.
- Do not perform retrospective fitting from known events.
- Do not perform single-indicator conclusion from life-body-axis evidence.

### Source locators and revisions

- Source `linden-ziwei-doushu-skill`
  - Locator: `SKILL.md#L130-L150`
  - Revision: `a842dd65dabdc4ce42ec9688b88ae876858a9977`
  - Normalization note: The source identifies Life and Body as global skeleton inputs; the card retains only their emitted canonical palace relationship and excludes personality meanings.
- Source `linden-ziwei-doushu-skill`
  - Locator: `references/gongwei.md#L257-L264`
  - Revision: `a842dd65dabdc4ce42ec9688b88ae876858a9977`
  - Normalization note: The non-isolation principle is adapted to require palace-network evidence; age, causality, ranking, and unavailable palace theories in the same range are not adopted.
- Source `linden-ziwei-method-authority`
  - Locator: `SKILL.md#L130-L150`
  - Revision: `a842dd65dabdc4ce42ec9688b88ae876858a9977`
  - Normalization note: Owner-attested method authority backing ziwei.claim.life-body-axis.v1 (standards/reviews/ziwei/zhongzhou-domain-claim-rules.yaml).

**End method card:** `ziwei.method.life-body-axis.v1`

## Method card `ziwei.method.palace-network.v1`

- Method card ID: `ziwei.method.palace-network.v1`
- School profile ID: `ziwei.school.zhongzhou.v1`
- Topic: `palace-network`
- Version: `1`
- Status: `school-specific`

### Requires

- `ziwei.school.zhongzhou.v1`
- `ziwei.palace-relation.opposite`
- `ziwei.palace-relation.trine`

### Workflow

1. After Life-Body evaluation, choose a target only from an explicit user question or from a prior named analysis scope. If no unambiguous target palace is available, record target selection unavailable rather than mapping a domain from memory.
2. Evaluate the target palace with its oppositePalaceId and both trinePalaceIds. Construct PALACE_NETWORK:=target.palaceId+target.oppositePalaceId+target.trinePalaceIds[0]+target.trinePalaceIds[1], resolve all members from ZiweiProfile.palaces, and require exactly four distinct palaceId values.
3. Treat target.oppositePalaceId as ziwei.palace-relation.opposite and both target.trinePalaceIds as ziwei.palace-relation.trine. Use the emitted IDs directly; do not reconstruct the network from labels, assumed fixed palace names, branch arithmetic, or source prose.
4. Inventory each network member's star facts, brightness, transformations, and Life-Body flags. Preserve provenance and overlap with previous groups, and never convert the relation itself into support, opposition, benefit, harm, causality, or an event.
5. Compare same-palace evidence with opposite and trine evidence as methodological groups, then retrieve explicit counter-evidence from every network member. Contradictory occurrences remain side by side; absence of a star or transformation is not automatically a counter-indicator.
6. Apply MAJOR_CLAIM_GATE:=at-least-two-distinct-methodological-indicator-groups+explicit-counter-indicator-check. The grouping is not statistical independence; target plus opposite does not count twice when both observations derive from the same star occurrence or unsupported meaning.
7. Apply QUALIFYING_SUPPORT_GROUP:=group.status===SUPPORTING and CONFLICT_GROUP:=retain-for-disclosure-and-counter-review+exclude-from-supporting-group-count. A target, trine, or opposite group with both statuses stays visible as conflict and does not qualify as support.
8. Emit target selection, the four-member canonical network, per-member evidence, overlap, supporting and counter-evidence, conflicts, and unavailable fields. Pass these facts to transformation analysis without a single-palace or single-star conclusion.
9. This workflow implements ziwei.claim.palace-network.v1, approved by the normalization-safety-review at revision task-1-claim-rule-review.2026-09-04 (standards/reviews/ziwei/zhongzhou-domain-claim-rules.yaml).

### Supporting indicators

- None declared.

### Counter-indicators

- None declared.

### Output obligations

- `target-selection`
- `canonical-palace-network`
- `per-palace-evidence`
- `supporting-and-counter-evidence`
- `overlap-conflicts-and-limits`

### Report mapping

| Output obligation | Existing report field |
| --- | --- |
| `target-selection` | `domainAnalysis` |
| `canonical-palace-network` | `structuralDiagnosis` |
| `per-palace-evidence` | `structuralDiagnosis` |
| `supporting-and-counter-evidence` | `structuralDiagnosis` |
| `overlap-conflicts-and-limits` | `limitations` |

Preserve supporting, counter, conflict, and unavailable states separately. Never fill an unavailable prerequisite from memory or source narrative.

### Safety policy

- Do not activate methodology outside `ziwei.school.zhongzhou.v1` or the method cards explicitly declared in `requires`.
- Do not present accident-injury, death, financial, incarceration, legal, medical, or self-harm claims as any outcomes.
- Do not perform cross-school mixing from undeclared methods.
- Do not perform deterministic outcome from palace-network evidence.
- Do not perform diagnosis, prognosis, or treatment from palace-network evidence.
- Do not perform numeric outcome scoring from palace-network evidence.
- Do not perform professional advice from palace-network evidence.
- Do not perform remediation or purchase prescription from palace-network evidence.
- Do not perform retrospective fitting from known events.
- Do not perform single-indicator conclusion from palace-network evidence.

### Source locators and revisions

- Source `linden-ziwei-doushu-skill`
  - Locator: `SKILL.md#L151-L168`
  - Revision: `a842dd65dabdc4ce42ec9688b88ae876858a9977`
  - Normalization note: Palace analysis is adapted to canonical same-palace, opposite, and trine retrieval; source domain meanings are excluded, and the following verification-signal example is separately quarantined.
- Source `linden-ziwei-doushu-skill`
  - Locator: `references/gongwei.md#L26-L46`
  - Revision: `a842dd65dabdc4ce42ec9688b88ae876858a9977`
  - Normalization note: The mechanical four-member Sanfang Sizheng table supports emitted opposite and trine composition without importing deterministic interpretations attached elsewhere in the source.
- Source `linden-ziwei-doushu-skill`
  - Locator: `references/gongwei.md#L257-L264`
  - Revision: `a842dd65dabdc4ce42ec9688b88ae876858a9977`
  - Normalization note: The non-isolation instruction supports checking the entire emitted network; unsupported layer priority, age rules, and auxiliary schools remain unavailable.
- Source `linden-ziwei-method-authority`
  - Locator: `references/gongwei.md#L26-L46`
  - Revision: `a842dd65dabdc4ce42ec9688b88ae876858a9977`
  - Normalization note: Owner-attested method authority backing ziwei.claim.palace-network.v1 (standards/reviews/ziwei/zhongzhou-domain-claim-rules.yaml).

**End method card:** `ziwei.method.palace-network.v1`

## Method card `ziwei.method.four-transformations.v1`

- Method card ID: `ziwei.method.four-transformations.v1`
- School profile ID: `ziwei.school.zhongzhou.v1`
- Topic: `four-transformations`
- Version: `1`
- Status: `school-specific`

### Requires

- `ziwei.school.zhongzhou.v1`
- `ziwei.transformation.lu`
- `ziwei.transformation.quan`
- `ziwei.transformation.ke`
- `ziwei.transformation.ji`

### Workflow

1. After the palace network, apply same-palace stars, brightness only where facts support it, Four Transformations, and modifiers. Read only canonical ZiweiStarFact records already emitted for the target network and the whole-chart inventory.
2. Construct TRANSFORMATION_OCCURRENCES from every ZiweiStarFact.transformationId that equals ziwei.transformation.lu, ziwei.transformation.quan, ziwei.transformation.ke, or ziwei.transformation.ji, retaining its palaceId and starId. Preserve transformationId === null as unavailable for that occurrence.
3. For each same-palace configuration retain starId, typeId, scopeId, non-null brightnessId, and optional transformationId as separate fact fields. Do not translate a transformation label into resource, power, reputation, pressure, morality, or outcome semantics.
4. Compare transformation occurrences across the full chart before focusing on the target network, and disclose when an occurrence is reused by the global, Life-Body, and palace-network groups. A repeated occurrence is one item of evidence, not multiple confirmations.
5. ZiweiProfile emits natal star transformations but no canonical palace-stem flying path, self-transformation direction, chain, or alternate-school transformation layer. Therefore do not derive flying paths or self-transformations; mark each requested unsupported operation unavailable.
6. Apply MAJOR_CLAIM_GATE:=at-least-two-distinct-methodological-indicator-groups+explicit-counter-indicator-check. The groups are not statistical independence; two transformation occurrences alone remain one transformation group, and missing counter-evidence makes a major claim insufficient.
7. Apply QUALIFYING_SUPPORT_GROUP:=group.status===SUPPORTING and CONFLICT_GROUP:=retain-for-disclosure-and-counter-review+exclude-from-supporting-group-count. Transformation prominence inside a conflict group remains disclosed but cannot turn that group into qualifying support.
8. Emit the natal transformation inventory, same-palace facts, supported brightness, network placement, counter-evidence, conflicts, and unavailable dynamic operations. Do not compute a second chart or import Feixing or Qintian rules into Zhongzhou.
9. This workflow implements ziwei.claim.four-transformations.v1, approved by the normalization-safety-review at revision task-1-claim-rule-review.2026-09-04 (standards/reviews/ziwei/zhongzhou-domain-claim-rules.yaml).

### Supporting indicators

- None declared.

### Counter-indicators

- None declared.

### Output obligations

- `natal-transformation-inventory`
- `same-palace-facts`
- `brightness-and-network-placement`
- `supporting-and-counter-evidence`
- `unavailable-dynamics-and-limits`

### Report mapping

| Output obligation | Existing report field |
| --- | --- |
| `natal-transformation-inventory` | `structuralDiagnosis` |
| `same-palace-facts` | `structuralDiagnosis` |
| `brightness-and-network-placement` | `structuralDiagnosis` |
| `supporting-and-counter-evidence` | `structuralDiagnosis` |
| `unavailable-dynamics-and-limits` | `limitations` |

Preserve supporting, counter, conflict, and unavailable states separately. Never fill an unavailable prerequisite from memory or source narrative.

### Safety policy

- Do not activate methodology outside `ziwei.school.zhongzhou.v1` or the method cards explicitly declared in `requires`.
- Do not present accident-injury, death, financial, incarceration, legal, medical, or self-harm claims as any outcomes.
- Do not perform cross-school mixing from undeclared methods.
- Do not perform deterministic outcome from four-transformations evidence.
- Do not perform diagnosis, prognosis, or treatment from four-transformations evidence.
- Do not perform numeric outcome scoring from four-transformations evidence.
- Do not perform professional advice from four-transformations evidence.
- Do not perform remediation or purchase prescription from four-transformations evidence.
- Do not perform retrospective fitting from known events.
- Do not perform single-indicator conclusion from four-transformations evidence.

### Source locators and revisions

- Source `linden-ziwei-doushu-skill`
  - Locator: `SKILL.md#L173-L190`
  - Revision: `a842dd65dabdc4ce42ec9688b88ae876858a9977`
  - Normalization note: The source's transformation-analysis phase is narrowed to canonical natal transformation occurrence retrieval; meanings, flying paths, and Qintian chains are not adopted.
- Source `linden-ziwei-doushu-skill`
  - Locator: `references/xingyao.md#L617-L626`
  - Revision: `a842dd65dabdc4ce42ec9688b88ae876858a9977`
  - Normalization note: Per-star brightness and transformation inspection is adapted as fact inventory only, with whole-chart context and no positive star or transformation interpretation.
- Source `linden-ziwei-method-authority`
  - Locator: `SKILL.md#L173-L190`
  - Revision: `a842dd65dabdc4ce42ec9688b88ae876858a9977`
  - Normalization note: Owner-attested method authority backing ziwei.claim.four-transformations.v1 (standards/reviews/ziwei/zhongzhou-domain-claim-rules.yaml).

**End method card:** `ziwei.method.four-transformations.v1`

## Method card `ziwei.method.domain-analysis.v1`

- Method card ID: `ziwei.method.domain-analysis.v1`
- School profile ID: `ziwei.school.zhongzhou.v1`
- Topic: `domain-analysis`
- Version: `1`
- Status: `school-specific`

### Requires

- `ziwei.school.zhongzhou.v1`

### Workflow

1. Require an explicit user question and a safe reflective domain before domain analysis. If the question requests professional advice, deterministic outcomes, or an unreviewed palace-to-domain mapping, record the boundary and ask for a narrower reflective scope rather than inventing a target.
2. Use only the previously verified whole-chart inventory, Life-Body axis, canonical four-palace network, same-palace configurations, supported brightness, and natal transformation occurrences. Preserve exact canonical IDs and provenance for every cited fact.
3. Classify only structural expression from emitted occurrences. Apply BRIGHTNESS_SUPPORT:=ziwei.brightness.miao|ziwei.brightness.wang|ziwei.brightness.de, BRIGHTNESS_COUNTER:=ziwei.brightness.bu|ziwei.brightness.xian, and BRIGHTNESS_UNAVAILABLE:=ziwei.brightness.li|ziwei.brightness.ping|null. These statuses describe structural expression only, never favorability, personality, a domain outcome, or confidence.
4. Apply PAIR_GROUPS:=ziwei.star.zuo-fu+ziwei.star.you-bi|ziwei.star.wen-chang+ziwei.star.wen-qu|ziwei.star.tian-kui+ziwei.star.tian-yue within each source-keyed palace-relation group. A complete pair is structural support, exactly one emitted partner is a structural counter, and no emitted partner is unavailable; never attach the source's person-level meanings.
5. Treat any non-null ZiweiStarFact.transformationId as structural prominence only. Partition occurrences into disjoint target-same-palace, trine-palaces, and opposite-palace groups; the same occurrence cannot satisfy two groups even when it has both brightness and transformation fields.
6. Now retrieve supporting and counter-pattern evidence by status only: SUPPORTING means an explicit fact from one methodological group fits a bounded conditional observation; COUNTER means a distinct explicit fact limits it; CONFLICT means procedures disagree; UNAVAILABLE means a required fact or reviewed mapping is absent.
7. Do not import the vendored pattern library, traditional profession lists, palace meanings, or star descriptions as an interpretation corpus. Source references justify procedure and limits only; labels and remembered meanings cannot fill missing canonical mappings.
8. For a major conditional observation, require two non-overlapping methodological groups and identify the exact counter-indicator check. Repeated stars, the same palace reused in two views, or two fields on one occurrence do not become independent evidence.
9. Apply MAJOR_CLAIM_GATE:=at-least-two-distinct-methodological-indicator-groups+explicit-counter-indicator-check. This means methodological grouping and not statistical independence; conflict, unavailable counter-evidence, or fewer than two groups yields insufficient evidence.
10. Apply QUALIFYING_SUPPORT_GROUP:=group.status===SUPPORTING and CONFLICT_GROUP:=retain-for-disclosure-and-counter-review+exclude-from-supporting-group-count. Retain both sides of every conflict for provenance and reflection, but count only resolved supporting groups toward the major structural observation gate.
11. Synthesize only bounded reflective questions and conditional observations, keeping canonical fact, school procedure, inference, and user-provided context separate. Never turn an observation into a verdict about identity, aptitude, compatibility, wellbeing, professional merit, or future outcome.
12. Emit the requested domain, target selection or unavailable status, evidence groups, supporting and counter-evidence, overlap, conflicts, unavailable mappings, provenance, and reflection questions. Then pass no conclusion to timing unless the user supplied a target period and separate canonical layer facts exist.
13. Apply REQUESTED_DOMAIN_MAPPING:=unavailable-no-reviewed-canonical-mapping. Structural groups may be classified, but every person-level or life-domain analysis remains explicitly unavailable until a separately reviewed canonical mapping exists; never imply that structural classification supplies that mapping.
14. This workflow implements ziwei.claim.domain-analysis.v1, approved by the normalization-safety-review at revision task-1-claim-rule-review.2026-09-04 (standards/reviews/ziwei/zhongzhou-domain-claim-rules.yaml).

### Supporting indicators

- `ziwei.brightness.miao`
- `ziwei.brightness.wang`
- `ziwei.brightness.de`

### Counter-indicators

- `ziwei.brightness.bu`
- `ziwei.brightness.xian`

### Output obligations

- `requested-domain-and-target`
- `methodological-evidence-groups`
- `supporting-and-counter-evidence`
- `overlap-conflicts-and-unavailable`
- `provenance-and-reflection`

### Report mapping

| Output obligation | Existing report field |
| --- | --- |
| `requested-domain-and-target` | `domainAnalysis` |
| `methodological-evidence-groups` | `structuralDiagnosis` |
| `supporting-and-counter-evidence` | `structuralDiagnosis` |
| `overlap-conflicts-and-unavailable` | `limitations` |
| `provenance-and-reflection` | `domainAnalysis` |

Preserve supporting, counter, conflict, and unavailable states separately. Never fill an unavailable prerequisite from memory or source narrative.

### Safety policy

- Do not activate methodology outside `ziwei.school.zhongzhou.v1` or the method cards explicitly declared in `requires`.
- Do not present accident-injury, death, financial, incarceration, legal, medical, or self-harm claims as any outcomes.
- Do not perform cross-school mixing from undeclared methods.
- Do not perform deterministic outcome from domain-analysis evidence.
- Do not perform diagnosis, prognosis, or treatment from domain-analysis evidence.
- Do not perform numeric outcome scoring from domain-analysis evidence.
- Do not perform professional advice from domain-analysis evidence.
- Do not perform remediation or purchase prescription from domain-analysis evidence.
- Do not perform retrospective fitting from known events.
- Do not perform single-indicator conclusion from domain-analysis evidence.

### Source locators and revisions

- Source `linden-ziwei-doushu-skill`
  - Locator: `README.md#L69-L78`
  - Revision: `a842dd65dabdc4ce42ec9688b88ae876858a9977`
  - Normalization note: Wholeness and evidence-chain principles are adapted into multi-group conditional reasoning; verification signals and their positive outcomes are not adopted.
- Source `linden-ziwei-doushu-skill`
  - Locator: `SKILL.md#L225-L232`
  - Revision: `a842dd65dabdc4ce42ec9688b88ae876858a9977`
  - Normalization note: Evidence attribution, uncertainty, and restrained output are adapted while personality images, professional recommendations, and source-specific output claims are excluded.
- Source `linden-ziwei-doushu-skill`
  - Locator: `references/xingyao.md#L7-L17`
  - Revision: `a842dd65dabdc4ce42ec9688b88ae876858a9977`
  - Normalization note: Only the emitted brightness ordering is adapted into structural expression statuses; positive and negative trait descriptions are not executable meanings.
- Source `linden-ziwei-doushu-skill`
  - Locator: `references/xingyao.md#L529-L534`
  - Revision: `a842dd65dabdc4ce42ec9688b88ae876858a9977`
  - Normalization note: Only the three named pair-completeness relationships are adapted; all benefic labels, person descriptions, and outcome meanings remain excluded.
- Source `linden-ziwei-doushu-skill`
  - Locator: `references/xingyao.md#L617-L626`
  - Revision: `a842dd65dabdc4ce42ec9688b88ae876858a9977`
  - Normalization note: Same-palace, trine, opposite, brightness, transformation, pair, and whole-chart procedures are narrowed to source-keyed structural classification without interpretation.
- Source `linden-ziwei-method-authority`
  - Locator: `README.md#L69-L78`
  - Revision: `a842dd65dabdc4ce42ec9688b88ae876858a9977`
  - Normalization note: Owner-attested method authority backing ziwei.claim.domain-analysis.v1 (standards/reviews/ziwei/zhongzhou-domain-claim-rules.yaml).

**End method card:** `ziwei.method.domain-analysis.v1`

## Method card `ziwei.method.timing.v1`

- Method card ID: `ziwei.method.timing.v1`
- School profile ID: `ziwei.school.zhongzhou.v1`
- Topic: `timing`
- Version: `1`
- Status: `school-specific`

### Requires

- `ziwei.school.zhongzhou.v1`

### Workflow

1. Require a user-supplied target period and the bounded natal/domain synthesis. If the target is absent, ambiguous, or asks for a guaranteed outcome, return timing unavailable without selecting a period from the current clock.
2. Now apply natal, then decade, then annual layers only when the required deterministic layer facts exist. Define NATAL_LAYER:=ZiweiProfile.palaces and preserve its canonical facts and provenance before inspecting any later layer.
3. Define DECADE_LAYER:=unavailable-unless-separate-deterministic-canonical-facts. ZiweiProfile has no canonical decade-layer envelope; never promote display.decadal, display ages, source prose, current age arithmetic, or a library label into canonical decade evidence.
4. Define ANNUAL_LAYER:=unavailable-unless-separate-deterministic-canonical-facts. ZiweiProfile has no canonical annual-layer envelope; do not calculate a missing layer from source prose, memory, user confirmation, or an unreviewed transformation table.
5. When a future reviewed layer is supplied, require its schema, target period, school convention, time basis, and provenance to match the selected Zhongzhou context. Keep natal, decade, and annual occurrences source-keyed and never merge equal IDs across layers.
6. Compare each available layer only through the same whole-chart, Life-Body, palace-network, and natal-transformation procedures. Retrieve counter-evidence at each layer and mark cross-layer conflict or missing prerequisites instead of turning recurrence into certainty.
7. Apply MAJOR_CLAIM_GATE:=at-least-two-distinct-methodological-indicator-groups+explicit-counter-indicator-check. This is not statistical independence; recurrence across layers cannot count when a layer is absent, unverified, or derived from the same underlying occurrence.
8. Apply QUALIFYING_SUPPORT_GROUP:=group.status===SUPPORTING and CONFLICT_GROUP:=retain-for-disclosure-and-counter-review+exclude-from-supporting-group-count. Preserve cross-layer conflict when layers exist, and never count a conflicted layer group as qualifying support.
9. Finally retrieve supporting and counter-pattern evidence, then synthesize conditionally, preserving conflicts and unavailable evidence. Return target period, available layer facts, unavailable layers, counter-indicators, provenance, and limits without predicting an event or outcome.

### Supporting indicators

- None declared.

### Counter-indicators

- None declared.

### Output obligations

- `target-period`
- `natal-layer`
- `decade-layer-or-unavailable`
- `annual-layer-or-unavailable`
- `counter-indicators-conflicts-and-limits`

### Report mapping

| Output obligation | Existing report field |
| --- | --- |
| `target-period` | `timeline` |
| `natal-layer` | `timeline` |
| `decade-layer-or-unavailable` | `timeline` |
| `annual-layer-or-unavailable` | `timeline` |
| `counter-indicators-conflicts-and-limits` | `limitations` |

Preserve supporting, counter, conflict, and unavailable states separately. Never fill an unavailable prerequisite from memory or source narrative.

### Safety policy

- Do not activate methodology outside `ziwei.school.zhongzhou.v1` or the method cards explicitly declared in `requires`.
- Do not present accident-injury, death, financial, incarceration, legal, medical, or self-harm claims as any outcomes.
- Do not perform cross-school mixing from undeclared methods.
- Do not perform deterministic outcome from timing evidence.
- Do not perform diagnosis, prognosis, or treatment from timing evidence.
- Do not perform numeric outcome scoring from timing evidence.
- Do not perform professional advice from timing evidence.
- Do not perform remediation or purchase prescription from timing evidence.
- Do not perform retrospective fitting from known events.
- Do not perform single-indicator conclusion from timing evidence.

### Source locators and revisions

- Source `linden-ziwei-doushu-skill`
  - Locator: `SKILL.md#L192-L205`
  - Revision: `a842dd65dabdc4ce42ec9688b88ae876858a9977`
  - Normalization note: The source's natal-before-decade ordering is adapted as an availability-gated sequence; source age calculation, decadal meanings, and absent annual tools are not adopted.
- Source `linden-ziwei-doushu-skill`
  - Locator: `SKILL.md#L287-L292`
  - Revision: `a842dd65dabdc4ce42ec9688b88ae876858a9977`
  - Normalization note: Evidence attribution, explicit uncertainty, and non-alarmist limits are retained; current-time lookup and unsupported predictive procedures are excluded.

**End method card:** `ziwei.method.timing.v1`

# Deferred profiles

These profiles have no reviewed executable method cards and cannot be selected or inherit cards from the default profile:

- `ziwei.school.sanhe.v1`: unavailable
- `ziwei.school.feixing.v1`: unavailable
- `ziwei.school.qintian-sihua.v1`: unavailable
