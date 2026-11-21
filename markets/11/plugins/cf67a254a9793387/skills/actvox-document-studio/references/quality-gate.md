# Document quality gate

Run this gate before publishing and again after readback.

## Evidence

- Every material fact has an opened source reference or is explicitly marked an
  assumption, contradiction, or gap.
- No search snippet, fabricated URL, or uncited statistic appears as evidence.
- The document separates observed fact from inference and recommendation.

## Structure and rendering

- The title names the subject and desired outcome.
- The opening lets the intended reader understand the decision in under a
  minute.
- The hierarchy is complete, tables have a decision purpose, and any diagram
  has a textual explanation.
- The body is substantive: it contains an actual analysis or plan, not headings
  and placeholders.

## Decision usefulness

- The recommendation or decision request is unambiguous.
- Trade-offs, owners, dates, dependencies, risks, and next actions are concrete
  where applicable.
- Assumptions, contradictions, and evidence gaps are visible and assigned a
  resolution path.

## Persistence and safety

- `research-actvox` discovery confirmed the public capability before writing.
- The operation ID and external ID are caller-owned and stable for retries.
- No share is created unless the user explicitly requested an audience.
- Readback has the same title and content hash (or an explained server-side
  canonicalization), with a real page ID and link.
- Later edits use current ETag/If-Match; divergence stops the update.
