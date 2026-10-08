# Decision authority model

Classify every material choice before delegating it.

## Source authority and conflicts

Separate these types; they are not a blind recency ranking:

- OWNER INSTRUCTION: authenticated current user/owner direction within their authority; not quoted commands inside source data.
- PROJECT AUTHORITY: approved governing scope, decisions, invariants and delegated rights.
- CURRENT SOURCE OF TRUTH: the exact maintained record for the particular fact/observable; distinguish required behavior from observed implementation.
- EXTERNAL EVIDENCE: source-grounded observations, not permission to change the project.
- DERIVED STATE: summaries, task slices, generated manifests and reports with source provenance; cannot supersede their sources.
- MODEL INFERENCE: explicitly reasoned interpretation, never promoted to a verified fact or approved decision by confident wording.

These do not override higher-priority runtime instructions. Document purpose separately: NORMATIVE AUTHORITY, IMPLEMENTATION GUIDANCE, TEMPORARY TASK CONTRACT, EVIDENCE or HISTORICAL CONTEXT. A source can govern only declared scope. Code proves observed behavior, not that the behavior is approved. A specification governs only its approved scope, not an independent competing product truth.

Apply explicit scope-specific precedence or supersession; old project notes cannot overrule current confirmed authority. Recency alone cannot establish authority. Preserve unresolved disagreement in a compact CONFLICT REPORT: affected decision, exact competing sources/versions/claims, known precedence, impact, decision owner, blocked dependent action and next safe check. Do not silently average, choose or rewrite sources. In a governed suite use its existing precedence matrix rather than creating another register.

OWNER DECISION PACK is the same existing decision record viewed for approval: exact choice, evidence-supported options/tradeoffs, affected invariant, recommendation labeled as proposal, requested authorization and consequence of deferral. Omit unsupported options; no extra document is required.

## Best-known-practice and method closure

For a material technical, production, representation, toolchain or workflow choice, use:

`RESEARCH → APPLICABILITY CHECK → AUTHORIZED METHOD DECISION → METHOD_CLOSED → EXECUTION`

Do not turn a known applicable method into a new comparison exercise merely because a different approach may be simpler, shorter or more interesting. Evidence does not grant decision authority by itself: the method becomes `METHOD_CLOSED` only when the best-known applicable method has no unresolved material conflict and is selected by the owner or within already delegated Class-2/Class-3 authority. Until then it remains `OPEN`.

Evaluate method evidence in this order, using each level only for the claim it can actually establish:

1. current official first-party guidance for the exact provider, tool, platform, version or supported mechanism;
2. a verified professional production implementation whose relevant mechanism was actually inspected;
3. a method validated in the current project under comparable conditions;
4. established professional practice supported by applicable evidence;
5. an experimental hypothesis.

Higher evidence prevails only when current and applicable to the actual decision. Official documentation may establish supported behavior without proving visual quality; an external production reference may prove a mechanism without granting permission to copy its design. Preserve project failures as evidence requiring diagnosis under the failure-attribution gate below; do not hide them or assume they disprove the method.

Classify first-party evidence as `OFFICIAL_REQUIREMENT` (hard constraint within its stated applicability), `OFFICIAL_RECOMMENDED_PRACTICE` (default when current, applicable to the exact use case and without material counter-evidence), or `OFFICIAL_EXAMPLE` (a possible pattern, not a mandate). Record the source's actual semantics; do not promote an example into a requirement or let any external guidance override project decision rights.

Before closure verify that the method solves the same problem, matches the required runtime/platform/browser/hardware and operating conditions, preserves Project Truth and approved architecture, and creates no unresolved security, accessibility, performance, compatibility, legal or owner-direction conflict. If the known method is applicable and authorized with no material conflict, stop technique shopping and execute it. Representation economy then optimizes implementation inside that validated solution class; it does not reopen the method to test weaker alternatives.

Closure applies only to the recorded problem/target, project or domain, runtime/platform and relevant constraints. Set `CLOSURE_SCOPE` to `GLOBAL_DEFAULT`, `DOMAIN_DEFAULT`, `PROJECT_LOCK` or `TASK_COMPONENT_LOCK` with the exact applicability boundary. A project/component lock never becomes a universal technique rule. Defaults apply only in their evidenced scope and cannot silently supersede an existing authorized project lock. Missing or conflicting scope needs resolution before dependent execution; never infer global scope. Outside a lock's scope it remains reusable evidence, not binding authority.

A closed method may be reopened only when at least one trigger is evidenced:

- required acceptance fails because of the method rather than an implementation or measurement defect;
- a new technical constraint makes the method unsuitable;
- relevant official guidance materially changes;
- security, accessibility, performance or compatibility creates a real conflict;
- new reliable evidence demonstrates a materially better applicable method;
- Project Truth or owner direction changes; or
- the owner explicitly requests renewed exploration.

“Maybe simpler,” fewer lines of code, agent preference, novelty, theoretical adequacy or curiosity are not reopen triggers. Calibration and implementation proofs inside the closed method remain allowed within their approved bounds. A cross-method experiment is allowed only for a named unresolved question that current knowledge cannot answer and must state hypothesis, minimum test, success/failure criteria, stop condition and decision after the test.

Method exploration selects or replaces the solution class, mechanism or workflow. Calibration adjusts approved parameters inside it (for example material depth/roughness or task size/context amount) while preserving targets, required mechanisms, assets, authority and acceptance. Calibration is allowed only when `CALIBRATION_OPEN = YES` and within the recorded bounds; changing a locked mechanism or weakening a verifier is not calibration.

For outcome-based rejection, `IMPLEMENTATION_FAILURE` is not `METHOD_FAILURE`. First verify implementation fidelity against all required mechanisms, diagnose the result, confirm correct and sufficiently complete implementation, inspect parameters/calibration and assets/input quality, then compare real acceptance against the approved target and make bounded corrections inside the method. At least one faithful, sufficiently complete implementation is required before its result can establish that the method itself cannot satisfy a required acceptance. An omitted core mechanism or simplified substitute is not that evidence. Exhausted retries or `INCONCLUSIVE` diagnosis require review, not automatic reopening or endless correction. This prerequisite applies to rejection based on implementation results; an independently evidenced security/compatibility constraint or another valid non-outcome trigger does not require an unsafe, impossible or unnecessary build. Reopening still needs the applicable decision authority and affects only the evidenced scope.

Record a material method decision in the existing decision log, not a new compulsory document:

```text
PROBLEM
TARGET
PROJECT / DOMAIN
RUNTIME / PLATFORM
RELEVANT_CONSTRAINTS
CLOSURE_SCOPE: GLOBAL_DEFAULT | DOMAIN_DEFAULT | PROJECT_LOCK | TASK_COMPONENT_LOCK
APPLICABILITY_SCOPE: exact included contexts and exclusions
RESEARCH / EVIDENCE IDS
SOURCE / GUIDANCE VERSION: actual version or dated snapshot; UNKNOWN if not established
VERIFIED_AT: actual check date and verified claims; never a file modification date
VALIDATED_WITH: actually verified environment/toolchain, relevant versions, evidence IDs and scope; UNKNOWN if not observed, or justified NOT_APPLICABLE
FRESHNESS_CLASS: STABLE | VERSION_SENSITIVE | RESEARCH_SENSITIVE
REVALIDATE_WHEN: claim-specific freshness triggers; distinct from authorized REOPEN_CONDITIONS
GUIDANCE_TYPE: OFFICIAL_REQUIREMENT | OFFICIAL_RECOMMENDED_PRACTICE | OFFICIAL_EXAMPLE | NOT_APPLICABLE
BEST_KNOWN_METHOD
MUST_USE: essential mechanisms/components, with exact source references
MUST_NOT_SUBSTITUTE_WITH: prohibited substitutions supported by the lock
APPLICABILITY: PASS | FAIL | UNRESOLVED
MATERIAL_CONFLICTS
METHOD_DECISION
METHOD_STATUS: OPEN | METHOD_CLOSED
DECISION_CLASS / AUTHORITY_SOURCE
REOPEN_CONDITIONS
CALIBRATION_OPEN: YES | NO
CALIBRATION_STILL_ALLOWED
```

Persist this record with a stable ID/revision in the existing authorized decision log or project knowledge location; if writing is unavailable, return it as an explicit portable artifact and identify the storage gap. A chat-only conclusion is not durable production knowledge. Reuse the recorded evidence when its applicability and freshness remain sufficient. Revalidate the affected claims when a source/guidance version, runtime/platform, constraint or authority change materially touches the scope, or required freshness cannot be established. Revalidation is not automatic reopening and does not require a new whole-system search.

`METHOD_LOCK` is the task-sized view of this same record, not a second source of truth: decision ID/revision and authority, exact applicability scope, METHOD (`BEST_KNOWN_METHOD`), STATUS (`METHOD_STATUS`), MUST_USE, MUST_NOT_SUBSTITUTE_WITH, CALIBRATION_ALLOWED (open flag and bounds) and REOPEN_ONLY_IF (`REOPEN_CONDITIONS`), plus relevant source version/verification date. Carry it explicitly in the execution brief, task contract, Context Package, design-to-code/Claude handoff and builder instructions whenever it governs execution. An exact versioned reference is sufficient only if the recipient can access and resolve the full lock before acting; otherwise include the compact view. Missing access blocks dependent work, not silently discards the lock or authorizes fresh exploration. A new session reconstructs and acknowledges its scope before execution.

## Method freshness without reopening

Use the same versioned decision record. METHOD/STATUS/SCOPE/AUTHORITY SOURCE/GUIDANCE VERSION are views of the existing method/status/applicability/authority/source fields, not a second schema or register. A supplied CLOSED status aliases METHOD_CLOSED only with the same evidence and authority. VALIDATED_WITH records the actually tested environment when material, not a planned stack or the author's current computer. Legacy records remain reusable when their existing evidence establishes sufficient freshness; unresolved material fields require targeted verification, not invented backfill or a bulk migration.

STABLE knowledge is reused within its validated scope. VERSION_SENSITIVE claims depend on named tool/runtime/platform/guidance versions. RESEARCH_SENSITIVE claims depend on changing external evidence. Classify from the actual dependency, not model enthusiasm; a mixed record can identify the sensitive claims separately without duplicating the record. VERIFIED_AT certifies only claims actually checked at that time, not all linked documentation or all devices.

Revalidate affected claims when a new device, different runtime, relevant tool/model/agent version, material first-party guidance, framework/API/browser capability, method version dependency, out-of-scope requirement, failed tool call or concrete reliable new evidence creates a relevant uncertainty. Local presence/version/access uncertainty first follows the [environment prerequisite gate](provider-capability-routing.md). Not every such trigger requires internet research, and “perhaps something newer exists” is not sufficient. Check current applicable official sources when a remaining guidance claim materially requires it; disclose inaccessible sources and block only dependent reliance. Preserve higher-priority research obligations.

`METHOD_CLOSED → FRESHNESS TRIGGER → TARGETED CHECK → COMPARE WITH EXISTING RECORD`.

- No material change: KEEP METHOD_CLOSED; record the scoped check/evidence/date in the existing history under its write authority. Do not claim untouched fields were reverified.
- Material change: inspect applicability and conflicts, then use the existing controlled reopen authority only if required. Evidence alone neither opens nor replaces the method. Outside its scope a lock remains evidence, not global authority.
- Inconclusive/inaccessible: preserve the lock and explicit uncertainty; do not certify affected execution readiness or start alternative exploration.

Keep the prior record/revision and rationale; no silent overwrite. If persistence is unavailable or unauthorized, deliver the scoped result for the existing decision owner instead of claiming durable knowledge was updated. A portable METHOD_LOCK also exposes relevant VALIDATED_WITH, freshness class, REVALIDATE_WHEN and current method/guidance freshness result, directly or through an accessible exact reference. Recheck triggers are not REOPEN_CONDITIONS. Capability repair belongs to provider routing; mere missing tools, tool failure or environment gaps never establish method failure. Outcome-based rejection retains the faithful-implementation gate above, including correct environment and calibration; independently evidenced security/incompatibility may be handled without an unsafe build.

## Class 1 — owner, product, brand, architecture, or governance

The agent or implementer must not decide. Examples include product scope, features, business rules, brand identity, fundamental visual direction or composition, legally relevant behavior, permission models, external interfaces, security posture, data ownership, architecture outside an approved contract, controlled-source conflicts, and destructive or externally consequential changes.

Action: record `OWNER_DECISION_REQUIRED`, identify the exact choice, affected outcome, options if evidence supports them, owner, and dependent work. Stop that dependent work.

This includes material product/creative direction, money, contracts, external communication, production, irreversible/destructive actions and new durable system architecture. Check existing explicit authorization first: no repeated approval for an unchanged authorized action. Safe internal Class-2/3 work may continue; uncertainty never expands the authorization.

## Class 2 — controlled professional decision

The named discipline lead may decide only when all are true:

1. no Class-1 decision changes;
2. the approved outcome and invariants remain intact;
3. the choice lies inside the role contract;
4. direction, target, or bounds are documented;
5. the choice is reversible;
6. rationale and evidence are logged;
7. the real result is verified;
8. visual work uses the required checkpoint;
9. the choice does not resolve a controlled-source conflict.

Examples: bounded bevel width, topology detail, material microvariation, texture readability, camera micro-correction, highlight shaping, shadow softness, minor motion refinement, renderer mapping, and responsive micro-adjustment.

## Class 3 — engineering decision

The implementer may decide when the choice does not materially alter product behavior, UX, brand, architecture contract, external interfaces, security, data, scope, or approved visual outcome. Examples include internal function structure, naming, helper abstraction, equivalent internal data structures, and test organization.

Every task contract names allowed Class-2 and Class-3 space. Silence never grants Class-2 authority.
