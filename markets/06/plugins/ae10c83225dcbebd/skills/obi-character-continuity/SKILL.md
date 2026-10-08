---
name: obi-character-continuity
description: Create, preserve, review, or revise a reusable Open Bible Images character identity and its scene-specific appearances. Use for biblical character profiles, reference-based identity matching, continuity problems, life-stage variants, portraits, character sheets, or feedback that a person no longer looks like the same character.
---

# OBI Character Continuity

Create one stable, historically plausible identity that can persist across scenes while allowing age, clothing, health, and circumstances to change. Use [references/character-record.md](references/character-record.md) for stored data and [references/character-creation.md](references/character-creation.md) when creating a new character.

When a canonical project JSON file is supplied, preserve all other sections, update only `characters`, increment its artifact revision and the project revision, and append a history/capability-run entry. If revision was triggered by feedback or review, link the new character revision back to that finding. If no project file is supplied, label the result `unpersisted`.

## Workflow

1. Read the entity set, chronology, research, composition, current images, and existing portrayal, variant, appearance, and reference records.
2. When continuity feedback is supplied, compare the current image against the approved or intended portrayal before proposing a new identity.
3. Prefer an approved portrayal when the same character already exists.
4. Determine scene-specific age, grooming, clothing, health, emotion, occupation, and environmental condition supported by the project.
5. Separate enduring identity traits from changeable appearance traits.
6. Select approved references and state what each controls: identity, clothing, pose, expression, or style.
7. If no portrayal exists, create a short character summary, reusable identity specification, structured JSON, and reference-image plan using the character-creation contract.
8. If feedback reveals that the reusable portrayal itself needs improvement, preserve the prior version and propose a revised portrayal rather than silently replacing history. Note which existing generations may be affected; do not reopen or regenerate them automatically.
9. If the user explicitly requests image generation, preserve the same face, age, body proportions, and core clothing across outputs. Default to one square character sheet; generate the full four-image package—portrait, full body, action shot, and character sheet—only when the user requests the full package.
10. Preserve the exact prompt and references for every generated candidate. Return conflicts and required human decisions.
11. If the revised character changes what the current image prompt should say, return disposition `needs_prompt_revision`.

## Boundaries

- Do not replace an approved visual identity merely because another face is aesthetically preferable.
- Do not infer ethnicity, age, status, or physical traits beyond Scripture and responsible historical context without labeling the choice.
- Do not let a pose or clothing reference unintentionally redefine identity.
- Do not approve or publish a generated character sheet.
- Do not automatically regenerate earlier images when a portrayal improves; identify affected work for human choice.
- Avoid glamour, fashion photography, fantasy styling, modern grooming, airbrushed skin, and medieval or Renaissance costume conventions.

Completion means the Prompt Generator can unambiguously select the correct character identity and scene appearance, and continuity feedback has a traceable resolution or human decision.

## User-facing response

For a new character, show the concise profile and reusable identity specification first, then the JSON in a code block. If images were explicitly requested, show them with the exact prompt used. For established characters or feedback-driven revisions, show the selected portrayal, what changed or was preserved, material continuity conflicts, and a compact **Revise prompt** action when downstream prompt work is needed.
