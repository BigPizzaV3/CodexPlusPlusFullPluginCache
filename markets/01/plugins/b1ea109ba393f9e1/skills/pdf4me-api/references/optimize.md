# Optimize — Parameter Reference

Parameter reference for the PDF4me **optimize** endpoint. This file documents the payload shape — _what_ keys to send and _how_ to fill them. For authentication, base64 encoding, the common response envelope, error codes, see [`auth-and-conventions.md`](auth-and-conventions.md).

All optimize requests use `POST https://api.pdf4me.com/api/v2/<Action>`.

Docs index: https://docs.pdf4me.com/pdf4me-api/optimize/

---

## Table of Contents

- [Quick index — pick the right endpoint](#quick-index--pick-the-right-endpoint)
- [Optimize](#optimize)

---

## Quick index — pick the right endpoint

| User intent                               | Action                                                      |
| ----------------------------------------- | ----------------------------------------------------------- |
| Compress or reduce the file size of a PDF | `Optimize`                                                  |
| Optimize a PDF for web delivery           | `Optimize` with `optimizeProfile: "Web"`                    |
| Optimize a PDF for printing               | `Optimize` with `optimizeProfile: "Print"`                  |
| Maximum compression of a PDF              | `Optimize` with `optimizeProfile: "Max"` or `"CompressMax"` |

---

## Optimize

`POST /api/v2/Optimize` — compresses a PDF using a selectable optimization profile tuned for general use, web delivery, printing, or maximum size reduction.

**Docs:** https://docs.pdf4me.com/pdf4me-api/optimize/compress-pdf.md

| JSON Key          | Type          | Required | Allowed values / notes                                                                    |
| ----------------- | ------------- | -------- | ----------------------------------------------------------------------------------------- |
| `docContent`      | base64 string | Yes      | Base64 of the source PDF. Docs note a 100 MB max and recommend keeping files under 50 MB. |
| `docName`         | string        | Yes      | Source filename with `.pdf` extension, e.g. `document.pdf`.                               |
| `optimizeProfile` | string        | Yes      | One of the profile values listed below.                                                   |

**Optimize profile values:**

| Value         | Description                                           |
| ------------- | ----------------------------------------------------- |
| `Default`     | Balanced compression for general use.                 |
| `Web`         | Small file size and fast download for online viewing. |
| `WebMax`      | Maximum web optimization.                             |
| `Print`       | Print-oriented output with correct fonts and colors.  |
| `PrintMax`    | Maximum print optimization.                           |
| `PrintGray`   | Grayscale print optimization.                         |
| `Max`         | Maximum file size reduction.                          |
| `Compress`    | Standard compression.                                 |
| `CompressMax` | Maximum compression.                                  |

**Example payload:**

```json
{
  "docContent": "Please put PDF base64 content",
  "docName": "output.pdf",
  "optimizeProfile": "Web"
}
```

**Notes:** `Web` is a safe default for browser delivery. Use `Print` or `PrintMax` when output fidelity matters more than file size, and `Max` or `CompressMax` when storage reduction is the priority.

---

## See also

- [`auth-and-conventions.md`](auth-and-conventions.md) — auth, base64 encoding, common response envelope, error codes.
- Docs index: https://docs.pdf4me.com/pdf4me-api/optimize/
