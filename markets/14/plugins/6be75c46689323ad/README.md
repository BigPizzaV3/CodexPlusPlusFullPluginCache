# The Buffers plugin

Research historic UK railtours, unusual workings and diversions with original
sources and labelled route schematics. Publisher: Mike Newman.

The package connects to `https://buffers.mikegtn.net/mcp` using Streamable HTTP
without authentication. It bundles a setup skill and a railway research skill.
The connected assistant interprets the evidence; no separate model/API key is
required. Public sources may be fetched and cached by the server. Avoid putting
private information in queries; routine web access logs are retained on the host.

## Install and verify

For repository-local testing in a supported Codex/ChatGPT desktop client, open
this repository and restart the desktop app to refresh local plugin sources.
In the Plugins Directory, select **The Buffers — local development** and install
**The Buffers**. Run its setup workflow and verify that `research_guidance`
returns current coverage. Test a new chat as well as an existing conversation.
Client availability varies; a package or local catalogue does not itself prove
that installation or the MCP connection succeeded.

For a portable package, use `dist/the-buffers-1.0.0.zip` from the repository root
with a client or developer portal that accepts Agent Plugins ZIPs. It contains
one top-level `the-buffers` folder. Root `plugin.json`/`mcp.json` are the portable
format; `.codex-plugin/plugin.json`/`.mcp.json` provide compatibility with Codex
clients that use that layout.

## Try it

- Did the McBuffer-Puffer traverse the City Union line?
- Which Pathfinder tours visited Ironbridge, and where did they reverse?
- Which locomotives operated the Christmas spin-and-win in 1995?
- Compare the Forth McFreighter's booked and actual timings.

## Coverage and publication

The source catalogue is broader than detailed report coverage. Reports are
indexed incrementally and fetched on demand. The tools expose actual coverage.
Scans may require visual reading, and some archives require manual access.
Schematics show source order rather than surveyed historical track geometry.

This package has not been submitted to or approved for the public plugin
directory. Public submission additionally requires developer-account registration,
domain verification, listing assets and support/privacy/terms URLs, then portal
tool/skill scans and review. Do not invent a registered app ID in `.app.json`.

Packaging: https://developers.openai.com/plugins/build/plugins
Submission: https://developers.openai.com/plugins/deploy/submission
