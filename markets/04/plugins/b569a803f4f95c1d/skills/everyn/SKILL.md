---
name: everyn
description: Work with hosted Everyn datasets, jobs, runs, and exports.
license: Apache-2.0
metadata:
  io.everyn/host: openai-codex
  io.everyn/canonical: docs/mcp-v1-guidance/skill.md
---

Host packaging only. Do not fork tools, authorization, errors, side effects, or
workflow rules. Install recipes stay on the published Connect page. Reconnect
and revoke stay in Everyn Settings.

- Install: https://www.everyn.ai/docs/mcp/connect
- Connection control: https://app.everyn.ai/settings/mcp

The public production MCP endpoint is live at
https://mcp.everyn.ai/mcp. Configure a host with that Streamable HTTP URL
and complete WorkOS OAuth.

# Everyn

You are connected to Everyn, a hosted Dataset-to-results workspace. Use the
fourteen tools in this catalog. Never invent a fifteenth tool or a host-specific
shortcut.

The public production MCP endpoint is live at `https://mcp.everyn.ai/mcp`.
Configure a host with that Streamable HTTP URL and complete WorkOS OAuth.
See [Connect](https://www.everyn.ai/docs/mcp/connect) for host install recipes.

## Required agent behavior

- Never treat a local filesystem path as a hosted file. Use `upload_csv` or
  rediscover a Dataset the user uploaded in the app.
- Never silently widen a sample Run into a full-dataset Run.
- Do not invent cost, plan, usage, or funding values. If a section is
  `available: false`, say so and use the provided handoff.
- After the user asked you to wait, keep calling bounded `get_run` waits
  without asking them to prompt again.
- Do not blindly retry quality or spec failures.
- Do not stop at terminal Run status. Export, download, and analyze the
  complete-results CSV.
- Do not ask for a second approval to export or analyze an already authorized
  Run.
- After discovery, use exact Everyn IDs. Do not guess resources by name.
- Never echo a signed transfer descriptor object in later tool inputs or logs.
  Tool text may include compact transfer facts (method, URL, required headers,
  expiry, and next step) so ordinary HTTPS clients can complete the transfer.
  Prefer the structured descriptor when the host exposes it. Do not require a
  dedicated host transfer handler.
- Do not fetch arbitrary URLs. Only Everyn-issued transfer targets exist, and
  the client moves bytes.

## Workflow

1. Call `get_context` for the current authenticated organization only.
2. Upload or rediscover a Dataset. If `upload_csv` returns a signed transfer
   descriptor or compact transfer text, PUT the CSV to the issued HTTPS target.
   Never echo the descriptor object in later tool inputs or logs.
3. Create or patch a Job with `save_job`. Prefer a sample before an unverified
   full Run.
4. Start work with exactly one `start_run` form: new, resume, or retry.
5. Wait with bounded `get_run` calls. Preview with `get_run_results` if needed.
6. When `next_action` is `export_and_analyze`, call `export_run`, download the
   CSV locally, and analyze that file for the user.

## Job development

Prepare or select a Dataset, author the output contract, choose models and
capabilities, sample, inspect, revise, and pin the verified Job version.

Progressive references:

- [Datasets](https://www.everyn.ai/docs/mcp/datasets)
- [Jobs](https://www.everyn.ai/docs/mcp/jobs)
- [Help: complete your first workflow](https://www.everyn.ai/help/getting-started/complete-your-first-workflow)

If the host cannot move local CSV bytes, use the Datasets fallback at
`https://app.everyn.ai/datasets`, then rediscover the Dataset. Do not treat a
local path as a hosted file.

## Run operations

Start an explicit sample or full Run, wait without cancelling work, preview
only as a bounded quality check, retry or resume when the Run state allows it,
harvest or cancel when the user asked, then export and locally analyze the
complete-results CSV.

Progressive references:

- [Runs](https://www.everyn.ai/docs/mcp/runs)
- [Export](https://www.everyn.ai/docs/mcp/export)
- [Help: waits, retries, and cancellation](https://www.everyn.ai/help/mcp/upload-wait-and-cancel)
- [Help: export and support](https://www.everyn.ai/help/mcp/export-and-support)

Do not stop at terminal Run status. Do not ask for a second export approval.

## Setup and account

Authenticate through WorkOS OAuth. One grant binds one user, one client, and
exactly one organization. Inspect, reconnect, and revoke from Everyn Settings.
Do not request organization IDs. Do not use API keys when WorkOS failed.

Progressive references:

- [Connect](https://www.everyn.ai/docs/mcp/connect) for host install recipes
- [Authentication](https://www.everyn.ai/docs/mcp/authentication) for scopes
- [MCP connection settings](https://app.everyn.ai/settings/mcp) for reconnect and revoke
- [Help: connect and reconnect](https://www.everyn.ai/help/mcp/connect-and-reconnect)
- [Privacy](https://www.everyn.ai/docs/mcp/privacy), [Privacy Policy](https://www.everyn.ai/privacy), and [Terms](https://www.everyn.ai/terms)

Paid `start_run` uses Everyn's shared billing controls. If admission is denied,
report the stable error and send the user to Usage and Billing at
`https://app.everyn.ai/settings`. Do not offer checkout, funding top-up, plan change, or payment mutation.

## Consequential actions

A direct user request for the exact sample, full Run, retry, resume, or
cancellation is sufficient intent. If you propose one of those actions, show
the receipt summary and ask first. Host-native confirmation may still appear.

## Out of scope

Do not request organization IDs. Do not use API keys when WorkOS failed. Do
not fetch arbitrary URLs. Do not ask the user for another credential to
complete a constrained transfer. Do not paste access tokens, refresh tokens,
or signed transfer descriptors into chat, tickets, or logs.
