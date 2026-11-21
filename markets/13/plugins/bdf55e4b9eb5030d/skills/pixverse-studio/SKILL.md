---
name: pixverse-studio
description: "Workflow discovery: choose a PixVerse capability or shape an underspecified brief. Concrete media, editing and Canvas tasks use their direct workflows."
---

# PixVerse Studio

## Execution Surface

Read `../../skills-shared/execution-surface.md` before execution. Prefer a usable managed CLI; local execution follows `../../skills-shared/cli-workflow.md`.
In MCP mode, read `../../skills-shared/mcp-workflow.md` and follow the MCP scope below.
Do not execute the local setup, queue, filesystem, QA or finishing instructions below in MCP mode.
Script-only work needs no login or tools.

### MCP Scope

Help choose among the MCP-supported scopes on installed Skills. Do not activate desktop-only production instructions or promise a finished film from raw generation.

List accessible workspaces or inspect the current selection. Switch only to the user's explicitly requested workspace using the freshly verified expected_current_workspace_id. This does not authorize spending or team administration.

When this workflow generates images or video, apply `../../skills-shared/quality-policy.md`:
Sunburst 2K/high for images, Seedance 2.5 1080p with automatic prompt enhancement for video,
and a stopped upgrade/fallback choice for Free/Basic or model-entitlement rejection.


Help the user choose the existing workflow that fits the requested result.
This is a planning and discovery entry, not a prerequisite for other public skills.

## Installed Command

Before running helper commands, resolve the absolute plugin root from this `SKILL.md` path: it is two directories above this skill directory and contains `scripts/pixverse-runtime`. In every new shell session, set:

```bash
PIXVERSE_RUNTIME="<absolute-plugin-root>/scripts/pixverse-runtime"
```

Run helper commands through `"${PIXVERSE_RUNTIME}"`. Do not assume the user's current working directory is the plugin checkout, and do not bypass the installed wrapper with a module invocation.

For template/effect discovery or creation from a selected template, use
`../pixverse-template/SKILL.md` directly.

## First Move

Canvas first-confirmation fast path:

1. If the user asks to create, open, continue, inspect, edit, sync, or generate in a PixVerse Canvas
   project or shared Agent/Web editor, read `../../skills-internal/pixverse-agent-canvas/SKILL.md` and
   execute its early browser handoff before ordinary preparation. Merely starting a new Codex task is
   not Canvas intent and does not open a browser automatically. This route short-circuits generic
   production routing until the first useful paid confirmation: keep only this Studio entrypoint, the
   Canvas playbook, and `web-handoff.md` on that critical path. Do not also expand production,
   gateway, project-memory, creative-orchestration, or their references unless an unresolved blocker
   or a field needed by that first batch cannot be handled by the Canvas playbook itself. Load those
   playbooks after confirmation or at the later stage that actually needs them.
   Continue to use the Canvas playbook's **Cloud Preview And On-Demand Delivery** contract after
   confirmation. It overrides this entrypoint's queue/local defaults: preview in Canvas, reuse cloud
   references, and do not automatically download, run local QA, or query post-generation credits.
   A directory binding alone never activates that policy. For Canvas continuation use
   `project resume [hint] --surface canvas --format markdown`; use the same explicit surface on
   portfolio and handoff. No local media is required for cloud delivery.
2. For ordinary generation, select the matching public workflow below and read it directly.
   Read `../../skills-shared/cli-workflow.md` when execution starts; it preserves the existing
   preflight, paid retry, preview and handoff rules.
3. For setup, login or dependency problems, use `../pixverse-setup/SKILL.md`.
4. For project recovery, inspection or file delivery, use `../pixverse-delivery/SKILL.md`.

## Existing Workflows

| Requested result | Public workflow |
|---|---|
| Create Images | `../pixverse-create-image/SKILL.md` |
| Create Videos | `../pixverse-create-video/SKILL.md` |
| Music and songs | `../pixverse-create-music/SKILL.md` |
| Product Videos | `../pixverse-product-video/SKILL.md` |
| UGC Videos | `../pixverse-ugc-video/SKILL.md` |
| Music Videos | `../pixverse-music-video/SKILL.md` |
| Cinematic Story Clips | `../pixverse-cinematic-story/SKILL.md` |
| Short Drama | `../pixverse-short-drama/SKILL.md` |
| Game Trailers | `../pixverse-game-trailer/SKILL.md` |
| Character Sheets | `../pixverse-character-sheet/SKILL.md` |
| Video Editing | `../pixverse-video-editing/SKILL.md` |
| Product photography and still try-on | `../pixverse-product-stills/SKILL.md` |
| Product detail cards and exact specifications | `../pixverse-listing-images/SKILL.md` |
| Video thumbnails and covers | `../pixverse-cover-art/SKILL.md` |
| Specific image treatments or short motion effects | `../pixverse-visual-recipes/SKILL.md` |
| Try-on and wearable demonstrations | `../pixverse-fashion-video/SKILL.md` |
| Package opening and product reveals | `../pixverse-unbox-video/SKILL.md` |
| Step-by-step product operation | `../pixverse-howto-video/SKILL.md` |
| Independent variations of a supplied ad | `../pixverse-ad-variants/SKILL.md` |
| Complete narrator-led explainers | `../pixverse-explainer/SKILL.md` |
| Recurring presenter episodes | `../pixverse-presenter/SKILL.md` |
| Full spoken scripts without media generation | `../pixverse-video-script/SKILL.md` |
| Natural narration or fixed-window takes | `../pixverse-create-voice/SKILL.md` |
| Captions burned into video | `../pixverse-captions/SKILL.md` |
| Fast music-led motion, beat-synced typography and graphics | `../pixverse-motion-design/SKILL.md` |
| Generated brand visuals and mockups | `../pixverse-brand-system/SKILL.md` |
| Rebuild a reference video as your own version | `../pixverse-video-remake/SKILL.md` |
| Change the look of existing footage, keep its motion | `../pixverse-video-restyle/SKILL.md` |
| Tier lists, top-N, comparisons with a live board | `../pixverse-ranking-video/SKILL.md` |
| Two-host podcast or interview clips | `../pixverse-podcast-clip/SKILL.md` |
| Street interviews with timed reveals | `../pixverse-street-interview/SKILL.md` |
| Speaking takes with word timing | `../pixverse-talking-head/SKILL.md` |
| Many versions of one generated project | `../pixverse-video-variants/SKILL.md` |
| The same video in another language | `../pixverse-video-translate/SKILL.md` |

For unresolved production depth, model-route comparison, or production scaffolds, read
`../../skills-internal/pixverse-production/SKILL.md` only when that guidance is needed.
Read `../../skills-shared/web-handoff.md` before OAuth, subscription, workspace-management
or Canvas browser work.

Existing projects can be recovered in one call:

```bash
"${PIXVERSE_RUNTIME}" project resume [title-or-slug-hint] --format markdown
```

Use `project portfolio` only if several projects may match. For Canvas resume/portfolio/handoff,
select `--surface canvas`; its **Cloud Preview And On-Demand Delivery** contract overrides
ordinary queue/local defaults. A directory binding alone does not activate Canvas.

Prompt enhancement also runs automatically before Seedance 2.5 generation.