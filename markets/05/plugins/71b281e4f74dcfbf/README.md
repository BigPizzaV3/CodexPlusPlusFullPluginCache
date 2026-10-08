# Bits & Bolts Remote

The hosted MCP Extensions demo for ChatGPT and Codex. This package contains its skills, onboarding, and SVG branding; public app binding is pending. The MCP server, widget, and CAD assets remain in the existing Vercel deployment at `https://mcp-extensions-examples.vercel.app/bits-and-bolts/mcp`.

## Identity

- Reserved global plugin: `Plugin_d854f570dcdc81918e88c18223a6dacd`.
- Package name: `bits-and-bolts-remote`.
- Public app: not yet bound.

The reserved plugin is `GLOBAL`, `RESTRICTED`, and `UNLISTED`, with no published release. Its source mapping is recorded in `project/cloud_plugins_import/cloud_plugins_import/global_plugin_registry.json`. The existing workspace app and canonical plugin remain separate; do not reuse their binding for this release. The package does not run a local MCP server.

## Public release

Publish only the remote implementation, named **Bits & Bolts Remote**. Bits & Bolts Local remains internal. This source entry prepares the maintained package. Merging it does not publish the MCP app or change the existing plugin's audience.

1. Give the developer organization ownership of the reserved plugin's submission target, upload a draft declaring the remote server in `.mcp.json`, and create the backing app through plugin-first MCP conversion using this plugin ID, submission ID, and MCP server key. Complete app configuration and approval, and verify the Personal or Work demo-account connection flow.
2. Add the resulting app's verified ID to this package's `.app.json` and restore the manifest's `apps` reference before publishing. Preserve plugin-managed app ownership; do not create a separate canonical plugin or add app-managed release ownership fields to the registry.
3. Follow [Publish One Plugin](../../docs/maintainer-guide.md#publish-one-plugin). Verify the destination's actual app publication state, installation policy, authentication policy, product availability, and rollout restrictions. The catalog requests optional installation with authentication on install.
4. Validate the completed package and publish its first release to the reserved plugin through the supported release workflow. Keep it unlisted; use an enforced access gate for tester-only releases, since `RESTRICTED` does not enforce private access and `UNLISTED` remains searchable.
5. From an external account, install the public plugin, connect a demo account, open the Parts Library, and exercise settings, a composer mention, and a supported CAD file. Update the developer documentation's install link if the public identity changed.

The version here is a release candidate; the plugin record is reserved, but no release has been published. Server and widget updates continue through the [remote MCP publication steps](../../../../project/mcp_extensions/skills/mcp-extensions/references/bits-and-bolts.md#bits--bolts-remote-mcp).
