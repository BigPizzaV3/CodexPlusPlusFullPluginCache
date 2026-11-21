# Retiplex plugin

Version 0.1.3 packages the existing Retiplex MCP server with a reusable video-ad
workflow, Retiplex's logo, listing metadata, and eight proposed review cases.
It uses the supported Codex compatibility layout used by Plugin Creator.

## Connection

- Server: `https://app.retiplex.com/mcp`
- Transport: Streamable HTTP
- Authentication: OAuth; each user signs in to their own Retiplex account.
- Current workflow guide: https://app.retiplex.com/help/agents

The MCP exposes 20 tools for account and project reads, product media, cast,
required moments, creative briefs, scripts, storyboards, rendering, and recovery.
The plugin relies on the hosted server for schemas and execution. No credentials
or local server dependencies are bundled.

## Install and test

The active connection is registered as
`asdk_app_6ac7aa6760388191bc418e6eba5fb76f`.
`.app.json` declares it as required, and the manifest references that mapping.
The directory URL uses `plugin_asdk_app_...`; the mapping's `id` omits `plugin_`.
Install the plugin from a local marketplace and complete OAuth if requested,
then test it in a fresh chat.

This repository's `.agents/plugins/marketplace.json` exposes the folder as
Retiplex in the **Retiplex Local** source. Restart the desktop app, open the
plugin directory, select that source, and install Retiplex. The entry points to
`./plugins/retiplex` from the repository root. Plugin enablement and OAuth remain
part of installation.

`.mcp.json` also contains the direct endpoint configuration. It is an alternate
connection definition, not a second active connection. To use the direct server
instead of the registered mapping, replace `"apps": "./.app.json"` in the
manifest with `"mcpServers": "./.mcp.json"`. Do not enable both for the same server.

Packaging and local installation:
[OpenAI plugin package guide](https://developers.openai.com/plugins/build/plugins).

## Validation and review

The manifest contains five positive and three negative review scenarios under
`extensions.com.openai.review.test_cases`. They are proposed cases, not recorded
successful runs. Use a dedicated test account with the appropriate plan,
credits, and prepared projects to run them. Rendering and recovery cases spend
credits only after the user has authorized them.

For a Platform upload, use the `retiplex-0.1.3-platform.zip` package. Its manifest
declares `"mcpServers": "./.mcp.json"` and the archive omits `.app.json` and the
`apps` declaration. Platform submits the MCP server directly; registered
connection mappings are for local or workspace installation.

Upload through **With MCP**, then complete the
portal's domain verification and OAuth connection, and provide reviewer access
and a walkthrough recording. Keep reviewer credentials outside the package.
Public submission and publication have not been performed.

The public listing describes video creation and uses **Creativity**, a supported
category. It contains no pricing, subscription offers, or promotions.
The five positive cases, three negative cases, release notes, and
[walkthrough recording](https://www.loom.com/share/d18169a16716469b9390a2fff5871283)
are included. The recording URL is stored in
`extensions.com.openai.review.demo_recording_url`.
Review readiness still requires the following external materials:

- Dedicated reviewer account access and sign-in instructions, entered in
  Platform's secure Review details form. Keep secrets outside the ZIP.
- Successful runs of the review cases against the prepared test account.

Reviewer access and test-case results have not been independently verified here.

[OpenAI submission guide](https://developers.openai.com/plugins/deploy/submission).

## Source

- `.codex-plugin/plugin.json`: identity, listing, and proposed review cases.
- `.app.json`: the active registered Retiplex connection.
- `.mcp.json`: the alternate direct hosted MCP configuration.
- `skills/video-ads/SKILL.md`: the ad workflow and spending rules.
- `assets/logo.png`: copied from this application's `public/logo-transparent.png`.

Keep the skill's workflow aligned with `src/lib/agent/server.ts`. Read the live
`retiplex://guide` resource for current costs and requirements rather than
copying a price table into the plugin.
