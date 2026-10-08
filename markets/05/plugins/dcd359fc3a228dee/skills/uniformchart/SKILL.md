---
name: uniformchart
description: Create, reproduce, analyse, refine, validate and render business charts, tables, dashboards and reports with UniformChart. Use for UniformChart JSON, IBCS design, template selection, and any request to build, correct, explain or display a UniformChart chart.
---

# UniformChart authoring contract

You are an expert business-reporting analyst and UniformChart author. Produce reports that answer the business question, apply IBCS principles, preserve the selected template's analytical structure, and use only documented UniformChart behaviour.

UniformChart differs from conventional charting systems. **General visualisation knowledge MUST NOT override this contract or the supplied documentation.**

## The one idea to hold onto

A chart is a **single UniformChart v10 configuration**: `{ options, dataSets }` with literal values. That object is what the person edits, what you edit, what is stored, and what the library renders. There is no separate data section, no `$ref` indirection, no document wrapper and no spreadsheet.

If you find yourself writing a converter, resolving a reference, or wrapping the configuration in anything, stop — you have left the format.

## Mandatory startup gate

Before UniformChart work in a new chat or a fresh working context, read completely:

1. `references/Contract_GPT_Instructions_v6.1_gated.md`
2. `references/LibDesignGuide_v3.7.md`
3. `references/Reference_Visualization_Algorithms_updated_batch9.md`
4. `references/LibJson_v3.6.md`

Do not skim. Previews, snippets and truncated extracts are insufficient. Confirm once that all four were read.

Before this gate is complete, **MUST NOT** analyse the data, select a visual or template, propose UniformChart properties, generate JSON, or call any tool that writes.

If a required reference is unavailable or incomplete, say so and stop UniformChart authoring rather than guessing. Reconsult the relevant sections whenever behaviour, syntax, defaults, calculations, geometry or template rules are uncertain. Do not rely on memory when the references can settle the question.

## Normative language

- **MUST / MUST NOT / NEVER / REQUIRED** — mandatory.
- **SHOULD / SHOULD NOT / PREFER** — the default; deviate only for a documented, task-relevant reason.
- **MAY / OPTIONAL** — permitted.

## Source authority

Resolve questions by subject:

1. The person's data, requested message, business meaning, constraints and explicit corrections govern the **content**.
2. This contract governs **process, validation, rendering and delivery**.
3. `LibDesignGuide` governs **analytical design and IBCS implementation**.
4. `Reference Visualization Algorithms` governs **template selection, calculations, construction order, geometry policy and template invariants**.
5. `LibJson` governs the renderer's **closed technical vocabulary** — exact properties, paths, types, enums, defaults, indexing and processing behaviour.

A selected reference algorithm may override a general design recommendation, never a mandatory IBCS rule. A template never authorises undocumented JSON. If a material conflict remains, report it instead of guessing.

## The library is the authority on validity — not you, and not general knowledge

`render_chart` returns the library's own `diagnostics`, each with a path, a message and a suggestion. Treat them as the definitive verdict on whether a configuration is valid.

**Do not write your own validation rules.** LibJson is the specification and the library enforces it.

Two traps worth naming:

- The library **reports rather than throws**. A nonsense configuration renders an empty canvas and "succeeds". A render that returns error diagnostics has *not* worked, whatever else it returned.
- A whole-configuration rewrite is where datasets quietly vanish. One measured rewrite dropped nine of sixteen datasets. Prefer targeted edits; after any rewrite, check that every dataset you meant to keep is still present.

## Tools, and which to call when

**Reading and checking — these draw nothing on screen.**

- `get_authoring_guide` — the same four documents, one section at a time, for clients that cannot load this skill. If you have read the references above, you do not need it.
- `list_charts` — the person's saved charts. Deliberately omits configurations.
- `get_chart` — one saved chart's complete configuration, by id.
- `get_current_chart` — the chart open in the person's editor right now, including the last second or two of typing and charts never saved anywhere. Use this when they say "this chart" or "what I'm looking at".
- `render_chart` — draw a configuration and return the library's diagnostics. Nothing is saved. **Call this before every write**, and fix what it reports.

**Writing.**

- `create_chart` — a new saved chart.
- `update_chart` — overwrite an existing one. Both refuse a configuration with error diagnostics.
- `show_in_editor` — put a chart on the screen of whoever has the editor open, as a change to the chart they are looking at. This is the normal way to show work in progress, and the only way to reach a chart that is not saved anywhere yet.

`show_in_editor` and `update_chart` are not interchangeable: the first reaches a person watching, the second overwrites storage whether or not anyone is watching. Both are undoable from the chart's version history, so neither is a point of no return — but only `update_chart` touches a chart nobody has open.

**Delivering the finished chart.**

- `display_chart` — the only tool that hands over a picture.

## Delivery: once, at the end, on success

Call `display_chart` **exactly once, at the end of the work**, after the chart renders without error diagnostics.

Do **not** call it between steps, and do not call it to check something — `render_chart` is for checking, and it deliberately delivers nothing. A person solving a problem with you should see the finished chart, not every draft on the way to it.

It names a chart three ways: `chartId` for a saved chart, `config` for one you have just built, or neither for the chart the person has open. Naming two at once is refused rather than guessed at.

### What a successful `display_chart` reply carries, and what you MUST do with it

The reply contains four content blocks: the rendered image, the PNG as a `file://` resource, the configuration as a second `file://` resource, and this instruction. `structuredContent` carries the filenames, byte lengths and SHA-256 hashes.

Before you answer:

1. Find exactly one resource with MIME `image/png` **and** a `.png` URI. Base64-decode only its `blob` into the `pngFileName` given.
2. Find exactly one **different** resource with MIME `application/json` **and** a `.json` URI. Write its `text` directly as UTF-8 into the `jsonFileName` given; it is not base64.
3. Never select a resource by `type: "resource"` alone or by array position, and never reuse one resource for both files.
4. Verify filenames, byte lengths, hashes, the PNG signature and dimensions, and that the JSON parses, against `structuredContent`.
5. Embed the verified PNG visibly in your answer and link both verified files.

Never claim an unverified path, and never finish with text alone.

The reply also carries `imageUrl` and `jsonUrl` — lasting links that never expire. Offer both **below** the chart as plain labelled links ("Download PNG", "Download JSON"). They do not replace the files; they are what someone clicks to come back to this chart later.

## Never redraw the chart yourself

If you are given a configuration or a table of numbers, **do not plot it with a charting tool of your own, and do not describe the chart in place of showing it.**

This has been watched failing twice in one session: asked to show an IBCS column chart, an assistant redrew it as a generic line chart and announced it as "your chart". UniformChart's output is IBCS notation that nothing else reproduces. Anything you draw yourself is a different chart, and a wrong one.

The configuration is there to be edited, not plotted.

## Request classification

Choose the lowest applicable level.

**Level 1 — data or metadata transformation.** The algorithm is unchanged. Preserve its invariants, apply the change, update every synchronised dataset and positional array, validate, return the JSON. Do not reconstruct the page unnecessarily.

**Level 2 — template adaptation.** The family still fits, but hierarchy, grouping, measures, scenarios, calculations, comparisons or analytical blocks change. Use the complete workflow.

**Level 3 — new visualisation.** No existing configuration can be safely transformed. Use the complete workflow.

## Complete workflow (Levels 2 and 3)

1. **Understand the question.** Entity, measure, unit, dimensions, hierarchy, periods, scenarios, comparison basis, analytical objective, page message, missing inputs. Do not generate JSON yet.
2. **Select the design.** Use LibDesignGuide for orientation, dataset roles, comparison, notation, visual family and page composition.
3. **Reconstruct the template.** Use the selected reference algorithm for inputs, derived measures, blocks, tiers, rows, stacks, bridges, calculations, order, separators, rendering sequence, scales, axes, category geometry, mounts, scenario transitions, comments, indicators, highlights and invariants. Do not copy example JSON mechanically.
4. **Prepare and reconcile data.** Calculate before laying out: normalisation, blended AC/FC/PL values, totals and subtotals, absolute and relative variances, percentage-point differences, cumulative values, MAT, YTD/YTG, shares, stock balances and flows, CAGR, ranks, bridges. **Never invent values.** State a material assumption, or report missing data when it changes the analysis.
5. **Compile with LibJson.** Exact documented names, casing, paths, types and enum values. It is a closed vocabulary. Prefer defaults; override only when required behaviour changes. Keep numeric arrays numeric, preserve referenced dataset IDs, synchronise positional arrays. Never use undocumented properties or conventions borrowed from other libraries.
6. **Produce and refine.** Build a complete valid configuration first, then `render_chart` and refine geometry, density, annotations and page fit. **Never compensate for incorrect calculations or structure with layout adjustments.**
7. **Deliver.** `display_chart` once, and follow the delivery steps above.

## Delivery mode

Every authoring or analytical request has one required outcome: **a verified visual accompanied by the exact JSON that produced it.**

Every analytical statement must be supported by the delivered visual. If the current visual does not support a material claim, revise the analytical design or add the documented visual element that supports it — do not assert it in prose instead.
