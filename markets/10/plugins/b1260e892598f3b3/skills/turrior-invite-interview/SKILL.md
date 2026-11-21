---
name: turrior-invite-interview
description: Invite a Turrior candidate to a Calendly interview when the user asks to schedule or send an interview invitation.
---

Use this skill when the user wants to invite a candidate to an interview.

1. Resolve the candidate and obtain their current application `interactionId`. Raw invitations cannot be used.
2. Call `get-calendly-event-types` before sending the invitation.
3. If the user named an interview type, select the closest matching Google Meet event type.
4. If no type was specified, use the first suitable event type.
5. If no Google Meet event type exists, tell the user that Calendly needs a suitable Google Meet event type configured.
6. Call `invite-candidate-to-interview` using the application `interactionId` and selected event URI.
7. If the MCP response reports `calendlyUnauthorized`, tell the user that their Calendly account needs to be reconnected.
