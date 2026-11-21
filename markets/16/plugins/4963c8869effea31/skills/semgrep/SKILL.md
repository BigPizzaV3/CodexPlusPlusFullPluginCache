---
name: semgrep
description: Triage and fix Semgrep findings, investigate dependencies and advisories, manage rules and policies, and run scans and Agentic Workflows through the connected hosted Semgrep MCP server. Use when the user asks about their organization's Semgrep findings, issues, projects, scans, supply chain advisories, rules, policies, schedules, automations, or Agentic Workflows, or wants to change any of them. Don't use for general Semgrep CLI or rule-writing questions that don't need the user's platform data.
---

# Work with Semgrep AppSec Platform

Use the tools from this plugin's `semgrep` connection. Begin with
`semgrep_account` to identify its authorized organization. Use the returned
organization id as deploymentId; do not infer it from a repository name or a
different connection. Changing organizations requires reconnecting.

The server's current tools and instructions are authoritative. When an operation
or its contract is unknown, use `discover` with a self-contained task summary;
set `readOnly: true` for investigations. Omit credentials, source code, and raw
finding payloads from discovery arguments. Reuse known contracts rather than
discovering the same tool repeatedly.

Distinguish persistent issues from individual scan findings. Code issues include
SAST and AI SAST; request both issue types when the user asks for all Code
issues. Agentic Workflow issues have a separate PublicIssuesService source.
Inspect each source's filters and pagination before combining results. Keep the
source attached to IDs and totals, and follow result cursors before claiming a
complete list. Use focused response field masks when the server supports them.

Read the existing configuration before making requested changes, and avoid
creating duplicate rules, policies, or schedules. AI detection scans and Agentic
Workflow runs consume Semgrep credits. State the intended action and scope before
executing a requested write. Never run a scan or modify configuration merely to
test the connection.

The server serves conditional instructions at
`skill://semgrep-automations/SKILL.md`. Read that resource and its applicable
references before working on workflow schedules, automations, or detection or
remediation policies. Use the server-rendered version so organization-specific
capabilities are respected.

If `semgrep_run_job` is listed, follow its task contract and polling interval;
otherwise use the listed launch and status operations. Report actual results,
including partial launches and API errors, without claiming work completed just
because it was accepted. Use `semgrep_app_link` for links to supported app pages.

If access is restricted, explain the server's actual reason. An organization
without the MCP entitlement needs eligible access; an eligible organization
without enablement may expose `request_access`. Ask for the user's use case
before calling that tool, and explain that requesting access does not grant it.
