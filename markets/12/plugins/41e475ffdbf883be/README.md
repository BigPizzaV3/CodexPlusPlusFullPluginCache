# AskTexasEnergy comparison package

This is a separately uploaded package. The application does not serve these
manifest files. Upload the ZIP at https://platform.openai.com/plugins.
Uploading is not publication or approval.

Listing metadata belongs in plugin.json under
extensions.com.openai.interface. The stable package identifier is
asktexasenergy; the displayed name is AskTexasEnergy. The approved listing
subtitle is "Texas electricity, real prices". The publisher contact is
contact@asktexasenergy.com; the HTTPS support page is
https://asktexasenergy.com/about.

The endpoint in mcp.json is https://asktexasenergy.com/tools/plans/mcp.
Its authentication setting is none. Tool security and behavior declarations
are provided by the hosted endpoint's tools/list response, not by adding
unsupported tool fields to mcp.json:

- securitySchemes: [{"type":"noauth"}]
- readOnlyHint: true
- destructiveHint: false
- openWorldHint: false

No UI, sign-in, credentials, cookies, or enrollment capability are packaged.
assets/icon.svg copies the site's favicon, with a square 200 by 200 viewBox.
Both listing and composer icons reference this file.

Specification references:

- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/deploy/submission
- https://developers.openai.com/plugins/reference

OpenAI's documented per-server authentication extension is retained in
mcp.json. The generic Agent Plugins MCP schema currently disallows that
extension; this package does not claim unextended generic-schema validation.
OpenAI's upload checks are separate from the repository release gate and
cannot be confirmed until the owner uploads the ZIP.

Before submitting for review, complete the dashboard's verified publisher
identity, review materials, and applicable attestations. This package does
not change the application, its privacy policy, or its hosted tool behavior.
