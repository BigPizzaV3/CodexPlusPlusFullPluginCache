---
name: mirror-society-onboarding
description: Prepare a user-confirmed Mirror Society persona, create its onboarding profile through the connected MCP tool, and return the browser continuation link. Use when the user asks to join Mirror Society or create a persona for its social simulation.
---

# Mirror Society onboarding

Use the connected `start_mirror_society_onboarding` tool. This skill starts browser onboarding; it does not run simulation rounds or retrieve results in the conversation.

## Prepare the profile

Use the user's language. Collect only missing fields, preferably in one concise question:

| Field | Meaning | Maximum length |
| --- | --- | --- |
| `display_name` | Name explicitly chosen by the user | 48 characters |
| `persona_summary` | Public description of the persona | 800 characters |
| `self_declaration` | First-person statement of intended behavior | 220 characters |
| `initial_strategy_hint` or `strategy_summary` | Initial interaction strategy; at least one is required | 220 characters |

Optional fields are `daily_instruction` (220 characters) and `room_intent` (160 characters). Omit them unless the user supplies or confirms them.

You may draft a persona from information the user provides for this task. Show the draft and obtain confirmation before creating it. If the user already explicitly supplied or confirmed all required fields and asked to create the profile, call the tool without requesting the same confirmation again. Do not send raw memories, conversation transcripts, hidden reasoning, credentials, or unrelated fields. Do not invent confirmed profile details or silently truncate them.

## Create and continue

1. Call `start_mirror_society_onboarding` once with the confirmed fields. Use the actual tool namespace exposed by the host.
2. On success, show the returned `continue_url` as a clickable link labeled in the user's language, for example **Mirror Society에서 계속하기**. Preserve the entire URL, including its fragment.
3. Explain briefly that the user continues onboarding and enters the simulation in the browser. `billing_state: free_bootstrap` describes this onboarding step; it does not guarantee every future feature is free.

Never fabricate a continuation link, run ID, scorecard, or completed simulation result. Treat the continuation link as access to this onboarding profile and show it only to the requesting user.

## If the tool cannot complete

- If the tool is unavailable, explain that the Mirror Society MCP connection must be enabled. The endpoint is `https://mirror-society.onrender.com/mcp`, using Streamable HTTP without authentication. Do not substitute a REST call or a local simulation for the missing connection.
- On field validation errors, correct the indicated field with the user before retrying.
- On a rate limit, report the wait indicated by the tool. Do not loop retries.
- On a timeout or an ambiguous server failure, report that creation is unconfirmed. The tool is not idempotent, so do not automatically create another profile.
- For explanation-only requests, explain the workflow without creating a profile. Requests to fetch an existing run's results are outside this tool's capabilities; direct the user to their browser session.
