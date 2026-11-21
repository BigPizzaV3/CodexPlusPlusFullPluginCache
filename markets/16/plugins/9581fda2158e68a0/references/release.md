# Release guidance

- OpenAI packaging: https://developers.openai.com/plugins/build/plugins
- Submission: https://developers.openai.com/plugins/deploy/submission
- Plugin guidelines: https://developers.openai.com/plugins/plugin-guidelines
- Generated MCP server docs: https://ts.sdk.modelcontextprotocol.io/v2/

This **MCP App Builder** package is skills-only and does not bundle any remote MCP URL or built-in code execution. It can author MCP servers and UI in a host that provides coding tools. Do not add a dummy MCP endpoint; the generated apps are users' independent projects, not dependencies of this plugin.

To publish this package publicly: upload ZIP in OpenAI's plugin submission portal; verify developer identity/metadata/icon; resolve automated findings; submit for review and publish only after approval. Skills-only public listing may have additional eligibility conditions. If later adding the builder's own hosted MCP server, the public plugin identity may need a separate initial submission; OpenAI currently does not allow adding MCP to an already-submitted skills-only plugin. This is a **product decision**, not a reason to invent an endpoint now.

Never claim private Creator upload is equivalent to public submission. Plugin Creator can create/update private plugins; publication requires portal actions and review where available.
