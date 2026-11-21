# Flova for Codex

Plugin ID: `flova`. Version: `0.0.5`.
MCP endpoint: `https://service.flova.ai/api/mcp/`. Client header: `X-Plugin-Agent: codex`.

See the repository's root [README](https://github.com/FlovaAI/flova-plugin/blob/main/README.md) for installation instructions. This directory is a self-contained plugin package with an Agent Plugins manifest, a Codex compatibility manifest, MCP configuration, icons, and Skills. Keep the identity, version, and interface metadata consistent across both manifests.

## Skills and Media Previews

- `flova`: Generate media directly, or delegate planning, production, and delivery to Flova Agent within a project.
- `flova-debrief`: Review creative performance and prepare recommendations for the next production.
- Query actual progress first. Open a preview card once at least one resource succeeds, without waiting for every task to finish.
- A run or batch may have multiple cards for new resources, production stages, or user-selected groups. Existing cards refresh through the service's `data.refresh` instructions and merge resources by ID.
- Continue tracking the run and pending approvals. Avoid repeatedly presenting unchanged media, and never treat a preview as approval to generate.
- If the tool is unavailable or a card cannot be displayed, follow the service's instructions using supported media or returned links.

See the [Skill](skills/flova/SKILL.md) and its references for the complete rules. The package does not include the backend or UI. A successful tool call does not establish that a card loaded or its media was inspected.

The Skills are shared with the Claude package. When updating them, keep the Skill instructions, reference documents, and assets identical across both packages. Keep `agents/openai.yaml` only in this Codex package.
