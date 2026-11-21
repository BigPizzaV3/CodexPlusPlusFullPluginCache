# Nobl9

Nobl9 is the reliability platform, built on service level objectives
(SLOs) and error budgets. It tells you whether the services your
customers depend on are working, how much room you have before they
notice a problem, and what to fix first.

With this plugin you can ask ChatGPT and Codex those questions in plain
words and get answers from your own live Nobl9 data.

## What you need

- A Nobl9 account. Sign up at https://www.nobl9.com if you do not have one.
- Access to the organization you want to work with.

## Connecting

On first use the plugin opens the Nobl9 sign-in page in your browser.
Sign in with your own Nobl9 account and approve the access request. No
API keys are needed.

The assistant sees only what you can see. If you belong to more than one
organization, it asks which one to use.

If your company runs Nobl9 on a dedicated instance (for example
`us1.nobl9.com`), connect to `https://<instance>/api/mcp` instead of the
default `https://app.nobl9.com/api/mcp`.

## What you can ask

- "Which of my services are closest to failing their customers right now?"
- "Explain the most recent alert on my checkout service and whether it was worth the page."
- "Draft a 99.9% availability target for my payments service and show me before you apply it."
- "Show me the error rate for the payments service from the Prometheus data source over the last seven days."

Asking questions never changes anything. When you ask it to set up or
change a target or an alert, it drafts the change, validates it against
your organization, and shows you the full definition before applying.

## Data handling

Data leaves the assistant only through calls to the Nobl9 MCP server,
which acts on your organization under your own identity. See the
[Nobl9 privacy policy](https://www.nobl9.com/privacy-policy) and
[terms of use](https://www.nobl9.com/terms-of-use).

## Help

- Documentation: https://docs.nobl9.com/tools-and-utilities/mcp-server
- Support: https://www.nobl9.com/contact/support
