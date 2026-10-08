---
name: kb-bootstrap
description: Initialize a project knowledge base shared by Codex and Claude Code, or onboard an existing KB to shared agent guidance, canonical-source routing and handoffs. Use when asked to set up the KB; not to scaffold game code, infrastructure or accounts.
---

# KB Bootstrap

Create a small, usable project KB with one set of operating rules and durable
work state. The shared plugin supplies methods; the receiving KB owns facts,
local policy, decisions and progress. Apply the
[receiving-project contract](../../references/project-context.md) and the
[Knowledge Steward](../knowledge-steward/SKILL.md) for durable writes.

## Establish the target

Resolve the KB location, project name, owner when known, existing content and
the first work objective. Reuse supplied answers. Ask only for missing choices
that change where or what to write. Keep an unknown product brief or unavailable
source explicitly unknown; neither blocks creating the authorized KB structure.
Use the project's language policy; otherwise canonical notes use English and
conversation uses the user's language.

Inspect the target before writing. A new empty KB can use the bundled starter.
An existing KB needs mapped ownership and a scoped adoption plan, not a second
taxonomy. A setup request authorizes its routine KB writes; do not repeatedly
ask for approval already given. Do not invent design decisions or approve a
product direction as a side effect of setup.

## Create or adopt

Read [setup and handoff guidance](references/setup.md) for the output contract,
existing-KB route and Codex/Claude setup checks.

For an empty local directory, use the create-only
[bootstrap helper](scripts/bootstrap_kb.py). Resolve its installed path; the
following locations are placeholders:

```sh
python3 /installed/kb-bootstrap/scripts/bootstrap_kb.py /target/KB --project "Project name" --owner "Project owner"
python3 /installed/kb-bootstrap/scripts/bootstrap_kb.py /target/KB --project "Project name" --owner "Project owner" --apply
python3 /installed/kb-bootstrap/scripts/bootstrap_kb.py /target/KB --project "Project name" --check
```

The first command previews without writes. `--apply` creates missing files only;
it preserves existing files on a recognized rerun and refuses a foreign nonempty
directory. `--check` verifies starter structure, not semantic or host readiness.
It requires only Python 3.9+; lint has its own declared dependencies.
Pass a supplied first work objective with `--objective "..."` in both preview and
apply so it is persisted in the initial brief/checkpoint before later enrichment.

Read the generated notes and adapt the brief, sources and first checkpoint from
actual user information. Add only the first needed domain and its context when
there is durable content to own; do not manufacture empty game-system folders.
The helper deliberately does not infer facts from its project-name argument.

Keep `AGENTS.md` as the shared operating guide. For a new KB, `CLAUDE.md` imports
that guide rather than maintaining another policy. Use host skill discovery for
the installed Sparkore workflows; never write a user's cache path into the KB
or copy plugin skills into it. Preserve meaningful existing host instructions
when adopting a KB and reconcile conflicts explicitly.

When Python/local filesystem access is unavailable, create the same logical
artifacts through the available file tools or return the exact unperformed work.
Do not claim script execution, local sync or host discovery without observing it.

## Verify and hand off

- Read back changed files and verify source ownership and local links.
- Run the starter structure check when using the helper, then the installed
  [KB Maintenance](../kb-maintenance/SKILL.md) lint with the KB root/profile.
  Inspect coverage; no decisions in a new KB is normal, not an audit of decisions.
- Test the available host's startup route using only the KB artifacts: find the
  current objective, next action, owner and relevant workflow without chat history.
- Exercise an authorized durable update and update the work checkpoint; confirm
  another agent can read the resulting state. Shared storage is not a file lock:
  overlapping writes must be serialized through the work record's ownership.
- Record bootstrap, lint, semantic-route and actual host checks separately in the
  setup work note. Missing Claude Code execution stays untested; a link check is
  not a Claude session. Finish with the usable KB location, next task and gaps.

Only configure KB files. Engine projects, Git remotes, cloud storage, sync clients,
credentials, app permissions and plugin installation are outside this workflow
unless separately requested. Installing a plugin alone does not run bootstrap.
