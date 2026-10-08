---
name: looki-memory
description: Retrieve and search the user's captured Looki moments through the connected Looki MCP; use for a specific day or date range, chronological recaps, people, places, topics, past experiences, moment details, and captured photos or videos.
---

# Looki Memories

Use captured Looki moments as evidence for questions about the user's past. Route profile-only requests to `$looki-profile`, generated-content requests to `$looki-highlights`, and current-context requests to `$looki-realtime`.

## Choose the retrieval path

- For one known date, call `Looki:list_moments_on_date` with `YYYY-MM-DD`.
- For a date range, call `Looki:get_moments_calendar` first, then retrieve moments only for the relevant active dates.
- For a person, place, topic, event, or experience without a known date, call `Looki:search_moments` with one concise natural-language query and optional date bounds.
- For more context about a selected result, call `Looki:get_moment_detail` with its moment UUID.
- For captured photos, videos, locations, or media, identify the moment first and then call `Looki:get_moment_files`.

Use `Looki:get_user_profile` only when the user's timezone is required to resolve a relative date and is not already known.

## Date and recap workflow

1. Resolve the exact inclusive date or date range in the user's timezone.
2. Keep the range as narrow as the request permits.
3. Order retrieved moments by their returned start times.
4. Summarize activities, people, places, and transitions only when supported by the returned data.
5. For longer ranges, call out recurring themes only when multiple moments support them.

Do not treat a day without results as proof that nothing happened. Say that Looki returned no captured moments for that date.

## Search and detail workflow

1. Convert the request into one literal semantic query.
2. Add `start_date` and `end_date` only when the user gives or implies a bounded period.
3. Start with `page=1` and a small `page_size`.
4. Open only the most relevant result when its list summary is insufficient.
5. If several results are plausible, summarize the candidates and ask which one to inspect.

Preserve the returned timezone and distinguish capture time from dates mentioned inside the content.

## Captured media workflow

- Call `Looki:get_moment_files` only after identifying a moment.
- Use `highlight=true` first when the user asks for the best photos or clips.
- Continue pagination only until enough relevant media is found or `has_more` is `false`.
- Treat temporary media URLs as private. Do not reproduce or download them unless the request requires it.

## Example requests

- "Review what I did yesterday."
- "Which places did I visit last week?"
- "Find the memory where I had dinner with Alice."
- "Show me the best photos from that trip."

## Guardrails

- Use Looki MCP tools only. Do not read local credential files, request API keys, or call the legacy REST API.
- If Looki tools are unavailable, ask the user to enable the Looki plugin and complete OAuth.
- Retrieve the minimum personal context needed to answer the request.
- Do not expose unrelated people, locations, conversations, or personal details.
- Never claim an event occurred when no matching evidence was returned.
- The current MCP does not expose Looki journals. State that limitation when the user asks for diary or journal entries; do not invent a tool or fall back to the legacy REST API.

## Response style

- Lead with the recalled event, recap, or absence of a match.
- For one day, use a short overview followed by a chronological timeline.
- For a range, organize the answer by date and then summarize supported themes.
- Separate observations from interpretation and mention important coverage gaps.
