# LIUYAO method pack

This procedure-only reference is generated from reviewed OMDS school profiles and method cards. Returned canonical facts remain authoritative; source notes do not supply missing facts or interpretations.

# Selected profile: `liuyao.school.jingfang-zengshan.v1`

Apply these cards in the declared order below only when this profile is selected. This default profile is isolated; do not merge cards from another profile.

## Profile source locators and revisions

- Source `yigram-najia-rules`
  - Locator: `rules/palace-and-generation.md#palace-generation-and-shiying-positions`
  - Revision: `0bb53f14c1cd379afeeccaa5a3dbb8531686ffe9`
  - Normalization note: Jingfang eight-palace and Shi-Ying seed reference.
- Source `johnson-liuyao-divination`
  - Locator: `skill/liuyao-divination/SKILL.md#L20-L36`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Najia, month-day, and moving-change board reference.
- Source `johnson-liuyao-divination`
  - Locator: `skill/liuyao-divination/SKILL.md#L37-L76`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Pinned source order normalized into the seven procedure-only cards listed in primaryMethods.
- Source `johnson-liuyao-divination`
  - Locator: `references/08-断卦步骤.md#L5-L22`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Pinned eight-step order normalized into method-card dependencies; conclusion-writing stages are excluded.
- Source `johnson-liuyao-divination`
  - Locator: `references/08-断卦步骤.md#L23-L33`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Pinned per-step counter-checks retained to support the source-backed primaryMethods order.

## Method card `liuyao.method.question-contract.v1`

- Method card ID: `liuyao.method.question-contract.v1`
- School profile ID: `liuyao.school.jingfang-zengshan.v1`
- Topic: `question-contract`
- Version: `1`
- Status: `core`

### Requires

- `liuyao.school.jingfang-zengshan.v1`
- `liuyao.role.world`
- `liuyao.role.response`
- `liuyao.relation.parents`
- `liuyao.relation.siblings`
- `liuyao.relation.offspring`
- `liuyao.relation.wealth`
- `liuyao.relation.official-ghost`

### Workflow

1. Read context.question exactly as supplied; if it is absent, record the question contract as incomplete and stop before selecting a focus line.
2. Extract only the explicit subject, object, declared relationship, time horizon, and decision alternatives without adding motives, traits, or unstated history.
3. Classify whether the request concerns a Liuyao decision object; preserve ambiguity when the text could refer to more than one object or relation category.
4. Use liuyao.role.world and liuyao.role.response only as structural self and counterpart positions, keeping those roles separate from the five relationId categories.
5. List missing inputs that would change relation selection, especially an unnamed object, ambiguous counterpart, or absent time horizon.
6. Hand the explicit object and every unresolved alternative to use-spirit selection without evaluating strength, timing, or result.
7. This workflow implements liuyao.claim.question-contract-scope.v1, approved by the normalization-safety-review at revision task-1-claim-rule-review.2026-09-03 (standards/reviews/liuyao/jingfang-zengshan-claim-rules.yaml).

### Supporting indicators

- None declared.

### Counter-indicators

- None declared.

### Output obligations

- `explicit-question`
- `decision-object`
- `structural-parties`
- `time-horizon`
- `alternatives-and-missing-inputs`
- `selection-handoff`

### Report mapping

| Output obligation | Existing report field |
| --- | --- |
| `explicit-question` | `domainAnalysis` |
| `decision-object` | `domainAnalysis` |
| `structural-parties` | `domainAnalysis` |
| `time-horizon` | `timeline` |
| `alternatives-and-missing-inputs` | `limitations` |
| `selection-handoff` | `domainAnalysis` |

Preserve supporting, counter, conflict, and unavailable states separately. Never fill an unavailable prerequisite from memory or source narrative.

### Safety policy

- Do not activate methodology outside `liuyao.school.jingfang-zengshan.v1` or the method cards explicitly declared in `requires`.
- Do not present death, financial, incarceration, legal, or medical claims as any outcomes.
- Do not perform cross-school mixing from undeclared methods.
- Do not perform deterministic outcome from question-contract evidence.
- Do not perform diagnosis, prognosis, or treatment from question-contract evidence.
- Do not perform numeric outcome scoring from question-contract evidence.
- Do not perform personality or destiny assertion from question-contract evidence.
- Do not perform professional advice from question-contract evidence.
- Do not perform remediation or purchase prescription from question-contract evidence.
- Do not perform retrospective fitting from known events.
- Do not perform suppressed counterevidence from question-contract evidence.

### Source locators and revisions

- Source `johnson-liuyao-divination`
  - Locator: `skill/liuyao-divination/SKILL.md#L14-L19`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Scope distinctions retained while prediction and professional-domain examples are excluded.
- Source `johnson-liuyao-divination`
  - Locator: `references/02-用神取用.md#L54-L63`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: The explicit question-object prerequisite is retained; absolute result claims are excluded.
- Source `johnson-liuyao-divination`
  - Locator: `skill/liuyao-divination/SKILL.md#L201-L203`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Professional-advice and factual-prediction boundaries are retained as prohibited inferences.
- Source `johnson-liuyao-method-authority`
  - Locator: `skill/liuyao-divination/SKILL.md#L14-L19`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Owner-attested method authority backing liuyao.claim.question-contract-scope.v1 (standards/reviews/liuyao/jingfang-zengshan-claim-rules.yaml).

**End method card:** `liuyao.method.question-contract.v1`

## Method card `liuyao.method.use-spirit-selection.v1`

- Method card ID: `liuyao.method.use-spirit-selection.v1`
- School profile ID: `liuyao.school.jingfang-zengshan.v1`
- Topic: `use-spirit-selection`
- Version: `1`
- Status: `school-specific`

### Requires

- `liuyao.school.jingfang-zengshan.v1`
- `liuyao.relation.parents`
- `liuyao.relation.siblings`
- `liuyao.relation.offspring`
- `liuyao.relation.wealth`
- `liuyao.relation.official-ghost`
- `liuyao.role.world`
- `liuyao.role.response`
- `common.element.wood`
- `common.element.fire`
- `common.element.earth`
- `common.element.metal`
- `common.element.water`
- `liuyao.state.month-supported`
- `liuyao.state.month-broken`
- `liuyao.state.day-supported`
- `liuyao.state.day-clashed`
- `liuyao.state.void`

### Workflow

1. Read context.question together with the question-contract output; if either lacks an explicit object, record selection as unresolved and stop before evaluating line strength.
2. Apply OBJECT_RELATION_MAP only to explicit wording: parents|elders|documents|contracts|credentials|houses|land|vehicles=>liuyao.relation.parents; siblings|peers|friends|business-partners|competitors|colleagues=>liuyao.relation.siblings; children|juniors|subordinates|students|pets|livestock|entertainment=>liuyao.relation.offspring; money|funds|goods|food-stocks|crops=>liuyao.relation.wealth; jobs|offices|promotions|authority|managers|explicit-theft-suspects=>liuyao.relation.official-ghost.
3. Apply safe source extensions only to the named object: ancestral-property|boats|clothing=>liuyao.relation.parents; clergy=>liuyao.relation.offspring; litigation|legal-dispute=>liuyao.relation.official-ghost; finance|business=>liuyao.relation.wealth, adding liuyao.relation.offspring only when the explicit object is an income source rather than a projected return.
4. Apply only explicit compound classes: examinations|job-applications|promotions=>liuyao.relation.official-ghost+liuyao.relation.parents; lost-property|theft=>liuyao.relation.wealth, adding liuyao.relation.official-ghost only when the question explicitly asks about a responsible party; partnership|competition=>liuyao.relation.siblings; building-or-buying-home=>liuyao.relation.parents.
5. For an explicitly named wife or girlfriend use liuyao.relation.wealth as a source-tradition candidate, and for an explicitly named husband or boyfriend use liuyao.relation.official-ghost; never infer the questioner's gender, identity, or relationship role. A traveler uses the declared kin or object mapping, while an unspecified counterpart remains liuyao.role.response rather than a relationId.
6. For a self-directed general question use liuyao.role.world as the structural focus, and for another person or an object with no supported relation class use liuyao.role.response; neither role is converted into a relationId.
7. Do not map symptoms, diagnosis, treatment, legal merits, investment recommendations, weather-state claims, servitude labels, or asserted worries through the source table; record the professional or factual-prediction boundary and leave selection unresolved unless a safe explicit object independently maps above.
8. Locate visible lines whose relationId matches each candidate and preserve position, elementId, roleIds, stateIds, changing, and changed.elementId when present without ranking them.
9. If no visible line matches, inspect hiddenLine.relationId and record a hidden candidate with its sourcePosition; absence is missing evidence rather than a result.
10. Compare candidate positions with liuyao.role.world and liuyao.role.response to distinguish self and counterpart while keeping role and relation conceptually separate.
11. Select one focus only when the explicit question and structural facts agree; otherwise return the candidate set and exact clarification, and stop before the element comparison below.
12. Use GENERATION_CYCLE exactly as directional pairs: common.element.wood->common.element.fire, common.element.fire->common.element.earth, common.element.earth->common.element.metal, common.element.metal->common.element.water, common.element.water->common.element.wood.
13. Use CONTROL_CYCLE exactly as directional pairs: common.element.wood->common.element.earth, common.element.earth->common.element.water, common.element.water->common.element.fire, common.element.fire->common.element.metal, common.element.metal->common.element.wood.
14. Relative to the selected focus elementId, record a generator-line candidate only when another line's elementId points to the focus through GENERATION_CYCLE, and record a controller-line candidate only when it points to the focus through CONTROL_CYCLE; record an indirect-line candidate only when its element controls the generator element and generates the controller element. These are procedural candidates, not emitted four-spirit role IDs.
15. For every generator-line candidate, controller-line candidate, and indirect-line candidate, record changing and the exact liuyao.state.month-supported, liuyao.state.day-supported, liuyao.state.month-broken, liuyao.state.day-clashed, and liuyao.state.void markers present; when changed.elementId exists, rerun both cycles for that changed element. Preserve mixed evidence and do not manufacture an effectiveness score.
16. Return the focus basis, visible and hidden candidates, structural role cross-check, element-relation candidates, emitted counterchecks, and unresolved inputs without a narrative conclusion.
17. This workflow implements liuyao.claim.use-spirit-selection.v1, approved by the normalization-safety-review at revision task-1-claim-rule-review.2026-09-03 (standards/reviews/liuyao/jingfang-zengshan-claim-rules.yaml).

### Supporting indicators

- None declared.

### Counter-indicators

- None declared.

### Output obligations

- `selection-basis`
- `candidate-lines`
- `hidden-line-check`
- `role-cross-check`
- `selected-focus-or-clarification`
- `element-relation-candidates`
- `candidate-state-counterchecks`

### Report mapping

| Output obligation | Existing report field |
| --- | --- |
| `selection-basis` | `structuralDiagnosis` |
| `candidate-lines` | `structuralDiagnosis` |
| `hidden-line-check` | `structuralDiagnosis` |
| `role-cross-check` | `structuralDiagnosis` |
| `selected-focus-or-clarification` | `domainAnalysis` |
| `element-relation-candidates` | `domainAnalysis` |
| `candidate-state-counterchecks` | `structuralDiagnosis` |

Preserve supporting, counter, conflict, and unavailable states separately. Never fill an unavailable prerequisite from memory or source narrative.

### Safety policy

- Do not activate methodology outside `liuyao.school.jingfang-zengshan.v1` or the method cards explicitly declared in `requires`.
- Do not present death, financial, incarceration, legal, or medical claims as any outcomes.
- Do not perform cross-school mixing from undeclared methods.
- Do not perform deterministic outcome from use-spirit-selection evidence.
- Do not perform diagnosis, prognosis, or treatment from use-spirit-selection evidence.
- Do not perform numeric outcome scoring from use-spirit-selection evidence.
- Do not perform personality or destiny assertion from use-spirit-selection evidence.
- Do not perform professional advice from use-spirit-selection evidence.
- Do not perform remediation or purchase prescription from use-spirit-selection evidence.
- Do not perform retrospective fitting from known events.
- Do not perform unsupported role assumption from use-spirit-selection evidence.

### Source locators and revisions

- Source `johnson-liuyao-divination`
  - Locator: `references/02-用神取用.md#L5-L14`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Object-to-relation mappings are conditionalized on explicit wording; diagnosis and gender assumptions are excluded.
- Source `johnson-liuyao-divination`
  - Locator: `references/02-用神取用.md#L15-L32`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Common selection mappings are conditionalized on the declared object and never treated as universal outcomes.
- Source `johnson-liuyao-divination`
  - Locator: `references/02-用神取用.md#L33-L43`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: World and response are retained as structural cross-checks without favorable or adverse result claims.
- Source `johnson-liuyao-divination`
  - Locator: `references/02-用神取用.md#L44-L53`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Hidden-line lookup is retained as missing-visible-candidate procedure; asserted implications are excluded.
- Source `johnson-liuyao-divination`
  - Locator: `references/02-用神取用.md#L54-L63`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Question-first selection and ambiguity handling are retained as ordered procedure.
- Source `johnson-liuyao-divination`
  - Locator: `references/09-四神与有力无力.md#L7-L19`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Four-spirit definitions are reduced to exact element-cycle candidates because LiuyaoReading emits no four-spirit role IDs.
- Source `johnson-liuyao-divination`
  - Locator: `references/09-四神与有力无力.md#L20-L27`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Generator support tests use only emitted state markers and changed element facts, without an effectiveness verdict.
- Source `johnson-liuyao-divination`
  - Locator: `references/09-四神与有力无力.md#L28-L38`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Generator counterconditions are limited to emitted break, clash, and void markers; un-emitted stages are excluded.
- Source `johnson-liuyao-divination`
  - Locator: `references/09-四神与有力无力.md#L39-L46`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Controller candidates are identified by the exact control cycle and evaluated only through available line facts.
- Source `johnson-liuyao-divination`
  - Locator: `references/09-四神与有力无力.md#L47-L56`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Controller counterchecks preserve mixed or missing evidence rather than reversing or asserting an effect.
- Source `johnson-liuyao-divination`
  - Locator: `references/09-四神与有力无力.md#L57-L62`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: A resolved focus element is retained as a hard prerequisite; root, viability, and outcome claims are excluded.
- Source `johnson-liuyao-divination`
  - Locator: `references/09-四神与有力无力.md#L63-L66`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: The indirect chain is retained only as an element-cycle candidate with no asserted force or domain meaning.
- Source `johnson-liuyao-method-authority`
  - Locator: `references/02-用神取用.md#L5-L14`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Owner-attested method authority backing liuyao.claim.use-spirit-selection.v1 (standards/reviews/liuyao/jingfang-zengshan-claim-rules.yaml).

**End method card:** `liuyao.method.use-spirit-selection.v1`

## Method card `liuyao.method.month-day-strength.v1`

- Method card ID: `liuyao.method.month-day-strength.v1`
- School profile ID: `liuyao.school.jingfang-zengshan.v1`
- Topic: `month-day-strength`
- Version: `1`
- Status: `school-specific`

### Requires

- `liuyao.school.jingfang-zengshan.v1`
- `liuyao.state.month-supported`
- `liuyao.state.month-broken`
- `liuyao.state.day-supported`
- `liuyao.state.day-clashed`
- `liuyao.state.void`
- `common.element.wood`
- `common.element.fire`
- `common.element.earth`
- `common.element.metal`
- `common.element.water`
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

1. Require a non-null ganzhi context; when it is absent, mark month, day, and void evaluation unavailable rather than reconstructing a casting time.
2. For the selected focus, world, and response lines, record branchId, elementId, and the exact liuyao.state.month-supported, liuyao.state.month-broken, liuyao.state.day-supported, liuyao.state.day-clashed, and liuyao.state.void values present before comparing lines.
3. Evaluate liuyao.state.month-supported and liuyao.state.month-broken independently, preserving both when the deterministic reading emits both and never deriving control, drain, expenditure, or combination from these two markers.
4. Evaluate liuyao.state.day-supported and liuyao.state.day-clashed independently, without turning either marker into a combined strength label.
5. Cross-check liuyao.state.void against ganzhi.voidBranchIds and identify missing or conflicting evidence instead of inferring a void effect.
6. Use BRANCH_ELEMENT_MAP only to compare explicit control sources: common.branch.yin|common.branch.mao=>common.element.wood; common.branch.si|common.branch.wu=>common.element.fire; common.branch.chen|common.branch.xu|common.branch.chou|common.branch.wei=>common.element.earth; common.branch.shen|common.branch.you=>common.element.metal; common.branch.hai|common.branch.zi=>common.element.water.
7. Use CONTROL_CYCLE only in these directions: common.element.wood->common.element.earth, common.element.earth->common.element.water, common.element.water->common.element.fire, common.element.fire->common.element.metal, common.element.metal->common.element.wood.
8. For the selected focus, inventory distinct control-source candidates from ganzhi.month.branchId, every changing line's elementId, and each present changed.elementId; count a source only when its mapped element points to the focus element through CONTROL_CYCLE.
9. When the focus branchId exactly equals ganzhi.day.branchId or ganzhi.month.branchId, do not infer immunity. Record MULTIPLE_CONTROL_CANDIDATE only when at least two distinct control sources were found, keep all emitted support and counter markers beside the count, and withhold any damage or override verdict.
10. Compare the fact matrix line by line; keep mixed month-day evidence unresolved, do not replace it with a numeric score, and pass only facts and conditional control-source counts to later cards.
11. This workflow implements liuyao.claim.month-day-strength.v1, approved by the normalization-safety-review at revision task-1-claim-rule-review.2026-09-03 (standards/reviews/liuyao/jingfang-zengshan-claim-rules.yaml).

### Supporting indicators

- `liuyao.state.month-supported`
- `liuyao.state.day-supported`

### Counter-indicators

- `liuyao.state.month-broken`
- `liuyao.state.day-clashed`
- `liuyao.state.void`

### Output obligations

- `focus-line-facts`
- `month-markers`
- `day-markers`
- `void-cross-check`
- `unresolved-conflicts`

### Report mapping

| Output obligation | Existing report field |
| --- | --- |
| `focus-line-facts` | `structuralDiagnosis` |
| `month-markers` | `timeline` |
| `day-markers` | `timeline` |
| `void-cross-check` | `structuralDiagnosis` |
| `unresolved-conflicts` | `limitations` |

Preserve supporting, counter, conflict, and unavailable states separately. Never fill an unavailable prerequisite from memory or source narrative.

### Safety policy

- Do not activate methodology outside `liuyao.school.jingfang-zengshan.v1` or the method cards explicitly declared in `requires`.
- Do not present death, financial, incarceration, legal, or medical claims as any outcomes.
- Do not perform cross-school mixing from undeclared methods.
- Do not perform deterministic outcome from month-day-strength evidence.
- Do not perform diagnosis, prognosis, or treatment from month-day-strength evidence.
- Do not perform numeric outcome scoring from month-day-strength evidence.
- Do not perform professional advice from month-day-strength evidence.
- Do not perform remediation or purchase prescription from month-day-strength evidence.
- Do not perform retrospective fitting from known events.
- Do not perform unsupported force aggregation from month-day-strength evidence.

### Source locators and revisions

- Source `johnson-liuyao-divination`
  - Locator: `references/03-旺衰月日.md#L7-L12`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Month and day are retained as separate context inputs rather than a certainty rule.
- Source `johnson-liuyao-divination`
  - Locator: `references/03-旺衰月日.md#L50-L62`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Only emitted support, break, and clash markers are retained; control, drain, expenditure, and combination claims are excluded.
- Source `johnson-liuyao-divination`
  - Locator: `references/03-旺衰月日.md#L63-L69`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Aggregate strength language is replaced by an ordered comparison that preserves conflicting emitted states.
- Source `johnson-liuyao-divination`
  - Locator: `references/03-旺衰月日.md#L88-L101`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: A distinct multiple-control inventory is implemented while categorical privilege, immunity, and damage claims are excluded.
- Source `johnson-liuyao-method-authority`
  - Locator: `references/03-旺衰月日.md#L7-L12`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Owner-attested method authority backing liuyao.claim.month-day-strength.v1 (standards/reviews/liuyao/jingfang-zengshan-claim-rules.yaml).

**End method card:** `liuyao.method.month-day-strength.v1`

## Method card `liuyao.method.moving-line-effects.v1`

- Method card ID: `liuyao.method.moving-line-effects.v1`
- School profile ID: `liuyao.school.jingfang-zengshan.v1`
- Topic: `moving-line-effects`
- Version: `1`
- Status: `school-specific`

### Requires

- `liuyao.school.jingfang-zengshan.v1`
- `liuyao.polarity.yin`
- `liuyao.polarity.yang`
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
- `common.element.wood`
- `common.element.fire`
- `common.element.earth`
- `common.element.metal`
- `common.element.water`
- `liuyao.relation.parents`
- `liuyao.relation.siblings`
- `liuyao.relation.offspring`
- `liuyao.relation.wealth`
- `liuyao.relation.official-ghost`
- `liuyao.state.month-supported`
- `liuyao.state.month-broken`
- `liuyao.state.day-supported`
- `liuyao.state.day-clashed`
- `liuyao.state.void`

### Workflow

1. Inventory every line and split it explicitly into changing === true and changing === false groups; an empty changing group skips only primary-to-changed tests and does not skip static day-clash review.
2. For each changing === false line containing liuyao.state.day-clashed, record DARK_MOVEMENT_CANDIDATE only when liuyao.state.month-supported or liuyao.state.day-supported is also present; retain liuyao.state.month-broken and liuyao.state.void as counterconditions, and mark mixed evidence unresolved rather than scoring it.
3. For the same static day-clashed set, record DAY_BREAK_CANDIDATE only when neither support marker is present and liuyao.state.month-broken or liuyao.state.void is present; otherwise record an unresolved day-clash candidate, never a definitive movement or break state.
4. Enumerate lines where changing === true; if none exist, emit a no-moving-lines fact and do not manufacture changed-line effects.
5. Verify that every changing line has a changed object and that the reading has a changed hexagram; record any mismatch as unavailable evidence.
6. For each moving line, compare primary and changed polarityId, branchId, elementId, and relationId as separate transitions using only the declared liuyao.polarity.yin, liuyao.polarity.yang, and five liuyao.relation IDs.
7. When primary and changed elementId match, use PROGRESSION_PAIRS exactly: common.branch.yin->common.branch.mao, common.branch.si->common.branch.wu, common.branch.shen->common.branch.you, common.branch.hai->common.branch.zi, common.branch.chou->common.branch.chen, common.branch.chen->common.branch.wei, common.branch.wei->common.branch.xu.
8. Use RETREAT_PAIRS only in the reverse directions: common.branch.mao->common.branch.yin, common.branch.wu->common.branch.si, common.branch.you->common.branch.shen, common.branch.zi->common.branch.hai, common.branch.chen->common.branch.chou, common.branch.wei->common.branch.chen, common.branch.xu->common.branch.wei; any other same-element transition remains unclassified.
9. Use GENERATION_CYCLE exactly as common.element.wood->common.element.fire, common.element.fire->common.element.earth, common.element.earth->common.element.metal, common.element.metal->common.element.water, common.element.water->common.element.wood.
10. Use CONTROL_CYCLE exactly as common.element.wood->common.element.earth, common.element.earth->common.element.water, common.element.water->common.element.fire, common.element.fire->common.element.metal, common.element.metal->common.element.wood; when elementId differs, compare changed.elementId toward the primary elementId through these cycles and withhold an overall evaluation.
11. Use BRANCH_ELEMENT_MAP for emitted branches: common.branch.yin|common.branch.mao=>common.element.wood; common.branch.si|common.branch.wu=>common.element.fire; common.branch.chen|common.branch.xu|common.branch.chou|common.branch.wei=>common.element.earth; common.branch.shen|common.branch.you=>common.element.metal; common.branch.hai|common.branch.zi=>common.element.water.
12. For each changed.branchId, derive liuyao.state.void only by ganzhi.voidBranchIds membership, derive month/day break or clash only by the opposition table below, and derive support only from same element or GENERATION_CYCLE; keep these changed-branch candidates separate from primary stateIds.
13. Use TOMB_MAP for a changed-tomb candidate only: common.element.wood->tomb:common.branch.wei, common.element.fire->tomb:common.branch.xu, common.element.metal->tomb:common.branch.chou, common.element.water->tomb:common.branch.chen, common.element.earth->tomb:common.branch.chen; require changed.branchId to equal the primary element's mapped tomb and defer release checks to the tomb card.
14. Use OPPOSITION_PAIRS exactly: common.branch.zi&lt;>common.branch.wu, common.branch.chou&lt;>common.branch.wei, common.branch.yin&lt;>common.branch.shen, common.branch.mao&lt;>common.branch.you, common.branch.chen&lt;>common.branch.xu, common.branch.si&lt;>common.branch.hai.
15. When at least one moving line exists and every changing line has a changed.branchId that is the exact opposition partner of its primary branchId, record FAN_YIN_CANDIDATE as the source's limited sufficient pattern; incomplete or nonmatching comparisons do not establish absence.
16. For fu-yin, require comparable current and changed branches at all six positions; only when all six positions are present and each changed.branchId === primary branchId may the procedure record FU_YIN_CANDIDATE. Fewer than six complete pairs make this aggregate check unavailable.
17. Keep FAN_YIN_CANDIDATE and FU_YIN_CANDIDATE separate from the primary-versus-changed palaceElementId comparison; apply the same element cycles to palace elements only as an auxiliary pattern and counter-check every aggregate candidate against focus-line transitions and mixed states.
18. Return static day-clash candidates, transition facts, matched lookup procedures, aggregate checks, counter indicators, and unresolved cases without a narrative result.
19. This workflow implements liuyao.claim.moving-line-effects.v1, approved by the normalization-safety-review at revision task-1-claim-rule-review.2026-09-03 (standards/reviews/liuyao/jingfang-zengshan-claim-rules.yaml).

### Supporting indicators

- `liuyao.state.month-supported`
- `liuyao.state.day-supported`

### Counter-indicators

- `liuyao.state.month-broken`
- `liuyao.state.day-clashed`
- `liuyao.state.void`

### Output obligations

- `static-day-clash-candidates`
- `moving-lines`
- `primary-to-changed-facts`
- `conditional-transition-tests`
- `aggregate-fan-fu-checks`
- `palace-level-cross-check`
- `unresolved-conflicts`

### Report mapping

| Output obligation | Existing report field |
| --- | --- |
| `static-day-clash-candidates` | `structuralDiagnosis` |
| `moving-lines` | `structuralDiagnosis` |
| `primary-to-changed-facts` | `structuralDiagnosis` |
| `conditional-transition-tests` | `scenarios` |
| `aggregate-fan-fu-checks` | `scenarios` |
| `palace-level-cross-check` | `structuralDiagnosis` |
| `unresolved-conflicts` | `limitations` |

Preserve supporting, counter, conflict, and unavailable states separately. Never fill an unavailable prerequisite from memory or source narrative.

### Safety policy

- Do not activate methodology outside `liuyao.school.jingfang-zengshan.v1` or the method cards explicitly declared in `requires`.
- Do not present death, financial, incarceration, legal, or medical claims as any outcomes.
- Do not perform cross-school mixing from undeclared methods.
- Do not perform deterministic outcome from moving-line-effects evidence.
- Do not perform diagnosis, prognosis, or treatment from moving-line-effects evidence.
- Do not perform numeric outcome scoring from moving-line-effects evidence.
- Do not perform professional advice from moving-line-effects evidence.
- Do not perform remediation or purchase prescription from moving-line-effects evidence.
- Do not perform retrospective fitting from known events.
- Do not perform suppressed counterevidence from moving-line-effects evidence.
- Do not perform unsupported force aggregation from moving-line-effects evidence.
- Do not perform unsupported transition classification from moving-line-effects evidence.

### Source locators and revisions

- Source `johnson-liuyao-divination`
  - Locator: `references/04-动静暗破.md#L10-L22`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: The exact six opposition pairs are retained for branch checks while month-break outcome meanings are excluded.
- Source `johnson-liuyao-divination`
  - Locator: `references/04-动静暗破.md#L5-L9`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Explicit changing status is retained; narrative meanings of movement are excluded.
- Source `johnson-liuyao-divination`
  - Locator: `references/04-动静暗破.md#L23-L51`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Day-clash distinctions are converted into conditional checks using emitted facts and counter evidence.
- Source `johnson-liuyao-divination`
  - Locator: `references/04-动静暗破.md#L52-L79`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Void distinctions are retained only when ganzhi and changed branch facts support the conditional check.
- Source `johnson-liuyao-divination`
  - Locator: `references/05-进退神化.md#L5-L25`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Exact same-element branch direction pairs are retained while directional result claims are excluded.
- Source `johnson-liuyao-divination`
  - Locator: `references/05-进退神化.md#L26-L38`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Changed-to-primary element relations are retained as conditional structural comparisons, not outcomes.
- Source `johnson-liuyao-divination`
  - Locator: `references/05-进退神化.md#L39-L48`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Changed branch void, break, and tomb checks are retained only when derivable from emitted ganzhi facts.
- Source `johnson-liuyao-divination`
  - Locator: `references/05-进退神化.md#L49-L59`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: The ordered transition questions are retained as procedure with a required counter-evidence pass.
- Source `johnson-liuyao-divination`
  - Locator: `references/10-卦变反伏.md#L7-L21`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Palace element comparison is retained as an auxiliary pattern; absolute favorable and adverse claims are excluded.
- Source `johnson-liuyao-divination`
  - Locator: `references/10-卦变反伏.md#L22-L30`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Reversal is conditionalized to exact emitted branch transitions; narrative domain outcomes are excluded.
- Source `johnson-liuyao-divination`
  - Locator: `references/10-卦变反伏.md#L31-L39`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Repetition is conditionalized to complete emitted branch comparisons; narrative domain outcomes are excluded.
- Source `johnson-liuyao-divination`
  - Locator: `references/10-卦变反伏.md#L40-L46`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: The distinction checklist is retained only as an evidence test with unresolved status when incomplete.
- Source `johnson-liuyao-method-authority`
  - Locator: `references/04-动静暗破.md#L5-L9`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Owner-attested method authority backing liuyao.claim.moving-line-effects.v1 (standards/reviews/liuyao/jingfang-zengshan-claim-rules.yaml).

**End method card:** `liuyao.method.moving-line-effects.v1`

## Method card `liuyao.method.combinations.v1`

- Method card ID: `liuyao.method.combinations.v1`
- School profile ID: `liuyao.school.jingfang-zengshan.v1`
- Topic: `combinations`
- Version: `1`
- Status: `school-specific`

### Requires

- `liuyao.school.jingfang-zengshan.v1`
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
- `liuyao.state.month-supported`
- `liuyao.state.month-broken`
- `liuyao.state.day-supported`
- `liuyao.state.day-clashed`
- `liuyao.state.void`

### Workflow

1. Inventory branchId values from primary lines, moving-line changed facts, ganzhi.month, and ganzhi.day while preserving each branch origin and changing status.
2. Use TRIADS exactly: common.branch.shen+common.branch.zi+common.branch.chen[middle=common.branch.zi], common.branch.hai+common.branch.mao+common.branch.wei[middle=common.branch.mao], common.branch.yin+common.branch.wu+common.branch.xu[middle=common.branch.wu], common.branch.si+common.branch.you+common.branch.chou[middle=common.branch.you]; do not infer a triad from shared elementId.
3. Derive activity locally for this card from each primary line: DARK_MOVEMENT_CANDIDATE := changing === false AND liuyao.state.day-clashed present AND (liuyao.state.month-supported OR liuyao.state.day-supported) AND liuyao.state.month-broken absent AND liuyao.state.void absent. Do not consume an ephemeral label from another card.
4. Define ACTIVE_TRIAD_PARTICIPANT := changing === true OR DARK_MOVEMENT_CANDIDATE. A changed branch inherits active status from its explicitly changing source line, but count that source line at most once; month and day context branches never count as active participants.
5. For a complete triad, count unique ACTIVE_TRIAD_PARTICIPANT sources. Three active participants or two active plus one inactive branch meet the activity threshold; one changing participant plus one qualifying DARK_MOVEMENT_CANDIDATE counts as two active participants.
6. Record a realized triad candidate only with at least two unique ACTIVE_TRIAD_PARTICIPANT sources and an explicit middle-branch line carrying liuyao.state.month-supported or liuyao.state.day-supported. Zero or one active participant cannot satisfy the threshold, and a static day-clashed line carrying liuyao.state.month-broken or liuyao.state.void is not active; record the exact unmet condition.
7. Use COMBINE_PAIRS exactly: common.branch.zi+common.branch.chou, common.branch.yin+common.branch.hai, common.branch.mao+common.branch.xu, common.branch.chen+common.branch.you, common.branch.si+common.branch.shen, common.branch.wu+common.branch.wei.
8. For each exact pair, record whether each participant is static, changing, changed, month, or day context before retaining binding and activation as unresolved alternatives.
9. Use OPPOSITION_PAIRS exactly: common.branch.zi&lt;>common.branch.wu, common.branch.chou&lt;>common.branch.wei, common.branch.yin&lt;>common.branch.shen, common.branch.mao&lt;>common.branch.you, common.branch.chen&lt;>common.branch.xu, common.branch.si&lt;>common.branch.hai.
10. Counter-check every pair or triad against exact opposing participants and against liuyao.state.month-broken, liuyao.state.day-clashed, and liuyao.state.void on participating lines; a single marker does not automatically cancel a candidate.
11. Do not assign a resultant element force unless the realization conditions and supporting markers are explicit; preserve competing combination candidates.
12. Output the branch evidence, classification test, counter-checks, and unresolved conditions as structured procedure results.
13. This workflow implements liuyao.claim.combinations.v1, approved by the normalization-safety-review at revision task-1-claim-rule-review.2026-09-03 (standards/reviews/liuyao/jingfang-zengshan-claim-rules.yaml).

### Supporting indicators

- `liuyao.state.month-supported`
- `liuyao.state.day-supported`

### Counter-indicators

- `liuyao.state.month-broken`
- `liuyao.state.day-clashed`
- `liuyao.state.void`

### Output obligations

- `branch-inventory`
- `candidate-pairs-and-triads`
- `realization-test`
- `clash-and-void-counterchecks`
- `unresolved-conditions`

### Report mapping

| Output obligation | Existing report field |
| --- | --- |
| `branch-inventory` | `structuralDiagnosis` |
| `candidate-pairs-and-triads` | `structuralDiagnosis` |
| `realization-test` | `scenarios` |
| `clash-and-void-counterchecks` | `structuralDiagnosis` |
| `unresolved-conditions` | `limitations` |

Preserve supporting, counter, conflict, and unavailable states separately. Never fill an unavailable prerequisite from memory or source narrative.

### Safety policy

- Do not activate methodology outside `liuyao.school.jingfang-zengshan.v1` or the method cards explicitly declared in `requires`.
- Do not present death, financial, incarceration, legal, medical, or relationship claims as any outcomes.
- Do not perform cross-school mixing from undeclared methods.
- Do not perform deterministic outcome from combinations evidence.
- Do not perform diagnosis, prognosis, or treatment from combinations evidence.
- Do not perform numeric outcome scoring from combinations evidence.
- Do not perform professional advice from combinations evidence.
- Do not perform remediation or purchase prescription from combinations evidence.
- Do not perform retrospective fitting from known events.
- Do not perform unsupported favorability from combinations evidence.
- Do not perform unsupported force aggregation from combinations evidence.

### Source locators and revisions

- Source `johnson-liuyao-divination`
  - Locator: `references/04-动静暗破.md#L10-L22`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: The exact opposition table is retained only for bilateral checks; predicted month-break effects are excluded.
- Source `johnson-liuyao-divination`
  - Locator: `references/06-三合六合.md#L5-L42`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Triad sets use a local supported and unbroken dark-movement derivation plus a two-active-source threshold; asserted meanings are excluded.
- Source `johnson-liuyao-divination`
  - Locator: `references/06-三合六合.md#L43-L65`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Exact branch pairs are retained with binding and activation treated as alternatives requiring facts.
- Source `johnson-liuyao-divination`
  - Locator: `references/06-三合六合.md#L66-L77`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Clash interactions are retained as counter-checks without favorable or adverse outcome labels.
- Source `johnson-liuyao-method-authority`
  - Locator: `references/06-三合六合.md#L5-L42`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Owner-attested method authority backing liuyao.claim.combinations.v1 (standards/reviews/liuyao/jingfang-zengshan-claim-rules.yaml).

**End method card:** `liuyao.method.combinations.v1`

## Method card `liuyao.method.tomb-storage.v1`

- Method card ID: `liuyao.method.tomb-storage.v1`
- School profile ID: `liuyao.school.jingfang-zengshan.v1`
- Topic: `tomb-storage`
- Version: `1`
- Status: `school-specific`

### Requires

- `liuyao.school.jingfang-zengshan.v1`
- `common.element.wood`
- `common.element.fire`
- `common.element.earth`
- `common.element.metal`
- `common.element.water`
- `common.branch.chen`
- `common.branch.xu`
- `common.branch.chou`
- `common.branch.wei`
- `liuyao.state.month-supported`
- `liuyao.state.month-broken`
- `liuyao.state.day-supported`
- `liuyao.state.day-clashed`
- `liuyao.state.void`

### Workflow

1. Use TOMB_MAP exactly: common.element.wood->tomb:common.branch.wei, common.element.fire->tomb:common.branch.xu, common.element.metal->tomb:common.branch.chou, common.element.water->tomb:common.branch.chen, common.element.earth->tomb:common.branch.chen.
2. Inspect ganzhi.month, ganzhi.day, moving primary branches, and moving changed branches for the mapped tomb branch, recording the exact entry source.
3. Evaluate liuyao.state.month-supported and liuyao.state.day-supported beside liuyao.state.month-broken and liuyao.state.day-clashed on every selected line before distinguishing storage-like and constraint-like hypotheses; keep mixed markers unresolved.
4. If the mapped tomb branch appears in ganzhi.voidBranchIds or the selected line carries liuyao.state.void, record a void countercondition without assuming release or continuation.
5. Use TOMB_RELEASE_PAIRS exactly: tomb:common.branch.wei->release:common.branch.chou, tomb:common.branch.xu->release:common.branch.chen, tomb:common.branch.chou->release:common.branch.wei, tomb:common.branch.chen->release:common.branch.xu.
6. Treat a mapped release branch as a candidate only when it appears in month, day, a changing line, or changed.branchId; these four release branches map to common.element.earth, so test common.element.earth against every selected focus through GENERATION_CYCLE common.element.wood->common.element.fire, common.element.fire->common.element.earth, common.element.earth->common.element.metal, common.element.metal->common.element.water, common.element.water->common.element.wood.
7. Also counter-check the release element through CONTROL_CYCLE common.element.wood->common.element.earth, common.element.earth->common.element.water, common.element.water->common.element.fire, common.element.fire->common.element.metal, common.element.metal->common.element.wood; an opposing branch is not presumed supportive.
8. When a moving line changes to its TOMB_MAP branch, record a conditional changed-tomb transition and cross-check liuyao.state.void, liuyao.state.month-broken, and liuyao.state.day-clashed facts.
9. Return tomb candidates, entry sources, strength context, release counter-effects, and missing evidence without assigning a result.
10. This workflow implements liuyao.claim.tomb-storage.v1, approved by the normalization-safety-review at revision task-1-claim-rule-review.2026-09-03 (standards/reviews/liuyao/jingfang-zengshan-claim-rules.yaml).

### Supporting indicators

- `liuyao.state.month-supported`
- `liuyao.state.day-supported`

### Counter-indicators

- `liuyao.state.month-broken`
- `liuyao.state.day-clashed`
- `liuyao.state.void`

### Output obligations

- `tomb-candidates`
- `entry-source`
- `strength-context`
- `void-and-release-counterchecks`
- `unresolved-conditions`

### Report mapping

| Output obligation | Existing report field |
| --- | --- |
| `tomb-candidates` | `structuralDiagnosis` |
| `entry-source` | `structuralDiagnosis` |
| `strength-context` | `structuralDiagnosis` |
| `void-and-release-counterchecks` | `structuralDiagnosis` |
| `unresolved-conditions` | `limitations` |

Preserve supporting, counter, conflict, and unavailable states separately. Never fill an unavailable prerequisite from memory or source narrative.

### Safety policy

- Do not activate methodology outside `liuyao.school.jingfang-zengshan.v1` or the method cards explicitly declared in `requires`.
- Do not present death, financial, incarceration, legal, or medical claims as any outcomes.
- Do not perform cross-school mixing from undeclared methods.
- Do not perform deterministic outcome from tomb-storage evidence.
- Do not perform diagnosis, prognosis, or treatment from tomb-storage evidence.
- Do not perform numeric outcome scoring from tomb-storage evidence.
- Do not perform professional advice from tomb-storage evidence.
- Do not perform remediation or purchase prescription from tomb-storage evidence.
- Do not perform retrospective fitting from known events.
- Do not perform suppressed counterevidence from tomb-storage evidence.
- Do not perform unsupported favorability from tomb-storage evidence.
- Do not perform unsupported force aggregation from tomb-storage evidence.

### Source locators and revisions

- Source `johnson-liuyao-divination`
  - Locator: `references/04-动静暗破.md#L10-L22`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: The exact opposition pairs are reused only to identify release candidates, not to import month-break meanings.
- Source `johnson-liuyao-divination`
  - Locator: `references/07-墓库论.md#L5-L24`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Element-to-tomb mapping is retained as a deterministic candidate lookup without narrative meaning.
- Source `johnson-liuyao-divination`
  - Locator: `references/07-墓库论.md#L25-L35`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Entry locations are retained only when the corresponding month, day, moving, or changed branch is emitted.
- Source `johnson-liuyao-divination`
  - Locator: `references/07-墓库论.md#L36-L44`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Storage and constraint alternatives are conditionalized on independent strength markers, not assumed.
- Source `johnson-liuyao-divination`
  - Locator: `references/07-墓库论.md#L45-L74`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Void and opposing-branch effects are retained as bilateral counter-checks; asserted outcomes are excluded.
- Source `johnson-liuyao-divination`
  - Locator: `references/07-墓库论.md#L86-L98`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: The summary is used only as a candidate checklist, never as a result template.
- Source `johnson-liuyao-method-authority`
  - Locator: `references/07-墓库论.md#L5-L24`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Owner-attested method authority backing liuyao.claim.tomb-storage.v1 (standards/reviews/liuyao/jingfang-zengshan-claim-rules.yaml).

**End method card:** `liuyao.method.tomb-storage.v1`

## Method card `liuyao.method.timing.v1`

- Method card ID: `liuyao.method.timing.v1`
- School profile ID: `liuyao.school.jingfang-zengshan.v1`
- Topic: `timing`
- Version: `1`
- Status: `school-specific`

### Requires

- `liuyao.school.jingfang-zengshan.v1`
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
- `common.element.wood`
- `common.element.fire`
- `common.element.earth`
- `common.element.metal`
- `common.element.water`
- `liuyao.state.month-supported`
- `liuyao.state.month-broken`
- `liuyao.state.day-supported`
- `liuyao.state.day-clashed`
- `liuyao.state.void`

### Workflow

1. Require an explicit time horizon from the question contract, a resolved focus line, and non-null ganzhi; otherwise mark timing procedure unavailable.
2. Record the focus branchId, elementId, changing status, exact liuyao.state.month-supported, liuyao.state.day-supported, liuyao.state.month-broken, liuyao.state.day-clashed, and liuyao.state.void markers, changed.branchId when present, and prior combination or tomb candidates.
3. Use BRANCH_ELEMENT_MAP exactly: common.branch.yin|common.branch.mao=>common.element.wood; common.branch.si|common.branch.wu=>common.element.fire; common.branch.chen|common.branch.xu|common.branch.chou|common.branch.wei=>common.element.earth; common.branch.shen|common.branch.you=>common.element.metal; common.branch.hai|common.branch.zi=>common.element.water.
4. Use GENERATION_CYCLE exactly as common.element.wood->common.element.fire, common.element.fire->common.element.earth, common.element.earth->common.element.metal, common.element.metal->common.element.water, common.element.water->common.element.wood, and CONTROL_CYCLE exactly as common.element.wood->common.element.earth, common.element.earth->common.element.water, common.element.water->common.element.fire, common.element.fire->common.element.metal, common.element.metal->common.element.wood.
5. Use COMBINE_PAIRS exactly: common.branch.zi+common.branch.chou, common.branch.yin+common.branch.hai, common.branch.mao+common.branch.xu, common.branch.chen+common.branch.you, common.branch.si+common.branch.shen, common.branch.wu+common.branch.wei.
6. Use OPPOSITION_PAIRS exactly: common.branch.zi&lt;>common.branch.wu, common.branch.chou&lt;>common.branch.wei, common.branch.yin&lt;>common.branch.shen, common.branch.mao&lt;>common.branch.you, common.branch.chen&lt;>common.branch.xu, common.branch.si&lt;>common.branch.hai.
7. From explicit focus facts only, set STATIC_TRIGGER_CANDIDATES to the focus value branch plus its exact OPPOSITION_PAIRS partner when changing is false. For a changing line, set MOVING_TRIGGER_CANDIDATES to the focus value branch plus its COMBINE_PAIRS partner only when no progression or retreat transition matched; when either transition matched, do not also emit MOVING_TRIGGER_CANDIDATES and use only the source-specific map below.
8. When liuyao.state.month-broken is present, set BROKEN_TRIGGER_CANDIDATES to the focus value branch plus its combine partner; when liuyao.state.void is present, set VOID_TRIGGER_CANDIDATES to the focus value branch plus its opposition partner. liuyao.state.day-clashed remains a countercheck rather than a separate deterministic window.
9. Use TOMB_RELEASE_PAIRS exactly: tomb:common.branch.wei->release:common.branch.chou, tomb:common.branch.xu->release:common.branch.chen, tomb:common.branch.chou->release:common.branch.wei, tomb:common.branch.chen->release:common.branch.xu; retain only the mapped release branch from a prior tomb candidate. For a prior pair or triad, retain only its explicit missing participant or exact opposing branch.
10. Record COUNTER_ONLY_FOCUS only when neither liuyao.state.month-supported nor liuyao.state.day-supported is present and at least one counter marker is present; this is not a weak classification. Its conditional support-branch candidates are only branches whose BRANCH_ELEMENT_MAP element equals or generates the focus element through GENERATION_CYCLE.
11. Record TOO_STRONG_UNAVAILABLE because LiuyaoReading has no strength magnitude, growth-stage, or multiple-support threshold; do not derive a too-strong class or its upstream tomb/opposition timing rule from support markers alone.
12. When the moving-line card matched an exact progression transition, use PROGRESSION_TRIGGER_MAP exactly: common.branch.yin->common.branch.mao=>current:common.branch.yin; common.branch.si->common.branch.wu=>current:common.branch.si; common.branch.shen->common.branch.you=>current:common.branch.shen; common.branch.hai->common.branch.zi=>current:common.branch.hai; common.branch.chou->common.branch.chen=>current:common.branch.chou; common.branch.chen->common.branch.wei=>current:common.branch.chen; common.branch.wei->common.branch.xu=>current:common.branch.wei. PROGRESSION_TRIGGER_CANDIDATES contain only the primary/current endpoint.
13. When the moving-line card matched an exact retreat transition, use RETREAT_TRIGGER_MAP exactly: common.branch.mao->common.branch.yin=>changed:common.branch.yin+opposition:common.branch.shen; common.branch.wu->common.branch.si=>changed:common.branch.si+opposition:common.branch.hai; common.branch.you->common.branch.shen=>changed:common.branch.shen+opposition:common.branch.yin; common.branch.zi->common.branch.hai=>changed:common.branch.hai+opposition:common.branch.si; common.branch.chen->common.branch.chou=>changed:common.branch.chou+opposition:common.branch.wei; common.branch.wei->common.branch.chen=>changed:common.branch.chen+opposition:common.branch.xu; common.branch.xu->common.branch.wei=>changed:common.branch.wei+opposition:common.branch.chou. RETREAT_TRIGGER_CANDIDATES contain only the changed endpoint and that branch's opposition partner.
14. Express candidates as canonical branch triggers and relative month, day, or stated-horizon units; do not manufacture a Gregorian date from branch symbolism.
15. For each trigger, use BRANCH_ELEMENT_MAP with GENERATION_CYCLE and CONTROL_CYCLE to record its element relation to the focus and other selected lines, plus any exact opposition, combination, break, void, or competing condition it introduces.
16. Intersect independent prerequisites when more than one gate is present; retain conflicting windows instead of choosing one favorable trigger.
17. Label every candidate as fact-backed, conditional, or unavailable according to emitted inputs and return the evidence boundary without certainty language.
18. This workflow implements liuyao.claim.timing.v1, approved by the normalization-safety-review at revision task-1-claim-rule-review.2026-09-03 (standards/reviews/liuyao/jingfang-zengshan-claim-rules.yaml).

### Supporting indicators

- `liuyao.state.month-supported`
- `liuyao.state.day-supported`

### Counter-indicators

- `liuyao.state.month-broken`
- `liuyao.state.day-clashed`
- `liuyao.state.void`

### Output obligations

- `time-horizon`
- `focus-state`
- `candidate-trigger-branches`
- `state-and-transition-classes`
- `competing-effects`
- `evidence-boundary`

### Report mapping

| Output obligation | Existing report field |
| --- | --- |
| `time-horizon` | `timeline` |
| `focus-state` | `timeline` |
| `candidate-trigger-branches` | `timeline` |
| `state-and-transition-classes` | `timeline` |
| `competing-effects` | `scenarios` |
| `evidence-boundary` | `limitations` |

Preserve supporting, counter, conflict, and unavailable states separately. Never fill an unavailable prerequisite from memory or source narrative.

### Safety policy

- Do not activate methodology outside `liuyao.school.jingfang-zengshan.v1` or the method cards explicitly declared in `requires`.
- Do not present death, financial, incarceration, legal, or medical claims as any outcomes.
- Do not perform cross-school mixing from undeclared methods.
- Do not perform deterministic outcome from timing evidence.
- Do not perform diagnosis, prognosis, or treatment from timing evidence.
- Do not perform numeric outcome scoring from timing evidence.
- Do not perform professional advice from timing evidence.
- Do not perform remediation or purchase prescription from timing evidence.
- Do not perform retrospective fitting from known events.
- Do not perform suppressed counterevidence from timing evidence.
- Do not perform unsupported calendar date from timing evidence.
- Do not perform unsupported favorability from timing evidence.

### Source locators and revisions

- Source `johnson-liuyao-divination`
  - Locator: `references/04-动静暗破.md#L10-L22`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: The exact opposition table is used for conditional trigger lookup only; month-break consequence claims are excluded.
- Source `johnson-liuyao-divination`
  - Locator: `references/04-动静暗破.md#L52-L79`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Void state membership remains separate from value-fill and opposition trigger candidates; asserted effects are excluded.
- Source `johnson-liuyao-divination`
  - Locator: `references/05-进退神化.md#L5-L25`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Exact progression and retreat pairs gate candidate triggers without importing direction or outcome meanings.
- Source `johnson-liuyao-divination`
  - Locator: `references/06-三合六合.md#L43-L65`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Exact combine pairs support conditional pair-trigger lookup; binding and activation meanings remain unresolved.
- Source `johnson-liuyao-divination`
  - Locator: `references/06-三合六合.md#L66-L77`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Combination-opposition interaction is retained only as a competing-trigger countercheck without valence.
- Source `johnson-liuyao-divination`
  - Locator: `references/07-墓库论.md#L45-L74`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Tomb release branches and their bilateral element effects are retained as candidates, never promised windows.
- Source `johnson-liuyao-divination`
  - Locator: `references/08-断卦步骤.md#L94-L123`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Selected rows become conditional candidates; progression uses current only, while retreat uses changed plus opposition, with counterchecks.
- Source `johnson-liuyao-divination`
  - Locator: `references/08-断卦步骤.md#L135-L137`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: The safety boundary is retained: method output is reflective procedure, not factual prediction or professional advice.
- Source `johnson-liuyao-method-authority`
  - Locator: `references/08-断卦步骤.md#L94-L123`
  - Revision: `1a5a78b513c0e7b46dfb29f74043bcf978c32a3e`
  - Normalization note: Owner-attested method authority backing liuyao.claim.timing.v1 (standards/reviews/liuyao/jingfang-zengshan-claim-rules.yaml).

**End method card:** `liuyao.method.timing.v1`
