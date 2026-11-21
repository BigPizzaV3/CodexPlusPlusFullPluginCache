# RelayQ ChatGPT submission package

This package creates a fresh OpenAI listing named `relayq-chatgpt`, displayed as RelayQ. The original legacy listing export and earlier replacement package are retained separately.
It contains the listing metadata, production icon, MCP connection, explicit OAuth dynamic registration settings, and five positive and three negative review tests.

Build and validate from the repository root:

```sh
node scripts/build-chatgpt-plugin.mjs
```

Upload the generated ZIP as a new plugin. Complete MCP connection and tool discovery before submitting for review. Preserve the listing's existing verified developer identity and availability settings.

Reviewer sign-in credentials are entered only in OpenAI's secure dashboard. They must never be added to this package. Domain challenge tokens and OAuth client secrets are also excluded.

All positive tests read tasks or create expiring previews. None commits task changes or deletes the demo fixtures. The hosted MCP server may expose additional tools beyond these review cases.
