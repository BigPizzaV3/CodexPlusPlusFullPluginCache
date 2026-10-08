# OpenAI Credit Bridge skill

This is a portable skills-only Agent Plugin package. It replaces the rejected ChatGPT app-submission manifest with a root `plugin.json` and a skill under `skills/`.

It does not include or expose an API key. To perform OpenAI API calls, separately deploy and connect a secure MCP gateway exposing the tools described in `SKILL.md`.
