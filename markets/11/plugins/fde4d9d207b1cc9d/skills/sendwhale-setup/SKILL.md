---
name: sendwhale-setup
description: Audit an existing app's email triggers, create or reuse SendWhale drafts and wire authorized transactional backend sends without duplicate delivery.
---

Inspect the app before asking the user to describe its stack. Find existing providers, templates, event triggers, queues, scheduled jobs, campaigns, webhooks and notification services. Preserve working triggers and recipient rules.

Reuse a connected SendWhale MCP and read the approved brand. Continue the local audit while browser authorization is pending. Resolve the matching workspace; ask only if more than one is plausible. Read current drafts before creating missing ones. Ground each draft in code evidence: trigger, recipient, variables, subject, CTA and timing. Create a related series in one save and retain every returned campaign ID and review link.

Hosted MCP saves drafts for review; it cannot deliver or schedule. Product-triggered transactional delivery uses the server-side Node SDK's `SendWhaleTransactional` or the existing `transactional-send` HTTP endpoint. Its separate purpose-bound `email:send` key is never a hosted MCP token. Read the packaged `sendwhale-public-api` contracts before wiring. Send HTML/text explicitly; the endpoint does not expand campaign IDs or template variables.

Integrate into the app's real backend service or queue. Keep stable event-based idempotency keys and logs of returned operation IDs/status. Add a dry-run test that checks the correct content, recipient and key without reaching an inbox. Obtain the user's approval for a concrete test or production send when it is not already authorized. Preparing drafts and wiring reviewed local code do not themselves authorize customer delivery or migration of traffic.

Treat a user-pasted “use this SendWhale email in my app” brief as the task plus identifiers. Resolve any supplied campaign or conversation ID inside the approved workspace before selecting content. Use the saved HTML returned by `get_campaign`; explicitly substitute and escape the app's real variables on the backend. A campaign ID does not become a transactional template ID. Keep related trigger-to-draft mappings together, including their recipient rule, sender and queue timing. The app owns lifecycle timers; saving a series creates no enrollment or delivery schedule.

For frontend-only apps, complete the audit and drafts, then identify the backend prerequisite. Never put a delivery credential in browser code. Use native SendWhale campaign approval for marketing audiences; retain subscribed status, suppression checks and real postal footer details.

Report the email touchpoints, brand used, drafts reused/created, changed files, dry-run results, sender status and remaining prerequisites. Do not claim an unsupported endpoint or unpublished npm package exists.
