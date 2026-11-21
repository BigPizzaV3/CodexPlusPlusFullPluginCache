# HeyMark plugin

![HeyMark](assets/logo.svg)

[HeyMark](https://heymark.ai) is where community managers, agencies and creators run the social media of one or many brands. This plugin connects your AI assistant to your HeyMark account and adds skills for the work you do every week:

| Skill | What it does |
| --- | --- |
| `weekly-content-plan` | Plans a week of content from your brand profile, recent results and what is already scheduled, then saves the approved ideas in HeyMark. |
| `inbox-triage` | Ranks unread messages, escalations and recent comments, drafts replies in your brand voice, and sends only the replies you approve. |
| `performance-review` | Reviews post performance for a period, explains what worked, and suggests three prioritized actions. |
| `backlog-to-schedule` | Checks what your ideas and drafts are missing, proposes publishing times, and schedules the posts you approve. |

The skills work in English and Spanish.

## How to use it

1. Install the plugin from your assistant's plugin directory, or add the MCP server `https://mcp.heymark.ai` as a custom connector.
2. Sign in with your HeyMark account when asked. Sign-in uses OAuth; the plugin never sees your password.
3. Ask in plain language, for example "Plan next week's content for my brand" or "¿Qué comentarios tengo que responder hoy?".

You need a HeyMark account with at least one brand. Scheduling and publishing also need a connected social account.

## What data it sends

The plugin contains only instructions (Markdown) and configuration (JSON). It runs no code on your machine.

It connects to one server, `https://mcp.heymark.ai`, operated by HeyMark Inc. Through that server your assistant reads and changes the HeyMark brands your account can access: brand profile, posts and drafts, scheduled publications, inbox messages, comments and analytics. What you type in the conversation is processed by your AI assistant's provider; HeyMark receives only the tool calls the assistant makes.

Public actions, such as replying to a comment or a direct message, hiding a comment, publishing or deleting, show a preview first and run only after you approve it.

- Privacy policy: https://heymark.ai/privacy-policy/
- Terms of service: https://heymark.ai/terms-of-service/
- Support: soporte@heymark.ai

## Repository layout

- `.claude-plugin/plugin.json` and `.mcp.json`: manifest and MCP server for the Claude directory and Claude Code.
- `plugin.json` and `mcp.json`: Agent Plugins manifest and MCP server for the OpenAI directory (ChatGPT and Codex).
- `skills/`: one folder per skill, shared by both directories.
- `assets/`: logos.

Skill text must stay provider neutral (say "the model", never name an AI assistant or its maker), use no em dashes, and use neutral Spanish tuteo with "publicación". CI checks the first two rules, the manifests and secrets on every pull request.

Tool and argument names in the skills come from the HeyMark MCP server. Check them against its `tools/list` before editing a skill, and bump `version` in both manifests with every release.

## License

MIT. See [LICENSE](LICENSE).
