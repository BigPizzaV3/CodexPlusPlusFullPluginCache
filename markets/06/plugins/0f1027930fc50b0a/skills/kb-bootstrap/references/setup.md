# Shared KB setup and handoff

## Minimal output contract

For a new KB, the bundled starter supplies:

| Artifact | Responsibility |
| --- | --- |
| `AGENTS.md` | Shared operating rules and task-to-skill routing |
| `CLAUDE.md` | Thin import of `AGENTS.md` for Claude Code |
| `Home.md` | Human entry point, including opening the folder in Obsidian |
| `PROJECT_STATE.md` | Current objective, blockers and active-work route |
| `Project Brief.md` | Project identity, accepted scope and explicit unknowns |
| `00_System/Source of Truth.md` | Project-specific canonical-source ownership |
| `00_System/Domain Index.md` | Small ownership lookup; extend as domains appear |
| `00_System/Document Lifecycle.md` | Local metadata, decisions and retirement rules |
| `00_System/Decisions/Active.md`, `Index.md`, `Records/` | Current constraints and historical rationale |
| `00_System/Work/Index.md`, `Active/`, `Archive/` | Claimed work, checkpoints and handoffs |
| `00_System/Backlog/Index.md` | Pending work, distinct from active execution |
| `99_Archive/` | Retired material outside the default startup route |
| `.kb-lint.json` | Explicit profile matching this KB's conventions |

The setup work record is an initial checkpoint. Empty decision/archive directories
are intentional; do not create fake decisions, past work or evidence to fill them.
The `.kb-bootstrap.json` marker only identifies a helper-created layout and
project name for safe reruns. It is not an authority record or readiness score.

The templates are [bundled assets](../assets/vault/). For a host without script
execution, replace the project/owner/date placeholders, use valid YAML quoting,
and create these artifacts through its file tools. Preserve existing artifacts.
The default text is English; adapt it when an established writing policy differs.

## Existing KB

Inspect current agent guides, local skills, domain/state documents and designated
data sources. Map each responsibility above to the existing owner. Add only a
missing responsibility needed for shared operation; do not copy the entire starter
over existing work or run the empty-directory helper with a bypass.

Treat an existing `CLAUDE.md` as meaningful work. Consolidate genuinely shared
rules into the accepted common guide and preserve host-specific rules in the
adapter. A local skill remains authoritative until an authorized cutover assigns
its role to the installed plugin. Do not delete local skills as part of setup.

Choose a compatible lint profile and test the mapped startup routes. The helper's
`--check` only applies to its own starter layout; an adopted layout is verified
against the mapped responsibilities and KB lint instead.

## Host startup

Open the KB root as the working directory in both clients. Codex uses root
`AGENTS.md`; the supplied Claude Code adapter uses `@AGENTS.md` to import the same
guide. If the KB is nested inside a larger repository, inspect ancestor guidance
too; add an outer pointer only when that edit is authorized. Do not claim either
host will discover a nested KB guide from an unrelated working directory.

Resolve the installed `sparkore-core` skills through the host, not a hardcoded
cache/version path. A user can explicitly select the namespaced workflow when
automatic routing is uncertain; in Claude Code this is typically
`/sparkore-core:kb-bootstrap`. If the plugin is missing in one client, report that
capability gap. Markdown remains readable, but skill availability is unverified.
The separate market plugin is optional and needed only for a market question.

Google Drive, a shared filesystem or a repository can carry the same KB files.
Bootstrap does not install or verify a synchronization service. Cross-device
handoff requires the receiver to see the latest saved checkpoint and source files.

## Collaboration contract

Each multi-session task has a work record with task ID, human decision owner,
executing agent, claimed files/scope, current objective, completed work, accepted
decisions, open questions and the next action. Use one canonical owner for each
fact and separate work records for independent tasks.

Before writing, re-read the canonical note and work record. If another agent is
editing overlapping files, coordinate a handoff or work on disjoint files. A claim
in Markdown is advisory, not an atomic lock or conflict-free merge mechanism.
After writing, read back and update the checkpoint; do not overwrite intervening
edits or infer a finished task from an old chat.

## Acceptance

Distinguish these outcomes:

1. **Structure created:** the intended files exist and a create-only rerun
   preserves user changes. No absolute cache paths or source-game facts leaked.
2. **KB checked:** local links/metadata pass the selected lint profile and source
   ownership, brief and next action are meaningful. Product unknowns remain visible.
3. **Host checked:** record the actual client/version, plugin path/version, prompt,
   inputs, files changed and observed startup/update/handoff. Each client needs its
   own run; a simulated route does not demonstrate automatic loading in that client.

Use a synthetic or explicitly selected pilot KB for behavioral trials. Ask one
agent to persist a scoped accepted rule and a second to continue from the saved
checkpoint. The receiver should find the rule's owner and next action without
receiving the prior chat. Also try a setup rerun after a human edit. Never run
these synthetic mutations against the user's real game KB just to claim a pass.
