# Ultrametric

Use company process guides and saved company context from your agent. The plugin connects to `https://api.ultrametric.ai/mcp` and includes instructions for discovering processes, preparing sourced drafts, saving progress, and resuming work. It runs no local server and requires no Ultrametric CLI.

The API checks your account, selected organization, permissions, and process access. The active agent follows the guides with its available tools. Opening a process or saving its reported progress does not execute a filing, purchase, or other external action.

## Connect

Reuse an existing working connection. For a new account, complete [workspace setup](https://api.ultrametric.ai/auth/setup), install the package through your host, and finish its MCP sign-in. Keep one Ultrametric connection active for the work.

Ask your agent to list available Ultrametric processes, then resume your company work or start a relevant process. If the account or organization is wrong, check connection status and reconnect through the host. Do not paste passwords or tokens into chat or package files.

## Package formats

| Host | Files |
| --- | --- |
| ChatGPT/Codex, Cursor, Copilot/VS Code, Kiro | Root `plugin.json`, `mcp.json`, and `skills/` |
| Claude | `.claude-plugin/plugin.json`, `.mcp.json`, and the same `skills/` |
| Gemini CLI | `gemini-extension.json` and the same `skills/` |

Each configuration uses the same production endpoint. Hosts manage their own OAuth credentials and approval settings. Optional UI depends on host support; text and structured results remain available.

Clone the [package repository](https://github.com/ultrametricai/ultrametric-plugin), then run these commands from its root. For an extracted ZIP, use its root. For an API source checkout, first run `cd plugin`.

```sh
# Claude Code: load for this session.
claude --plugin-dir .

# Copilot: install the package directory.
copilot plugin install .

# Gemini: link the extension directory.
gemini extensions link .
```

For a persistent Claude Code installation, run these commands from the extracted package root. The bundled marketplace resolves to this same directory.

```sh
claude plugin marketplace add .
claude plugin install ultrametric@ultrametric
```

After the package containing this catalog is published to the public repository, users can add it with `claude plugin marketplace add ultrametricai/ultrametric-plugin` and use the same install command. The local catalog does not establish a published marketplace or directory listing.

In Kiro, use **Add Custom Power → Import power from a folder** and select the package root. For other hosts, use their documented local package or marketplace flow.

For a ZIP installation, extract the archive and select its root directory, or upload it through a host that accepts plugin ZIPs. `server.json` is metadata for the official MCP Registry; it does not configure an additional connection.

These files are prepared for the documented formats. A package does not establish a public listing or verify every host.

## Distribution

This repository contains generated package files. The private API repository maintains the source and validates the package before export. Make changes there, then export a new package; do not maintain a second implementation here. `plugin.json` records the package version. Distribution commits record the source revision. Shared process guides remain hosted API content.

## Data and access

The service stores submitted company drafts, documents, progress, and authorized vault references in the selected organization. Draft storage is separate from user approval. Record changes retain revisions; deletion records a tombstone. Removing the plugin does not delete hosted records.

Send only information needed for the current task. Do not submit SSNs, banking credentials, payroll data, or secrets. Protected records require separate permission. A successful save receipt confirms storage, not the truth of a statement or completion of an external action.

Website: [ultrametric.ai](https://ultrametric.ai). [Privacy policy](https://ultrametric.ai/privacy/). [Terms of Service and contact](https://ultrametric.ai/tos/). The package is proprietary; see [LICENSE](LICENSE).
