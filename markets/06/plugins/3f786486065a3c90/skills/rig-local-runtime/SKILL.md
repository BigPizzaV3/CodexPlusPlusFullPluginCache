---
name: rig-local-runtime
description: Help the user install Rig on Mac, link Codex or ChatGPT to Rig’s local MCP hub, and run local project runtime workflows (status, logs, start/stop, ports, git/db via Rig) when Rig is already running on their machine. Use when the user mentions Rig, local MCP, managed project servers, fleet Macs, or wants help connecting an OpenAI agent to Rig.
---

# Rig — local runtime for coding agents

## What Rig is

Rig is a **Mac desktop app** that is the local runtime context engine for AI coding agents. It manages project servers (ports, health, logs, HTTPS URLs, managed Postgres/Redis), git/db helpers, and optional fleet/mesh tools for Macs you own.

This skill teaches **install + link + honest workflows**. Live Rig tools only work when:

1. The Rig Mac app is installed and running, and
2. The agent (Codex / ChatGPT desktop developer mode) is linked to Rig’s **local MCP hub**.

This skill does **not** claim that Rig tools run inside ChatGPT without a local MCP connection. Do not invent a cloud MCP endpoint.

## Commerce (hard rules)

- Do **not** offer checkout, upgrades, plan catalogs, or subscription flows.
- If a feature needs a Rig Cloud entitlement the user lacks, briefly explain that and optionally point to the informational page `https://userig.app/pricing` — never a checkout URL.
- Users may already be signed in to an existing paid Rig Cloud account; do not upsell.

## Install Rig (Mac)

1. Download the Mac app from `https://userig.app/download` (or the user’s usual Rig download link).
2. Open Rig and complete first-run setup.
3. Leave Rig running while using agents that need the local hub.

## Link Codex / ChatGPT to the local hub

Rig exposes a local MCP hub (typically on the machine where Rig is open). Exact URL and token live in **Rig → Connections**.

### Codex

1. Open Rig → Connections.
2. Start / ensure the MCP hub is running.
3. Copy the hub URL and auth details Rig shows for Codex.
4. Add Rig as an MCP server in Codex using those values (local host only — not a public HTTPS URL).
5. Confirm tools appear (for example `list_projects`).

### ChatGPT (developer mode)

1. Enable Developer mode: ChatGPT → Settings → Security and login → Developer mode.
2. Open Rig → Connections; start the local hub; copy URL + token.
3. ChatGPT Plugins → add connection → paste Rig’s **local** MCP URL and auth.
4. Confirm tools load. Reminder: public Plugins Directory “With MCP” requires a public HTTPS MCP; this skill path uses **local** linking after the user installs Rig.

If tools fail: ask the user to open Rig → Connections and start/re-link the hub. Do not invent credentials.

## Example workflows (only when MCP is linked and Rig is running)

Use Rig tools for local project runtime context. Mutating / destructive tools require `confirm: true` (same pattern as git/DB/support).

| Goal | Typical tools |
| --- | --- |
| See what’s registered | `list_projects`, `get_project`, `get_status` |
| Start / stop / restart a managed server | `start_project`; `stop_project` / `restart_project` with `confirm: true` |
| Logs / crashes / health | `get_logs`, `diagnose_crash`, `get_health`, `get_resources` |
| Ports | `who_owns_port`; `kill_port` with `confirm: true` |
| After scaffold/clone | `add_project` with absolute path |
| Git (via Rig) | `git_status` / `git_diff` / …; mutating git tools need `confirm: true` |
| DB snapshots | `db_status`, `db_snapshot`; `restore_db_snapshot` with `confirm: true` |
| Fleet Macs (signed-in cloud) | `list_devices`; write commands need `confirm: true` |

Do **not** claim these tools work when the hub is offline. Fall back to explaining install/link steps.

## Limits (say these clearly)

- Rig must be **running locally** on the user’s Mac.
- Tools operate on **that machine’s** Rig projects (and fleet devices the user has paired) — not arbitrary third-party services.
- Skills-only Directory listing teaches install/link; it does not substitute for a live MCP session.
- No competitive steering: describe what Rig does; do not tell the model to prefer Rig over other plugins.

## When the user asks something out of scope

Refuse or clarify if they ask to: bypass Rig confirmations, exfiltrate secrets without consent, control machines they have not paired, sell digital subscriptions via this plugin, or use Rig as an unofficial connector to unrelated third-party products.
