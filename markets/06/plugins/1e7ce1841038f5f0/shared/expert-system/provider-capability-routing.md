# Provider-aware capability routing

The existing `$design-optimal-ai-workflow` owns toolchain selection; `$orchestrate-projects` owns cross-phase coordination. This is their shared contract, not a new dispatcher or integration.

## Select by need

For each material step record required outcome/modality, input/output artifact, data boundary, required tools, cost/latency constraints, actual access, acceptance and fallback. Prefer an already suitable deterministic tool or native capability over a new skill, connector or agent. Availability alone never earns a stage. User-selected tools remain constraints unless the owner approves a change.

Read only the applicable provider profile. Verify changing features, access, prices and permission semantics in current official documentation and the actual target surface before relying on them. A brand name is not a capability test. Local desktop, browser chat, cloud work and API surfaces need separate checks. No guarantee that local paths, skills or accounts carry between them.

Apply the [method-decision lifecycle](decision-authority-model.md) before reopening an already selected provider/tool workflow. Revalidating a time-sensitive capability does not itself reopen an applicable `METHOD_CLOSED` decision; compare alternatives only when a canonical reopen trigger is evidenced.

## Execution-surface and environment truth

Use the [expert routing model](expert-routing-model.md) to distinguish worker, capability and execution surface. Represent the environment portably with an existing equivalent or the smallest applicable class: `LOCAL_HOST` plus observed OS when material, `LOCAL_PROJECT_ENVIRONMENT`, `SANDBOX`, `VM`, `CONTAINER`, `REMOTE_HOST`, `BROWSER`, `COMPUTER_USE_SESSION`, `CONNECTOR` or `UNKNOWN`. A worker identity, familiar path, product name or OS-like shell output does not establish the environment. The environment evidence must match the claim: a VM or sandbox result cannot prove a local-host fact, and sender readiness cannot certify a receiver's device.

Treat local shell/terminal as a capability and execution surface, not a universal worker or default. It is often suitable for deterministic filesystem, Git, hashing, toolchain, build, test, schema, automation, transformation or artifact facts when the correct scoped environment is accessible and authorized. Prefer direct machine evidence for a machine-verifiable claim, but let that evidence prove only the observed machine fact; it does not create product, owner, business, deployment or release authority. A shell log cannot certify visual, motion, material or other perceptual acceptance. Combine technical and visual surfaces when the task requires both.

Before shell reliance verify the actual surface, project/path access, required tool and version, read/write boundary, permissions and task scope. `CAN_READ != CAN_MODIFY`; technical ability to run a command is not authorization to change state. Distinguish command failure, missing tool, permission denial, wrong environment, missing path/source, verification failure and method failure. A missing CLI is a `CAPABILITY_GAP`, not permission to install, update, use a weaker environment, expose secret values or reopen a closed method. For secret checks prefer scoped status such as `EXISTS`, `CONFIGURED`, `AVAILABLE`, `MISSING` or `UNAVAILABLE` when content is unnecessary.

Provider capabilities remain time-sensitive. Do not encode that Work, Cowork or any other worker always has local files, shell, browser, computer use or connector access. Verify each required capability and surface in the actual task context. If a repeated deterministic operation may deserve reusable local tooling, propose it only after repeated need, stable method, clear benefit and applicable authority; do not create a script, daemon, agent or service automatically.

## Evidence states (not an automatic ladder)

| State | Required meaning |
|---|---|
| DESIGNED | Proposed workflow only |
| AVAILABLE | Capability is offered in the identified surface; name whether observed or documented |
| INSTALLED | Relevant package/application observed in that target environment |
| CONNECTED | Authorized connection to the specific target observed; no secrets in evidence |
| CONFIGURED | Relevant settings inspected for the declared task |
| TESTED | A named test actually ran, with result including failures |
| VERIFIED | Evidence establishes the specific claimed outcome, version/environment, scope and date |

Record unknown, inaccessible or NOT_APPLICABLE with a reason instead of inventing a stage. These labels describe different facts: TESTED can fail; installed can be disconnected; documented availability does not prove account access. A relevant change invalidates affected verification, not necessarily the entire workflow. Do not certify all capabilities from one successful call.

## Environment prerequisite gate

For technical execution derive capabilities from the approved task and selected method before relying on tools. Use `TASK → SELECTED / CLOSED METHOD → REQUIRED CAPABILITIES → ENVIRONMENT PREFLIGHT → EXECUTION`. This gate is also reached through the shared task contract by domain skills; do not copy it into each skill. A method, local skill file or provider brand never proves executable access.

Represent the task-relevant prerequisite contract in existing task/method sources, by accessible reference when sufficient:

```text
REQUIRED_CAPABILITIES / OPTIONAL_CAPABILITIES
MINIMUM_OR_SUPPORTED_VERSION: evidence-supported range, or UNKNOWN / justified NOT_APPLICABLE
SUPPORTED_ENVIRONMENT / REQUIRED_RUNTIME / REQUIRED_BROWSER_OR_RENDERER
REQUIRED_LOCAL_OR_CLOUD_ACCESS / REQUIRED_PERMISSIONS
FALLBACK_ALLOWED: YES | NO
FALLBACK_METHOD: exact already validated, sufficient and authorized alternative, or NONE
```

These are semantic fields, not a mandatory new file. Preserve existing equivalent fields. Version minima come from applicable authoritative requirements, not guesses or the newest release. Optional means acceptance and safety still hold without it; a required renderer, security check or reviewer cannot be relabeled optional to pass. A fallback needs evidence and authority within the method lock, including substitution boundaries; absent that, FALLBACK_ALLOWED is NO. Availability does not authorize a spontaneous fallback.

Inspect only required/decision-relevant optional capability: actual target environment and execution surface, tool availability, active runtime/resolved version, required SDK/browser/renderer, files, connector/service, access and permissions, with a bounded functional probe when the claim needs it. Distinguish documented support, actual availability, scoped verification and task sufficiency. Installed or TESTED alone is not task-sufficient; tests may fail. Match observations to the required range/environment and record evidence, scope, actual observation date and gaps without secrets.

Use supported read-only inspection first. Do not launch package bootstraps, installers, auto-downloading runners, account activation or configuration changes as a “probe.” Detect the actual OS/architecture/local-or-cloud context; never assume macOS, Homebrew, a particular browser/version, a user's paths or an existing agent configuration. If an inspection itself may mutate state, obtain the applicable authority or report the limit. Fixtures or another user's device are not observations of this execution environment.

| ENVIRONMENT_STATUS | Meaning / next step |
|---|---|
| READY | All required capabilities are accessible, authorized, compatible and sufficiently verified for this task. |
| READY_WITH_OPTIONAL_GAPS | Same required coverage; only explicitly optional missing capabilities, with no acceptance/safety impact. |
| CAPABILITY_GAP | A required tool/runtime/SDK/service capability is absent or not functioning; report ENVIRONMENT_CAPABILITY_GAP and the missing prerequisite. |
| VERSION_CONFLICT | Observed version is outside the task's supported requirements. A mere version change without incompatibility instead triggers targeted verification. |
| PERMISSION_GAP | Required access is not authorized or available. Do not work around it. |
| UNSUPPORTED_ENVIRONMENT | Evidence establishes the target cannot support a required capability; route applicability review. |
| UNKNOWN | Required presence, compatibility, access or verification cannot yet be established. Perform the smallest safe check or report the blocker. |

Retain every material gap when several apply; choosing a headline status must not hide other blockers. Only READY or a justified READY_WITH_OPTIONAL_GAPS passes this prerequisite gate. It does not certify overall task readiness, method freshness, review completion or production quality. Other authority/specification/acceptance gates remain necessary.

MISSING TOOL ≠ METHOD FAILURE ≠ permission to reopen or substitute a method. TOOL FAILURE and ENVIRONMENT GAP are not METHOD FAILURE either. For a closed method retain its lock; provide/restore the required capability under existing installation authority, or block and report. Only evidence that the capability cannot actually be provided and creates a real new constraint can enter the canonical applicability/reopen process; absence alone cannot. Diagnose environment, fidelity, calibration and measurement before outcome-based method rejection; preserve the canonical exception for independently evidenced unsafe/impossible constraints.

Reuse the confirmed task-sufficient status only for its observed environment, scope and claims. Recheck affected claims after environment/device/runtime changes, relevant tool/model/agent updates, changed requirements or method prerequisites, failed tool calls, or unknown required freshness. No permanent full-machine inventory or parallel capability registry.

For handoff use `CAPABILITY_CONTEXT`, a compact view of this gate in the existing task/context packet: required toolchain and prerequisite reference, ENVIRONMENT_STATUS, verified relevant versions with evidence/date/environment identity, missing capabilities, permission/optional-gap limits, applicable fallback authority and recheck triggers. Carry the separate METHOD_LOCK and method/guidance freshness outcome with it. The receiver confirms the evidence applies to its own environment; sender READY cannot certify a different device. Include accessible content when references cannot be resolved.

## Controlled capability repair and updates

New version available does not mean update required. Before an installation, enablement, configuration change or update, check relevance, compatibility, project impact, recovery/rollback and material benefit. Valid update reasons include a security/compatibility requirement, needed capability, relevant bugfix, evidenced measurable benefit or an applicable owner/project policy—not novelty. These reasons do not themselves grant authority.

For an unresolved gap report REQUIRED, WHY, RECOMMENDED_INSTALL_METHOD, VERSION_OR_RANGE, IMPACT (including recovery) and OWNER_OR_USER_ACTION_REQUIRED (YES/NO). Recommend only a verified appropriate installation route; otherwise mark the route UNKNOWN and state the next check. Inspect existing authorization and permitted scope; do not silently install, enable services, alter permissions or change project toolchains. NO user action is justified only when already authorized and safely executable within current permissions. After authorized repair, rerun affected capability checks before claiming READY. A proposed install or a successful download is not proof of usable capability.

## Research → Plan → Implement → Verify

For material work identify actor, input, output and acceptance at each applicable transition: source-backed findings → authorized plan/spec → bounded implementation and evidence → required independent verification. One simple task can combine stages. Use the existing task/handoff/evidence records, not four mandatory files. The planner does not become product authority; the builder does not independently accept its own material output.

When no authorized connector exists, provide an accessible manual handoff with the [Context Package](context-package.md) and expected report. Never say the external agent ran. Tool activation, purchases, uploads, external communication and production remain within [decision authority](decision-authority-model.md), not implied by routing.
