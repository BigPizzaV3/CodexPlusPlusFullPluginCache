# Customer Alliance

Connects your AI assistant to Customer Alliance, so you can ask about your properties' guest reviews, ratings, topics, benchmarks, competitors and survey results, and draft review replies.

## Connecting

The plugin connects to `https://app.customer-alliance.com/mcp`. The first time you use it, you sign in to Customer Alliance with your usual account (password or Google) and approve the connection. No API key is needed.

Requirement: an account admin has switched on AI assistant connections under Settings > API & Webhooks > MCP.

## What the assistant can do

- **Read** (`read` scope): properties, reviews, review statistics, topics, the Customer Alliance benchmark, competitors, surveys and survey results, reply guidelines and recommendations. It sees only the properties your user can see in the dashboard.
- **Draft** (`drafts` scope): save a reply draft or add an internal note on a review. Nothing is published: you review and send the reply from the Customer Alliance dashboard.

## Disconnecting

Remove the connection in your assistant, or revoke it in Customer Alliance under Settings > API & Webhooks > MCP. An admin can revoke any connection in the account.

## Support

https://support.customer-alliance.com/v2-knowledge-base
