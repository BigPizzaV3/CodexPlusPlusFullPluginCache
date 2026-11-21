# MCP Tool Specification: `get_3chat_workspace_readiness`

Development specification for the read-only startup tool required by plugin version 1.1.0. Do not submit this plugin version until the production MCP server exposes the tool with a compatible contract.

## Title

Check 3Chat startup milestones

## Tool Description

Returns whether the current authenticated 3Chat workspace has ever completed two startup milestones: publishing a 3Chat Agent and connecting a messaging channel. These are durable onboarding achievements. Once a milestone is complete, later unpublishing or removing the Agent, disabling or disconnecting a channel, or revoking channel authorization does not reset it. This tool does not report current operational availability and does not create or modify configuration.

## Input

The tool has no business input. The current tenant and workspace are resolved from the authenticated connection context.

```json
{
  "type": "object",
  "properties": {},
  "additionalProperties": false
}
```

## Successful Response

```json
{
  "code": 200,
  "data": {
    "workspace_id": "workspace_1001",
    "workspace_name": "Acme Growth",
    "readiness_status": "ACTION_REQUIRED",
    "milestones": {
      "agent_published": {
        "status": "NOT_COMPLETED",
        "completed_at": null
      },
      "channel_connected": {
        "status": "COMPLETED",
        "completed_at": 1791763200000
      }
    },
    "missing_requirements": [
      "AGENT_PUBLISHED"
    ],
    "actions": [
      {
        "code": "BUILD_OR_PUBLISH_AGENT",
        "label": "Build and publish a 3Chat Agent",
        "url": "https://app.3chat.ai/embedded-app/subapp?url=/butler/agent/builder"
      }
    ],
    "checked_at": 1791766800000,
    "request_id": "request_1001"
  }
}
```

## Status Semantics

`data.readiness_status`:

- `READY`: both startup milestones have been completed at least once.
- `ACTION_REQUIRED`: one or both startup milestones have never been completed.

Each `data.milestones.*.status` is:

- `COMPLETED`: the milestone has been completed at least once.
- `NOT_COMPLETED`: the milestone has never been recorded as complete.

`completed_at` is the earliest known completion time as a Unix millisecond timestamp. It may be `null` for a completed legacy workspace when the exact historical time is unavailable.

`missing_requirements` contains only `AGENT_PUBLISHED` and/or `CHANNEL_CONNECTED` when unmet. `actions` contains only applicable next steps. Each action has a machine-readable `code`, a display `label`, and an absolute `url`. `BUILD_OR_PUBLISH_AGENT` and `CONNECT_CHANNEL` are action-code values, not URLs or separate MCP tools. The tool must not return a model-facing workflow or perform redirects.

`READY` does not prove that an Agent is currently published, a channel is currently enabled or authorized, customer data exists, or a message can currently be sent. Business tools perform their own current-state validation and return their own structured errors.

## Action URLs

The server returns absolute URLs derived from its configured public application origin, never from user input or an untrusted request header.

Supported origins:

- International: `https://app.3chat.ai`
- China: `https://app.3chatai.cn`

Paths:

- `BUILD_OR_PUBLISH_AGENT`: `/embedded-app/subapp?url=/butler/agent/builder`
- `CONNECT_CHANNEL`: `/embedded-app/subapp?url=/butler/channels/overview`

Examples:

- `https://app.3chat.ai/embedded-app/subapp?url=/butler/agent/builder`
- `https://app.3chat.ai/embedded-app/subapp?url=/butler/channels/overview`
- `https://app.3chatai.cn/embedded-app/subapp?url=/butler/agent/builder`
- `https://app.3chatai.cn/embedded-app/subapp?url=/butler/channels/overview`

Links must not contain credentials. Only actions for incomplete milestones are returned.

## Internal Logic

1. Resolve the tenant and current workspace exclusively from the validated connection identity.
2. Read durable onboarding milestone records for that workspace.
3. Mark `agent_published` complete when the workspace publishes an Agent for the first time.
4. Mark `channel_connected` complete when the workspace successfully connects a messaging channel for the first time.
5. Once set, never reset either milestone because current resources are unpublished, disabled, unauthorized, disconnected, or removed.
6. For workspaces created before milestone tracking exists, backfill from reliable publication and channel-connection history. If current records can be deleted, retain a dedicated milestone record or auditable historical event so completion is not lost.
7. Set `READY` only when both durable milestones are complete; otherwise set `ACTION_REQUIRED`.
8. Return only action links applicable to incomplete milestones, using the deployment's configured application origin.

Do not implement this tool by counting currently published Agents, active channels, or authorized channels. Those values represent operational state and would violate the durable achievement semantics.

## Errors

Use the server's standard structured error envelope and existing `aiAction` vocabulary.

| Error code | Meaning | Expected action |
| --- | --- | --- |
| `UNAUTHORIZED` | The connection credential is missing, invalid, or expired. | Reconnect or authorize 3Chat. |
| `FORBIDDEN` | The authenticated user cannot access the current workspace. | Stop and report the permission problem. |
| `WORKSPACE_NOT_FOUND` | The connection context no longer resolves to an accessible workspace. | Stop and reconnect or select a valid workspace through 3Chat. |
| `READINESS_CHECK_FAILED` | A temporary internal dependency prevented the milestone check. | Follow the returned `aiAction`; retry only when explicitly allowed. |

Example:

```json
{
  "code": 503,
  "error_code": "READINESS_CHECK_FAILED",
  "error_message": "Workspace startup milestones could not be checked.",
  "aiAction": "RETRY_SAME_REQUEST",
  "request_id": "request_1002"
}
```

## MCP Annotations

```json
{
  "readOnlyHint": true,
  "destructiveHint": false,
  "openWorldHint": false
}
```
