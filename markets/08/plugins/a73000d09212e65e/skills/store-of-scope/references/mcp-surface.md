# Store of Scope MCP surface

Authentication: not required.

## Tools

| Tool | Description | Behavior | Visibility |
| --- | --- | --- | --- |
| `approve_content_plan` | Persist the exact reviewed content-plan proposal and digest at the expected revision. | write; confirmation required | model and app |
| `begin_workflow_run` | Acquire or replay one idempotent workflow run at the expected automation-state revision. | write | model and app |
| `calculate_due_work` | Calculate due Store of Scope branches without writing. The local date and weekday must already correspond to the configured workspace timezone. | read-only; idempotent | model and app |
| `commit_workflow_run` | Commit a pending workflow only after artifact validation passes and any enabled delivery has a provider receipt. | write | model and app |
| `get_store_of_scope_status` | Read a redacted Store of Scope workspace summary, state revisions, archive count, pending run, recent runs, and safest next action. | read-only; idempotent | model and app |
| `propose_content_plan` | Create a deterministic, reviewable unread-newsletter plan without writing caller state. | read-only; idempotent | model and app |
| `reconcile_archive_index` | Merge up to 250 normalized Gmail message records by immutable message id without deleting prior archive ids. | write | model and app |
| `retire_workspace` | Permanently complete all caller-scoped Store of Scope state handles. Completed handles become read-only. | write; destructive; confirmation required | model and app |
| `save_workspace_config` | Validate, normalize, and save one caller-scoped Store of Scope workspace configuration at an expected revision. | write; confirmation required | model and app |
| `set_automation_paused` | Pause or resume unattended Store of Scope workflow orchestration at the expected configuration revision. | write; confirmation required | model and app |

## Resources

| Resource | Description |
| --- | --- |

## Prompts

| Prompt | Description | Arguments |
| --- | --- | --- |

## Widgets

| Widget | Description | Opening tool |
| --- | --- | --- |
