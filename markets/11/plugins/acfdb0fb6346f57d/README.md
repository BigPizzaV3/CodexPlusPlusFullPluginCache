# ProBeauty AI ChatGPT plugin

This package connects to the existing production MCP server. It contains no server implementation and requires no new hosting.

- Endpoint: https://app.probeauty.ai/api/mcp
- Transport: streamable HTTP
- Authentication: OAuth 2.1 with dynamic client registration
- Protected-resource discovery: https://app.probeauty.ai/.well-known/oauth-protected-resource
- No API keys or credentials belong in this package. Authentication is handled through the host's OAuth connection flow and server discovery, not hard-coded headers or invented OAuth fields.

The server owns tool schemas and annotations. Read-only tools: `list_workspaces`, `get_schedule`, `search_clients`, `get_client`, `list_services`, `find_availability`. Write tools: `create_booking`, `create_payment_request`, `reschedule_booking`, `cancel_booking`.

Support: https://www.probeauty.ai/support — support@probeauty.ai

Preparation status: manifest, MCP configuration, supplied icon, one front-desk skill, and draft review cases are packaged. See SUBMISSION.md for demo recording guidance and remaining review requirements. Protected-resource discovery was verified. No authenticated tool tests or write actions have been performed here.
