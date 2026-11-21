---
name: pixverse-brand-system
description: "Brand visuals: generate coherent logo concepts, palette boards, brand guide images and branded mockups using the user's accepted visual references."
---

# Brand Visuals

## Execution Surface

Read `../../skills-shared/execution-surface.md` before execution. Prefer a usable managed CLI; local execution follows `../../skills-shared/cli-workflow.md`.
In MCP mode, read `../../skills-shared/mcp-workflow.md` and follow the MCP scope below.
Do not execute the local setup, queue, filesystem, QA or finishing instructions below in MCP mode.
Script-only work needs no login or tools.

### MCP Scope

Generate raster logo concepts, palette boards, brand guide images and mockups from accepted references. No vector export, exact typesetting or packaging.

List accessible workspaces or inspect the current selection. Switch only to the user's explicitly requested workspace using the freshly verified expected_current_workspace_id. This does not authorize spending or team administration.

When this workflow generates images or video, apply `../../skills-shared/quality-policy.md`:
Sunburst 2K/high for images, Seedance 2.5 1080p with automatic prompt enhancement for video,
and a stopped upgrade/fallback choice for Free/Basic or model-entitlement rejection.


Build a small set of decisions that can be reused across real deliverables. Each application should derive from the same accepted identity.

## Required Recipes

Read `./references/foundation.md` for every brand task: source assets, three distinct
logo mechanisms, palette/type direction, durable decisions and selective revisions.
Read `./references/applications.md` for mockups, packaging, merchandise, signage, social
graphics, posters and brand guide images. Preserve their concrete stage
and output contracts. Existing assets and explicit delegated choices take precedence.

## Define The Direction

Establish the name, audience, offering, personality and intended uses from the brief. Separate fixed brand facts from exploratory choices. Start with concise distinct directions only when the user needs concept selection; do not generate a large pack before the identity is decided.

Generate distinct mark and wordmark concepts as images. Keep silhouette, letterforms, spacing and small-size legibility deliberate. Supplied official logos remain authoritative references. Record the selected concept and palette for later generated applications.

## Make The System

Record palette values, readable text/background combinations, typography direction, spacing and image treatment. Use a supplied font specimen when precise letterforms matter, and distinguish the intended font from visually generated lettering.

Use a simple dependency chain: accepted name/mark, core tokens, layout templates, applications. A mark change updates the dependent guide and examples; it should not leave old logos scattered through the output.

Provide relevant image outputs: profile image, social card, packaging mockup, cover or hero visual. Use `../pixverse-product-stills/SKILL.md` for photo applications and `../pixverse-listing-images/SKILL.md` for information cards. Keep original marks as explicit edit references in mockups.

## Example Direction

For a fictional neighborhood repair studio: a compact joint motif, warm off-white field, deep blue text, restrained orange accents, sturdy humanist lettering and close photographs of tools. The motif should remain recognizable at small size.

## Deliver And Revise

Deliver the agreed PNG/JPG image set with palette values, accepted copy and source references. Check small-size legibility, contrast and consistency. Refine images through Sunburst using the accepted result; regenerate only affected applications.

Keep the delivered image count and contents aligned with the requested brand visuals.

## Execution

Read `../../skills-shared/production-brief.md` for reference roles, prompt construction and revisions.
For media execution, follow `../../skills-shared/cli-workflow.md`; load the gateway before manual
CLI commands or queue specs. Resolve the plugin root from this skill's installed path:
set `PIXVERSE_RUNTIME="<absolute-plugin-root>/scripts/pixverse-runtime"` and invoke `"${PIXVERSE_RUNTIME}"` with the documented arguments.
Prompt-only work ends with the usable plan and prompts; it needs no account or generation calls.