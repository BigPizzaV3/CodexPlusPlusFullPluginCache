---
name: raqim-workflow
description: Use when the user asks to create, format, validate, or share a Raqim research board or flashcard deck from conversation content.
---

# Raqim workflow

Use the Raqim MCP server to turn material already present in the conversation into a Raqim board or flashcard deck.

## Choose the export type

- Use a **board** for research notes, quotations, citations, arguments, timelines, comparisons, and connected concepts.
- Use **flashcards** when the user wants active-recall study cards.
- If the user has not specified and the intended output is unclear, ask one concise question.

## Mandatory export sequence

1. Call `raqim_export_spec` with the correct `kind` before constructing any Raqim JSON. Treat its returned contract as authoritative for every item/card field and source rule.
2. Build the JSON only from information actually present in the conversation or retrieved through connected research tools. Never invent Arabic passages, quotations, page numbers, book IDs, narrator details, or citations.
3. Keep verbatim quotations exact. Do not use ellipses inside a quotation. Distinguish paraphrase, inference, and direct quotation.
4. Do not claim a source was checked unless a source-reading or verification tool actually checked it. If a source cannot be checked, mark it unverified exactly as the export contract requires and state that limitation plainly.
5. Call `raqim_validate` with the complete export before sharing. Fix every reported error and revalidate. Treat warnings carefully; do not silently invent missing source details to clear them.
6. Call `raqim_share` with the validated complete JSON. Only report success and provide a share URL if the tool returns one.
7. In the final answer, provide both the Raqim link and the complete JSON in one fenced code block. State how many citations remain unverified; do not imply that Raqim's shape validator checks factual accuracy.

## Verification boundaries

The Raqim chat server is an export and sharing service, not a searchable book library. Its quotation and isnad verification endpoints may return `unverifiable` because this server has no Shamela corpus. Do not present an `unverifiable` response as a successful check. For actual book lookup, page inspection, quotation verification, narrator research, or translation, use a separately connected Maktabah/Shamela research service and cite the material it returns.

## Good output practice

- Preserve the user's requested language; use Malaysian Malay when the user writes in Malay.
- Keep Arabic text readable and accurately vocalized only when the source provides it.
- Include full bibliographic details only when actually available.
- Separate established source evidence from the assistant's explanation or synthesis.
- Prefer a concise title that accurately describes the board or deck.
