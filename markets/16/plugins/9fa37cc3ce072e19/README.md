# Sitebulb Cloud

The official Sitebulb plugin for Sitebulb Cloud. It gives your AI assistant five technical-SEO skills and a read-only connection to the audits in your Sitebulb Cloud account. Ask what to fix first, what changed since the last crawl, or for a client-ready audit document, dev tickets or a post-release check. Every answer comes from your real crawl data.

For audits in Sitebulb Desktop, install the `sitebulb-desktop` plugin instead.

## Install

Install Sitebulb Cloud from the plugin directory in ChatGPT or Codex. If you installed the `sitebulb` plugin from the public repository, uninstall it first, because it has the same five skills.

For other assistants, install the `sitebulb` plugin from the public repository at https://github.com/sitebulb/sitebulb-plugin.

## Connection

The plugin declares one remote MCP server, `https://cloud.mcp.sitebulb.com/mcp`. When you first use it, your assistant asks you to sign in to your Sitebulb account with OAuth. The connection is read-only: the skills can read your audits, but they cannot start crawls or change settings.

## Skills

| Skill | What it does |
|---|---|
| `sitebulb-what-to-fix-first` | The 3–5 issue clusters most worth fixing for your business, impact against effort |
| `sitebulb-what-changed` | The change story between your two most recent audits |
| `sitebulb-technical-seo-audit` | A focused client-facing audit document (.docx working draft, 5–10 issues) |
| `sitebulb-dev-handoff` | Dev-ready tickets from audit findings, sent to your connected PM tool |
| `sitebulb-release-check` | Your configured post-release watch-list check with thresholds and alerts |

## What the plugin runs and sends

- The skills run small Python scripts that use only the standard library: an effort scorer and a Word document builder. The scripts make no network requests.
- Your assistant reads audit data from the MCP server above. Your assistant also sends prompts, and the audit data that the skills read, to its model provider.
- `sitebulb-dev-handoff` and `sitebulb-release-check` can write to a project-management or messaging tool, but only one that you connected yourself.

Privacy and security details: [PRIVACY.md](https://github.com/sitebulb/sitebulb-plugin/blob/main/PRIVACY.md) and [SECURITY.md](https://github.com/sitebulb/sitebulb-plugin/blob/main/SECURITY.md). The Sitebulb privacy policy is at https://sitebulb.com/policies/cookie-and-privacy-policy/.

## Support

For help, go to https://sitebulb.com/support/ or email support@sitebulb.com.

## Licence

MIT. See [LICENSE](LICENSE). © Sitebulb Ltd.
