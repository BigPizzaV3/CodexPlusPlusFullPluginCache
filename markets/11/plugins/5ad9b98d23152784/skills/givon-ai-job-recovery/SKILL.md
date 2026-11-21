---
name: givon-ai-job-recovery
description: "Inspect and recover a Givon AI generation by checking its status, errors, balance or quota, and MCP readiness."
metadata:
  version: skill-render-ea6bd93365667f6d
---

# Givon AI Job Recovery

Separate transport/config failures from in-band generation results. A failed job
is still a normal status response when the transport succeeded.

## Route

1. If the user has a job id, call `givon_get_generation_status`.
2. Treat `succeeded`, `failed`, and `canceled` as terminal.
3. For `queued` or `processing`, report progress briefly and keep polling only
   if the user asked you to wait.
4. For balance or quota questions, call `givon_get_balance`.
5. If tools are unavailable in a web chat, ask the user to reconnect Givon in
   the host's plugin/connector settings. With shell access, use the configured
   CLI/MCP doctor path before asking for more information.

## Playbook

- Transport/tool unavailable: reconnect through the host's browser sign-in.
  With shell access, `givon login` (no key) or
  `givon mcp doctor --client <client>` are available. A web user does not need
  to install or run a CLI.
- Auth failure: tell the user to reconnect — `givon login` (browser, no key) or
  reconnect the MCP client; for CI keys, create/rotate one in the Givon cabinet.
  Do not request the secret in chat.
- Schema/input issue: remove unsupported fields or ask for the missing required
  fields together.
- Model/job failure: explain `errorCode` and `errorMessage`; propose a narrower
  retry prompt or supported parameter change.
- Balance/quota issue: report live balance; do not guess spend or discounts.

Read [references/troubleshooting.md](references/troubleshooting.md) for concise
operator notes.
