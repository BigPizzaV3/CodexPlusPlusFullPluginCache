# Lifeinvader Ads Editor plugin — 0.1.6

Website: https://li.mailme.cfd/
Remote MCP endpoint: https://li.mailme.cfd/mcp
Authentication: None. No application account, license or API key.

## Update in the publishing dashboard

1. Open the existing plugin draft/listing in https://platform.openai.com/plugins.
2. Upload the new ZIP as a new version of that existing plugin.
3. Check Metadata & Skills: version 0.1.6, Badhon Vitality, logo, composer icon,
   website, support, privacy and terms links.
4. Under MCPs, connect/reconnect the HTTPS endpoint above with Authentication: None.
   Complete any portal domain verification and rescan the tools if requested.
5. Test the skill and tools in a new ChatGPT web conversation, then submit the
   update through the dashboard when ready. Publishing/review is not performed by
   uploading this local archive here. Availability remains subject to the host.

## Web-compatible package

The package uses a remote HTTPS Streamable HTTP server, not a local executable.
It has no desktop-only requirement, lifecycle hook or local MCP process. The root
portable manifest and mcp.json are canonical. The .codex-plugin/plugin.json and
.mcp.json files remain as a desktop compatibility fallback; both use the same
branding and endpoint. No registered app IDs or credentials have been invented.

Icons are bundled locally under assets/ rather than relying on the host to fetch
an external image URL. icon.svg is the original website icon; PNG derivatives
provide a 128x128 composer icon and a 512x512 listing logo.

The ad-editing SKILL.md includes the corrected canonical-item workflow. It specifies short copyable
Edited/Category output, individual history reuse, automatic public saves, Cloud
Agent attribution and no MCP history export. Editing automatically publishes raw
input with the edited ad and reported agent name. Do not include private information.

## Changes in 0.1.3

- Package the website icon as SVG and PNG assets.
- Set interface.logo and interface.composerIcon in both supported manifests.
- Add actual website, support, privacy and terms listing fields.
- Correct the developer name to Badhon Vitality.
- Preserve the existing skill and anonymous remote MCP configuration.

This package has not been installed or approved inside your ChatGPT account by
this local preparation step. Complete the dashboard connection and web test.

References:
- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/deploy/submission

## Formatting fixes in 0.1.3

Resolve existing item names through search_catalog and pass supported selectors
separately. For example, `selling pink lu vi pant price nego` must produce
`Selling pink Lui Vi pants. Price: Negotiable.` Preserve the raw source exactly.
The live server resolves known spelling/singular variants and preserves inline
modifiers when another selector changes. Unknown custom items are not guessed.

The server advertises version 1.4.0 and per-item selector options. Rescan MCP tools
in the publishing dashboard, then upload this package to update the bundled skill.
Use a fresh chat/refresh the connection to test the current tool metadata.
MCP history lookup and automatic saves remain anonymous; no MCP export tool exists.
Browser exports alone require a license.


Version 0.1.6: MCP server 1.4.0 adds the operator-approved Lighting Charge and pet entries and shared local search with aliases, reordered words, punctuation and conservative spelling suggestions. suggestedSpelling marks a candidate, not permission to replace the intended model or item. Use the exact intended returned catalog name; composition still rejects unknown names and NOT Sellable cars before saving. Automatic public saving, Cloud Agent attribution and browser export licensing remain unchanged. Search matches and history reuse do not create records. Upload this updated skill, rescan tools and start a fresh chat.
