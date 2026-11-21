# HTML documents and printing

Use these helpers from the originally selected project, after `task-dir`. They run locally with Node.js 18+; no model calls, document service, project upload or new network account is needed. The print check uses an installed Edge/Chrome in an isolated temporary profile. The existing artifact workflow still owns folder validation, upload and submission.

## Choose and write

- `document`: reports, plans, research, minutes and other continuous prose; A4 portrait, 18 mm page margins.
- `presentation`: slide-based reports or persuasive presentations; A4 landscape, 10 mm page margins, one section per slide. Use subsequent slides for overflow; never remove evidence, hide overflow or shrink text until unreadable. A4 landscape is not 16:9. If the user explicitly requires another ratio or a native Office source, honor that request and verify that output separately.
- Preserve the original tables/columns and meaningful sections. The template does not dictate a business outline or fixed slide count.
- Put the UTF-8 input JSON in `support_dir`. Text is literal, not Markdown or raw HTML. Encode emphasis through headings and structure. Use real Unicode text; do not supply literal backslash-n sequences in prose.

```json
{
  "layout": "document",
  "title": "실행계획",
  "subtitle": "검토용",
  "language": "ko",
  "sections": [
    {
      "heading": "실행 과제",
      "blocks": [
        { "type": "paragraph", "text": "확인된 사실과 미확인 사항을 구분합니다." },
        {
          "type": "table",
          "columns": ["과제", "완료 기준"],
          "rows": [["고객 조사", "출처와 조사 결과 확인"]]
        }
      ]
    }
  ]
}
```

Both layouts accept `sections: [{heading, blocks}]`; every slide needs a heading. `subtitle` is for the document layout. Supported blocks:

| Type                 | Fields                                                                                                     |
| -------------------- | ---------------------------------------------------------------------------------------------------------- |
| `paragraph`, `quote` | `text`                                                                                                     |
| `heading`            | `text`, `level: 2 or 3`                                                                                    |
| `list`               | `items: string[]`, optional `ordered: true`                                                                |
| `table`              | `columns: string[]`, `rows: string[][]`, optional `caption`; keep exactly the same number of cells per row |
| `image`              | `src`: embedded PNG/JPEG/WebP/GIF data URL, `alt`, optional `caption`                                      |
| `links`              | `items: [{label, url}]`; HTTP(S) source URLs without credentials                                           |

Pre-render charts/diagrams as images when needed and retain their data/source evidence. Compress images before embedding; each uploaded artifact must remain within 8 MiB. Do not add remote scripts, styles, images or font dependencies. The template supplies a trusted print button and a restrictive content policy.

## Build, check, inspect

Use the exact relative paths returned by `task-dir`, replacing the placeholders below. Direct build/inspection files into `support_dir` and final user deliverables into `relative_dir`.

```text
node "<plugin-root>/scripts/document.mjs" build --input "<support_dir>/document.json" --output "<relative_dir>/실행계획.html"
node "<plugin-root>/scripts/document.mjs" check --file "<relative_dir>/실행계획.html" --pdf "<relative_dir>/실행계획.pdf" --evidence "<support_dir>/print-check.json"
```

The PDF option is optional. Without it the helper still prints to a temporary PDF to verify A4 page geometry. To inspect a PDF that is not a deliverable, use `--pdf "<support_dir>/print-preview.pdf"`. If browser discovery fails, pass `--browser "<installed browser executable>"` or set `DXIR_PRINT_BROWSER`; do not install software or pretend the check passed.

The check detects broken images, horizontal overflow, slides exceeding their content area, table rows taller than a portrait page, incorrect PDF dimensions and slide/page-count mismatches. It returns the exact HTML SHA-256 and page count. It does not prove content correctness or visual quality: render the PDF pages with available PDF tools and inspect for clipped text, oversized table rows, stray blank pages, Korean glyphs, image quality and readable spacing. If no visual tool is available, disclose the remaining visual check.

Build/check never overwrite an existing target. During drafting use new revision filenames and support receipts; do not delete/rewrite reserved deliverables to make a rerun pass. Recheck after any HTML edit because prior validation is tied to its SHA-256. Do not register the document until its intended required checks are satisfied, or explicitly report the unmet requirement as allowed by the Room's contract.

## Submit

Use MIME `text/html` (without a charset parameter) for the HTML and `application/pdf` for a PDF. UTF-8 is declared inside the HTML. Reserve and upload each intended deliverable using the existing checkpoint/prepare/upload/complete flow, then submit verified artifact IDs. Do not upload drafts or inspection sidecars as customer deliverables.

Keep original MD files and reservations intact. If converting an existing result, preserve its full content, create a new HTML version and use new artifact IDs. A reporting retry must reuse its exact previously reserved bytes and payload; it must not recreate a document merely to recover synchronization.
