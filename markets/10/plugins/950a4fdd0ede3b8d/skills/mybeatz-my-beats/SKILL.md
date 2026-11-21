---
name: mybeatz-my-beats
description: Find and open the connected user's MyBeatz beats, check their credit balance when requested, or follow a known existing generation without creating a replacement.
---

# Find and follow my MyBeatz beats

Use the bundled `mybeatz` MCP server. This is an account/library workflow, not a public artist catalogue lookup or a request to generate new audio.

- Use `list_my_beats` for the user's library, starting at page 1. Display returned titles, known style/BPM/key values, audio availability and `libraryUrl` links. Use the returned `nextPage` if more results are wanted; deduplicate beat IDs and stop at null. Do not call one page the complete library when more pages remain.
- Use `get_my_account` for an explicitly requested balance or plan check. Report the returned current values; do not estimate credits, change a subscription, purchase credits or expose credentials.
- For a generation already identified in the conversation, call `get_generation` with its actual `generationId`. Do not use a beat ID as a generation ID. The current library projection does not expose each beat's task ID: if no generation ID is available, show its known library/availability state or ask for the generation reference; do not invent one or claim to have queried the latest generation.
- Between status checks, wait at least `max(10, pollAfterSeconds)` seconds and respect Retry-After. Pending audio is not ready audio. Keep requested and measured BPM distinct; missing measurements remain unknown. Show returned refund information only if present.
- A “not found” response does not authorize probing guessed IDs, switching identities or accessing someone else's private beats. OAuth failures require the normal connection flow, not a password/token in chat. Stop repeated failures until the relevant blocker changes.

Never call `prepare_beat` or `create_beat` merely to populate an empty library, replace a pending/failed request, or demonstrate playback. An empty library is a valid result. Return concise factual status with the available MyBeatz links, in the user's language. Do not claim background monitoring, completed downloads or audio playback without evidence.
