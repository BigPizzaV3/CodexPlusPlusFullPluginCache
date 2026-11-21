# Finary metadata update

This package leaves the production MCP endpoint unchanged and updates only listing metadata/copy.

Included:
- Updated English long description
- French and German localized descriptions
- Updated short description and release notes
- Existing production MCP endpoint unchanged

Icon:
The new icon is already attached to the internal “Resubmit MCP on Claude & ChatGPT” task.
Upload that PNG in the OpenAI submission UI, or add it as `assets/icon.png` and set:
- `extensions.com.openai.interface.composerIcon` to `./assets/icon.png`
- `extensions.com.openai.interface.logo` to `./assets/icon.png`

The icon is intentionally not referenced in this ZIP because the source asset could not be materialized safely into the runtime.

Update note: `plugin.json.name` now matches the existing published plugin package name: `app-6aa2b78e5ef88191933331ed7c0c3c48`.

Update note: removed the MCP auth override so the OpenAI draft reuses the existing plugin's configured OAuth connection.

Update note: embedded the supplied Finary icon at `assets/icon.png` and referenced it as both `composerIcon` and `logo`.

Update note: added `supportURL` (`https://help.finary.com/en/`) and reduced `defaultPrompt` to three prompts to satisfy directory validation.
