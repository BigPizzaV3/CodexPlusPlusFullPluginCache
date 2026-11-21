# Senda

Ask about your company's Senda shipments, orders, containers, document details and tally reports, and get HS code suggestions. Read-only.

## What it does

Senda is where trade operations teams keep their orders, shipments, containers, documents and tally reports. Connect Senda to ask about your own company's records in plain language: where a shipment stands, which bill of lading and booking numbers it carries, when it is due, which documents are on file for an order or shipment, a container's type, weights and the shipments it is linked to, and how many pieces and board feet a tally report counted. Find any record by its shipment, booking, bill of lading, order, invoice or container number; every record the tools return carries its link in Senda.

Describe a product in plain words to get suggested 6-digit HS subheadings, with the US tariff schedule revision they were checked against. Suggestions are a starting point to confirm with a licensed customs broker, not a classification.

The connection is read-only: it cannot create, change, delete, file or submit anything, and it never returns file contents. It reads only the company you sign in to, and a Senda admin can disconnect it at any time from Settings → Integrations. Requires a Senda account with API access.

## Use it

The plugin adds Senda's MCP server, `https://sendaship.com/api/mcp`, and 2 skills that tell the assistant how to use it:

- **hs-code-suggestions**: Suggest HS codes for a product with Senda's find_hs_codes tool, and present them as suggestions to confirm with a licensed customs broker. Use when the user asks for an HS code, an HTS number, a tariff heading or "what code does this fall under", or describes a product they import or export and wants its classification.
- **trade-desk**: Answer questions about the user's own Senda records with Senda's read-only tools. Use when the user mentions a shipment, booking, bill of lading, order, invoice or container number, asks where a shipment or container stands or when it is due, which documents are on file, what a tally report counted, or anything else about their company's orders, shipments, containers, documents or tally reports in Senda.

Connect the Senda server when the assistant asks, sign in to Senda, check the company shown and approve. Then ask, for example:

- "Which of my shipments are in transit, and when is each one due?"
- "What documents are on file for my latest shipment?"
- "Suggest HS codes for kiln-dried white oak lumber."

You need a Senda account whose plan includes API access. Setup guides: https://sendaship.com/docs/assistants

## Data

Every question the assistant answers with Senda is a call to https://sendaship.com/api/mcp, signed in with your Senda account. Senda returns only what that call asks for, from the company you signed in to: The connected company's own shipments, orders, containers, document details (type, what it is attached to, whether a file was uploaded, when; never file contents or download links) and tally reports, and Senda's copy of the US Harmonized Tariff Schedule.

What it changes in Senda: Nothing. Every tool is read-only and runs inside a read-only database transaction.

What Senda keeps: For each connection: the name the app gave itself, its return addresses, who approved it, which company, what it may do, when it was connected, expires, was last used and (if ended early) why, a per-minute request count for the rate limit, and one-way hashes of its codes and tokens, never the raw values. One log line per tool call with the tool name, duration, outcome, company and sign-in method, never the arguments or the results.

How long: Sign-in codes: deleted 1 day after they expire. Access and refresh tokens: deleted 7 days after they expire or are revoked. A connection that ended (disconnected or expired after 30 days unused): deleted 90 days after it ended, with its registration. Registrations nobody approved: deleted after a day. Hashed network counts for abuse limits: expire after 24 hours, then deleted. Request logs: kept by the hosting provider for one day.

Who else receives it: Only the assistant provider the customer chooses (OpenAI for ChatGPT and Codex, Anthropic for Claude) receives what each request returns, at the customer's direction and under that provider's own terms. Senda shares nothing from the connection with anyone else beyond the hosting and database providers its privacy policy names, and uses none of it to train AI models.

The skills are instructions only. They run no code, fetch nothing and send nothing anywhere else.

Privacy policy: https://sendaship.com/privacy (assistant connections: https://sendaship.com/privacy#ai-assistants). Terms: https://sendaship.com/terms. Disconnect at any time in Senda under Settings → Integrations → Connected assistants. Privacy questions: team@sendaship.com.

## Support

https://sendaship.com/contact or team@sendaship.com.
