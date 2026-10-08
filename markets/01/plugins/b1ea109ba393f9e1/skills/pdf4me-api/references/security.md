# Security — Parameter Reference

Parameter reference for every PDF4me **security** endpoint. This file documents only the per-endpoint payload shape — _what_ keys to send and _how_ to fill them. For authentication, base64 encoding, the common response envelope, error codes, see [`auth-and-conventions.md`](auth-and-conventions.md).

All security requests use `POST https://api.pdf4me.com/api/v2/<Action>`.

Docs index: https://docs.pdf4me.com/pdf4me-api/security/

---

## Table of Contents

- [Quick index — pick the right endpoint](#quick-index--pick-the-right-endpoint)
- [Protect](#protect)
- [Unlock](#unlock)

---

## Quick index — pick the right endpoint

| User intent                                                 | Action    |
| ----------------------------------------------------------- | --------- |
| Password-protect or encrypt a PDF                           | `Protect` |
| Set permissions such as print, copy, annotate, or form fill | `Protect` |
| Remove password protection from a PDF                       | `Unlock`  |
| Unlock a password-protected PDF                             | `Unlock`  |

---

## Protect

`POST /api/v2/Protect` — applies password encryption and permission restrictions to a PDF.

**Docs:** https://docs.pdf4me.com/pdf4me-api/security/protect-document.md

> **Key-casing note:** despite some docs labels using title case, the payload keys here are camelCase.

| JSON Key        | Type          | Required | Allowed values / notes                                      |
| --------------- | ------------- | -------- | ----------------------------------------------------------- |
| `docContent`    | base64 string | Yes      | Base64 of the source PDF.                                   |
| `docName`       | string        | Yes      | Source filename with `.pdf` extension, e.g. `document.pdf`. |
| `password`      | string        | Yes      | Password to apply to the protected PDF.                     |
| `pdfPermission` | string        | Yes      | One of the permission values listed below.                  |

**`pdfPermission` values:**

| Value                  | Description                |
| ---------------------- | -------------------------- |
| `All`                  | Grant all permissions.     |
| `None`                 | Deny all permissions.      |
| `Copy`                 | Allow copying content.     |
| `Annotate`             | Allow annotations.         |
| `Fill Forms`           | Allow form filling.        |
| `Support Disabilities` | Allow accessibility tools. |
| `Assemble`             | Allow document assembly.   |
| `Digital Print`        | Allow digital printing.    |

**Example payload:**

```json
{
  "docContent": "Please put PDF base64 content",
  "docName": "output.pdf",
  "password": "1234",
  "pdfPermission": "All"
}
```

---

## Unlock

`POST /api/v2/Unlock` — removes password protection from a PDF.

**Docs:** https://docs.pdf4me.com/pdf4me-api/security/unlock-pdf.md

| JSON Key     | Type          | Required | Allowed values / notes                                      |
| ------------ | ------------- | -------- | ----------------------------------------------------------- |
| `docContent` | base64 string | Yes      | Base64 of the password-protected PDF.                       |
| `docName`    | string        | Yes      | Source filename with `.pdf` extension, e.g. `document.pdf`. |
| `password`   | string        | Yes      | Current password of the protected PDF.                      |

**Example payload:**

```json
{
  "docContent": "Please put PDF base64 content",
  "docName": "output.pdf",
  "password": "1234"
}
```

**Notes:** The docs note that the unlock response contains only `File Content`, not a `File Name` field.

---

## See also

- [`auth-and-conventions.md`](auth-and-conventions.md) — auth, base64 encoding, common response envelope, error codes.
- Docs index: https://docs.pdf4me.com/pdf4me-api/security/
