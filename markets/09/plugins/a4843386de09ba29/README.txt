ARTLIST — DEVELOPER REVIEW PACKAGE

Review before deployment or Platform submission.

Contents
plugin.json — Listing metadata, starter prompts, primary demo link, five positive and three negative review test cases, release notes.
mcp.json — Artlist remote MCP endpoint.
assets/artlist-icon.png — Listing and composer icon.
dev-review/artlist-mcp-tools-list-proposed.json — Single proposed version of all 29 tools. This is not a verified live-server export.
dev-review/annotation-review.txt — Proposed changes, annotation rationale, and implementation questions.
dev-review/package-audit.txt — Full package audit and remaining submission checks.
dev-review/submission-notes.txt — Web, Android and iOS demo links and reviewer setup notes.

Start with dev-review/package-audit.txt, then annotation-review.txt. Verify the proposed tool descriptions and hints against the server implementation, especially upload_widget behavior, create_style_kit behavior, and irreversible credit charges. Apply the final reviewed definitions to the hosted server and rescan in Platform. Including a tools JSON file in this ZIP does not activate its definitions.

Reviewer passwords, tokens and client secrets are excluded. Enter reviewer credentials separately in Platform Review details.
The ZIP has been checked locally for JSON parsing, file references, and archive integrity. Live authentication, tool behavior, reviewer access, and review cases have not been tested by Codex. This is a developer review bundle, not the clean Platform upload ZIP.
