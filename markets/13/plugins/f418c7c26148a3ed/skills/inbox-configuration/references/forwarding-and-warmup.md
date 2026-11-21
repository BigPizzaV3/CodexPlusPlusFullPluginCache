# Reply forwarding and warmup

## Reply forwarding

Forwards replies from a sending mailbox to the client's own external inbox. Off by default when a mailbox is provisioned.

- One inbox: on the Email Delivery page, the inbox's Inbox actions > Edit inbox > Reply forwarding, the destination address, Save changes.
- Many inboxes: the same, once per inbox.
- Turn it off: clear Reply forwarding and save.

Only an external destination is accepted: a destination on a platform-hosted address or on one of the workspace's managed sending domains is rejected. Google, Outlook, and Azure mailboxes all accept it. The provider queues the change, so it can take a few minutes to apply.

This is reply forwarding, not the domain's forwarding URL (where people who open the domain land). That one is a domain setting: on the Inboxes tab, select the domain's inboxes, then Set forwarding URL, and Apply.

## Warmup

Every new managed mailbox is enrolled in warmup automatically. Warmup sends share the mailbox's provider budget with cold sends, so do not set a cold limit that leaves no room for it.

Warmup is not readable here. The inbox's Inbox actions menu shows Pause warmup while it warms, and Resume warmup or Enable warmup when it does not. When the user can tell you the warmup status, act on it:

| `status` | What to do |
|----------|------------|
| `in_progress` | Already warming. Nothing to do |
| `pending` | Bought and waiting to activate. Leave it alone |
| `paused` | Resume only if the user asks: Inbox actions > Resume warmup |
| `failed` | The provider cannot warm it. Re-enabling does not fix it. Tell the user it needs the support team |
| `not_started` | No warmup subscription. Enrolling is a staff step, not available from this skill |
| `completed`, `maintenance`, `degraded` | An older warmup record, shown when no warmup provider tracks the inbox now. Nothing to resume from this skill; if the user wants it warming, it needs the support team |

Pause is Inbox actions > Pause warmup. Pause and resume need the admin role and a yes from the user. An inbox the cold-send gate still holds while it warms is waited out rather than given a higher limit.
