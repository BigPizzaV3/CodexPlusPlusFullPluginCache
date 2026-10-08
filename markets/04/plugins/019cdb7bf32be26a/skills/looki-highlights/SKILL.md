---
name: looki-highlights
description: Browse the user's AI-generated Looki highlights through the connected Looki MCP; use for generated vlogs, creative recaps, liked highlights, and questions about what is new in the user's Looki feed.
---

# Looki Highlights

Retrieve AI-generated highlights created from the user's memories. Keep this workflow separate from raw captured moments: use `$looki-memory` when the user asks what actually happened on a date or wants a specific captured memory.

## Quick start

1. Call `Looki:list_for_you_items` with the narrowest filters supported by the request.
2. Use `group=all` unless the user explicitly asks for `vlog` or `other`.
3. Filter by `recorded_from` and `recorded_to` when the user refers to when an experience happened.
4. Filter by `created_from` and `created_to` when the user refers to when a highlight was generated.
5. Continue pagination only when the user requests a complete list or the first page cannot answer the question.

## Example requests

- "Show my latest Looki vlogs."
- "What is new in my Looki highlights?"
- "Find the creative recaps generated from last month's memories."
- "Show the highlights I liked."

## Guardrails

- Use Looki MCP tools only; authentication is provided by the connected OAuth session.
- If Looki tools are unavailable, ask the user to enable the Looki plugin and complete OAuth.
- Do not describe generated content as a complete or authoritative record of the user's day.
- Preserve the distinction between `recorded_at` and `created_at`.
- Treat titles, descriptions, cover images, and media URLs as private personal data.
- Do not reproduce or download temporary media URLs unless the user's request requires the media.

## Response style

- Lead with the most relevant generated highlights.
- Include the highlight type and recording date when they help disambiguate the result.
- Separate the highlight's generated description from any inference you add.
- State when no matching highlight was returned.
