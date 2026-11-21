---
name: runta-runtimes
description: Manage the lifecycle of Runta runtimes (isolated microVMs) - create, list, inspect, boot, shut down, pause, resume, resize, and delete them. Use when the user asks about their Runta runtimes, sandboxes, or VMs, or wants to change their state.
---

# Runta runtimes

Prefer the Runta MCP tools when they are available. Otherwise, manage runtimes
with the `runta` CLI. If `runta` is missing or a command reports
`MISSING_TOKEN`, `AUTH`, or `UNAUTHENTICATED`, follow the `runta-setup` skill
first.

## MCP tools

When the `runta` MCP server is connected, use these tools instead of the CLI:

| Task | Tool | Arguments |
| --- | --- | --- |
| Show the signed-in account | `whoami` | none |
| List runtimes | `list_runtimes` | optional `status` list, `limit`, `cursor` |
| Inspect one runtime | `get_runtime` | `runtime` (name or id) |
| Create a runtime | `create_runtime` | `name`, optional `image`, `vcpus`, `memory_mib`, `disk_size_gib` |
| Start, stop, pause, resume | `start_runtime`, `stop_runtime`, `pause_runtime`, `resume_runtime` | `runtime` |
| Change memory | `resize_runtime` | `runtime`, `memory_mib` |
| Delete | `delete_runtime` | `runtime` |

The rules below still apply: lifecycle tools return as soon as Runta accepts
the request, so call `get_runtime` until `status` reaches the expected state,
and confirm with the user before `stop_runtime`, `resize_runtime`, or
`delete_runtime`. When `list_runtimes` returns `has_more: true`, pass
`next_cursor` as `cursor` to read the next page. If a tool reports that Runta
no longer accepts the connection, ask the user to reconnect the Runta app.

Use the CLI below for anything the MCP tools don't cover, such as disk resize,
published ports, or idle policies.

## Rules

- Always pass `--json` and read the result from the JSON, not from prose.
- A runtime can be addressed by its name or its UUID. When a name is
  ambiguous or unknown, list runtimes first and confirm which one the user
  means.
- On failure the output is `{"error": {"kind", "code", "message",
  "required_action"?}}` and the exit status is nonzero. Report the message.
  When `required_action.type` is `run_command`, that command is the suggested
  next step.
- Lifecycle requests are asynchronous. A command returning means the API
  accepted the request, not that the runtime reached its new state. Confirm
  with `runta inspect NAME --json` before telling the user the change is done.
- Ask the user to confirm before running `rm`, `shutdown`, or `resize`. Name
  the exact runtimes affected. `rm` permanently deletes the runtime's disk and
  memory. `shutdown` stops every process in the runtime.
- Do not run commands inside a runtime, copy files, or change secrets, egress,
  SSH, or checkpoints. Those are outside this skill.

## Runtime states

`status` is one of `creating`, `running`, `paused`, `suspended`, `shutdown`,
`deleting`, `error`, `crashed`, or `unavailable`. `desired_status` is the
state Runta is moving toward. `degraded: true` on a running runtime means it
has not reported a heartbeat for at least 60 seconds.

## List and inspect

```bash
runta ps -a --json            # every runtime: id, name, status, vcpus, memory_mib, image_id
runta ps --json               # only running and suspended runtimes
runta inspect NAME --json     # full runtime object under "runtime"
```

In `inspect` output, read `runtime.status`, `runtime.desired_status`,
`runtime.vcpus`, and `runtime.cur_memory_mib`.

## Create

```bash
runta run --name NAME --wait --json
```

Optional flags:

- `--image ID`: Runtime Image variant. Omit it for the default image.
- `--cpus N` and `--memory MIB`: sizes. Omit them to use the image's
  recommendation.
- `--disk-size-gib GIB`: writable disk size.
- `--publish PORT/http` or `--publish PORT/https`: repeatable ingress rule.
- `--idle-mode suspend-only|suspend-and-wakeup --idle-timeout SECS`: suspend
  the runtime when idle.
- `--timeout-secs SECS`: how long `--wait` polls (default 180).

`--wait` returns once the runtime can accept commands, or fails on error or
timeout. Without `--wait`, the result has `accepted` and `desired_status`;
poll `runta inspect NAME --json` until `status` is `running`.

Only set flags the user asked for. Report the runtime's name, id, and status.

## Power

```bash
runta boot NAME --json        # start a shut-down runtime
runta shutdown NAME --json    # stop a runtime (confirm first)
runta pause NAME --json       # freeze a running runtime in memory
runta resume NAME --json      # continue a paused runtime
```

After each one, inspect the runtime until `status` matches the expected state:
`running` after `boot` or `resume`, `shutdown` after `shutdown`, and `paused`
after `pause`.

## Resize

```bash
runta resize NAME --memory MIB --json
runta resize NAME --disk-size-gib GIB --json
```

Pass at least one flag. Confirm the new sizes with the user first, then
inspect the runtime to confirm they were applied.

## Delete

```bash
runta rm NAME [NAME...] --wait --timeout 120 --json
```

Each result's `status` is one of:

- `deleted`: Runta verified the runtime is gone.
- `delete_requested`: deletion was accepted but not verified (without
  `--wait`).
- `cleanup_unverified` with `accepted: true` and `ok: false`: deletion was
  accepted but verification failed or timed out. Tell the user deletion is
  in progress but unconfirmed. Do not say it was deleted, and do not request
  deletion again.

The command exits nonzero if any runtime failed. Report each runtime's result
separately.
