# Avalara

Review and manage Avalara transactions, liabilities, exemptions, nexus items, returns, deadlines, and reports. The plugin works through the Avalara Product Portal and the permissions of your signed-in account.

The skill loads focused guidance for AvaTax transactions and imports, nexus, reports,
exemption certificates, and Managed Returns as the task needs it. It helps investigate
issues such as missing tax, certificate mismatches, stale reports, and filing variances.

This plugin is built and maintained by OpenAI. It is powered by computer use, and is not an Avalara-provided API or MCP integration.

## Supported Flows

Live Avalara sign-in, review, and account changes require local browser access in ChatGPT Desktop or desktop Codex. Use desktop-local Work; web, mobile, and cloud-backed tasks are not supported for live account access. A Work handoff is usable only when it leads to a supported desktop-local session. Explanations and analysis based on material you provide can stay in Chat.

| Execution environment | Browser |
| --- | --- |
| Desktop Codex | In-app browser (IAB) |
| Desktop-local Work | In-app browser (IAB) |

The local browser must be available and permitted by your organization's authentication, VPN, device, and site policies. Unsupported hosts must report the limitation instead of substituting a cloud browser or another transport.

## Try It

- Review recent Avalara transactions and flag unusual tax calculations.
- Summarize liabilities, exemptions, and nexus items that need attention.
- Open my latest Avalara report and explain the key changes.
- Update the Avalara transaction I select and show me the result.
- Add the exemption certificate I provide to the customer I select.
- Generate a liability report for the company and filing period I specify.
- Investigate why this customer's valid exemption certificate did not apply.
- Review my transaction import's company and process codes before uploading it.

Sign in through the browser when prompted, then ask the assistant to continue. Select the correct company, product, live or sandbox environment, period, and jurisdiction before account data is read. Do not put passwords, one-time codes, recovery codes, or session details in chat.

Use [Avalara's product sign-in page](https://www.avalara.com/us/en/signin.html) for the
appropriate product. AvaTax has separate production and sandbox accounts; the assistant
preserves your selected account and environment and verifies the signed-in context.

You can request record updates, imports, certificate or customer changes, report generation, and account configuration supported by your Avalara product and role. The assistant verifies the target and result and preserves unrelated settings. Reviewing or drafting does not authorize saving, filing, or payment.

Consequential actions, including committing or voiding transactions, changing tax or filing settings, approving returns, and scheduling or making payments, require explicit approval of the affected records and final details. Approval of a liability worksheet can also authorize filing and remittance. Personal attestations and funding authorizations are handed to you in the browser. Some operations, such as amendments or backfiling, may require Avalara support.

Imports verify company codes inside the file as well as the selected company, operation
codes, document identifiers, and any automatic commit behavior. Certificate handling
distinguishes pause, invalidation, expiry, and deletion. Returns workflows check current
deadlines and automation because leaving a return unapproved may not stop filing.

The assistant reports the status actually shown by Avalara and avoids repeating actions whose outcome is uncertain. It does not provide legal or tax advice or certify calculations and filings; use your authorized tax owner for those determinations.

## Brand Asset

The packaged icon is Avalara's A-Check vector mark in the approved Avalara Orange (`#FF6600`) and blue (`#059BD2`). The partner-provided source is [Avalara Brand Assets](https://brandfolder.com/avalara-brand-assets/#!asset/6c833w9h2f3q5kpxjzcxhwf); Avalara also serves the same A-Check mark from its [official website](https://www.avalara.com/etc.clientlibs/avalara-core-components/clientlibs/clientlib-site/resources/images/a-check.svg). Keep the supplied geometry, proportions, and colors unchanged.
