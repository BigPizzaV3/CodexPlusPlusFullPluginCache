# Compatibility and acceptance

## Packaged surfaces

| Surface | Files or path | Status |
| --- | --- | --- |
| Portable Agent Plugins | `plugin.json`, `mcp.json`, ten `skills/*` folders | Packaged; validate against pinned schemas |
| Claude Code | `.claude-plugin`, `.mcp.json` | Packaged; authenticated client rehearsal pending |
| Codex | `.agents/plugins/marketplace.json`, portable package | Packaged; authenticated client rehearsal pending |
| Cursor | `.cursor-plugin` | Packaged; authenticated client rehearsal pending |
| Grok Build | `.grok-plugin` | Packaged; authenticated client rehearsal pending |
| Gemini CLI | `gemini-extension.json`, `GEMINI.md` | Packaged; authenticated client rehearsal pending |
| Skills CLI | Ten individually selectable skills | Skill-only installation; does not register MCP |

No public marketplace approval, registry publication, or authenticated client acceptance is implied by these files. The package's registry descriptor version is independent of the deployed server descriptor version. Server deployment is outside this repository.

## Public discovery evidence

The tool snapshot in `skills/vitae/references/tools.json` comes from unauthenticated `tools/list` at the public endpoint. It contains schemas only, no customer records. Its retrieval timestamp is recorded in that file. The server descriptor was also readable at `https://mcp.vitae.ai/server.json` on 2026-09-24.

## Client rehearsal

Record client version, OS, date, package commit, and outcome. Use a designated demonstration workspace.

1. Install the package or explicitly install the skill plus connector. Confirm all ten skills are visible after plugin installation; a Skills CLI installation should expose only the selected skills.
2. Complete OAuth in the client's browser flow and select the intended workspace.
3. List tools, then use live status and job-list read tools (`agent_status` and `list_jobs` when listed). Confirm only the intended workspace's records appear.
4. Ask for a job and candidate summary using supplied IDs or returned search results. Check IDs and claims against source records.
5. In a demonstration workspace only, request an authorized draft mutation. Confirm pending approval remains pending until the user decides. Check the record after execution; do not test destructive actions.
6. Revoke or disconnect access through the product and confirm the next protected call fails rather than silently using another credential.

Keep customer data and authentication evidence out of public reports. Publishing to a directory is a separate, explicit release action.
