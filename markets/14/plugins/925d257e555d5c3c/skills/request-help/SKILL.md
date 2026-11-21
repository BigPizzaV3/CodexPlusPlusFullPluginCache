---
name: request-help
description: Send a user-approved request to Solder when the user wants a human to follow up about component questions, board design, or review services.
---

Use `request_help` only when the user wants Solder to contact them. Ask for their email address if they have not provided it. Draft a concise, accurate description of the issue or requested service using only relevant details the user has chosen to share. Show the exact email address and message to the user, explain that both will be sent to Solder so the team can follow up, and let them edit the message. Ask the user to explicitly confirm sending those exact details before calling the tool. If the user has already expressly authorized sending the same email and message, that confirmation is sufficient.

After confirmation, create a distinct UUID `requestId` for the approved submission. Call `request_help` with that `requestId`, the confirmed `email` and `issue`, and `consent: true`. Reuse the same `requestId` for retries of the same submission; create a new UUID for a new approved submission. Never ask the user for this ID. If the user changes either field, obtain confirmation of the changed details before sending. Do not send unrelated conversation history, secrets, or confidential details the user has not approved. Do not solicit a request merely because the user asked a technical question.

When the tool reports `accepted`, explain that the email provider accepted the request for delivery; do not guarantee receipt. If the tool fails, explain that acceptance was not confirmed and let the user decide whether to retry. Do not promise a response time or claim Solder has reviewed the request.
