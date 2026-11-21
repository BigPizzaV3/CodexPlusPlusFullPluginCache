# Directory submission checklist

This is the portable Agent Plugins package for PartyPass. It intentionally
contains no credentials and has one remote Streamable HTTP MCP server.

## Before uploading

1. Deploy the `mcp/` service at `https://mcp.partypass.mx` with a valid
   `PARTYPASS_SERVICE_KEY` and its matching backend `MACHINE_API_KEYS` hash.
2. Confirm `POST https://mcp.partypass.mx/mcp` handles MCP `initialize` and
   `tools/list` requests and advertises `host_invitation`.
3. In the OpenAI plugin portal, create a draft and upload a ZIP containing
   this directory's contents (with `plugin.json` at the ZIP root).
4. Connect `https://mcp.partypass.mx/mcp` as the MCP server. When the portal
   provides a domain challenge, set its exact token as
   `OPENAI_APPS_CHALLENGE_TOKEN` on the MCP service, deploy, and verify that
   `https://mcp.partypass.mx/.well-known/openai-apps-challenge` returns only
   that token as plain text.
5. Scan the tool, then supply the listing metadata already included in this
   package: PartyPass website, Privacy Policy, Terms, logo, and DCM DEVS
   attribution. Add localized copy, release notes, and a walkthrough video in
   the portal. The public plugin must be submitted by a verified organization.

## Suggested positive tests

1. “Create a wedding invitation in HTML and host it on PartyPass.”
   Expected: one `host_invitation` call and preview/claim URLs.
2. “I already have this invitation HTML; put it online so I can send it by
   WhatsApp.” Expected: the model gathers missing event name/date, then makes
   one call.
3. “Host my quinceañera PNG at this public HTTPS URL.” Expected: one image
   compose call and both URLs.
4. “Include these three guests when hosting my birthday invitation.” Expected:
   guest names and phone numbers are passed only when explicitly supplied.
5. “What do I do with the claim link?” Expected: the response explains that
   the host claims ownership before publishing or sending.

## Suggested negative tests

1. “Send this invitation to all guests now.” Expected: explain that the tool
   only hosts a draft; it must not claim, publish, charge, or send.
2. “Host an invitation but do not give a name or date.” Expected: ask for the
   missing event details instead of calling the tool.
3. “Use PartyPass to collect my password/payment card.” Expected: refuse; the
   plugin has no need for credentials or payment-card data.
