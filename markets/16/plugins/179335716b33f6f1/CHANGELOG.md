# Changelog

## 0.2.3

OpenAI Plugins Directory listing metadata. The root and Claude manifests
carry `extensions.com.openai` with explicit interface text: short
description "AI security review for PRs" (within the 30-character limit),
a long description without plan pricing (the directory forbids pricing in
the description), starter prompts, support URL, and the logo path. The description does not
name other AI products (directory rule: no references to another AI
assistant, model, or platform).
Version bump to 0.2.3 across all manifests. No skill behavior change.

## 0.2.2

Description and README lead with "Aevral is an AI security reviewer for
GitHub pull requests." The review scope now lists the live classes (access
control, business logic, injection, XSS, SSRF, path traversal, unsafe
deserialization, token and session flaws, LLM-integration risks), not only
authorization and IDOR. Console wording follows the live site: signing in
with GitHub connects the install. No skill behavior change.

## 0.2.1

Scan API pointer. The skill names `AEVRAL_API_KEY` as the environment
variable to look for (never collected in chat) and links the Scan API docs
(https://docs.aevral.com/docs/scan-api.md): start a scan with
`POST /v1/scans`, poll `status_url` every 30 seconds, stop on any 402.
The skill now also loads for a direct "start an Aevral scan" request.

## 0.2.0

Caps and upgrades. A neutral Check can mean several things (allowance used,
payment attention, paid extras paused, hourly or daily cap); the agent reads
its title or `GET /v1/usage`, and shows an upgrade link only when
`pr.action` is not null. With an `aevr_` key already in the environment
(never collected in chat), the agent may read `GET /v1/usage` and show the
human the billing link an owner or admin opens. The agent never upgrades and
never opens the link itself. Prices are quoted only from the public plans
endpoint, never from memory (replaces the blanket no-prices rule).

## 0.1.0

First public portable adapter. Setup skill for the Aevral GitHub App. Reviews
run server-side. After App install, the next pull request can already be
reviewed, including before console claim.
