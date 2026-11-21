---
name: pyai-get-started
description: "Connect to PyAI, discover its voice AI tools, or choose between speech, transcription, voice agents, Trace, Recap, dubbing and narration."
---

# Get Started

Use the connected PyAI tool schemas as the source of truth; clients may prefix tool IDs with the server name. If PyAI is disconnected, direct the user to the host's browser sign-in. Keep credentials out of chat. Respect the selected project and the user's authorized task.

Tools: `get_started`, `discover_tools`, `whoami`

Call `get_started` for the current integration guide, then `discover_tools` with the user's use case. Before project operations, use `whoami` to confirm the selected workspace and granted scopes; do not read project data merely to demonstrate connectivity.

For a connection check, use only `get_started` and `discover_tools` with query `TTS`. Report whether they succeeded without generating audio or creating resources.

For application development, consult https://api.pyai.com/openapi.json and https://docs.pyai.com before writing request fields. Use the official SDK for realtime media sessions. Prefer existing user-supplied files and IDs; do not manufacture example customer data in the connected project.

A scope error needs appropriate project consent; a credit error needs user action. Do not loop on either. CLI fallback and setup: https://pyai.com/cli and https://pyai.com/mcp.

Supply only recordings and text the user is authorized to process. Do not solicit or submit payment-card data, protected health information, government identifiers, passwords, or API keys. Hosted MCP does not purchase phone numbers or initiate checkout. Explain entitlement limits without directing the user into a purchase.
