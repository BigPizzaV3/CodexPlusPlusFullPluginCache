# Imago Plugin

Version: 0.1.0

Imago is a skills-only visual-first creative and information-design plugin for direct image generation, editing, redesign, reference-based creation, and factual/data-driven visual work.

## Core philosophy

```text
User asks for a visual
        ↓
Inspect supplied references/files
        ↓
Research only if factual freshness matters
        ↓
Infer non-blocking creative decisions
        ↓
Generate or edit the visual directly
        ↓
Iterate with preservation
```

Imago is not primarily a prompt-writing workflow.

## Package structure

```text
plugin.json
assets/
  icon.svg
  logo.svg
skills/
  imago/
    SKILL.md
    agents/
      openai.yaml
    assets/
      icon.svg
    references/
      visual_creation_workflow.md
      reference_editing_fidelity.md
      factual_visuals_and_data_integrity.md
      text_layout_and_format.md
      official_source_registry.md
submission/
  listing-and-prompts.md
  test-cases.md
  public-submission-checklist.md
  release-notes.md
docs/
  RESEARCH_NOTES.md
PLUGIN_CREATOR_PROMPT.md
README.md
```

## Architecture

No MCP server is required for v0.1. Imago relies on image-generation/editing capabilities already available in the host product.

## Branding

The included SVG is a temporary neutral Imago icon. Replace it with the canonical production Imago logo before public submission if the original asset is available.

## Recommended next step

Review the package, test direct creation/editing behavior in ChatGPT, replace the temporary icon if needed, and upload the ZIP only when ready.

This package has **not** been created, installed, or submitted as a plugin.
