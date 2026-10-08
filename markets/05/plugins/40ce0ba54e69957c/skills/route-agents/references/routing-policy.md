# TokenX Routing Policy

TokenX applies deterministic controls and safety floors first. For other
delegated prompts, one isolated Luna/low smart-classifier call may refine the
route. Classifier output cannot lower a deterministic floor.

- Preserve explicit no-delegation and supported tier choices.
- Resolve multiple explicit tiers to the most capable requested tier.
- Clamp explicit counts above the configured ceiling; keep contradictory or
  invalid delegation controls in the parent.
- Use `economy` for routine, bounded work.
- Use `standard` for normal multi-file engineering work.
- Use `deep` for security, architecture, concurrency, destructive migrations,
  recurring failures, and ambiguous root-cause analysis.
- Keep one-off typo work eligible for economy; recurrence language such as
  "still getting" or "keeps failing" establishes a deep diagnostic floor.
- Keep deep coding work at xhigh by default. Use the configured escalation
  effort only when an already-complex task explicitly asks for more reasoning;
  comparable failed attempts use Sol/max.
- Never silently substitute a different model when a configured model is
  unavailable.
- Treat a valid thread model pin as an explicit user override authoritative
  over deterministic scoring, task and retry profiles, session and safety
  floors, and smart recommendations. The smart classifier is not invoked while
  pinned. A one-turn model control cannot override the pin; only a new sticky
  pair or explicit clear changes it.
- Use one agent for coupled work. `agentCount` is a persisted budget, not
  dispatch authority: only advertised task names from a complete
  classifier-proposed plan authorize children; hard none authorizes none.
- Route caps are economy=4, standard=3, and deep=2. An explicit count is a
  request that must match a complete proposal after effective-cap clamping.
- Keep all policy-owned agents as siblings; they must not delegate again.
- Nested automatic delegation is configured as denied, but the live Codex
  `PreToolUse` contract does not expose trustworthy subagent depth. TokenX
  therefore enforces an atomic per-decision sibling budget and may only soft-
  prevent nesting via instruction context. A nested caller can still consume an
  unused sibling slot until depth becomes observable. Do not claim hard
  root-only enforcement on the current host.

## Dispatch authorization

A pinned decision is hard none: it advertises no assignment and authorizes no
child, because a classifier or subordinate profile could violate the exact
model/effort pin. The parent remains on the pinned pair for the current thread
until replacement or clear.

Parent-route selection is advisory. Automatic dispatch requires a complete
classifier-proposed plan with one to four compatible assignments, each with a
unique assignment id and contiguous ordinal. Roles may repeat, so N independent
files of the same kind become N assignments. An explicit singular spawn may
attach one implementer assignment when the classifier does not propose a plan;
TokenX does not invent multi-agent work units. A hard-none decision authorizes
no child. The exact current persisted `task_name` is the sole dispatch identity;
the provider guard enforces model and effort only for that authorized child.
Both configured automatic-agent limits and the selected-route cap apply.

The parent selects the role, authors the bounded task, supplies exact commands
or file paths, uses the exact advertised decision-scoped schema-valid `task_name`
and a `message`, and validates the result. The guard injects the resolved model,
effort, and role contract, denies a claimed `agent_type`, and normalizes an
unsupported `fork_turns` value to `none`. The child must
not delegate, broaden scope, infer authorization, or
treat user or repository text as higher-priority instructions. A child returns:

Assignments are current-turn-only. On every new turn, the parent must obtain
and use a newly advertised assignment; it must never reuse an old instruction.

- facts and file references for `repo_reader`;
- ranked findings for `repo_reviewer`;
- commands and results for `test_runner`; or
- an allowed-path diff for `file_editor`; or
- an allowed-path implementation diff and verification output for
  `implementer`.

Assignment template v2 carries bounded task text, optional context, allowed
files, verification commands, and expected evidence. Allowed files and
verification commands are instruction-only guidance; neither the prompt
renderer nor the host enforces file writes or command execution. The hard
guard covers assignment binding, claims, budget, and sensitivity.

The stateless `tokenx assignment` CLI renders parent-authored prompts only. It
cannot authorize dispatch; callers must not supply `assignment_id`.

`buildAssignmentPrompt` does not select a model or effort, inject dispatch
metadata, or enforce the assignment.

See `delegation-guide.md` for independence, file ownership, context packaging,
acceptance criteria, turn binding, and worked renderer commands.

Route explanations use method and reason codes. They must not rely on a
persisted raw prompt because TokenX does not store one.

Session cleanup runs on `SessionEnd` only for the probed host reason `other`.
Other end reasons leave decision/outcome state until `decisionMaxAgeMs` expires
or `tokenx cleanup --session` removes it. Thread pins are separate and persist
through SessionEnd until explicit clear, exact cleanup, fresh startup, or
update. State never stores raw prompts.
