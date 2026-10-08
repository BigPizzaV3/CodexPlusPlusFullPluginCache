# PDF4me Platform — Parameter Reference

Parameter reference for the PDF4me **platform** endpoints covered by this skill. This file documents only the per-endpoint payload shape — _what_ keys to send and _how_ to fill them. For authentication, base64 encoding, the common response envelope, error codes, see [`auth-and-conventions.md`](auth-and-conventions.md).

All requests in this file use `POST https://api.pdf4me.com/api/v2/<Action>`.

Docs index: https://docs.pdf4me.com/pdf4me-api/pdf4me/

---

## Table of Contents

- [Quick index — pick the right endpoint](#quick-index--pick-the-right-endpoint)
- [WebhookSubscribe](#webhooksubscribe)
- [UpdateHyperlinkAnnotation](#updatehyperlinkannotation)

---

## Quick index — pick the right endpoint

| User intent                                                              | Action                      |
| ------------------------------------------------------------------------ | --------------------------- |
| Trigger a webhook or Power Automate flow when a PDF4me document is ready | `WebhookSubscribe`          |
| Update hyperlink URLs or display text inside a PDF                       | `UpdateHyperlinkAnnotation` |

---

## WebhookSubscribe

`POST /api/v2/WebhookSubscribe` — registers a callback URL that PDF4me will POST to when a document becomes available.

**Docs:** https://docs.pdf4me.com/pdf4me-api/pdf4me/get-document-from-pdf4me.md

| JSON Key      | Type   | Required | Allowed values / notes                                      |
| ------------- | ------ | -------- | ----------------------------------------------------------- |
| `docName`     | string | Yes      | Document filename, e.g. `output_text` or `document.pdf`.    |
| `CallBackUrl` | string | Yes      | Publicly reachable callback URL that PDF4me should POST to. |

**Example payload:**

```json
{
  "docName": "output.pdf",
  "CallBackUrl": "https://prod-xx.westus.logic.azure.com/workflows/..."
}
```

---

## UpdateHyperlinkAnnotation

`POST /api/v2/UpdateHyperlinkAnnotation` — finds hyperlink annotations in a PDF and replaces their display text and/or destination URLs. Multiple updates can be sent in one request.

**Docs:** https://docs.pdf4me.com/pdf4me-api/pdf4me/update-hyperlinks-annotation.md

| JSON Key                        | Type          | Required | Allowed values / notes                                            |
| ------------------------------- | ------------- | -------- | ----------------------------------------------------------------- |
| `docName`                       | string        | Yes      | PDF filename with `.pdf` extension, e.g. `document.pdf`.          |
| `docContent`                    | base64 string | Yes      | Base64 of the source PDF.                                         |
| `updatehyperlinkannotationlist` | array         | Yes      | One or more hyperlink update objects. Fields are described below. |

**Each item in `updatehyperlinkannotationlist`:**

| Field              | Type    | Required | Notes                                                  |
| ------------------ | ------- | -------- | ------------------------------------------------------ |
| `SearchOn`         | string  | Yes      | How to locate the hyperlink, e.g. `Text`.              |
| `SearchValue`      | string  | Yes      | Value to search for.                                   |
| `IsExpression`     | boolean | Yes      | `true` for regex matching, `false` for exact matching. |
| `TextCurrentValue` | string  | Yes      | Current display text of the hyperlink.                 |
| `TextNewValue`     | string  | Yes      | New display text to apply.                             |
| `URLCurrentValue`  | string  | Yes      | Current URL to replace.                                |
| `URLNewValue`      | string  | Yes      | New URL destination.                                   |

**Example payload:**

```json
{
  "docName": "document.pdf",
  "docContent": "<base64>",
  "updatehyperlinkannotationlist": [
    {
      "SearchOn": "Text",
      "SearchValue": "Example 1",
      "IsExpression": true,
      "TextCurrentValue": "Example 1",
      "TextNewValue": "Example 2",
      "URLCurrentValue": "http://www.google.com/",
      "URLNewValue": "www.pdf4me.com"
    },
    {
      "SearchOn": "Text",
      "SearchValue": "Example 2",
      "IsExpression": true,
      "TextCurrentValue": "Example 2",
      "TextNewValue": "Example 1",
      "URLCurrentValue": "www.pdf4me.com",
      "URLNewValue": "www.google.com"
    }
  ]
}
```

---

## See also

- [`auth-and-conventions.md`](auth-and-conventions.md) — auth, base64 encoding, common response envelope, error codes.
- Docs index: https://docs.pdf4me.com/pdf4me-api/pdf4me/
