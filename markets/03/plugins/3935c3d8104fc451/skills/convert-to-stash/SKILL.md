---
name: convert-to-stash
description: Use when the prompt contains /convert-to-stash, or the user explicitly asks to convert an existing answer or conversation into reviewable native Stashiro cards.
---

# Convert conversation content to Stashiro

The literal `/convert-to-stash` token converts content already present in the conversation. It does not request new research, search saved Stashiro content, or authorize saving.

1. When the user sends `/convert-to-stash`, immediately call `present_stashiro_cards` with useful completed content from the conversation. If the command asks for a specific focus or identifies a message or range, answer that request from the existing conversation. Otherwise produce a concise answer-shaped summary of the conversation, using the latest substantive completed answer as the primary source. Do not repeat the analysis outside the tool, browse the web, call `search`, or add facts. If no substantive prior content exists, ask which content to convert.
2. Build ordered `sections` so the result reads as one coherent answer. Give each section only the heading and connecting prose it needs, then place the relevant zero-based `cardIndexes` directly after that prose. Use every card index exactly once. Do not repeat full card details in the prose.
3. Preserve the source content and its organizing axis. Keep an ordinary note under 60 words and about one subject; split independent facts, resources, decisions, or actions. Create each source link in the same section, immediately with the item it supports, rather than batching links after notes. Use a table or chart for structured comparisons, a map only when coordinates exist, a flight only when its required details exist, and an image only for supplied files. When a specialized card lacks required data, use a note or table instead of researching or inventing it.
4. Pass `preferredBoardId` only when the destination is known. Use returned Spaces to suggest a clearly relevant destination, or suggest a new Space name when none fits.
5. Call `save_capture` only with the exact board, cards, and sections confirmed in the capture UI. Reuse its payload and a stable `requestId` so retries remain idempotent and semantic groups survive saving.
6. Report `savedCount`, the destination board name, and the exact `boardUrl`. Do not expose temporary image download URLs or internal file identifiers.
