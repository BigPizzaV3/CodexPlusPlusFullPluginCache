# Notestack plugin package

This directory contains the source for the Notestack plugin ZIP.

The public package intentionally contains only:

- `plugin.json` for listing, review, and publication metadata
- `mcp.json` for the hosted MCP endpoint
- `skills/notestack/SKILL.md` for safe behavior when the MCP connection is unavailable
- public brand icons under `assets/`

The manifest points to the public support, privacy-policy, and terms-of-service pages on `notestack.ai`. Before submitting
for review, deploy those frontend routes, then add a reviewer demo recording and test-account credentials in the secure
dashboard fields. Credentials must never be added to this package.
