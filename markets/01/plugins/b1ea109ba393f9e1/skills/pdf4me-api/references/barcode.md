# Barcode — Parameter Reference

Parameter reference for every PDF4me **barcode** endpoint. This file documents only the per-endpoint payload shape — _what_ keys to send and _how_ to fill them. For authentication, base64 encoding, the response envelope, error codes, see [`auth-and-conventions.md`](auth-and-conventions.md).

All endpoints use `POST https://api.pdf4me.com/api/v2/<Action>`.

Docs index: https://docs.pdf4me.com/pdf4me-api/barcode/

---

## Table of Contents

- [Quick index — pick the right endpoint](#quick-index--pick-the-right-endpoint)
- [addbarcode — Add Barcode to PDF](#addbarcode--add-barcode-to-pdf)
- [CreateBarcode](#createbarcode)
- [ReadSwissQRBill — Read SwissQR Code](#readswissqrbill--read-swissqr-code)
- [CreateSwissQRBill](#createswissqrbill)
- [ReadBarcodes — Read Barcode from PDF](#readbarcodes--read-barcode-from-pdf)

---

## Quick index — pick the right endpoint

| User intent                                                         | Action              |
| ------------------------------------------------------------------- | ------------------- |
| Add a barcode or QR code to pages of an existing PDF                | `addbarcode`        |
| Generate a standalone barcode image (PNG) without a source document | `CreateBarcode`     |
| Extract SwissQR payment data from a PDF                             | `ReadSwissQRBill`   |
| Add a Swiss QR payment slip to an existing PDF                      | `CreateSwissQRBill` |
| Detect and read all barcodes embedded in a PDF                      | `ReadBarcodes`      |

---

## addbarcode — Add Barcode to PDF

`POST /api/v2/addbarcode` — overlays a barcode or QR code onto specified pages of an existing PDF, with full control over type, position, size, and appearance.

**Docs:** https://docs.pdf4me.com/pdf4me-api/barcode/add-barcode-to-pdf.md

**Supported inputs:** any PDF.

| JSON Key          | Type          | Required | Allowed values / notes                                                                                     |
| ----------------- | ------------- | -------- | ---------------------------------------------------------------------------------------------------------- |
| `docContent`      | base64 string | Yes      | Base64 of the source PDF.                                                                                  |
| `docName`         | string        | Yes      | Output filename with `.pdf` extension.                                                                     |
| `text`            | string        | Yes      | Data string to encode in the barcode.                                                                      |
| `barcodeType`     | string        | Yes      | `qrCode`, `code128`, `dataMatrix`, `aztec`, `hanxin`, `pdf417`, `code39`, `ean13`, `ean8`, `upcA`, `upcE`. |
| `pages`           | string        | Yes      | Page range — `"all"`, `"1"`, `"1,3,5"`, `"2-5"`, `"1,3,7-10"`, `"2-"`.                                     |
| `alignX`          | string        | Yes      | `Left`, `Center`, `Right`.                                                                                 |
| `alignY`          | string        | Yes      | `Top`, `Middle`, `Bottom`.                                                                                 |
| `hideText`        | boolean       | Yes      | `true` to hide the human-readable text label; `false` to show it.                                          |
| `heightInMM`      | string        | No       | Barcode height in millimetres. Takes precedence over `heightInPt` when both are set.                       |
| `widthInMM`       | string        | No       | Barcode width in millimetres.                                                                              |
| `marginXInMM`     | string        | No       | Horizontal margin from the alignment edge, in millimetres.                                                 |
| `marginYInMM`     | string        | No       | Vertical margin from the alignment edge, in millimetres.                                                   |
| `heightInPt`      | string        | No       | Barcode height in points (1 pt = 1/72 in). Use when working in point units instead of MM.                  |
| `widthInPt`       | string        | No       | Barcode width in points.                                                                                   |
| `marginXInPt`     | string        | No       | Horizontal margin in points.                                                                               |
| `marginYInPt`     | string        | No       | Vertical margin in points.                                                                                 |
| `opacity`         | integer       | No       | Transparency: 0 (fully transparent) – 100 (fully opaque).                                                  |
| `displayText`     | string        | No       | `above` or `below` — position of the text label relative to the barcode when `hideText` is `false`.        |
| `showOnlyInPrint` | boolean       | No       | `true` to embed as a print-only annotation (invisible on screen).                                          |
| `isTextAbove`     | boolean       | No       | `true` places the label above the bars; `false` below. Superseded by `displayText` when both are provided. |

**Example payload:**

```json
{
  "docContent": "JVBERi0xLjQK...",
  "docName": "output.pdf",
  "text": "https://example.com",
  "barcodeType": "qrCode",
  "pages": "all",
  "alignX": "Right",
  "alignY": "Bottom",
  "hideText": true,
  "widthInMM": "30",
  "heightInMM": "30",
  "marginXInMM": "10",
  "marginYInMM": "10",
  "opacity": 100
}
```

**Notes:** Use MM or Pt units, not both — send one pair or the other. Fixed-length barcodes require exact digit counts: `ean13` → 12 digits, `ean8` → 7, `upcA` → 11, `upcE` → 6. For QR codes, `text` can be any URL, plain string, or structured payload (vCard, WiFi config, etc.).

---

## CreateBarcode

`POST /api/v2/CreateBarcode` — generates a standalone barcode or QR code image (PNG) from a text string, with no input document required.

**Docs:** https://docs.pdf4me.com/pdf4me-api/barcode/create-barcode.md

> **Response differs from other endpoints:** sync calls return a raw binary PNG (`Content-Type: image/png`), not a JSON envelope. Save the response body directly as a `.png` file.

| JSON Key      | Type    | Required | Allowed values / notes                                                                         |
| ------------- | ------- | -------- | ---------------------------------------------------------------------------------------------- |
| `text`        | string  | Yes      | Data string to encode.                                                                         |
| `barcodeType` | string  | Yes      | Same set as `addbarcode`: `qrCode`, `code128`, `dataMatrix`, `aztec`, `hanXin`, `pdf417`, etc. |
| `hideText`    | boolean | Yes      | `true` to suppress the human-readable text label.                                              |

**Example payload:**

```json
{
  "text": "https://example.com",
  "barcodeType": "qrCode",
  "hideText": false
}
```

**Notes:** This endpoint has no `docContent` or `docName` — there is no input document.

---

## ReadSwissQRBill — Read SwissQR Code

`POST /api/v2/ReadSwissQRBill` — parses the SwissQR code embedded in a Swiss payment slip PDF and returns the structured payment data as JSON.

**Docs:** https://docs.pdf4me.com/pdf4me-api/barcode/read-swissqr-code.md

**Supported inputs:** any PDF containing a Swiss QR bill payment slip.

| JSON Key     | Type          | Required | Allowed values / notes                   |
| ------------ | ------------- | -------- | ---------------------------------------- |
| `docContent` | base64 string | Yes      | Base64 of the source PDF.                |
| `docName`    | string        | Yes      | Source PDF filename, e.g. `invoice.pdf`. |

**Example payload:**

```json
{
  "docContent": "JVBERi0xLjQK...",
  "docName": "invoice.pdf"
}
```

**Response (sync, 200):**

```json
{
  "fileName": "invoice.pdf",
  "mimeType": "application/pdf",
  "fileSize": 123456,
  "success": true,
  "swissQrCodeData": {
    "amount": "1000.00",
    "currency": "CHF",
    "iban": "CH0200700110003765824",
    "creditorName": "Test AG",
    "paymentReference": "000000000000000000000012345",
    "dueDate": "2025-12-31",
    "purpose": "Invoice payment"
  }
}
```

**Notes:** This endpoint returns data extracted _from_ a PDF rather than producing one, so the response envelope is `swissQrCodeData` — not the usual `docContent`/`docName`. Always check `success: true` before using the nested payment fields.

---

## CreateSwissQRBill

`POST /api/v2/CreateSwissQRBill` — appends a compliant Swiss QR payment slip to an existing PDF and returns the updated document.

**Docs:** https://docs.pdf4me.com/pdf4me-api/barcode/create-swissqr-bill.md

**Supported inputs:** any PDF.

| JSON Key                 | Type          | Required | Allowed values / notes                                                                                             |
| ------------------------ | ------------- | -------- | ------------------------------------------------------------------------------------------------------------------ |
| `docContent`             | base64 string | Yes      | Base64 of the source PDF.                                                                                          |
| `docName`                | string        | Yes      | Output filename with `.pdf` extension.                                                                             |
| `iban`                   | string        | Yes      | Swiss IBAN of the creditor (CH-format), e.g. `CH0200700110003765824`.                                              |
| `crName`                 | string        | Yes      | Creditor name or company.                                                                                          |
| `crAddressType`          | string        | Yes      | `S` (Structured) or `K` (Combined / unstructured).                                                                 |
| `crStreetOrAddressLine1` | string        | Yes      | Street name (Structured) or full address line 1 (Combined).                                                        |
| `crStreetOrAddressLine2` | string        | Yes      | Street number (Structured) or address line 2 (Combined).                                                           |
| `crPostalCode`           | string        | Yes      | Creditor postal code.                                                                                              |
| `crCity`                 | string        | Yes      | Creditor city.                                                                                                     |
| `amount`                 | string        | Yes      | Payment amount as a numeric string, no leading zeros — e.g. `"1000"`.                                              |
| `currency`               | string        | Yes      | `CHF`, `EUR`, or `USD`.                                                                                            |
| `udName`                 | string        | Yes      | Debtor name or company.                                                                                            |
| `udAddressType`          | string        | Yes      | `S` or `K`.                                                                                                        |
| `udStreetOrAddressLine1` | string        | Yes      | Debtor street name or address line 1.                                                                              |
| `udStreetOrAddressLine2` | string        | Yes      | Debtor street number or address line 2.                                                                            |
| `udPostalCode`           | string        | Yes      | Debtor postal code.                                                                                                |
| `udCity`                 | string        | Yes      | Debtor city.                                                                                                       |
| `referenceType`          | string        | Yes      | `QRR` (QR reference, 27-digit), `NON` (no reference), or `SCOR` (ISO 11649 creditor reference).                    |
| `languageType`           | string        | Yes      | `English`, `German`, `French`, or `Italian`.                                                                       |
| `seperatorLine`          | string        | Yes      | `LineWithScissor`, `DashedLineWithScissor`, or `SolidLine`. (Key is `seperatorLine` — the docs use this spelling.) |

**Example payload:**

```json
{
  "docContent": "JVBERi0xLjQK...",
  "docName": "invoice-with-qr.pdf",
  "iban": "CH0200700110003765824",
  "crName": "Test AG",
  "crAddressType": "S",
  "crStreetOrAddressLine1": "Test Strasse",
  "crStreetOrAddressLine2": "1",
  "crPostalCode": "8000",
  "crCity": "Zurich",
  "amount": "1000",
  "currency": "CHF",
  "udName": "Test Debt AG",
  "udAddressType": "S",
  "udStreetOrAddressLine1": "Test Deb Strasse",
  "udStreetOrAddressLine2": "2",
  "udPostalCode": "8000",
  "udCity": "Zurich",
  "referenceType": "NON",
  "languageType": "English",
  "seperatorLine": "LineWithScissor"
}
```

**Notes:** Use key name `seperatorLine` (not `separatorLine`) — this is the documented spelling. `QRR` requires a 27-digit structured reference number; `NON` has no reference field; `SCOR` uses an ISO 11649 creditor reference.

---

## ReadBarcodes — Read Barcode from PDF

`POST /api/v2/ReadBarcodes` — detects and decodes all barcodes found on specified pages of a PDF, returning type, text content, and position for each.

**Docs:** https://docs.pdf4me.com/pdf4me-api/barcode/read-barcode-from-pdf.md

**Supported inputs:** any PDF.

| JSON Key      | Type             | Required | Allowed values / notes                                                              |
| ------------- | ---------------- | -------- | ----------------------------------------------------------------------------------- |
| `docContent`  | base64 string    | Yes      | Base64 of the source PDF.                                                           |
| `docName`     | string           | Yes      | Source PDF filename, e.g. `document.pdf`.                                           |
| `barcodeType` | array of strings | Yes      | `["all"]` to detect every type, or a subset: `["qrCode"]`, `["code128", "qrCode"]`. |
| `pages`       | string           | Yes      | Page range — `"all"`, `"1"`, `"1,3,5"`, `"2-5"`, `"1,3,7-10"`, `"2-"`.              |

**Example payload:**

```json
{
  "docContent": "JVBERi0xLjQK...",
  "docName": "document.pdf",
  "barcodeType": ["all"],
  "pages": "all"
}
```

**Response (sync, 200):**

```json
{
  "barcodes": [
    {
      "type": "qrCode",
      "text": "https://example.com",
      "page": 1,
      "x": 100,
      "y": 200,
      "width": 50,
      "height": 50
    }
  ]
}
```

**Notes:** `barcodeType` is an **array**, not a string — always send `["all"]`, not `"all"`. Coordinates (`x`, `y`, `width`, `height`) are in points measured from the top-left corner of the page.

---

## See also

- [`auth-and-conventions.md`](auth-and-conventions.md) — auth, base64 encoding, response envelope, error codes.
- Docs index: https://docs.pdf4me.com/pdf4me-api/barcode/
