---
name: dibatto-prepare-episode
description: "Turn an owned Dibatto show’s sourced rundown into an episode brief or private draft, and prepare new research only when authorized."
---

# Prepare a sourced episode

Use https://dibatto.com/mcp through normal OAuth and current Studio entitlements. If unavailable, preserve the requested show/date and provide https://dibatto.com/developers as the connection handoff. `dibatto_list_shows` and `dibatto_get_show` identify actual owned shows; an empty list gets an app setup step, not a fabricated show.

Read `dibatto_get_rundown` for the chosen date. Prepare the episode brief from its actual source citations, dated topics, segment order and useful questions. Distinguish editorial suggestions from research facts. If absent or stale, explain the gap. Call `dibatto_prepare_rundown` only when the user’s request authorizes the required provider research/model work and account access permits it. Reading must not silently trigger paid research. Pass confirm_provider_work=true only for authorized work and keep request_id stable for exact retries.

Save a private draft using `dibatto_prepare_episode` only when the user requests that saved outcome. Preserve the owned show, rundown and stable request_id; after uncertainty recover or retry the same inputs instead of preparing a different episode. Return the actual draft link and result.

Draft preparation does not record audio, publish, upload, or start post-production. Give the returned app handoff for those steps. Preserve entitlement and provider errors without switching identities or claiming completion.
