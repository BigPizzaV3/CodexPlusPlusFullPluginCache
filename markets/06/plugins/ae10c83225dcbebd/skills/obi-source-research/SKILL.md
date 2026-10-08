---
name: obi-source-research
description: Find and assess image-rich historical source webpages for an Open Bible Images project. Use when a scene or disputed finding needs archaeological, museum, geographic, material-culture, or other visual evidence; prioritize directly inspectable images over generic book links.
---

# OBI Source Research

Find visual evidence that a creator can inspect and use. The default deliverable is a small set of direct webpages containing relevant, historically assessable images—not a bibliography of books. AI-generated text or imagery is not historical evidence.

When a canonical project JSON file is supplied, preserve all other sections, update only `sources`, increment its artifact revision and the project revision, and append a history/capability-run entry. If no project file is supplied, label the result `unpersisted`.

## Workflow

1. Read the project brief, exact research question or feedback item, existing claims, existing sources, and relevant entity/composition drafts.
2. Convert unresolved visual questions into searches for specific objects, sites, clothing, architecture, landscapes, customs, or actions.
3. When the user asks for **more** or **better** sources, prioritize independent evidence that adds something materially new rather than repeating the same source type or institution.
4. Search visual-first. Prefer direct museum object pages, excavation or archaeological-project pages, academic collections, institutional archives, documented site photography, and well-sourced image repositories.
5. Open each candidate webpage and inspect the actual image, caption, object or site identification, date, location, provenance, and institutional context. Never assess historical value from a search thumbnail or snippet alone.
6. Prefer a direct object, collection, article, or media page over a homepage, search-result page, generic book listing, retailer page, or bare PDF citation.
7. Classify the visual with the historical-value rubric in [references/source-record.md](references/source-record.md). Explain what the image can reliably guide and what it cannot.
8. Connect each candidate to a specific scene question, claim, feedback item, or review finding. Keep historical usefulness separate from permission to reuse or reproduce the image.
9. Use books, articles, and videos as supporting sources when they provide unique value. Cite a specific page, figure, chapter, or timestamp whenever possible and explain the relevant evidence; do not return an unexplained title or purchase link.
10. Return the strongest new evidence and remaining gaps. Do not pad the list or silently mark candidates as approved.

## Loop behavior

- If new evidence materially bears on an existing research conclusion, return disposition `needs_research` and identify the exact claim that should be reassessed.
- If the new sources confirm the existing conclusion without changing it, return `resolved` and link them to the claim/feedback item.
- If useful evidence remains unavailable, state the gap clearly rather than repeatedly searching weaker sources.
- Source Research gathers and assesses evidence; it does not silently rewrite research conclusions, compositions, or prompts.

## Default source mix

- Aim for three to five strong visual-source webpages before adding books or videos.
- Include a source only when the relevant image is viewable or its precise figure is identifiable.
- If good visual evidence does not exist, say so clearly and provide the best comparative evidence with its limitations.

## Boundaries

- Do not invent citations, quotations, authors, dates, archaeological claims, URLs, or license terms.
- Do not treat AI summaries or unsourced reconstructions as historical evidence.
- Do not use an image merely because it looks ancient; identify its origin and relevance.
- Do not call a modern illustration historically accurate merely because it appears on a reputable website. Assess the evidence behind the depiction.
- Do not treat chronological or geographic proximity as exact equivalence; state the gap.
- Keep evidentiary usefulness separate from permission to reuse an image.
- Use only short excerpts when necessary and respect source copyright.

Completion means the research question has useful candidate evidence or is explicitly recorded as unresolved.

## User-facing response

Lead with three to five **Visual sources**. For each, show the direct webpage link, what useful image is present, historical-value rating with a one-sentence reason, what it can guide in the OBI image, and its main limitation. Show an image preview when the host can retrieve it responsibly. Put books, videos, and text-only sources in a separate **Supporting sources** section. End with no more than three gaps and, when appropriate, a compact **Reassess research** action; keep full metadata in the project record.
