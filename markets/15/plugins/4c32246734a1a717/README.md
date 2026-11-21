# ISMS Copilot

The compliance specialist your AI calls.

ISMS Copilot is a governance, risk and compliance (GRC) assistant. Connect your ISMS Copilot account and Claude can hand it the compliance part of your work: framework interpretation, policy drafting, control mapping, gap analysis, Statement of Applicability justifications, risk register entries and audit preparation for ISO 27001, ISO 27701, ISO 42001, SOC 2, GDPR, NIS 2, DORA, the EU AI Act, the Cyber Resilience Act, NIST SP 800-171 and CMMC, HIPAA and PCI DSS.

What the connector does:

- Starts and continues conversations with the ISMS Copilot specialist, one conversation per deliverable, saved to your ISMS Copilot account.
- Reads your plan name, workspaces, document names and processing status, memories, company profile and client companies, so answers fit your organization. When you ask the specialist in a workspace, it may use that workspace's processed documents as context for its answer.
- Creates workspaces, adds or updates memories and updates your company profile when you ask. If you advise several organizations, it can also create, update, link and delete client companies (one profile per client); deleting a company unlinks its workspaces and never deletes workspace data.

What it does not do: it does not read Claude's chat history or files you upload to Claude, no tool returns a stored file as such, and it has no payment, checkout or API key tools.

Sign in with your ISMS Copilot account; new users can create one on the sign-in page. ISMS Copilot uses AI. Answers are general compliance information, not legal advice: have a qualified professional review legal or regulatory interpretations before you rely on or share them. ISMS Copilot is made by Better ISMS and is not affiliated with Microsoft or GitHub.

## What this plugin contains

- One remote MCP server, `ismscopilot`, at `https://account.ismscopilot.com/v1/account/mcp` (Streamable HTTP). The first time a tool runs, your client opens the ISMS Copilot sign-in and consent page (OAuth 2.1). The plugin stores no credentials and asks for no API key.
- One skill, `get-started`, that tells the assistant what to hand to the specialist and what stays on your machine.

It has no hooks, scripts, commands or local code. It sends data only to the ISMS Copilot server above: whatever the assistant puts into a tool call (questions for the specialist, memories, company context, workspace and document requests, including any excerpt it chooses to quote).

## Install

### Claude Code

```bash
claude plugin marketplace add better-isms/ismscopilot-plugin
claude plugin install ismscopilot@ismscopilot
```

Then run `/mcp`, pick `ismscopilot` and sign in. Or add the server on its own:

```bash
claude mcp add --transport http ismscopilot https://account.ismscopilot.com/v1/account/mcp
```

### Gemini CLI

```bash
gemini extensions install https://github.com/better-isms/ismscopilot-plugin
```

Restart Gemini CLI, then run `/mcp auth ismscopilot` to sign in.

### Other MCP clients

Setup guide: https://docs.ismscopilot.com/docs/agents/connect-any-mcp-client

## Links

- Website: https://www.ismscopilot.com/mcp?ref=claude-code-plugins
- Privacy policy: https://trust.ismscopilot.com/en/privacy-policy
- Support: support@ismscopilot.com

## Package layout (maintainers)

- `.claude-plugin/plugin.json`: Claude Code manifest (it also carries the `extensions.com.openai` block, which Claude Code ignores).
- `.cursor-plugin/plugin.json`: Cursor manifest (cursor.directory); points Cursor at `.mcp.json`.
- `.claude-plugin/marketplace.json`: one-plugin Claude Code marketplace, so the repo installs with `claude plugin marketplace add`.
- `.mcp.json`: the MCP server entry for Claude Code (type `http`).
- `gemini-extension.json` and `GEMINI.md`: Gemini CLI extension manifest and its context file.
- `plugin.json` and `mcp.json`: Agent Plugins manifest and server entry for the ChatGPT and Codex plugins directory.
- `skills/get-started/SKILL.md`: onboarding skill.
- `assets/logo.png`: listing icon.

Releases use merge-commit PRs to `main`. Raise `version` in the manifests with every release.

## License

MIT. See [LICENSE](LICENSE).
