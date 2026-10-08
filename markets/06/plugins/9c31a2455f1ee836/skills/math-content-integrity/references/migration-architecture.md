# Structured Ingestion Architecture

Use this reference when designing or reviewing the durable replacement for legacy dollar-sign inference.

## Root cause and target path

The defect class starts when one flat string uses `$` for both visible currency and math delimiters. Markdown, JSON generation, auto-rendering, or packaging can consume escapes or reinterpret the same string differently. KaTeX then receives the wrong input; it is usually the last visible stage, not the owning cause.

Fix the path, not only the screen:

```text
approved PDF or book source
  -> preserved canonical capture and provenance
  -> source-aware ingestion parser
  -> typed, reproducible derived projection
  -> shared renderer
  -> verified production artifact
  -> authenticated learner screen
```

The approved source remains unchanged and auditable. The typed projection is rebuilt from it and may be replaced at any time by running its declared generator.

## Derived record

Use repository-native names, but preserve the following meaning:

```json
{
  "source": {
    "path": "approved-book.pdf",
    "page": 42,
    "itemId": "math-l2-042",
    "version": "approved-edition-v3",
    "sha256": "..."
  },
  "sourceRaw": "The price is $5 and the constraint is $x+2$.",
  "segments": [
    {"type": "text", "value": "The price is "},
    {"type": "currency", "value": "$5"},
    {"type": "text", "value": " and the constraint is "},
    {"type": "math-inline", "latex": "x+2"},
    {"type": "text", "value": "."}
  ],
  "parserVersion": "...",
  "projectionHash": "..."
}
```

Retain figures, tables, display mode, order, field association, and other structured blocks alongside these segments. Do not force them into prose.

## Classification boundary

Resolve meaning at ingestion from the approved source, authored metadata, item structure, and surrounding context. Regex and numeric shape may identify candidates but cannot decide authority. A balanced `$5$` can be math or a price; `$7,000$` can be a mathematical number; and escaped dollars may be consumed by another layer.

Emit `unresolved` when evidence is insufficient. Do not let an unresolved segment silently fall back to currency or math in production.

## Migration sequence

1. Keep the current shared legacy adapter and release gates stable while current content is clean.
2. Inventory every record and route still using flat-string inference. Record item ID, field, parser result, source reference, and owning generator.
3. Add typed output to the owning ingestion or generation step without mutating the canonical source.
4. Compare the typed projection with the source and the previous learner-visible result. Record legitimate changes and false positives as fixtures.
5. Move each screen to the shared typed renderer. Avoid a second auto-render pass over mixed content.
6. Remove the legacy adapter only when its inventory is zero and source, generated data, artifact, desktop, mobile, and authenticated checks pass.

Until the final condition is met, describe the system accurately: current rendering may be correct and release-protected while the structural migration remains incomplete.

## Why the skill remains necessary

Typed data removes runtime guessing; it does not prove the projection is correct. Continue verifying that ingestion classified currency and math correctly, the projection matches the approved source, generators are reproducible, KaTeX accepts every typed expression, packaging preserves the verified bytes or semantics, and learner screens contain no raw math syntax.
