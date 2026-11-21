---
name: pixverse-character-sheet
description: "Character design: create reusable character sheets, expressions, turnarounds and identity references for consistent scenes, animation or episodic video."
---

# Character Sheets

## Execution Surface

Read `../../skills-shared/execution-surface.md` before execution. Prefer a usable managed CLI; local execution follows `../../skills-shared/cli-workflow.md`.
In MCP mode, read `../../skills-shared/mcp-workflow.md` and follow the MCP scope below.
Do not execute the local setup, queue, filesystem, QA or finishing instructions below in MCP mode.
Script-only work needs no login or tools.

### MCP Scope

Generate character sheets and views from shared identity references. No sheet slicing, exact layout, file assembly or continuity guarantees.

List accessible workspaces or inspect the current selection. Switch only to the user's explicitly requested workspace using the freshly verified expected_current_workspace_id. This does not authorize spending or team administration.

## Installed Command

Before running helper commands, resolve the absolute plugin root from this `./SKILL.md` path: it is two directories above this skill directory and contains `scripts/pixverse-runtime`. In every new shell session, set:

```bash
PIXVERSE_RUNTIME="<absolute-plugin-root>/scripts/pixverse-runtime"
```

Run helper commands through `"${PIXVERSE_RUNTIME}"`. Do not assume the user's current working directory is the plugin checkout, and do not bypass the installed wrapper with a module invocation.

## CLI Execution

Apply `../../skills-shared/quality-policy.md` to all generated images/videos: Sunburst 2K/high,
Seedance 2.5 1080p with automatic prompt enhancement, and an explicit upgrade/fallback
choice for Free/Basic or model-entitlement rejection.

For an explicitly selected Canvas project or node, read
`../../skills-internal/pixverse-agent-canvas/SKILL.md` first and follow its Canvas
preflight and delivery contract; the ordinary queue/local route below does not replace it.

For ordinary creation or editing, read `../../skills-shared/cli-workflow.md` before
executing this workflow. It contains the existing account-aware routing, paid-work
confirmation, progress, preview and project-handoff rules. Studio and Production are
not prerequisites. The shared account, confirmation and direct-medium rules govern the
examples and defaults below. Read the gateway only when writing manual CLI commands or queue specs.
Creation command examples below are queue-task fragments, not permission to submit paid
`pixverse create` commands directly.

Use this when a person, creature, mascot, prop, outfit, or vehicle must survive across multiple images/videos.

Read:

- `../../skills-shared/extended-capabilities.md#reference-information`
- `../../skills-shared/prompt-craft.md`

Read `./references/identity.md` for accepted reference images, supported view evidence
and consistent identity, wardrobe and scene roles across generated shots.

## Fast Path

1. Collect existing references or write identity anchors.
2. Generate character/item sheet before narrative clips.
3. Record sheet task id and URL in project memory.
4. Use reference mode or image-to-video for future clips.

## Character Sheet Prompt

Include:

- front, side, back, head detail
- outfit materials and colors
- silhouette
- age/body/posture
- face/hair/accessories
- expression range
- neutral clean background

## Prop Sheet Prompt

Include:

- front/side/top views
- material
- scale relationship
- logo/mark placement
- wear/detail
- what must never change

## CLI Shape

```bash
pixverse create image --model gpt-image-2.5-sunburst --quality 1440p --detail-level high --aspect-ratio 16:9 --images <refs...> --prompt "..."
```

Then:

```bash
pixverse create reference --images <character-sheet> <prop-sheet> --prompt "..."
```

## Quality Checks

- all views describe the same character/item
- no extra unwanted characters
- face and outfit are stable enough
- sheet is useful as future reference
- memory maps name -> task id, absolute local path, provider URL, and role