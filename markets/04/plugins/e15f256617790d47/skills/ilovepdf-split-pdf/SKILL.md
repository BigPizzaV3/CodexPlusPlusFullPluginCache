---
name: ilovepdf-split-pdf
description: |
  Split a PDF into multiple files by page range, fixed chunk size, or by removing pages.
  Use this skill whenever the user wants to divide, extract pages from, or remove pages
  from a PDF.
---

# iLovePDF — Split PDF

Splits a single PDF into multiple files. Supports splitting by custom page ranges,
fixed chunk sizes, removing specific pages, or splitting by file size.

## When to Use

- "Split this PDF into individual pages"
- "Extract pages 3 to 7 from this PDF"
- "Remove page 5 from this PDF"
- "Split every 2 pages into a separate file"

## Tool to Call

Use the `ilovepdf` or `ilovepdf_attach` MCP tool with `tool: "split-pdf"`.

Use `ilovepdf_attach` when the user has attached a file to the chat message.
Use `ilovepdf` when the user provides a file URL.

## Accepted File Types

`.pdf`

## Options

| Option         | Type    | Values / Format                                   | Default    |
| -------------- | ------- | ------------------------------------------------- | ---------- |
| `split_mode`   | string  | `"fixed_range"`, `"ranges"`, `"remove_pages"`, `"filesize"` | —    |
| `fixed_range`  | number  | Pages per chunk (e.g. `1` for individual pages)   | —          |
| `ranges`       | string  | Page ranges e.g. `"1-3,4-6,7-end"`               | —          |
| `remove_pages` | string  | Pages to remove e.g. `"2,5,8-12"`                | —          |
| `merge_after`  | boolean | Re-merge all ranges into one PDF after split      | `false`    |

### Split Mode Guide

| Mode            | Use When                                                        |
| --------------- | --------------------------------------------------------------- |
| `fixed_range`   | "Split every N pages" — pass `fixed_range: N`                  |
| `ranges`        | "Extract pages X to Y" — pass `ranges: "X-Y"`                  |
| `remove_pages`  | "Remove pages X, Y, Z" — pass `remove_pages: "X,Y,Z"`          |
| `filesize`      | "Split by file size" — collected in-widget                      |

**Keywords:** `"first"` and `"last"` are valid in `ranges` (e.g. `"first-5"`, `"6-last"`).
`"last"` is **not** valid in `fixed_range` or `remove_pages`.

If `split_mode` is not clear from the user's message, pass the tool call without it —
the widget will collect it in-card.

## Example Calls

```json
// Split into individual pages
{ "tool": "split-pdf", "options": { "split_mode": "fixed_range", "fixed_range": 1 } }

// Extract pages 2 to 5
{ "tool": "split-pdf", "options": { "split_mode": "ranges", "ranges": "2-5" } }

// Remove pages 3 and 7
{ "tool": "split-pdf", "options": { "split_mode": "remove_pages", "remove_pages": "3,7" } }
```

## Notes

- The widget handles the upload, processing, and download — do not claim the operation
  is complete before the widget confirms.
- Do not ask the user for split options before calling; the widget provides fallback UI
  for all parameters not supplied.
