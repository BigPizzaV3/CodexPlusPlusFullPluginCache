# Submission Notes

Use these notes while completing the OpenAI plugin dashboard review form.

## Plugin Identity

- Package name: `pretture-erp-ai`
- Display name: `Pretture ERP AI`
- Category: `Data & Analytics`
- MCP server name: `pretture-erp`
- MCP URL: `https://mcp.pretture.com/v1/mcp`
- Demo recording URL: `https://www.youtube.com/watch?v=Az2PGjGYz28`

## Privacy Policy Review

OpenAI's plugin guidelines require the published privacy policy to clearly explain at least:

- Categories of personal data collected.
- Purposes for using that data.
- Categories of recipients or processors.
- Data retention timelines.
- User controls for access, correction, deletion, or withdrawal.

The current manifest points to `https://pretture.com/pluginprivacy`. Make sure that page explicitly covers the ChatGPT/MCP plugin, ERP credentials/tokens, query content, activity logs, OAuth/session data, retention, processors, and contact controls before final submission.

## Reviewer Setup

Prepare a dedicated test account with sample ERP data. Do not use a real user account.

Provide reviewers with:

- Login URL for the ChatGPT connection flow.
- Test ERP JWT or sign-in instructions, if your enrollment flow requires it.
- A short description of sample data available in the test account.
- Any expected enabled API registry entries.

Enter reviewer credentials only in the OpenAI dashboard's Review details form. Do not include credentials in `plugin.json`, `mcp.json`, README files, notes, or any other file in the ZIP.

## Required Positive Test Cases

The manifest includes five positive cases:

1. Summarize sales for a completed period.
2. Group sales by month.
3. Break down sales by customer.
4. Filter sales analytics.
5. Respect authentication and credential boundaries.

## Required Negative Test Cases

The manifest includes three negative cases:

1. Unsupported payment action.
2. Request for secrets.
3. Unsupported destructive action.

## Before Final Submission

- Confirm the MCP server is publicly reachable over HTTPS.
- Confirm OAuth enrollment works from ChatGPT.
- Confirm `get_sales_analytics` is visible after connection.
- Confirm the demo video URL is accessible to reviewers.
- Confirm all listing URLs are live and match your production legal/support pages.
