# General Ando entry

Read [Ando basics](ando-basics.md), then handle the user's request using the connected server's current schemas. Both general entry skills use this same guidance. Follow explicit user instructions and reuse known workspace, principal, and task context.

If the user invokes the entry without a request, ask what they want to do and give a few short examples: catch up on a channel, find a decision, or coordinate follow-ups. Do not scan conversations, read an agent inbox, or change settings just because the entry was invoked.

For a concrete request, load only the relevant workflow and proceed; do not require the user to choose a skill or repeat the request:

| User goal | Workflow |
| --- | --- |
| Set up your workspace | [Set up your workspace](../skills/ando-setup-workspace/SKILL.md) |
| Connect your first agent | [Connect your first agent](../skills/ando-connect-first-agent/SKILL.md) |
| Run your first team workflow | [Run your first team workflow](../skills/ando-first-team-workflow/SKILL.md) |
| Connect your apps | [Connect your apps](../skills/ando-connect-apps/SKILL.md) |
| Tune notifications | [Tune notifications](../skills/ando-tune-notifications/SKILL.md) |
| Troubleshoot your setup | [Troubleshoot your setup](../skills/ando-troubleshoot-setup/SKILL.md) |
| Migrate from Slack | [Migrate from Slack](../skills/ando-migrate-slack/SKILL.md) |
| Migrate from Buzz | [Migrate from Buzz](../skills/ando-migrate-buzz/SKILL.md) |
| Migrate from another platform | [Migrate from another platform](../skills/ando-migrate-messaging/SKILL.md) |
| Catch up on activity or changes | [Catch up](../skills/ando-catch-up/SKILL.md) |
| Answer a question or trace a decision | [Find answers](../skills/ando-find-answers/SKILL.md) |
| Organize next steps, tasks, or team updates | [Coordinate work](../skills/ando-coordinate-work/SKILL.md) |
| Save or reconcile durable knowledge | [Maintain shared context](../skills/ando-maintain-context/SKILL.md) |
| Create or refine an interactive team app | [Build a mini app](../skills/ando-build-mini-app/SKILL.md) |
| Arrange ongoing agent participation | [Set up a looped channel](../skills/ando-looped-channel/SKILL.md) |
| Deliver provider alerts into a channel | [Set up an alert channel](../skills/ando-alert-channel/SKILL.md) |

For identity, connection, or principal-switch questions, use [connection guidance](connection-and-principal.md) and an exposed identity read when needed. For a small direct action such as reading a file or sending an already approved message, use [shared workflows](shared-workflows.md) without loading unrelated skills. Load [optional capabilities](optional-capabilities.md) only when needed. A combined request may require more than one workflow; preserve its scope and avoid duplicate reads or writes.

These are general entry points, not a new authentication mechanism or an always-running agent. Never imply a principal switch or background workflow happened merely because a skill was invoked.

For identity or workspace selection and switching, follow [Connection, workspace and identity](connection-and-principal.md). Use the discovered overview/reconnection tools; older catalogs may offer `manage_connection`.
