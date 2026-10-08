# Prompt for `@plugin-creator`

Create and wire a private/local plugin named **Job Outreach Copilot** from the attached `job-outreach-copilot-plugin.zip`.

The ZIP is already authored as a portable Agent Plugins package with root `plugin.json`. Treat that root manifest as canonical.

## Requirements

1. Keep this as a **skills-only plugin** for v0.1.
2. Do **not** add an MCP server, `.app.json`, external apps, hooks, authentication, network dependencies, or custom UI.
3. Preserve the existing skill at `skills/job-outreach-copilot/SKILL.md` and all reference files.
4. Preserve the supplied paper-airplane branding in `assets/icon.svg` and `assets/logo.svg`.
5. Preserve the behavior that the workflow is generic across candidates and that candidate facts must come from the active supplied profile/resume/context.
6. Never hardcode Krishna's personal resume, rates, work authorization, contact information, or job history into the reusable plugin.
7. Preserve the truth-safety rules: never invent experience, skills, metrics, compensation, work authorization, application status, recruiter statements, hiring stages, or contact information.
8. Preserve recruiter-thread continuity: for an ongoing conversation, answer the latest message without repeating previously settled analysis/details.
9. Preserve the opportunity triage framework: Strong / Partial / Weak fit and Proceed / Qualify first / Skip action, without arbitrary percentage scoring.
10. Preserve support for recruiter replies, LinkedIn/email outreach, connection notes, referrals, application follow-ups, interview-stage messages, compensation/work-authorization qualification, and privacy/scam safeguards.
11. If exact LinkedIn/email/product limits or current hiring-platform behavior matter, the skill should verify current official information when available rather than hardcoding stale limits.
12. Do not claim that a message, application, referral, or follow-up was sent unless a tool actually performs it or the user confirms it.

## Local testing setup

Create a **personal marketplace entry** so I can install and test this plugin locally/private first.

If your current scaffold needs `.codex-plugin/plugin.json`, create it only as a compatibility fallback and keep it consistent with the root portable manifest. Do not replace or discard the root `plugin.json`.

## Validate

Before finishing, check:
- root manifest parses and package identity is `job-outreach-copilot`;
- the skill is discovered from `skills/job-outreach-copilot/SKILL.md`;
- all reference paths resolve;
- icon and logo files resolve and are square SVG assets;
- no MCP/app/hook dependency was introduced;
- starter prompts stay within current OpenAI listing limits;
- the plugin activates for job-outreach/recruiter workflows but does not hijack unrelated requests.

Return the created plugin location/URL, marketplace setup, files created or changed, and any validation warnings that still need attention.
