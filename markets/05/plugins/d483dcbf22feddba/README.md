# Saive plugin for ChatGPT and Codex

This folder is the plugin OpenAI's directory lists (bead sv-9pee, spec
`docs/plans/sv-9pee-openai-plugin.md`). It holds static files only: no build
step, and it sits outside the pnpm workspace.

- `plugin.json` is the manifest, and `mcp.json` points at
  `https://app.saive.my/api/mcp`.
- `skills/` holds one folder per skill, and ChatGPT discovers them on its own.
- `review/` holds the submission materials. The zip leaves it out.

## Build the submission zip

    scripts/package-openai-plugin.sh

The script writes `dist/saive-openai-plugin-<version>.zip`.

## Test locally

1. Copy this folder to `~/.codex/plugins/saive`.
2. Add it to `~/.agents/plugins/marketplace.json`:

       {
         "name": "local",
         "interface": { "displayName": "Local plugins" },
         "plugins": [
           {
             "name": "saive",
             "source": { "source": "local", "path": "./saive" },
             "policy": { "installation": "AVAILABLE", "authentication": "ON_INSTALL" },
             "category": "Productivity"
           }
         ]
       }

3. Restart the ChatGPT desktop app, install Saive from Plugins, and run the
   cases in `review/test-cases.md`.

`__tests__/openai-plugin-package.test.ts`, at the repo root, checks the package
against the Agent Plugins schemas.
