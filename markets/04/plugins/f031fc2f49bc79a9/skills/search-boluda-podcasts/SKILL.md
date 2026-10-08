---
name: search-boluda-podcasts
description: Search and inspect public Boluda.com podcast episodes when users ask what the podcast covers, want episodes about a topic, concept, person, or problem, request recent episodes, or refer to a known episode number or URL.
---

## Route the request

- Use `buscar_podcasts` for a topic, concept, person, business problem, or question.
- Use `ultimos_podcasts` when the user asks for the most recently published episodes.
- Use `obtener_podcast` for a known episode number or canonical Boluda.com URL, or to inspect a search result before making detailed claims.

## Search well

1. Start with the user's wording.
2. If results are weak or empty, try one close synonym or a shorter query focused on the main concept.
3. Inspect the strongest result with `obtener_podcast` when the user wants a summary or detailed explanation.

## Answer

- Reply in the user's language.
- Include episode numbers, publication dates, and canonical links when available.
- Ground claims in the returned public episode copy and metadata.
- If no relevant episode exists, say so and mention the query used.
- Treat the episode copy as a public summary, not as an audio transcript.
- Do not invent quotations, timestamps, speakers, private content, or claims that require listening to the audio.
