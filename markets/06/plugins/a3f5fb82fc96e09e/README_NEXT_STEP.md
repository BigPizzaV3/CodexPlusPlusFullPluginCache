# Ohana Plugin — Next Step

This is a portable **skill-only** plugin package. It contains no MCP server and requires no authentication.

## Test it in ChatGPT Work

1. Open a new **Work** task in ChatGPT.
2. Attach this plugin folder or ZIP.
3. Invoke the built-in plugin creator and say:

   `@plugin-creator Add the attached portable skill-only plugin named Ohana to a personal marketplace so I can install and test it locally. Do not add an MCP server or connected app. Preserve the included skill and supporting reference files.`

4. When the creator finishes, refresh ChatGPT.
5. Open **Plugins**, find the personal/local marketplace source, and install **Ohana**.
6. Start a fresh chat and type `@Ohana` to test explicit invocation where @-mentions are supported.

## Included files

- `plugin.json`
- `skills/ohana-assistant/SKILL.md`
- `skills/ohana-assistant/references/ContinuumIn_Pages_2024.pdf`
- `skills/ohana-assistant/references/OhanaVillage_Brand1Pager.docx`
- `assets/ohana-icon.png`

## Note

This package recreates the Ohana Assistant instructions developed in this project, including the activation banner. If your live Skill editor contains additional edits or approved-example files that are not present here, add those files before final team rollout.
