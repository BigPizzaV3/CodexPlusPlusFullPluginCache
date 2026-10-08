# Atelier Pottery Mentor Plugin

Version: 0.1.1

A skills-only pottery and ceramics mentor for technique, critique, ceramics-focused image generation/editing, glaze/firing troubleshooting, kiln/cone education, controlled testing, functional-ware caution, and studio safety.

## Architecture

```text
Atelier Pottery Mentor
└── pottery-mentor
    ├── pottery technique & process
    ├── ceramic critique
    ├── ceramics visualization / image editing
    ├── glaze / firing troubleshooting
    ├── kiln / cone guidance
    ├── functional-ware safety
    └── studio safety / materials
```

No MCP server is required for v0.1.1.

The plugin can use native host image generation/editing for ceramics visualizations. It does not control kilns, execute firing programs, chemically test glazes, or certify food safety.

## Package structure

```text
plugin.json
assets/
  icon.png
  logo.png
skills/
  pottery-mentor/
    SKILL.md
    agents/
      openai.yaml
    assets/
      icon.png
    references/
      critique_framework.md
      ceramics_visualization_workflow.md
      pottery_technique_and_process.md
      glaze_firing_troubleshooting.md
      kiln_cones_and_firing.md
      studio_safety_and_materials.md
      functional_ware_safety.md
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

## Recommended next step

Review the package, test it with real pottery photos and real firing/glaze scenarios, and upload the ZIP through the plugin submission workflow only when ready.

This package has **not** been created, installed, or submitted as a plugin.
