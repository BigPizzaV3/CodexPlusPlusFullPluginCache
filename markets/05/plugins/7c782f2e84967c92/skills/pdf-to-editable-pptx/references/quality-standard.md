# Quality standard

## Contents

- Page routing
- Acceptance gates
- Editability classification
- Required QA report
- Escalation rules

## Page routing

| Page signal | Route | Required verification |
|---|---|---|
| Reliable embedded text and vector geometry | Direct PDF extraction | Text equality plus render diff |
| Full-page raster with absent/unreliable text | OCR and layout extraction | OCR confidence, text check, render diff |
| Reliable text plus raster diagrams/screenshots | Hybrid region route | Direct text check plus image-region comparison |
| Complex table, formula, handwriting, or damaged scan | Specialized parser or vision fallback on crops | Manual review of flagged regions |

Classify per page, not only per document.

## Acceptance gates

All applicable gates must pass:

1. **Structure:** PPTX slide count equals PDF page count; print-PDF page count equals PPTX slide count.
2. **Text:** Normalized extracted text matches exactly for digital pages. OCR pages require no known missing/duplicated content and must list low-confidence regions.
3. **Editability:** Normal content is represented by editable PowerPoint objects. Any retained flattened region is listed by page and reason.
4. **Geometry:** No clipped, overflowing, off-slide, or unintentionally overlapping text. Page size, rotation, and aspect ratio match.
5. **Visual:** Every slide has been rendered and compared with its source page. No unexplained missing image, large displacement, wrong color block, or font-driven reflow remains.
6. **Integrity:** Final PPTX and print PDF reopen successfully and have expected counts.

Do not invent a universal pixel-difference threshold. Antialiasing and renderer differences can create harmless noise. Use image diff to locate anomalies, then inspect the regions.

## Editability classification

Assign one result to each slide:

- `native`: text and major objects are editable; only ordinary photographic/illustrative images remain raster.
- `hybrid`: text is editable, but one or more complex visual regions remain flattened.
- `flattened`: most of the page is one background image; this is not an acceptable final result unless the user explicitly permits it.

The deck-level result is the least editable slide classification. Report counts for all three classes.

## Required QA report

Use this exact structure:

```markdown
# Conversion QA

- Source: ...
- Slides/pages: ...
- Page size/aspect ratio: ...
- Page types: digital ..., scan ..., mixed ...
- Editability: native ..., hybrid ..., flattened ...
- Text verification: ...
- Visual verification: ...
- Print PDF verification: ...

## Exceptions and manual review

| Page | Severity | Issue | What was retained or changed | Recommended action |
|---:|---|---|---|---|

## Fonts and substitutions

| Source font | Output font | Pages | Effect |
|---|---|---|---|

## Non-editable elements

| Page | Element | Reason |
|---:|---|---|
```

If there are no exceptions, explicitly write `None found after rendered comparison`.

## Escalation rules

Escalate only the problematic page or crop:

1. Retry direct extraction or OCR with corrected rotation/crop.
2. Try a specialized document parser for tables, formulas, or reading order.
3. Use a vision model to adjudicate ambiguous content or structure.
4. Request manual review only after deterministic and model-assisted routes disagree or remain uncertain.

Never send a complete confidential document to a remote service unless the user explicitly allows remote processing. When remote processing is allowed, minimize disclosure by sending only required crops and state that choice in QA.
