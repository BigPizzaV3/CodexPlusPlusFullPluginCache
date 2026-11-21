# REAHUB public plugin submission checklist

This ZIP is prepared for the OpenAI public plugin submission flow and intentionally contains no `.app.json` file.

## Included
- Portable `plugin.json` manifest
- Remote Streamable HTTP MCP configuration in `mcp.json`
- REAHUB grounding skill in `skills/instructions/SKILL.md`
- Square app icon in `assets/reahub-icon.svg`
- Public website, support, privacy and legal/terms URLs
- Exactly 5 positive and 3 negative MCP review test cases
- Global publication targeting (`countries: []`)

## Complete outside the ZIP before pressing Submit for review
1. Select a verified developer identity. The manifest uses `La Salle - Universitat Ramon Llull`; business verification must match the identity selected in the OpenAI Platform dashboard.
2. Connect the MCP endpoint `https://arc.salleurl.edu/reahubapi/mcp` using the **With MCP** submission flow.
3. Complete domain verification when the dashboard provides the challenge token.
4. Add a reviewer-accessible demo video URL in Review details. The manifest deliberately omits `review.demo_recording_url` because an invented or inaccessible URL would cause review failure.
5. Confirm the MCP scanner accepts the server-side metadata for both tools. OpenAI currently expects explicit `readOnlyHint`, `destructiveHint`, and `openWorldHint` annotations plus justifications on every tool. Both REAHUB tools should be read-only and non-destructive; the exact annotations must be declared by the MCP server itself, not by this ZIP.

No reviewer credentials are needed if the REAHUB MCP remains publicly accessible without authentication.
