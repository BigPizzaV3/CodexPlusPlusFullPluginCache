---
name: daoco-brand-context
description: Read and apply a personal or business brand's saved voice, audience, positioning, rules, and visual identity from Daoco, get the brief for one piece of work, save the person's standing rules, and export the brand. Use for brand questions, to ground the person's current work in their Daoco context, or to take the brand's files out of Daoco.
---

# Use brand context

Read [the shared Daoco workflow](../daoco-marketing/SKILL.md) for brand selection and tool boundaries. These reads use no workspace tokens.

## Read the brand

- `get_brand_context`: who the brand is: identity, summary, voice and tone, audience, positioning, colors, and typography. Its `sections` and `task` arguments are deprecated; use the reads below.
- `get_brief` with a `task` (the piece of work in a sentence) and optionally a `channel`: everything that applies to that work, in the order a writer weighs it. `rules` are the person's standing instructions and preferences, `voice` is the brand's learned voice, `whatsWorking` is what the brand's results show for that channel, and it adds the visual style, colors, logo, and matching passages. Where a rule and a What's working line disagree, the rule wins. Call it before writing anything for the brand.
- `get_brand_visuals`: the full visual identity, including the Daoco Looks and their example images.
- `list_brand_documents`: the brand's documents and shared files. `search_brand` finds passages in them or in brand images, and reads a document's full text by `documentId`.

If `get_brand_context` reports `setup`, the brand is still being set up; follow `daoco-brand-setup` instead of treating its context as complete.

## Apply it

For a personal brand, keep the person's stated expertise, point of view, audience, and voice. Do not invent credentials, experiences, endorsements, or first-person stories, and do not treat a belief Daoco inferred as one the person stated. When opinions, stories, audience, or positioning are thin, Daoco can interview the person: its `pov`, `beliefs`, `stories`, `audience`, and `positioning` workflows (by command where `run_workflow` is listed; otherwise ask in words, such as "interview me about what I believe on pricing"). A run asks its questions and ends; the person answers through `continue_work` on that thread, in their words. The result is a proposal the person reviews in Daoco. For a business, keep its offers, customers, positioning, and approved claims. Do not assume every personal brand is casual or every business says "we".

Answer the question rather than dumping every document. When the person asks how to write in their voice, pull the relevant traits from `get_brief` and show a short example, kept distinct from a saved rule. For a voice review, compare the text with the brief, point to specific phrases, and suggest a revision without changing supported claims. Distinguish saved facts from your suggestions; if a detail is missing, ask or name the gap. If documents conflict, prefer a clearly dated or designated current source, and ask when the choice matters.

Reading and advising here does not need a paid Daoco run. To change the saved brand, delegate through `start_work` and report the result: Daoco proposes brand changes for review in Daoco, and a proposal is not a saved change.

## Save the person's rules

When the person states a standing rule for the brand in their own words ("never use emojis in captions", "always link the pricing page"), offer to save it, then call `remember` with `kind` (instruction or preference), the rule as they said it, and `appliesTo` (writing, visuals, or all). Save only what the person said, never your own inference, a one-off request, or anything about approvals or permissions. `following` is `pending` until Daoco checks whether it is a rule for all future work; say so rather than promising it is followed everywhere. A rule the person tells Daoco directly always outranks one this app passed on.

`remember` works only after a workspace owner or admin turns on **May pass on what I tell it** for this app on Daoco's Assistants page, with the app's brand selected in that workspace. When it is refused, tell the person that, or suggest they tell Daoco the rule themselves. `forget` archives memories this app saved, by the `memoryId` `remember` returned. An app keeps at most 20 memories per brand.

## Use the brand outside Daoco

When the person writes copy, builds a page, or designs something in this app, apply the brand directly: `get_brief` for the work, `get_brand_visuals` for logo, colors, fonts, and reference images.

`export_brand` builds a zip of the brand: profile, summary, rules, documents, voice, Daoco Looks with examples, competitors, skills as `SKILL.md` folders, and library files. Connections, posts, threads, and analytics are left out. Only a workspace owner or admin can export. Call again while it builds; the download link works for a day. `create_brand` can set up a brand from an export's files.
