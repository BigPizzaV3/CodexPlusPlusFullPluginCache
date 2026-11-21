# Store of Scope setup contract

## Release boundary

This package connects to the hosted Store of Scope MCP deployment on Noodle Seed. If the MCP connection rejects the user or cannot establish a caller-scoped workspace, stop and report the connection boundary; do not request Noodle credentials or attempt a workaround.

Noodle Seed is hosting infrastructure, not a user dependency. Users install Store of Scope and explicitly connect their own Google apps.

## Dependency contract

| Capability | Requirement | Minimum proof |
| --- | --- | --- |
| Store of Scope MCP | Required | `get_store_of_scope_status` returns a caller-scoped response |
| Gmail read | Required | One bounded, read-only sender query succeeds |
| Gmail send | Conditional | Required only when delivery is enabled; first send remains approval-gated |
| Calendar | Optional | Required only when the user enables the managed reading event |
| Drive | Optional | Required only when the user requests cloud artifact copies |
| Scheduled tasks | Preferred | One task is created after explicit schedule approval, otherwise manual mode |

Installing an app and authorizing an account are distinct. Never claim a dependency is ready until both the capability and a safe proof are present.

## Approval ledger

Record these as separate decisions in the setup summary:

- initial ingestion;
- first send;
- future unattended sending;
- Calendar event management;
- one daily scheduled task; and
- destructive retirement or deletion.

Approval for one item never implies another.

## Automation contract

Create one automation named **Store of Scope daily orchestration**.

- Schedule: daily at the configured local time, default `18:00`, in the configured timezone.
- Scope: the current Store of Scope workspace.
- Creation gate: MCP status is available, configuration validates, Gmail read proof succeeds, no unresolved pending run exists, and the user approves the exact schedule and prompt.
- Delivery gate: sending remains disabled unless future unattended delivery was separately approved.

Automation prompt:

> Run the Store of Scope daily orchestration for this workspace. Read status, calculate due work using the configured local date and weekday, and stop on any blocker or pending run. Reconcile only normalized Gmail metadata. Never generate, send, or commit without the required approval and receipts. Return `no_action_due` without writing when nothing is due. Report the run ID, completed branches, artifact receipts, delivery receipt when applicable, and safest next action.

After creation, report the task name, schedule, timezone, next run, delivery mode, and pause instructions. Do not claim automation is active until the host confirms creation.

## Manual mode

If the host cannot create scheduled tasks, preserve the validated workspace and report manual mode. Give the user this invocation:

> Run today's Store of Scope newsletter workflow.

Manual mode is a valid fallback, not scheduled automation. Do not claim automation is active.

## Failure behavior

- Gmail read failure: stop before ingestion.
- Gmail send failure: leave the run pending and uncommitted.
- Artifact validation failure: do not deliver or commit.
- Provider receipt exists but commit failed: reconcile the receipt before retrying; do not resend.
- Calendar failure: report it separately and continue newsletter delivery when Calendar is optional.
- Duplicate Calendar events: stop creating events and request approval before cleanup.
