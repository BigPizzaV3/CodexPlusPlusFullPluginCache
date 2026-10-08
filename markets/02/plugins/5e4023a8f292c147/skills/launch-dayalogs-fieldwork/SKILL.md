---
name: launch-dayalogs-fieldwork
description: Prepare, test, launch, and monitor Dayalogs survey fieldwork through the Dayalogs MCP. Use when a user wants to publish a survey, create hosted links or LinkSets, configure an embed, import an audience, send a campaign, test delivery, apply quotas or dates, or monitor collection and campaign delivery.
---

# Launch Dayalogs Fieldwork

Move a reviewed draft into the correct collection channel without accidental publication or sending.

## Choose The Channel

- Hosted link: one reusable entry point for anonymous or metadata-driven access.
- LinkSet: a managed set of individual links, often linked to audience contacts or intended for export to another delivery channel.
- Embed: a modal placement on an approved website origin, backed by an eligible reusable share link.
- Email campaign: a Dayalogs-managed send to eligible audience contacts.

Explain the choice if the user's request could reasonably use more than one channel.

## Workflow

1. Read the current survey and confirm it is the intended version. Preview it before any public action.
2. Check collection dates, quota behavior, link metadata, audience rules, and survey compatibility for the chosen channel.
3. For audiences, use repeatable imports and inspect import status. Do not treat a transport error as proof that a chunk failed; verify the persisted import state before retrying.
4. Create or configure the channel:
   - Use share-link and LinkSet tools for hosted access and personalized links.
   - Use embed compatibility and embed tools for website placements. Restrict origins deliberately.
   - Use campaign tools for email. Preview the campaign and use `send_survey_campaign_test` before a real send when practical.
5. Ask for explicit confirmation immediately before each public or outbound action: starting collection, creating a real link when guarded, sending a campaign, retrying failed recipients, or another irreversible operation.
6. Start collection only after confirmation. Do not infer approval from the user asking for a preview, link design, or campaign draft.
7. Monitor the resulting channel. Use campaign events and campaign state for queued, sent, delivered, delayed, bounced, complaint, and failed counts.

## Delivery Rules

- Permanent email delivery failures exclude contacts from Dayalogs email campaign queues, but not from LinkSets or link exports that may be delivered through SMS, messaging, or offline channels.
- Explain excluded-recipient counts when a campaign audience is smaller than its source segment.
- Do not expose provider names as user-facing delivery statuses.
- Do not claim click tracking is active when `tracking_available` is false. Report click totals as unavailable, not zero.
- Campaigns freeze their survey version when the first real recipients are queued. Tests and unsent previews use the current version.

## Completion

Report what was created, whether collection is active, the concrete channel, audience and exclusion totals, and current delivery state. Include identifiers useful for later monitoring, but do not expose access tokens or secrets.
