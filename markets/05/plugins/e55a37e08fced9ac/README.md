# Parsewise

Extract data from document sets with citations. Turn collections of contracts, reports, invoices, and other documents into structured results you can trace back to the source. Define the fields you need, compare information across documents, calculate derived metrics, and investigate missing or inconsistent results. Organise your document sets in Parsewise projects and track extraction progress directly from your assistant.

## Connection

- Server: `https://api.parsewise.ai/mcp`
- Transport: Streamable HTTP
- Authentication: OAuth through the host's connection flow
- Required access: a Parsewise account and organisation with permission to perform the requested operation

All tools exposed by the server are available to the host; the package does not restrict tools or override the user's permissions. Tool availability follows the connected server. The accompanying `parsewise` skill explains the workflows and operational details.

Document uploads need a host capable of sending file bytes to the temporary upload URL returned by Parsewise. If that capability is unavailable, upload in the Parsewise app and continue through MCP.

## Package layout

- `plugin.json`: portable Agent Plugins manifest with OpenAI presentation metadata.
- `mcp.json`: production remote MCP connection.
- `.codex-plugin/plugin.json` and `.mcp.json`: matching Codex compatibility manifests.
- `skills/parsewise/SKILL.md`: workflow guidance.
- `assets/`: Parsewise brand icons.

The package contains no credentials, customer documents, backend source, or local environment configuration.

## Links

- [Parsewise](https://www.parsewise.ai)
- [MCP documentation](https://docs.parsewise.ai/parsewise-mcp)
- [Support](https://www.parsewise.ai/contact) · support@parsewise.ai
- [Privacy policy](https://www.parsewise.ai/privacy-policy)
- [Terms and conditions](https://www.parsewise.ai/terms-and-conditions)
