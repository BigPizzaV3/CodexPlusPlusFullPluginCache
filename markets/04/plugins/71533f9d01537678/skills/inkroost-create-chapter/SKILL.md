---
name: inkroost-create-chapter
description: Plan, generate, review, finish, and optionally submit a chapter for any existing Inkroost comic, webtoon, or manga series. Use for requests such as a new chapter, next episode, another instalment, or revisions to a draft chapter.
---

# Create an Inkroost chapter

Author a complete chapter through Inkroost's MCP tools while preserving the series' established story, format, cast, visual continuity, accessibility text, and publication boundaries.

This workflow uses MCP tools, not a code sandbox. Discover tools through the client's normal MCP tool-discovery mechanism and call the exact actions named below.

## Ask only when the answer changes the work

Use the client's structured question tool when available; otherwise ask concise questions in chat. Ask no more than three related questions at once.

Resolve missing decisions only when they materially affect story or spend and cannot be inferred safely after loading the series context, such as an ambiguous target series or a required character the request leaves unclear. A broad request such as "make the next chapter" delegates unspecified premise, length, cast, and dialogue choices: derive them from the established series, propose them in the beat sheet, and avoid conducting an interview. Ask about moderation only when the user's publication intent is unclear.

Credit-charged generation needs informed approval. Before the first generation call, show the beat sheet, planned page count and variant count, call `estimate-generation-cost-tool`, and ask the user to approve the plan and estimated spend unless their request already explicitly approved that exact plan and spend. The estimate tool's `page_count` must be the total number of images requested (`story pages × variant_count`), not only the number of story pages. A client message such as "approval not received" is not a transient error: stop and ask the user rather than retrying around it.

## Resolve the series and its rules

1. Use `search-series-tool` or `list-series-tool` to resolve the user's series name. Never guess an ID; if several series match, show the matches and ask which one.
2. Call `get-story-state-tool`, `get-consistency-context-tool`, `get-chapters-tool`, `get-locations-tool`, and `get-props-tool` for the resolved series.
3. Determine the next unused chapter number, avoid title or premise repetition, and preserve reading direction, reading mode, maturity, established voices, style constraints, and any no-text rule.
4. Fix incomplete context before generation. Update weak character profiles and create missing location or prop sheets for recurring places/objects. Pass their IDs during generation and also use their names or aliases in scene text.
5. Call `check-balance-tool`, `estimate-generation-cost-tool`, and `get-daily-limit-status-tool` before proposing a generation plan.

## Plan before spending credits

Write a concise premise and page-by-page beat sheet. A normal chapter is 8–24 sequential pages, adjusted to the series and user request. It should establish one dramatic question early, escalate it through cause and effect, and pay it off or deliberately turn it on the final page.

Choose each page's panel count from the beat rather than using a fixed quota. Use structured `panels` for reliable layout: one panel for establishing images or reveals, two or three for a sustained beat, and more only when the exchange truly benefits from density. Stay within the live generation schema's panel and dialogue limits.

For every page plan, identify:

- the characters, location sheets, and prop sheets required;
- the camera/framing and emotional beat;
- continuity state carried from earlier pages;
- whether in-image text is allowed, and every exact dialogue line if it is;
- the alt text and transcript facts that must later match the final image.

## Create and generate

1. After plan/spend approval, call `create-chapter-tool` with the resolved `series_id`, next number, title, and a synopsis that includes the chapter's actual arc.
2. Generate with `generate-pages-batch-tool` where practical. Use `variant_count: 1` unless the user knowingly approves the extra cost of alternatives. Keep batches manageable and preserve their job-ID-to-page order.
3. Pass the `chapter_id` on every generation call. Pass the character, prop, and location IDs used by each beat.
4. Prefer structured `panels`. For a text-free series, set `allow_text: false` and explicitly prohibit bubbles, signs, labels, packaging text, screens, and background writing. For text-enabled pages, include only essential dialogue and explicitly prohibit unplanned writing.
5. Repeat critical continuity facts in each affected page, especially exact object counts, empty-state negative space, injuries, outfits, handedness, and the identity of recurring minor characters. Batch-level notes alone are not enough for premise-critical facts.

## Inspect, correct, and approve

1. Poll every job with `get-art-status-tool`. `processing` with no result URLs is normal; wait and poll again. Do not regenerate merely because one job finishes later than the others.
2. When a job reaches `review`, inspect the returned image or call `get-page-image-tool`. Verify composition, character identity, continuity, object counts, panel order, anatomy, and every rendered word.
3. If a page is wrong, refine only that beat and regenerate it. Repeated failure should lead to a simpler composition or a question to the user, not an unbounded retry loop.
4. Never claim visual verification when the client could not display the image. Explain the limitation and ask whether to hold the chapter or approve unseen.
5. Approve accepted jobs in ascending story order with `approve-pages-tool` or `batch-approve-pages-tool`. If approval order differs, call `reorder-pages-tool` with every current page ID exactly once.

## Add the readable text layer

After approval, call `set-page-text-tool` for every page, preferably in one bulk call:

- `alt_text`: one or two plain sentences describing the visible setting, characters, action, and important composition;
- `transcript`: the full reader-facing text version in the series' reading order, including scene description, visible characters, and exact dialogue.

Ground both fields in the inspected final image. Do not keyword-stuff, reuse one generic description, or describe elements the artwork does not show. This step is required even for silent chapters because it is the accessibility and discovery layer.

## Verify and optionally submit

1. Call `get-pages-tool` and check the complete sequence. Fix ordering if necessary.
2. Call `confirm-page-order-tool` with `confirmed: true` only after actually verifying the narrative order. Any later insert, delete, reorder, or new approval requires reconfirmation.
3. If the user explicitly asked to publish or submit, call exactly one of `publish-chapter-tool` or `submit-for-review-tool`. In Inkroost, this begins moderation; approved work can then become public. If submission intent is unclear, ask first.
4. Report the chapter ID, page count, text-layer completeness, order confirmation, generation failures/retries, and moderation status. Do not wait indefinitely for moderation unless the user asked you to monitor it.

## Revising a draft or rejected chapter

- Start with `get-pages-tool`; IDs remain stable while page numbers may move.
- Use `regenerate-page-tool` to replace one page in place when its beat remains valid.
- For a structural rewrite, use `delete-page-tool`, generate replacement beats, then `reorder-pages-tool`.
- Pages are locked while pending review or approved. If edits are unavailable, explain the state rather than attempting to bypass it.
- Regeneration spends credits; obtain approval for additional spend that was not part of the accepted plan.

The detailed platform and tool reference is available at https://inkroost.com/llms-full.txt.
