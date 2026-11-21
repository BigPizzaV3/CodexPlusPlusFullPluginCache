SMARTe OpenAI Plugin - Codex-compatible submission package

This package uses the format accepted by the current upload validator:

.codex-plugin/plugin.json
.mcp.json
assets/icon.png
assets/logo.png

MCP endpoint:
https://mcp.smarte.pro/mcp

The prior portable package used root plugin.json + mcp.json. OpenAI's current
documentation supports that portable format, but the dashboard error shown by
the user explicitly requested a recognized compatibility manifest such as
.codex-plugin/plugin.json and plugin content such as .mcp.json. This package
therefore uses the Codex compatibility layout.

After upload:
1. Connect/scan the MCP in the MCPs tab.
2. Complete domain verification.
3. Check all automated findings.
4. Verify the demo recording is reviewer-accessible.
5. Enter reviewer credentials only in the secure dashboard fields.
