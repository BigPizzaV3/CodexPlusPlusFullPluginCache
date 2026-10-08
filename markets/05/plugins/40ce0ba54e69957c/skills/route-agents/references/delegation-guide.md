# TokenX Delegation Guide

## Independence test

Delegate only when each assignment can finish from its own bounded inputs and
return evidence the parent can evaluate without depending on another child.
Keep coupled sequencing, shared mutable decisions, and final synthesis with the
parent. If two assignments must coordinate while running, they are one task.

## One writer per file

Assign at most one writing child to any file. Read-only assignments may overlap
file scopes, but `file_editor` and `implementer` assignments must have disjoint
allowed-file lists. The parent resolves conflicts and owns the integrated result.

## Context package

Every assignment should state:

- Goal: one observable outcome.
- Constraints: behavior and boundaries that must remain true.
- File scope: exact readable or writable paths; writers need allowed files.
- Verification: exact commands when the role supports them; an `implementer`
  requires at least one command.
- Expected evidence: the facts, findings, command output, or diff the child must
  return.

Task and context files must be regular mode-`0600` files. Template v2 fields
guide the child. Allowed files and verification commands are instruction-only;
TokenX does not enforce writes or command execution from prompt text.

## Acceptance criteria phrasing

Write criteria as observable pass conditions: "the focused test exits 0 and
the response contains no raw prompt" is actionable; "make it robust" is not.
Name required negative cases and evidence. The parent validates the returned
result instead of accepting a completion claim.

## Turn binding

Only a complete classifier-proposed plan authorizes a child. A hard-none route,
disabled dynamic agents or smart classification, timeout, and classifier
fallback authorize no child. The exact current persisted `task_name` is the
sole dispatch identity; never supply `assignment_id`. Objective/evidence keys
describe expected result structure, not filesystem enforcement or proof that
the assignments are independent.

A thread model pin is also hard none and advertises no assignment. It
authorizes no child for as long as the pin is active, even if the task would
normally be separable or the prompt explicitly asks for delegation. Replace or
clear the pin before requesting an assignment.

Install TokenX, then inspect and trust its hooks with `/hooks`. Dispatch a role
with its exact advertised `task_name` and a `message`; omit `agent_type`,
`model`, and `reasoning_effort`. `PreToolUse` updates do replace `agent_type`
on codex-cli 0.146.0, but TokenX denies a claimed assignment that carries one
because a custom agent's pinned model beats an injected model. `fork_turns` is
optional for the caller because TokenX always sets it: an omitted or
unsupported value becomes `none`. Omitting it is not a bounded fork — on
codex-cli 0.146.0 an absent `fork_turns` forks the full parent conversation,
so TokenX pins it rather than leaving it to the host default. An explicit
positive integer is kept.

Assignments remain valid only within the turn that advertised them. Dispatch
with the exact advertised decision-scoped `task_name` in that
turn. On every new turn, re-submit the prompt and use only its newly advertised
assignment; never reuse an old instruction. Its opaque decision fragment makes
the host task name fresh for each new decision. There is no grace window for
stale authorization. A stale call that reaches TokenX is denied as
`turn_changed`; exact reuse may instead be rejected by Codex's duplicate agent
path before `PreToolUse`, which is also fail-closed because no child starts.

## Worked examples

Each example assumes the named task file already contains the bounded task and
has mode `0600`.

```bash
export CODEX_HOME_DIR="${CODEX_HOME:-$HOME/.codex}"
export TOKENX="$(find "$CODEX_HOME_DIR/plugins/cache" -path '*/tokenx/*/scripts/tokenx.mjs' | sort -V | tail -1)"
export PLUGIN_DATA="$CODEX_HOME_DIR/plugins/data/tokenx-tokenx"
```

### Repository reader

```bash
node "$TOKENX" assignment \
  --role repo_reader --parent-route deep \
  --task-file /tmp/tokenx-repo-reader-task.txt \
  --evidence "Verified facts with exact file references"
```

### Repository reviewer

```bash
node "$TOKENX" assignment \
  --role repo_reviewer --parent-route deep \
  --task-file /tmp/tokenx-repo-reviewer-task.txt \
  --context-file /tmp/tokenx-review-context.txt \
  --evidence "Severity-ranked findings and remaining test gaps"
```

### Test runner

Put the exact permitted test commands in the bounded task text, then render it:

```bash
node "$TOKENX" assignment \
  --role test_runner --parent-route standard \
  --task-file /tmp/tokenx-test-runner-task.txt \
  --evidence "Exact commands, exit codes, and pass/fail counts"
```

### File editor

```bash
node "$TOKENX" assignment \
  --role file_editor --parent-route standard \
  --task-file /tmp/tokenx-file-editor-task.txt \
  --files docs/routing.md \
  --verify "node --test tests/publication.test.mjs" \
  --evidence "Allowed-file diff and focused test output"
```

### Implementer

```bash
node "$TOKENX" assignment \
  --role implementer --parent-route standard \
  --task-file /tmp/tokenx-implementer-task.txt \
  --files src/router.mjs,tests/router.test.mjs \
  --verify "node --test tests/router.test.mjs" \
  --verify "npm test" \
  --evidence "Scoped diff plus focused and full test output" \
  --json
```
