# 10Signals

10Signals helps online stores, startups and agencies understand their competition, starting with a website address. It researches public websites to find competitors and compare products and prices. The chat plugin lets you request research, explore available reports, compare rival offers, and monitor selected products for price changes.

New here? Ask “What does 10Signals do?” or “How could it help my store?” No connected account is needed for an explanation. Connect a 10Signals account to run research or access and manage your private reports and watches; plan allowances and available credits apply. Research covers the pages found and checked, not every product or competitor in the market.

Cards and tables are available in compatible chat clients. No credentials are bundled.

## Included actions

See [the complete action guide](ACTIONS.md) for all 84 registered tools, exact names, permissions, examples, confirmation steps and limitations. It covers report creation, catalogues, competitors, insights, comparison choices, price watches, notifications, refreshes, sharing and organisation tracking. Tools are discovered from the remote MCP server after authorisation; `plugin.json` describes the plugin rather than defining each API action.

## Install for local/team testing
Add this repository as a local plugin marketplace in a supported desktop host. Select **10Signals** and complete OAuth consent. This package targets OpenAI hosts; its documented OAuth extension is not accepted by the unextended Agent Plugins 1.0.0 MCP JSON schema. This OpenAI package uses a registered public OAuth client with PKCE and explicit consent. Run the setup skill in a fresh chat. UI requires an MCP Apps-compatible host; other clients retain structured tool results.

The repo marketplace is private/team distribution, not public-directory approval. For ChatGPT web register https://10signals.xyz/mcp through Add custom MCP server / Create as a plugin, then verify the issued plugin_asdk_app ID before adding a registered-app mapping. Do not invent an ID or substitute another connector. Public submission also requires verified publisher, support contact and a reviewer account configured securely in the portal. Review the existing analytics privacy page for complete plugin disclosures before public submission.

## Acceptance
Fresh consent, authenticated tool discovery, refresh/revoke, scoped reads, action-specific confirmation/replay, and actual in-chat rendering must be recorded independently. Fixtures are for automated tests only. Do not test deletion on customer records. Changes that start research or monitoring must be tested within the agreed allowance.

OAuth uses the OpenAI per-server authentication extension in mcp.json: a provided public client (no client secret), the 10Signals MCP resource and offline_access as a base scope. Endpoints and resource scopes are discovered from the server. Never configure a fixed bearer key. Existing registrations with cached scopes may need to be updated and reauthorized.

## Public submission review
The manifest includes five positive and three negative review scenarios and release notes. These scenarios are review instructions, not a claim that live acceptance has passed. Before submitting, run them with an isolated reviewer account and add the actual accessible demo recording URL to review.demo_recording_url. Configure reviewer credentials only in the secure portal, never in this package. Publisher/domain verification and first-load card acceptance must also be confirmed.
