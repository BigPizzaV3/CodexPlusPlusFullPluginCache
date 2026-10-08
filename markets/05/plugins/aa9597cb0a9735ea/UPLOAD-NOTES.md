# Platform upload notes

This package is prepared for the OpenAI Platform **Skills only** plugin upload flow.

Validation-sensitive choices in this package:

- `.codex-plugin/plugin.json` is present at the plugin root.
- At least one skill exists at `skills/<skill>/SKILL.md`.
- `author.name` and `interface.developerName` are present and match the currently selected verified developer identity.
- `interface.shortDescription` is within the final directory limit of 30 characters.
- `interface.defaultPrompt` contains no more than three prompts, each under the final directory limit.
- No MCP or `.app.json` configuration is included.

The Platform submission flow is for public review/publishing. Uploading creates a draft; it does not by itself make the plugin a private normal-Chat plugin.
