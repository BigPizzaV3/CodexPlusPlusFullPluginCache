# Unreasonable Eco

![Unreasonable Eco](assets/eco-logo-0.1.2.png)

Find people and ventures in your Unreasonable community, follow up on offers of help, prepare for your program, find people from your programs who share your personal interests, and draft fundraising introduction requests. This plugin connects Claude and OpenAI hosts to the hosted Eco MCP server at **https://unreasonable.eco/mcp**. An authorized Eco account is required; public installation does not grant community or staff access.

## Five workflows

- **Find the right people:** identify relevant community members using returned profile evidence, with clear reasons and source links.
- **Follow up on commitments:** review commitments made to you and draft follow-ups. Record status changes only when you authorize them.
- **Prepare for your program:** build a practical brief from your program schedule, announcements, onboarding steps, and participant context.
- **Find people who share your interests:** find people from your programs who share your personal interests, with closer locations ranked higher.
- **Request fundraising introductions:** review recommended funders and draft individual requests to the returned connectors. Record an introduction request only after you confirm it was sent.

Describe what you need in plain language. For example: “Find people who could help with water conservation,” “Who from my programs shares my personal interests?”, or “Prepare me for my upcoming program.” Your account permissions and current program or fundraising context determine the results available.

## Installation and connection

For Claude Code, add the repository marketplace and install the plugin:

```sh
claude plugin marketplace add unreasonable/eco-mcp
claude plugin install unreasonable-eco@unreasonable
```

Restart your session and use `/mcp` to connect your Eco account through the browser authorization flow. Invoke a workflow explicitly with `/unreasonable-eco:find-people-who-share-your-interests`, or describe your task.

For supported OpenAI clients, add the repository marketplace with `codex plugin marketplace add unreasonable/eco-mcp`, then install Unreasonable Eco from the Unreasonable source in the client's plugin directory. A versioned ZIP is also available from the repository's GitHub Releases for supported upload flows. Marketplace availability varies by host. A custom MCP connection alone provides tools but does not install the bundled skills.

## What runs and what data is sent

The plugin loads workflow instructions and connects to the Eco MCP endpoint. It contains no executable scripts, hooks, package launchers, or background jobs. Tool requests send search terms, record IDs, or explicitly authorized updates to Eco. Returned records are processed by your chosen AI host and limited by your Eco account's visibility. OAuth credentials are managed by the host and are not bundled with the plugin.

Read-only searches do not update records. Some Eco tools support requested updates; the skills keep drafts, sent requests, follow-ups, and fulfilled commitments distinct. Drafting an email does not send it. These workflows do not automatically contact people, submit forms, sign agreements, or make payments. Staff tools remain governed by Eco permissions. Following returned website, deck, signing, or download links can contact those destinations; the workflows do not automatically fetch them.

## Support and policies

- [Support](https://unreasonable.eco/support)
- [Privacy policy](https://unreasonable.eco/privacy)
- [Terms of service](https://unreasonable.eco/terms)
- Technical contact: tech@unreasonablegroup.com

The plugin files are MIT licensed. The license does not grant rights to Unreasonable's trademarks, hosted service, or community data. Eco access remains subject to its terms and your account permissions.
