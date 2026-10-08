---
name: ilovepdf-pdf-ocr
description: |
  Extract and make searchable the text in scanned PDFs using OCR (Optical Character Recognition).
  Use this skill whenever the user wants to make a scanned PDF searchable, extract text
  from an image-based PDF, or run OCR on a document.
---

# iLovePDF — OCR PDF

Runs Optical Character Recognition (OCR) on a scanned or image-based PDF, producing
a searchable PDF where the text can be selected, copied, and indexed.

## When to Use

- "Run OCR on this scanned PDF"
- "Make this PDF searchable"
- "Extract text from this scanned document"
- "OCR this PDF in Spanish"
- "Convert this image PDF to a text-selectable PDF"

## Tool to Call

Use the `ilovepdf` or `ilovepdf_attach` MCP tool with `tool: "pdf-ocr"`.

Use `ilovepdf_attach` when the user has attached a file to the chat message.
Use `ilovepdf` when the user provides a file URL.

## Accepted File Types

`.pdf`

## Options

| Option          | Type            | Description                                     | Default      |
| --------------- | --------------- | ----------------------------------------------- | ------------ |
| `ocr_languages` | array of string | Language codes for OCR engine                   | `["eng"]`    |

### Language Codes

Pass `ocr_languages` when the user has stated the document language. Default is English.

Common codes:

| Language   | Code  |
| ---------- | ----- |
| English    | `eng` |
| Spanish    | `spa` |
| French     | `fra` |
| German     | `deu` |
| Italian    | `ita` |
| Portuguese | `por` |
| Chinese (Simplified) | `chi_sim` |
| Chinese (Traditional) | `chi_tra` |
| Japanese   | `jpn` |
| Korean     | `kor` |
| Arabic     | `ara` |
| Russian    | `rus` |

Multiple languages can be combined: `["spa", "eng"]`.

Full list of supported codes: `afr, amh, ara, asm, aze, bel, ben, bod, bos, bul,
cat, ces, chi_sim, chi_tra, dan, deu, ell, eng, epo, est, eus, fas, fil, fin, fra,
gla, gle, glg, guj, heb, hin, hrv, hun, hye, ind, isl, ita, jpn, kan, kat, kaz,
khm, kor, lao, lat, lav, lit, mal, mar, mkd, mlt, mon, msa, mya, nep, nld, nor,
pan, pol, por, ron, rus, sin, slk, slv, spa, sqi, srp, swa, swe, tam, tel, tgl,
tha, tur, ukr, urd, vie, yid`

## Example Calls

```json
// OCR in English (default)
{ "tool": "pdf-ocr", "options": { "ocr_languages": ["eng"] } }

// OCR in Spanish + English
{ "tool": "pdf-ocr", "options": { "ocr_languages": ["spa", "eng"] } }

// OCR in Japanese
{ "tool": "pdf-ocr", "options": { "ocr_languages": ["jpn"] } }
```

## Notes

- The widget handles the upload, processing, and download — do not claim the operation
  is complete before the widget confirms.
- If the user does not mention a language, default to `["eng"]` and let the widget
  provide a language selector as fallback.
- OCR works on scanned/image PDFs. A PDF that already has a text layer may not benefit
  from this operation.
