---
name: trustcloud-lp-blueprint
description: "Use when an external MCP client authors, reviews, saves, or patches a Homin Cloud event LP while preserving facts, booking behavior, and publication boundaries."
---

# External LP blueprint workflow

Shared references provide business knowledge. Runtime, UI, tool, or save examples
inside them describe the internal surface and must not be executed as written.
Follow this external workflow, the current live contract, and its confirmation
requirements.

Read the event/LP context and canonical schema before authoring. Preserve supplied
facts, existing block IDs, reservation calendar bindings, booking windows, and
unknown values. Omit unsupported claims instead of filling gaps. The MCP client
must author the copy and structured LP; Homin Cloud validates and persists it.

Build a decision path from the event promise through evidence, participation or
visit details, reservation conditions, and a final CTA. Adapt the structure to the
actual evidence. Do not force a fixed block count, duplicate a source fact across
several sections, or turn distinct features into an invented process. Use a
faithful edit/composite only when the image tool receives the source pixels. For
a new LP prefer a verified text-bearing source-based hero unless original-only,
no-generation or editable-overlay input takes precedence.

On native MCP, use `events.lp.schema.get`, `events.lp.context.get`, and the
preview/apply modes of `events.lp.draft.update` or `events.lp.draft.patch`. Read back
the saved context, verify the persisted version, and run `events.lp.draft.review`.
On ChatGPT Apps, author the dedicated proposal payload and use the immutable
prepare, review, apply, and status sequence described by the event interview skill.

Treat save and publish as separate outcomes. A saved draft must remain unpublished
unless the user expressly requests publication and the publish prerequisites pass.
Never report completion from a preview, schema validation, or successful save alone.

Use selective references for the complete block catalog and premium housing
guidance. These references guide composition; the live schema and current event
context remain authoritative for accepted fields and facts.


## Shared LP color settings

Read the current document theme before editing. The native form/calendar colors are
stored in theme.colorOverrides, an optional map with page, surface, input,
selection, action, error, and success. Each override is a pair:
{"background":"#161b27","foreground":"#fafafa"} (lowercase six-digit hex).
Missing or null roles use automatic colors derived from the background and accent.
Explicit pairs are preserved; low contrast is advisory and never a draft-save gate.
Use 4.5:1 for normal text and 3:1 for necessary state indicators. Check rendered
hover/focus/selected/error states, not just CSS declarations.

Use the existing LP read/context operation and update_theme semantic patch. Preserve
other roles when setting colorOverrides (the map replaces the previous map).
Set one role to null to restore that role; unset colorOverrides to restore all.
Keep expected_updated_at, preview/commit, authorization and idempotency safeguards.
Get the current canonical schema/reference tool when the argument shape is unclear;
reference retrieval is available throughout editing and is not a prerequisite.
Free-design HTML lives in a separate frame; apply matching colors in its authored
CSS when needed. Native UI settings do not rewrite free-design HTML or photographs.

# Canonical domain guidance

# Shared LP business quality rules

These rules apply to both the Homin Cloud internal assistant and external MCP
clients. Transport-specific tool names and save mechanics do not change them.

- Choose useful visual roles and visitor decision material from confirmed source
  facts. Do not require fixed image counts, value-point counts, chapter counts or
  FAQ invented only to fill a structure. Keep advertised activities, organizer,
  conditions, practical details, source testimonials and the real booking flow.
  Restore compressed PDF photos from their original pixels without inventing
  subject details. Respect image-free, no-generation and original-only input.
  The client decides whether to publish; include disclosures only when requested.
  Never invent reviews, performance, venue plans or event results.
- For a new full LP or complete redesign, author the body in free-design HTML/CSS.
  Use native blocks for real calendar, form and map behavior and where their
  composition fits. Do not replace working booking controls with static HTML
  imitations. Preserve partial-edit scope and the user's explicit format choices.
- When an existing LP receives copy-only edits, preserve its current `composition`,
  `presentation`, `imageHeightMode`, and `theme.designPreset` values. Change those
  fields only when the user asks to change the rendering or structure.
- Use `予約する` for an on-page booking CTA to `#booking-section`. Respect explicit
  wording or genuinely different actions. Do not copy flyer wording such as
  `ホームページから予約する` onto the website itself.

## Selective references

Open only the references needed for the current task. In an installed package, use the relative links below. With an MCP-only client, fetch the exact document ID shown for the reference.

- [references/housing-exhibition-premium-canonical.md](references/housing-exhibition-premium-canonical.md) — MCP doc ID: `skill/trustcloud-lp-blueprint/v1/references/housing-exhibition-premium-canonical.md`
- [references/lp-block-catalog-complete.md](references/lp-block-catalog-complete.md) — MCP doc ID: `skill/trustcloud-lp-blueprint/v1/references/lp-block-catalog-complete.md`
- [references/lp-block-catalog.json](references/lp-block-catalog.json) — MCP doc ID: `skill/trustcloud-lp-blueprint/v1/references/lp-block-catalog.json`
- [references/lp-template-structure.md](references/lp-template-structure.md) — MCP doc ID: `skill/trustcloud-lp-blueprint/v1/references/lp-template-structure.md`
- [references/shared-lp-business-quality.md](references/shared-lp-business-quality.md) — MCP doc ID: `skill/trustcloud-lp-blueprint/v1/references/shared-lp-business-quality.md`
