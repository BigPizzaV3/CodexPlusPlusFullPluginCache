# Math Content Contract

The ingestion boundary should preserve the original source value and emit explicit semantic segments as a separate, reproducible projection. A representative segment shape is:

```json
[
  {"type": "text", "value": "The price is "},
  {"type": "currency", "value": "$84"},
  {"type": "text", "value": " and the constraint is "},
  {"type": "math-inline", "latex": "0 < z < 10"},
  {"type": "math-block", "latex": "x^2+y^2=25"}
]
```

Equivalent repository-native names are acceptable if they preserve the same distinctions and round-trip without loss.

Attach source path, page or item ID, edition or version, source hash, parser version, and projection hash when the repository can support them. `sourceRaw` or an equivalent immutable capture should retain the canonical string used to create the segments. Read [migration-architecture.md](migration-architecture.md) for the full record and rollout path.

## Ingestion rules

- Preserve original text, ordering, meaningful whitespace, figures, tables, and structured prompt blocks.
- Generate typed data from the preserved source; do not make the typed projection the only remaining copy of the source.
- Keep the transformation deterministic. The same source, parser version, and configuration must produce the same semantic projection.
- Prefer `\(...\)` and `\[...\]` when delimiter syntax is needed.
- Treat legacy `$...$` as an input format requiring source-aware classification. Balanced dollar signs do not prove mathematical intent.
- Do not rely on numeric shape to distinguish money from math. `$7,000$`, `$28, 20$`, `$64n$`, and `$0 < z < 10$` demonstrate why.
- Do not use `\$` as the primary boundary between prose currency and math. Escapes can be consumed or rescanned by Markdown, JSON, or auto-render layers.
- Keep an unresolved item explicit when source evidence is insufficient. Include its ID, field, candidate text, source checked, and reason.
- Reject raw TeX commands in prose unless the approved source intentionally presents code.
- Do not silently coerce an unresolved segment during a later build or browser render. Resolution requires source evidence and a regenerated projection.

## Structured content

For `promptBlocks` or an equivalent structure, retain every block, order, display mode, and association with stems, choices, explanations, and figures. Compare source, generated, and rendered block counts. Ensure legacy stem rendering does not omit structured blocks.

## Rendering rules

- Send only `math-inline` and `math-block` values to `katex.render` or `renderToString`.
- Create prose and currency through text-safe rendering.
- Use one shared typed renderer across Course, Lesson, Practice, Review, Full Test, Diagnostic, Placement, and equivalent math-bearing surfaces.
- Do not run an auto-render pass over already classified mixed content.
- In a validation-only gate, parse with `throwOnError: true` or equivalent and record failures by item ID and field. Keep learner-facing error containment separate.
- Count expected math segments and rendered KaTeX roots. Investigate every mismatch.
- Check learner-visible output for raw delimiters, TeX commands, placeholders, and omitted blocks.

Legacy adapters may translate old fields into this contract during migration. Keep the adapter deterministic, fixture-tested, and observable. Record every item still using it, assign an owner, and define a measurable removal condition. Report the affected surface as `PARTIAL` until the inventory reaches zero and the heuristic is removed; only then is that migration eligible for `PASS`.
