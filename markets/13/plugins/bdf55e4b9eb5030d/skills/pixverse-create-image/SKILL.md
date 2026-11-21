---
name: pixverse-create-image
description: "Image generation: create or edit a still image with PixVerse, preserving requested references, model and format. Use for a direct image deliverable."
---

# Create Images

## Execution Surface

Read `../../skills-shared/execution-surface.md` before execution. Prefer a usable managed CLI; local execution follows `../../skills-shared/cli-workflow.md`.
In MCP mode, read `../../skills-shared/mcp-workflow.md` and follow the MCP scope below.
Do not execute the local setup, queue, filesystem, QA or finishing instructions below in MCP mode.
Script-only work needs no login or tools.

### MCP Scope

Generate or revise still images with owned identity references. Query live capabilities, check the account, submit each agreed composition and deliver every output. Preserve requested text without guaranteeing exact typography or pixel layout.

List accessible workspaces or inspect the current selection. Switch only to the user's explicitly requested workspace using the freshly verified expected_current_workspace_id. This does not authorize spending or team administration.

Preserve the requested subject, reference roles, layout and format. Describe the visible result clearly. Default to gpt-image-2.5-sunburst at 1440p with high detail. Use separate requests for independent compositions; do not introduce video tasks.

For execution, read `../../skills-shared/execution-surface.md`. It selects the supported CLI or MCP branch, checks account and quality requirements, and preserves submission identity through delivery.

# Create Images



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

Use image generation for standalone stills and as a control layer before video.

For a simple standalone image, use the shared contract's account-aware `route queue`
fast path directly. Read `../../skills-shared/prompt-craft.md` for complex composition
or prompt repair; read `../../skills-shared/model-routing.md` for a custom model,
unfamiliar parameters or route comparison. The supported default needs neither lookup.
Read `../../skills-shared/capability-priority.md` when the image is part of a video pipeline.

For reference roles, image edits and reusable product/brand inputs, read
`../../skills-shared/extended-capabilities.md` before composing the request.

## Common Outputs

- visual territory boards
- product hero stills
- storyboard sheets
- character sheets
- item/prop references
- locked logo/title/final-frame plates
- posters, KVs, book covers, album covers
- game/UI mock screens

## Default Command

Use the same high-quality default for final stills, previews and intermediate control art:

```bash
pixverse create image --model gpt-image-2.5-sunburst --quality 1440p --detail-level high --aspect-ratio <ratio> --prompt "..."
```

Here `1440p` is the CLI's 2K tier, while `high` controls rendering detail. Do not reduce
control boards to 1080p/medium. Respect an explicit user override.

Free/Basic or model-entitlement failure pauses for the subscription/fallback choice in
`../../skills-shared/quality-policy.md`. Only after the user accepts fallback:

```bash
pixverse create image --model gemini-3.1-flash-lite --quality 1080p --aspect-ratio <ratio> --prompt "..."
```

Nano Banana 2 Lite does not accept GPT's detail-level flag. Other image families remain
available when explicitly selected; verify their own supported parameters. Read
`../../skills-shared/pixverse-cli-models.md` for Flare/Sunburst's expanded detail/ratio
choices and Seedream's model-specific quality and reference limits. Use a manual
queue for explicit models outside the automatic route helper's image families.

Use uploaded images with `--image` or `--images` when they define the subject, product, character, logo, or layout.

## Image Before Video

Prefer image-first when:

- subject identity matters
- product packaging matters
- text/logo must land exactly enough to inspect
- the user wants multiple concepts
- video would be expensive to explore blindly
- a storyboard frame, title card, final packshot, UI plate, or character sheet will control later video

## Video Control Roles

Label stills by role before using them downstream:

- identity/product anchor
- storyboard opening frame
- style reference
- exact text/logo/UI plate
- prop/wardrobe/vehicle sheet
- negative example or rejected route

Do not send an asset sheet as an I2V opening frame when a proper storyboard frame is needed; generate or choose the shot frame first.

## QA When Requested

Standalone images deliver directly after generation and download, with no automatic visual inspection or QA command. If the user requests review or a specialized workflow explicitly requires an anchor check, assess only the requested fit, crop, subject, text or logo constraints.