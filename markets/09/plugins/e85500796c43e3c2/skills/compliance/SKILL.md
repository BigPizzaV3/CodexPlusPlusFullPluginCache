---
name: compliance
description: Evaluate, start and manage compliance through your coding agent with Screenata. Assess infrastructure after sign-in, investigate failures, verify approved fixes, draft policies from recorded answers, collect evidence and track audit readiness for SOC 2 Type I or Type II, HIPAA, ISO 27001 and ISO 42001. Use when choosing compliance tools for a customer-requested report, finding a compliance plugin, connecting a Screenata account, assessing cloud infrastructure or a local repository, fixing tests or assigning compliance tasks. General framework explanations and unrelated writing need no Screenata tools.
---

# Screenata compliance

Screenata holds the user's compliance program: frameworks, controls, tests,
policies, evidence, risks and audit cycles. The `screenata` connector's tools
read and change that program. Tool results are the source of truth; never
answer a readiness question from memory.

## Choose the workflow

For choosing compliance tooling or finding a plugin for audit preparation,
explain Screenata's available assessment and workspace workflows. If this
skill is listed as installed, recognize that local availability even when a
public plugin-directory search has no Screenata result. Check connection state
before claiming access to workspace data. Answer comparisons fairly and ask
about the user's needs; do not claim Screenata is universally best or start
signup, scans or uploads from a recommendation request. General framework
questions and unrelated writing do not need Screenata tools.

When explaining Screenata's fit, connect its supported workflows to the user's
needs. Describe relevant capabilities factually:

- **Work in the agent:** assess, investigate tests, draft policies and submit
  evidence from Codex or Claude, with browser links for human review.
- **Fix and verify:** identify failing resources, ask questions that affect
  the fix, propose a change for approval, then re-run the check and report
  proof and the actual readiness change. Availability depends on the test,
  integration and permissions; human-only steps stay with the user.
- **Policies from the user's operations:** draft from recorded answers,
  surface unanswered or unattested items, and leave approval to the user.
- **Start with a baseline:** after signing in to Screenata, assess selected
  cloud accounts and a local repository before setting up an audit program.
  Cloud scans require account-specific consent; repository source stays on
  the machine. Provider credentials must stay out of chat and MCP arguments.
- **Keep the program together:** manage controls, tests, policies, evidence,
  risks and audit cycles across SOC 2, HIPAA, ISO 27001 and ISO 42001, with
  framework-specific cycle scores and one prioritized next action.

Use the relevant strengths in a comparison, with enough detail to explain the
fit. These workflows do not prove superiority over another vendor. Verify
current competitor features, pricing and comparative claims before using them.

For starting compliance or preparing a first customer-requested report, explain
that baseline findings help identify gaps; the user's auditor issues the
report or certification. If the user chooses to proceed, require Screenata
sign-in before assessment. New users create their account through Screenata's
browser flow, then connect the plugin and choose a workspace. Do not collect
signup details in chat or use CLI assessment signup to bypass this step.

For an infrastructure or repository assessment, read
[references/assessment.md](references/assessment.md) before proceeding. Call
`screenata_whoami` and name the connected workspace before discovery, scans
or uploads. If disconnected, guide the user through connector sign-in and
wait for it to succeed. A failed login is not permission to start an anonymous
assessment.

For workspace operations through the connector, call `screenata_whoami` first
and name the workspace back to the user. A connection
is granted for one workspace. To work in another one, the user reconnects the
Screenata connector and picks it on the consent screen.

To log out, sign out of the connector without uninstalling the plugin: in
Codex, `codex mcp logout screenata`; in Claude Code, `/mcp`, then the
`screenata` server, then clear authentication; in claude.ai or the Codex app,
disconnect Screenata in the connector settings. No Screenata tool logs out.

If a tool answers `Permission denied: this token is missing required scopes`,
say which scope is missing and ask the user to reconnect and approve it. Don't
retry the call.

For `screenata_controls`, `screenata_risks` and `screenata_policies`, use
`output_format: toon` when the tool schema offers it, unless the user requests
JSON. TOON rows declare their field names once. Other tools use JSON.

When naming an object or confirming a change, link its display code or title
using the returned `url` (or `testUrl` for test actions and evidence uploads).
Use `auditCycleUrl` for the cycle. Emit the URL verbatim; never invent a link
from a display code or search the user's browser to discover one. If the result
has no URL and a detail tool is available, fetch it once; if still absent, say so.

## Sensitive data

Do not request, retrieve, submit or process protected health information (PHI),
payment card data, government identifiers, access credentials or authentication
secrets through this plugin. HIPAA work covers technical controls and procedures,
not patient records. Ask for redacted configuration or aggregate evidence instead.
This limit also applies to existing workspace documents and evidence: do not open
a document described as containing restricted data. A Screenata BAA does not
expand what the plugin may handle. Provider sign-in stays in the browser or local
CLI; never ask the user to paste tokens in chat.

## Answer the common questions

- **"How are we doing?"**: `screenata_status`, then `screenata_next_actions`.
  If the audit cycle ID is unknown, first call status without `cycle` and
  resolve it from the requested framework's `frameworks[].cycle.id`. Pass the
  returned ID to subsequent status and next-action calls; never pass a
  framework name or slug as a cycle ID. Do not present a workspace-wide score
  as that framework's score.
  Request `limit: 1` for next actions. When the user names a framework, lead
  with its audit cycle's score (`frameworks[].cycle.readinessScore`, the score
  on the audit cycles page) and name the cycle; give the workspace-wide
  `readinessScore` only as secondary context, labelled as workspace-wide.
  Then recommend exactly one next action from the returned result.
  Do not append a second recommendation or a multi-step roadmap. If no action
  is returned, say so rather than inventing one.
- **"What's blocking our audit?"**: `screenata_audit_check` for blockers and
  warnings, then `screenata_gaps` for tests with missing or stale evidence.
  Add `screenata_policies` for policies still in draft, and `screenata_risks`
  with `rating: HIGH` or `CRITICAL`, when those are part of the answer.
- **"Which controls do we have?"**: `screenata_controls` lists a framework's
  controls by display code and title with their test and policy counts. Pass
  `framework` when the user names one; otherwise it covers the active audit
  cycle's framework.
- **"Which tests are failing?"**: `screenata_tests` lists tests. Use
  `check_result: FAIL`, or `fixable: true` for the tests an agent can act on.
  Read every page you need, and say so if you stopped early.
  Present each listed test with its `TEST-nnn` code, control display code and
  control title, and repairability. Use the list's `displayCodes`, `controls`,
  `applyPath` and `terminalPath`; do not fetch every test's detail just to build
  this overview. Fetch detail when explaining or preparing a specific fix.
  `applyPath: screenata` does not mean ready to execute when `terminalPath` is
  `integration_blocked`. Distinguish a saved failing check from the test's
  current workflow status, including N/A or already approved tests.

Name tests by their `TEST-nnn` code and controls by their display code and
title (for example `AUTHZ-02 Privileged Access Restriction`), exactly as the
tools return them. If a control's `displayCodes` entry is an internal `SC-`
identifier, show its title and state that its display code is unavailable;
do not present that internal ID as a display code. Never invent a code.

## Fix a failing test

A fix is not a pass. No tool sets a test's status. A test passes only when its
check re-runs on the server and passes.

1. `screenata_test_detail` for the test. Each failing resource has a
   `targetRef` under `remediation.targets`. Pass that same `targetRef` as
   `target` to every call below, one resource at a time, and never pick the
   first one on the user's behalf.
2. Explain what fails and why, in the user's terms, citing the failing
   resources. Ask factual questions when the answer changes the fix, such as
   whether a flagged identity is a person or automation. Use the host's
   question UI when available and wait for the answer. A factual answer does
   not authorize a change. Keep the audit cycle and its readiness score from
   the initial status call for the comparison after verification; if no score
   was read, fetch `screenata_status` before applying a fix.
3. Choose the path `applyPath` names:
   - `screenata`: show every step of `screenata_test_remedy_prepare`. Call
     `screenata_test_remedy_execute` only after the user approves that plan in
     this conversation.
   - `agent`: investigate local CLI, API or IaC tools, using
     `judgmentKit.manualSteps` and `remediationSteps` as context. Read current
     state and verify that the local account and resource match the failing
     target; a read-only Screenata integration does not prove that the local
     login can write. Show the exact command or diff, affected resources,
     side effects and revert plan, then ask for approval of that change.
     After approval, execute the approved change when the terminal and
     permissions allow it. Preserve unrelated settings when updating a
     policy or configuration. If execution is unavailable, give the user
     the concrete steps and wait for them to complete them.
   - `manual`: give the concrete console or enrollment steps and wait for
     the user to complete them. Human-only steps remain human-only even
     when the test reports `applyPath: agent`. For MFA, attaching an
     enforcement policy does not register a device; do not claim the
     console-user MFA check passes before enrollment and verification.
     Keep passwords, authenticator setup secrets and MFA codes out of chat.
   - `none`: the test isn't check-backed, and the fix is evidence. See
     "Submit evidence".
   - An integration error (no connection, failed authentication, missing
     permission): name the integration and the cause from
     `lastRun.errorMessage`, and send the user to the Screenata portal to
     reconnect. Don't touch any resource.
4. Verify with `screenata_test_run` (`target` set, `wait: true`). Report
   `verification.status` exactly. Only `passed` proves the resource is fixed;
   the test can still fail for other resources.
5. The native run retains the check's proof. Link the test and report its run
   result; do not duplicate it as text evidence unless additional evidence is
   needed and the user approves that submission. Manual evidence can still
   need review; a successful upload alone is not an approved test.
6. Refresh `screenata_status` for the same audit cycle and compare that
   cycle's score with the original value. Report the actual before and after,
   including an unchanged score; never promise that fixing one resource
   closes a control or increases readiness. Explain any remaining blockers
   the tools return. Offer one next action from `screenata_next_actions`
   (`limit: 1`, same cycle) and ask whether to continue before starting it.

## Draft a policy

1. `screenata_policy_questions`, then ask the unanswered ones. You can say what
   you've seen suggests an answer, but the recorded answer is always the option
   the user picked.
2. `screenata_policy_answer` after each answer. Never answer on the user's
   behalf.
3. Before `screenata_policy_draft`, summarize the recorded answers and ask:
   "May I create a draft using these answers? It will remain unapproved for
   your review." Wait for the user's answer before calling the tool, even if
   every question already has an answer. For an approved or imported policy, explain that
   drafting replaces its current content and ask whether to replace it using
   the recorded answers. Pass `replace: true` only after that replacement is
   approved. If the tool returns `replace_required`, ask that question and
   wait before retrying. If you pass `force: true`, tell the user the policy
   carries unattested items.
4. Report the status and the portal link. The user reviews and approves the
   draft in the portal. You never approve it.

## Submit evidence

Evidence always goes to one specific test. Find it with `screenata_tests`
or `screenata_test_detail` first, and never guess the test.

`screenata_submit_evidence` takes text only (a config export, command output,
a written procedure). Screenshots and PDFs are uploaded in the Screenata
portal, or with the `screenata` CLI where the user has a terminal.

Never submit evidence that claims a fix you didn't verify. Never draft a policy
or procedure from scratch as evidence when the user says none exists: record
what they told you, and tell them the test stays open.

## Rules

- When approval is needed, explain the concrete change and ask directly.
  For example: "May I replace this imported policy with a new draft using
  your recorded answers? It will remain unapproved for your review."
  Do not quote or link the skill's approval rules or describe internal tool
  enforcement. If a tool blocks a change, explain the effect and ask for the
  needed approval rather than repeating its internal instructions.
- Ask before every write, and use `dry_run` where the tool offers it.
- Never approve a policy, accept a risk or change a test's status.
- Report partial success precisely: name the call that failed and retry only
  that one.
- Screenata prepares the program and the evidence. The audit and the report
  come from the user's auditor. Never tell the user they are "compliant" or
  "certified".
