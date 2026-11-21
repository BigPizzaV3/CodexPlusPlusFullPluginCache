# Sulvo public diagnostic scope

This plugin connects to `https://publisher-revenue-audit.sulvo.com/chatgpt/mcp`. Its five tools provide public website diagnostics and a reference checklist. No Sulvo account or email is required to get results in chat.

- Findings are directional public evidence. They do not prove revenue loss or promise a revenue improvement. The publisher can compare them with their own reporting.
- Each of the four diagnostics can also email a PDF when the user explicitly requests delivery to a specified `reportEmail`. Email is used only to fulfill that request. Do not ask for it during an ordinary diagnostic.
- SendGrid processes the recipient and PDF to deliver the requested message. Open and click tracking are disabled. Provider acceptance does not prove inbox delivery.
- The public integration does not create admin or CRM lead records and does not use the hostname, recipient, inputs, or report for sales outreach or marketing. There is no signup step in this diagnostic flow.
- Reports are processed in memory. Hashed deduplication and rate-limit records expire within 24 hours. They are not a contact list. Do not promise that an email provider or recipient deletes its delivered copy when those records expire.
- Do not transmit conversation history, credentials, or unrelated personal information. Optional diagnostic metrics are limited to `fillRate` and `dashboardViewabilityRate`; output and scan controls affect the requested report.
- Private account reports, onboarding, and ad-unit changes use the separate authenticated `/mcp` endpoint. They are not exposed by this plugin. Documentation: https://sulvo.com/developers.
- Privacy information: https://sulvo.com/privacy. Support: https://sulvo.com/contact.

These are the MCP 0.4.0 contract requirements. Confirm deployment and the published privacy wording before resubmitting plugin 0.5.0. Do not use older sales-lead instructions or demos for this release.
