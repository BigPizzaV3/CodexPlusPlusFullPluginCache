---
name: artist-persona
description: Build reusable de-identified artist personas with vocal DNA, production world, lyric lens, and optional WizPrompt cloud save.
---

Use this skill when the user asks for an artist persona, vocal identity, sonic DNA, reusable character, or consistent voice for future songs.

Follow the Artist Persona template in `../../references/output-templates.md`.

Workflow:

1. Call `get_studio_guidance` with `workflow: "persona"` when the tool is available.
2. If the user asks to reuse existing work, call `get_creative_context`, `search`, or `fetch` when available before writing a variant.
3. Convert the user's references into de-identified traits. The final persona may describe vocal range, texture, delivery, phrasing, emotional posture, production palette, and lyric themes, but must not depend on naming a real artist.
4. Build the persona in four layers: vocal identity, technical delivery, emotional context, and sonic anchor.
5. Add a `Prompt Anchor` that can be reused in future style prompts without containing real artist names.
6. Make clear through wording that a WizPrompt persona is a reusable creative brief for continuity, not a native Suno persona and not a promise that Suno will recreate an identical voice.
7. If the user asks to save a new persona, call `create_persona` only after the draft is complete, supplying the approved name, genre, vocal signature, optional production/visual signatures, and an `idempotency_key`. Reuse the same key and identical approved payload for retries. Reopen it with `get_persona` using the returned ID. Map the reusable Prompt Anchor into the supported signature fields; do not claim an unsupported standalone field was stored.
8. If the user asks to change an existing persona, reopen the known owned record with `get_persona`, then call `update_persona` with its `persona_id` and only the approved changes. Signature objects replace the supplied signature, so preserve its unchanged fields. Reopen to verify the result.
9. Use `save_creative_brief` only for approved continuity decisions on a known project with `project_id`; it does not create or update a persona and accepts no `idempotency_key`. Confirm saved only after the appropriate tool returns success. If no persona save tool is available, explain that the draft exists in chat but has not been saved to WizPrompt.

Quality checks:

- The persona reads like a usable studio brief, not a label.
- Vocal traits include range, texture, delivery, phrasing, and processing.
- The sonic anchor is concise enough to reuse inside song prompts.
- The persona avoids identity claims, imitation promises, protected artist names in generation fields, and confusion with native Suno persona or voice features.
