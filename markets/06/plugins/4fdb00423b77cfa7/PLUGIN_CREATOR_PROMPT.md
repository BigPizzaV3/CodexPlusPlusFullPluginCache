# Plugin Creator Prompt — Imago

Create/validate a **skills-only plugin** from the attached archive.

## Identity
- Package: `imago`
- Skill: `imago`
- Display name: `Imago`
- Version: `0.1.0`
- Category: `Creativity`

## Product definition

Imago is an **image-first visual creation and editing workflow**, not an image-prompt generator.

The highest-priority behavior is:

> When a user asks for a visual and the host has image-generation/editing capability, create or edit the visual directly.

Do not replace a requested visual with:
- a generated prompt;
- code;
- JSON;
- tool arguments;
- a file path;
- a long explanation.

unless the user explicitly asks for those outputs.

## Architecture

Keep v0.1 skills-only.

Do **not** add:
- MCP;
- an external image-generation API;
- authentication;
- remote storage;
- publishing integrations;
- custom UI.

Use the host's native image-generation/editing capability when available.

## Required workflow

Preserve:
- create vs edit routing;
- reference-image role detection;
- localized edit preservation;
- multi-turn visual continuity;
- exact text handling;
- aspect-ratio inference;
- transparent-background handling when requested/supported;
- document/data-to-visual workflows;
- screenshot/UI redesign;
- web research for current factual visuals;
- strict no-fabrication rules for data, statistics, quotes, prices, and labels;
- concise visual-first responses;
- no fake paths or claims of generated artifacts.

## Files to preserve
- `SKILL.md`
- all references
- `agents/openai.yaml`
- public listing material
- test cases
- research notes

## Branding
The bundled icon is a temporary neutral Imago icon because the canonical production logo was not present in the available source library. Replace it with the canonical Imago logo before public publication if the original asset is available.

## Validate
1. ZIP root discovery.
2. `plugin.json` and `skills: "./skills/"`.
3. Skill frontmatter.
4. `agents/openai.yaml`.
5. In-package asset paths.
6. Display/subtitle/capability/prompt limits.
7. `Creativity` category.
8. Five positive and three negative test cases.
9. No MCP dependency added.
10. No instructions that turn Imago into a prompt-only assistant.

Do not create, install, or submit the plugin unless the user explicitly asks for that action.
