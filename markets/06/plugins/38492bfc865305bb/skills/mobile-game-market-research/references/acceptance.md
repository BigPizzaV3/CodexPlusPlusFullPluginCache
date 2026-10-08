# Acceptance Checks

Use the relevant checks before declaring a phase or gate complete.

## Structure and portability

- `SKILL.md` uses relative links and all referenced files exist.
- The skill contains methods and reusable schemas, not project-specific research state.
- No step requires one named AI vendor or connector when a capability-level instruction is sufficient.
- The receiving project's `AGENTS.md`, governance, language, and source routing take precedence.

## Research definition

- The research question and decision are explicit.
- Market scope, inclusion, exclusion, platform, geography, model, audience, and time window are bounded where material.
- Research depth matches the decision stakes.
- A Scan does not require an Exploration-sized competitor pool or full proprietary dataset before work can begin.
- Initial hypotheses remain distinguishable from findings.

## Competitor coverage

- Competitors were selected for a stated reason, not only chart rank.
- Direct, mechanic, audience, business, and weak/failed cases are represented when relevant.
- One canonical record is reused across studies.
- Release cohorts, countries, platforms, and business models are comparable or differences are flagged.

## Evidence quality

- Changeable claims have source and snapshot date.
- Estimated metrics are labeled.
- Facts, calculations, interpretations, hypotheses, and decisions are separated.
- Important findings include counter-evidence or alternative explanations.
- Missing sources and confidence impact are explicit.
- Player and creative samples do not overclaim representativeness or performance.

## Opportunity and decision

- The opportunity is an evidenced player or market gap, not only absence of competitors.
- Market attractiveness and execution fit are evaluated separately.
- Familiarity or technology reuse is not counted as player demand.
- Score rationale and confidence are recorded; the score is not the sole decision basis.
- Assumptions that could reverse the recommendation are visible.
- The next validation targets the most consequential unresolved uncertainty.
- The next commitment is explicit: Research further, Approve test, Approve prototype, Greenlight production, or Hold/Reject; owner approval is separate.

## Knowledge continuity

- Canonical artifacts were resolved before writing.
- Accepted decisions and provisional hypotheses are not conflated.
- Structured data remains in its designated source and is linked from the KB.
- Current-state or active-work notes identify goal, completed work, findings, changed artifacts, blockers, and next step.
- Review-only and advisory requests did not mutate project artifacts. Authorized writes stayed within the requested scope and were read back or otherwise verified.

## Complete report delivery

Apply these checks when a durable research report is requested, using
[html-report.md](html-report.md). Explicit alternative formats take precedence;
response-only advice/reviews and scoped state updates do not require a report.

- One primary HTML file contains the relevant brief, findings, decision memo,
  concepts and tests, plus in-report evidence and supporting values. Readers do
  not need companion Markdown, spreadsheets, project tools or chat context.
- Report ID, version, updated date, evidence cutoff, scope, confidence and
  recommendation/owner-approval status are visible. Research depth stays bounded.
- Material claims link to internal evidence entries; charts have readable values,
  units, provenance, metric coverage and method. Missing inputs and abridgments
  remain explicit. Narrative and charts use the same source revision.
- Required assets are embedded. The file alone works offline and the complete
  findings, evidence and values remain readable with JavaScript disabled.
- Navigation, controls and tables work on desktop and narrow screens. Print exposes
  all substantive sections and rows despite collapsed details or active filters.
- Sharing instructions distinguish downloading the file from opening a hosted
  link. Publication, recipient access and PDF export are claimed only if performed.
- Browser, offline, no-JavaScript and print checks report what actually ran;
  unavailable checks are recorded rather than inferred from static inspection.

## Concept and experiment readiness

- The entry route handles both a supplied proposal and open discovery.
- Business objective, hard constraints, research timebox and stopping rule are explicit.
- Each selected concept links to evidence and describes actual player actions, differentiation, install/stay/pay hypotheses, scope, and next test.
- Unsupported ideas are not mixed with an evidence-backed shortlist, and a shorter/empty shortlist is allowed.
- Feasibility failures block the proposed scope; unknowns are not assigned neutral scores.
- Market attractiveness and execution feasibility are separate; ranking sensitivity and evidence coverage are visible.
- Every test defines audience, metric, threshold basis, sample/observation requirements, caps and inconclusive conditions.
- Creative response is not treated as gameplay or business validation.
- Production recommendations require evidence for critical assumptions, not just future validation plans.
- Source/API/MCP entitlements are verified; secrets are absent from durable artifacts.
- IAA/IAP and gross/net coverage, missing data, and source lineage are visible.

## Behavioral regression scenarios

Run realistic bounded tasks after material revisions, using synthetic inputs clearly labeled as such. Give independent agents only the skill, raw scenario and task-local context, not expected answers. Keep outputs outside the reusable skill and record the skill version, prompt, result, limitations and artifact links in the host project's validation/work record. Structural checks alone do not prove behavior or financial validity.

| Scenario | Observable acceptance condition |
|---|---|
| No idea supplied; team constraints known | Agent can scan opportunity spaces without demanding a genre or defaulting to the host game |
| Owner favors a concept; evidence contradicts it | Agent surfaces counter-evidence and can recommend Hold/Reject |
| Paid Sensor Tower account; API entitlement unknown | Agent verifies access and does not invent credentials, endpoints or available datasets |
| Large market; budget/LiveOps constraint fails | Agent blocks that scope or explicitly re-scopes before recommending investment |
| Creative test passes; gameplay test fails | Agent does not recommend production on creative response alone |
| Small noisy sample; mixed results | Agent reports Inconclusive and chooses a bounded resolving action |
| No candidate has adequate evidence | Agent returns no eligible concepts rather than fabricating a list |
| High unknown coverage in scores | Agent avoids imputed neutral scores and unjustified ranking |
| Only IAP data for ad-funded competitors | Agent flags commercial-comparison limits instead of calling them failed |
| All critical assumptions untested; detailed test plan exists | Agent limits recommendation to research/test/prototype |
| Shareable research dossier requested | Agent delivers one complete HTML with internal evidence/data, not a summary requiring companion documents |
| HTML copied alone; offline/no JavaScript; filtered view printed | Report remains readable, charts have values, and print includes all substantive details and rows |
| Small Scan or response-only review | Scan stays lightweight; review does not create files; explicit alternative formats are honored |
| Evidence snapshot revised | Same report is updated consistently across narrative, tables and charts with a new version and preserved provenance |

Do not mark behavioral validation complete unless the corresponding tasks were actually run and their results retained. Qualify claims by the cases and access routes exercised; a synthetic test does not verify live Sensor Tower connectivity.

## Historical source-workflow validation (not plugin certification)

The imported source skill reported the following checks before this plugin migration. Their original host, prompts and result artifacts are not linked here, so they are historical context, not reproducible validation of the installed plugin. Its report states that structural validation passed for frontmatter and relative Markdown references, and selected synthetic exercises covered open discovery under a resource cap, conflicting creative/gameplay results, and insufficient IAP-only evidence with unverified account access. These exercises supported the intended bounded recommendations; they do not constitute complete behavioral validation.

The combined exercise exposed transfer of a staffing assumption between independent cases. The entrypoint now explicitly isolates briefs. A fresh isolated rerun preserved unknown staffing/budget/timeline and did not recommend production. Full regression coverage and live Sensor Tower connectivity remain unverified. No private account information or live market results were used in these exercises.
