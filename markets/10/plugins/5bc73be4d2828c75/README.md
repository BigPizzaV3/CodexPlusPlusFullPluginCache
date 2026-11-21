<p align="center"><a href="https://vitae.ai"><img src="assets/logo.png" width="96" height="96" alt="Vitae.ai" /></a></p>

# Vitae for AI assistants

Find candidates, inspect jobs and pipelines, and prepare recruiting work from your assistant.

One **Vitae** plugin bundles the hosted MCP connector, app usage and onboarding guidance, and nine recruiting workflows. Install it once to work with Vitae and prepare recruiting artifacts. This repository is the canonical source for all ten skills; no second plugin or runtime download of another repository is required.

## Connect

```text
https://mcp.vitae.ai/mcp
```

Use Streamable HTTP and complete Vitae OAuth in your client. A Vitae account and access to the intended workspace are required. Public discovery works without signing in; accessing recruiting records does not.

## Install

### Claude Code

```text
/plugin marketplace add vitaedotai/agent
/plugin install vitae@vitae
```

Open `/mcp`, select Vitae, and finish OAuth. MCP-only alternative:

```bash
claude mcp add --transport http vitae --scope user https://mcp.vitae.ai/mcp
```

### Codex

```bash
codex plugin marketplace add vitaedotai/agent
```

In a supported Codex client, refresh the plugin sources and install Vitae. Registering the source alone does not install the package. MCP-only alternative:

```bash
codex mcp add vitae --url https://mcp.vitae.ai/mcp
codex mcp login vitae
```

### Cursor

Add the remote server in Cursor's MCP settings:

```json
{"mcpServers":{"vitae":{"url":"https://mcp.vitae.ai/mcp"}}}
```

This connects tools only. Install selected skills with the Skills CLI below, or install the native plugin to get all ten. This repository also includes a native Cursor plugin manifest; it does not imply a public Cursor marketplace listing.

### Grok

For Grok chat, add a custom connector with the MCP URL and authenticate. Grok Build packaging is in `.grok-plugin/`, with all ten skills and the hosted connector. Chat connectors and Build plugins are separate installation surfaces. No public Grok marketplace listing is claimed.

### Gemini CLI

```bash
gemini extensions install https://github.com/vitaedotai/agent
```

Complete OAuth when prompted. The extension loads `GEMINI.md`, which routes Vitae tasks to the bundled skills.

### Individual skills

```bash
bunx skills add vitaedotai/agent --skill vitae
bunx skills add vitaedotai/agent --skill candidate-outreach
bunx skills add vitaedotai/agent --list
```

The Skills CLI installs instructions only. Choose the app skill, a recruiting workflow, or all ten. Recruiting drafts can use supplied context without an account. Configure the connector and complete OAuth when you need connected Vitae actions.

## Included skills

| Skill | Use it to |
| --- | --- |
| [vitae](skills/vitae/SKILL.md) | Operate Vitae through its hosted MCP connector: find ATS candidates and jobs, inspect pipelines, prepare drafts, and handle pending approvals. Use for work in a Vitae workspace, not generic recruiting copywriting. |
| [job-intake](skills/job-intake/SKILL.md) | Turn a recruiting vacancy or hiring-manager conversation into an agreed job brief, with requirements, constraints, and open questions. |
| [hiring-scorecard](skills/hiring-scorecard/SKILL.md) | Build a job-related evaluation scorecard with evidence criteria and anchored ratings before screening or interviews. |
| [sourcing-strategy](skills/sourcing-strategy/SKILL.md) | Translate an agreed hiring brief into candidate search hypotheses, search queries, channels, and a measurable sourcing plan. |
| [candidate-screening](skills/candidate-screening/SKILL.md) | Compare candidate evidence with an agreed role scorecard, identify missing information, and prepare a recruiter review without making automatic hiring decisions. |
| [candidate-outreach](skills/candidate-outreach/SKILL.md) | Write personalized initial recruiting invitations and follow-ups using verified role and candidate facts, with clear calls to action and respectful stop conditions. |
| [interview-invitation](skills/interview-invitation/SKILL.md) | Draft a clear interview invitation or rescheduling message with confirmed stage, time zone, duration, format, participants, and preparation. |
| [interview-kit](skills/interview-kit/SKILL.md) | Prepare a structured interview plan with job-related questions, follow-up probes, evidence notes, and calibrated assessment guidance. |
| [candidate-presentation](skills/candidate-presentation/SKILL.md) | Create a factual candidate shortlist or client presentation from authorized candidate records, role criteria, and screening or interview evidence. |
| [recruitment-workflow](skills/recruitment-workflow/SKILL.md) | Coordinate a recruitment assignment from intake to candidate presentation, select the appropriate recruiter skill, and track evidence, owners, approvals, and next actions. |

Vitae assistant skills are the workflows above. The MCP tool `search_skills` looks up candidate/job competencies such as TypeScript; it does not list plugin skills. Internal repository engineering skills are separate from this recruiting bundle.

## Try it

- “Show my open jobs in Vitae.”
- “Find this candidate in my existing ATS and summarize the evidence relevant to this job.”
- “Prepare a candidate presentation for this role, including missing information.”
- “Draft an outreach email from these candidate and role facts.”
- “Prepare an interview kit using this agreed scorecard.”

Inspect the live tool catalog before taking an action; available tools depend on the deployed server and the caller's permissions. Skills can draft messages and interview plans. Use a verified tool for a connected action only within the user's authorization; otherwise return a precise handoff for the recruiter to complete in Vitae. Business-data changes can return a pending approval instead of executing.

## Verification and privacy

Check the live catalog and verify authenticated workspace status and job-list reads in the intended workspace (`agent_status` and `list_jobs` when listed). Tool listing alone is insufficient. See [compatibility and acceptance](docs/compatibility.md), [data handling](docs/privacy.md), and [the operating skill](skills/vitae/SKILL.md).

No local daemon, hooks, or telemetry are installed by this package. Tool arguments go to Vitae's hosted MCP service and its API. Your AI client also handles the conversation according to its own settings.

## Build a directory upload

Run `python3 scripts/package.py` to build `build/vitae-0.2.4.zip`. It contains the portable manifest, MCP configuration, all ten skills, public reference files, and static assets. It downloads no skill content at installation or runtime. A built package is not directory approval; publisher verification and client acceptance are separate checks.

[Vitae.ai](https://vitae.ai) · [MCP setup](https://mcp.vitae.ai) · [Documentation](https://docs.vitae.ai/reference/mcp) · [Contributing](CONTRIBUTING.md)

[LinkedIn](https://www.linkedin.com/company/vitae-ai) · [X](https://x.com/vitaeai) · [Open Vitae](https://app.vitae.ai)
