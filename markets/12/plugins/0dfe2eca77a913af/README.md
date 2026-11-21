# Franlever plugin

Upload package for Franlever's existing remote MCP connection. Includes OAuth configuration, guided setup, daily operations and diagnosis instructions, brand artwork, and five positive / three negative review cases.

The plugin reads authorized store data and existing briefs. Franlever's backend continues daily monitoring and automatic delivery. This package does not deploy a server, modify the app or database, or schedule messages.

## Upload and connect

1. Select the intended organization/project at https://platform.openai.com and open Plugins > Upload new or existing plugin. Upload `franlever-1.0.3.zip`.
2. Select the verified individual publisher identity, Nathan David-Michael Steele and review Metadata & Skills findings.
3. In MCPs, connect `https://app.franlever.com/mcp`, complete domain verification, and authenticate with Franlever. OAuth uses dynamic client registration and `openid email profile` scopes, matching the existing server configuration. Confirm deployed discovery and callback support through this flow.
4. Run the bundled review cases with authorized connected store data. Include a restricted membership for scope checks. Check setup both in a fresh chat and after installation during a chat.
5. Provide reviewer access through the secure portal and add a reviewer-accessible demo video. Keep credentials out of the ZIP. Resolve automated findings before submitting; publish when ready.

Local validation: manifest schema, base MCP transport schema, skill frontmatter, asset paths, review-case counts, referenced tool names, and ZIP integrity. The published base MCP schema does not include OpenAI’s documented `extensions.com.openai.auth` field; that extension was checked separately against OpenAI’s packaging guide, not a published extension schema.

The draft now has a verified domain and authorized OAuth connection to the isolated sample-data reviewer workspace. The portal discovered 22 production tools and the first MCP scan reported no findings. The review recording uses actual ChatGPT MCP test captures with sample data, with waits shortened. It covers five positive cases and three boundary cases. Hourly shift data is intentionally absent in the sample; the correct outcome is to disclose the gap. Upload is not publication or proof of live delivery. See `docs/openai-plugin-submission.md` in the repository for operational setup notes.

Existing account/data setup happens in Franlever: Connect Data, Confirm Locations, Configure AI COO. Workspace assistant access must permit ChatGPT.

Official references:
- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/deploy/submission
