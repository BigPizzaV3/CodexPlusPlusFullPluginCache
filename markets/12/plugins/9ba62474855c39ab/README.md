# Mitsa Mail plugin

This portable plugin connects ChatGPT and Codex to the public Mitsa Mail MCP server at `https://mitsa.email/mcp`.

Version 1.0 exposes Mitsa mail, contacts, calendar, and reminder tools through OAuth protected-resource discovery with dynamic client registration and PKCE. Reading can execute directly after account authorization. AI can prepare emails and replies, but a message is sent only after the account owner reviews and approves its exact recipient, subject, and body in Mitsa. `mail_send` creates that immutable approval request and returns its Mitsa review URL.

## Local test

1. Restart the ChatGPT desktop app so it reloads the repository marketplace.
2. Open the Plugins Directory and select **Mitsa Development**.
3. Install **Mitsa Mail** and complete the Mitsa OAuth flow.
4. Start a new chat and try: “Show my unread Mitsa Mail messages.”

Public distribution requires uploading the plugin ZIP through the OpenAI plugin portal and submitting the same remote MCP server separately through the Claude Connectors Directory. See [SUBMISSION.md](./SUBMISSION.md) for the prepared listing copy and final account-side steps.
