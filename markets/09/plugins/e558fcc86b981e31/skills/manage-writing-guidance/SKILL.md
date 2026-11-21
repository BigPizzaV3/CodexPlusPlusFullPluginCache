---
name: manage-writing-guidance
description: Use when the user wants to build or migrate a writing voice from skills, documents, URLs, samples or corrections, find writing inspirations, refine a company guide or named voice, review or restore history, archive a voice, or export saved instructions from BuyerTwin.
---

Use the connected workspace’s published writing guidance as authority. Resolve the company with `get_company_writing_guide`; resolve named voices using `list_named_voices` and stable IDs. Normal listings are active; request `lifecycle_status=all` or `archived` only when lifecycle management needs it. Never substitute company context for an unavailable requested person.

For style discovery, call `list_company_writing_styles` with user qualities, keywords and returned pagination. Users need not know author names. Show the real style/author, available qualities and annotated examples, distinguishing original demonstrations from sourced quotations. Respect `any`/`all` filter semantics and report no matches honestly. A requested author missing from the library is not a saved catalog record. Selecting multiple authors should preserve each author name, selected borrow/avoid qualities and blend direction.

For finished buyer-facing content, voice-only drafts or rewrites, use `create-buyer-content` and the shared retrieval reference below; for buyer knowledge mutation, use `update-buyer-knowledge`. These are different targets and workflows. This skill does not publish content or send messages.

Read [the proposal/apply and inheritance reference](references/writing-guidance-workflow.md) before any setup, correction, restore or lifecycle mutation. A request to brainstorm, draft or generate a sample is not persistent-update intent. Propose only the requested changes; show the exact immutable preview and apply only after authorization of that preview, using the matching proposal ID, hash and confirmation field. A proposal is not a saved guide. Respect collaborator read-only access; do not work around a denial with another tool.

For building a voice from supplied resources, read [resource-to-guide migration](references/resource-to-guide-migration.md). This covers existing skills as well as documents, URLs, writing samples and corrections; do not require the user to supply an author inspiration or a structured skill folder.

Before writing with an existing guide, read [using saved writing guidance](references/use-saved-writing-guidance.md). Resolve the requested target and channel, then use applicable guidance and example entries, not just the effective-instruction array. Private editing sessions, transcripts, pending proposals and unsaved samples are not shared guidance. A published illustrative example can inform writing without being an author-approved sample.

For portable instructions, call `get_writing_instructions_markdown` using the resolved target. Use `reference` for the all-channel guide, or `applied` for the requested channel (omitted means General). Return the actual Markdown and snapshot metadata; it is a static export, not an installed or automatically synchronized skill. Unknown targets and access denials must be reported, not silently replaced.

If required tools are missing from the connected catalog, explain the limitation and offer a read-only connection check. Do not fabricate tools, data or successful updates.
