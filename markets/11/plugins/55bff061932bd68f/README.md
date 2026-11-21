# Employed by Guaq AI: agent plugin

Live job search for AI agents. [Employed by Guaq AI](https://jobs.guaqai.me) indexes roles verified on about 5,000 real employer applicant-tracking boards (Greenhouse, Lever, Workday, Ashby, SmartRecruiters and more). This plugin connects your agent to it, so you can ask for jobs in plain language and get live roles with the employer's own apply link.

<img src="assets/icon-512.png" alt="Employed by Guaq AI logo" width="96" height="96">

## What you get

- **A remote MCP connector** at `https://jobs.guaqai.me/mcp`. Search tools: `search_jobs`, `count_jobs`, `get_job`, `list_companies`, `company_profile`, `market_signal`, `api_meta` (plus `export_jobs` on the local `npx` server). Your own account: `get_my_profile`, `update_my_profile`, `profile_options`, `get_my_feed`, `list_my_applications`, `track_job`, `untrack_job`, `get_my_alerts`, `follow_company`, `unfollow_company`, `set_email_alerts`, so you can set up your profile from a CV, read your ranked feed and track applications without leaving the chat.
- **Five skills** that teach the agent how to use it well:

  | Skill | Use it to |
  |---|---|
  | `employed-jobs` | Search with the exact filter vocabulary (domain, seniority, location, work mode, tech, visa signal) |
  | `job-search-from-resume` | Turn a resume or background into a ranked shortlist |
  | `employer-research` | See what one or more employers hire for right now |
  | `hiring-market-brief` | Size demand for a skill, role or city, with limits stated |
  | `application-tracker` | Keep a Markdown or CSV tracker you own |

- **Two agents** (`job-search-agent`, `employer-research-agent`) and **three slash commands** (`/employed:find-jobs`, `/employed:company`, `/employed:market`) on platforms that support them.
- **Interactive results UI** (MCP Apps and the ChatGPT Apps SDK) served by the remote server where the host renders it.
- No hooks. Nothing in this bundle runs code on your machine.

## Install

| Platform | How |
|---|---|
| Claude Code | `/plugin marketplace add Guaq-AI/employed-plugins` then `/plugin install employed@employed-marketplace`, then `/mcp` to sign in |
| Claude.ai, Claude Desktop | Add a custom connector with URL `https://jobs.guaqai.me/mcp` |
| ChatGPT, Codex | Add the MCP URL as a custom connector, or install the plugin from the directory once listed |
| GitHub Copilot CLI | `copilot plugin marketplace add Guaq-AI/employed-plugins` then `copilot plugin install employed@employed-marketplace` |
| Qwen Code | `qwen extensions install https://github.com/Guaq-AI/employed-plugins:employed` |
| Gemini CLI | `gemini extensions install https://github.com/Guaq-AI/employed-plugins` |
| Antigravity | `agy plugin install https://github.com/Guaq-AI/employed-plugins` |
| Cursor, Kiro, Devin, Qoder, ZCode, MiniMax, Hermes, OpenClaw, Cline, DeepSeek Harness, Mistral Vibe, OpenHands, Microsoft 365 Copilot | See [docs/INSTALL.md](docs/INSTALL.md) |

Every route signs in with an Employed account (OAuth in the browser). API keys from your [profile page](https://jobs.guaqai.me/profile) work too, for hosts without OAuth.

## Try it

- "Find entry-level backend roles in India that likely sponsor a visa."
- "Which companies are hiring Rust engineers remotely?"
- "Is Stripe hiring in London right now, and for what?"
- "Here is my resume. What should I apply to?"

## Data this plugin sends

When your agent calls a tool, the connector sends **the search filters and ids the agent chose** (for example `role_type=new_grad`, `location_scope=india`, a company name, a posting id) and your sign-in token to `https://jobs.guaqai.me`, plus, when you ask it to update your profile or tracker, the profile fields or status you agreed to. It does not send your resume file, conversation, or anything else from your machine. Skills are plain instructions; they contain no code. The optional `npx` launcher described in [docs/INSTALL.md](docs/INSTALL.md) runs the open-source `employed-mcp` package, pinned to an exact version, and talks to the same service.

Read the [privacy policy](https://jobs.guaqai.me/privacy-policy) and [terms](https://jobs.guaqai.me/terms-of-service). Support: <https://jobs.guaqai.me/support> or support@guaqai.me.

## Honest by design

- Every role links to the employer's own apply page. The plugin never applies for you or contacts anyone.
- Visa sponsorship marked `likely` is an inference from posting text and employer history, not a guarantee. `stated` means the posting says so.
- Counts describe postings live on employer boards, not total headcount or hires.
- Posting text is third-party content. The skills tell the agent to treat it as data, never as instructions.

## Layout

```
.claude-plugin/        Claude Code plugin and marketplace manifests
plugin.json, mcp.json  Agent Plugins 1.0.0 (Copilot CLI, Cursor, Kiro, Codex, Hermes, Qwen)
.cursor-plugin/ .qoder-plugin/ .zcode-plugin/ .devin-plugin/ .minimax-plugin/ .plugin/   per-platform manifests
.dsh-plugin/           DeepSeek Harness bundle
skills/ agents/ commands/   shared content
assets/ screenshots/   icons and store screenshots
mcp-registry/          server.json for the official MCP Registry
docs/                  install guide and marketplace research
```

## Version, license, changes

Version 1.1.0. MIT licensed, see [LICENSE](LICENSE). Release notes in [CHANGELOG.md](CHANGELOG.md). Report security issues as described in [SECURITY.md](SECURITY.md).
