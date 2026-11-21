# Notamify

Search NOTAMs, explore affected infrastructure and generate informational airport and flight briefings in your assistant.

Connect through your existing Notamify account. Requires an active Pro subscription or an existing API agreement and uses your API credits.

MCP endpoint: `https://mcp.notamify.com/mcp`

[Setup guide](https://notamify.com/manual/reference/connected-apps) | [Manage connections](https://notamify.com/account#connections)

## Connect

For Claude Code, load the downloaded ZIP with `claude --plugin-dir /absolute/path/to/notamify-plugin.zip`, run `/mcp` and sign in.

For Codex, install the package from the Notamify marketplace, then run:

```sh
codex mcp login notamify --scopes notams:read,briefings:write
```

For ChatGPT and Claude web or desktop, add the MCP endpoint using OAuth. Briefing generation requires the additional permission shown during sign-in. Use the separate Muse package for Meta Muse Code.

## Privacy and support

Notamify processes your queries and supplied flight details to provide results. Review the [Privacy policy](https://notamify.com/privacy) and [Terms](https://notamify.com/terms). You can revoke access in [Account settings](https://notamify.com/account#connections).

Interpretations and generated briefings are informational. Verify operational decisions against current official aviation sources.

This connector package is MIT licensed. Contact [hello@notamify.com](mailto:hello@notamify.com).
