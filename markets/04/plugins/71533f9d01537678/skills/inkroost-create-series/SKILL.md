---
name: inkroost-create-series
description: Create and prepare a new comic, webtoon, or manga series through the Inkroost MCP. Use when a user asks to start, set up, design, or create a new Inkroost series; do not use for adding a chapter to an existing series.
---

# Create an Inkroost series

Build a usable series foundation through Inkroost's MCP tools. The result should be a private series with a complete visual profile and enough character, location, and prop context to generate consistent chapters later.

This workflow uses MCP tools, not a code sandbox. Discover the connected Inkroost tools through the client's normal tool-discovery mechanism and use the exact action names below.

## Clarify only material gaps

Use the client's structured question tool when one is available; otherwise ask concise questions in chat. Group related questions and ask no more than three at a time.

Before creating records, establish these decisions when the user has not already supplied or delegated them:

- working title and one-paragraph premise;
- comic format: paged comic/manga or vertical webtoon, plus LTR or RTL panel order;
- intended audience and deliberate maturity rating (`all_ages`, `teen`, or `mature`);
- tone, genre, visual style, colour treatment, and major constraints;
- named lead characters and the recurring places or objects central to the premise.

Do not make the user choose details they explicitly asked the assistant to invent. If several materially different directions remain plausible, present two or three short options and ask which one they prefer. If the assistant had to infer important creative choices, summarize the proposed series blueprint before creating it.

## Workflow

1. Call `search-series-tool` with the proposed title to detect a likely duplicate. If a close match exists, show it and ask whether to continue with a distinct new series.
2. Read the live `create-series-tool` schema before calling it. Its `genre_ids` description contains the valid genre catalogue; never guess a genre ID.
3. Call `create-series-tool` with a strong synopsis, deliberate maturity rating, reading direction, and reading mode. Keep the returned `series_id`.
4. Immediately call `set-series-style-profile-tool`. Fill all four groups with concrete visual instructions:
   - `subject`: the series-wide human/creature rendering baseline;
   - `photography`: medium, linework, shading, framing, lens/camera tendencies, and composition;
   - `background`: recurring environment language, atmosphere, lighting, and time-of-day defaults;
   - `constraints`: palette, logo/text restrictions, anatomy or continuity constraints, and other hard rules.
5. For every named character, call `create-character-tool`, then `set-character-style-profile-tool`. Record reproducible traits rather than adjectives: build, age range, hair length/colour/parting, eye shape/colour, distinguishing marks, default outfit, posture, and expression range.
6. Create a `create-location-tool` sheet for each recurring place whose geometry matters. Include aliases used in story beats, concrete measurements/counts/relative positions, materials, and continuity rules.
7. Create a `create-prop-tool` sheet for each recurring object with a describable shape. Include aliases, concrete appearance notes, continuity rules, and either a supported `looks_like` key or a brand-free `real_world_model_anchor`. One-off objects do not need sheets.
8. Call `get-consistency-context-tool`. Fix incomplete profiles or sheets before declaring the foundation ready.
9. Return a concise summary with the series ID, character IDs, location IDs, prop IDs, format, maturity rating, and any intentionally deferred work.

## Boundaries

- Creating the requested private foundation is within a clear request to create a series. Do not generate credit-charged art unless the user also asks for it and approves the spend.
- Do not accept the content policy or choose a maturity rating on the user's behalf when the user has not delegated that creative decision.
- Do not submit or publish the series as part of setup unless the user explicitly asks. Publication begins a moderation workflow and can make approved work public.
- When the user wants the first chapter, continue with the `inkroost-create-chapter` workflow rather than improvising a shorter path.

The detailed platform and tool reference is available at https://inkroost.com/llms-full.txt.
