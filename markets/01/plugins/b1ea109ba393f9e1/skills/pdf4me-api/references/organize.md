# Organize — Parameter Reference

Parameter reference for every PDF4me **organize** endpoint. This file documents only the per-endpoint payload shape — _what_ keys to send and _how_ to fill them. For authentication, base64 encoding, the common response envelope, error codes, see [`auth-and-conventions.md`](auth-and-conventions.md).

All organize requests use `POST https://api.pdf4me.com/api/v2/<Action>`.

Docs index: https://docs.pdf4me.com/pdf4me-api/organize/

---

## Table of Contents

- [Quick index — pick the right endpoint](#quick-index--pick-the-right-endpoint)
- [DeleteBlankPages](#deleteblankpages)
- [DeletePages](#deletepages)
- [ExtractPages](#extractpages)
- [RotatePage](#rotatepage)
- [RotateDocument](#rotatedocument)

---

## Quick index — pick the right endpoint

| User intent                                          | Action             |
| ---------------------------------------------------- | ------------------ |
| Remove blank or empty pages from a PDF automatically | `DeleteBlankPages` |
| Delete specific pages by number or range             | `DeletePages`      |
| Extract specific pages into a new PDF                | `ExtractPages`     |
| Rotate specific pages within a PDF                   | `RotatePage`       |
| Rotate all pages in an entire PDF                    | `RotateDocument`   |

---

## DeleteBlankPages

`POST /api/v2/DeleteBlankPages` — removes blank pages from a PDF based on whether pages contain text, images, or both.

**Docs:** https://docs.pdf4me.com/pdf4me-api/organize/delete-blank-pages-from-pdf.md

| JSON Key           | Type          | Required | Allowed values / notes                                      |
| ------------------ | ------------- | -------- | ----------------------------------------------------------- |
| `docContent`       | base64 string | Yes      | Base64 of the source PDF.                                   |
| `docName`          | string        | Yes      | Source filename with `.pdf` extension, e.g. `document.pdf`. |
| `deletePageOption` | string        | Yes      | `NoTextNoImages`, `NoText`, or `NoImages`.                  |

**Example payload:**

```json
{
  "docContent": "Please put PDF base64 content",
  "docName": "output.pdf",
  "deletePageOption": "NoTextNoImages"
}
```

**Notes:** `NoTextNoImages` is the strictest blank-page rule. Use `NoText` if image-only pages should be preserved, and `NoImages` if text-only pages should be preserved.

---

## DeletePages

`POST /api/v2/DeletePages` — deletes one or more pages from a PDF using a page-number string.

**Docs:** https://docs.pdf4me.com/pdf4me-api/organize/delete-pages.md

| JSON Key      | Type          | Required | Allowed values / notes                                                                 |
| ------------- | ------------- | -------- | -------------------------------------------------------------------------------------- |
| `docName`     | string        | Yes      | Source filename with `.pdf` extension, e.g. `document.pdf`.                            |
| `docContent`  | base64 string | Yes      | Base64 of the source PDF.                                                              |
| `pageNumbers` | string        | Yes      | Page selector like `"1,3,5"`, `"1-5,10-15"`, or `"1,3-7,10"`. Page indexes start at 1. |

**Example payload:**

```json
{
  "docName": "document.pdf",
  "docContent": "Please put PDF base64 content",
  "pageNumbers": "1,3,5"
}
```

---

## ExtractPages

`POST /api/v2/ExtractPages` — extracts one or more specific pages into a new PDF.

**Docs:** https://docs.pdf4me.com/pdf4me-api/organize/extract-pages.md

| JSON Key      | Type          | Required | Allowed values / notes                                                                 |
| ------------- | ------------- | -------- | -------------------------------------------------------------------------------------- |
| `docContent`  | base64 string | Yes      | Base64 of the source PDF.                                                              |
| `docName`     | string        | Yes      | Source filename with `.pdf` extension, e.g. `document.pdf`.                            |
| `pageNumbers` | string        | Yes      | Page selector like `"1,3,5"`, `"1-5,10-15"`, or `"1,3-7,10"`. Page indexes start at 1. |

**Example payload:**

```json
{
  "docContent": "Please put PDF base64 content",
  "docName": "document.pdf",
  "pageNumbers": "1,3,5"
}
```

---

## RotatePage

`POST /api/v2/RotatePage` — rotates selected pages inside a PDF while leaving the rest of the document unchanged.

**Docs:** https://docs.pdf4me.com/pdf4me-api/organize/rotate-page.md

| JSON Key       | Type          | Required | Allowed values / notes                                                                 |
| -------------- | ------------- | -------- | -------------------------------------------------------------------------------------- |
| `docContent`   | base64 string | Yes      | Base64 of the source PDF.                                                              |
| `docName`      | string        | Yes      | Source filename with `.pdf` extension, e.g. `document.pdf`.                            |
| `rotationType` | string        | Yes      | `90`, `180`, `270`, or `-90`.                                                          |
| `pages`        | string        | Yes      | Page selector like `"1,3,5"`, `"1-5,10-15"`, or `"1,3-7,10"`. Page indexes start at 1. |

**Example payload:**

```json
{
  "docContent": "Please put PDF base64 content",
  "docName": "document.pdf",
  "rotationType": "90",
  "pages": "1,3,5"
}
```

---

## RotateDocument

`POST /api/v2/RotateDocument` — rotates all pages in a PDF by the same angle.

**Docs:** https://docs.pdf4me.com/pdf4me-api/organize/rotate-document.md

| JSON Key       | Type          | Required | Allowed values / notes                                      |
| -------------- | ------------- | -------- | ----------------------------------------------------------- |
| `docContent`   | base64 string | Yes      | Base64 of the source PDF.                                   |
| `docName`      | string        | Yes      | Source filename with `.pdf` extension, e.g. `document.pdf`. |
| `rotationType` | string        | Yes      | `90`, `180`, `270`, or `-90`.                               |

**Example payload:**

```json
{
  "docContent": "Please put PDF base64 content",
  "docName": "document.pdf",
  "rotationType": "90"
}
```

---

## See also

- [`auth-and-conventions.md`](auth-and-conventions.md) — auth, base64 encoding, common response envelope, error codes.
- Docs index: https://docs.pdf4me.com/pdf4me-api/organize/
