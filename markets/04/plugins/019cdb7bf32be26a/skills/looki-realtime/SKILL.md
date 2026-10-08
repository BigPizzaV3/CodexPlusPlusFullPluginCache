---
name: looki-realtime
description: Check the latest realtime event detected by the user's Looki device through the connected Looki MCP; use when the user asks what is happening now or requests immediate context from proactive mode.
---

# Looki Realtime

Use the latest realtime Looki event only for explicit current-context requests. This capability is beta and depends on proactive mode being enabled in the Looki app.

## Workflow

1. Call `Looki:get_latest_realtime_event` once.
2. If it returns an event, summarize its description, time range, timezone, and location only as needed.
3. If it returns `null`, explain that Looki has no recent realtime event or proactive mode may be unavailable.
4. If the user needs historical context, route the request to `$looki-memory`.

## Example requests

- "What is happening around me right now?"
- "Check the latest realtime event detected by Looki."
- "Based on my latest Looki event, what may be happening around me?"

## Guardrails

- Use Looki MCP tools only; authentication is provided by the connected OAuth session.
- Do not repeatedly poll unless the user explicitly asks to monitor.
- Do not claim that an event is still occurring after its returned end time.
- Treat realtime location and activity as highly sensitive.
- Do not infer safety, health, intent, or identity beyond the returned event description.
- If the tool is unavailable, ask the user to connect Looki and enable proactive mode; do not request API credentials.

## Response style

- Lead with the latest returned event or the absence of one.
- Include the event time and location only when they are relevant.
- Make uncertainty explicit, especially when the event has already ended.
