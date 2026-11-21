# FlowsDesigner ChatGPT plugin package

Upload `flowsdesigner-plugin.zip` at platform.openai.com/plugins → "Upload new or existing plugin"
(an Organization owner, or a member with the Apps Management Write role, under a verified developer identity).

Contents: `plugin.json` (listing), `mcp.json` (the remote MCP server at https://flowsdesigner.com/api/mcp,
OAuth with dynamic client registration), `assets/` (logo 512 px, composer icon 256 px).
Review-form text (test cases, annotation justifications, release notes, reviewer account) is in
`REVIEW-DETAILS.md`, kept outside the ZIP on purpose.

Rebuild the ZIP after edits:  `cd integrations/openai-plugin && rm -f flowsdesigner-plugin.zip && zip -r flowsdesigner-plugin.zip plugin.json mcp.json assets`
