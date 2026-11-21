# YouArt Plugin

The official portable Agent Plugin package for
[YouArt](https://youart.ai). It combines a focused creative workflow Skill
with YouArt's production OAuth-protected MCP endpoint.

## Package contents

- `plugin.json` — portable Plugin identity and presentation metadata
- `mcp.json` — production Streamable HTTP MCP connection
- `skills/creative-workflow/` — general image, video, and audio workflow guidance
- `assets/youart.svg` — Plugin branding
- `.agents/plugins/marketplace.json` — ChatGPT/Codex marketplace catalog
- `INSTALL.md` — agent-readable installation and update protocol

## Install

Give an agent this instruction:

```text
Install or update the YouArt Plugin:
https://github.com/youart-open-source/youart-plugin/blob/main/INSTALL.md
```

Or add the repository marketplace directly:

```sh
codex plugin marketplace add youart-open-source/youart-plugin --ref main
codex plugin add youart@youart
codex mcp login youart-plugin
```

Completely restart ChatGPT Desktop or Codex Desktop after installation or
update.

## Architecture

This repository contains no YouArt backend source code or credentials.
`mcp.json` connects the installed Plugin to:

```text
https://mcp.youart.ai/plugin/mcp
```

That curated endpoint is implemented and deployed from YouArt's private
backend. It shares core YouArt services with the general MCP endpoint while
maintaining a separate public tool contract, OAuth resource audience, and
rollout switch.

## Validate the package

Run the dependency-free package checks before creating a release ZIP:

```sh
python3 -m unittest discover -s tests
```

## Security

- Never commit OAuth tokens, API keys, reviewer credentials, or signed URLs.
- Complete YouArt authentication only through the native browser OAuth flow.
- Review consequential and paid actions before approving them.
- Report security issues privately to `support@youart.ai`.
- Get installation and product help through
  [YouArt Support](https://youart.ai/support).

## Legal

Copyright © 2026 Formative Intelligence Inc. All rights reserved. The Plugin is
provided under the [YouArt Plugin Proprietary License](./LICENSE).

[Privacy Policy](https://youart.ai/privacy-policy) ·
[Terms of Service](https://youart.ai/terms-of-service)
