# OBI capability routing and feedback loops

The user asks for an outcome; the Image Project front door chooses the lightest specialist work that can achieve it. A capability is the user-facing action. Specialist skills provide the method. Host tools perform concrete actions such as web research or image generation.

## Manual calls always work

When the user explicitly names a capability or specialist, follow that choice unless it is impossible or would violate a human-decision boundary. Do not replace an explicit request with a different workflow merely because another route seems preferable.

Common manual phrases:

| User asks for | Capability | Primary specialist |
| --- | --- | --- |
| “Research this” / “check the history” | `research_context` | `$obi-biblical-historical-research` |
| “Find more/better sources” | `find_sources` | `$obi-source-research` |
| “Identify/define the people, place, or object” | `define_entities` | `$obi-entities` |
| “Revise the scene/composition” | `revise_composition` | `$obi-composition` |
| “Fix/compare this character” | `character_continuity` | `$obi-character-continuity` |
| “Write/update the image prompt” | `build_prompt` | `$obi-prompt-generator` |
| “Generate/render/revise the image” | `generate_draft` | `$obi-image-generator` |
| “Review/check this image” | `review_image` | `$obi-image-review` |

The user may also name the specialist directly. Treat “use Source Research” and “find more sources” as equivalent manual routing.

## Automatic routing

When the user does not name a capability, infer it from the requested outcome and current project state. Prefer one useful action over asking the user which specialist to call.

A plain request may require several specialist hops. Continue automatically when the next hop is evidence-gathering or analysis needed to complete the user’s stated goal. Stop before image generation unless the user explicitly requested an image, and stop before approval, publication, canonicalization, or other human decisions.

Examples:

- “This image seems off; review it and figure out why.” → `review_image`; if a scored finding needs evidence, route to `research_context` and, if evidence is insufficient, `find_sources`; then return to the review finding.
- “I don’t trust that conclusion; find stronger evidence.” → `find_sources`; if useful new evidence is found, rerun `research_context` on the affected claim.
- “Peter does not look like the same person.” → `review_image` or `character_continuity` depending on whether an actual image is supplied; update the character proposal before revising the prompt.
- “Fix the image.” → identify the earliest responsible artifact first, revise that artifact, rebuild the prompt if necessary, and generate only because the user explicitly asked to fix the image.

## Route problems to the earliest responsible artifact

Do not patch the final prompt or image when an upstream artifact is wrong.

| Finding origin | Route back to |
| --- | --- |
| weak or missing evidence | `research_context` or `find_sources` |
| wrong/missing person, place, object identity | `define_entities` |
| character identity/age/clothing continuity | `character_continuity` |
| wrong narrative moment, count, placement, action, camera, setting | `revise_composition` |
| correct project facts translated poorly into image instructions | `build_prompt` |
| anatomy, text artifact, rendering defect, or model failure with correct prompt | `generate_draft` |
| genuinely disputed interpretation or approval question | human/consultant decision |

## Feedback as a trigger

Treat comments from the user, collaborators, consultants, external reviewers, or prior review findings as feedback attached to a target artifact or image. Preserve who said it and what it targeted. Feedback does not become fact merely because a reviewer stated it.

For each material feedback item record:

- stable `feedback_id`
- source (`user`, `creator`, `consultant`, `external_reviewer`, `image_review`, or `other`)
- target artifact/image and region when known
- original comment
- status (`open`, `investigating`, `resolved`, `dismissed`, or `needs_human_decision`)
- inferred root-cause artifact when known
- next capability
- capability-run IDs and resulting artifact revisions
- resolution note

A feedback item may re-open earlier work without erasing approved history. New revisions supersede older working versions; they do not rewrite history.

## Loop behavior

A capability may return one of these dispositions:

- `resolved` — the user’s question is answered or the proposal is ready for human consideration.
- `needs_sources` — invoke `find_sources` when stronger evidence can materially answer the question.
- `needs_research` — invoke `research_context` with the focused unresolved question.
- `needs_entity_revision` — invoke `define_entities` or `character_continuity`.
- `needs_composition_revision` — invoke `revise_composition`.
- `needs_prompt_revision` — invoke `build_prompt`.
- `needs_generation` — generate only when the user explicitly requested generation/revision.
- `needs_human_decision` — stop and present the decision clearly.

After a follow-up capability completes, return to the originating feedback/finding and update its disposition. Do not loop indefinitely. Stop when the issue is resolved, evidence remains genuinely inconclusive, the next step needs a human decision, or the next step would require generation the user did not request.

## User-facing behavior

Keep routing quiet. Do not narrate “I am invoking Skill A then Skill B” unless the user asks. Show the useful result, material unresolved decisions, and compact actions such as **Research this**, **Find more sources**, **Revise composition**, **Update character**, **Revise prompt**, or **Generate revision** when a manual next step would be useful.
