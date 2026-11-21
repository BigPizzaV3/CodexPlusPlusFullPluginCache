# Landfillom by Agel AI

Approved brand: Landfillom / Agel AI / https://landfillom.com/.

The app icon is the green O with two leaves on navy from the LANDFILLOM brochure,
approved on 2026-09-27. The exact same PNG is used for the plugin, MCP server and
browser favicon. Its native dimensions are 1254 x 1254.

`plugin.json` is the portable manifest, with OpenAI presentation fields under
`extensions.com.openai.interface`. `mcp.json` connects to the existing OAuth MCP
endpoint. `.codex-plugin/plugin.json` and `.mcp.json` provide a compatibility
package using the same presentation fields and endpoint. No credentials are bundled.

The MCP server advertises websiteUrl and icons in its initialization identity and
serves only the fixed public PNG at `/assets/landfillom-icon-v2.png`. Tools still
require authentication. Developer name is package/listing metadata, not a standard
MCP serverInfo field. Refreshing an existing URL-only MCP connection may not apply
all plugin listing fields; do not claim the ChatGPT information screen changed
until observed. Public directory submission requires the OpenAI publisher workflow.

The browser icon is set in front/index.html with a versioned PNG URL. Existing tabs
may need reloading. This package is prepared locally; installation/listing publication
is separate from deploying the server.

References:
- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/deploy/connect-chatgpt
- https://developers.openai.com/plugins/deploy/submission
