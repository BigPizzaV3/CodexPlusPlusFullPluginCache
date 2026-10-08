# Claude Code provider profile

Documentation reviewed: 2026-09-03. Classification below distinguishes current documented support from local runtime verification. A documented mechanism is not proof that it is installed, enabled, configured or tested on the user's device. Recheck the actual installed runtime before consequential workflow/configuration changes. If offline, mark capability verification pending; do not guess commands, flags or event schemas.

## VERIFIED_CURRENT in official documentation

- `CLAUDE.md` and automatic memory can supply persistent context. New sessions/worktrees must not be assumed memory-free. Inspect applicable instruction sources and memory; instruction text is not an enforced permission system. [Memory documentation](https://code.claude.com/docs/en/memory).
- Project skills use `.claude/skills/<name>/SKILL.md` and can be invoked as `/skill-name`; plugin skills are namespaced. Discover actual loading and name precedence before relying on a particular skill. Local files do not prove availability in a remote session. [Skills documentation](https://code.claude.com/docs/en/slash-commands).
- Project subagent definitions can live in `.claude/agents/`; subagents support separated context, but review independence and permissions must still be established. [Subagents](https://code.claude.com/docs/en/sub-agents).
- Plan Mode supports read/plan work before approved edits. Availability and behavior can vary by surface/version. It is not owner approval of a proposed architecture or authorization to deploy. [Permission modes](https://code.claude.com/docs/en/permission-modes).
- Hooks attach to lifecycle events. `PreToolUse` can block a tool call; `PostToolUse` cannot undo an action that already happened. A hook allow does not override an applicable deny/ask permission rule. Check and test the current event contract before relying on a guard. [Hooks guide](https://code.claude.com/docs/en/hooks-guide), [Permissions](https://code.claude.com/docs/en/permissions).
- Worktrees provide optional task isolation. Use them only when the repository, ownership and merge strategy justify the added branch/state complexity. [Worktrees](https://code.claude.com/docs/en/worktrees).
- Checkpointing supports recovery of Claude-made edits but is not a complete backup: changes made through Bash commands and most subagent changes are outside its tracked scope. It also cannot reverse external effects. Preserve concurrent edits and confirm restore scope before rewinding. [Checkpointing](https://code.claude.com/docs/en/checkpointing).
- `/goal` can evaluate measurable completion conditions through a fresh small-model evaluator that sees the session transcript. The evaluator cannot independently inspect files or run commands. Use it only for objective conditions surfaced in the transcript; never treat it as independent code, security, visual, perceptual or owner acceptance. [Goal verification](https://code.claude.com/docs/en/goal).
- Verification and deliberate context management are documented workflows. Browser/screenshot access must be checked in the actual environment; never claim a visual test from reasoning alone. [Best practices](https://code.claude.com/docs/en/best-practices).

## SUPPORTED WITH LOCAL VERIFICATION REQUIRED

Context-specific recheck: 2026-09-09. [Memory](https://code.claude.com/docs/en/memory) and [context window](https://code.claude.com/docs/en/context-window) document persistent instruction/memory loading and compaction effects. `/context` can inspect the current context breakdown; `/memory` exposes instruction/memory sources where supported. Do not infer exact usage from a generic documentation example. Skill instructions may be truncated or dropped under documented compaction budgets, so keep essential boundaries early and persist current authority in accessible artifacts. This verifies documented behavior only, not this user's Claude runtime. The [goal evaluator](https://code.claude.com/docs/en/goal) still judges surfaced conversation evidence rather than independently inspecting files; [checkpointing](https://code.claude.com/docs/en/checkpointing) is not a full backup. Other entries above retain their stated earlier review date and need rechecking before reliance.

- Browser, screenshot, design-file, test-runner, worktree, subagent, hook and `/goal` use requires confirmation in the actual runtime and project. Documentation alone does not establish availability, configuration or evidence quality.
- `CLAUDE.md`, skills and automatic memory provide context; they are not enforcement boundaries. Permissions, protected environments, repository rules, independent evidence and owner gates remain separate controls.
- Provider-native checkpoints may supplement but never replace an authorized repository/data backup and rollback plan.

## UNVERIFIED UNTIL OBSERVED

- Installed Claude Code version, active model/mode, permission mode, loaded instruction hierarchy, enabled hooks, skill discovery, MCP/tools and filesystem/network reach.
- Whether a specific subagent is actually independent, whether a screenshot came from the acceptance environment, and whether a reported command ran against the declared revision.

## Task-start application (policy, not new vendor verification)

Use the shared [session start decision](../../../../shared/expert-system/session-lifecycle.md) and [provider gate](../../../../shared/expert-system/provider-capability-routing.md). For the current Claude task identify required runtime/toolchain and relevant versions, actual availability/access, applicable closed method and freshness, and whether a changed Claude/model/tool capability or current Anthropic guidance materially affects the task. Inspect the execution environment first; recheck only relevant official guidance claims that still need it. Decide whether the evidence actually requires context/skill/harness adjustment under existing authority; otherwise reuse the validated workflow. Missing runtime is an environment gap, not an alternate coding-method decision. This addition does not refresh the documentation dates or certify any local Claude installation above.

## Skill OS policy applied to Claude

Keep durable invariants in CLAUDE.md and situational details in the approved task packet. Before a fresh session record branch/revision/dirty tree, checkpoint, source manifest, harness version, applicable memory/instructions and evidence; verify the new session sees that state. Use only the smallest justified local skills and reviewers. A reviewer that built or owns the critical decision cannot independently accept it, even in a separate session.

Inspect permissions and actual tools before choosing automatic dispatch or manual copy/paste. If this controller has no Claude connector, prepare the prompt and request its report; do not claim Claude ran. Do not install Claude, create project harness files, turn on provider services, change permissions or deploy under the authority of this profile alone.
