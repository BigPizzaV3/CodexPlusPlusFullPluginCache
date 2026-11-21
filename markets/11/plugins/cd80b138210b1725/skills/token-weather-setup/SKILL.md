---
name: token-weather-setup
description: Check local runtime access and help a person use the Skills-only Token Weather package in a Codex project.
---

# Set up Token Weather

Find this skill's plugin folder two levels up. Run
`python3 "<plugin-root>/scripts/weather.py" --help` to check the bundled helper.
It needs Python 3.11 or later; if unavailable, explain how to choose an already
installed interpreter with TOKEN_WEATHER_PYTHON. Do not download dependencies
or change Codex's installed settings to check setup.

Use the current project's absolute workspace and exact current root chat ID
from trusted host metadata. Follow token-weather for one on-demand reading.
If local access or the record format is unavailable, explain the limitation;
do not guess a different chat or invent numbers.

Before first data access, explain the limited source and storage scope in
[local data and privacy](../../docs/PRIVACY.md). A one-off reading stores no
history and reads no config by default. Saved history and the persistent page
are explicit choices. `privacy-status` reports chosen local data locations
without creating folders; it does not delete anything.

This edition includes a separate numeric MCP and optional local helper scripts.
This local setup does not connect/deploy the MCP; it has no lifecycle hooks or automatic alerts. Do not register a project hook bridge,
change trust settings or enable a server connection. The full local plugin
remains a separate edition. Only start the loopback weather page when asked;
closing a browser tab does not stop its collector. Use weather-service stop
with the same chat ID to stop it. Checkpoint setup is separate and requires
an explicit request to enrol a workflow.
