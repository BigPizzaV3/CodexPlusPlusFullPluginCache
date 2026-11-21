# Data handling

This package supplies instructions and connection configuration. It installs no daemon, hooks, or telemetry. The Skills CLI and AI client have their own data handling policies.

The client sends tool arguments to `https://mcp.vitae.ai/mcp`; Vitae authorizes the call and routes it to its API. Arguments and results can include candidate, client, job, and pipeline information. Use the intended workspace and include only what the task requires.

OAuth is the preferred authentication route. Store credentials through the client, never in this repository, a shared document, a URL, or a chat message. If OAuth is unavailable, follow Vitae's current setup documentation; do not silently create a token fallback.

Respect explicit user authorization and Vitae's server approval requirements. A pending approval is not a completed action. No skill should bypass role checks or approval boundaries.

See [Vitae privacy](https://vitae.ai/privacy) and [terms](https://vitae.ai/terms).
