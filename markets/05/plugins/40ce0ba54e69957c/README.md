# TokenX Plugin

TokenX applies deterministic controls and safety floors, then uses one bounded
Luna/low classifier v3 call with a fixed local signals digest and confidence
gates for uncertain delegated prompts. Simple creative
economy prompts and fixed one-agent safety, retry, and explicit-depth floors
remain deterministic. It stores no raw
prompt, transcript, file content, diff, or credential. Disable the classifier
with `routing.smartClassifier.enabled=false` to use deterministic routing only.

## Routes

- `economy`: Luna low for read-only work and Luna medium for bounded file edits.
- `standard`: Terra medium for implementation and Terra high for complex coding.
- `deep`: Sol high for analysis, Sol xhigh for architecture, and Sol max after
  recurring failure.
- qualified escalation: the configured Sol ultra effort only after an explicit
  request for more reasoning; prior failure uses the retry profile instead.
- `parent`: preserve an explicit no-delegation choice.
- `passthrough`: add no routing instruction for conversational prompts.

## Thread model pin

`Use only Sol/xhigh; do not switch the current model.` or `Keep using
Terra/high for this thread.` pins the exact named pair on the same prompt and
every consecutive prompt in the current thread until replacement or clear.
Both model and effort are required. `Clear the model pin.` and `Resume
automatic routing.` remove it before any task in that prompt is classified.

A plain one-turn control cannot override an active pin; a new sticky pair
replaces it. Pinned turns bypass the smart classifier and authorize no child,
so TokenX makes no automatic adjustment or delegation. Unsupported or
malformed pairs fail visibly without substitution. The dedicated pin record
stores fixed enums under a hashed opaque session key and does not store the raw
prompt.

One-off typo work may remain economy. Recurrence signals such as "still
getting this error" or "keeps failing" use deep/max for diagnosis.
Bounded prompts of 256 bytes or more receive smart-model assessment, which
judges the primary task as a whole rather than downgrading it because a
subordinate read or file-creation step could use a cheaper model. Dynamic
agent/model-orchestration planning has a deep architecture floor. Contract
drift and classifier failures fall back visibly to deterministic routing.

TokenX selects a per-turn budget of sibling agents. Routine independent work
can use up to four Luna agents, normal independent work up to three Terra
agents, and automatically inferred deep work up to two Sol agents. The budget
is the persisted `agentCount`, but only advertised task names from a complete
classifier-proposed plan authorize children; hard none authorizes none.

Automatic dispatch requires a complete classifier-proposed plan with one to
four compatible assignments, each carrying a unique assignment id. Roles may
repeat for independent work of the same kind. An explicit singular request such
as `spawn sol agent` may attach one implementer assignment at the selected
parent profile when the smart classifier does not propose a plan; multi-agent
counts still require a complete classifier proposal. A hard-none parent route is
advisory guidance and authorizes no child. The exact current persisted `task_name` is the sole dispatch identity;
do not supply `assignment_id`, `agent_type`, `model`, or `reasoning_effort`.
The provider guard enforces model and effort only for that authorized child.
Disabled dynamic agents or smart classification, timeout, and fallback all
produce hard none. Objective/evidence keys are structural result metadata, not
filesystem enforcement or proof of independence.
Assignments are current-turn-only: on every new turn, obtain and use a newly
advertised assignment; never reuse an old instruction.
Sensitive cheaper assignments are denied. Assignment prompts guide scope but
do not allowlist paths or rewrite parent-authored text.

The `tokenx assignment` command validates and renders assignment template v2
prompts with optional context and evidence plus role-appropriate verification
commands. It is stateless: it does not spawn an agent, read session state, or
consume an assignment slot. File scope and verification remain instruction-only
controls.

Prompt-free session counters record retry escalation, sensitivity denials,
smart fallbacks, and the last route. Two retry escalations raise subsequent
non-explicit delegated economy work to the standard floor. Configuration schema
v3 adds the implementer profile in place; earlier development schemas are not
migrated.

Compaction preserves the active routing decision; startup, resume, and clear
events remove stale decision state. A thread pin survives resume, compact, and
`SessionEnd`; fresh startup, host clear, exact `tokenx cleanup`, and update
remove it. Nested automatic delegation is configured
as denied, but the current Codex
hook contract does not expose subagent depth. Enforcement is therefore an
atomic sibling-call budget plus instruction-level guidance, not a hard proof
that only the root thread can spawn. Session cleanup runs for the probed
`SessionEnd` reason `other`; other end reasons rely on decision TTL or
`tokenx cleanup`.

TokenX keeps work in the parent when configured models cannot be verified and
keeps invalid stored configuration in parent-only control instead of silently
substituting a profile or repeatedly failing the prompt hook. Run
`tokenx update` to refresh the supplying marketplace, normalize plugin data,
and invalidate stale routing state, then start a new thread.

TokenX does not create or manage user-level custom-agent files. Removing the
plugin leaves user-created agents unchanged.

Review `/hooks` before trusting the installed hook commands. Use the
`route-agents` skill for explanations, configuration, and diagnostics.

TokenX verifies routing behavior but makes no exact savings claim without
reliable usage measurements.

## License

TokenX is source-available under the PolyForm Perimeter License 1.0.1.
Internal business use, including use by companies in paid work, is permitted.
TokenX may be used without a TokenX license fee for educational use and for
developing or maintaining open-source projects. This no-fee use does not
permit providing a competing TokenX-derived product or plugin.
Providing TokenX or a TokenX-derived competing product or plugin to others,
whether paid or free, requires a separate written license from Pagonya LLC.
Request permission at `info@pagonya.co`. The controlling terms are in
`LICENSE`.

TokenX is published by Pagonya LLC. Product, support, privacy, and terms are
available at https://pagonya.co/tokenx/. Support email is `info@pagonya.co`.
