# Aevral for coding agents

Aevral is an AI security reviewer for GitHub pull requests. Built by Better
ISMS, the company behind ISMS Copilot, in Paris, France.

**Catch security flaws before you merge.** Pull request reviews look for
access control, business logic, SQL and command injection, XSS, SSRF, path
traversal, unsafe deserialization, token and session flaws, and
LLM-integration risks, with a suggested fix you apply. Reviews are advisory
and never block a merge. The optional whole-repo scan reads authorization,
IDOR, and business-logic access control only. Not secret, dependency, or
memory-corruption scanning, and not a general SAST. GitHub only.

This plugin does **not** review code on your machine. It is a setup skill for
the [Aevral GitHub App](https://github.com/apps/aevral). After the App is
installed, the next pull request can already be reviewed, including before
anyone signs in to the console. MCP is not live. Do not invent an MCP server.

## Install

### Claude Code

```
/plugin marketplace add better-isms/aevral-plugin
/plugin install aevral@aevral-plugins
```

Then run `/aevral:review`.

### Codex CLI

```
codex plugin marketplace add better-isms/aevral-plugin
```

Then `/plugins` and install `aevral`.

### Cursor

Load the repo as an Agent Plugin (root `plugin.json`) from Customize, or install
from the Cursor Marketplace once listed. Local test: symlink this repo into
`~/.cursor/plugins/local/aevral`.

### GitHub Copilot CLI

```
copilot plugin marketplace add better-isms/aevral-plugin
copilot plugin install aevral@aevral-plugins
```

### Grok

```
grok plugin marketplace add better-isms/aevral-plugin
grok plugin install aevral --trust
```

### Gemini CLI

```
gemini extensions install https://github.com/better-isms/aevral-plugin
```

Then ask the agent to set up Aevral. Gemini does not expose `/aevral:review`.

### skills.sh (optional)

```
npx skills add better-isms/aevral-plugin
```

That installer keys off the skill YAML name `review`. If another skill with
that name is already installed the same way, they share that destination.
Prefer the marketplace commands above when more than one review plugin is in
use.

## What the human clicks

Same GitHub user for both.

1. Tagged console login (so the listing source is stored), for example
   https://app.aevral.com/login?ref=claude-plugin
2. GitHub App: https://github.com/apps/aevral

Reviews can start on the next pull request after the App install. Signing in
with GitHub connects the install; the console is for reports, turning reviews
off, and an optional whole-repo scan.

## Pricing

- **Public repositories:** free up to 500 reviews per organization per month.
- **Private repositories:** free up to 25 per month, plus a 14-day trial (up
  to 500 private reviews) when you sign in with GitHub. No card.

Priced per organization, never per seat.

Paid plans: https://aevral.com/pricing

## Links

- Website: https://aevral.com
- Docs: https://docs.aevral.com
- Setup with your agent: https://docs.aevral.com/docs/setup-with-an-agent
- Official agent prompt: https://docs.aevral.com/agent-setup/prompt.md
- Privacy: https://trust.ismscopilot.com/en/privacy-policy
- Terms: https://trust.ismscopilot.com/en/terms
- Support: support@ismscopilot.com

## License

MIT. See [LICENSE](./LICENSE).
