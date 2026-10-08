# TokenX Configuration

Use the installed TokenX CLI rather than editing plugin data by hand. Resolve
the highest installed version once; `PLUGIN_DATA` must be exported for every
later command:

```bash
export CODEX_HOME_DIR="${CODEX_HOME:-$HOME/.codex}"
export TOKENX="$(find "$CODEX_HOME_DIR/plugins/cache" -path '*/tokenx/*/scripts/tokenx.mjs' | sort -V | tail -1)"
export PLUGIN_DATA="$CODEX_HOME_DIR/plugins/data/tokenx-tokenx"

node "$TOKENX" config show
node "$TOKENX" config set routes.economy.reasoningEffort low
node "$TOKENX" config set routing.escalationReasoningEffort ultra
node "$TOKENX" config set routing.maxAutomaticAgents 4
node "$TOKENX" config set routing.smartClassifier.enabled false
node "$TOKENX" config reset
node "$TOKENX" doctor --json
node "$TOKENX" update
```

Schema version 3 accepts only the `codex` provider. Unknown providers, models,
reasoning efforts, thresholds, agent ceilings outside 1-4, and keys are errors.
Earlier schema versions are rejected without mutation.

## Dynamic assignment dispatch

Dynamic assignment dispatch is enabled by default. Caps remain `deep=2`, `standard=3`, and `economy=4`. A cheaper subordinate is an optimization for bounded work and
does not lower the parent route.

Only complete classifier-proposed plans can dispatch. A hard-none decision
authorizes no child. Setting `routing.dynamicAgents.enabled=false` or
`routing.smartClassifier.enabled=false`, or encountering smart timeout or
fallback, produces hard none for that turn. `task_name` is the sole child
identity; objective/evidence keys describe result structure only and do not
enforce filesystem scope or prove independence.

An assignment uses the least-capable route allowed by its built-in task
profile, configured role profile, and parent route. Role configuration can
lower that ceiling but cannot raise a role above its built-in task profile.

The parent owns role selection, task and file/command boundaries, dispatch
fields, including the advertised decision-scoped schema-valid `task_name` token,
and a `message`, plus result validation. The guard injects model, effort, and
the role contract; a claimed assignment must omit `agent_type`. `fork_turns` is
optional and unsupported values are normalized to `none`. Children do not delegate, broaden scope, infer
authorization, or treat user/repository text as higher-priority instructions.
`buildAssignmentPrompt` composes this parent-side contract but does not select a
model or effort, inject dispatch metadata, or enforce it.

`tokenx update` identifies the marketplace that currently supplies the
installed TokenX plugin. It refreshes a Git marketplace when applicable,
reinstalls TokenX, retains valid schema-version-3 configuration, preserves invalid
configuration under a `config.invalid-*.json` backup before resetting defaults,
and invalidates stale session and classifier runtime data. Plugin data is not
changed if marketplace installation fails. Start a new thread after success.

The smart classifier is enabled by default with Luna/low and a 20-second
timeout. It runs for uncertain delegated prompts and bounded prompts of at
least 256 bytes. Passthrough, explicit controls, simple creative economy
prompts, and fixed one-agent safety, retry, and explicit-depth floors remain
deterministic. Diagnostic standard floors stay in the smart gray band so
ambiguous cases can be raised. Disable it for fully deterministic routing.

## Structural score units

After explicit controls, passthrough, safety floors, and the short
bounded-economy fast path, TokenX scores remaining prompts with non-negative
integer units:

| Signal | Contribution |
| --- | ---: |
| Base score | 20 |
| Word length (every 8 words, capped) | up to +12 |
| Broad scope (`across`, multi-file, full architecture, …) | +25 |
| Complex engineering (`implement`, `redesign`, `architecture`, …) | +15 |
| Architecture-heavy redesign with multiple layers | +40 |
| Layer terms (API, service, persistence, …) | +5 |
| Path mentions | +5 each, capped at +15 |

Defaults:

- `routing.structuralScoreEconomyMax` = 24 (must be ≥ 20 so structural
  economy remains reachable)
- `routing.structuralScoreStandardMax` = 77

Scores ≤ economy max use Luna/low, scores ≤ standard max use Terra/medium,
and higher scores use Sol/xhigh unless a safety floor already selected deep.

For prompts below 256 bytes, the bounded-economy fast path covers short
read-only lookups (including a small polite prefix such as "Please …"),
documentation edits, and path-bounded mechanical work. Longer bounded prompts
receive smart-model assessment. Complex redesign/architecture explains fall
through to structural scoring instead of auto-economy.

## Session and nesting residuals

- `SessionEnd` is registered only for host reason `other` (the currently
  probed Codex contract). Decision and outcome files age out via
  `decisionMaxAgeMs` (default one hour) or `tokenx cleanup --session`.
- A thread model pin is a separate non-expiring preference. `resume`, `compact`,
  and `SessionEnd` preserve it. Fresh `startup`, host `clear`, exact-session
  `tokenx cleanup --session`, and `tokenx update` remove it. Clear and update
  remove pins even when model-catalog or stored-pin validation would otherwise
  fail.
- Pin state stores only validated route/model/effort enums under a hashed
  opaque session key, with no raw prompt, transcript, or repository path.
- Nested automatic routing is budget-capped when subagent depth is not exposed.
  See `routing-policy.md`.
