---
name: tables-figures-and-supplements
description: Extract research data from tables, figures, charts, appendices, and supplementary files while preserving labels, units, notes, and source locations. Use for visual or structured research evidence.
---

# Tables, figures, and supplements

Inspect the actual supplied page/image/document. If an element is too small, cropped, low-resolution, or inaccessible, say exactly what cannot be read and request a clearer copy. Never claim to have inspected hidden pages or unsupported file contents.

## Tables

1. Record table number/title and source page/section.
2. Preserve column headers, row labels, units, group names, denominators, symbols, superscripts, and footnote markers.
3. Extract footnotes separately and connect each marker to its note.
4. Keep groups, timepoints, outcome types, and adjusted/unadjusted analyses separate.
5. Distinguish mean/median, SD/SE, IQR/range, N/event counts/percentages.
6. Check arithmetic consistency without rewriting the printed values. Flag mismatched totals, denominators, or sample sizes.
7. Do not derive missing counts/statistics unless requested and valid inputs are given.

## Figures and charts

Read caption first; identify axes, labels, units, groups, symbols, scale, and error-bar definition. Preserve figure number and cite the caption/legend/page. Extract exact values only when explicitly labeled or legible. Never reverse-engineer exact numbers from bar/line position on an unlabeled plot. If the user explicitly requests approximate visual estimation, label every estimate `APPROXIMATE_VISUAL_ESTIMATE`, state the basis and image-resolution limits, and do not present it as author-reported data.

## Supplements and appendices

Record file/appendix identifier and pagination when available. Keep supplement-derived fields traceable and distinguish them from main-text results. If multiple versions or files disagree, report both locations and values.

## Output

Prefer tidy rows with: source element, row/column or figure element, group, value, unit, note/denominator, location, confidence. Include `UNCLEAR` when labels or value mapping are ambiguous; do not guess the intended row/column.
