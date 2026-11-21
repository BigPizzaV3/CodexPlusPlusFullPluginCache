# SalesBlink OpenAI Plugin Package

This directory contains the distributable plugin metadata for the hosted SalesBlink MCP server. It intentionally does not contain application source code, dependencies, credentials, or environment files.

## Upload

1. Confirm that `https://mcp.salesblink.io/mcp` is publicly reachable over HTTPS and that OAuth login works.
2. Create a ZIP whose root contains `plugin.json`, `mcp.json`, and `assets/`.
3. In the OpenAI Platform Plugins dashboard, select **Upload new or existing plugin** and use the **With MCP** flow to upload the ZIP.
4. Connect the `salesblink` MCP server, host the domain-verification token supplied by the dashboard at `/.well-known/openai-apps-challenge`, and complete the server scan.
5. Before submitting for review, add the required reviewer test account details in the dashboard and add a public video walkthrough URL to `extensions.com.openai.review.demo_recording_url` in `plugin.json`.

## Reviewer fixture checklist

Create a dedicated review workspace, with no MFA, magic-link, email-code, or private-network dependency. Its sample data must remain available for the full review period:

- a sender named `Review Sender`
- a contact list named `Review List` with safe sample contacts
- an email template named `Review Template`
- an inbox thread with the unique subject `Review reply test`, addressed only to a controlled test mailbox
- a paused sequence named `Review Q4 outreach` with delivery, open, click, and reply statistics available

The review cases intentionally discover these fixtures by name before they call ID-based tools. Do not rename or remove them between resubmissions.

The included five positive and three negative review cases are adapted from `../chatgpt-app-submission.json`.
