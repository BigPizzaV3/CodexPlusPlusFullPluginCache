# Merge & Split — Parameter Reference

Parameter reference for every PDF4me **merge-split** endpoint. This file documents only the per-endpoint payload shape — _what_ keys to send and _how_ to fill them. For authentication, base64 encoding, the common response envelope, error codes, see [`auth-and-conventions.md`](auth-and-conventions.md).

All merge and split requests use `POST https://api.pdf4me.com/api/v2/<Action>`, though a few split endpoints use non-standard key casing or `_old` in the action path.

Docs index: https://docs.pdf4me.com/pdf4me-api/merge-split/

---

## Table of Contents

- [Quick index — pick the right endpoint](#quick-index--pick-the-right-endpoint)
- [Merge](#merge)
- [MergeOverlay](#mergeoverlay)
- [SplitPDF](#splitpdf)
- [SplitPdfByBarcode](#splitpdfbybarcode)
- [SplitPdfBySwissQR](#splitpdfbyswissqr)
- [SplitByText](#splitbytext)

---

## Quick index — pick the right endpoint

| User intent                                              | Action              |
| -------------------------------------------------------- | ------------------- |
| Merge multiple PDFs into one                             | `Merge`             |
| Overlay one PDF on top of another                        | `MergeOverlay`      |
| Split a PDF by page number, range, or recurring interval | `SplitPDF`          |
| Split a PDF at pages that contain a barcode value        | `SplitPdfByBarcode` |
| Split a PDF at pages that contain a Swiss QR bill code   | `SplitPdfBySwissQR` |
| Split a PDF at pages that contain specific text          | `SplitByText`       |

---

## Merge

`POST /api/v2/Merge` — merges multiple PDFs into one output document.

**Docs:** https://docs.pdf4me.com/pdf4me-api/merge-split/merge.md

| JSON Key     | Type                    | Required | Allowed values / notes                    |
| ------------ | ----------------------- | -------- | ----------------------------------------- |
| `docContent` | array of base64 strings | Yes      | Base64-encoded PDF inputs in merge order. |
| `docName`    | string                  | Yes      | Output filename, e.g. `output.pdf`.       |

**Example payload:**

```json
{
  "docContent": [
    "Please put First PDF base64 content",
    "Please put Second PDF base64 content"
  ],
  "docName": "output.pdf"
}
```

---

## MergeOverlay

`POST /api/v2/MergeOverlay` — overlays one PDF on top of another, using one as the base layer and one as the top layer.

**Docs:** https://docs.pdf4me.com/pdf4me-api/merge-split/merge-overlay.md

| JSON Key          | Type          | Required | Allowed values / notes                    |
| ----------------- | ------------- | -------- | ----------------------------------------- |
| `baseDocContent`  | base64 string | Yes      | Base64 of the base PDF.                   |
| `baseDocName`     | string        | Yes      | Base PDF filename, e.g. `base.pdf`.       |
| `layerDocContent` | base64 string | Yes      | Base64 of the overlay PDF.                |
| `layerDocName`    | string        | Yes      | Overlay PDF filename, e.g. `overlay.pdf`. |

**Example payload:**

```json
{
  "baseDocContent": "Please put First PDF base64 content",
  "baseDocName": "output.pdf",
  "layerDocContent": "Please put Second PDF base64 content",
  "layerDocName": "output.pdf"
}
```

---

## SplitPDF

`POST /api/v2/SplitPDF` — splits a PDF by a recurring page interval, a single break page, a split sequence, or explicit page ranges.

**Docs:** https://docs.pdf4me.com/pdf4me-api/merge-split/split-pdf.md

| JSON Key            | Type             | Required    | Allowed values / notes                                                          |
| ------------------- | ---------------- | ----------- | ------------------------------------------------------------------------------- |
| `docContent`        | base64 string    | Yes         | Base64 of the source PDF.                                                       |
| `docName`           | string           | Yes         | Source filename, e.g. `document.pdf`.                                           |
| `splitAction`       | string           | Yes         | `RecurringSplitAfterPage`, `SplitAfterPage`, `SplitSequence`, or `SplitRanges`. |
| `fileNaming`        | string           | Yes         | Output naming strategy, e.g. `NameAsPerOrder`.                                  |
| `splitActionNumber` | number           | Conditional | Used with `RecurringSplitAfterPage` and `SplitAfterPage`.                       |
| `splitSequence`     | array of numbers | Conditional | Used with `SplitSequence`, e.g. `[1, 3, 8]`.                                    |
| `splitRanges`       | string           | Conditional | Used with `SplitRanges`, e.g. `1-4` or `10-21`.                                 |

**`splitAction` behavior:**

| Value                     | Behavior                                              |
| ------------------------- | ----------------------------------------------------- |
| `RecurringSplitAfterPage` | Split every `N` pages using `splitActionNumber`.      |
| `SplitAfterPage`          | Split once after page `N` using `splitActionNumber`.  |
| `SplitSequence`           | Split at specific page numbers using `splitSequence`. |
| `SplitRanges`             | Extract one or more page ranges using `splitRanges`.  |

**Example payload:**

```json
{
  "docContent": "Please put PDF base64 content",
  "docName": "output.pdf",
  "splitAction": "RecurringSplitAfterPage",
  "splitActionNumber": 1,
  "fileNaming": "NameAsPerOrder"
}
```

**Notes:** The split response uses the API’s documented spelling `splited Documents`.

---

## SplitPdfByBarcode

`POST /api/v2/SplitPdfByBarcode_old` — splits a PDF at pages where a specified barcode value is found.

**Docs:** https://docs.pdf4me.com/pdf4me-api/merge-split/split-by-barcode.md

> **Path note:** the `_old` suffix in the action path is part of the documented endpoint name.

| JSON Key                                       | Type          | Required | Allowed values / notes                                  |
| ---------------------------------------------- | ------------- | -------- | ------------------------------------------------------- |
| `DocContent`                                   | base64 string | Yes      | Base64 of the source PDF.                               |
| `DocName`                                      | string        | Yes      | Source filename, e.g. `document.pdf`.                   |
| `Barcode String`                               | string        | Yes      | Barcode text or pattern to search for.                  |
| `Barcode Filter`                               | string        | Yes      | `Contains`, `Equals`, `StartsWith`, or `EndsWith`.      |
| `Barcode Type`                                 | string        | Yes      | Barcode format such as `Code128`, `QRCode`, or `EAN13`. |
| `Split Barcode Page`                           | string        | Yes      | `Before` or `After`.                                    |
| `Combine Pages With Same Consecutive Barcodes` | boolean       | Yes      | `true` to group consecutive identical barcodes.         |
| `Pdf Render Dpi`                               | string        | Yes      | Render DPI for recognition, e.g. `300`.                 |

**Example payload:**

```json
{
  "DocName": "document.pdf",
  "DocContent": "Please put PDF base64 content",
  "Barcode String": "barcode_text",
  "Barcode Filter": "Contains",
  "Barcode Type": "Code128",
  "Split Barcode Page": "After",
  "Combine Pages With Same Consecutive Barcodes": true,
  "Pdf Render Dpi": "300"
}
```

---

## SplitPdfBySwissQR

`POST /api/v2/SplitPdfByBarcode` — splits a PDF at pages that contain a Swiss QR bill.

**Docs:** https://docs.pdf4me.com/pdf4me-api/merge-split/split-pdf-by-swiss-qr.md

> **Path note:** despite the different behavior, this endpoint uses the `SplitPdfByBarcode` path without the `_old` suffix.

| JSON Key                           | Type          | Required | Allowed values / notes                                     |
| ---------------------------------- | ------------- | -------- | ---------------------------------------------------------- |
| `File Content`                     | base64 string | Yes      | Base64 of the source PDF.                                  |
| `File Name`                        | string        | Yes      | Source filename, e.g. `document.pdf`.                      |
| `Split QR Page`                    | string        | Yes      | `After` or `Before`.                                       |
| `PDF Render DPI`                   | string        | Yes      | `100`, `150`, `200`, or `250`.                             |
| `Combine Pages With Same Barcodes` | boolean       | Yes      | `true` to merge consecutive pages with identical QR codes. |
| `Return as Zip`                    | boolean       | Yes      | `true` to return all split files in a ZIP archive.         |

**Example payload:**

```json
{
  "File Content": "Please put PDF base64 content",
  "File Name": "document.pdf",
  "Split QR Page": "After",
  "PDF Render DPI": "200",
  "Combine Pages With Same Barcodes": false,
  "Return as Zip": false
}
```

---

## SplitByText

`POST /api/v2/SplitByText` — splits a PDF when matching text is found on a page.

**Docs:** https://docs.pdf4me.com/pdf4me-api/merge-split/split-pdf-by-text.md

| JSON Key        | Type          | Required | Allowed values / notes                             |
| --------------- | ------------- | -------- | -------------------------------------------------- |
| `docContent`    | base64 string | Yes      | Base64 of the source PDF.                          |
| `docName`       | string        | Yes      | Source filename, e.g. `document.pdf`.              |
| `text`          | string        | Yes      | Text string or pattern to search for on each page. |
| `splitTextPage` | string        | Yes      | `before` or `after`.                               |
| `fileNaming`    | string        | Yes      | Output naming strategy, e.g. `NameAsPerOrder`.     |

**Example payload:**

```json
{
  "docContent": "Please put PDF base64 content",
  "docName": "output.pdf",
  "text": "Chapter 1",
  "splitTextPage": "before",
  "fileNaming": "NameAsPerOrder"
}
```

---

## See also

- [`auth-and-conventions.md`](auth-and-conventions.md) — auth, base64 encoding, common response envelope, error codes.
- Docs index: https://docs.pdf4me.com/pdf4me-api/merge-split/
