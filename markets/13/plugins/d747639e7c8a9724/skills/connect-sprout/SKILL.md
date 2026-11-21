---
name: connect-sprout
description: Connect a Sprout account, inspect its connection, or set up a first Sprout project. Use when the user installs Sprout, asks to connect or reconnect it, or needs account setup before building an app.
---

Use the Sprout MCP tools for account setup. Preserve the user's existing request and authorization; installation alone does not authorize creating an app or sending email.

1. Call `get_sprout_session`. If connected, use the returned apps or `list_apps` to identify the requested app. A setup-only request ends with the connection status and a useful next step. Do not create a demonstration project automatically.
2. For an existing account, call `connect_sprout` and let the client's OAuth interface handle sign-in and consent. Resume the original task after connection. Do not request passwords, tokens, or cookies in chat.
3. For a requested first project, obtain the user's email and agreed project title if missing. Explain that `start_onboarding` sends a confirmation email and that confirming creates the app. Use private visibility unless the user requested public access. Call once, preserve the returned `onboardingId`, and show the non-secret `launchUrl`.
4. After the owner confirms, call `complete_onboarding` with the same ID. `awaiting_email_verification` is still pending. An expired grant or lost session after confirmation requires `connect_sprout`, not another project request.

If delivery reports `emailSent: false`, explain the failure and make at most one retry with the same details. Stop on rate limiting, using the latest confirmation message or the returning-user connection path. Do not poll repeatedly while waiting for the human.

If the tools are unavailable, explain that the Sprout plugin must be enabled or connected in this client. Do not fabricate a connection, use a pasted bearer token, or silently install a CLI as a substitute.

Return only the connection status, relevant app choices, and any specific user action still required. Keep private completion material and credential values inside the connection flow. Account restrictions remain enforced by Sprout; report a limit without attempting to evade it or soliciting a purchase.
