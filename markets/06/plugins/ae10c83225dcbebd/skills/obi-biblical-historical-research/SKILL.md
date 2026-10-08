---
name: obi-biblical-historical-research
description: Produce or revise a sourced biblical and historical visual research brief for an Open Bible Images project. Use when Scripture, cultural context, geography, clothing, architecture, objects, customs, chronology, or a review finding must be investigated.
---

# OBI Biblical and Historical Research

Create research that helps a visual creator make responsible decisions. Read [references/evidence-framework.md](references/evidence-framework.md) before classifying claims and structuring the two research outputs.

When a canonical project JSON file is supplied, preserve all other sections, update only `research`, increment its artifact revision and the project revision, and append a history/capability-run entry. If no project file is supplied, label the result `unpersisted`.

## Workflow

1. Read the Scripture scope in context, image brief, source records, existing entities, draft composition, and the exact feedback/review finding that triggered this research when applicable.
2. Identify what the text explicitly states and what the image must visibly communicate.
3. Synthesize historical and archaeological evidence using linked source IDs.
4. Classify every material visual claim using the evidence framework.
5. Note source disagreements and plausible alternatives rather than forcing false agreement.
6. Translate findings into visual implications: required, preferred, optional, uncertain, or avoid.
7. List unanswered questions that would materially affect the image.
8. Save a 1,000–2,000-word full brief as `research.full_brief`. Derive an approximately 200-word shareable OBI summary as `research.public_summary`; it must not add claims absent from the full brief.
9. Record three to five material confidence notes as `High`, `Medium`, or `Low`, each with a brief explanation.
10. If the available evidence is not strong enough to resolve a material question, return disposition `needs_sources` with a focused source-search question instead of inventing certainty. If the research resolves feedback, link the revised claim and artifact revision back to that feedback/finding.
11. Return the concise summary by default and make the full saved brief available without pasting it into chat unless requested. Never mark either approved yourself.

## Loop behavior

- When invoked after Source Research, reassess only the affected claims plus any dependent visual implications; do not rewrite unrelated research merely because new sources exist.
- When invoked from Image Review, answer the focused review question first and state whether the finding is supported, weakened, disproven, or still inconclusive.
- When the conclusion requires a change upstream, return the earliest next capability: `needs_entity_revision`, `needs_composition_revision`, `needs_prompt_revision`, or `needs_human_decision`.
- Do not repeatedly request more sources when additional evidence is unlikely to resolve a genuinely disputed question; mark the uncertainty and stop.

## OBI constraints

- Favor historically and geographically grounded depictions over Westernized, fantasy, or decorative conventions.
- Do not add halos, fake writing, anachronistic objects, or certainty unsupported by evidence.
- Do not confuse later religious art with evidence for the depicted period.
- Do not let a visual preference alter what Scripture explicitly says.
- Clearly label creative recommendations as creative recommendations.

Research is ready for approval when important visual claims are sourced, classified, and understandable to a creator who has not read the sources.

## User-facing response

Lead with the approximately 200-word public summary or, for a focused feedback investigation, the direct answer to that question. Add no more than three material uncertainties or decisions. When evidence is insufficient, end with a compact **Find more sources** recommendation and the precise question to research. Do not narrate the research process or reproduce the full brief unless the user asks for it.
