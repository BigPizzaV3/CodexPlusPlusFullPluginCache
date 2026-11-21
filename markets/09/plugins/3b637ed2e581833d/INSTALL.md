# Install or update the YouArt Plugin

This repository is the official source distribution for the complete YouArt
Plugin package: its manifest, creative workflow Skill, brand assets, and the
production YouArt MCP connection.

## Before installing

- Confirm the user asked to install or update YouArt.
- Never request, copy, print, or store a YouArt OAuth access token.
- Use the native browser OAuth flow when authentication is requested.

## First installation

Run:

```sh
codex plugin marketplace add youart-open-source/youart-plugin --ref main
codex plugin add youart@youart
codex mcp login youart-plugin
```

If the marketplace command cannot read the repository, stop and verify the
repository URL and network access. Do not replace the source with an untrusted
fork.

## Update an existing installation

Refresh the marketplace snapshot and reinstall the same Plugin:

```sh
codex plugin marketplace upgrade youart
codex plugin add youart@youart
```

Run `codex mcp login youart-plugin` only when the client reports that YouArt needs to
be authenticated again.

## Finish and verify

1. Completely quit and reopen ChatGPT Desktop or Codex Desktop.
2. Start a new Work task.
3. Confirm that one enabled Plugin named **YouArt** appears.
4. Confirm its MCP entry is named `youart-plugin` and connects to:

   ```text
   https://mcp.youart.ai/plugin/mcp
   ```

5. Confirm the bundled `creative-workflow` Skill is present.
6. Complete YouArt OAuth in the browser if prompted.
7. Try:

   > Show my three most recent YouArt projects.

Restart the client after an update so it loads the refreshed package. Do not
report installation as successful until the Plugin, Skill, MCP connection,
and OAuth state have all been checked.

## What YouArt can do

YouArt can find and create projects, build image, video, and audio workflows,
import source media, run approved generation steps, and return generated
assets in the conversation. Paid workflow runs require user confirmation and
consume the connected YouArt account's credits.

Privacy: https://youart.ai/privacy-policy

Terms: https://youart.ai/terms-of-service

Support: https://youart.ai/support

Security and privacy reports: support@youart.ai
